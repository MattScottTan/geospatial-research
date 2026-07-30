"""
Port of compute-atlas Finding 3 (Global Moran's I + Getis-Ord Gi*) to esda/libpysal.

Background
----------
The published StoryMap attributes these statistics to the ArcGIS Pro Spatial Statistics
toolbox, and `submission/award-materials/methods/SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md` specifies
"K Nearest Neighbors, K = 8, Row standardization". But the shipped pipeline
(`code/pipeline.py`) computes both statistics itself in numpy/scipy, using a
*binary symmetrized* kNN adjacency -- it never row-standardises.

This script reproduces the pipeline result, then re-runs the same data through esda
under both weighting schemes so the effect of that choice is visible.

Reference values
----------------
StoryMap:  I = 0.066, z = 2.86, p = 0.008, n = 319
           Gi*: 7 hot spots, 33 cold spots (1 hot at 99%, Macau)
Shipped:   data/gis/cities_with_hotspots.geojson carries gi_star_z / hotspot_class

Usage
-----
    python analysis/spatial_diagnostics_esda.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.spatial import cKDTree
from scipy.stats import norm

from libpysal.weights import W as PysalW
from esda.moran import Moran

K_NN = 8
N_PERM = 999
SEED = 42

ROOT = Path(__file__).resolve().parents[1]
CITY_CSV = ROOT / "data" / "raw" / "city_access_ai.csv"
HOTSPOT_GEOJSON = ROOT / "data" / "gis" / "cities_with_hotspots.geojson"


# --------------------------------------------------------------------------
# Data: collapse the 328 OpenAlex matches to 319 unique cities, as the
# pipeline's aggregate_ai_city_matches() does (sum works, then log1p).
# --------------------------------------------------------------------------
def load_unique_cities() -> pd.DataFrame:
    df = pd.read_csv(CITY_CSV)
    grouped = (
        df.groupby("id", dropna=False)
        .agg(
            city=("city", "first"),
            country=("country", "first"),
            lat=("lat", "first"),
            lng=("lng", "first"),
            works=("openalex_ai_works_recent", "sum"),
        )
        .reset_index()
    )
    grouped["log_ai_works"] = np.log1p(grouped["works"])
    return grouped


# --------------------------------------------------------------------------
# Weights
# --------------------------------------------------------------------------
def _to_xyz(lat: np.ndarray, lon: np.ndarray) -> np.ndarray:
    lat_r, lon_r = np.radians(lat), np.radians(lon)
    return np.column_stack(
        [np.cos(lat_r) * np.cos(lon_r), np.cos(lat_r) * np.sin(lon_r), np.sin(lat_r)]
    )


def knn_adjacency(lat, lon, k=K_NN, symmetrize=True) -> csr_matrix:
    """Binary kNN adjacency on the unit sphere. Mirrors pipeline.build_knn_graph."""
    xyz = _to_xyz(lat, lon)
    _, idx = cKDTree(xyz).query(xyz, k=k + 1)
    n = len(lat)
    rows = np.repeat(np.arange(n), k)
    cols = idx[:, 1:].reshape(-1)  # drop self
    W = csr_matrix((np.ones_like(rows, dtype=float), (rows, cols)), shape=(n, n))
    if symmetrize:
        W = ((W + W.T) > 0).astype(float).tocsr()
    return W


def row_standardize(W: csr_matrix) -> csr_matrix:
    rs = np.asarray(W.sum(axis=1)).ravel()
    rs[rs == 0] = 1.0
    return csr_matrix(W.multiply(1.0 / rs[:, None]))


def to_pysal(W: csr_matrix) -> PysalW:
    """Convert a sparse matrix to a libpysal W without re-transforming it."""
    Wc = W.tocsr()
    neighbors, weights = {}, {}
    for i in range(Wc.shape[0]):
        s, e = Wc.indptr[i], Wc.indptr[i + 1]
        neighbors[i] = Wc.indices[s:e].tolist()
        weights[i] = Wc.data[s:e].tolist()
    out = PysalW(neighbors, weights, silence_warnings=True)
    out.transform = "O"  # keep our weights exactly as supplied
    return out


# --------------------------------------------------------------------------
# The pipeline's own estimators, reimplemented verbatim for comparison
# --------------------------------------------------------------------------
def pipeline_moran(values, W, n_permutations=499, seed=SEED) -> dict:
    x = np.asarray(values, float)
    c = x - x.mean()
    denom = float(c @ c)
    s0 = float(W.sum())
    n = len(x)
    observed = float((n / s0) * (c @ np.asarray(W @ c).ravel()) / denom)

    rng = np.random.default_rng(seed)
    perm = np.empty(n_permutations)
    for i in range(n_permutations):
        p = rng.permutation(c)
        perm[i] = float((n / s0) * (p @ np.asarray(W @ p).ravel()) / denom)

    sd = float(perm.std(ddof=1))
    return {
        "I": observed,
        "z": (observed - perm.mean()) / sd,
        "p_two_sided": (np.count_nonzero(np.abs(perm) >= abs(observed)) + 1)
        / (n_permutations + 1),
    }


def pipeline_gi_star(values, W) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(values, float)
    n = len(x)
    Ws = W.copy().tolil()
    Ws.setdiag(1.0)  # Gi* includes self
    Ws = Ws.tocsr()

    mean_x, std_x = float(x.mean()), float(x.std(ddof=1))
    sw = np.asarray(Ws.sum(axis=1)).ravel()
    sw2 = np.asarray(Ws.power(2).sum(axis=1)).ravel()
    numer = np.asarray(Ws @ x).ravel() - mean_x * sw
    denom = std_x * np.sqrt(np.maximum((n * sw2 - sw**2) / (n - 1), 0.0))
    z = np.divide(numer, denom, out=np.zeros(n), where=denom > 0)
    return z, 2.0 * norm.sf(np.abs(z))


def classify(z: np.ndarray) -> np.ndarray:
    lab = np.full(len(z), "not_significant", dtype=object)
    lab[(z >= 1.96) & (z < 2.58)] = "hot_spot_95"
    lab[z >= 2.58] = "hot_spot_99"
    lab[(z <= -1.96) & (z > -2.58)] = "cold_spot_95"
    lab[z <= -2.58] = "cold_spot_99"
    return lab


def counts(labels: np.ndarray) -> tuple[int, int]:
    hot = int(np.isin(labels, ["hot_spot_95", "hot_spot_99"]).sum())
    cold = int(np.isin(labels, ["cold_spot_95", "cold_spot_99"]).sum())
    return hot, cold


# --------------------------------------------------------------------------
def main() -> None:
    cities = load_unique_cities()
    y = cities["log_ai_works"].to_numpy()
    lat, lng = cities["lat"].to_numpy(), cities["lng"].to_numpy()
    n = len(cities)

    print(f"n unique cities: {n}   (published: 319)")
    print(f"log_ai_works: mean={y.mean():.4f} sd={y.std(ddof=1):.4f}\n")

    W_sym_bin = knn_adjacency(lat, lng, K_NN, symmetrize=True)
    W_sym_row = row_standardize(W_sym_bin)
    W_dir_bin = knn_adjacency(lat, lng, K_NN, symmetrize=False)
    W_dir_row = row_standardize(W_dir_bin)

    variants = {
        "symmetrized binary   (what pipeline.py ships)": W_sym_bin,
        "symmetrized row-std": W_sym_row,
        "directed kNN binary": W_dir_bin,
        "directed kNN row-std (the documented ArcGIS spec)": W_dir_row,
    }

    print("=" * 78)
    print("GLOBAL MORAN'S I    published: I = 0.066, z = 2.86, p = 0.008")
    print("=" * 78)
    print(f"{'weights':52s} {'I':>8s} {'z':>7s} {'p':>7s}  {'engine':>8s}")
    print("-" * 78)

    results = {}
    for name, Wm in variants.items():
        pipe = pipeline_moran(y, Wm)
        # transformation="O" is essential: esda.Moran row-standardises by default,
        # which would silently discard the binary weighting under test.
        mi = Moran(y, to_pysal(Wm), transformation="O", permutations=N_PERM)
        print(f"{name:52s} {pipe['I']:8.4f} {pipe['z']:7.2f} {pipe['p_two_sided']:7.4f}  {'pipeline':>8s}")
        print(f"{'':52s} {mi.I:8.4f} {mi.z_sim:7.2f} {mi.p_sim:7.4f}  {'esda':>8s}")
        results[name] = {
            "pipeline_I": pipe["I"], "pipeline_z": pipe["z"], "pipeline_p": pipe["p_two_sided"],
            "esda_I": float(mi.I), "esda_z_sim": float(mi.z_sim), "esda_p_sim": float(mi.p_sim),
            "esda_EI": float(mi.EI),
        }

    print("\n" + "=" * 78)
    print("GETIS-ORD Gi*       published: 7 hot spots, 33 cold spots")
    print("=" * 78)
    print(f"{'weights':52s} {'hot':>5s} {'cold':>5s}")
    print("-" * 78)
    for name, Wm in variants.items():
        z, _ = pipeline_gi_star(y, Wm)
        hot, cold = counts(classify(z))
        print(f"{name:52s} {hot:5d} {cold:5d}")
        results[name]["gi_hot"] = hot
        results[name]["gi_cold"] = cold

    # ---- check against the shipped ArcGIS-attributed artifact ----
    if HOTSPOT_GEOJSON.exists():
        feats = json.loads(HOTSPOT_GEOJSON.read_text(encoding="utf-8"))["features"]
        shipped = pd.DataFrame(
            [{"id": f["properties"]["city_id"], "z_shipped": f["properties"]["gi_star_z"]}
             for f in feats]
        )
        z_mine, _ = pipeline_gi_star(y, W_sym_bin)
        merged = shipped.merge(
            pd.DataFrame({"id": cities["id"], "z_mine": z_mine}), on="id", how="inner"
        )
        if len(merged):
            diff = (merged["z_shipped"] - merged["z_mine"]).abs()
            print("\n" + "=" * 78)
            print(f"vs shipped cities_with_hotspots.geojson  (matched {len(merged)}/{len(shipped)})")
            print("=" * 78)
            print(f"  max |diff| in Gi* z : {diff.max():.2e}")
            print(f"  correlation         : {merged['z_shipped'].corr(merged['z_mine']):.6f}")

    out = ROOT / "outputs" / "tables" / "morans_i_esda_comparison.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(
        {"n": n, "k_nn": K_NN, "n_permutations": N_PERM, "seed": SEED,
         "published": {"I": 0.066, "z": 2.86, "p": 0.008, "gi_hot": 7, "gi_cold": 33},
         "variants": results}, indent=2), encoding="utf-8")
    print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
