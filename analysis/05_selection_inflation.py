"""
T-003 -- How much does choosing k inflate the false-positive rate?

Moran's I answers "is this map spatially patterned?" But to ask whether *neighbours*
resemble each other you must first say who counts as a neighbour, and that choice -- k --
is made by the analyst. The spatial statistics literature openly describes selecting the
weights matrix by maximising Moran's I. The resulting p-value is then reported as though
k had been fixed in advance. It was not.

This script measures the damage as a surface rather than a point: across selection rules,
candidate grids, and sample sizes, how often does a map with NO spatial structure at all
produce a "significant" result?

Four selection rules, chosen to span what analysts actually do:

  union      reject if ANY k in the grid reaches significance
  argmax     pick the k maximising Moran's I, test only that one
  first_sig  scan k upward, stop at the first significant one
  majority   reject only if MORE THAN HALF the grid agrees -- the "robustness check"
             a careful practitioner believes protects them

The gap between observed inflation and the Bonferroni bound is explained by the
correlation between the statistics on a grid: they are computed from the same data with
overlapping neighbourhoods, so the grid buys fewer independent looks than its size.

    python analysis/05_selection_inflation.py

Outputs
    analysis/outputs/selection_inflation.json      full surface
    papers/paper2/data/inflation_surface.csv       committed compact summary
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(ROOT))

from spatialrmt import weights  # noqa: E402

SEED = 42
B = 20000                 # replicates; MC SE at rate 0.14 is ~0.25 percentage points
CHUNK = 2000              # replicate block size, to bound memory
ALPHA = 0.05

GRIDS = {
    "coarse":  (4, 8, 16, 32),
    "fine":    (4, 6, 8, 10, 12, 16, 20),
    "wide":    (2, 3, 4, 6, 8, 12, 20, 32, 64),
    "narrow":  (6, 8, 10),
    "standard": (4, 6, 8, 12, 20, 40),      # the reference grid
}
N_VALUES = (200, 500, 1000)


def moran_matrix(Ws, S0, n, rng, B, chunk):
    """
    Null distribution of Moran's I for every k, vectorised over replicates.

    Returns (B, n_k). Data are iid standard normal on fixed locations -- no spatial
    structure whatsoever -- so any rejection is by construction a false positive.
    """
    ks = list(Ws)
    out = np.empty((B, len(ks)))
    done = 0
    while done < B:
        m = min(chunk, B - done)
        Y = rng.standard_normal((n, m))
        Z = Y - Y.mean(axis=0, keepdims=True)
        den = (Z * Z).sum(axis=0)
        for j, k in enumerate(ks):
            WZ = Ws[k] @ Z
            out[done:done + m, j] = (n / S0[k]) * (Z * WZ).sum(axis=0) / den
        done += m
    return out


def apply_rules(I, q):
    """
    Rejection indicator per replicate for each selection rule.
    `q` is the per-k critical value, so every individual k has exactly 5% Type I error
    by construction -- the inflation comes only from choosing among them.
    """
    exceed = I > q
    B_, K = I.shape
    rows = np.arange(B_)
    argmax = exceed[rows, I.argmax(axis=1)]
    first = exceed.argmax(axis=1)                       # index of first True (0 if none)
    first_sig = exceed[rows, first] & exceed.any(axis=1)
    majority = exceed.sum(axis=1) > (K / 2.0)
    return {
        "union": exceed.any(axis=1),
        "argmax": argmax,
        "first_sig": first_sig,
        "majority": majority,
    }


def main() -> None:
    t0 = time.time()
    cities = pd.read_csv(ROOT / "analysis" / "data" / "ai_cities_319.csv")
    wc = pd.read_csv(ROOT / "eip" / "data" / "raw" / "worldcities.csv").dropna(subset=["lat", "lng"])

    print(f"null simulation: {B:,} replicates per configuration, iid noise, no spatial structure")
    print(f"Monte Carlo SE at rate p is sqrt(p(1-p)/B); at p=0.14 that is "
          f"{np.sqrt(0.14*0.86/B)*100:.2f} percentage points\n")

    rows = []
    master = np.random.default_rng(SEED)

    # ---- reference configuration first, as a correctness check ----
    lat, lon = cities.lat.to_numpy(), cities.lon.to_numpy()
    ks = GRIDS["standard"]
    Ws = {k: weights.knn_weights(lat, lon, k, symmetrize=True, transform="binary") for k in ks}
    S0 = {k: float(Ws[k].sum()) for k in ks}
    I = moran_matrix(Ws, S0, len(lat), np.random.default_rng(SEED), B, CHUNK)
    q = np.quantile(I, 1 - ALPHA, axis=0)
    ref = apply_rules(I, q)
    corr = np.corrcoef(I.T)[np.triu_indices(len(ks), 1)].mean()
    print("reference check (319 AI cities, standard grid):")
    print(f"  union {ref['union'].mean():.1%} (expect 14.4%)   "
          f"argmax {ref['argmax'].mean():.1%} (expect 11.4%)   "
          f"mean corr {corr:.3f} (expect 0.605)")
    ok = abs(ref["union"].mean() - 0.144) < 0.01 and abs(corr - 0.605) < 0.02
    print(f"  {'REPRODUCES' if ok else 'DOES NOT REPRODUCE -- investigate'}\n")

    # ---- the surface ----
    for gname, grid in GRIDS.items():
        for n in N_VALUES:
            sub = wc.iloc[master.choice(len(wc), n, replace=False)]
            la, lo = sub.lat.to_numpy(), sub.lng.to_numpy()
            gk = tuple(k for k in grid if k < n)
            Ws = {k: weights.knn_weights(la, lo, k, symmetrize=True, transform="binary") for k in gk}
            S0 = {k: float(Ws[k].sum()) for k in gk}
            I = moran_matrix(Ws, S0, n, np.random.default_rng(SEED + n), B, CHUNK)
            q = np.quantile(I, 1 - ALPHA, axis=0)
            res = apply_rules(I, q)
            c = np.corrcoef(I.T)[np.triu_indices(len(gk), 1)].mean()
            bonf = 1 - (1 - ALPHA) ** len(gk)
            for rule, rej in res.items():
                r = float(rej.mean())
                rows.append({
                    "grid": gname, "grid_size": len(gk), "n": n, "rule": rule,
                    "type_I": r, "inflation": r / ALPHA,
                    "mean_corr": float(c), "bonferroni_bound": float(bonf),
                    "mc_se": float(np.sqrt(r * (1 - r) / B)),
                })
            print(f"  {gname:9s} n={n:5d} |grid|={len(gk)} corr={c:.3f}  " +
                  "  ".join(f"{k}={v.mean():.1%}" for k, v in res.items()))

    df = pd.DataFrame(rows)

    print("\n" + "=" * 78)
    print("TYPE I ERROR BY SELECTION RULE  (nominal 5.0%)")
    print("=" * 78)
    print(df.pivot_table(index=["grid", "grid_size"], columns="rule", values="type_I")
            .map(lambda v: f"{v:.1%}").to_string())

    print("\n" + "=" * 78)
    print("HEADLINES")
    print("=" * 78)
    for rule in ("union", "argmax", "first_sig", "majority"):
        s = df[df.rule == rule]
        print(f"  {rule:10s} {s.type_I.min():.1%} to {s.type_I.max():.1%}   "
              f"(inflation {s.inflation.min():.1f}x to {s.inflation.max():.1f}x)")
    print(f"\n  max MC standard error across all cells: {df.mc_se.max()*100:.2f} pp")
    u = df[df.rule == "union"]
    print(f"  union inflation grows with grid size: " +
          ", ".join(f"|{g}|={gs}: {v:.1%}" for g, gs, v in
                    u.groupby(["grid", "grid_size"]).type_I.mean().reset_index()
                     .sort_values("grid_size")[["grid", "grid_size", "type_I"]].values))
    print(f"\n  observed union rate vs Bonferroni bound (the gap the correlation explains):")
    for _, r in u.groupby(["grid", "grid_size"]).agg(
            obs=("type_I", "mean"), bonf=("bonferroni_bound", "first"),
            corr=("mean_corr", "mean")).reset_index().sort_values("grid_size").iterrows():
        print(f"    {r['grid']:9s} |grid|={int(r['grid_size'])}  observed {r['obs']:.1%}  "
              f"Bonferroni {r['bonf']:.1%}  mean corr {r['corr']:.3f}")

    out = ROOT / "analysis" / "outputs"; out.mkdir(parents=True, exist_ok=True)
    pdir = ROOT / "papers" / "paper2" / "data"; pdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(pdir / "inflation_surface.csv", index=False)
    (out / "selection_inflation.json").write_text(json.dumps({
        "seed": SEED, "replicates": B, "alpha": ALPHA,
        "reference": {"union": float(ref["union"].mean()), "argmax": float(ref["argmax"].mean()),
                      "mean_corr": float(corr), "reproduces": bool(ok)},
        "max_mc_se": float(df.mc_se.max()),
        "by_rule": {r: {"min": float(g.type_I.min()), "max": float(g.type_I.max())}
                    for r, g in df.groupby("rule")},
        "surface": df.to_dict(orient="records"),
    }, indent=2), encoding="utf-8")
    print(f"\nwrote analysis/outputs/selection_inflation.json")
    print(f"wrote papers/paper2/data/inflation_surface.csv")
    print(f"elapsed {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
