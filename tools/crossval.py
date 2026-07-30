"""
Spatial cross-validation.

The single most consequential correction to standard ML practice on spatial data, and
the one most often skipped.

Random k-fold CV assumes the held-out set is independent of the training set. Under
spatial autocorrelation it is not: a held-out point almost always has a near neighbour
in training, so the model interpolates rather than predicts, and the reported score
measures autocorrelation instead of skill. The gap is not small -- on strongly
autocorrelated fields random CV routinely reports R^2 twice what spatial CV does.

Which splitter is right depends on the target:

    predicting at unobserved locations inside the surveyed area  -> buffered / spatial k-fold
    extrapolating to a new region                                -> block CV with large blocks
    predicting for new times at observed locations               -> neither; this is temporal

See analysis/03_spatial_cv.py for the size of the gap on the eip data.

References: Roberts et al. 2017 (Ecography); Ploton et al. 2020 (Nat. Commun.) on
overoptimistic random-CV in spatial ML.
"""

from __future__ import annotations

from typing import Iterator

import numpy as np
from scipy.spatial import cKDTree


def _as_xy(coords: np.ndarray) -> np.ndarray:
    c = np.asarray(coords, float)
    if c.ndim != 2 or c.shape[1] < 2:
        raise ValueError("coords must be (n, 2) or (n, 3)")
    return c


# --------------------------------------------------------------------------
def spatial_block_split(
    coords: np.ndarray,
    n_folds: int = 5,
    *,
    block_size: float | None = None,
    seed: int = 42,
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """
    Block CV: tile space into square blocks, assign whole blocks to folds at random.

    Blocks must be larger than the range of spatial autocorrelation, or neighbouring
    blocks still leak. Fit a variogram first and set `block_size` above its range --
    guessing is the usual failure mode.
    """
    c = _as_xy(coords)[:, :2]
    if block_size is None:
        span = c.max(axis=0) - c.min(axis=0)
        block_size = float(span.max() / (2 * n_folds))

    ij = np.floor((c - c.min(axis=0)) / block_size).astype(int)
    _, block_id = np.unique(ij, axis=0, return_inverse=True)

    rng = np.random.default_rng(seed)
    blocks = np.unique(block_id)
    fold_of_block = dict(zip(rng.permutation(blocks), np.arange(len(blocks)) % n_folds))
    fold = np.array([fold_of_block[b] for b in block_id])

    for f in range(n_folds):
        test = np.flatnonzero(fold == f)
        train = np.flatnonzero(fold != f)
        if len(test) and len(train):
            yield train, test


def buffered_loo_split(
    coords: np.ndarray,
    buffer_dist: float,
    *,
    distance: np.ndarray | None = None,
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """
    Leave-one-out with a dead zone: hold out point i, and also *drop from training*
    every point within `buffer_dist` of it.

    This is the strictest common scheme and the closest to honest prediction error at
    an unvisited location. It is expensive (n fits) and discards data, which is the
    trade for removing leakage.
    """
    c = _as_xy(coords)
    n = len(c)
    D = np.asarray(distance, float) if distance is not None else None
    tree = cKDTree(c) if D is None else None

    for i in range(n):
        near = np.flatnonzero(D[i] <= buffer_dist) if D is not None \
            else np.asarray(tree.query_ball_point(c[i], buffer_dist), dtype=int)
        train = np.setdiff1d(np.arange(n), near, assume_unique=False)
        if len(train):
            yield train, np.array([i])


def spatial_kfold_split(
    coords: np.ndarray,
    n_folds: int = 5,
    *,
    seed: int = 42,
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """
    k-means on coordinates, each cluster a fold. Cheaper than block CV and adapts to
    irregular point densities, but folds vary in size and shape.
    """
    c = _as_xy(coords)[:, :2]
    rng = np.random.default_rng(seed)
    centers = c[rng.choice(len(c), n_folds, replace=False)]
    for _ in range(100):
        lab = np.argmin(((c[:, None, :] - centers[None]) ** 2).sum(-1), axis=1)
        new = np.array([c[lab == k].mean(axis=0) if np.any(lab == k) else centers[k]
                        for k in range(n_folds)])
        if np.allclose(new, centers):
            break
        centers = new
    for f in range(n_folds):
        test = np.flatnonzero(lab == f)
        train = np.flatnonzero(lab != f)
        if len(test) and len(train):
            yield train, test


def random_kfold_split(
    n: int, n_folds: int = 5, *, seed: int = 42
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """Ordinary random k-fold. Included as the baseline to measure leakage against."""
    rng = np.random.default_rng(seed)
    fold = rng.permutation(n) % n_folds
    for f in range(n_folds):
        yield np.flatnonzero(fold != f), np.flatnonzero(fold == f)


# --------------------------------------------------------------------------
def cross_validate(fit_predict, X, y, splits) -> dict:
    """
    Run a splitter and collect out-of-sample scores.

    `fit_predict(X_train, y_train, X_test) -> y_pred`, so any estimator works without
    depending on a particular ML library's interface.
    """
    X, y = np.asarray(X, float), np.asarray(y, float).ravel()
    obs, prd, sizes = [], [], []
    for train, test in splits:
        p = np.asarray(fit_predict(X[train], y[train], X[test]), float).ravel()
        obs.append(y[test]); prd.append(p); sizes.append(len(test))
    o, p = np.concatenate(obs), np.concatenate(prd)
    resid = o - p
    ss_res = float(resid @ resid)
    ss_tot = float(((o - o.mean()) ** 2).sum())
    return {
        "n_folds": len(sizes),
        "n_predictions": int(len(o)),
        "rmse": float(np.sqrt(ss_res / len(o))),
        "mae": float(np.abs(resid).mean()),
        "r2": float(1.0 - ss_res / ss_tot) if ss_tot > 0 else float("nan"),
        "bias": float(resid.mean()),
    }


def leakage_report(fit_predict, X, y, coords, *, n_folds=5, seed=42, **kw) -> dict:
    """
    Same estimator under random and spatial CV. The difference is the leakage.

    A large positive `r2_inflation` means the random-CV score is measuring spatial
    autocorrelation rather than predictive skill.
    """
    n = len(y)
    rnd = cross_validate(fit_predict, X, y, random_kfold_split(n, n_folds, seed=seed))
    blk = cross_validate(fit_predict, X, y, spatial_block_split(coords, n_folds, seed=seed, **kw))
    knn = cross_validate(fit_predict, X, y, spatial_kfold_split(coords, n_folds, seed=seed))
    return {
        "random_kfold": rnd,
        "spatial_block": blk,
        "spatial_kmeans": knn,
        "r2_inflation": float(rnd["r2"] - blk["r2"]),
        "rmse_understatement": float(blk["rmse"] - rnd["rmse"]),
    }
