"""
Moran eigenvector maps (MEM) and eigenvector spatial filtering (ESF).

Standard practice in spatial ecology and econometrics: take the eigenvectors of the
doubly-centred weights matrix MWM, treat them as synthetic spatial predictors, select
some, and add them to a regression to soak up spatial autocorrelation.

The eigenvectors are orthogonal by construction and each has a known Moran's I --
eigenvalue lambda_i corresponds to Moran's I of (n/S0) * lambda_i -- so they form a
basis ordered from large-scale patterns to fine-grained ones. That much is standard.

What is not standard, and is why this module carries `localisation_report`: whether
those eigenvectors are *global patterns at all* depends on the weights matrix. A
delocalised eigenvector spread over the whole domain is a spatial trend. A localised
one supported on a handful of neighbouring units is a bump. Both get called "a spatial
filter" and entered into the regression identically, but they mean different things,
and selection by correlation with y cannot tell them apart.

analysis/02_band_matrix_edge.py finds occupancy of ~8% at the bandwidth analogous to the
k = 8 both submissions use. Check before interpreting.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.sparse import issparse


def _dense(W):
    return np.asarray(W.todense() if issparse(W) else W, float)


@dataclass
class MEMBasis:
    vectors: np.ndarray        # (n, m) eigenvectors, descending eigenvalue
    eigenvalues: np.ndarray    # (m,)
    moran_I: np.ndarray        # Moran's I of each eigenvector
    occupancy: np.ndarray      # 1/IPR, effective number of units occupied
    n: int

    def positive(self) -> "MEMBasis":
        """Keep only eigenvectors with positive Moran's I (positive autocorrelation)."""
        m = self.moran_I > 0
        return MEMBasis(self.vectors[:, m], self.eigenvalues[m],
                        self.moran_I[m], self.occupancy[m], self.n)

    def __str__(self):
        return (f"MEM basis: {self.vectors.shape[1]} vectors, n={self.n}\n"
                f"  Moran's I  {self.moran_I.min():+.3f} to {self.moran_I.max():+.3f}\n"
                f"  occupancy  {self.occupancy.min():.0f} to {self.occupancy.max():.0f} "
                f"of {self.n} units "
                f"({self.occupancy.min()/self.n:.1%} to {self.occupancy.max()/self.n:.1%})")


def moran_eigenvectors(W, *, max_vectors: int | None = None) -> MEMBasis:
    """
    Eigen-decomposition of the doubly-centred weights matrix MWM, M = I - 11'/n.

    The centering is not cosmetic: it removes the constant vector, which for a
    non-negative W carries the Perron eigenvalue. That is what leaves a spectrum
    resembling a mean-zero random matrix rather than one dominated by a single spike.
    """
    Wd = _dense(W)
    n = Wd.shape[0]
    M = np.eye(n) - np.ones((n, n)) / n
    A = M @ (0.5 * (Wd + Wd.T)) @ M

    ev, vecs = np.linalg.eigh(A)
    order = np.argsort(ev)[::-1]
    ev, vecs = ev[order], vecs[:, order]

    keep = np.abs(ev) > 1e-10
    ev, vecs = ev[keep], vecs[:, keep]
    if max_vectors:
        ev, vecs = ev[:max_vectors], vecs[:, :max_vectors]

    s0 = float(Wd.sum())
    moran = (n / s0) * ev if s0 > 0 else np.full_like(ev, np.nan)
    occupancy = 1.0 / np.sum(vecs**4, axis=0)
    return MEMBasis(vecs, ev, moran, occupancy, n)


