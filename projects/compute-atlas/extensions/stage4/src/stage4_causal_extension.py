from __future__ import annotations

from pathlib import Path
import json
import math

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

STAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
OUTDIR = STAGE_ROOT / "outputs" / "stage4"
FIGDIR = OUTDIR / "figures"
TABLEDIR = OUTDIR / "tables"
DOCSDIR = STAGE_ROOT / "docs"


def ensure_dirs() -> None:
    for p in [OUTDIR, FIGDIR, TABLEDIR, DOCSDIR]:
        p.mkdir(parents=True, exist_ok=True)


def haversine_matrix(lat1: np.ndarray, lon1: np.ndarray, lat2: np.ndarray, lon2: np.ndarray) -> np.ndarray:
    """Vectorized great-circle distance matrix in kilometers."""
    R = 6371.0088
    lat1 = np.radians(np.asarray(lat1))[:, None]
    lon1 = np.radians(np.asarray(lon1))[:, None]
    lat2 = np.radians(np.asarray(lat2))[None, :]
    lon2 = np.radians(np.asarray(lon2))[None, :]
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    return 2.0 * R * np.arcsin(np.sqrt(np.clip(a, 0.0, 1.0)))


def load_analysis_frame() -> pd.DataFrame:
    city_ai = pd.read_csv(REPO_ROOT / "outputs" / "tables" / "city_access_ai.csv")
    inst = pd.read_csv(REPO_ROOT / "data" / "raw" / "openalex_ai_institutions_top.csv")
    countries = gpd.read_file(REPO_ROOT / "data" / "raw" / "ne_110m_admin_0_countries.geojson")
    countries = countries[["ISO_A2", "GDP_MD", "POP_EST", "INCOME_GRP", "CONTINENT", "REGION_UN", "SUBREGION"]].copy()
    countries["ISO_A2"] = countries["ISO_A2"].astype(str).str.upper()

    inst["geo_country_code"] = inst["geo_country_code"].astype(str).str.upper()
    inst_city = (
        inst.groupby(["geo_city", "geo_country_code"], dropna=False)
        .agg(
            top_inst_count=("institution_id", "nunique"),
            top_inst_ai_recent=("ai_works_count_recent", "sum"),
            top_inst_total_works=("works_count_total", "sum"),
            top_inst_mean_total_works=("works_count_total", "mean"),
        )
        .reset_index()
    )

    df = city_ai.merge(
        inst_city,
        how="left",
        left_on=["openalex_geo_city", "iso2"],
        right_on=["geo_city", "geo_country_code"],
    )
    df = df.merge(countries, how="left", left_on="iso2", right_on="ISO_A2")

    # Fill institution-derived controls. They are used only in aggressive sensitivity checks.
    for col in ["top_inst_count", "top_inst_ai_recent", "top_inst_total_works", "top_inst_mean_total_works"]:
        df[col] = df[col].fillna(0)

    # Base covariates.
    df["match_ok"] = df["openalex_match_ok"].fillna(False).astype(bool)
    df["dist1000"] = df["dist_km_nearest_region"] / 1000.0
    df["log_pop"] = np.log(df["population"].clip(lower=1))
    df["is_primary_capital"] = (df["capital"] == "primary").astype(int)
    df["is_admin_capital"] = df["capital"].isin(["primary", "admin"]).astype(int)
    df["log1p_top_inst_total_works"] = np.log1p(df["top_inst_total_works"])
    df["log1p_top_inst_count"] = np.log1p(df["top_inst_count"])

    # Country-level context from Natural Earth.
    df["SUBREGION"] = df["SUBREGION"].fillna("Unknown")
    df["INCOME_GRP"] = df["INCOME_GRP"].fillna("Unknown")
    for col in ["GDP_MD", "POP_EST"]:
        positive = df.loc[df[col].notna() & (df[col] > 0), col]
        fill_value = float(positive.median()) if not positive.empty else 1.0
        df[col] = df[col].fillna(fill_value)
        df.loc[df[col] <= 0, col] = fill_value
    df["log_gdp_md"] = np.log(df["GDP_MD"])
    df["log_country_pop"] = np.log(df["POP_EST"])

    # Cloud-density features from the raw provider lists.
    regions = []
    for provider, fn in [("aws", "cloud_regions_aws.csv"), ("azure", "cloud_regions_azure.csv"), ("gcp", "cloud_regions_gcp.csv")]:
        tmp = pd.read_csv(REPO_ROOT / "data" / "raw" / fn)
        tmp["provider"] = provider
        regions.append(tmp[["provider", "region", "lat", "lon"]])
    regions = pd.concat(regions, ignore_index=True)

    D = haversine_matrix(df["lat"].to_numpy(), df["lng"].to_numpy(), regions["lat"].to_numpy(), regions["lon"].to_numpy())
    for provider in ["aws", "azure", "gcp"]:
        mask = regions["provider"].to_numpy() == provider
        dprov = D[:, mask]
        df[f"dist_{provider}_nearest"] = dprov.min(axis=1)
        for rad in [500, 1000]:
            df[f"{provider}_regions_within_{rad}km"] = (dprov <= rad).sum(axis=1)
    for rad in [250, 500, 1000]:
        within = D <= rad
        df[f"regions_within_{rad}km"] = within.sum(axis=1)
        provider_counts = []
        provider_values = regions["provider"].to_numpy()
        for i in range(within.shape[0]):
            provider_counts.append(pd.unique(provider_values[within[i]]).size)
        df[f"providers_within_{rad}km"] = provider_counts

    # Country-demeaned diagnostics for within-country comparison.
    multi = df[df["match_ok"]].groupby("iso2").filter(lambda x: len(x) >= 2).copy()
    for col in ["log_ai_works", "dist1000", "log_pop"]:
        multi[f"{col}_dm"] = multi[col] - multi.groupby("iso2")[col].transform("mean")

    return df, multi


