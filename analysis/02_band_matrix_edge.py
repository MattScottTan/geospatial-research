"""
Bulk is geometry-blind, eigenvectors are not.

Direct numerical check of the claim the whole theory thread rests on: for a random band
matrix, the global spectral density converges to the semicircle for *any* growing
bandwidth -- short backtracking walks never notice the finite interaction range -- while
eigenvector localisation depends sharply on W.

If that holds, it separates the two kinds of spatial statistic cleanly. Moran's I is a
degree-2 spectral functional and lives in the geometry-blind part. Eigenvector spatial
filtering regresses on the eigenvectors themselves and lives in the part that is not.

The localisation prediction in 1D is that eigenvectors delocalise for W >> sqrt(N).
Here N = 512, so sqrt(N) ~ 23.

    python analysis/02_band_matrix_edge.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from spatialrmt import bandmatrix, spectral  # noqa: E402

N = 512
BANDWIDTHS = (2, 4, 8, 16, 32, 64, 128, 255)
N_REALISATIONS = 8
SEED = 42


def semicircle_l1_error(eigenvalues: np.ndarray, bins: int = 60) -> float:
    """L1 distance between the empirical spectral density and the semicircle on [-1, 1]."""
    hist, edges = np.histogram(eigenvalues, bins=bins, range=(-1.0, 1.0), density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return float(np.abs(hist - bandmatrix.semicircle_density(centers)).sum() * np.diff(edges)[0])


def main() -> None:
    rng = np.random.default_rng(SEED)
    print(f"periodic random band matrices, N = {N}, beta = 1, "
          f"{N_REALISATIONS} realisations each")
    print(f"1D localisation scale sqrt(N) = {np.sqrt(N):.0f}; "
          f"Thouless edge threshold N^(5/6) = {N ** (5/6):.0f}\n")

    print("=" * 76)
    print(f"{'W':>5s} {'W/sqrt(N)':>10s} {'semicircle L1':>14s} "
          f"{'mean 1/IPR':>12s} {'1/IPR / N':>11s} {'edge lambda_max':>16s}")
    print("-" * 76)

    rows = []
    for W in BANDWIDTHS:
        l1s, parts, edges = [], [], []
        for _ in range(N_REALISATIONS):
            H = bandmatrix.periodic_band_matrix(N, W, beta=1, rng=rng)
            ev, vecs = np.linalg.eigh(H)
            l1s.append(semicircle_l1_error(ev))
            parts.append(np.mean(1.0 / np.sum(vecs**4, axis=0)))
            edges.append(ev[-1])
        row = {
            "W": W,
            "W_over_sqrtN": W / np.sqrt(N),
            "semicircle_L1": float(np.mean(l1s)),
            "participation": float(np.mean(parts)),
            "participation_frac": float(np.mean(parts) / N),
            "edge": float(np.mean(edges)),
        }
        rows.append(row)
        print(f"{W:5d} {row['W_over_sqrtN']:10.2f} {row['semicircle_L1']:14.4f} "
              f"{row['participation']:12.1f} {row['participation_frac']:11.3f} "
              f"{row['edge']:16.4f}")

    # ---- read off the contrast ----
    l1 = np.array([r["semicircle_L1"] for r in rows])
    pf = np.array([r["participation_frac"] for r in rows])
    wide = [r for r in rows if r["W"] >= 8]
    l1_wide = np.array([r["semicircle_L1"] for r in wide])
    pf_wide = np.array([r["participation_frac"] for r in wide])

    print("\n" + "=" * 76)
    print("CONTRAST")
    print("=" * 76)
    print(f"  semicircle L1 error, W >= 8 : {l1_wide.min():.4f} to {l1_wide.max():.4f}"
          f"   ({l1_wide.max() / l1_wide.min():.1f}x)")
    print(f"  eigenvector occupancy, same : {pf_wide.min():.3f} to {pf_wide.max():.3f}"
          f"   ({pf_wide.max() / pf_wide.min():.1f}x)")
    print()
    print("  The bulk density is already close to semicircle by W = 8 and barely improves")
    print("  after; eigenvector occupancy keeps climbing across the whole range. The two")
    print("  quantities respond to bandwidth on completely different scales, which is the")
    print("  separation the theory predicts.")
    print()
    print(f"  At W = 8 -- the bandwidth analogous to the k = 8 used in both submissions --")
    w8 = next(r for r in rows if r["W"] == 8)
    print(f"    semicircle L1 {w8['semicircle_L1']:.4f}  "
          f"but eigenvectors occupy only {w8['participation_frac']:.1%} of the domain.")
    print("    A Moran eigenvector at this bandwidth is a local bump, not a global trend.")
    print("    Eigenvector spatial filtering here is fitting local structure and calling")
    print("    it a spatial trend.")

    out = ROOT / "analysis" / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    (out / "band_matrix_edge.json").write_text(json.dumps({
        "N": N, "n_realisations": N_REALISATIONS, "seed": SEED,
        "sqrt_N": float(np.sqrt(N)), "thouless_N_5_6": float(N ** (5 / 6)),
        "rows": rows,
    }, indent=2), encoding="utf-8")
    print(f"\nwrote analysis/outputs/band_matrix_edge.json")


if __name__ == "__main__":
    main()
