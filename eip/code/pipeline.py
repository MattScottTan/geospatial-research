#!/usr/bin/env python3
"""
AI Compute Accessibility Atlas (Project #1)
Reproducible pipeline:
  - prepare data (cities + cloud regions)
  - compute compute-access metrics (distance, score)
  - join OpenAlex AI research overlay
  - fit two spatial models:
      * Model 1: Gaussian Process regression (GP) + drivers
      * Model 2: Latent Gaussian CAR/GMRF + drivers (Empirical Bayes / conjugate Gaussian)
  - export GIS layers + rasters
  - generate figures for the LaTeX report

Run:
  python src/pipeline.py all

This code is designed to be "boring" and inspectable: no hidden magic.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd
import geopandas as gpd
from pyogrio import write_dataframe
from shapely.geometry import Point
from style_config import (
    ACCESS_CMAP,
    AI_SURFACE_CMAP,
    EXPORT_DPI,
    FIGURE_SIZES,
    HOTSPOT_COLORS,
    PANEL_BBOX,
    PALETTE,
    PRIORITY_CMAP,
    QUADRANT_COLORS,
    TYPOGRAPHY,
    apply_matplotlib_style,
)

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, ConstantKernel as C, WhiteKernel
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

import scipy
from scipy.spatial import cKDTree
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import spsolve, cg

import rasterio
from rasterio.transform import from_origin
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, PercentFormatter

# -------------------------
# Paths / Config
# -------------------------
@dataclass(frozen=True)
class Paths:
    root: Path
    raw: Path
    processed: Path
    outputs: Path
    figures: Path
    tables: Path
    gis: Path

    @staticmethod
    def from_root(root: Path) -> "Paths":
        return Paths(
            root=root,
            raw=root / "data" / "raw",
            processed=root / "data" / "processed",
            outputs=root / "outputs",
            figures=root / "outputs" / "figures",
            tables=root / "outputs" / "tables",
            gis=root / "outputs" / "gis",
        )


def ensure_dirs(p: Paths) -> None:
    for d in [p.raw, p.processed, p.outputs, p.figures, p.tables, p.gis]:
        d.mkdir(parents=True, exist_ok=True)


def write_gpkg_layer(gdf: gpd.GeoDataFrame, path: Path, layer: str) -> None:
    """
    Overwrite a GeoPackage layer in place.

    Explicit layer overwrite avoids backend-dependent behavior when the
    pipeline is rerun on an already-populated checkout.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    write_dataframe(
        gdf,
        path,
        layer=layer,
        driver="GPKG",
        layer_options={"OVERWRITE": "YES"},
    )


def write_geojson_file(gdf: gpd.GeoDataFrame, path: Path) -> None:
    """
    Rewrite a GeoJSON file from scratch.

    GeoJSON is a single-layer text format, so removing the old file first is the
    most predictable way to keep reruns idempotent across GDAL backends.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    write_dataframe(gdf, path, driver="GeoJSON")


def normalize_field_name(name: str) -> str:
    ascii_name = (
        unicodedata.normalize("NFKD", str(name))
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    ascii_name = re.sub(r"[^0-9a-z]+", "_", ascii_name)
    ascii_name = re.sub(r"_+", "_", ascii_name).strip("_")
    return ascii_name or "field"


def prepare_web_geodataframe(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Normalize a GeoDataFrame for web-facing GeoJSON export.

    ArcGIS and GeoJSON clients behave more predictably when fields are lowercase,
    ASCII-safe, and avoid the reserved `id` name.
    """
    gdf = gdf.copy()
    if "id" in gdf.columns and "city_id" not in gdf.columns:
        gdf = gdf.rename(columns={"id": "city_id"})

    rename_map: Dict[str, str] = {}
    used_names = set()
    for col in gdf.columns:
        if col == "geometry":
            continue
        safe = normalize_field_name(col)
        if safe == "id":
            safe = "city_id"
        base = safe
        suffix = 2
        while safe in used_names:
            safe = f"{base}_{suffix}"
            suffix += 1
        used_names.add(safe)
        rename_map[col] = safe

    gdf = gdf.rename(columns=rename_map)
    if gdf.crs is None:
        gdf = gdf.set_crs("EPSG:4326")
    else:
        gdf = gdf.to_crs("EPSG:4326")
    return gdf


# -------------------------
# Geodesy: haversine distance (km)
# -------------------------
def haversine_km(lat1, lon1, lat2, lon2) -> np.ndarray:
    """
    Vectorized haversine distance in kilometers.
    Inputs can be numpy arrays.
    """
    R = 6371.0088  # mean Earth radius (km)
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c


# -------------------------
# Step 1: Prepare cities + cloud regions
# -------------------------
def step_prepare(paths: Paths, top_n_cities: int = 8000) -> Dict[str, str]:
    """
    Prepare:
      - cities GeoPackage (EPSG:4326)
      - cloud regions GeoPackage (EPSG:4326)

    Inputs expected:
      - data/raw/worldcities.csv  (CC-BY-4.0; from condwanaland/worldcities)
      - data/raw/cloud_regions_{aws,azure,gcp}.csv (ODbL derived; from dgl/cloud-regions)

    Outputs:
      - data/processed/cities.gpkg (layer: cities)
      - data/processed/cloud_regions.gpkg (layer: regions)
    """
    ensure_dirs(paths)

    cities_csv = paths.raw / "worldcities.csv"
    if not cities_csv.exists():
        raise FileNotFoundError(f"Missing {cities_csv}. Put worldcities.csv into data/raw/.")

    # Load worldcities
    df = pd.read_csv(cities_csv)
    # Normalize column names we rely on
    expected_cols = {"city", "lat", "lng", "iso2", "iso3", "country", "admin_name", "population"}
    missing = expected_cols - set(df.columns)
    if missing:
        raise ValueError(f"worldcities.csv missing columns: {sorted(missing)}")

    df["population"] = pd.to_numeric(df["population"], errors="coerce")
    df = df.dropna(subset=["lat", "lng"])
    # Keep largest cities by population, but retain rows with missing population too (we'll append OpenAlex later)
    df_sorted = df.sort_values("population", ascending=False, na_position="last").head(top_n_cities).copy()

    gdf_cities = gpd.GeoDataFrame(
        df_sorted,
        geometry=gpd.points_from_xy(df_sorted["lng"], df_sorted["lat"]),
        crs="EPSG:4326",
    )

    cities_gpkg = paths.processed / "cities.gpkg"
    write_gpkg_layer(gdf_cities, cities_gpkg, layer="cities")

    # Cloud regions
    region_files = [
        ("aws", paths.raw / "cloud_regions_aws.csv"),
        ("azure", paths.raw / "cloud_regions_azure.csv"),
        ("gcp", paths.raw / "cloud_regions_gcp.csv"),
    ]
    region_frames = []
    for provider, fp in region_files:
        if not fp.exists():
            raise FileNotFoundError(f"Missing {fp}.")
        tmp = pd.read_csv(fp)
        need = {"region", "location_name", "lat", "lon"}
        if not need.issubset(tmp.columns):
            raise ValueError(f"{fp.name} missing columns {sorted(need - set(tmp.columns))}")
        tmp = tmp.copy()
        tmp["provider"] = provider
        region_frames.append(tmp)

    regions = pd.concat(region_frames, ignore_index=True)
    regions = regions.dropna(subset=["lat", "lon"])
    gdf_regions = gpd.GeoDataFrame(
        regions,
        geometry=gpd.points_from_xy(regions["lon"], regions["lat"]),
        crs="EPSG:4326",
    )

    regions_gpkg = paths.processed / "cloud_regions.gpkg"
    write_gpkg_layer(gdf_regions, regions_gpkg, layer="regions")

    return {
        "cities_gpkg": str(cities_gpkg),
        "regions_gpkg": str(regions_gpkg),
        "n_cities": str(len(gdf_cities)),
        "n_regions": str(len(gdf_regions)),
    }


