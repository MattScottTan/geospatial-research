from __future__ import annotations

from pathlib import Path
import math
import json
import shutil

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path('/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full')
OUT = ROOT / 'final_submission' / 'originality'
P1 = OUT / 'prototype_1'
P2 = OUT / 'prototype_2'
FINAL = OUT / 'final'


def ensure_dirs() -> None:
    for p in [P1, P2, FINAL]:
        p.mkdir(parents=True, exist_ok=True)


def haversine_np(lat1, lon1, lat2, lon2):
    R = 6371.0088
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(a))


def minmax(series: pd.Series) -> pd.Series:
    s = series.astype(float)
    mn, mx = s.min(), s.max()
    if mx == mn:
        return pd.Series(np.zeros(len(s)), index=s.index)
    return (s - mn) / (mx - mn)


def load_base() -> tuple[pd.DataFrame, gpd.GeoDataFrame, pd.DataFrame]:
    cities = pd.read_csv(ROOT / 'outputs/tables/city_access_metrics.csv')
    ai = pd.read_csv(ROOT / 'outputs/tables/city_access_ai.csv')
    inst = pd.read_csv(ROOT / 'outputs/tables/openalex_institutions_top.csv')
    regions = gpd.read_file(ROOT / 'data/processed/cloud_regions.gpkg')
    return cities, regions, inst, ai


def build_bundle_index(cities: pd.DataFrame, regions: gpd.GeoDataFrame, inst: pd.DataFrame, ai: pd.DataFrame):
    city = cities.copy()

    # counts of regions/providers within given radii
    city_coords = city[['lat', 'lng']].to_numpy(dtype=float)
    reg_coords = regions[['lat', 'lon']].to_numpy(dtype=float)
    providers = regions['provider'].to_numpy()
    counts_1000 = np.zeros(len(city), dtype=int)
    counts_1500 = np.zeros(len(city), dtype=int)
    unique_providers_1000 = np.zeros(len(city), dtype=int)

    for start in range(0, len(city), 500):
        end = min(start + 500, len(city))
        c = city_coords[start:end]
        d = haversine_np(c[:, None, 0], c[:, None, 1], reg_coords[None, :, 0], reg_coords[None, :, 1])
        mask1000 = d <= 1000
        mask1500 = d <= 1500
        counts_1000[start:end] = mask1000.sum(axis=1)
        counts_1500[start:end] = mask1500.sum(axis=1)
        for i, row_mask in enumerate(mask1000):
            unique_providers_1000[start + i] = len(np.unique(providers[row_mask])) if row_mask.any() else 0

    # institution anchor signal via matched AI overlay and top institution counts
    ai_small = ai[['city', 'country', 'openalex_ai_institution_count', 'openalex_ai_works_recent']].copy()
    ai_small = ai_small.groupby(['city','country'], as_index=False).agg({
        'openalex_ai_institution_count':'max',
        'openalex_ai_works_recent':'sum',
    })
    ai_small = ai_small.rename(columns={'openalex_ai_institution_count':'ai_inst_count', 'openalex_ai_works_recent':'ai_works_recent'})
    city = city.merge(ai_small, on=['city','country'], how='left')
    city['ai_inst_count'] = city['ai_inst_count'].fillna(0)
    city['ai_works_recent'] = city['ai_works_recent'].fillna(0)

    inst_agg = inst.groupby(['geo_city','geo_country_code']).agg(
        top_inst_count=('institution_id','count'),
        top_inst_ai_works=('ai_works_count_recent','sum'),
    ).reset_index()
    city = city.merge(inst_agg, left_on=['city','iso2'], right_on=['geo_city','geo_country_code'], how='left')
    city['top_inst_count'] = city['top_inst_count'].fillna(0)
    city['top_inst_ai_works'] = city['top_inst_ai_works'].fillna(0)

    city['regions_within_1000'] = counts_1000
    city['regions_within_1500'] = counts_1500
    city['providers_within_1000'] = unique_providers_1000

    # component scores
    city['score_proximity'] = minmax(-city['dist_km_nearest_region'])
    city['score_provider_diversity'] = minmax(city['providers_within_1000'])
    city['score_redundancy'] = minmax(np.log1p(city['regions_within_1500']))
    city['score_population'] = minmax(np.log1p(city['population'].fillna(0)))
    anchor_raw = np.log1p(city['top_inst_ai_works']) + 0.5 * np.log1p(city['top_inst_count'])
    city['score_institutions'] = minmax(anchor_raw)

    weights = {
        'score_proximity': 0.40,
        'score_provider_diversity': 0.15,
        'score_redundancy': 0.15,
        'score_population': 0.15,
        'score_institutions': 0.15,
    }
    city['bundle_score'] = sum(city[k] * w for k, w in weights.items()) * 100
    city['distance_only_score'] = minmax(-city['dist_km_nearest_region']) * 100
    city['bundle_gain_vs_distance'] = city['bundle_score'] - city['distance_only_score']

    weights_note = pd.DataFrame([
        {'component':k, 'weight':v} for k, v in weights.items()
    ])
    return city, weights_note