def select_eigenvectors(
    basis: MEMBasis,
    y: np.ndarray,
    *,
    method: str = "correlation",
    max_select: int = 20,
    alpha: float = 0.05,
) -> dict:
    """
    Choose which eigenvectors enter the regression.

    `correlation` ranks by |corr(v_i, y)| and keeps those passing an uncorrected
    two-sided test; `forward` adds vectors greedily while adjusted R^2 improves.

    Both are selection on the response. The subsequent regression p-values are
    therefore selective and not valid as reported -- the standard practice in the ESF
    literature, and a real inferential problem rather than a technicality. The returned
    dict includes `n_candidates` so the size of the selection can at least be stated.
    """
    y = np.asarray(y, float).ravel()
    V = basis.vectors
    n, m = V.shape
    yc = y - y.mean()

    if method == "correlation":
        r = (V.T @ yc) / (np.linalg.norm(yc) * np.linalg.norm(V, axis=0))
        t = r * np.sqrt((n - 2) / np.maximum(1 - r**2, 1e-12))
        from scipy.stats import t as tdist
        p = 2 * tdist.sf(np.abs(t), n - 2)
        idx = np.flatnonzero(p < alpha)
        idx = idx[np.argsort(-np.abs(r[idx]))][:max_select]
    elif method == "forward":
        idx, remaining, best = [], list(range(m)), -np.inf
        while remaining and len(idx) < max_select:
            gains = []
            for j in remaining:
                X = np.column_stack([np.ones(n)] + [V[:, k] for k in idx + [j]])
                b, *_ = np.linalg.lstsq(X, y, rcond=None)
                rss = float(((y - X @ b) ** 2).sum())
                k_ = X.shape[1]
                adj = 1 - (rss / (n - k_)) / (((y - y.mean()) ** 2).sum() / (n - 1))
                gains.append((adj, j))
            adj, j = max(gains)
            if adj <= best:
                break
            best, _ = adj, idx.append(j)
            remaining.remove(j)
        idx = np.array(idx, dtype=int)
    else:
        raise ValueError(f"unknown method {method!r}")

    sel_occ = basis.occupancy[idx] if len(idx) else np.array([])
    return {
        "selected": idx,
        "n_selected": int(len(idx)),
        "n_candidates": int(m),
        "moran_I": basis.moran_I[idx],
        "occupancy": sel_occ,
        "mean_occupancy_fraction": float(sel_occ.mean() / basis.n) if len(idx) else np.nan,
        "method": method,
    }


def esf_regression(y, X, basis: MEMBasis, selected: np.ndarray) -> dict:
    """OLS of y on [X, selected eigenvectors], reporting how much each block explains."""
    y = np.asarray(y, float).ravel()
    n = len(y)
    Xa = np.asarray(X, float).reshape(n, -1)
    base = np.column_stack([np.ones(n), Xa])
    full = np.column_stack([base, basis.vectors[:, selected]]) if len(selected) else base

    def _fit(D):
        b, *_ = np.linalg.lstsq(D, y, rcond=None)
        r = y - D @ b
        return b, float(r @ r)

    b0, rss0 = _fit(base)
    b1, rss1 = _fit(full)
    tss = float(((y - y.mean()) ** 2).sum())
    return {
        "beta_covariates_only": b0,
        "beta_with_filters": b1[: base.shape[1]],
        "r2_covariates_only": 1 - rss0 / tss,
        "r2_with_filters": 1 - rss1 / tss,
        "r2_gain": (rss0 - rss1) / tss,
        "n_filters": int(len(selected)),
        "coefficient_shift": (b1[: base.shape[1]] - b0).tolist(),
    }


def localisation_report(basis: MEMBasis, *, top: int = 20) -> dict:
    """
    Are the leading eigenvectors global trends or local bumps?

    Occupancy near n means delocalised (a genuine large-scale pattern); occupancy of a
    few units means the "spatial filter" is a bump on a handful of neighbours. The
    verdict field is deliberately blunt because this determines whether an ESF result
    means what its authors usually say it means.
    """
    occ = basis.occupancy[:top]
    frac = occ / basis.n
    return {
        "n": basis.n,
        "top": int(top),
        "occupancy_mean": float(occ.mean()),
        "occupancy_fraction_mean": float(frac.mean()),
        "occupancy_fraction_min": float(frac.min()),
        "occupancy_fraction_max": float(frac.max()),
        "verdict": (
            "delocalised -- eigenvectors are global spatial trends"
            if frac.mean() > 0.30 else
            "intermediate -- some eigenvectors are regional rather than global"
            if frac.mean() > 0.10 else
            "localised -- eigenvectors are local bumps, not spatial trends; "
            "ESF here is fitting local structure"
        ),
    }
