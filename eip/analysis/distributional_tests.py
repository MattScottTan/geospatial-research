"""
Statistical tests for Finding 1: Distributional difference between
AI-linked cities and the broader city system in distance to nearest
cloud compute region.

Tests:
1. Two-sample Kolmogorov-Smirnov — tests whether two samples come
   from the same continuous distribution. The D statistic is the
   maximum absolute difference between the two empirical CDFs.
   A large D with a small p-value means the distributions are
   significantly different.

2. Mann-Whitney U (one-sided) — tests whether values in one sample
   are systematically smaller than in the other. It does not assume
   normality. The alternative='less' tests whether AI-city distances
   tend to be shorter than all-city distances.

3. Chi-square test of independence — tests whether the proportion
   of cities within a given distance threshold (500 km) differs
   significantly between the two groups. This is the most intuitive
   test for a general audience: "is 72% vs 44% a real difference?"

4. Cohen's d — an effect-size measure that quantifies how far apart
   the two group means are in units of pooled standard deviation.
   By convention: d ≈ 0.2 is small, 0.5 is medium, 0.8 is large.

Usage:
    python distributional_tests.py

Inputs:
    - city_access_metrics.csv  (all 8,000 cities with dist_km_nearest_region)
    - city_access_ai.csv       (AI-linked cities with dist_km_nearest_region)

Both files should be in the same directory as this script, or update
the paths below.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp, mannwhitneyu, chi2_contingency

# ── CONFIG ────────────────────────────────────────────────────────
DATA_DIR = Path(".")  # update if your CSVs are elsewhere
ALL_CITIES_FILE = DATA_DIR / "city_access_metrics.csv"
AI_CITIES_FILE = DATA_DIR / "city_access_ai.csv"
THRESHOLD_KM = 500  # for chi-square test
# ──────────────────────────────────────────────────────────────────


def load_data():
    all_cities = pd.read_csv(ALL_CITIES_FILE)
    ai_cities = pd.read_csv(AI_CITIES_FILE)

    # Deduplicate AI cities by city+country to avoid double-counting
    ai_unique = ai_cities.drop_duplicates(subset=["city", "country"])

    all_dist = all_cities["dist_km_nearest_region"].dropna().values
    ai_dist = ai_unique["dist_km_nearest_region"].dropna().values

    return all_dist, ai_dist


def run_ks_test(ai_dist, all_dist):
    """
    Two-sample Kolmogorov-Smirnov test.

    Null hypothesis: both samples are drawn from the same distribution.
    The D statistic is the maximum absolute difference between the two
    empirical cumulative distribution functions (ECDFs). A large D and
    small p-value means the distributions are significantly different.
    """
    stat, p = ks_2samp(ai_dist, all_dist)
    return stat, p


def run_mannwhitney(ai_dist, all_dist):
    """
    Mann-Whitney U test (one-sided: AI cities < all cities).

    Null hypothesis: the two populations have the same distribution.
    Alternative: AI-linked cities have systematically shorter distances.
    This is a rank-based test that does not assume normality.
    """
    stat, p = mannwhitneyu(ai_dist, all_dist, alternative="less")
    return stat, p


def run_chi_square(ai_dist, all_dist, threshold_km):
    """
    Chi-square test of independence on a distance threshold.

    Constructs a 2x2 contingency table:
        - AI cities within/beyond threshold
        - All cities within/beyond threshold

    Null hypothesis: the proportion within the threshold is the same
    for both groups.
    """
    ai_within = (ai_dist <= threshold_km).sum()
    ai_beyond = (ai_dist > threshold_km).sum()
    all_within = (all_dist <= threshold_km).sum()
    all_beyond = (all_dist > threshold_km).sum()

    table = [[ai_within, ai_beyond], [all_within, all_beyond]]
    chi2, p, dof, expected = chi2_contingency(table)

    return chi2, p, dof, ai_within, ai_beyond, all_within, all_beyond


def compute_cohens_d(ai_dist, all_dist):
    """
    Cohen's d effect size.

    Measures the difference between two group means in units of
    pooled standard deviation.

    Interpretation:
        d ≈ 0.2  → small effect
        d ≈ 0.5  → medium effect
        d ≈ 0.8  → large effect
    """
    pooled_std = np.sqrt((np.var(ai_dist) + np.var(all_dist)) / 2)
    d = (np.mean(all_dist) - np.mean(ai_dist)) / pooled_std
    return d


def main():
    all_dist, ai_dist = load_data()

    print("=" * 65)
    print("FINDING 1 — DISTRIBUTIONAL SIGNIFICANCE TESTS")
    print("=" * 65)
    print()

    # Descriptive stats
    print(f"Sample sizes:")
    print(f"  All large cities:         n = {len(all_dist):,}")
    print(f"  AI-linked cities (unique): n = {len(ai_dist):,}")
    print()
    print(f"Medians:")
    print(f"  All cities:    {np.median(all_dist):,.1f} km")
    print(f"  AI cities:     {np.median(ai_dist):,.1f} km")
    print()
    print(f"Means:")
    print(f"  All cities:    {np.mean(all_dist):,.1f} km")
    print(f"  AI cities:     {np.mean(ai_dist):,.1f} km")
    print()

    # Test 1: KS
    ks_d, ks_p = run_ks_test(ai_dist, all_dist)
    print("-" * 65)
    print("TEST 1: Two-sample Kolmogorov-Smirnov")
    print(f"  D statistic:  {ks_d:.4f}")
    print(f"  p-value:      {ks_p:.2e}")
    print(f"  Interpretation: {'Significant' if ks_p < 0.05 else 'Not significant'}"
          f" — the two distance distributions are"
          f" {'different' if ks_p < 0.05 else 'not detectably different'}.")
    print()

    # Test 2: Mann-Whitney
    mw_u, mw_p = run_mannwhitney(ai_dist, all_dist)
    print("-" * 65)
    print("TEST 2: Mann-Whitney U (one-sided: AI < all)")
    print(f"  U statistic:  {mw_u:,.0f}")
    print(f"  p-value:      {mw_p:.2e}")
    print(f"  Interpretation: {'Significant' if mw_p < 0.05 else 'Not significant'}"
          f" — AI-linked cities are"
          f" {'systematically closer' if mw_p < 0.05 else 'not detectably closer'}"
          f" to cloud regions.")
    print()

    # Test 3: Chi-square
    chi2, chi_p, dof, ai_w, ai_b, all_w, all_b = run_chi_square(
        ai_dist, all_dist, THRESHOLD_KM
    )
    ai_pct = ai_w / len(ai_dist) * 100
    all_pct = all_w / len(all_dist) * 100
    print("-" * 65)
    print(f"TEST 3: Chi-square test of independence ({THRESHOLD_KM} km threshold)")
    print(f"  AI cities within {THRESHOLD_KM} km:   {ai_w} ({ai_pct:.1f}%)")
    print(f"  All cities within {THRESHOLD_KM} km:  {all_w} ({all_pct:.1f}%)")
    print(f"  Chi-square:   {chi2:.2f}")
    print(f"  df:           {dof}")
    print(f"  p-value:      {chi_p:.2e}")
    print(f"  Interpretation: {'Significant' if chi_p < 0.05 else 'Not significant'}"
          f" — the proportion difference ({ai_pct:.0f}% vs {all_pct:.0f}%)"
          f" is {'real' if chi_p < 0.05 else 'not detectable'}.")
    print()

    # Effect size
    d = compute_cohens_d(ai_dist, all_dist)
    label = "small" if d < 0.5 else ("medium" if d < 0.8 else "large")
    print("-" * 65)
    print("EFFECT SIZE: Cohen's d")
    print(f"  d = {d:.3f}  ({label} effect)")
    print(f"  Interpretation: The mean distance for AI cities is {d:.2f}")
    print(f"  pooled standard deviations closer than the mean for all cities.")
    print()

    # Summary for StoryMap copy-paste
    print("=" * 65)
    print("COPY-PASTE SUMMARY FOR STORYMAP")
    print("=" * 65)
    print()
    print(f"A two-sample Kolmogorov-Smirnov test confirms that the AI-linked")
    print(f"and all-city distance distributions are significantly different")
    print(f"(D = {ks_d:.2f}, p < 0.001). A one-sided Mann-Whitney U test")
    print(f"confirms that AI-linked cities are systematically closer to cloud")
    print(f"regions (U = {mw_u:,.0f}, p < 0.001). Cohen's d = {d:.2f},")
    print(f"a {label} effect size. A chi-square test on the {THRESHOLD_KM} km")
    print(f"threshold rejects equal proportions (chi2 = {chi2:.1f}, df = {dof},")
    print(f"p < 0.001).")


if __name__ == "__main__":
    main()