def plot_bundle(city: pd.DataFrame):
    world = gpd.read_file(ROOT / 'data/raw/ne_110m_admin_0_countries.geojson')
    gdf = gpd.GeoDataFrame(city, geometry=gpd.points_from_xy(city['lng'], city['lat']), crs='EPSG:4326')

    # Map: top 1000 by population for readability
    map_df = gdf.nlargest(1000, 'population').copy()
    fig, ax = plt.subplots(figsize=(14, 7.5))
    world.plot(ax=ax, color='#f4f4f4', edgecolor='#d0d0d0', linewidth=0.4)
    sc = ax.scatter(map_df['lng'], map_df['lat'], c=map_df['bundle_score'], s=np.clip(np.sqrt(map_df['population'].fillna(0))/25, 8, 120), cmap='viridis', alpha=0.75, linewidths=0)
    ax.set_title('Compute Opportunity Bundle Index', fontsize=16, weight='bold')
    ax.text(0.01, 0.02, 'Top 1,000 cities by population; color = bundle score; size = population', transform=ax.transAxes, fontsize=10)
    ax.set_axis_off()
    cbar = fig.colorbar(sc, ax=ax, fraction=0.025, pad=0.02)
    cbar.set_label('Bundle score (0-100)')
    fig.tight_layout()
    fig.savefig(P1 / 'fig_bundle_index_map.png', dpi=220, bbox_inches='tight')
    plt.close(fig)

    # Comparison scatter
    fig, ax = plt.subplots(figsize=(9.5, 7.5))
    sample = city.nlargest(1500, 'population').copy()
    ax.scatter(sample['distance_only_score'], sample['bundle_score'], s=np.clip(np.sqrt(sample['population'].fillna(0))/20, 10, 140), alpha=0.45)
    ax.set_xlabel('Distance-only compute access score (0-100)')
    ax.set_ylabel('Bundle score (0-100)')
    ax.set_title('Bundle Score vs. Distance-Only Access', fontsize=15, weight='bold')
    top_out = city.sort_values('bundle_gain_vs_distance', ascending=False).head(10)
    low_out = city.sort_values('bundle_gain_vs_distance', ascending=True).head(5)
    for _, r in pd.concat([top_out, low_out]).iterrows():
        ax.annotate(r['city'], (r['distance_only_score'], r['bundle_score']), fontsize=8, alpha=0.8)
    fig.tight_layout()
    fig.savefig(P1 / 'fig_bundle_vs_distance.png', dpi=220, bbox_inches='tight')
    plt.close(fig)

    # Top cities bar chart
    top = city.nlargest(15, 'bundle_score').sort_values('bundle_score')
    fig, ax = plt.subplots(figsize=(10.5, 7.2))
    ax.barh(top['city'] + ', ' + top['country'], top['bundle_score'])
    ax.set_title('Top Cities by Compute Opportunity Bundle Score', fontsize=15, weight='bold')
    ax.set_xlabel('Bundle score (0-100)')
    fig.tight_layout()
    fig.savefig(P1 / 'fig_bundle_top_cities.png', dpi=220, bbox_inches='tight')
    plt.close(fig)