# -------------------------
# Step 2: Compute access metrics
# -------------------------
def compute_nearest_region_distances(city_latlon: np.ndarray, region_latlon: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute nearest region for each city based on haversine distance.
    Returns (nearest_distance_km, nearest_index).
    """
    # Use KDTree in 3D unit sphere coordinates for speed.
    def to_xyz(lat, lon):
        lat_r = np.radians(lat)
        lon_r = np.radians(lon)
        x = np.cos(lat_r) * np.cos(lon_r)
        y = np.cos(lat_r) * np.sin(lon_r)
        z = np.sin(lat_r)
        return np.column_stack([x, y, z])

    city_xyz = to_xyz(city_latlon[:, 0], city_latlon[:, 1])
    region_xyz = to_xyz(region_latlon[:, 0], region_latlon[:, 1])

    tree = cKDTree(region_xyz)
    # chord distance in unit sphere
    d_chord, idx = tree.query(city_xyz, k=1)
    # Convert chord distance to central angle: chord = 2 sin(theta/2) => theta = 2 arcsin(chord/2)
    theta = 2 * np.arcsin(np.clip(d_chord / 2, 0, 1))
    R = 6371.0088
    d_km = R * theta
    return d_km, idx


def step_compute_access(paths: Paths, d0_km: float = 2000.0) -> Dict[str, str]:
    """
    Compute distance-to-nearest cloud region for each city.
    Also compute an accessibility score in [0, 100]:
        score = 100 * exp(-distance_km / d0_km)

    Outputs:
      - outputs/tables/city_access_metrics.csv
      - outputs/gis/ai_access_cities.gpkg (layer: cities_access)
      - outputs/gis/ai_access_cities.geojson
    """
    ensure_dirs(paths)
    cities_gpkg = paths.processed / "cities.gpkg"
    regions_gpkg = paths.processed / "cloud_regions.gpkg"
    if not cities_gpkg.exists() or not regions_gpkg.exists():
        raise FileNotFoundError("Run step_prepare first (cities.gpkg and cloud_regions.gpkg).")

    cities = gpd.read_file(cities_gpkg, layer="cities")
    regions = gpd.read_file(regions_gpkg, layer="regions")

    # Coordinates
    city_latlon = np.column_stack([cities["lat"].to_numpy(), cities["lng"].to_numpy()])
    region_latlon = np.column_stack([regions["lat"].to_numpy(), regions["lon"].to_numpy()])

    d_km, idx = compute_nearest_region_distances(city_latlon, region_latlon)
    cities = cities.copy()
    cities["nearest_region_idx"] = idx
    cities["dist_km_nearest_region"] = d_km
    cities["access_score"] = 100.0 * np.exp(-cities["dist_km_nearest_region"] / d0_km)

    # Bring region info
    region_cols = ["provider", "region", "location_name", "lat", "lon"]
    regions_small = regions.reset_index(drop=True)[region_cols].copy()
    regions_small.columns = [f"nearest_{c}" for c in regions_small.columns]
    cities = cities.reset_index(drop=True).join(regions_small.iloc[idx].reset_index(drop=True))

    # Table export
    out_parquet = paths.tables / "city_access_metrics.csv"
    cities.drop(columns="geometry").to_csv(out_parquet, index=False)

    # GIS export
    out_gpkg = paths.gis / "ai_access_cities.gpkg"
    write_gpkg_layer(cities, out_gpkg, layer="cities_access")
    out_geojson = paths.gis / "ai_access_cities.geojson"
    write_geojson_file(prepare_web_geodataframe(cities), out_geojson)

    return {
        "city_access_metrics_parquet": str(out_parquet),
        "cities_access_gpkg": str(out_gpkg),
        "cities_access_geojson": str(out_geojson),
    }


# -------------------------
# Step 3: Join OpenAlex overlay
# -------------------------
def step_join_openalex(paths: Paths, match_max_km: float = 75.0) -> Dict[str, str]:
    """
    Join OpenAlex "AI research intensity by city" overlay (provided by user)
    to the worldcities city table to inherit population/admin attributes.

    Inputs expected in data/raw/:
      - openalex_ai_city_overlay.csv
      - openalex_ai_institutions_top.csv
      - openalex_topics_used.json

    Outputs:
      - outputs/tables/city_access_ai.csv
      - outputs/gis/ai_access_ai_cities.gpkg (layer: cities_ai)
      - outputs/tables/openalex_institutions_top.csv
    """
    ensure_dirs(paths)

    overlay_fp = paths.raw / "openalex_ai_city_overlay.csv"
    inst_fp = paths.raw / "openalex_ai_institutions_top.csv"
    topics_fp = paths.raw / "openalex_topics_used.json"

    for fp in [overlay_fp, inst_fp, topics_fp]:
        if not fp.exists():
            raise FileNotFoundError(f"Missing {fp}")

    cities_access_fp = paths.gis / "ai_access_cities.gpkg"
    if not cities_access_fp.exists():
        raise FileNotFoundError("Run step_compute_access first (ai_access_cities.gpkg).")

    cities_access = gpd.read_file(cities_access_fp, layer="cities_access").copy()
    overlay = pd.read_csv(overlay_fp).copy()

    # Ensure numeric
    overlay["lat"] = pd.to_numeric(overlay["lat"], errors="coerce")
    overlay["lon"] = pd.to_numeric(overlay["lon"], errors="coerce")
    overlay["ai_works_recent"] = pd.to_numeric(overlay["ai_works_recent"], errors="coerce")
    overlay["ai_institution_count"] = pd.to_numeric(overlay["ai_institution_count"], errors="coerce")

    overlay = overlay.dropna(subset=["lat", "lon"])

    # Build matching index by country for speed
    cities_access["iso2"] = cities_access["iso2"].astype(str).str.upper()
    overlay["geo_country_code"] = overlay["geo_country_code"].astype(str).str.upper()

    # KDTree per country
    matched_rows = []
    for country, ogrp in overlay.groupby("geo_country_code"):
        cgrp = cities_access[cities_access["iso2"] == country]
        if len(cgrp) == 0:
            # fallback: match globally
            cgrp = cities_access
        # KDTree in 3D
        city_latlon = np.column_stack([cgrp["lat"].to_numpy(), cgrp["lng"].to_numpy()])
        reg_latlon = np.column_stack([ogrp["lat"].to_numpy(), ogrp["lon"].to_numpy()])

        # Build city tree
        def to_xyz(lat, lon):
            lat_r = np.radians(lat)
            lon_r = np.radians(lon)
            x = np.cos(lat_r) * np.cos(lon_r)
            y = np.cos(lat_r) * np.sin(lon_r)
            z = np.sin(lat_r)
            return np.column_stack([x, y, z])

        tree = cKDTree(to_xyz(city_latlon[:, 0], city_latlon[:, 1]))
        d_chord, idx = tree.query(to_xyz(reg_latlon[:, 0], reg_latlon[:, 1]), k=1)
        theta = 2 * np.arcsin(np.clip(d_chord / 2, 0, 1))
        d_km = 6371.0088 * theta

        match = cgrp.iloc[idx].copy()
        match = match.reset_index(drop=True)
        ogrp2 = ogrp.reset_index(drop=True)

        # keep match quality
        match["openalex_match_km"] = d_km
        match["openalex_geo_city"] = ogrp2["geo_city"].values
        match["openalex_ai_works_recent"] = ogrp2["ai_works_recent"].values
        match["openalex_ai_institution_count"] = ogrp2["ai_institution_count"].values
        match["openalex_lat"] = ogrp2["lat"].values
        match["openalex_lon"] = ogrp2["lon"].values
        matched_rows.append(match)

    cities_ai = pd.concat(matched_rows, ignore_index=True)

    # Flag dubious matches
    cities_ai["openalex_match_ok"] = cities_ai["openalex_match_km"] <= match_max_km

    # Derived measures
    cities_ai["log_ai_works"] = np.log1p(cities_ai["openalex_ai_works_recent"])
    # per-capita (per million) if population exists
    cities_ai["ai_works_per_million"] = np.where(
        cities_ai["population"].notna() & (cities_ai["population"] > 0),
        cities_ai["openalex_ai_works_recent"] / cities_ai["population"] * 1e6,
        np.nan,
    )
    cities_ai["log_ai_works_per_million"] = np.where(
        np.isfinite(cities_ai["ai_works_per_million"]),
        np.log1p(cities_ai["ai_works_per_million"]),
        np.nan,
    )

    # Table export
    out_parquet = paths.tables / "city_access_ai.csv"
    cities_ai.drop(columns="geometry").to_csv(out_parquet, index=False)

    # GIS export (use matched city geometry; also keep OpenAlex coords for overlay)
    cities_ai_gdf = gpd.GeoDataFrame(cities_ai, geometry=cities_ai["geometry"], crs="EPSG:4326")
    out_gpkg = paths.gis / "ai_access_ai_cities.gpkg"
    write_gpkg_layer(cities_ai_gdf, out_gpkg, layer="cities_ai")

    # Institutions export
    inst = pd.read_csv(inst_fp).copy()
    inst_out = paths.tables / "openalex_institutions_top.csv"
    inst.to_csv(inst_out, index=False)

    # Topics used export
    topics = json.loads(Path(topics_fp).read_text(encoding="utf-8"))
    topics_out = paths.tables / "openalex_topics_used.json"
    Path(topics_out).write_text(json.dumps(topics, indent=2), encoding="utf-8")

    return {
        "city_access_ai_parquet": str(out_parquet),
        "cities_ai_gpkg": str(out_gpkg),
        "institutions_top_parquet": str(inst_out),
        "topics_used_json": str(topics_out),
        "n_ai_cities": str(len(cities_ai)),
        "match_ok_rate": str(float(cities_ai["openalex_match_ok"].mean())),
    }


# -------------------------
# Step 4: Model 1 (GP + drivers)
# -------------------------
def step_model_gp(paths: Paths, target: str = "log_ai_works") -> Dict[str, str]:
    """
    Model 1: GP + drivers (reader-friendly)

    We fit an additive model:
        y(s) = X(s) beta + f(s) + eps
    where:
      - X(s) are interpretable drivers (distance-to-nearest cloud region, city size)
      - f(s) is a smooth spatial field (Gaussian Process with Matérn kernel)
      - eps is i.i.d. noise

    Implementation details:
      1) OLS regression for beta on drivers
      2) GP on *residuals* using coordinates only (lat/lon), with fixed hyperparameters
         to keep runtime stable/reproducible.

    Outputs:
      - outputs/tables/model_gp_summary.json
      - outputs/tables/model_gp_predictions.csv (city-level)
    """
    ensure_dirs(paths)
    ai_fp = paths.tables / "city_access_ai.csv"
    if not ai_fp.exists():
        raise FileNotFoundError("Run step_join_openalex first (city_access_ai.csv).")

    df = pd.read_csv(ai_fp)

    # Keep rows with target present
    df = df[df[target].notna()].copy()
    n = len(df)

    # Drivers (interpretable)
    df["log_pop"] = np.log(df["population"].fillna(df["population"].median()) + 1.0)
    X = np.column_stack([
        np.ones(n),
        (df["dist_km_nearest_region"].to_numpy() / 1000.0),  # per 1000 km
        df["log_pop"].to_numpy(),
    ])
    y = df[target].to_numpy()

    # Simple train/test split for a sanity-check RMSE
    rng = np.random.RandomState(42)
    idx = np.arange(n)
    rng.shuffle(idx)
    split = int(0.8 * n)
    tr, te = idx[:split], idx[split:]

    def fit_predict(train_idx: np.ndarray, test_idx: np.ndarray):
        Xtr, ytr = X[train_idx], y[train_idx]
        Xte, yte = X[test_idx], y[test_idx]

        # OLS
        beta, *_ = np.linalg.lstsq(Xtr, ytr, rcond=None)
        resid_tr = ytr - Xtr @ beta

        # GP on residuals: Matérn(ν=1.5) with fixed length-scale in degrees.
        coords_tr = df.loc[train_idx, ["lat", "lng"]].to_numpy()
        coords_te = df.loc[test_idx, ["lat", "lng"]].to_numpy()

        # Heuristic variance + noise for stability
        resid_var = float(np.var(resid_tr)) if len(resid_tr) > 5 else 0.1
        length_scale_deg = 20.0  # global-scale smoothness; not tuned to avoid slow optimization
        noise_var = max(1e-4, 0.15 * resid_var)

        kernel = C(resid_var, constant_value_bounds="fixed") * Matern(
            length_scale=length_scale_deg, length_scale_bounds="fixed", nu=1.5
        )
        gpr = GaussianProcessRegressor(
            kernel=kernel,
            alpha=noise_var,
            normalize_y=False,
            optimizer=None,
            random_state=42,
        )
        gpr.fit(coords_tr, resid_tr)

        resid_pred_te, resid_sd_te = gpr.predict(coords_te, return_std=True)
        y_pred_te = Xte @ beta + resid_pred_te
        rmse_te = float(np.sqrt(mean_squared_error(yte, y_pred_te)))

        # Fit full-data model for outputs
        beta_full, *_ = np.linalg.lstsq(X, y, rcond=None)
        resid_full = y - X @ beta_full
        coords_full = df[["lat", "lng"]].to_numpy()
        resid_var_full = float(np.var(resid_full)) if len(resid_full) > 5 else resid_var
        noise_var_full = max(1e-4, 0.15 * resid_var_full)

        kernel_full = C(resid_var_full, constant_value_bounds="fixed") * Matern(
            length_scale=length_scale_deg, length_scale_bounds="fixed", nu=1.5
        )
        gpr_full = GaussianProcessRegressor(
            kernel=kernel_full,
            alpha=noise_var_full,
            normalize_y=False,
            optimizer=None,
            random_state=42,
        )
        gpr_full.fit(coords_full, resid_full)

        resid_pred_full, resid_sd_full = gpr_full.predict(coords_full, return_std=True)
        y_pred_full = X @ beta_full + resid_pred_full
        rmse_in = float(np.sqrt(mean_squared_error(y, y_pred_full)))

        return {
            "beta": beta_full,
            "length_scale_deg": length_scale_deg,
            "resid_var": resid_var_full,
            "noise_var": noise_var_full,
            "rmse_in_sample": rmse_in,
            "rmse_holdout": rmse_te,
            "y_pred": y_pred_full,
            "y_sd": resid_sd_full,
            "resid_pred": resid_pred_full,
            "resid_sd": resid_sd_full,
        }

    fit = fit_predict(tr, te)

    df_out = df.copy()
    df_out["gp_pred"] = fit["y_pred"]
    df_out["gp_pred_sd"] = fit["y_sd"]
    df_out["gp_resid_pred"] = fit["resid_pred"]
    df_out["gp_resid_sd"] = fit["resid_sd"]

    pred_fp = paths.tables / "model_gp_predictions.csv"
    df_out.to_csv(pred_fp, index=False)

    beta = fit["beta"]
    summary = {
        "target": target,
        "n": int(n),
        "beta": {
            "intercept": float(beta[0]),
            "dist_per_1000km": float(beta[1]),
            "log_pop": float(beta[2]),
        },
        "gp_params_fixed": {
            "matern_nu": 1.5,
            "length_scale_deg": float(fit["length_scale_deg"]),
            "resid_var": float(fit["resid_var"]),
            "noise_var": float(fit["noise_var"]),
        },
        "rmse_in_sample": float(fit["rmse_in_sample"]),
        "rmse_holdout_20pct": float(fit["rmse_holdout"]),
        "notes": "Fixed-hyperparameter residual GP for stable runtimes. Holdout RMSE is a rough sanity check, not a full evaluation.",
    }
    summary_fp = paths.tables / "model_gp_summary.json"
    Path(summary_fp).write_text(json.dumps(summary, indent=2), encoding="utf-8")

    return {"model_gp_summary": str(summary_fp), "model_gp_predictions": str(pred_fp)}

# -------------------------
# Step 5: Model 2 (CAR/GMRF + drivers)
# -------------------------
def build_knn_graph(lat: np.ndarray, lon: np.ndarray, k: int = 8) -> csr_matrix:
    """
    Build symmetric kNN adjacency for points on the sphere (approx, using 3D unit vectors).
    Returns sparse adjacency W (binary).
    """
    def to_xyz(lat, lon):
        lat_r = np.radians(lat)
        lon_r = np.radians(lon)
        x = np.cos(lat_r) * np.cos(lon_r)
        y = np.cos(lat_r) * np.sin(lon_r)
        z = np.sin(lat_r)
        return np.column_stack([x, y, z])

    xyz = to_xyz(lat, lon)
    tree = cKDTree(xyz)
    # query k+1 because first neighbor is self
    d, idx = tree.query(xyz, k=k + 1)
    n = len(lat)
    rows = np.repeat(np.arange(n), k)
    cols = idx[:, 1:].reshape(-1)  # drop self
    data = np.ones_like(rows, dtype=float)
    W = csr_matrix((data, (rows, cols)), shape=(n, n))
    # symmetrize
    W = ((W + W.T) > 0).astype(float).tocsr()
    return W


def step_model_car(paths: Paths, target: str = "log_ai_works", k_nn: int = 8, rho: float = 0.99, lam: float = 1.0) -> Dict[str, str]:
    """
    Fit a latent Gaussian CAR/GMRF model with Gaussian likelihood (conjugate):
        y = X beta + u + eps
        eps ~ N(0, sigma2 I)
        u ~ N(0, tau^{-1} Q^{-1})  with CAR precision Q = D - rho W

    We estimate hyperparameters (sigma2, tau) via a simple empirical Bayes grid search
    on (log sigma2, log tau). rho is fixed close to 1 for spatial smoothing.

    Because the model is Gaussian, we can compute the posterior mean exactly by solving
    a sparse linear system.

    Outputs:
      - outputs/tables/model_car_summary.json
      - outputs/tables/model_car_predictions.csv
    """
    ensure_dirs(paths)
    ai_fp = paths.tables / "city_access_ai.csv"
    if not ai_fp.exists():
        raise FileNotFoundError("Run step_join_openalex first (city_access_ai.csv).")

    df = pd.read_csv(ai_fp)
    df = df[df[target].notna()].copy()

    # Features
    df["log_pop"] = np.log(df["population"].fillna(df["population"].median()) + 1.0)
    X = np.column_stack([
        np.ones(len(df)),
        (df["dist_km_nearest_region"].to_numpy() / 1000.0),  # per 1000 km
        df["log_pop"].to_numpy(),
    ])
    y = df[target].to_numpy()

    lat = df["lat"].to_numpy()
    lon = df["lng"].to_numpy()
    W = build_knn_graph(lat, lon, k=k_nn)
    n = len(df)
    d = np.array(W.sum(axis=1)).reshape(-1)
    D = diags(d)
    Q = (D - rho * W).tocsr()

    # Ridge prior on beta: beta ~ N(0, lam^{-1} I)
    # Equivalent: add lam to precision of beta block.
    # We will solve for posterior mean of (beta, u) in block system:
    # [ (1/sigma2) X'X + lam I     (1/sigma2) X' ]
    # [ (1/sigma2) X              (1/sigma2) I + tau Q ] [beta; u] = (1/sigma2) [X'y; y]
    #
    # This is (p+n)x(p+n) where p=3; n~300 -> manageable.

    p = X.shape[1]

    # Empirical Bayes grid over sigma2 and tau
    # Coarse grid, enough for stable smoothing, not overkill.
    sigma2_grid = np.exp(np.linspace(np.log(0.05), np.log(1.0), 10))
    tau_grid = np.exp(np.linspace(np.log(0.1), np.log(10.0), 10))

    best = None
    best_obj = np.inf

    XTX = X.T @ X
    XTy = X.T @ y

    I_p = np.eye(p)

    for sigma2 in sigma2_grid:
        for tau in tau_grid:
            # Build block matrix A and rhs b
            A11 = (1.0 / sigma2) * XTX + lam * I_p
            A12 = (1.0 / sigma2) * X.T
            A21 = (1.0 / sigma2) * X
            A22 = (1.0 / sigma2) * scipy.sparse.identity(n, format="csr") + tau * Q

            # Assemble sparse block matrix
            A = scipy.sparse.bmat([[csr_matrix(A11), csr_matrix(A12)], [csr_matrix(A21), A22]], format="csr")
            b = np.concatenate([(1.0 / sigma2) * XTy, (1.0 / sigma2) * y])

            # Solve
            try:
                sol = spsolve(A, b)
            except Exception:
                continue
            beta = sol[:p]
            u = sol[p:]
            y_hat = X @ beta + u
            resid = y - y_hat
            # Objective: negative log posterior up to constants
            obj = float((resid @ resid) / sigma2 + tau * (u @ (Q @ u)) + lam * (beta @ beta))
            if obj < best_obj:
                best_obj = obj
                best = {"sigma2": float(sigma2), "tau": float(tau), "beta": beta, "u": u, "y_hat": y_hat}

    if best is None:
        raise RuntimeError("CAR model fitting failed (no solution in grid search).")

    beta = best["beta"]
    u = best["u"]
    y_hat = best["y_hat"]
    resid = y - y_hat
    rmse = float(np.sqrt(np.mean(resid**2)))

    df_out = df.copy()
    df_out["car_pred"] = y_hat
    df_out["car_u"] = u
    df_out["car_resid"] = resid

    pred_fp = paths.tables / "model_car_predictions.csv"
    df_out.to_csv(pred_fp, index=False)

    summary = {
        "target": target,
        "n": int(len(df_out)),
        "k_nn": int(k_nn),
        "rho_fixed": float(rho),
        "beta": {
            "intercept": float(beta[0]),
            "dist_per_1000km": float(beta[1]),
            "log_pop": float(beta[2]),
        },
        "sigma2_hat": best["sigma2"],
        "tau_hat": best["tau"],
        "rmse_in_sample": rmse,
        "objective_best": best_obj,
        "notes": "Empirical Bayes grid search over (sigma2, tau) with fixed rho close to 1. This is a latent Gaussian model; posterior mean solved via sparse linear system.",
    }
    summary_fp = paths.tables / "model_car_summary.json"
    Path(summary_fp).write_text(json.dumps(summary, indent=2), encoding="utf-8")

    return {"model_car_summary": str(summary_fp), "model_car_predictions": str(pred_fp)}


# -------------------------
# Step 6: Spatial diagnostics + priority outputs
# -------------------------
def aggregate_ai_city_matches(cities_ai: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Collapse duplicate OpenAlex-to-city matches down to one row per city.

    The raw overlay can match multiple OpenAlex rows to the same city. Spatial
    diagnostics should operate on unique city geometries with summed AI output.
    """
    grouped = (
        cities_ai.groupby("id", dropna=False)
        .agg(
            city=("city", "first"),
            city_ascii=("city_ascii", "first"),
            lat=("lat", "first"),
            lng=("lng", "first"),
            country=("country", "first"),
            iso2=("iso2", "first"),
            iso3=("iso3", "first"),
            admin_name=("admin_name", "first"),
            population=("population", "first"),
            dist_km_nearest_region=("dist_km_nearest_region", "first"),
            access_score=("access_score", "first"),
            nearest_provider=("nearest_provider", "first"),
            nearest_region=("nearest_region", "first"),
            nearest_location_name=("nearest_location_name", "first"),
            nearest_lat=("nearest_lat", "first"),
            nearest_lon=("nearest_lon", "first"),
            geometry=("geometry", "first"),
            openalex_ai_works_recent=("openalex_ai_works_recent", "sum"),
            openalex_ai_institution_count=("openalex_ai_institution_count", "sum"),
            openalex_match_km=("openalex_match_km", "min"),
            overlay_match_count=("openalex_geo_city", "size"),
        )
        .reset_index()
    )
    grouped["log_ai_works"] = np.log1p(grouped["openalex_ai_works_recent"])
    return gpd.GeoDataFrame(grouped, geometry="geometry", crs=cities_ai.crs)