def fit_stage4_models(df: pd.DataFrame) -> pd.DataFrame:
    d = df[df["match_ok"]].copy()
    formulas = {
        "Stage4-B1 Baseline": "log_ai_works ~ dist1000 + log_pop",
        "Stage4-B2 Country+subregion controls": "log_ai_works ~ dist1000 + log_pop + is_primary_capital + is_admin_capital + log_gdp_md + log_country_pop + C(SUBREGION)",
        "Stage4-B3 Country fixed effects": "log_ai_works ~ dist1000 + log_pop + is_primary_capital + is_admin_capital + C(iso2)",
        "Stage4-B4 Country FE + aggressive research-capacity control": "log_ai_works ~ dist1000 + log_pop + is_primary_capital + is_admin_capital + log1p_top_inst_total_works + log1p_top_inst_count + C(iso2)",
        "Stage4-B5 Density-control stress test": "log_ai_works ~ dist1000 + log_pop + is_primary_capital + is_admin_capital + log_gdp_md + log_country_pop + regions_within_500km + providers_within_500km + C(SUBREGION)",
    }

    rows = []
    for model_name, formula in formulas.items():
        mod0 = smf.ols(formula, data=d)
        row_labels = pd.Index(mod0.data.row_labels)
        groups = d.loc[row_labels, "iso2"]
        mod = mod0.fit(cov_type="cluster", cov_kwds={"groups": groups})
        rows.append(
            {
                "model": model_name,
                "formula": formula,
                "n": int(mod.nobs),
                "coef_dist1000": float(mod.params["dist1000"]),
                "se_dist1000": float(mod.bse["dist1000"]),
                "p_dist1000": float(mod.pvalues["dist1000"]),
                "ci_low": float(mod.params["dist1000"] - 1.96 * mod.bse["dist1000"]),
                "ci_high": float(mod.params["dist1000"] + 1.96 * mod.bse["dist1000"]),
                "r2": float(mod.rsquared),
            }
        )
    return pd.DataFrame(rows)


def fit_within_country_diagnostic(multi: pd.DataFrame) -> pd.DataFrame:
    X = sm.add_constant(multi[["dist1000_dm", "log_pop_dm"]])
    mod = sm.OLS(multi["log_ai_works_dm"], X).fit(cov_type="cluster", cov_kwds={"groups": multi["iso2"]})
    out = pd.DataFrame(
        [
            {
                "model": "Within-country demeaned OLS",
                "n": int(mod.nobs),
                "countries": int(multi["iso2"].nunique()),
                "coef_dist1000_dm": float(mod.params["dist1000_dm"]),
                "se_dist1000_dm": float(mod.bse["dist1000_dm"]),
                "p_dist1000_dm": float(mod.pvalues["dist1000_dm"]),
                "coef_log_pop_dm": float(mod.params["log_pop_dm"]),
                "corr_demeaned": float(multi[["log_ai_works_dm", "dist1000_dm"]].corr().iloc[0, 1]),
            }
        ]
    )
    return out


