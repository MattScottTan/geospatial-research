from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

STAGE_ROOT = Path(__file__).resolve().parents[1]
OUT_T = STAGE_ROOT / 'outputs' / 'tables'
OUT_F = STAGE_ROOT / 'outputs' / 'figures'
DOCS = STAGE_ROOT / 'docs'
CACHE = STAGE_ROOT / 'cache' / 'openalex'
INPUT = STAGE_ROOT / 'city_url_map.csv'
TOPIC_FILTER = 'T10181|T12254|T10320'
START_YEAR = 2000
END_YEAR = 2025


def ensure_dirs() -> None:
    for p in [OUT_T, OUT_F, DOCS, CACHE]:
        p.mkdir(parents=True, exist_ok=True)


def fetch_grouped_counts(institution_ids: str, slug: str, force_refresh: bool = False, pause_s: float = 0.2) -> Dict[int, int]:
    cache_path = CACHE / f'{slug}.json'
    if cache_path.exists() and not force_refresh:
        payload = json.loads(cache_path.read_text())
    else:
        params = {
            'filter': f'institutions.id:{institution_ids},topics.id:{TOPIC_FILTER},from_publication_date:{START_YEAR}-01-01',
            'group_by': 'publication_year',
            'per-page': 200,
        }
        url = 'https://api.openalex.org/works?' + urlencode(params)
        req = Request(url, headers={'User-Agent': 'AI-Compute-Accessibility-Atlas/1.0 (local replication)'})
        with urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode('utf-8'))
        cache_path.write_text(json.dumps(payload, indent=2))
        time.sleep(pause_s)
    return {int(item['key']): int(item['count']) for item in payload.get('group_by', []) if item.get('key') is not None}


def build_panel(force_refresh: bool = False) -> pd.DataFrame:
    spec = pd.read_csv(INPUT)
    years = list(range(START_YEAR, END_YEAR + 1))
    rows: List[dict] = []
    for rec in spec.to_dict(orient='records'):
        counts = fetch_grouped_counts(str(rec['ids']), str(rec['slug']), force_refresh=force_refresh)
        treated = int(rec['treated_city'])
        event_year = None if pd.isna(rec['event_year']) else int(rec['event_year'])
        for year in years:
            rel_year = None if event_year is None else year - event_year
            post_full = int(treated == 1 and event_year is not None and year >= event_year + 1)
            rows.append(
                {
                    'slug': rec['slug'],
                    'city': rec['city'],
                    'country': rec['country'],
                    'cohort_label': rec['cohort_label'],
                    'treated_city': treated,
                    'event_year': event_year,
                    'year': year,
                    'ai_works_city_topinst': counts.get(year, 0),
                    'post_full': post_full,
                    'rel_year': rel_year,
                    'n_inst': int(rec['n_inst']),
                    'institution_ids': rec['ids'],
                }
            )
    df = pd.DataFrame(rows)
    df['log1p_ai'] = np.log1p(df['ai_works_city_topinst'])
    df['year_c'] = df['year'] - df['year'].min()
    return df


def fit_twfe(df: pd.DataFrame) -> pd.DataFrame:
    models = []
    m1 = smf.ols('log1p_ai ~ post_full + C(slug) + C(year)', data=df).fit(cov_type='cluster', cov_kwds={'groups': df['slug']})
    models.append(('TWFE baseline', m1))
    m2 = smf.ols('log1p_ai ~ post_full + C(slug) + C(year) + C(slug):year_c', data=df).fit(cov_type='cluster', cov_kwds={'groups': df['slug']})
    models.append(('TWFE + city trends', m2))
    m3 = smf.ols('log1p_ai ~ post_full + C(slug) + C(country):C(year)', data=df).fit(cov_type='cluster', cov_kwds={'groups': df['slug']})
    models.append(('City FE + country-year FE', m3))
    rows = []
    for name, mod in models:
        coef = float(mod.params.get('post_full', np.nan))
        se = float(mod.bse.get('post_full', np.nan))
        rows.append(
            {
                'model': name,
                'n_obs': int(mod.nobs),
                'coef_post_full': coef,
                'se_post_full': se,
                'p_post_full': float(mod.pvalues.get('post_full', np.nan)),
                'ci_low': coef - 1.96 * se,
                'ci_high': coef + 1.96 * se,
                'r2': float(mod.rsquared),
            }
        )
    return pd.DataFrame(rows)