def compute_global_morans_i(
    values: np.ndarray,
    weights: csr_matrix,
    n_permutations: int = 499,
    seed: int = 42,
) -> Dict[str, float]:
    values = np.asarray(values, dtype=float)
    centered = values - values.mean()
    denom = float(centered @ centered)
    s0 = float(weights.sum())
    n = len(values)

    if n < 2 or denom <= 0 or s0 <= 0:
        return {
            "morans_i": float("nan"),
            "expected_i": float("nan"),
            "perm_mean_i": float("nan"),
            "perm_sd_i": float("nan"),
            "z_score": float("nan"),
            "p_value_two_sided": float("nan"),
        }

    lag_centered = np.asarray(weights @ centered).ravel()
    observed = float((n / s0) * (centered @ lag_centered) / denom)

    rng = np.random.default_rng(seed)
    permuted = np.empty(n_permutations, dtype=float)
    for i in range(n_permutations):
        perm = rng.permutation(centered)
        permuted[i] = float((n / s0) * (perm @ np.asarray(weights @ perm).ravel()) / denom)

    perm_mean = float(permuted.mean())
    perm_sd = float(permuted.std(ddof=1)) if n_permutations > 1 else float("nan")
    z_score = float((observed - perm_mean) / perm_sd) if perm_sd and not np.isnan(perm_sd) else float("nan")
    p_value = float((np.count_nonzero(np.abs(permuted) >= abs(observed)) + 1) / (n_permutations + 1))

    return {
        "morans_i": observed,
        "expected_i": float(-1.0 / (n - 1)),
        "perm_mean_i": perm_mean,
        "perm_sd_i": perm_sd,
        "z_score": z_score,
        "p_value_two_sided": p_value,
    }


def compute_local_gi_star(values: np.ndarray, weights: csr_matrix) -> Tuple[np.ndarray, np.ndarray]:
    values = np.asarray(values, dtype=float)
    n = len(values)
    if n < 2:
        return np.zeros(n, dtype=float), np.ones(n, dtype=float)

    weights_star = weights.copy().tolil()
    weights_star.setdiag(1.0)
    weights_star = weights_star.tocsr()

    mean_x = float(values.mean())
    std_x = float(values.std(ddof=1))
    if std_x == 0.0:
        return np.zeros(n, dtype=float), np.ones(n, dtype=float)

    sum_w = np.asarray(weights_star.sum(axis=1)).ravel()
    sum_w_sq = np.asarray(weights_star.power(2).sum(axis=1)).ravel()
    numer = np.asarray(weights_star @ values).ravel() - mean_x * sum_w
    denom = std_x * np.sqrt(np.maximum((n * sum_w_sq - sum_w**2) / (n - 1), 0.0))
    gi_z = np.divide(numer, denom, out=np.zeros(n, dtype=float), where=denom > 0)
    gi_p = 2.0 * scipy.stats.norm.sf(np.abs(gi_z))
    return gi_z, gi_p


def classify_hotspot_zscores(gi_z: np.ndarray) -> np.ndarray:
    gi_z = np.asarray(gi_z, dtype=float)
    labels = np.full(len(gi_z), "not_significant", dtype=object)
    labels[(gi_z >= 1.96) & (gi_z < 2.58)] = "hot_spot_95"
    labels[gi_z >= 2.58] = "hot_spot_99"
    labels[(gi_z <= -1.96) & (gi_z > -2.58)] = "cold_spot_95"
    labels[gi_z <= -2.58] = "cold_spot_99"
    return labels


def step_spatial_outputs(
    paths: Paths,
    k_nn: int = 8,
    n_permutations: int = 499,
    priority_distance_quantile: float = 0.75,
) -> Dict[str, str]:
    """
    Restore the handoff-referenced spatial diagnostics and priority-city outputs.

    Outputs:
      - outputs/tables/morans_i_summary.csv
      - outputs/gis/cities_with_hotspots.geojson
      - outputs/tables/priority_cities.csv
      - outputs/gis/priority_cities.geojson
    """
    ensure_dirs(paths)
    cities_access_fp = paths.gis / "ai_access_cities.gpkg"
    cities_ai_fp = paths.gis / "ai_access_ai_cities.gpkg"
    if not cities_access_fp.exists() or not cities_ai_fp.exists():
        raise FileNotFoundError("Run step_compute_access and step_join_openalex first.")

    cities_access = gpd.read_file(cities_access_fp, layer="cities_access")
    cities_ai = gpd.read_file(cities_ai_fp, layer="cities_ai")
    ai_unique = aggregate_ai_city_matches(cities_ai)

    weights = build_knn_graph(ai_unique["lat"].to_numpy(), ai_unique["lng"].to_numpy(), k=k_nn)
    moran_values = ai_unique["log_ai_works"].to_numpy()
    moran_summary = compute_global_morans_i(moran_values, weights, n_permutations=n_permutations)
    row_sums = np.asarray(weights.sum(axis=1)).ravel()
    spatial_lag = np.divide(
        np.asarray(weights @ moran_values).ravel(),
        row_sums,
        out=np.zeros(len(ai_unique), dtype=float),
        where=row_sums > 0,
    )

    moran_out = pd.DataFrame(
        [
            {
                "metric": "log_ai_works",
                "n_unique_ai_cities": int(len(ai_unique)),
                "k_nn": int(k_nn),
                "n_permutations": int(n_permutations),
                **moran_summary,
            }
        ]
    )
    moran_fp = paths.tables / "morans_i_summary.csv"
    moran_out.to_csv(moran_fp, index=False)

    gi_z, gi_p = compute_local_gi_star(moran_values, weights)
    hotspots = ai_unique.copy()
    hotspots["spatial_lag_log_ai_works"] = spatial_lag
    hotspots["gi_star_z"] = gi_z
    hotspots["gi_star_p"] = gi_p
    hotspots["hotspot_class"] = classify_hotspot_zscores(gi_z)
    hotspots["hotspot_rank"] = np.where(
        hotspots["gi_star_z"] > 0,
        hotspots["gi_star_z"].rank(method="dense", ascending=False),
        np.nan,
    )
    hotspots["k_nn"] = int(k_nn)

    hotspots_export = prepare_web_geodataframe(
        hotspots[
            [
                "id",
                "city",
                "city_ascii",
                "country",
                "iso2",
                "iso3",
                "admin_name",
                "population",
                "openalex_ai_works_recent",
                "openalex_ai_institution_count",
                "overlay_match_count",
                "openalex_match_km",
                "dist_km_nearest_region",
                "access_score",
                "nearest_provider",
                "nearest_region",
                "nearest_location_name",
                "spatial_lag_log_ai_works",
                "gi_star_z",
                "gi_star_p",
                "hotspot_class",
                "hotspot_rank",
                "k_nn",
                "geometry",
            ]
        ]
    )
    hotspots_fp = paths.gis / "cities_with_hotspots.geojson"
    write_geojson_file(hotspots_export, hotspots_fp)

    ai_by_city = ai_unique[["id", "openalex_ai_works_recent"]].rename(
        columns={"openalex_ai_works_recent": "observed_ai_works_recent"}
    )
    priority = cities_access.merge(ai_by_city, on="id", how="left")
    priority["observed_ai_works_recent"] = priority["observed_ai_works_recent"].fillna(0.0)
    threshold_km = float(priority["dist_km_nearest_region"].quantile(priority_distance_quantile))
    priority = priority[
        (priority["observed_ai_works_recent"] <= 0)
        & (priority["dist_km_nearest_region"] >= threshold_km)
    ].copy()
    priority = priority.sort_values(
        ["population", "dist_km_nearest_region", "city"],
        ascending=[False, False, True],
        na_position="last",
    ).reset_index(drop=True)
    priority["priority_rank"] = np.arange(1, len(priority) + 1)
    priority["priority_rule"] = f"zero_observed_ai_and_distance_gte_q{int(priority_distance_quantile * 100)}"
    priority["priority_distance_threshold_km"] = threshold_km

    priority_export = prepare_web_geodataframe(
        priority[
            [
                "id",
                "city",
                "city_ascii",
                "country",
                "iso2",
                "iso3",
                "admin_name",
                "population",
                "dist_km_nearest_region",
                "access_score",
                "nearest_provider",
                "nearest_region",
                "nearest_location_name",
                "observed_ai_works_recent",
                "priority_rank",
                "priority_rule",
                "priority_distance_threshold_km",
                "geometry",
            ]
        ]
    )
    priority_csv = paths.tables / "priority_cities.csv"
    priority_geojson = paths.gis / "priority_cities.geojson"
    priority_export.drop(columns="geometry").to_csv(priority_csv, index=False)
    write_geojson_file(priority_export, priority_geojson)

    return {
        "morans_i_summary_csv": str(moran_fp),
        "cities_with_hotspots_geojson": str(hotspots_fp),
        "priority_cities_csv": str(priority_csv),
        "priority_cities_geojson": str(priority_geojson),
        "n_unique_ai_cities": str(len(ai_unique)),
        "n_priority_cities": str(len(priority_export)),
    }


# -------------------------
# Step 7: Surfaces (GeoTIFF)
# -------------------------
def rasterize_global_surface(
    lat_min: float,
    lat_max: float,
    lon_min: float,
    lon_max: float,
    resolution_deg: float,
    values: np.ndarray,
    out_tif: Path,
    nodata: float = -9999.0,
) -> None:
    """
    Save a global lat-lon grid as GeoTIFF (EPSG:4326).
    Values expected shape: (n_lat, n_lon) where lat index decreases from lat_max to lat_min.
    """
    n_lat, n_lon = values.shape
    transform = from_origin(lon_min, lat_max, resolution_deg, resolution_deg)
    out_tif.parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(
        out_tif,
        "w",
        driver="GTiff",
        height=n_lat,
        width=n_lon,
        count=1,
        dtype=np.float32,
        crs="EPSG:4326",
        transform=transform,
        nodata=nodata,
        compress="deflate",
        predictor=2,
    ) as dst:
        arr = values.astype(np.float32)
        dst.write(arr, 1)


def step_surfaces(paths: Paths, resolution_deg: float = 1.0) -> Dict[str, str]:
    """
    Produce three global rasters at coarse resolution:
      - distance-to-nearest region (km)
      - GP predicted log AI works (for a reference city size)
      - CAR predicted log AI works (interpolated from city nodes via IDW)

    Outputs:
      - outputs/gis/ai_access_surface_distance.tif
      - outputs/gis/ai_research_pred_gp.tif
      - outputs/gis/ai_research_pred_car.tif
    """
    ensure_dirs(paths)
    regions_gpkg = paths.processed / "cloud_regions.gpkg"
    if not regions_gpkg.exists():
        raise FileNotFoundError("Run step_prepare first.")
    regions = gpd.read_file(regions_gpkg, layer="regions")
    region_latlon = np.column_stack([regions["lat"].to_numpy(), regions["lon"].to_numpy()])

    # Grid definition (avoid poles for stability)
    lat_max = 80.0
    lat_min = -60.0
    lon_min = -180.0
    lon_max = 180.0
    lats = np.arange(lat_max, lat_min - 1e-9, -resolution_deg)  # descending
    lons = np.arange(lon_min, lon_max, resolution_deg)
    n_lat = len(lats)
    n_lon = len(lons)

    # Compute distance surface
    dist_surface = np.zeros((n_lat, n_lon), dtype=float)
    # chunk to avoid huge RAM
    for i, lat in enumerate(lats):
        lat_row = np.full(n_lon, lat)
        lon_row = lons
        grid_latlon = np.column_stack([lat_row, lon_row])
        d_km, _ = compute_nearest_region_distances(grid_latlon, region_latlon)
        dist_surface[i, :] = d_km

    dist_tif = paths.gis / "ai_access_surface_distance.tif"
    rasterize_global_surface(lat_min, lat_max, lon_min, lon_max, resolution_deg, dist_surface, dist_tif)

    # GP predicted surface (Model 1): y = X beta + residual GP(s)
    gp_pred_tif = paths.gis / "ai_research_pred_gp.tif"
    gp_summary_fp = paths.tables / "model_gp_summary.json"
    gp_pred_fp = paths.tables / "model_gp_predictions.csv"
    if gp_summary_fp.exists() and gp_pred_fp.exists():
        summ = json.loads(Path(gp_summary_fp).read_text(encoding="utf-8"))
        beta = np.array([
            summ["beta"]["intercept"],
            summ["beta"]["dist_per_1000km"],
            summ["beta"]["log_pop"],
        ], dtype=float)

        length_scale_deg = float(summ["gp_params_fixed"]["length_scale_deg"])
        resid_var = float(summ["gp_params_fixed"]["resid_var"])
        noise_var = float(summ["gp_params_fixed"]["noise_var"])

        df = pd.read_csv(gp_pred_fp)
        # Reconstruct training residuals
        Xtrain = np.column_stack([
            np.ones(len(df)),
            (df["dist_km_nearest_region"].to_numpy() / 1000.0),
            df["log_pop"].to_numpy(),
        ])
        ytrain = df["log_ai_works"].to_numpy()
        coords_train = df[["lat", "lng"]].to_numpy()
        resid = ytrain - Xtrain @ beta

        kernel = C(resid_var, constant_value_bounds="fixed") * Matern(
            length_scale=length_scale_deg, length_scale_bounds="fixed", nu=1.5
        )
        gpr = GaussianProcessRegressor(
            kernel=kernel,
            alpha=noise_var,
            normalize_y=False,
            optimizer=None,
            random_state=42,
        )
        gpr.fit(coords_train, resid)

        # Reference city size (1M) for the surface.
        ref_log_pop = math.log(1_000_000 + 1.0)

        gp_surface = np.zeros((n_lat, n_lon), dtype=float)
        for i, lat in enumerate(lats):
            lat_row = np.full(n_lon, lat)
            lon_row = lons
            grid_latlon = np.column_stack([lat_row, lon_row])
            d_km_row, _ = compute_nearest_region_distances(grid_latlon, region_latlon)
            X_row = np.column_stack([np.ones(n_lon), d_km_row / 1000.0, np.full(n_lon, ref_log_pop)])
            linear = X_row @ beta
            resid_row = gpr.predict(grid_latlon)
            gp_surface[i, :] = linear + resid_row

        rasterize_global_surface(lat_min, lat_max, lon_min, lon_max, resolution_deg, gp_surface, gp_pred_tif)

    # CAR predicted surface (IDW interpolation from city predictions)
    car_pred_tif = paths.gis / "ai_research_pred_car.tif"
    car_pred_fp = paths.tables / "model_car_predictions.csv"
    if car_pred_fp.exists():
        dfc = pd.read_csv(car_pred_fp)
        # Use predicted values at city nodes
        pts = np.column_stack([dfc["lat"].to_numpy(), dfc["lng"].to_numpy()])
        vals = dfc["car_pred"].to_numpy()

        # Build KDTree in 3D for neighbor search
        def to_xyz(lat, lon):
            lat_r = np.radians(lat)
            lon_r = np.radians(lon)
            x = np.cos(lat_r) * np.cos(lon_r)
            y = np.cos(lat_r) * np.sin(lon_r)
            z = np.sin(lat_r)
            return np.column_stack([x, y, z])

        tree = cKDTree(to_xyz(pts[:, 0], pts[:, 1]))

        car_surface = np.zeros((n_lat, n_lon), dtype=float)
        for i, lat in enumerate(lats):
            lat_row = np.full(n_lon, lat)
            lon_row = lons
            xyz = to_xyz(lat_row, lon_row)
            d_chord, idx = tree.query(xyz, k=8)
            # convert chord to km approx
            theta = 2 * np.arcsin(np.clip(d_chord / 2, 0, 1))
            d_km = 6371.0088 * theta
            # IDW weights
            w = 1.0 / np.maximum(d_km, 50.0) ** 2  # floor at 50km to avoid blow-up
            w_sum = w.sum(axis=1)
            pred = (w * vals[idx]).sum(axis=1) / w_sum
            car_surface[i, :] = pred

        rasterize_global_surface(lat_min, lat_max, lon_min, lon_max, resolution_deg, car_surface, car_pred_tif)

    return {
        "dist_surface_tif": str(dist_tif),
        "gp_pred_tif": str(gp_pred_tif),
        "car_pred_tif": str(car_pred_tif),
        "resolution_deg": str(resolution_deg),
    }