def fit_matching_checks(df: pd.DataFrame) -> pd.DataFrame:
    d = df[df["match_ok"]].copy()
    rows = []
    for threshold in [250, 500]:
        dd = d.copy()
        dd["treated"] = (dd["dist_km_nearest_region"] <= threshold).astype(int)
        X = dd[["log_pop", "is_primary_capital", "is_admin_capital", "log_gdp_md", "log_country_pop", "SUBREGION"]].copy()
        y = dd["treated"].to_numpy()

        pre = ColumnTransformer(
            [
                (
                    "num",
                    Pipeline([("imp", SimpleImputer(strategy="median"))]),
                    ["log_pop", "is_primary_capital", "is_admin_capital", "log_gdp_md", "log_country_pop"],
                ),
                (
                    "cat",
                    Pipeline(
                        [
                            ("imp", SimpleImputer(strategy="most_frequent")),
                            ("oh", OneHotEncoder(handle_unknown="ignore")),
                        ]
                    ),
                    ["SUBREGION"],
                ),
            ]
        )
        clf = Pipeline([("pre", pre), ("logit", LogisticRegression(max_iter=5000))])
        clf.fit(X, y)
        ps = np.clip(clf.predict_proba(X)[:, 1], 0.02, 0.98)
        att_weights = np.where(y == 1, 1.0, ps / (1.0 - ps))
        dd["att_weight"] = att_weights

        naive = smf.ols("log_ai_works ~ treated", data=dd).fit(cov_type="HC1")
        dr = smf.wls(
            "log_ai_works ~ treated + log_pop + is_primary_capital + is_admin_capital + log_gdp_md + log_country_pop + C(SUBREGION)",
            data=dd,
            weights=dd["att_weight"],
        ).fit(cov_type="HC1")

        rows.append(
            {
                "threshold_km": threshold,
                "treated_share": float(dd["treated"].mean()),
                "naive_diff": float(naive.params["treated"]),
                "naive_p": float(naive.pvalues["treated"]),
                "naive_ci_low": float(naive.params["treated"] - 1.96 * naive.bse["treated"]),
                "naive_ci_high": float(naive.params["treated"] + 1.96 * naive.bse["treated"]),
                "dr_att": float(dr.params["treated"]),
                "dr_p": float(dr.pvalues["treated"]),
                "dr_ci_low": float(dr.params["treated"] - 1.96 * dr.bse["treated"]),
                "dr_ci_high": float(dr.params["treated"] + 1.96 * dr.bse["treated"]),
            }
        )
    return pd.DataFrame(rows)


