"""Coordinate conversion and great-circle distance."""

from __future__ import annotations

import numpy as np

EARTH_RADIUS_KM = 6371.0088  # IUGG mean radius


def to_unit_sphere(lat: np.ndarray, lon: np.ndarray) -> np.ndarray:
    """
    Map lat/lon in degrees to 3D unit vectors.

    Neighbour *rankings* under Euclidean (chordal) distance in this embedding agree
    exactly with great-circle rankings, since chord = 2R sin(d/2R) is monotone in d.
    That is what makes a kd-tree on these coordinates a valid kNN search on the sphere.
    """
    lat_r, lon_r = np.radians(np.asarray(lat, float)), np.radians(np.asarray(lon, float))
    return np.column_stack(
        [np.cos(lat_r) * np.cos(lon_r), np.cos(lat_r) * np.sin(lon_r), np.sin(lat_r)]
    )


def chord_to_arc_km(chord: np.ndarray, radius: float = EARTH_RADIUS_KM) -> np.ndarray:
    """Convert a unit-sphere chord length to great-circle distance in km."""
    c = np.clip(np.asarray(chord, float) / 2.0, 0.0, 1.0)
    return 2.0 * radius * np.arcsin(c)


def haversine_km(lat1, lon1, lat2, lon2, radius: float = EARTH_RADIUS_KM) -> np.ndarray:
    """Vectorised great-circle distance in kilometres."""
    lat1, lon1, lat2, lon2 = map(lambda a: np.radians(np.asarray(a, float)), (lat1, lon1, lat2, lon2))
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    return 2.0 * radius * np.arcsin(np.sqrt(np.clip(a, 0.0, 1.0)))


def pairwise_haversine_km(lat: np.ndarray, lon: np.ndarray) -> np.ndarray:
    """Full n x n great-circle distance matrix in kilometres."""
    lat, lon = np.asarray(lat, float), np.asarray(lon, float)
    return haversine_km(lat[:, None], lon[:, None], lat[None, :], lon[None, :])
