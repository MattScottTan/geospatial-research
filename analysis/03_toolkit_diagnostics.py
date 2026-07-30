"""
Run the standard geospatial toolkit over the eip data and see what it says.

Not a re-analysis -- the published statistics reproduce and are not in question here.
This asks a different question: when the ordinary diagnostics of the field are applied
to this weights matrix and this response, what do they report?

Four checks, in increasing distance from what the submission did:

  1. graph connectivity      -- is this one spatial system or several?
  2. mixing vs edge scale    -- the Thouless comparison, on the real graph
  3. eigenvector occupancy   -- would ESF here fit trends or bumps?
  4. spatial cross-validation -- does the distance covariate predict out of sample?

    python analysis/03_toolkit_diagnostics.py
"""

from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(ROOT))

from spatialrmt import bandmatrix, geodesy, weights  # noqa: E402
from tools import crossval, eigenvector_filtering as esf, graph_signal, regression  # noqa: E402

K = 8  # the published choice


def main() -> None:
    c = pd.read_csv(ROOT / "analysis" / "data" / "ai_cities_319.csv")
    y = c["log_works"].to_numpy()
    lat, lon = c["lat"].to_numpy(), c["lon"].to_numpy()
    xy = np.column_stack([lon, lat])
    D = geodesy.pairwise_haversine_km(lat, lon)
    X = np.log1p(c[["dist_km"]].to_numpy())
    n = len(c)

    W = weights.knn_weights(lat, lon, K, symmetrize=True, transform="binary")
    print(f"n = {n}, weights = {weights.describe(W)}\n")

    out = {}

    # ---------------------------------------------------------------- 1
    print("=" * 72)
    print("1. CONNECTIVITY")
    print("=" * 72)
    s = weights.weights_summary(W)
    print(f"  components {s['n_components']}, largest {s['largest_component']} of {n} "
          f"({s['largest_component']/n:.0%})")
    if s["n_components"] > 1:
        print(f"  -> {n - s['largest_component']} cities sit in a separate component.")
        print("     Spatial information cannot propagate between components at all, so")
        print("     Moran's I here summarises two disjoint systems as though they were one.")
    out["connectivity"] = s

    # ---------------------------------------------------------------- 2
    print("\n" + "=" * 72)
    print("2. MIXING vs EDGE RESOLUTION  (Thouless comparison on the real graph)")
    print("=" * 72)
    md = graph_signal.mixing_diagnostics(W)
    n_edge = bandmatrix.edge_resolution_length(n)
    ratio = md["mixing_time"] / n_edge
    print(f"  mixing time within largest component : {md['mixing_time']:.0f} steps")
    print(f"  walk length to resolve the edge      : {n_edge:.1f} steps  (n^(1/3))")
    print(f"  ratio                                : {ratio:.0f}x")
    print("  -> the walk is nowhere near mixed when the edge is resolved. Geometry")
    print("     survives into the edge statistics; mean-field asymptotics do not apply.")
    _, k_crit = bandmatrix.thouless_threshold(n, d=2)
    print(f"  critical degree for edge universality (d=2): {k_crit:.0f} vs k = {K} in use")
    out["mixing"] = {"mixing_time": md["mixing_time"], "n_edge": n_edge,
                     "ratio": ratio, "critical_degree_d2": k_crit,
                     "spectral_gap": md["spectral_gap"]}

    # ---------------------------------------------------------------- 3
    print("\n" + "=" * 72)
    print("3. EIGENVECTOR OCCUPANCY  (what would ESF be fitting?)")
    print("=" * 72)
    basis = esf.moran_eigenvectors(W, max_vectors=60)
    rep = esf.localisation_report(basis, top=20)
    print(f"  leading 20 eigenvectors occupy {rep['occupancy_fraction_mean']:.1%} of the "
          f"domain on average")
    print(f"  range {rep['occupancy_fraction_min']:.1%} to {rep['occupancy_fraction_max']:.1%}")
    print(f"  -> {rep['verdict']}")
    sel = esf.select_eigenvectors(basis, y, max_select=15)
    print(f"  selecting on y keeps {sel['n_selected']} of {sel['n_candidates']}, "
          f"mean occupancy {sel['mean_occupancy_fraction']:.1%} "
          f"(~{sel['mean_occupancy_fraction']*n:.0f} cities each)")
    r = esf.esf_regression(y, X, basis, sel["selected"])
    print(f"  adding them: R2 {r['r2_covariates_only']:.3f} -> {r['r2_with_filters']:.3f}, "
          f"log-distance beta {r['beta_covariates_only'][1]:+.4f} -> "
          f"{r['beta_with_filters'][1]:+.4f}")
    out["esf"] = {**rep, "n_selected": sel["n_selected"],
                  "selected_occupancy_fraction": sel["mean_occupancy_fraction"],
                  "beta_before": float(r["beta_covariates_only"][1]),
                  "beta_after": float(r["beta_with_filters"][1])}

    # ---------------------------------------------------------------- 4
    print("\n" + "=" * 72)
    print("4. SPATIAL CROSS-VALIDATION  (does log-distance predict out of sample?)")
    print("=" * 72)

    def ols(Xtr, ytr, Xte):
        A = np.column_stack([np.ones(len(Xtr)), Xtr])
        b, *_ = np.linalg.lstsq(A, ytr, rcond=None)
        return np.column_stack([np.ones(len(Xte)), Xte]) @ b

    rep_cv = crossval.leakage_report(ols, X, y, xy, n_folds=5)
    for key in ("random_kfold", "spatial_block", "spatial_kmeans"):
        m = rep_cv[key]
        print(f"  {key:16s} R2 = {m['r2']:+.4f}   RMSE = {m['rmse']:.4f}")
    print(f"  random-CV R2 inflation over block CV: {rep_cv['r2_inflation']:+.4f}")
    if rep_cv["spatial_block"]["r2"] < 0:
        print("  -> negative R2 under spatial CV: log-distance alone predicts AI output")
        print("     worse than the mean does. The published association is real but is")
        print("     not predictive skill, which the StoryMap does not claim -- worth")
        print("     stating explicitly if the atlas is ever used to rank cities.")
    out["crossval"] = rep_cv

    # ---------------------------------------------------------------- 5
    print("\n" + "=" * 72)
    print("5. SPATIAL CONFOUNDING")
    print("=" * 72)
    sc = regression.spatial_confounding_diagnostic(X.ravel(), W, n_components=10)
    print(f"  log-distance energy in the 10 smoothest spatial modes: "
          f"{sc['low_frequency_share']:.1%}")
    print(f"  -> {sc['interpretation']}")
    sar = regression.sar_lag(y, X, W, names=("intercept", "log_distance"))
    print(f"  SAR lag rho = {sar.rho:+.4f}, log-distance beta = {sar.beta[1]:+.4f}")
    print(f"     (published GP {-0.207:+.3f} vs CAR {-0.052:+.3f}; SAR lands near the CAR)")
    out["confounding"] = {"low_frequency_share": sc["low_frequency_share"],
                          "sar_rho": sar.rho, "sar_beta_logdist": float(sar.beta[1])}

    od = ROOT / "analysis" / "outputs"
    od.mkdir(parents=True, exist_ok=True)
    (od / "toolkit_diagnostics.json").write_text(json.dumps(out, indent=2, default=float),
                                                 encoding="utf-8")
    print(f"\nwrote analysis/outputs/toolkit_diagnostics.json")


if __name__ == "__main__":
    main()