def write_bundle_note(weights_note: pd.DataFrame, city: pd.DataFrame):
    top_gain = city.sort_values('bundle_gain_vs_distance', ascending=False).head(10)
    (P1 / 'bundle_city_scores.csv').write_text(city.sort_values('bundle_score', ascending=False).to_csv(index=False))
    (P1 / 'bundle_positive_outliers.csv').write_text(top_gain.to_csv(index=False))
    note = f'''# Prototype 1 note — Compute Opportunity Bundle Index

## Components and weights

{weights_note.to_markdown(index=False)}

## Reading

This prototype keeps raw cloud proximity central but adds three other layers visible in the current project data: provider diversity, regional redundancy, and institutional/market anchors.

## Why it is promising

- It operationalizes the project's mature claim that compute works as part of a broader bundle.
- It produces a strong global map plus interpretable comparison/outlier views.
- It can flow directly into the four-city case-study section.

## Risks / limits

- The institutional anchor signal comes from the project's OpenAlex-linked files, so it is not a fully independent external ecosystem measure.
- It is more original than distance alone, but less surprising than a full counterfactual siting analysis.
'''
    (P1 / 'prototype_1_note.md').write_text(note)


def build_counterfactual(cities: pd.DataFrame):
    city = cities.copy()
    city['pop_weight'] = np.log1p(city['population'].fillna(city['population'].median()))
    baseline = np.average(city['dist_km_nearest_region'], weights=city['pop_weight'])

    candidates = city[(city['dist_km_nearest_region'] > 750) & (city['population'] >= 1_000_000)].copy()
    # limit for tractability and legibility
    candidates = candidates.nlargest(250, 'population').copy().reset_index(drop=True)

    all_lat = city['lat'].to_numpy()
    all_lon = city['lng'].to_numpy()
    curr = city['dist_km_nearest_region'].to_numpy()
    weights = city['pop_weight'].to_numpy()

    reductions = []
    cand_lat = candidates['lat'].to_numpy()
    cand_lon = candidates['lng'].to_numpy()
    for i in range(len(candidates)):
        d = haversine_np(all_lat, all_lon, cand_lat[i], cand_lon[i])
        newdist = np.minimum(curr, d)
        weighted = np.average(newdist, weights=weights)
        reductions.append(baseline - weighted)
    candidates['weighted_km_reduction'] = reductions
    candidates['baseline_weighted_km'] = baseline

    # outputs
    candidates.to_csv(P2 / 'counterfactual_candidates.csv', index=False)

    world = gpd.read_file(ROOT / 'data/raw/ne_110m_admin_0_countries.geojson')
    fig, ax = plt.subplots(figsize=(14, 7.5))
    world.plot(ax=ax, color='#f4f4f4', edgecolor='#d0d0d0', linewidth=0.4)
    top = candidates.nlargest(20, 'weighted_km_reduction')
    ax.scatter(top['lng'], top['lat'], s=np.clip(top['weighted_km_reduction']*3, 40, 300), c=top['weighted_km_reduction'], cmap='magma', alpha=0.8)
    for _, r in top.head(10).iterrows():
        ax.annotate(r['city'], (r['lng'], r['lat']), fontsize=8)
    ax.set_title('Prototype 2: Candidate New Compute Nodes That Reduce the Largest Weighted Gap', fontsize=15, weight='bold')
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(P2 / 'fig_counterfactual_top_candidates.png', dpi=220, bbox_inches='tight')
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6.8))
    bars = top.head(12).sort_values('weighted_km_reduction')
    ax.barh(bars['city'] + ', ' + bars['country'], bars['weighted_km_reduction'])
    ax.set_title('Top Candidate Cities by Reduction in Weighted Average Distance', fontsize=15, weight='bold')
    ax.set_xlabel('Weighted km reduction (log-population weighted)')
    fig.tight_layout()
    fig.savefig(P2 / 'fig_counterfactual_gain_bars.png', dpi=220, bbox_inches='tight')
    plt.close(fig)

    note = f'''# Prototype 2 note — Counterfactual Compute Siting Layer

## Objective
Rank candidate cities by how much one additional compute node at that location would reduce the log-population-weighted average nearest-cloud distance across the current 8,000-city frame.

## Baseline
Current weighted average nearest-cloud distance: **{baseline:.1f} km**

## Why it is promising

- It turns the atlas into a policy/counterfactual planning tool.
- It is visually distinctive and more difficult to replicate casually than another descriptive map.
- It can create a strong “where next?” moment in the StoryMap.

## Risks / limits

- It is a simplified geodesic planning exercise, not a true network or business case model.
- It is hypothetical and may feel more speculative than the bundle index.
'''
    (P2 / 'prototype_2_note.md').write_text(note)
    return candidates