def fit_cohort_did(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    cohort_years = sorted(int(y) for y in df.loc[df['treated_city'] == 1, 'event_year'].dropna().unique())
    for event_year in cohort_years:
        treated = df[df['event_year'] == event_year].copy()
        countries = sorted(treated['country'].unique())
        controls = df[(df['treated_city'] == 0) & (df['country'].isin(countries))].copy()
        cohort_df = pd.concat([treated, controls], ignore_index=True)
        cohort_df = cohort_df[(cohort_df['year'] >= event_year - 5) & (cohort_df['year'] <= event_year + 3)].copy()
        if cohort_df.empty:
            continue
        cohort_df['post_full_g'] = ((cohort_df['treated_city'] == 1) & (cohort_df['year'] >= event_year + 1)).astype(int)
        mod = smf.ols('log1p_ai ~ post_full_g + C(slug) + C(year)', data=cohort_df).fit(cov_type='cluster', cov_kwds={'groups': cohort_df['slug']})
        coef = float(mod.params.get('post_full_g', np.nan))
        se = float(mod.bse.get('post_full_g', np.nan))
        rows.append(
            {
                'event_year': event_year,
                'n_treated_cities': int(treated['slug'].nunique()),
                'coef_post': coef,
                'se_post': se,
                'p_post': float(mod.pvalues.get('post_full_g', np.nan)),
                'ci_low': coef - 1.96 * se,
                'ci_high': coef + 1.96 * se,
            }
        )
    return pd.DataFrame(rows)


def fit_stacked_did(df: pd.DataFrame) -> pd.DataFrame:
    stacks = []
    cohort_years = sorted(int(y) for y in df.loc[df['treated_city'] == 1, 'event_year'].dropna().unique())
    for event_year in cohort_years:
        treated = df[df['event_year'] == event_year].copy()
        countries = sorted(treated['country'].unique())
        controls = df[(df['treated_city'] == 0) & (df['country'].isin(countries))].copy()
        part = pd.concat([treated, controls], ignore_index=True)
        part = part[(part['year'] >= event_year - 5) & (part['year'] <= event_year + 3)].copy()
        if part.empty:
            continue
        part['stack_id'] = str(event_year)
        part['rel_window_year'] = part['year'] - event_year
        part['post_g'] = ((part['treated_city'] == 1) & (part['year'] >= event_year + 1)).astype(int)
        part['stack_slug'] = part['stack_id'] + '::' + part['slug']
        stacks.append(part)
    if not stacks:
        return pd.DataFrame(
            [
                {
                    'model': 'Stacked DID [-5,+3]',
                    'n_obs': 0,
                    'coef_post_g': np.nan,
                    'se_post_g': np.nan,
                    'p_post_g': np.nan,
                    'ci_low': np.nan,
                    'ci_high': np.nan,
                }
            ]
        )
    sdf = pd.concat(stacks, ignore_index=True)
    mod = smf.ols('log1p_ai ~ post_g + C(stack_slug) + C(stack_id):C(rel_window_year)', data=sdf).fit(cov_type='cluster', cov_kwds={'groups': sdf['stack_slug']})
    coef = float(mod.params.get('post_g', np.nan))
    se = float(mod.bse.get('post_g', np.nan))
    return pd.DataFrame(
        [
            {
                'model': 'Stacked DID [-5,+3]',
                'n_obs': int(mod.nobs),
                'coef_post_g': coef,
                'se_post_g': se,
                'p_post_g': float(mod.pvalues.get('post_g', np.nan)),
                'ci_low': coef - 1.96 * se,
                'ci_high': coef + 1.96 * se,
            }
        ]
    )


def make_raw_trends(df: pd.DataFrame, path: Path) -> None:
    avg = df.groupby(['year', 'treated_city'], as_index=False)['ai_works_city_topinst'].mean()
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for treated, label in [(1, 'Eventually treated cities'), (0, 'Never-treated controls')]:
        tmp = avg[avg['treated_city'] == treated]
        ax.plot(tmp['year'], tmp['ai_works_city_topinst'], marker='o', label=label)
    ax.set_xlabel('Year')
    ax.set_ylabel('Average AI works')
    ax.set_title('Stage 6 raw trends (live rebuild)')
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=220, bbox_inches='tight')
    plt.close(fig)


def write_summary(df: pd.DataFrame, twfe: pd.DataFrame, cohort: pd.DataFrame, stacked: pd.DataFrame, force_refresh: bool) -> None:
    lines = [
        '# Stage 6 expanded panel: broader city-year causal test (live rebuild)',
        '',
        '## What this script does',
        '- Rebuilds the selected-city panel from live OpenAlex group-by-year pulls using the institution IDs stored in `city_url_map.csv`.',
        '- Recomputes the staggered-adoption summaries that were used in the Stage 6 memo.',
        '- Writes cache files under `extensions/stage6/cache/openalex/` so subsequent reruns are faster and deterministic against the cached snapshot.',
        '',
        f'- Force refresh used: {force_refresh}',
        f'- Cities: {df["slug"].nunique()}',
        f'- Treated cities: {df.loc[df["treated_city"] == 1, "slug"].nunique()}',
        f'- Never-treated controls: {df.loc[df["treated_city"] == 0, "slug"].nunique()}',
        f'- Years: {df["year"].min()}-{df["year"].max()}',
        '',
        '## TWFE summaries',
        twfe.to_markdown(index=False),
        '',
        '## Cohort-by-cohort DID',
        cohort.to_markdown(index=False),
        '',
        '## Stacked DID',
        stacked.to_markdown(index=False),
        '',
        '## Interpretation',
        '- Live rebuilds can drift from the frozen Stage 6 tables because OpenAlex is continuously updated.',
        '- The causal read still depends on the same selected-city design, AWS-only treatment timing, and top-institution subset outcome.',
        '- Treat this as a reproducible support script for the preserved Stage 6 artifacts, not as stronger causal evidence than the main atlas.',
        '',
    ]
    (DOCS / 'stage6_live_rebuild_summary.md').write_text('\n'.join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--force-refresh', action='store_true', help='Ignore cached OpenAlex responses and fetch live data again.')
    args = parser.parse_args()

    ensure_dirs()
    df = build_panel(force_refresh=args.force_refresh)
    twfe = fit_twfe(df)
    cohort = fit_cohort_did(df)
    stacked = fit_stacked_did(df)

    df.to_csv(OUT_T / 'stage6_city_year_panel_live.csv', index=False)
    twfe.to_csv(OUT_T / 'stage6_twfe_summary_live.csv', index=False)
    cohort.to_csv(OUT_T / 'stage6_cohort_did_summary_live.csv', index=False)
    stacked.to_csv(OUT_T / 'stage6_stacked_did_summary_live.csv', index=False)
    make_raw_trends(df, OUT_F / 'fig_stage6_raw_trends_live.png')
    write_summary(df, twfe, cohort, stacked, args.force_refresh)


if __name__ == '__main__':
    main()