# -------------------------
# Step 8: Figures
# -------------------------
def _savefig(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=EXPORT_DPI, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def _create_map_figure(
    *,
    figsize_key: str,
    kicker: str,
    title: str,
    subtitle: str,
) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=FIGURE_SIZES[figsize_key], facecolor=PALETTE["figure_bg"])
    ax.set_facecolor(PALETTE["panel_bg"])
    fig.subplots_adjust(left=0.03, right=0.97, top=0.84, bottom=0.09)
    fig.text(
        0.03,
        0.95,
        kicker.upper(),
        fontsize=TYPOGRAPHY["kicker_size"],
        fontweight="bold",
        color=PALETTE["ai_edge"],
        family=TYPOGRAPHY["body_family"],
    )
    fig.text(
        0.03,
        0.915,
        title,
        fontsize=TYPOGRAPHY["title_size"],
        fontweight="bold",
        color=PALETTE["text_primary"],
        family=TYPOGRAPHY["title_family"],
    )
    fig.text(
        0.03,
        0.878,
        subtitle,
        fontsize=TYPOGRAPHY["subtitle_size"],
        color=PALETTE["text_muted"],
        family=TYPOGRAPHY["body_family"],
    )
    return fig, ax


def _create_chart_figure(
    *,
    figsize_key: str,
    kicker: str,
    title: str,
    subtitle: str,
    right_margin: float = 0.78,
    bottom_margin: float = 0.18,
) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=FIGURE_SIZES[figsize_key], facecolor=PALETTE["figure_bg"])
    ax.set_facecolor(PALETTE["panel_bg"])
    fig.subplots_adjust(left=0.09, right=right_margin, top=0.81, bottom=bottom_margin)
    fig.text(
        0.09,
        0.95,
        kicker.upper(),
        fontsize=TYPOGRAPHY["kicker_size"],
        fontweight="bold",
        color=PALETTE["ai_edge"],
        family=TYPOGRAPHY["body_family"],
    )
    fig.text(
        0.09,
        0.915,
        title,
        fontsize=TYPOGRAPHY["title_size"],
        fontweight="bold",
        color=PALETTE["text_primary"],
        family=TYPOGRAPHY["title_family"],
    )
    fig.text(
        0.09,
        0.878,
        subtitle,
        fontsize=TYPOGRAPHY["subtitle_size"],
        color=PALETTE["text_muted"],
        family=TYPOGRAPHY["body_family"],
    )
    return fig, ax


def _style_chart_axis(ax: plt.Axes, *, xlabel: str, ylabel: str) -> None:
    ax.set_xlabel(
        xlabel,
        color=PALETTE["text_primary"],
        family=TYPOGRAPHY["body_family"],
        labelpad=8,
    )
    ax.set_ylabel(
        ylabel,
        color=PALETTE["text_primary"],
        family=TYPOGRAPHY["body_family"],
        labelpad=8,
    )
    ax.grid(axis="y", color=PALETTE["gridline"], linewidth=0.8, alpha=0.85)
    ax.grid(axis="x", color=PALETTE["gridline"], linewidth=0.6, alpha=0.35)
    ax.set_axisbelow(True)
    for spine_name in ("top", "right"):
        ax.spines[spine_name].set_visible(False)
    for spine_name in ("left", "bottom"):
        ax.spines[spine_name].set_color(PALETTE["panel_edge"])
        ax.spines[spine_name].set_linewidth(1.0)
    ax.tick_params(colors=PALETTE["text_muted"])


def _format_share(value: float) -> str:
    return f"{value * 100:.0f}%"


def _distance_tick_formatter(value: float, _position: float) -> str:
    if value < 1:
        return f"{value:.1f}"
    return f"{int(round(value)):,}"


def _distance_band_transform(values: Iterable[float]) -> np.ndarray:
    return np.log10(np.asarray(list(values), dtype=float) + 1.0)


def _configure_log_distance_axis(ax: plt.Axes, values: Iterable[float]) -> None:
    cleaned = np.asarray(list(values), dtype=float)
    cleaned = cleaned[np.isfinite(cleaned) & (cleaned > 0)]
    if cleaned.size == 0:
        return

    lower = 0.1 if float(cleaned.min()) < 1 else 1.0
    upper = float(cleaned.max()) * 1.08
    ax.set_xscale("log")
    ax.set_xlim(lower, upper)
    candidate_ticks = [0.1, 1, 10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
    ticks = [tick for tick in candidate_ticks if lower <= tick <= upper * 1.02]
    if len(ticks) >= 2:
        ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(FuncFormatter(_distance_tick_formatter))
    ax.minorticks_off()


def _configure_distance_band_axis(ax: plt.Axes, raw_values: Iterable[float]) -> None:
    cleaned = np.asarray(list(raw_values), dtype=float)
    cleaned = cleaned[np.isfinite(cleaned) & (cleaned >= 0)]
    if cleaned.size == 0:
        return

    transformed = _distance_band_transform(cleaned)
    upper = float(transformed.max())
    ax.set_xlim(0.0, upper * 1.03 if upper > 0 else 1.0)
    tick_values = [0, 10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
    ticks = [math.log10(tick + 1.0) for tick in tick_values if tick <= float(cleaned.max()) * 1.05]
    labels = [f"{tick:,}" for tick in tick_values if tick <= float(cleaned.max()) * 1.05]
    if len(ticks) >= 2:
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)


def _weighted_quantile(values: np.ndarray, weights: np.ndarray, quantile: float) -> float:
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    mask = np.isfinite(values) & np.isfinite(weights) & (weights >= 0)
    values = values[mask]
    weights = weights[mask]
    if len(values) == 0 or float(weights.sum()) <= 0:
        return float("nan")

    order = np.argsort(values)
    values = values[order]
    weights = weights[order]
    cumulative = np.cumsum(weights)
    cutoff = float(quantile) * float(cumulative[-1])
    index = min(int(np.searchsorted(cumulative, cutoff, side="left")), len(values) - 1)
    return float(values[index])


def _label_horizontal_bars(ax: plt.Axes, y_positions: np.ndarray, values: List[float]) -> None:
    span = max(max((abs(v) for v in values), default=0.0), 0.05)
    for y_pos, value in zip(y_positions, values):
        direction = 1 if value >= 0 else -1
        x_pos = value + direction * span * 0.04
        ax.text(
            x_pos,
            y_pos,
            f"{value:+.3f}",
            va="center",
            ha="left" if direction > 0 else "right",
            fontsize=8.5,
            color=PALETTE["text_primary"],
            family=TYPOGRAPHY["body_family"],
        )


def _style_world_axis(
    ax: plt.Axes,
    bbox: Optional[Tuple[float, float, float, float]] = None,
) -> None:
    if bbox is None:
        ax.set_xlim(-180, 180)
        ax.set_ylim(-60, 85)
    else:
        ax.set_xlim(bbox[0], bbox[2])
        ax.set_ylim(bbox[1], bbox[3])
    for lon in range(-120, 181, 60):
        ax.axvline(lon, color=PALETTE["gridline"], linewidth=0.6, alpha=0.5, zorder=0)
    for lat in (-30, 0, 30, 60):
        ax.axhline(lat, color=PALETTE["gridline"], linewidth=0.6, alpha=0.5, zorder=0)
    ax.set_axis_off()


def _plot_world_base(
    ax: plt.Axes,
    world: gpd.GeoDataFrame,
    bbox: Optional[Tuple[float, float, float, float]] = None,
) -> None:
    world_layer = world if bbox is None else world.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
    world_layer.plot(
        ax=ax,
        color=PALETTE["country_fill"],
        edgecolor=PALETTE["country_edge"],
        linewidth=0.5,
        zorder=1,
    )
    _style_world_axis(ax, bbox=bbox)


def _plot_world_outline(
    ax: plt.Axes,
    world: gpd.GeoDataFrame,
    bbox: Optional[Tuple[float, float, float, float]] = None,
) -> None:
    world_layer = world if bbox is None else world.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
    world_layer.plot(
        ax=ax,
        color="none",
        edgecolor=PALETTE["panel_edge"],
        linewidth=0.45,
        zorder=4,
    )
    _style_world_axis(ax, bbox=bbox)


def _scale_marker_sizes(values: pd.Series, min_size: float, max_size: float) -> np.ndarray:
    arr = np.nan_to_num(values.to_numpy(dtype=float), nan=0.0, posinf=0.0, neginf=0.0)
    arr = np.log1p(np.maximum(arr, 0.0))
    if arr.max() == arr.min():
        return np.full(len(arr), min_size, dtype=float)
    scaled = (arr - arr.min()) / (arr.max() - arr.min())
    return min_size + scaled * (max_size - min_size)


def _format_int(value: float) -> str:
    return f"{int(round(float(value))):,}"


def _format_km(value: float) -> str:
    return f"{float(value):,.0f} km"


def _add_info_panel(ax: plt.Axes, heading: str, lines: Iterable[str]) -> None:
    body = "\n".join([heading, *lines])
    ax.text(
        1.01,
        0.98,
        body,
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=8.5,
        color=PALETTE["text_primary"],
        family=TYPOGRAPHY["body_family"],
        linespacing=1.45,
        bbox=PANEL_BBOX,
    )


def _add_footer(fig: plt.Figure, note: str) -> None:
    fig.text(
        0.03,
        0.035,
        note,
        fontsize=TYPOGRAPHY["note_size"],
        color=PALETTE["text_muted"],
        family=TYPOGRAPHY["body_family"],
    )


def _marker_legend(
    *,
    ax: plt.Axes,
    title: str,
    labels: List[str],
    sizes: List[float],
    color: str,
    edgecolor: str,
    bbox_to_anchor: Tuple[float, float],
) -> None:
    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markerfacecolor=color,
            markeredgecolor=edgecolor,
            markeredgewidth=0.8,
            alpha=0.85,
            markersize=max(4.5, math.sqrt(size)),
            label=label,
        )
        for label, size in zip(labels, sizes)
    ]
    legend = ax.legend(
        handles=handles,
        title=title,
        loc="lower left",
        bbox_to_anchor=bbox_to_anchor,
        frameon=True,
        facecolor=PALETTE["panel_bg"],
        edgecolor=PALETTE["panel_edge"],
        title_fontsize=8,
        fontsize=8,
    )
    ax.add_artist(legend)


def _size_legend_from_series(
    *,
    ax: plt.Axes,
    title: str,
    series: pd.Series,
    min_size: float,
    max_size: float,
    color: str,
    edgecolor: str,
    bbox_to_anchor: Tuple[float, float] = (0.01, 0.03),
) -> None:
    cleaned = series.replace([np.inf, -np.inf], np.nan).dropna()
    if cleaned.empty:
        return
    quantiles = cleaned.quantile([0.25, 0.5, 0.9]).to_numpy(dtype=float)
    labels = [_format_int(v) for v in quantiles]
    sizes = _scale_marker_sizes(pd.Series(quantiles), min_size, max_size).tolist()
    _marker_legend(
        ax=ax,
        title=title,
        labels=labels,
        sizes=sizes,
        color=color,
        edgecolor=edgecolor,
        bbox_to_anchor=bbox_to_anchor,
    )


def _build_quadrant_frame(cities_ai_unique: gpd.GeoDataFrame) -> Tuple[gpd.GeoDataFrame, float, float]:
    df = cities_ai_unique.copy()
    ai_threshold = float(np.nanmedian(df["openalex_ai_works_recent"]))
    access_threshold = float(np.nanmedian(df["access_score"]))
    quadrant_codes = (
        (df["openalex_ai_works_recent"] >= ai_threshold).astype(int) * 2
        + (df["access_score"] >= access_threshold).astype(int)
    )
    labels = {
        0: "Low AI / Low access",
        1: "Low AI / High access",
        2: "High AI / Low access",
        3: "High AI / High access",
    }
    df["quadrant_label"] = quadrant_codes.map(labels)
    return df, ai_threshold, access_threshold


def _annotate_map_labels(
    ax: plt.Axes,
    frame: gpd.GeoDataFrame,
    *,
    label_column: str,
    offsets: List[Tuple[float, float]],
) -> None:
    for row, offset in zip(frame.itertuples(index=False), offsets):
        geometry = row.geometry
        ax.annotate(
            getattr(row, label_column),
            (geometry.x, geometry.y),
            xytext=offset,
            textcoords="offset points",
            fontsize=8,
            color=PALETTE["text_primary"],
            family=TYPOGRAPHY["body_family"],
            bbox={
                "boxstyle": "round,pad=0.2,rounding_size=0.1",
                "facecolor": PALETTE["panel_bg"],
                "edgecolor": PALETTE["panel_edge"],
                "linewidth": 0.8,
            },
            arrowprops={
                "arrowstyle": "-",
                "color": PALETTE["panel_edge"],
                "linewidth": 0.7,
            },
            zorder=7,
        )


def _load_surface_raster(path: Path) -> Tuple[np.ndarray, Tuple[float, float, float, float]]:
    with rasterio.open(path) as src:
        arr = src.read(1).astype(float)
        bounds = (src.bounds.left, src.bounds.bottom, src.bounds.right, src.bounds.top)
    return arr, bounds


def _plot_surface_raster(
    ax: plt.Axes,
    arr: np.ndarray,
    bounds: Tuple[float, float, float, float],
    *,
    cmap: mcolors.Colormap,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
) -> mpl.image.AxesImage:
    return ax.imshow(
        np.ma.masked_invalid(arr),
        extent=(bounds[0], bounds[2], bounds[1], bounds[3]),
        origin="upper",
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        interpolation="bilinear",
        alpha=0.9,
        zorder=1,
    )