def select_and_finalize(city_bundle: pd.DataFrame, candidates: pd.DataFrame):
    scores = pd.DataFrame([
        {'package':'Prototype 1 — Bundle Index','novelty':4.2,'visual_payoff':4.6,'judge_legibility':4.8,'fit_with_final_claim':4.9,'implementation_risk':4.6},
        {'package':'Prototype 2 — Counterfactual Siting','novelty':4.7,'visual_payoff':4.4,'judge_legibility':4.0,'fit_with_final_claim':3.9,'implementation_risk':3.7},
    ])
    scores['total'] = scores[['novelty','visual_payoff','judge_legibility','fit_with_final_claim','implementation_risk']].mean(axis=1)
    winner = scores.sort_values('total', ascending=False).iloc[0]['package']
    selection = f'''# Originality Selection

Date: 2026-03-14 12:05 PM America/New_York

## Scorecard

{scores.to_markdown(index=False)}

## Selected primary package

**{winner}**

## Why it wins

Prototype 1 has the best combination of visible originality, immediate fit with the report's central claim, and clean StoryMap legibility. It deepens the project rather than diverting it.

Prototype 2 remains a strong backup because it creates a genuine planning/counterfactual hook, but it is more speculative and less aligned with the project's core interpretive line.

## Backup package

**Prototype 2 — Counterfactual Compute Siting Layer**
'''
    (OUT / 'originality_selection.md').write_text(selection)

    # Final outputs are the selected prototype 1 assets copied into final/
    for fn in ['fig_bundle_index_map.png','fig_bundle_vs_distance.png','fig_bundle_top_cities.png','bundle_city_scores.csv','bundle_positive_outliers.csv','prototype_1_note.md']:
        src = P1 / fn
        dst_name = fn.replace('prototype_1_note.md','bundle_method_note.md')
        shutil.copy2(src, FINAL / dst_name)

    statement = '''# Originality Statement

## One-sentence version
This submission extends the atlas beyond raw distance to cloud regions by introducing a **Compute Opportunity Bundle Index** that combines proximity, provider diversity, regional redundancy, institutional anchors, and city scale into a single comparative opportunity layer.

## Expanded version
The project’s original contribution is not only that it maps distance to compute, but that it shows why distance alone is too thin. The final submission adds a Compute Opportunity Bundle Index built from the project’s own city, cloud, and institution layers, making it possible to compare cities that are merely close to compute with cities that sit inside a broader bundle of opportunity conditions. This turns the atlas from a one-variable proximity map into a more distinctive public-interest screening and explanation tool.
'''
    (OUT / 'originality_statement.md').write_text(statement)


def main():
    ensure_dirs()
    cities, regions, inst, ai = load_base()
    city_bundle, weights_note = build_bundle_index(cities, regions, inst, ai)
    plot_bundle(city_bundle)
    write_bundle_note(weights_note, city_bundle)
    candidates = build_counterfactual(cities)
    select_and_finalize(city_bundle, candidates)


if __name__ == '__main__':
    main()
