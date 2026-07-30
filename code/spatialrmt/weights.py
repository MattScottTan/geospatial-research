"""
Spatial weights matrices, with the specification made explicit.

The eip submission's Gi* map turned out to depend entirely on two choices its methods
document never stated -- whether the kNN graph is symmetrized, and whether rows are
standardised. Moran's I moved by under 10% across all four combinations; the hot/cold
counts moved by a factor of two. So every constructor here takes `symmetrize` and
`transform` as required, visible arguments rather than defaults buried in a library.

See analysis/01_weights_sensitivity.py for the experiment that motivates this.
"""

from __future__ import annotations

from typing import Literal

import numpy as np
from scipy.sparse import csr_matrix, diags
from scipy.spatial import cKDTree

from .geodesy import EARTH_RADIUS_KM, to_unit_sphere

Transform = Literal["binary", "row", "doubly", "variance"]


# --------------------------------------------------------------------------
# Construction
# --------------------------------------------------------------------------
def knn_weights(
    lat: np.ndarray,
    lon: np.ndarray,
    k: int,
    *,
    symmetrize: bool = False,
    transform: Transform = "row",
) -> csr_matrix:
    """
    k-nearest-neighbour weights on the sphere.

    Parameters
    ----------
    symmetrize
        If True, take the union of i->j and j->i, so W becomes symmetric and row
        degrees vary (typically k to ~2.5k). If False, every row has exactly k
        neighbours and W is asymmetric.
    transform
        "binary" leaves entries at 1, "row" divides each row by its degree.

    Note the interaction: for a *directed* kNN graph every row has degree exactly k,
    so row-standardisation is a global rescaling that cancels in Moran's I. Under
    symmetrization degrees vary and the two transforms genuinely differ.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    xyz = to_unit_sphere(lat, lon)
    n = len(xyz)
    if k >= n:
        raise ValueError(f"k={k} must be < n={n}")

    _, idx = cKDTree(xyz).query(xyz, k=k + 1)  # +1 because the first hit is self
    rows = np.repeat(np.arange(n), k)
    cols = idx[:, 1:].reshape(-1)
    W = csr_matrix((np.ones(n * k), (rows, cols)), shape=(n, n))

    if symmetrize:
        W = ((W + W.T) > 0).astype(float).tocsr()
    return apply_transform(W, transform)


def distance_band_weights(
    lat: np.ndarray,
    lon: np.ndarray,
    threshold_km: float,
    *,
    transform: Transform = "row",
) -> csr_matrix:
    """
    Distance-band weights: neighbours are all points within `threshold_km`.

    This is the construction that maps directly onto the random band matrix model --
    a fixed interaction range, with the band width set by the threshold. Always
    symmetric by construction.
    """
    xyz = to_unit_sphere(lat, lon)
    n = len(xyz)
    # convert great-circle threshold to the corresponding chord length
    chord = 2.0 * np.sin(min(threshold_km / EARTH_RADIUS_KM, np.pi) / 2.0)
    pairs = cKDTree(xyz).query_pairs(chord, output_type="ndarray")
    if len(pairs) == 0:
        return csr_matrix((n, n))
    rows = np.concatenate([pairs[:, 0], pairs[:, 1]])
    cols = np.concatenate([pairs[:, 1], pairs[:, 0]])
    W = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    return apply_transform(W, transform)


# --------------------------------------------------------------------------
# Transforms
# --------------------------------------------------------------------------
def apply_transform(W: csr_matrix, transform: Transform) -> csr_matrix:
    """Apply a normalisation to a binary adjacency."""
    if transform == "binary":
        return W.tocsr()
    if transform == "row":
        deg = np.asarray(W.sum(axis=1)).ravel()
        deg[deg == 0] = 1.0
        return (diags(1.0 / deg) @ W).tocsr()
    if transform == "variance":
        # variance-stabilising: divide by sqrt(degree) on both sides, giving a
        # symmetric normalised adjacency D^-1/2 W D^-1/2 with spectrum in [-1, 1]
        deg = np.asarray(W.sum(axis=1)).ravel()
        deg[deg == 0] = 1.0
        d = diags(1.0 / np.sqrt(deg))
        return (d @ W @ d).tocsr()
    if transform == "doubly":
        return _sinkhorn(W)
    raise ValueError(f"unknown transform {transform!r}")


def _sinkhorn(W: csr_matrix, iters: int = 200, tol: float = 1e-10) -> csr_matrix:
    """Doubly-stochastic scaling. Preserves symmetry; rows and columns both sum to 1."""
    A = W.tocsr().astype(float)
    r = np.ones(A.shape[0])
    c = np.ones(A.shape[1])
    for _ in range(iters):
        rs = np.asarray((diags(r) @ A @ diags(c)).sum(axis=1)).ravel()
        rs[rs == 0] = 1.0
        r_new = r / rs
        cs = np.asarray((diags(r_new) @ A @ diags(c)).sum(axis=0)).ravel()
        cs[cs == 0] = 1.0
        c_new = c / cs
        if np.max(np.abs(r_new - r)) < tol and np.max(np.abs(c_new - c)) < tol:
            r, c = r_new, c_new
            break
        r, c = r_new, c_new
    return (diags(r) @ A @ diags(c)).tocsr()


# --------------------------------------------------------------------------
# Diagnostics
# --------------------------------------------------------------------------
def weights_summary(W: csr_matrix) -> dict:
    """Structural facts about a weights matrix, for reporting alongside any statistic."""
    from scipy.sparse.csgraph import connected_components

    Wc = W.tocsr()
    n = Wc.shape[0]
    deg = np.diff(Wc.indptr)
    sym = (abs(Wc - Wc.T) > 1e-12).nnz == 0
    rs = np.asarray(Wc.sum(axis=1)).ravel()
    n_comp, labels = connected_components(Wc, directed=not sym, connection="weak")
    sizes = np.bincount(labels)
    return {
        "n": int(n),
        "nnz": int(Wc.nnz),
        "density": float(Wc.nnz / (n * n)),
        "symmetric": bool(sym),
        "row_standardised": bool(np.allclose(rs[deg > 0], 1.0)),
        "degree_min": int(deg.min()),
        "degree_max": int(deg.max()),
        "degree_mean": float(deg.mean()),
        "islands": int((deg == 0).sum()),
        # Disconnection is not a curiosity: it caps how far spatial information can
        # propagate, makes whole-graph mixing undefined, and gives the normalised
        # adjacency eigenvalue 1 with multiplicity equal to the component count.
        "n_components": int(n_comp),
        "largest_component": int(sizes.max()),
        "S0": float(Wc.sum()),
    }


def describe(W: csr_matrix) -> str:
    """One-line human-readable weights specification."""
    s = weights_summary(W)
    kind = "symmetric" if s["symmetric"] else "directed"
    norm = "row-standardised" if s["row_standardised"] else "binary"
    return (
        f"n={s['n']} {kind} {norm} "
        f"degree {s['degree_min']}-{s['degree_max']} (mean {s['degree_mean']:.1f}) "
        f"density {s['density']:.4f}"
    )
