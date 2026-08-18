"""
T-002 -- How often do k-nearest-neighbour spatial weights silently disconnect?

Paper 1 rests on a finding observed in one dataset: the 319-city AI graph at k = 8 splits
into two components (252 and 67), and Getis-Ord Gi* -- which standardises every local
neighbourhood against the GLOBAL mean and standard deviation -- systematically mislabels
the smaller component.

The question this script answers is whether that is a curiosity or a condition analysts
routinely sit in without knowing. It sweeps sample size and k over real city geography,
under two sampling schemes an analyst might plausibly use, and records for every
configuration:

  * how many connected components the weights graph has
  * what share of units the largest component holds
  * how far each component's mean sits from the global mean
  * Gi* hot/cold counts under GLOBAL standardisation (what every tool does)
  * Gi* hot/cold counts under WITHIN-COMPONENT standardisation (the proposed fix)

A finding of "rare" is a perfectly good result and is reported as such. The experiment is
not tuned toward a desired answer.

    python analysis/04_disconnection_prevalence.py

Outputs
    analysis/outputs/disconnection_prevalence.json   full sweep
    papers/paper1/data/prevalence_summary.csv        committed compact summary
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.sparse.csgraph import connected_components

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(ROOT))

from spatialrmt import weights  # noqa: E402
from tools.autocorrelation import (  # noqa: E402
    classify_hotspots, getis_ord_gi_star, global_morans_i,
)

SEED = 42
N_VALUES = (100, 200, 319, 500, 1000, 2000, 5000)
K_VALUES = (3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40)
N_REPLICATES = 20          # independent subsamples per (n, k, scheme)
SCHEMES = ("top_by_population", "random")


# --------------------------------------------------------------------------
def gi_counts(y, W, labels=None):
    """Hot/cold counts. If `labels` given, standardise within each component."""
    if labels is None:
        z = getis_ord_gi_star(y, W)["z"]
    else:
        z = np.zeros(len(y))
        for c in np.unique(labels):
            idx = np.flatnonzero(labels == c)
            if len(idx) < 3:
                continue                     # too small for a variance; leaves z = 0
            sub = W[np.ix_(idx, idx)]
            if sub.sum() == 0 or y[idx].std(ddof=1) == 0:
                continue
            z[idx] = getis_ord_gi_star(y[idx], sub)["z"]
    cls = classify_hotspots(z)
    return (int(np.isin(cls, ["hot_spot_95", "hot_spot_99"]).sum()),
            int(np.isin(cls, ["cold_spot_95", "cold_spot_99"]).sum()))


def analyse(lat, lon, y, k):
    """One configuration: build weights, measure structure and both Gi* variants."""
    W = weights.knn_weights(lat, lon, k, symmetrize=True, transform="binary")
    ncomp, lab = connected_components(W, directed=False)
    sizes = np.bincount(lab)
    n = len(y)

    grand = y.mean()
    offsets = [float(y[lab == c].mean() - grand) for c in range(ncomp)]
    between = sum((lab == c).sum() * (y[lab == c].mean() - grand) ** 2 for c in range(ncomp))
    total = float(((y - grand) ** 2).sum())

    hot_g, cold_g = gi_counts(y, W)
    if ncomp > 1:
        hot_w, cold_w = gi_counts(y, W, labels=lab)
    else:
        hot_w, cold_w = hot_g, cold_g

    return {
        "n": int(n), "k": int(k),
        "n_components": int(ncomp),
        "largest_share": float(sizes.max() / n),
        "n_outside_largest": int(n - sizes.max()),
        "max_abs_offset": float(max(abs(o) for o in offsets)),
        "between_var_share": float(between / total) if total > 0 else 0.0,
        "hot_global": hot_g, "cold_global": cold_g,
        "hot_within": hot_w, "cold_within": cold_w,
        "cold_delta": cold_g - cold_w,
    }


# --------------------------------------------------------------------------
def main() -> None:
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    # ---- reference case: the exact published configuration ----
    ref = pd.read_csv(ROOT / "analysis" / "data" / "ai_cities_319.csv")
    r = analyse(ref.lat.to_numpy(), ref.lon.to_numpy(), ref.log_works.to_numpy(), 8)
    ref_ok = (r["n_components"] == 2 and r["n_outside_largest"] == 67)
    print(f"reference check (319 cities, k=8, real AI works):")
    print(f"  components={r['n_components']} outside largest={r['n_outside_largest']} "
          f"cold {r['cold_global']} -> {r['cold_within']}   "
          f"{'MATCHES 252/67' if ref_ok else 'DOES NOT MATCH -- investigate'}")
    if not ref_ok:
        raise SystemExit("reference configuration did not reproduce; aborting")

    # ---- the sweep, on the full 41k-city frame ----
    wc = pd.read_csv(ROOT / "eip" / "data" / "raw" / "worldcities.csv")
    wc = wc.dropna(subset=["lat", "lng", "population"])
    wc = wc[wc.population > 0].reset_index(drop=True)
    wc["logpop"] = np.log1p(wc.population.to_numpy())
    print(f"\nframe: {len(wc):,} cities with coordinates and population")
    print(f"sweep: {len(N_VALUES)}x{len(K_VALUES)}x{len(SCHEMES)}x{N_REPLICATES} "
          f"= {len(N_VALUES)*len(K_VALUES)*len(SCHEMES)*N_REPLICATES:,} configurations\n")

    by_pop = wc.sort_values("population", ascending=False).reset_index(drop=True)
    rows = []
    for scheme in SCHEMES:
        for n in N_VALUES:
            for rep in range(N_REPLICATES if scheme == "random" else 1):
                # top-by-population is deterministic, so one replicate suffices
                if scheme == "top_by_population":
                    sub = by_pop.iloc[:n]
                else:
                    sub = wc.iloc[rng.choice(len(wc), n, replace=False)]
                lat = sub.lat.to_numpy(); lon = sub.lng.to_numpy()
                y = sub.logpop.to_numpy()
                for k in K_VALUES:
                    if k >= n:
                        continue
                    d = analyse(lat, lon, y, k)
                    d["scheme"] = scheme; d["replicate"] = rep
                    rows.append(d)
            print(f"  {scheme:18s} n={n:5d} done ({time.time()-t0:.0f}s)")

    df = pd.DataFrame(rows)

    # ---- headline prevalence ----
    print("\n" + "=" * 74)
    print("PREVALENCE OF SILENT DISCONNECTION")
    print("=" * 74)
    overall = (df.n_components > 1).mean()
    print(f"  configurations that disconnect: {overall:.1%} of {len(df):,}\n")

    piv = df.pivot_table(index="k", columns="n", values="n_components",
                         aggfunc=lambda s: (s > 1).mean())
    print("  fraction disconnected, by k (rows) and n (cols):")
    print(piv.map(lambda v: f"{v:.0%}").to_string())

    print("\n  by sampling scheme:")
    for s in SCHEMES:
        m = df.scheme == s
        print(f"    {s:18s} {(df[m].n_components > 1).mean():.1%} "
              f"(median components when split: "
              f"{df[m & (df.n_components > 1)].n_components.median():.0f})")

    dis = df[df.n_components > 1]
    if len(dis):
        print("\n" + "=" * 74)
        print("CONSEQUENCE WHEN IT HAPPENS")
        print("=" * 74)
        print(f"  units outside the largest component: median "
              f"{dis.n_outside_largest.median():.0f} "
              f"({(1-dis.largest_share).median():.1%} of the sample)")
        print(f"  between-component share of variance: median "
              f"{dis.between_var_share.median():.2%}")
        chg = dis[dis.cold_delta != 0]
        print(f"  cold-spot count changes under the fix in "
              f"{len(chg)/len(dis):.1%} of disconnected configurations")
        print(f"  when it changes, median change: {chg.cold_delta.median():+.0f} "
              f"(global standardisation reports MORE cold spots when positive)")

    # ---- persist ----
    out = ROOT / "analysis" / "outputs"; out.mkdir(parents=True, exist_ok=True)
    pdir = ROOT / "papers" / "paper1" / "data"; pdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "disconnection_prevalence_full.csv", index=False)

    summary = {
        "seed": SEED, "n_configurations": int(len(df)),
        "reference_319_k8": r,
        "reference_reproduces": bool(ref_ok),
        "overall_disconnect_rate": float(overall),
        "by_scheme": {s: float((df[df.scheme == s].n_components > 1).mean()) for s in SCHEMES},
        "by_k": {int(k): float((g.n_components > 1).mean()) for k, g in df.groupby("k")},
        "by_n": {int(n): float((g.n_components > 1).mean()) for n, g in df.groupby("n")},
        "when_disconnected": ({
            "median_units_outside_largest": float(dis.n_outside_largest.median()),
            "median_share_outside_largest": float((1 - dis.largest_share).median()),
            "median_between_var_share": float(dis.between_var_share.median()),
            "frac_cold_count_changes": float((dis.cold_delta != 0).mean()),
            "median_cold_delta_when_changed": float(dis[dis.cold_delta != 0].cold_delta.median()),
        } if len(dis) else None),
    }
    (out / "disconnection_prevalence.json").write_text(json.dumps(summary, indent=2),
                                                       encoding="utf-8")
    piv.to_csv(pdir / "prevalence_by_n_k.csv")
    df.groupby(["scheme", "n", "k"]).agg(
        disconnect_rate=("n_components", lambda s: (s > 1).mean()),
        median_components=("n_components", "median"),
        median_cold_delta=("cold_delta", "median"),
    ).reset_index().to_csv(pdir / "prevalence_summary.csv", index=False)

    print(f"\nwrote analysis/outputs/disconnection_prevalence.json")
    print(f"wrote papers/paper1/data/prevalence_summary.csv")
    print(f"elapsed {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