def make_coef_plot(model_df: pd.DataFrame, output_path: Path) -> None:
    plot_df = model_df.copy()
    plot_df = plot_df.sort_values("coef_dist1000", ascending=True).reset_index(drop=True)
    y = np.arange(len(plot_df))
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.axvline(0.0, color="0.4", lw=1.0, ls="--")
    ax.errorbar(
        plot_df["coef_dist1000"],
        y,
        xerr=1.96 * plot_df["se_dist1000"],
        fmt="o",
        capsize=4,
        lw=1.2,
    )
    ax.set_yticks(y)
    ax.set_yticklabels(plot_df["model"])
    ax.set_xlabel("Distance coefficient on log(1 + AI works), per additional 1,000 km")
    ax.set_ylabel("")
    ax.set_title("Stage 4 causal stress tests: distance coefficient is not stable")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def make_within_country_scatter(multi: pd.DataFrame, output_path: Path) -> None:
    x = multi["dist1000_dm"].to_numpy()
    y = multi["log_ai_works_dm"].to_numpy()
    coef = np.polyfit(x, y, 1)
    xs = np.linspace(x.min(), x.max(), 200)
    ys = coef[0] * xs + coef[1]

    fig, ax = plt.subplots(figsize=(8.8, 5.6))
    ax.scatter(x, y, alpha=0.6, s=18)
    ax.plot(xs, ys, lw=1.6)
    ax.axhline(0.0, color="0.4", lw=0.8, ls="--")
    ax.axvline(0.0, color="0.4", lw=0.8, ls="--")
    ax.set_xlabel("Distance to nearest cloud region, demeaned within country (1,000 km)")
    ax.set_ylabel("log(1 + AI works), demeaned within country")
    ax.set_title("Within-country comparison: little residual distance gradient")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def write_markdown_summary(model_df: pd.DataFrame, within_df: pd.DataFrame, match_df: pd.DataFrame, output_path: Path) -> None:
    baseline = model_df.loc[model_df["model"] == "Stage4-B1 Baseline"].iloc[0]
    country_fe = model_df.loc[model_df["model"] == "Stage4-B3 Country fixed effects"].iloc[0]
    with_country = within_df.iloc[0]
    lines = [
        "# Stage 4 causal-extension summary",
        "",
        "## What was attempted",
        "- Re-estimate the distance relationship with richer geographic and country-level controls.",
        "- Test whether the coefficient survives within-country fixed effects.",
        "- Run a within-country demeaned regression as a direct diagnostic.",
        "- Run doubly robust treatment-effect checks for being very close to compute (<=250 km and <=500 km).",
        "",
        "## Core result",
        f"- Baseline cross-sectional OLS on the well-matched sample reproduces the original negative sign: {baseline['coef_dist1000']:.3f} per additional 1,000 km (p={baseline['p_dist1000']:.3f}).",
        f"- Once country fixed effects are added, the coefficient becomes {country_fe['coef_dist1000']:.3f} (p={country_fe['p_dist1000']:.3f}).",
        f"- The within-country demeaned regression gives {with_country['coef_dist1000_dm']:.3f} (p={with_country['p_dist1000_dm']:.3f}), with demeaned correlation {with_country['corr_demeaned']:.3f}.",
        "- Matching / weighting estimates are imprecise and unstable across thresholds; none support a clean causal claim.",
        "",
        "## Bottom line",
        "The current snapshot supports an association in descriptive and spatial-model terms, but it does not support a credible causal claim once stricter within-place comparisons are used.",
        "A real causal Stage 4 would need a city-year AI outcome and time-stamped cloud-region openings or other exogenous infrastructure shocks.",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    df, multi = load_analysis_frame()
    model_df = fit_stage4_models(df)
    within_df = fit_within_country_diagnostic(multi)
    match_df = fit_matching_checks(df)

    model_df.to_csv(TABLEDIR / "stage4_model_summary.csv", index=False)
    within_df.to_csv(TABLEDIR / "stage4_within_country_summary.csv", index=False)
    match_df.to_csv(TABLEDIR / "stage4_matching_summary.csv", index=False)

    make_coef_plot(model_df, FIGDIR / "fig_stage4_coef_stress_test.png")
    make_within_country_scatter(multi, FIGDIR / "fig_stage4_within_country_scatter.png")
    write_markdown_summary(model_df, within_df, match_df, DOCSDIR / "analysis_approach_stage4_summary.md")

    metrics = {
        "n_matched_total": int(df["match_ok"].sum()),
        "n_within_country": int(within_df.iloc[0]["n"]),
        "countries_within_country": int(within_df.iloc[0]["countries"]),
        "baseline_coef": float(model_df.loc[model_df["model"] == "Stage4-B1 Baseline", "coef_dist1000"].iloc[0]),
        "baseline_p": float(model_df.loc[model_df["model"] == "Stage4-B1 Baseline", "p_dist1000"].iloc[0]),
        "country_fe_coef": float(model_df.loc[model_df["model"] == "Stage4-B3 Country fixed effects", "coef_dist1000"].iloc[0]),
        "country_fe_p": float(model_df.loc[model_df["model"] == "Stage4-B3 Country fixed effects", "p_dist1000"].iloc[0]),
        "within_country_coef": float(within_df.iloc[0]["coef_dist1000_dm"]),
        "within_country_p": float(within_df.iloc[0]["p_dist1000_dm"]),
    }
    (TABLEDIR / "stage4_key_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("Wrote:")
    for fp in [
        TABLEDIR / "stage4_model_summary.csv",
        TABLEDIR / "stage4_within_country_summary.csv",
        TABLEDIR / "stage4_matching_summary.csv",
        TABLEDIR / "stage4_key_metrics.json",
        FIGDIR / "fig_stage4_coef_stress_test.png",
        FIGDIR / "fig_stage4_within_country_scatter.png",
        DOCSDIR / "analysis_approach_stage4_summary.md",
    ]:
        print(fp)


if __name__ == "__main__":
    main()