def _create_priority_deep_dive_figure(
    *,
    world: gpd.GeoDataFrame,
    regions: gpd.GeoDataFrame,
    access_frame: gpd.GeoDataFrame,
    priority_frame: gpd.GeoDataFrame,
    bbox: Tuple[float, float, float, float],
    kicker: str,
    title: str,
    subtitle: str,
    panel_lines: List[str],
    footer_note: str,
    top_n: int = 60,
) -> Tuple[plt.Figure, plt.Axes, gpd.GeoDataFrame]:
    fig, ax = _create_map_figure(
        figsize_key="map_deep_dive",
        kicker=kicker,
        title=title,
        subtitle=subtitle,
    )
    _plot_world_base(ax, world, bbox=bbox)

    access_plot = access_frame.copy()
    access_plot["marker_size"] = _scale_marker_sizes(access_plot["population"].fillna(0), 8, 48)
    access_norm = mcolors.Normalize(
        vmin=float(access_plot["dist_km_nearest_region"].min()),
        vmax=float(access_plot["dist_km_nearest_region"].max()),
    )
    access_plot.plot(
        ax=ax,
        column="dist_km_nearest_region",
        cmap=ACCESS_CMAP,
        vmin=access_norm.vmin,
        vmax=access_norm.vmax,
        markersize=access_plot["marker_size"],
        alpha=0.38,
        linewidth=0,
        zorder=2,
    )

    priority_plot = priority_frame.sort_values("priority_rank").copy()
    priority_top = priority_plot.head(top_n).copy()
    priority_rest = priority_plot.iloc[top_n:].copy()
    if not priority_rest.empty:
        priority_rest.plot(
            ax=ax,
            color=PALETTE["neutral"],
            markersize=8,
            alpha=0.16,
            linewidth=0,
            zorder=3,
        )
    regions.plot(
        ax=ax,
        color=PALETTE["cloud_region"],
        markersize=48,
        marker="x",
        alpha=0.9,
        linewidth=1.2,
        zorder=5,
    )
    if not priority_top.empty:
        priority_top["marker_size"] = _scale_marker_sizes(priority_top["population"].fillna(0), 34, 220)
        priority_top.plot(
            ax=ax,
            color=PALETTE["priority_fill"],
            markersize=priority_top["marker_size"],
            alpha=0.94,
            linewidth=0.5,
            edgecolor=PALETTE["panel_bg"],
            zorder=6,
        )
        _size_legend_from_series(
            ax=ax,
            title="Population (top priority cities)",
            series=priority_top["population"],
            min_size=34,
            max_size=220,
            color=PALETTE["priority_fill"],
            edgecolor=PALETTE["panel_bg"],
        )
    colorbar = fig.colorbar(
        plt.cm.ScalarMappable(norm=access_norm, cmap=ACCESS_CMAP),
        ax=ax,
        fraction=0.03,
        pad=0.02,
        shrink=0.78,
    )
    colorbar.set_label("Distance to nearest cloud region (km)", color=PALETTE["text_primary"])
    colorbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
    legend = ax.legend(
        handles=[
            Line2D(
                [0],
                [0],
                marker="o",
                linestyle="",
                markerfacecolor=PALETTE["chart_primary"],
                markeredgecolor="none",
                alpha=0.4,
                markersize=6,
                label="Large-city backdrop",
            ),
            Line2D(
                [0],
                [0],
                marker="o",
                linestyle="",
                markerfacecolor=PALETTE["priority_fill"],
                markeredgecolor=PALETTE["panel_bg"],
                markersize=7,
                label=f"Top {min(top_n, len(priority_plot))} priority cities",
            ),
            Line2D(
                [0],
                [0],
                marker="x",
                linestyle="",
                color=PALETTE["cloud_region"],
                markeredgewidth=1.2,
                markersize=8,
                label="Cloud region",
            ),
        ],
        loc="lower left",
        bbox_to_anchor=(0.17, 0.03),
        frameon=True,
        facecolor=PALETTE["panel_bg"],
        edgecolor=PALETTE["panel_edge"],
        fontsize=8,
    )
    ax.add_artist(legend)
    _add_info_panel(ax, "Quick read", panel_lines)
    _add_footer(fig, footer_note)
    return fig, ax, priority_top


def _copy_figures_to_report(paths: Paths, figure_names: Iterable[str]) -> Path:
    report_fig_dir = paths.root / "report" / "figures"
    report_fig_dir.mkdir(parents=True, exist_ok=True)
    for fname in figure_names:
        fp = paths.figures / fname
        if fp.exists():
            (report_fig_dir / fname).write_bytes(fp.read_bytes())
    return report_fig_dir


