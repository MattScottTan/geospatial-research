"""
Statistical tests for Finding 2: Weighted concentration analysis.

Tests whether high-output AI cities are disproportionately closer
to cloud compute, or whether the weighted median shift is just an
artifact of a few large cities.

Tests:
1. Spearman rank correlation — non-parametric test of whether
   distance and AI research output are monotonically related
   within the AI-linked sample. A negative rho means cities
   farther from compute tend to produce fewer works.

2. Pearson correlation (log-log) — parametric version on
   log-transformed distance and log-transformed works.

3. Permutation test on weighted median — shuffles AI works
   across the 319 cities 10,000 times and asks: how often
   does the reshuffled weighted median fall as low as the
   observed 164 km? A small p-value means the concentration
   near compute is not random.

4. Concentration ratios — compares the share of AI works
   within 250 km and 500 km to the share of AI cities within
   those thresholds. An excess means high-output cities are
   disproportionately close to compute.

Usage:
    python weighted_concentration_tests.py

Inputs:
    - city_access_ai.csv  (AI-linked cities with distance and works)

Place the CSV in the same directory, or update DATA_DIR below.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import spearmanr, pearsonr

# ── CONFIG ────────────────────────────────────────────────────────
DATA_DIR = Path(".")
AI_CITIES_FILE = DATA_DIR / "city_access_ai.csv"
N_PERMUTATIONS = 10_000
RANDOM_SEED = 42
# ──────────────────────────────────────────────────────────────────


def weighted_median(values, weights):
    """
    Compute the weighted median: the value at which the cumulative
    weight reaches 50% of total weight.
    """
    sorted_idx = np.argsort(values)
    sorted_vals = values[sorted_idx]
    sorted_weights = weights[sorted_idx]
    cumw = np.cumsum(sorted_weights)
    cutoff = sorted_weights.sum() / 2.0
    return sorted_vals[cumw >= cutoff][0]


def load_data():
    ai = pd.read_csv(AI_CITIES_FILE)
    ai_unique = ai.drop_duplicates(subset=["city", "country"]).copy()
    ai_unique = ai_unique.dropna(
        subset=["dist_km_nearest_region", "openalex_ai_works_recent"]
    )
    return ai_unique


def run_spearman(dist, works):
    """
    Spearman rank correlation between distance and AI works.

    This is a non-parametric test that does not assume linearity
    or normality. It asks: as distance rank increases, does
    AI-works rank tend to decrease?

    A negative rho with a small p-value would mean farther cities
    tend to produce fewer works (within the AI-linked sample).
    """
    rho, p = spearmanr(dist, works)
    return rho, p


def run_pearson_loglog(dist, works):
    """
    Pearson correlation on log-transformed values.

    Log transformation stabilizes variance and makes the
    relationship more linear. This is the parametric complement
    to the Spearman test above.
    """
    log_dist = np.log1p(dist)
    log_works = np.log1p(works)
    r, p = pearsonr(log_dist, log_works)
    return r, p


def run_permutation_test(dist, works, n_perms, seed):
    """
    Permutation test on the weighted median.

    Null hypothesis: the assignment of works to cities is
    independent of distance. Under this null, any city is
    equally likely to have any works count.

    Procedure:
    1. Compute the observed weighted median.
    2. Shuffle the works column 10,000 times.
    3. Recompute the weighted median each time.
    4. p-value = fraction of permuted medians <= observed.

    A small p-value means the observed concentration of
    high-output cities near compute is unlikely under random
    assignment.
    """
    observed = weighted_median(dist, works)

    np.random.seed(seed)
    perm_medians = np.empty(n_perms)
    for i in range(n_perms):
        shuffled = np.random.permutation(works)
        perm_medians[i] = weighted_median(dist, shuffled)

    p_value = (perm_medians <= observed).mean()
    return observed, np.median(perm_medians), p_value, perm_medians


def compute_concentration_ratios(ai_unique, thresholds_km=[250, 500, 1000]):
    """
    Concentration ratios at given distance thresholds.

    Compares:
    - % of AI cities within threshold
    - % of AI works within threshold

    If works % > cities %, high-output cities are
    disproportionately close to compute.
    """
    dist = ai_unique["dist_km_nearest_region"].values
    works = ai_unique["openalex_ai_works_recent"].values
    total_cities = len(ai_unique)
    total_works = works.sum()

    results = []
    for t in thresholds_km:
        mask = dist <= t
        n_cities = mask.sum()
        n_works = works[mask].sum()
        pct_cities = n_cities / total_cities * 100
        pct_works = n_works / total_works * 100
        excess = pct_works - pct_cities
        results.append({
            "threshold_km": t,
            "cities_within": n_cities,
            "pct_cities": pct_cities,
            "works_within": n_works,
            "pct_works": pct_works,
            "excess_pp": excess,
        })
    return pd.DataFrame(results)


def main():
    ai_unique = load_data()
    dist = ai_unique["dist_km_nearest_region"].values
    works = ai_unique["openalex_ai_works_recent"].values

    print("=" * 65)
    print("FINDING 2 — WEIGHTED CONCENTRATION TESTS")
    print("=" * 65)
    print()
    print(f"Unique AI cities: {len(ai_unique)}")
    print(f"Total AI works: {works.sum():,.0f}")
    print(f"Unweighted median distance: {np.median(dist):.1f} km")
    print()

    # Test 1: Spearman
    rho, p_s = run_spearman(dist, works)
    print("-" * 65)
    print("TEST 1: Spearman rank correlation (distance vs. AI works)")
    print(f"  rho = {rho:.4f}")
    print(f"  p-value = {p_s:.4f}")
    sig = "Significant" if p_s < 0.05 else "Not significant"
    print(f"  Interpretation: {sig} at alpha = 0.05.")
    if p_s >= 0.05:
        print("  Within the AI-linked sample, distance does not strongly")
        print("  predict research volume. The main signal is between")
        print("  AI-linked and non-AI cities (Finding 1), not within")
        print("  the AI-linked set.")
    print()

    # Test 2: Pearson log-log
    r, p_p = run_pearson_loglog(dist, works)
    print("-" * 65)
    print("TEST 2: Pearson correlation (log distance vs. log works)")
    print(f"  r = {r:.4f}")
    print(f"  p-value = {p_p:.4f}")
    print()

    # Test 3: Permutation test
    obs_wmed, null_wmed, perm_p, perm_medians = run_permutation_test(
        dist, works, N_PERMUTATIONS, RANDOM_SEED
    )
    print("-" * 65)
    print(f"TEST 3: Permutation test on weighted median ({N_PERMUTATIONS:,} shuffles)")
    print(f"  Observed weighted median:    {obs_wmed:.1f} km")
    print(f"  Null distribution median:    {null_wmed:.1f} km")
    print(f"  p-value (perm <= observed):  {perm_p:.4f}")
    sig = "Significant" if perm_p < 0.05 else "Borderline / not significant"
    print(f"  Interpretation: {sig} at alpha = 0.05.")
    print(f"  Null 5th percentile: {np.percentile(perm_medians, 5):.1f} km")
    print(f"  Null 95th percentile: {np.percentile(perm_medians, 95):.1f} km")
    print()

    # Test 4: Concentration ratios
    ratios = compute_concentration_ratios(ai_unique)
    print("-" * 65)
    print("TEST 4: Concentration ratios")
    print()
    for _, row in ratios.iterrows():
        t = int(row["threshold_km"])
        print(f"  Within {t} km:")
        print(f"    Cities: {int(row['cities_within'])} ({row['pct_cities']:.1f}%)")
        print(f"    Works:  {int(row['works_within']):,} ({row['pct_works']:.1f}%)")
        print(f"    Excess: +{row['excess_pp']:.1f} percentage points")
        print()

    # Summary
    print("=" * 65)
    print("COPY-PASTE SUMMARY FOR STORYMAP")
    print("=" * 65)
    print()
    print(f"The activity-weighted median distance drops to {obs_wmed:.0f} km,")
    print(f"compared to {np.median(dist):.0f} km in the unweighted view.")
    print(f"Within 500 km, {ratios.iloc[1]['pct_cities']:.0f}% of AI cities")
    print(f"account for {ratios.iloc[1]['pct_works']:.0f}% of all observed AI")
    print(f"works — an excess concentration of {ratios.iloc[1]['excess_pp']:.0f}")
    print(f"percentage points. Within 250 km, {ratios.iloc[0]['pct_cities']:.0f}%")
    print(f"of cities produce {ratios.iloc[0]['pct_works']:.0f}% of works.")
    print()
    print(f"A Spearman rank correlation within the AI-linked sample is")
    print(f"weakly negative (rho = {rho:.3f}, p = {p_s:.2f}), indicating")
    print(f"that once a city is in the AI-producing set, additional")
    print(f"proximity does not strongly predict higher output. A")
    print(f"permutation test on the weighted median is borderline")
    print(f"(p = {perm_p:.3f}). The concentration is driven primarily")
    print(f"by the fact that the largest AI hubs coincide with the")
    print(f"densest compute corridors.")


if __name__ == "__main__":
    main()
