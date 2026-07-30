"""
How much does the weights specification decide the answer?

The eip submission's Gi* map depends on two choices its methods document never stated:
whether the kNN graph is symmetrized, and whether rows are standardised. This
generalises that observation into a sweep -- vary k and the specification, hold the data
fixed, and watch which statistics move.

The prediction from theory/README.md is that they should move differently. Moran's I is
a degree-2 spectral functional, so it should be stable: low-order spectral moments are
geometry-blind. The Gi* classifications are an extreme-value question, and the tail is
where the specification lives, so they should not be.

    python analysis/01_weights_sensitivity.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(ROOT))

from spatialrmt import bandmatrix, weights  # noqa: E402
from tools.autocorrelation import (  # noqa: E402
    classify_hotspots, getis_ord_gi_star, global_morans_i, hotspot_counts,
)

DATA = ROOT / "analysis" / "data" / "ai_cities_319.csv"
OUT = ROOT / "analysis" / "outputs"
K_VALUES = (4, 6, 8, 12, 20, 40)
SPECS = (
    ("directed",    "binary", dict(symmetrize=False, transform="binary")),
    ("directed",    "row",    dict(symmetrize=False, transform="row")),
    ("symmetrized", "binary", dict(symmetrize=True,  transform="binary")),
    ("symmetrized", "row",    dict(symmetrize=True,  transform="row")),
)


def main() -> None:
    cities = pd.read_csv(DATA)
    y = cities["log_works"].to_numpy()
    lat, lon = cities["lat"].to_numpy(), cities["lon"].to_numpy()
    n = len(cities)

    print(f"n = {n} cities, log_works mean {y.mean():.3f} sd {y.std(ddof=1):.3f}")
    print("published (k=8, symmetrized binary): I = 0.066, p = 0.008, 7 hot / 33 cold\n")

    rows = []
    for k in K_VALUES:
        for sym, tr, kw in SPECS:
            W = weights.knn_weights(lat, lon, k, **kw)
            mi = global_morans_i(y, W, n_permutations=999, seed=42)
            gi = getis_ord_gi_star(y, W)
            hc = hotspot_counts(classify_hotspots(gi["z"]))
            rows.append({
                "k": k, "symmetry": sym, "transform": tr,
                "I": mi.I, "p": mi.p_value, "z": mi.z_score,
                "hot": hc["hot"], "cold": hc["cold"],
                "mean_degree": weights.weights_summary(W)["degree_mean"],
            })

    df = pd.DataFrame(rows)

    print("=" * 74)
    print("MORAN'S I")
    print("=" * 74)
    print(df.pivot_table(index="k", columns=["symmetry", "transform"], values="I")
            .round(4).to_string())

    print("\n" + "=" * 74)
    print("Gi* SIGNIFICANT UNITS  (hot + cold, out of %d)" % n)
    print("=" * 74)
    df["sig"] = df["hot"] + df["cold"]
    print(df.pivot_table(index="k", columns=["symmetry", "transform"], values="sig")
            .astype(int).to_string())

    # ---- decompose: specification effect (within k) vs scale effect (across k) ----
    # These are different questions and must not be pooled. Varying k changes the
    # estimand -- a wider neighbourhood genuinely averages over more distant units, so
    # I is expected to decay. Varying symmetry/transform at fixed k does not change the
    # question being asked, so any movement there is specification artifact.
    def rel_spread(g, col):
        return (g[col].max() - g[col].min()) / g[col].mean() if g[col].mean() else np.nan

    within = df.groupby("k").apply(
        lambda g: pd.Series({"I_spread": rel_spread(g, "I"), "sig_spread": rel_spread(g, "sig")}),
        include_groups=False,
    )
    across_I = (df.groupby("k")["I"].mean().max() - df.groupby("k")["I"].mean().min()) \
        / df["I"].mean()

    print("\n" + "=" * 74)
    print("SENSITIVITY  (relative spread = range / mean)")
    print("=" * 74)
    print("  within k -- symmetry and transform only, question unchanged:")
    print(f"{'':6s}{'k':>6s} {'I':>10s} {'Gi* flagged':>14s}")
    for k, r in within.iterrows():
        print(f"{'':6s}{k:6d} {r['I_spread']:9.1%} {r['sig_spread']:13.1%}")
    print(f"\n    median   I {within['I_spread'].median():.1%}"
          f"     Gi* {within['sig_spread'].median():.1%}")
    print(f"\n  across k -- neighbourhood scale, estimand genuinely changes:")
    print(f"    Moran's I mean over specs falls {df.groupby('k')['I'].mean().max():.4f}"
          f" (k={df.groupby('k')['I'].mean().idxmax()}) -> "
          f"{df.groupby('k')['I'].mean().min():.4f}"
          f" (k={df.groupby('k')['I'].mean().idxmin()}), "
          f"relative range {across_I:.0%}")

    sig_frac = (df["p"] < 0.05).mean()
    print(f"\n  Moran's I significant at 0.05 in {sig_frac:.0%} of all (k, spec) combinations")

    # ---- the published k sits where? ----
    by_k = df.groupby("k")["I"].mean()
    print(f"\n  Moran's I by k: " + "  ".join(f"k={k}:{v:.4f}" for k, v in by_k.items()))
    if by_k.idxmax() == 8:
        print("    the published k = 8 is the arg-max of I over the k sweep.")
        print("    If k was chosen by inspecting I, the reported p-value is a selective")
        print("    one and the permutation null does not account for that choice.")

    # ---- where these weights sit relative to edge universality ----
    print("\n" + "=" * 74)
    print("THOULESS REGIME  (d = 2)")
    print("=" * 74)
    _, k_crit = bandmatrix.thouless_threshold(n, d=2)
    print(f"  critical degree for edge universality at n={n}: {k_crit:.0f}")
    for k in K_VALUES:
        r = bandmatrix.classify_regime(n, k, d=2)
        print(f"  k = {k:3d}   ratio {r.ratio:6.3f}   {r.regime}")

    OUT.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT / "weights_sensitivity.csv", index=False)
    (OUT / "weights_sensitivity_summary.json").write_text(json.dumps({
        "n": n,
        "within_k_spread_median": {
            "moran_I": float(within["I_spread"].median()),
            "gi_flagged": float(within["sig_spread"].median()),
        },
        "across_k_relative_range_moran_I": float(across_I),
        "moran_significant_fraction": float(sig_frac),
        "moran_I_by_k": {int(k): float(v) for k, v in by_k.items()},
        "argmax_k": int(by_k.idxmax()),
        "thouless_critical_degree_d2": float(k_crit),
    }, indent=2), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}/weights_sensitivity.csv")


if __name__ == "__main__":
    main()