def step_figures(paths: Paths) -> Dict[str, str]:
    """
    Generate key figures used in report.

    Outputs at least:
      - outputs/figures/fig1_access_map.png
      - outputs/figures/fig2_ai_map.png
      - outputs/figures/fig3_quadrants.png
      - outputs/figures/fig11_hotspot_map.png
      - outputs/figures/fig12_priority_cities_map.png
      - outputs/figures/fig4_scatter_ai_vs_dist.png
      - outputs/figures/fig5_coef_compare.png
      - outputs/figures/fig6_sea_zoom.png
    """
    ensure_dirs(paths)
    apply_matplotlib_style()
    world_fp = paths.raw / "ne_110m_admin_0_countries.geojson"
    if not world_fp.exists():
        raise FileNotFoundError(f"Missing {world_fp}. Download Natural Earth countries GeoJSON into data/raw/.")
    world = gpd.read_file(world_fp)

    regions = gpd.read_file(paths.processed / "cloud_regions.gpkg", layer="regions")
    cities_access = gpd.read_file(paths.gis / "ai_access_cities.gpkg", layer="cities_access")
    cities_ai = gpd.read_file(paths.gis / "ai_access_ai_cities.gpkg", layer="cities_ai") if (paths.gis / "ai_access_ai_cities.gpkg").exists() else None
    cities_ai_unique = aggregate_ai_city_matches(cities_ai) if cities_ai is not None else None
    hotspots = gpd.read_file(paths.gis / "cities_with_hotspots.geojson") if (paths.gis / "cities_with_hotspots.geojson").exists() else None
    priority_cities = gpd.read_file(paths.gis / "priority_cities.geojson") if (paths.gis / "priority_cities.geojson").exists() else None
    generated_figure_names = [
        "fig1_access_map.png",
        "fig2_ai_map.png",
        "fig3_quadrants.png",
        "fig11_hotspot_map.png",
        "fig12_priority_cities_map.png",
        "fig4_scatter_ai_vs_dist.png",
        "fig5_coef_compare.png",
        "morans_i_scatterplot.png",
        "fig6_sea_zoom.png",
        "fig7_distance_hist.png",
        "fig8_ai_weighted_distance.png",
        "fig9_distance_surface.png",
        "fig10_gp_surface.png",
        "fig13_subsaharan_africa_deep_dive.png",
        "fig14_latin_america_deep_dive.png",
    ]
    access_norm = mcolors.Normalize(
        vmin=float(cities_access["dist_km_nearest_region"].min()),
        vmax=float(cities_access["dist_km_nearest_region"].max()),
    )

    # 1) Access map
    fig, ax = _create_map_figure(
        figsize_key="map_feature",
        kicker="Figure 1",
        title="Compute accessibility remains uneven across the global city system",
        subtitle="Marker area scales with city population and color tracks distance to the nearest deployed cloud region.",
    )
    _plot_world_base(ax, world)
    access_sizes = _scale_marker_sizes(cities_access["population"].fillna(0), 6, 80)
    cities_access.plot(
        ax=ax,
        column="dist_km_nearest_region",
        cmap=ACCESS_CMAP,
        vmin=access_norm.vmin,
        vmax=access_norm.vmax,
        markersize=access_sizes,
        alpha=0.82,
        linewidth=0.12,
        edgecolor=PALETTE["panel_bg"],
        zorder=3,
    )
    regions.plot(
        ax=ax,
        color=PALETTE["cloud_region"],
        markersize=42,
        marker="x",
        alpha=0.9,
        linewidth=1.2,
        zorder=4,
    )
    _size_legend_from_series(
        ax=ax,
        title="Population",
        series=cities_access["population"],
        min_size=6,
        max_size=80,
        color=PALETTE["cloud_region"],
        edgecolor=PALETTE["panel_bg"],
    )
    region_legend = ax.legend(
        handles=[
            Line2D(
                [0],
                [0],
                marker="x",
                color=PALETTE["cloud_region"],
                linestyle="",
                markeredgewidth=1.3,
                markersize=8,
                label="Cloud region",
            )
        ],
        loc="lower left",
        bbox_to_anchor=(0.19, 0.03),
        frameon=True,
        facecolor=PALETTE["panel_bg"],
        edgecolor=PALETTE["panel_edge"],
    )
    ax.add_artist(region_legend)
    access_cbar = fig.colorbar(
        plt.cm.ScalarMappable(norm=access_norm, cmap=ACCESS_CMAP),
        ax=ax,
        fraction=0.03,
        pad=0.02,
        shrink=0.78,
    )
    access_cbar.set_label("Distance to nearest cloud region (km)", color=PALETTE["text_primary"])
    access_cbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
    _add_info_panel(
        ax,
        "Quick read",
        [
            f"{_format_int(len(cities_access))} large cities in the frame",
            f"Median distance: {_format_km(cities_access['dist_km_nearest_region'].median())}",
            f"Median access score: {cities_access['access_score'].median():.2f}",
        ],
    )
    _add_footer(
        fig,
        "Sources: Natural Earth, hyperscaler region inventory, and the repo's processed city layer. Descriptive infrastructure geography only.",
    )
    out1 = paths.figures / "fig1_access_map.png"
    _savefig(fig, out1)

    # 2) AI research map
    if cities_ai_unique is not None:
        fig, ax = _create_map_figure(
            figsize_key="map_feature",
            kicker="Figure 2",
            title="Recent AI research activity is concentrated in cities already near cloud regions",
            subtitle="Unique matched AI cities are sized by recent OpenAlex output and colored by their distance to the nearest cloud region.",
        )
        _plot_world_base(ax, world)
        regions.plot(
            ax=ax,
            color=PALETTE["cloud_region"],
            markersize=40,
            marker="x",
            alpha=0.9,
            linewidth=1.2,
            zorder=4,
        )
        ai_sizes = _scale_marker_sizes(cities_ai_unique["openalex_ai_works_recent"].fillna(0), 20, 240)
        cities_ai_unique.plot(
            ax=ax,
            column="dist_km_nearest_region",
            cmap=ACCESS_CMAP,
            vmin=access_norm.vmin,
            vmax=access_norm.vmax,
            markersize=ai_sizes,
            alpha=0.92,
            linewidth=0.35,
            edgecolor=PALETTE["panel_bg"],
            zorder=5,
        )
        ax.set_title("AI research activity (OpenAlex): recent AI works by city (size ∝ sqrt(count))")
        _size_legend_from_series(
            ax=ax,
            title="Recent AI works",
            series=cities_ai_unique["openalex_ai_works_recent"],
            min_size=20,
            max_size=240,
            color=PALETTE["ai_fill"],
            edgecolor=PALETTE["panel_bg"],
        )
        ai_region_legend = ax.legend(
            handles=[
                Line2D(
                    [0],
                    [0],
                    marker="x",
                    color=PALETTE["cloud_region"],
                    linestyle="",
                    markeredgewidth=1.3,
                    markersize=8,
                    label="Cloud region",
                )
            ],
            loc="lower left",
            bbox_to_anchor=(0.2, 0.03),
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
        )
        ax.add_artist(ai_region_legend)
        ai_cbar = fig.colorbar(
            plt.cm.ScalarMappable(norm=access_norm, cmap=ACCESS_CMAP),
            ax=ax,
            fraction=0.03,
            pad=0.02,
            shrink=0.78,
        )
        ai_cbar.set_label("Distance to nearest cloud region (km)", color=PALETTE["text_primary"])
        ai_cbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
        total_ai_works = float(cities_ai_unique["openalex_ai_works_recent"].sum())
        top25_share = 0.0
        if total_ai_works > 0:
            top25_share = (
                cities_ai_unique["openalex_ai_works_recent"].sort_values(ascending=False).head(25).sum()
                / total_ai_works
            )
        _add_info_panel(
            ax,
            "Quick read",
            [
                f"{_format_int(len(cities_ai_unique))} unique AI-city matches",
                f"Median distance: {_format_km(cities_ai_unique['dist_km_nearest_region'].median())}",
                f"Top 25 cities account for {top25_share:.0%} of recent AI works",
            ],
        )
        _add_footer(
            fig,
            "OpenAlex matches are aggregated to unique cities before mapping. The figure is descriptive and does not imply that proximity causes research output.",
        )
        ax.set_title("")
        out2 = paths.figures / "fig2_ai_map.png"
        _savefig(fig, out2)

    # 3) Quadrant plot (high AI vs high access)
    if cities_ai_unique is not None:
        df, ai_thr, access_thr = _build_quadrant_frame(cities_ai_unique)
        df["marker_size"] = _scale_marker_sizes(df["openalex_ai_works_recent"].fillna(0), 18, 170)
        fig, ax = _create_map_figure(
            figsize_key="map_feature",
            kicker="Figure 3",
            title="AI hubs and high-access cities do not fully overlap",
            subtitle=(
                f"Matched AI cities are split at the medians: {ai_thr:,.0f} recent works and "
                f"{access_thr:.2f} access score. Marker area scales with recent AI works."
            ),
        )
        _plot_world_base(ax, world)
        regions.plot(
            ax=ax,
            color=PALETTE["cloud_region"],
            markersize=34,
            marker="x",
            alpha=0.85,
            linewidth=1.0,
            zorder=4,
        )
        legend_handles: List[Line2D] = []
        for label, color in QUADRANT_COLORS.items():
            sub = df[df["quadrant_label"] == label]
            if sub.empty:
                continue
            sub.plot(
                ax=ax,
                color=color,
                markersize=sub["marker_size"],
                alpha=0.9,
                linewidth=0.3,
                edgecolor=PALETTE["panel_bg"],
                zorder=5,
            )
            legend_handles.append(
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=color,
                    markeredgecolor=PALETTE["panel_bg"],
                    markersize=7,
                    label=f"{label} ({len(sub)})",
                )
            )
        legend_handles.append(
            Line2D(
                [0],
                [0],
                marker="x",
                linestyle="",
                color=PALETTE["cloud_region"],
                markeredgewidth=1.2,
                markersize=8,
                label="Cloud region",
            )
        )
        quadrant_legend = ax.legend(
            handles=legend_handles,
            loc="lower left",
            bbox_to_anchor=(0.01, 0.02),
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        ax.add_artist(quadrant_legend)
        quadrant_counts = df["quadrant_label"].value_counts()
        _add_info_panel(
            ax,
            "Quadrant counts",
            [
                f"High AI / High access: {_format_int(quadrant_counts.get('High AI / High access', 0))}",
                f"High AI / Low access: {_format_int(quadrant_counts.get('High AI / Low access', 0))}",
                f"Low AI / High access: {_format_int(quadrant_counts.get('Low AI / High access', 0))}",
                f"Low AI / Low access: {_format_int(quadrant_counts.get('Low AI / Low access', 0))}",
            ],
        )
        _add_footer(
            fig,
            "Quadrants are a descriptive sorting device, not a causal typology. They show where research intensity and compute accessibility co-occur or diverge.",
        )
        out3 = paths.figures / "fig3_quadrants.png"
        _savefig(fig, out3)

    # 3b) Hot-spot map
    if hotspots is not None:
        hotspot_plot = hotspots.copy()
        hotspot_plot["marker_size"] = _scale_marker_sizes(
            hotspot_plot["openalex_ai_works_recent"].fillna(0), 22, 190
        )
        hotspot_plot.loc[hotspot_plot["hotspot_class"] == "not_significant", "marker_size"] = 18
        hotspot_labels = {
            "hot_spot_99": "Hot spot (99%)",
            "hot_spot_95": "Hot spot (95%)",
            "not_significant": "Not significant",
            "cold_spot_95": "Cold spot (95%)",
            "cold_spot_99": "Cold spot (99%)",
        }
        fig, ax = _create_map_figure(
            figsize_key="map_feature",
            kicker="Figure 11",
            title="Local AI research hot spots are concentrated in a small set of cities",
            subtitle="Local Gi* is calculated on unique matched AI cities. Color shows cluster class and marker area scales with recent AI works.",
        )
        _plot_world_base(ax, world)
        regions.plot(
            ax=ax,
            color=PALETTE["cloud_region"],
            markersize=34,
            marker="x",
            alpha=0.85,
            linewidth=1.0,
            zorder=4,
        )
        hotspot_handles: List[Line2D] = []
        for hotspot_class in ["cold_spot_99", "cold_spot_95", "not_significant", "hot_spot_95", "hot_spot_99"]:
            sub = hotspot_plot[hotspot_plot["hotspot_class"] == hotspot_class]
            if sub.empty:
                continue
            alpha = 0.35 if hotspot_class == "not_significant" else 0.92
            sub.plot(
                ax=ax,
                color=HOTSPOT_COLORS[hotspot_class],
                markersize=sub["marker_size"],
                alpha=alpha,
                linewidth=0.3,
                edgecolor=PALETTE["panel_bg"],
                zorder=5,
            )
            hotspot_handles.append(
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=HOTSPOT_COLORS[hotspot_class],
                    markeredgecolor=PALETTE["panel_bg"],
                    markersize=7,
                    alpha=alpha,
                    label=f"{hotspot_labels[hotspot_class]} ({len(sub)})",
                )
            )
        hotspot_handles.append(
            Line2D(
                [0],
                [0],
                marker="x",
                linestyle="",
                color=PALETTE["cloud_region"],
                markeredgewidth=1.2,
                markersize=8,
                label="Cloud region",
            )
        )
        hotspot_legend = ax.legend(
            handles=hotspot_handles,
            loc="lower left",
            bbox_to_anchor=(0.01, 0.02),
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        ax.add_artist(hotspot_legend)
        top_hot = hotspot_plot[hotspot_plot["hotspot_class"].isin(["hot_spot_95", "hot_spot_99"])].sort_values(
            ["hotspot_rank", "gi_star_z"],
            ascending=[True, False],
        )
        top_cold = hotspot_plot[hotspot_plot["hotspot_class"].isin(["cold_spot_95", "cold_spot_99"])].sort_values(
            "gi_star_z"
        )
        hotspot_lines = [
            f"Significant hot spots: {_format_int(len(top_hot))}",
            f"Significant cold spots: {_format_int(len(top_cold))}",
        ]
        if not top_hot.empty:
            hotspot_lines.append(f"Top hot spot: {top_hot.iloc[0]['city']} ({top_hot.iloc[0]['country']})")
        if not top_cold.empty:
            hotspot_lines.append(f"Strongest cold spot: {top_cold.iloc[0]['city']} ({top_cold.iloc[0]['country']})")
        _add_info_panel(ax, "Quick read", hotspot_lines)
        _add_footer(
            fig,
            "The Gi* surface highlights local clustering in observed AI research activity. It should be read as descriptive spatial concentration rather than evidence of a causal treatment effect.",
        )
        out11 = paths.figures / "fig11_hotspot_map.png"
        _savefig(fig, out11)

    # 3c) Priority-city map
    if priority_cities is not None:
        priority_plot = priority_cities.copy().sort_values("priority_rank")
        priority_top = priority_plot.head(100).copy()
        priority_rest = priority_plot.iloc[100:].copy()
        priority_top["marker_size"] = _scale_marker_sizes(priority_top["population"].fillna(0), 28, 230)
        threshold_km = float(priority_plot["priority_distance_threshold_km"].iloc[0]) if not priority_plot.empty else float("nan")
        fig, ax = _create_map_figure(
            figsize_key="map_feature",
            kicker="Figure 12",
            title="Priority cities stack long compute distances on top of zero observed AI output",
            subtitle=(
                f"Cities qualify when observed AI works are zero and distance exceeds the upper-quartile threshold "
                f"({_format_km(threshold_km)}). The top 100 ranks are emphasized."
            ),
        )
        _plot_world_base(ax, world)
        if not priority_rest.empty:
            priority_rest.plot(
                ax=ax,
                color=PALETTE["neutral"],
                markersize=10,
                alpha=0.18,
                linewidth=0,
                zorder=2,
            )
        regions.plot(
            ax=ax,
            color=PALETTE["cloud_region"],
            markersize=34,
            marker="x",
            alpha=0.85,
            linewidth=1.0,
            zorder=4,
        )
        if not priority_top.empty:
            priority_top.plot(
                ax=ax,
                column="priority_rank",
                cmap=PRIORITY_CMAP,
                vmin=1,
                vmax=max(len(priority_top), 1),
                markersize=priority_top["marker_size"],
                alpha=0.94,
                linewidth=0.4,
                edgecolor=PALETTE["panel_bg"],
                zorder=5,
            )
            priority_cbar = fig.colorbar(
                plt.cm.ScalarMappable(
                    norm=mcolors.Normalize(vmin=1, vmax=max(len(priority_top), 1)),
                    cmap=PRIORITY_CMAP,
                ),
                ax=ax,
                fraction=0.03,
                pad=0.02,
                shrink=0.78,
            )
            priority_cbar.set_label("Priority rank (1 = highest)", color=PALETTE["text_primary"])
            priority_cbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
            _size_legend_from_series(
                ax=ax,
                title="Population (top 100)",
                series=priority_top["population"],
                min_size=28,
                max_size=230,
                color=PRIORITY_CMAP(0.18),
                edgecolor=PALETTE["panel_bg"],
            )
        priority_legend = ax.legend(
            handles=[
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=PALETTE["neutral"],
                    markeredgecolor="none",
                    markersize=6,
                    alpha=0.35,
                    label="All qualifying cities",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=PRIORITY_CMAP(0.18),
                    markeredgecolor=PALETTE["panel_bg"],
                    markersize=7,
                    label="Top 100 highlighted",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="x",
                    linestyle="",
                    color=PALETTE["cloud_region"],
                    markeredgewidth=1.2,
                    markersize=8,
                    label="Cloud region",
                ),
            ],
            loc="lower left",
            bbox_to_anchor=(0.18, 0.03),
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        ax.add_artist(priority_legend)
        _add_info_panel(
            ax,
            "Quick read",
            [
                f"{_format_int(len(priority_plot))} cities meet the rule",
                f"{_format_int(priority_plot['country'].nunique())} countries represented",
                "Ranking sorts by population first, then compute distance",
            ],
        )
        _add_footer(
            fig,
            "Priority cities are a policy-screening layer based on the delivered overlay: no observed AI works plus weak compute proximity. They are not a causal forecast.",
        )
        out12 = paths.figures / "fig12_priority_cities_map.png"
        _savefig(fig, out12)

    # 4) Scatter: AI vs distance
    if cities_ai is not None:
        scatter_frame = cities_ai.dropna(
            subset=["dist_km_nearest_region", "log_ai_works", "population", "openalex_ai_works_recent"]
        ).copy()
        scatter_frame = scatter_frame[scatter_frame["dist_km_nearest_region"] > 0].copy()
        fig, ax = _create_chart_figure(
            figsize_key="chart_feature",
            kicker="Figure 4",
            title="Most high-output AI cities remain close to deployed cloud regions",
            subtitle="Points use the matched OpenAlex city sample; marker area scales with population and the line shows equal-count bin medians on a log-scaled distance axis.",
        )
        _style_chart_axis(
            ax,
            xlabel="Distance to nearest hyperscaler region (km, log scale)",
            ylabel="log(1 + AI works) (OpenAlex)",
        )
        ax.axvspan(
            float(scatter_frame["dist_km_nearest_region"].min()),
            250,
            color=PALETTE["chart_secondary_fill"],
            alpha=0.14,
            zorder=0,
        )
        scatter_sizes = _scale_marker_sizes(scatter_frame["population"].fillna(0), 18, 190)
        ax.scatter(
            scatter_frame["dist_km_nearest_region"],
            scatter_frame["log_ai_works"],
            s=scatter_sizes,
            color=PALETTE["chart_primary"],
            alpha=0.45,
            linewidths=0.5,
            edgecolors=PALETTE["panel_bg"],
            zorder=2,
        )
        scatter_frame["distance_bin"] = pd.qcut(
            scatter_frame["dist_km_nearest_region"].rank(method="first"),
            q=6,
            labels=False,
        )
        scatter_profile = (
            scatter_frame.groupby("distance_bin")
            .agg(
                distance_mid=("dist_km_nearest_region", "median"),
                log_ai_mid=("log_ai_works", "median"),
            )
            .reset_index(drop=True)
        )
        ax.plot(
            scatter_profile["distance_mid"],
            scatter_profile["log_ai_mid"],
            color=PALETTE["chart_negative"],
            linewidth=2.3,
            marker="o",
            markersize=5,
            zorder=4,
        )
        top_cities = (
            scatter_frame.sort_values("openalex_ai_works_recent", ascending=False)
            .drop_duplicates("city_ascii")
            .head(6)
            .copy()
        )
        top_sizes = _scale_marker_sizes(top_cities["population"].fillna(0), 80, 240)
        ax.scatter(
            top_cities["dist_km_nearest_region"],
            top_cities["log_ai_works"],
            s=top_sizes,
            color=PALETTE["priority_fill"],
            alpha=0.95,
            linewidths=0.8,
            edgecolors=PALETTE["panel_bg"],
            zorder=5,
        )
        label_offsets = [(8, 12), (8, -14), (8, 10), (-54, 10), (8, -16), (-48, -12)]
        for (row, offset) in zip(top_cities.itertuples(index=False), label_offsets):
            ax.annotate(
                row.city_ascii,
                (row.dist_km_nearest_region, row.log_ai_works),
                xytext=offset,
                textcoords="offset points",
                fontsize=8.5,
                color=PALETTE["text_primary"],
                family=TYPOGRAPHY["body_family"],
                bbox={
                    "boxstyle": "round,pad=0.2,rounding_size=0.1",
                    "facecolor": PALETTE["panel_bg"],
                    "edgecolor": PALETTE["panel_edge"],
                    "linewidth": 0.8,
                },
                arrowprops={
                    "arrowstyle": "-",
                    "color": PALETTE["panel_edge"],
                    "linewidth": 0.8,
                },
                zorder=6,
            )
        _configure_log_distance_axis(ax, scatter_frame["dist_km_nearest_region"])
        y_values = scatter_frame["log_ai_works"].to_numpy(dtype=float)
        ax.set_ylim(max(0.0, float(y_values.min()) - 0.25), float(y_values.max()) + 0.45)
        scatter_legend = ax.legend(
            handles=[
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=PALETTE["chart_primary"],
                    markeredgecolor=PALETTE["panel_bg"],
                    alpha=0.6,
                    markersize=8,
                    label="Matched AI city",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=PALETTE["priority_fill"],
                    markeredgecolor=PALETTE["panel_bg"],
                    markersize=8,
                    label="Top-output city",
                ),
                Line2D(
                    [0],
                    [0],
                    color=PALETTE["chart_negative"],
                    linewidth=2.3,
                    marker="o",
                    markersize=5,
                    label="Equal-count bin median",
                ),
            ],
            loc="lower right",
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        ax.add_artist(scatter_legend)
        _size_legend_from_series(
            ax=ax,
            title="Population",
            series=scatter_frame["population"],
            min_size=18,
            max_size=190,
            color=PALETTE["chart_primary"],
            edgecolor=PALETTE["panel_bg"],
            bbox_to_anchor=(0.01, 0.02),
        )
        near_cloud_share = float((scatter_frame["dist_km_nearest_region"] <= 250).mean())
        _add_info_panel(
            ax,
            "Quick read",
            [
                f"{_format_int(len(scatter_frame))} matched AI city records",
                f"Median distance: {_format_km(scatter_frame['dist_km_nearest_region'].median())}",
                f"{_format_share(near_cloud_share)} fall within 250 km of a deployed region",
                "Large population does not fully erase the near-cloud clustering pattern",
            ],
        )
        _add_footer(
            fig,
            "Descriptive association only. This figure keeps the raw matched AI-city sample used by the model tables rather than implying a causal treatment effect.",
        )
        out4 = paths.figures / "fig4_scatter_ai_vs_dist.png"
        _savefig(fig, out4)

    # 4b) Distance distributions (context: are AI cities systematically closer?)
    if cities_ai is not None:
        distance_all = cities_access["dist_km_nearest_region"].to_numpy(dtype=float)
        distance_ai = cities_ai["dist_km_nearest_region"].to_numpy(dtype=float)
        distance_all = distance_all[np.isfinite(distance_all) & (distance_all > 0)]
        distance_ai = distance_ai[np.isfinite(distance_ai) & (distance_ai > 0)]
        distance_all_band = _distance_band_transform(distance_all)
        distance_ai_band = _distance_band_transform(distance_ai)
        distance_band_max = max(float(distance_all_band.max()), float(distance_ai_band.max()))
        distance_bins = np.linspace(0.0, distance_band_max * 1.02, 24)
        all_share, _ = np.histogram(distance_all_band, bins=distance_bins)
        ai_share, _ = np.histogram(distance_ai_band, bins=distance_bins)
        all_share = all_share / all_share.sum()
        ai_share = ai_share / ai_share.sum()
        fig, ax = _create_chart_figure(
            figsize_key="chart_feature",
            kicker="Figure 7",
            title="AI-linked cities sit materially closer to deployed cloud regions",
            subtitle="Equal-width bands on a log-distance scale keep the global tail visible while still resolving the sharp left shift in the AI-city sample.",
        )
        _style_chart_axis(
            ax,
            xlabel="Distance to nearest hyperscaler region (km, log scale)",
            ylabel="Share of cities in band",
        )
        ax.yaxis.set_major_formatter(PercentFormatter(1.0))
        ax.stairs(
            all_share,
            distance_bins,
            fill=True,
            facecolor=PALETTE["chart_primary_fill"],
            edgecolor=PALETTE["chart_primary"],
            alpha=0.28,
            linewidth=1.6,
            label=f"All large cities (n={len(distance_all):,})",
            zorder=2,
        )
        ax.stairs(
            ai_share,
            distance_bins,
            color=PALETTE["chart_secondary"],
            linewidth=2.3,
            label=f"Matched AI cities (n={len(distance_ai):,})",
            zorder=3,
        )
        ax.axvline(
            math.log10(float(np.median(distance_all)) + 1.0),
            color=PALETTE["chart_primary"],
            linewidth=1.2,
            linestyle="--",
            zorder=4,
        )
        ax.axvline(
            math.log10(float(np.median(distance_ai)) + 1.0),
            color=PALETTE["chart_secondary"],
            linewidth=1.2,
            linestyle="--",
            zorder=4,
        )
        _configure_distance_band_axis(ax, np.concatenate([distance_all, distance_ai]))
        ax.legend(
            loc="upper right",
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        _add_info_panel(
            ax,
            "Quick read",
            [
                f"Median AI-city distance: {_format_km(np.median(distance_ai))}",
                f"Median all-city distance: {_format_km(np.median(distance_all))}",
                f"{_format_share(float((distance_ai <= 500).mean()))} of AI cities are within 500 km",
                f"{_format_share(float((distance_all <= 500).mean()))} of all large cities are within 500 km",
            ],
        )
        _add_footer(
            fig,
            "Distributional contrast only. The comparison uses the pipeline's 8,000-city accessibility frame against the matched OpenAlex AI-city subset.",
        )
        out7 = paths.figures / "fig7_distance_hist.png"
        _savefig(fig, out7)

        # AI-weighted (where AI output is concentrated)
        weighted_frame = cities_ai.dropna(
            subset=["dist_km_nearest_region", "openalex_ai_works_recent"]
        ).copy()
        weighted_frame = weighted_frame[weighted_frame["dist_km_nearest_region"] > 0].copy()
        weighted_values = weighted_frame["dist_km_nearest_region"].to_numpy(dtype=float)
        weighted_values_band = _distance_band_transform(weighted_values)
        weighted_weights = weighted_frame["openalex_ai_works_recent"].clip(lower=0).to_numpy(dtype=float)
        weighted_band_share, _ = np.histogram(
            weighted_values_band,
            bins=distance_bins,
            weights=weighted_weights,
        )
        weighted_band_share = weighted_band_share / weighted_band_share.sum()
        cumulative_share = np.cumsum(weighted_band_share)
        weighted_median = _weighted_quantile(weighted_values, weighted_weights, 0.5)
        bin_centers = (distance_bins[:-1] + distance_bins[1:]) / 2.0
        fig, ax = _create_chart_figure(
            figsize_key="chart_feature",
            kicker="Figure 8",
            title="Observed AI work is even more concentrated near deployed cloud regions",
            subtitle="Histogram bars are weighted by recent OpenAlex AI works, with a cumulative share line to show how quickly activity concentrates near cloud access.",
            right_margin=0.74,
        )
        _style_chart_axis(
            ax,
            xlabel="Distance to nearest hyperscaler region (km, log scale)",
            ylabel="Share of recent AI works in band",
        )
        ax.yaxis.set_major_formatter(PercentFormatter(1.0))
        ax.stairs(
            weighted_band_share,
            distance_bins,
            fill=True,
            facecolor=PALETTE["priority_fill"],
            edgecolor=PALETTE["priority_edge"],
            alpha=0.26,
            linewidth=1.6,
            zorder=2,
        )
        ax.plot(
            bin_centers,
            weighted_band_share,
            color=PALETTE["priority_edge"],
            linewidth=1.8,
            zorder=3,
        )
        ax.axvline(
            math.log10(weighted_median + 1.0),
            color=PALETTE["chart_secondary"],
            linewidth=1.5,
            linestyle="--",
            zorder=4,
        )
        _configure_distance_band_axis(ax, weighted_values)
        ax2 = ax.twinx()
        ax2.plot(
            bin_centers,
            cumulative_share,
            color=PALETTE["chart_tertiary"],
            linewidth=2.2,
            zorder=5,
        )
        ax2.set_ylim(0, 1.02)
        ax2.yaxis.set_major_formatter(PercentFormatter(1.0))
        ax2.set_ylabel(
            "Cumulative share of AI works",
            color=PALETTE["text_primary"],
            family=TYPOGRAPHY["body_family"],
            labelpad=6,
        )
        ax2.tick_params(colors=PALETTE["text_muted"])
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_color(PALETTE["panel_edge"])
        ax2.spines["right"].set_linewidth(1.0)
        ax2.grid(False)
        ax.legend(
            handles=[
                Line2D(
                    [0],
                    [0],
                    color=PALETTE["priority_edge"],
                    linewidth=1.8,
                    label="Share of recent AI works",
                ),
                Line2D(
                    [0],
                    [0],
                    color=PALETTE["chart_tertiary"],
                    linewidth=2.2,
                    label="Cumulative share of AI works",
                ),
                Line2D(
                    [0],
                    [0],
                    color=PALETTE["chart_secondary"],
                    linewidth=1.5,
                    linestyle="--",
                    label="Weighted median",
                ),
            ],
            loc="upper right",
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        _add_info_panel(
            ax,
            "Quick read",
            [
                f"Weighted median distance: {_format_km(weighted_median)}",
                f"{_format_share(float(weighted_weights[weighted_values <= 250].sum() / weighted_weights.sum()))} of AI works fall within 250 km",
                f"{_format_share(float(weighted_weights[weighted_values <= 500].sum() / weighted_weights.sum()))} fall within 500 km",
                f"{_format_share(float(weighted_weights[weighted_values <= 1000].sum() / weighted_weights.sum()))} fall within 1,000 km",
            ],
        )
        _add_footer(
            fig,
            "Weights equal recent OpenAlex AI works. The chart summarizes concentration in observed activity, not a causal estimate of what cloud access alone produces.",
        )
        out8 = paths.figures / "fig8_ai_weighted_distance.png"
        _savefig(fig, out8)

        # 4d) Raster surface previews (coarse 1° grid)
        dist_tif = paths.gis / "ai_access_surface_distance.tif"
        if dist_tif.exists():
            with rasterio.open(dist_tif) as src:
                arr = src.read(1)
            fig, ax = plt.subplots(figsize=FIGURE_SIZES["chart_wide"])
            ax.imshow(arr, aspect="auto")
            ax.set_title("Global surface (1°): distance to nearest hyperscaler region (km)")
            ax.set_axis_off()
            out9 = paths.figures / "fig9_distance_surface.png"
            _savefig(fig, out9)

        gp_tif = paths.gis / "ai_research_pred_gp.tif"
        if gp_tif.exists():
            with rasterio.open(gp_tif) as src:
                arr = src.read(1)
            fig, ax = plt.subplots(figsize=FIGURE_SIZES["chart_wide"])
            ax.imshow(arr, aspect="auto")
            ax.set_title("Global surface (1°): GP-predicted log(1+AI works) for a reference 1M-person city")
            ax.set_axis_off()
            out10 = paths.figures / "fig10_gp_surface.png"
            _savefig(fig, out10)

        # D1 rebuild of the global surface family
        if dist_tif.exists():
            dist_arr, dist_bounds = _load_surface_raster(dist_tif)
            fig, ax = _create_map_figure(
                figsize_key="map_feature",
                kicker="Figure 9",
                title="The global compute-access surface leaves the deepest gaps across Africa and interior South America",
                subtitle="Surface values come from the nearest deployed cloud region at 1 degree resolution, using the same distance metric as the city overlay.",
            )
            dist_vmax = float(np.nanpercentile(dist_arr, 98))
            image = _plot_surface_raster(
                ax,
                dist_arr,
                dist_bounds,
                cmap=ACCESS_CMAP,
                vmin=0.0,
                vmax=dist_vmax,
            )
            _plot_world_outline(ax, world)
            colorbar = fig.colorbar(image, ax=ax, fraction=0.03, pad=0.02, shrink=0.78)
            colorbar.set_label("Distance to nearest cloud region (km)", color=PALETTE["text_primary"])
            colorbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
            _add_info_panel(
                ax,
                "Quick read",
                [
                    f"Median surface distance: {_format_km(np.nanmedian(dist_arr))}",
                    f"95th percentile: {_format_km(np.nanpercentile(dist_arr, 95))}",
                    f"{_format_int(len(regions))} cloud regions anchor the current footprint",
                    "The shortest-distance belts cluster around North America, Europe, and East Asia",
                ],
            )
            _add_footer(
                fig,
                "This is a descriptive nearest-region surface, not a travel-time or capacity-weighted model. Ocean cells remain visible to show the geometry of the current cloud footprint.",
            )
            out9 = paths.figures / "fig9_distance_surface.png"
            _savefig(fig, out9)

        if gp_tif.exists():
            gp_arr, gp_bounds = _load_surface_raster(gp_tif)
            fig, ax = _create_map_figure(
                figsize_key="map_feature",
                kicker="Figure 10",
                title="The GP surface points to broad regional AI gradients rather than local hotspot spikes",
                subtitle="Predictions are for a reference 1M-person city, so the surface should be read as a smooth regional field rather than a city-by-city forecast.",
            )
            gp_vmin = float(np.nanpercentile(gp_arr, 2))
            gp_vmax = float(np.nanpercentile(gp_arr, 98))
            image = _plot_surface_raster(
                ax,
                gp_arr,
                gp_bounds,
                cmap=AI_SURFACE_CMAP,
                vmin=gp_vmin,
                vmax=gp_vmax,
            )
            _plot_world_outline(ax, world)
            colorbar = fig.colorbar(image, ax=ax, fraction=0.03, pad=0.02, shrink=0.78)
            colorbar.set_label("GP-predicted log(1 + AI works)", color=PALETTE["text_primary"])
            colorbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
            _add_info_panel(
                ax,
                "Quick read",
                [
                    "Reference population fixed at 1 million people",
                    f"Median predicted log outcome: {np.nanmedian(gp_arr):.2f}",
                    f"95th percentile: {np.nanpercentile(gp_arr, 95):.2f}",
                    "The strongest modeled peak centers on Singapore and maritime Southeast Asia",
                ],
            )
            _add_footer(
                fig,
                "The GP field smooths residual geography on purpose. It is useful for broad regional context, but it should not be read as a local causal scorecard.",
            )
            out10 = paths.figures / "fig10_gp_surface.png"
            _savefig(fig, out10)

    # 5) Coefficient compare (GP and CAR/GMRF)
    coef_path = paths.figures / "fig5_coef_compare.png"
    gp_sum_fp = paths.tables / "model_gp_summary.json"
    car_sum_fp = paths.tables / "model_car_summary.json"
    model_summaries: List[Tuple[str, Dict[str, object]]] = []
    if gp_sum_fp.exists():
        model_summaries.append(("GP", json.loads(Path(gp_sum_fp).read_text(encoding="utf-8"))))
    if car_sum_fp.exists():
        model_summaries.append(("CAR/GMRF", json.loads(Path(car_sum_fp).read_text(encoding="utf-8"))))
    if model_summaries:
        predictor_keys = ["dist_per_1000km", "log_pop"]
        predictor_labels = ["Distance to region (per 1,000 km)", "Population (log)"]
        fig, ax = _create_chart_figure(
            figsize_key="chart_feature_compact",
            kicker="Figure 5",
            title="Distance keeps a negative sign across both spatial model specifications",
            subtitle="Bars show point estimates from the stored summary JSON files. The chart is directional only because interval estimates are not available in the current pipeline outputs.",
            bottom_margin=0.22,
        )
        _style_chart_axis(ax, xlabel="Effect on log AI works", ylabel="")
        base_positions = np.arange(len(predictor_keys), dtype=float)
        offsets = np.array([0.0]) if len(model_summaries) == 1 else np.linspace(-0.18, 0.18, num=len(model_summaries))
        bar_height = 0.32 if len(model_summaries) > 1 else 0.42
        model_colors = {
            "GP": PALETTE["chart_tertiary"],
            "CAR/GMRF": PALETTE["ai_fill"],
        }
        all_values: List[float] = []
        for offset, (model_name, summary) in zip(offsets, model_summaries):
            beta = summary["beta"]
            values = [float(beta[key]) for key in predictor_keys]
            positions = base_positions + offset
            ax.barh(
                positions,
                values,
                height=bar_height,
                color=model_colors.get(model_name, PALETTE["chart_primary"]),
                alpha=0.9,
                edgecolor=PALETTE["panel_bg"],
                linewidth=0.8,
                label=model_name,
                zorder=3,
            )
            _label_horizontal_bars(ax, positions, values)
            all_values.extend(values)
        max_effect = max((abs(value) for value in all_values), default=0.1)
        ax.axvline(0, color=PALETTE["text_muted"], linewidth=1.0, zorder=2)
        ax.set_xlim(-max_effect * 1.55, max_effect * 1.85)
        ax.set_yticks(base_positions)
        ax.set_yticklabels(predictor_labels)
        ax.invert_yaxis()
        ax.legend(
            loc="lower right",
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        gp_distance = None
        car_distance = None
        for model_name, summary in model_summaries:
            beta = summary["beta"]
            if model_name == "GP":
                gp_distance = float(beta["dist_per_1000km"])
            if model_name == "CAR/GMRF":
                car_distance = float(beta["dist_per_1000km"])
        panel_lines = []
        if gp_distance is not None:
            panel_lines.append(f"GP distance beta: {gp_distance:+.3f}")
        if car_distance is not None:
            panel_lines.append(f"CAR distance beta: {car_distance:+.3f}")
        panel_lines.append("Population remains positive in every stored model summary")
        panel_lines.append("Use this as a directional sign check, not a causal effect size")
        _add_info_panel(ax, "Model readout", panel_lines)
        _add_footer(
            fig,
            "Point estimates only. The current pipeline stores posterior/EB means but not the uncertainty intervals needed for a fuller inferential comparison.",
        )
        _savefig(fig, coef_path)

    # 5b) Moran scatterplot refresh
    moran_fp = paths.tables / "morans_i_summary.csv"
    moran_scatter_path = paths.figures / "morans_i_scatterplot.png"
    if hotspots is not None and moran_fp.exists():
        moran_summary = pd.read_csv(moran_fp)
        if not moran_summary.empty:
            moran_stats = moran_summary.iloc[0]
            moran_frame = hotspots.copy()
            moran_frame["log_ai_works"] = np.log1p(moran_frame["openalex_ai_works_recent"].clip(lower=0))
            mean_log_ai = float(moran_frame["log_ai_works"].mean())
            std_log_ai = float(moran_frame["log_ai_works"].std(ddof=0))
            if std_log_ai > 0:
                moran_frame["standardized_log_ai"] = (moran_frame["log_ai_works"] - mean_log_ai) / std_log_ai
                moran_frame["standardized_spatial_lag"] = (
                    moran_frame["spatial_lag_log_ai_works"] - mean_log_ai
                ) / std_log_ai
                fig, ax = _create_chart_figure(
                    figsize_key="chart_feature",
                    kicker="Moran scatterplot",
                    title="Local clustering is present but modest in the matched AI-city network",
                    subtitle="The fitted line uses the global Moran's I summary for log AI works across the unique-city hotspot diagnostics.",
                )
                _style_chart_axis(
                    ax,
                    xlabel="Standardized log(1 + AI works)",
                    ylabel="Spatial lag of standardized log(1 + AI works)",
                )
                ax.axhline(0, color=PALETTE["panel_edge"], linewidth=1.0, zorder=1)
                ax.axvline(0, color=PALETTE["panel_edge"], linewidth=1.0, zorder=1)
                class_order = [
                    "not_significant",
                    "cold_spot_95",
                    "cold_spot_99",
                    "hot_spot_95",
                    "hot_spot_99",
                ]
                class_labels = {
                    "not_significant": "Not significant",
                    "cold_spot_95": "Cold spot (95%)",
                    "cold_spot_99": "Cold spot (99%)",
                    "hot_spot_95": "Hot spot (95%)",
                    "hot_spot_99": "Hot spot (99%)",
                }
                class_counts = moran_frame["hotspot_class"].value_counts().to_dict()
                legend_handles = []
                for class_name in class_order:
                    subset = moran_frame[moran_frame["hotspot_class"] == class_name]
                    if subset.empty:
                        continue
                    color = HOTSPOT_COLORS[class_name]
                    alpha = 0.32 if class_name == "not_significant" else 0.85
                    size = 18 if class_name == "not_significant" else 34
                    ax.scatter(
                        subset["standardized_log_ai"],
                        subset["standardized_spatial_lag"],
                        s=size,
                        color=color,
                        alpha=alpha,
                        linewidths=0.0,
                        zorder=2 if class_name == "not_significant" else 3,
                    )
                    legend_handles.append(
                        Line2D(
                            [0],
                            [0],
                            marker="o",
                            linestyle="",
                            markerfacecolor=color,
                            markeredgecolor=color,
                            markersize=6 if class_name == "not_significant" else 7,
                            alpha=alpha,
                            label=f"{class_labels[class_name]} ({class_counts.get(class_name, 0)})",
                        )
                    )
                max_extent = max(
                    float(np.nanmax(np.abs(moran_frame["standardized_log_ai"]))),
                    float(np.nanmax(np.abs(moran_frame["standardized_spatial_lag"]))),
                )
                max_extent = max(max_extent, 2.5)
                axis_limits = (-max_extent * 1.08, max_extent * 1.08)
                ax.set_xlim(*axis_limits)
                ax.set_ylim(*axis_limits)
                moran_slope = float(moran_stats["morans_i"])
                x_line = np.linspace(axis_limits[0], axis_limits[1], 200)
                ax.plot(
                    x_line,
                    moran_slope * x_line,
                    color=PALETTE["cloud_region"],
                    linewidth=2.0,
                    zorder=4,
                )
                legend_handles.append(
                    Line2D(
                        [0],
                        [0],
                        color=PALETTE["cloud_region"],
                        linewidth=2.0,
                        label=f"Moran slope = {moran_slope:.3f}",
                    )
                )
                ax.legend(
                    handles=legend_handles,
                    loc="lower right",
                    frameon=True,
                    facecolor=PALETTE["panel_bg"],
                    edgecolor=PALETTE["panel_edge"],
                    fontsize=8,
                )
                hot_spot_count = int(
                    class_counts.get("hot_spot_95", 0) + class_counts.get("hot_spot_99", 0)
                )
                cold_spot_count = int(
                    class_counts.get("cold_spot_95", 0) + class_counts.get("cold_spot_99", 0)
                )
                _add_info_panel(
                    ax,
                    "Quick read",
                    [
                        f"Moran's I: {moran_slope:.3f}",
                        f"Permutation z-score: {float(moran_stats['z_score']):.2f}",
                        f"Two-sided p-value: {float(moran_stats['p_value_two_sided']):.3f}",
                        f"{hot_spot_count} hot spots and {cold_spot_count} cold spots in the unique-city diagnostics",
                    ],
                )
                _add_footer(
                    fig,
                    "This scatterplot summarizes descriptive spatial autocorrelation in the restored hotspot diagnostics. It should not be read as evidence of a causal spillover mechanism.",
                )
                _savefig(fig, moran_scatter_path)

    # 6) Southeast Asia zoom (Singapore relevance)
    if cities_ai is not None:
        bbox = (90, -15, 130, 25)  # lon_min, lat_min, lon_max, lat_max
        fig, ax = plt.subplots(figsize=FIGURE_SIZES["map_regional"])
        world.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]].plot(ax=ax, color=PALETTE["country_fill"], edgecolor=PALETTE["country_edge"], linewidth=0.5)
        # regions
        regions.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]].plot(ax=ax, color=PALETTE["cloud_region"], marker="x", markersize=50, alpha=0.9)
        # AI cities
        sub = cities_ai.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]].copy()
        size = np.sqrt(sub["openalex_ai_works_recent"].fillna(0)) * 10
        sub.plot(ax=ax, markersize=size, alpha=0.8)
        ax.set_title("Southeast Asia focus: AI cities and hyperscaler regions")
        ax.set_axis_off()
        out6 = paths.figures / "fig6_sea_zoom.png"
        _savefig(fig, out6)

    # D1 rebuild of the regional/deep-dive family
    if cities_ai is not None:
        sea_bbox = (90, -15, 130, 25)
        sea_access = cities_access.cx[sea_bbox[0]:sea_bbox[2], sea_bbox[1]:sea_bbox[3]].copy()
        sea_regions = regions.cx[sea_bbox[0]:sea_bbox[2], sea_bbox[1]:sea_bbox[3]].copy()
        sea_ai = (
            cities_ai_unique.cx[sea_bbox[0]:sea_bbox[2], sea_bbox[1]:sea_bbox[3]].copy()
            if cities_ai_unique is not None
            else None
        )
        sea_priority = (
            priority_cities.cx[sea_bbox[0]:sea_bbox[2], sea_bbox[1]:sea_bbox[3]].copy()
            if priority_cities is not None
            else None
        )
        fig, ax = _create_map_figure(
            figsize_key="map_deep_dive",
            kicker="Figure 6",
            title="Southeast Asia combines dense cloud buildout with a narrow set of AI hubs",
            subtitle="Backdrop color shows compute distance for the wider city system while larger orange markers highlight matched AI cities and the Singapore-centered research corridor.",
        )
        _plot_world_base(ax, world, bbox=sea_bbox)
        sea_access["marker_size"] = _scale_marker_sizes(sea_access["population"].fillna(0), 8, 42)
        sea_access_norm = mcolors.Normalize(
            vmin=float(sea_access["dist_km_nearest_region"].min()),
            vmax=float(sea_access["dist_km_nearest_region"].max()),
        )
        sea_access.plot(
            ax=ax,
            column="dist_km_nearest_region",
            cmap=ACCESS_CMAP,
            vmin=sea_access_norm.vmin,
            vmax=sea_access_norm.vmax,
            markersize=sea_access["marker_size"],
            alpha=0.4,
            linewidth=0,
            zorder=2,
        )
        sea_regions.plot(
            ax=ax,
            color=PALETTE["cloud_region"],
            marker="x",
            markersize=52,
            alpha=0.9,
            linewidth=1.2,
            zorder=5,
        )
        if sea_ai is not None and not sea_ai.empty:
            sea_ai["marker_size"] = _scale_marker_sizes(
                sea_ai["openalex_ai_works_recent"].fillna(0),
                42,
                280,
            )
            sea_ai.plot(
                ax=ax,
                color=PALETTE["ai_fill"],
                markersize=sea_ai["marker_size"],
                alpha=0.9,
                linewidth=0.5,
                edgecolor=PALETTE["panel_bg"],
                zorder=6,
            )
            top_ai_cities = sea_ai.sort_values("openalex_ai_works_recent", ascending=False).head(5).copy()
            _annotate_map_labels(
                ax,
                top_ai_cities,
                label_column="city_ascii",
                offsets=[(-42, -14), (8, 10), (-44, 10), (8, -12), (8, 8)],
            )
            _size_legend_from_series(
                ax=ax,
                title="Recent AI works",
                series=sea_ai["openalex_ai_works_recent"],
                min_size=42,
                max_size=280,
                color=PALETTE["ai_fill"],
                edgecolor=PALETTE["panel_bg"],
            )
        sea_colorbar = fig.colorbar(
            plt.cm.ScalarMappable(norm=sea_access_norm, cmap=ACCESS_CMAP),
            ax=ax,
            fraction=0.03,
            pad=0.02,
            shrink=0.78,
        )
        sea_colorbar.set_label("Distance to nearest cloud region (km)", color=PALETTE["text_primary"])
        sea_colorbar.ax.tick_params(labelsize=8, colors=PALETTE["text_muted"])
        sea_legend = ax.legend(
            handles=[
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=PALETTE["chart_primary"],
                    markeredgecolor="none",
                    alpha=0.4,
                    markersize=6,
                    label="Large-city backdrop",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="",
                    markerfacecolor=PALETTE["ai_fill"],
                    markeredgecolor=PALETTE["panel_bg"],
                    markersize=7,
                    label="Matched AI city",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="x",
                    linestyle="",
                    color=PALETTE["cloud_region"],
                    markeredgewidth=1.2,
                    markersize=8,
                    label="Cloud region",
                ),
            ],
            loc="lower left",
            bbox_to_anchor=(0.17, 0.03),
            frameon=True,
            facecolor=PALETTE["panel_bg"],
            edgecolor=PALETTE["panel_edge"],
            fontsize=8,
        )
        ax.add_artist(sea_legend)
        singapore_distance = None
        if sea_ai is not None and not sea_ai.empty:
            singapore_match = sea_ai[sea_ai["city_ascii"] == "Singapore"]
            if not singapore_match.empty:
                singapore_distance = float(singapore_match.iloc[0]["dist_km_nearest_region"])
        bangkok_distance = None
        if sea_priority is not None and not sea_priority.empty:
            bangkok_priority = sea_priority[sea_priority["city"] == "Bangkok"]
            if not bangkok_priority.empty:
                bangkok_distance = float(bangkok_priority.iloc[0]["dist_km_nearest_region"])
        sea_panel_lines = [
            f"{_format_int(len(sea_regions))} cloud regions in frame",
            f"Median city distance: {_format_km(sea_access['dist_km_nearest_region'].median())}",
        ]
        if singapore_distance is not None:
            sea_panel_lines.append(f"Singapore sits only {_format_km(singapore_distance)} from deployed cloud capacity")
        if bangkok_distance is not None:
            sea_panel_lines.append(f"Bangkok still sits {_format_km(bangkok_distance)} away despite its scale")
        _add_info_panel(ax, "Quick read", sea_panel_lines)
        _add_footer(
            fig,
            "This regional panel contrasts local AI hubs with the broader compute-access field. It remains a descriptive overlay rather than a claim that cloud presence alone determines AI outcomes.",
        )
        out6 = paths.figures / "fig6_sea_zoom.png"
        _savefig(fig, out6)

    if priority_cities is not None:
        ssa_bbox = (-20, -35, 55, 20)
        ssa_access = cities_access.cx[ssa_bbox[0]:ssa_bbox[2], ssa_bbox[1]:ssa_bbox[3]].copy()
        ssa_priority = priority_cities.cx[ssa_bbox[0]:ssa_bbox[2], ssa_bbox[1]:ssa_bbox[3]].copy()
        ssa_regions = regions.cx[ssa_bbox[0]:ssa_bbox[2], ssa_bbox[1]:ssa_bbox[3]].copy()
        if not ssa_access.empty and not ssa_priority.empty:
            fig, ax, ssa_top = _create_priority_deep_dive_figure(
                world=world,
                regions=ssa_regions,
                access_frame=ssa_access,
                priority_frame=ssa_priority,
                bbox=ssa_bbox,
                kicker="Figure 13",
                title="Sub-Saharan Africa's current cloud footprint is concentrated in South Africa",
                subtitle="Large-city backdrop colors compute distance while highlighted priority cities show where population size and weak access combine most sharply.",
                panel_lines=[
                    f"{_format_int(len(ssa_access))} large cities and {_format_int(len(ssa_priority))} priority cities in frame",
                    f"Median city distance: {_format_km(ssa_access['dist_km_nearest_region'].median())}",
                    f"{_format_int(len(ssa_regions))} cloud regions, all in South Africa",
                    "Lagos and Kinshasa lead the current screening layer",
                ],
                footer_note="Priority cities combine zero observed AI works in the delivered overlay with long compute distance. They are a screening layer for follow-up, not a causal forecast.",
            )
            _annotate_map_labels(
                ax,
                ssa_top.head(6),
                label_column="city",
                offsets=[(-28, 10), (8, -14), (8, 10), (8, -12), (8, 10), (8, -14)],
            )
            out13 = paths.figures / "fig13_subsaharan_africa_deep_dive.png"
            _savefig(fig, out13)

        latam_bbox = (-105, -60, -30, 24)
        latam_access = cities_access.cx[latam_bbox[0]:latam_bbox[2], latam_bbox[1]:latam_bbox[3]].copy()
        latam_priority = priority_cities.cx[latam_bbox[0]:latam_bbox[2], latam_bbox[1]:latam_bbox[3]].copy()
        latam_regions = regions.cx[latam_bbox[0]:latam_bbox[2], latam_bbox[1]:latam_bbox[3]].copy()
        if not latam_access.empty and not latam_priority.empty:
            fig, ax, latam_top = _create_priority_deep_dive_figure(
                world=world,
                regions=latam_regions,
                access_frame=latam_access,
                priority_frame=latam_priority,
                bbox=latam_bbox,
                kicker="Figure 14",
                title="Latin America's cloud buildout is concentrated in Brazil and Chile",
                subtitle="The regional surface is better than in Sub-Saharan Africa, but the priority layer still clusters along the Andes, northern South America, and the Caribbean corridor.",
                panel_lines=[
                    f"{_format_int(len(latam_access))} large cities and {_format_int(len(latam_priority))} priority cities in frame",
                    f"Median city distance: {_format_km(latam_access['dist_km_nearest_region'].median())}",
                    f"{_format_int(len(latam_regions))} cloud regions concentrated in Brazil and Chile",
                    "Lima and Bogota sit at the top of the current screening layer",
                ],
                footer_note="This deep dive combines the regional access backdrop with the priority-city screen so the atlas can show both where cloud coverage exists and where large-city gaps remain.",
            )
            _annotate_map_labels(
                ax,
                latam_top.head(6),
                label_column="city",
                offsets=[(-30, -14), (8, 10), (8, 10), (8, -12), (8, 10), (8, -14)],
            )
            out14 = paths.figures / "fig14_latin_america_deep_dive.png"
            _savefig(fig, out14)

    # Copy a subset into report/figures
    report_fig_dir = _copy_figures_to_report(paths, generated_figure_names)

    return {"figures_dir": str(paths.figures), "report_figures_dir": str(report_fig_dir)}


