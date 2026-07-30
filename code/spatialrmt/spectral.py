"""
Spectral quantities for spatial weights matrices.

Why these and not others: every statistic the two submissions report is a functional of
the spectrum of a structured sparse matrix.

    Moran's I  = (n/S0) (z'Wz)/(z'z)          Rayleigh quotient
    Getis-Ord  = local quadratic forms in the same W
    Mantel r   = tr(D1 D2) / sqrt(tr D1^2 tr D2^2)
    CAR/SAR    Q = (I - rho W)/tau^2, so Q^-1 is the resolvent of W at z = 1/rho

The low-order moments (tr W, tr W^2, tr W^3) are geometry-blind -- the semicircle law
holds for any growing bandwidth because short backtracking walks never notice the finite
interaction range. Edge statistics need Chebyshev degree ~ n^(1/3), and walks that long
do feel the geometry. `chebyshev_coefficients` is the tool for that regime.
"""

from __future__ import annotations

import numpy as np
from scipy.sparse import csr_matrix, identity, issparse
from scipy.sparse.linalg import eigsh


def _dense(W) -> np.ndarray:
    return np.asarray(W.todense() if issparse(W) else W, dtype=float)


def spectrum(W, *, centered: bool = False) -> np.ndarray:
    """
    Eigenvalues of a symmetric weights matrix, ascending.

    `centered` applies M W M with M = I - 11'/n, projecting out the constant vector.
    That is exactly what Moran's I does, and it is the step that removes the Perron
    eigenvalue of a non-negative W -- which is what makes mean-zero random matrix
    theory applicable to an otherwise non-negative matrix.
    """
    A = _dense(W)
    A = 0.5 * (A + A.T)
    if centered:
        n = A.shape[0]
        M = np.eye(n) - np.ones((n, n)) / n
        A = M @ A @ M
    return np.linalg.eigvalsh(A)


def spectral_moments(W, max_order: int = 6, *, normalize: bool = True) -> np.ndarray:
    """
    Moments m_k = tr(W^k) / n for k = 1..max_order, computed from the spectrum.

    These are the quantities the classical Moran's I variance formula depends on
    (via S0, S1, S2), and they are the geometry-blind part of the spectrum.
    """
    ev = spectrum(W)
    n = len(ev)
    out = np.array([np.sum(ev**k) for k in range(1, max_order + 1)], dtype=float)
    return out / n if normalize else out


def chebyshev_coefficients(W, degrees, *, scale: float | None = None) -> np.ndarray:
    """
    mu(n) = (1/N) tr U_n(W_scaled), with U_n the Chebyshev polynomial of the second kind.

    U_n satisfies the three-term recurrence U_n = 2x U_{n-1} - U_{n-2}, which exactly
    matches extending a non-backtracking walk by one step and subtracting the immediate
    reversal -- so these coefficients count non-backtracking walks rather than the
    backtracking clutter that dominates ordinary moments. That is the object that
    carries edge information.

    `scale` divides the matrix to place the spectrum in [-1, 1]; defaults to the
    spectral radius.
    """
    ev = spectrum(W)
    s = scale if scale is not None else max(abs(ev[0]), abs(ev[-1]))
    if s <= 0:
        raise ValueError("degenerate spectrum")
    x = np.clip(ev / s, -1.0, 1.0)

    degrees = np.atleast_1d(np.asarray(degrees, dtype=int))
    dmax = int(degrees.max())
    n = len(x)

    out = np.empty(dmax + 1, dtype=float)
    u_prev = np.ones_like(x)          # U_0 = 1
    u_curr = 2.0 * x                  # U_1 = 2x
    out[0] = u_prev.mean()
    if dmax >= 1:
        out[1] = u_curr.mean()
    for d in range(2, dmax + 1):
        u_prev, u_curr = u_curr, 2.0 * x * u_curr - u_prev
        out[d] = u_curr.mean()
    return out[degrees]


def inverse_participation_ratio(W, *, k: int | None = None, which: str = "LA") -> np.ndarray:
    """
    IPR_j = sum_i v_ij^4 for unit-norm eigenvectors.

    A delocalised eigenvector spread over all n sites has IPR ~ 1/n; one localised on
    O(1) sites has IPR ~ O(1). The reciprocal 1/IPR estimates how many sites the
    eigenvector actually occupies.

    This is the quantity that decides what eigenvector spatial filtering is doing:
    delocalised Moran eigenvectors are global spatial trends, localised ones are bumps
    on a handful of neighbouring units.
    """
    A = _dense(W)
    A = 0.5 * (A + A.T)
    if k is None:
        _, vecs = np.linalg.eigh(A)
    else:
        _, vecs = eigsh(csr_matrix(A), k=k, which=which)
    return np.sum(vecs**4, axis=0)


def participation_number(W, **kw) -> np.ndarray:
    """1 / IPR -- the effective number of sites each eigenvector occupies."""
    return 1.0 / inverse_participation_ratio(W, **kw)


def resolvent(W, z: complex):
    """
    G(z) = (W - zI)^-1.

    For real z outside the spectrum this is the CAR/SAR covariance up to scaling:
    with Q = (I - rho W)/tau^2, Q^-1 = -(tau^2/rho) G(1/rho). So the admissible range
    of rho is exactly (1/lambda_min, 1/lambda_max).
    """
    A = _dense(W)
    return np.linalg.inv(A - z * np.eye(A.shape[0]))


def car_admissible_rho(W) -> tuple[float, float]:
    """Interval of rho for which the CAR/SAR precision (I - rho W) stays positive definite."""
    ev = spectrum(W)
    lo, hi = float(ev[0]), float(ev[-1])
    return (1.0 / lo if lo < 0 else -np.inf, 1.0 / hi if hi > 0 else np.inf)


def stieltjes_transform(W, z: complex) -> complex:
    """m(z) = (1/n) tr (W - z)^-1, from the spectrum."""
    ev = spectrum(W)
    return complex(np.mean(1.0 / (ev - z)))