# -------------------------
# Orchestration
# -------------------------
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", choices=["prepare","access","openalex","spatial_outputs","model_gp","model_car","surfaces","figures","all"])
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--top_n_cities", type=int, default=8000)
    parser.add_argument("--resolution_deg", type=float, default=1.0)
    args = parser.parse_args()

    paths = Paths.from_root(Path(args.root))
    ensure_dirs(paths)

    if args.cmd == "prepare":
        res = step_prepare(paths, top_n_cities=args.top_n_cities)
    elif args.cmd == "access":
        res = step_compute_access(paths)
    elif args.cmd == "openalex":
        res = step_join_openalex(paths)
    elif args.cmd == "spatial_outputs":
        res = step_spatial_outputs(paths)
    elif args.cmd == "model_gp":
        res = step_model_gp(paths)
    elif args.cmd == "model_car":
        res = step_model_car(paths)
    elif args.cmd == "surfaces":
        res = step_surfaces(paths, resolution_deg=args.resolution_deg)
    elif args.cmd == "figures":
        res = step_figures(paths)
    elif args.cmd == "all":
        res = {}
        res["prepare"] = step_prepare(paths, top_n_cities=args.top_n_cities)
        res["access"] = step_compute_access(paths)
        res["openalex"] = step_join_openalex(paths)
        res["spatial_outputs"] = step_spatial_outputs(paths)
        res["model_gp"] = step_model_gp(paths)
        res["model_car"] = step_model_car(paths)
        res["surfaces"] = step_surfaces(paths, resolution_deg=args.resolution_deg)
        res["figures"] = step_figures(paths)
    else:
        raise ValueError(args.cmd)

    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
