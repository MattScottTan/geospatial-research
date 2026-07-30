"""
Random band matrices and the Thouless threshold.

A periodic band matrix on Z/NZ with bandwidth W -- entries vanishing when the cyclic
distance exceeds W -- is a distance-band spatial weights matrix on a 1D transect.
Same object, different literature.

The Thouless criterion compares two scales at the spectral edge:

    mixing time of the band walk       n_mix  ~ N^(2/d) / W^2
    walk length that resolves the edge n_edge ~ N^(1/3)

Setting them equal gives the crossover bandwidth. In d = 1 that is W ~ N^(5/6), which
is Sodin's theorem. Extending the same heuristic to d dimensions gives

    W_c ~ N^(1/d - 1/6)        (radius)
    k_c ~ N^(1 - d/6)          (degree)

so in d = 2 -- actual geography -- edge universality needs degree ~ N^(2/3). For the
eip frame of 8,000 cities that is ~400 neighbours; standard practice is k = 8. Real
spatial weights matrices sit orders of magnitude below the threshold, in the regime
where geometry survives into the limit.

The d-dimensional exponents are the Thouless heuristic transplanted, not a theorem. The
1D proof's Fourier diagonalisation of the band walk does not carry over.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.sparse import csr_matrix


# --------------------------------------------------------------------------
# Ensembles
# --------------------------------------------------------------------------
def periodic_band_matrix(
    N: int,
    W: int,
    *,
    beta: int = 1,
    rng: np.random.Generator | None = None,
    normalize: bool = True,
) -> np.ndarray:
    """
    Periodic random band matrix on Z/NZ.

    beta = 1 gives real symmetric entries with random signs (orthogonal class);
    beta = 2 gives random phases (unitary class). Entries are unimodular, so every
    non-zero has modulus 1 and the expectation of a product along a closed walk is
    either 0 or 1.

    With `normalize`, divides by 2*sqrt(2W) to place the spectrum on [-1, 1].
    """
    if not 1 <= W < N / 2:
        raise ValueError("require 1 <= W < N/2")
    rng = rng or np.random.default_rng()

    idx = np.arange(N)
    d = np.abs(idx[:, None] - idx[None, :])
    cyclic = np.minimum(d, N - d)
    band = (cyclic <= W) & (cyclic > 0)

    iu = np.triu(band, k=1)
    if beta == 1:
        vals = rng.choice([-1.0, 1.0], size=iu.sum())
        H = np.zeros((N, N))
        H[iu] = vals
        H = H + H.T
    elif beta == 2:
        vals = np.exp(1j * rng.uniform(0, 2 * np.pi, size=iu.sum()))
        H = np.zeros((N, N), dtype=complex)
        H[iu] = vals
        H = H + H.conj().T
    else:
        raise ValueError("beta must be 1 or 2")

    return H / (2.0 * np.sqrt(2.0 * W)) if normalize else H


def band_adjacency(N: int, W: int, *, periodic: bool = True) -> csr_matrix:
    """
    Deterministic band adjacency -- the graph a distance-band weights matrix induces
    on evenly spaced points along a line (or cycle).
    """
    idx = np.arange(N)
    d = np.abs(idx[:, None] - idx[None, :])
    if periodic:
        d = np.minimum(d, N - d)
    A = ((d <= W) & (d > 0)).astype(float)
    return csr_matrix(A)


# --------------------------------------------------------------------------
# The threshold
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class ThoulessRegime:
    n: int
    d: int
    degree: float
    critical_degree: float
    critical_radius: float
    ratio: float

    @property
    def regime(self) -> str:
        if self.ratio >= 1.0:
            return "supercritical (geometry invisible, Airy/Tracy-Widom edge)"
        if self.ratio >= 0.5:
            return "near-critical"
        return "subcritical (geometry visible, deterministic edge)"

    def __str__(self) -> str:
        return (
            f"n={self.n} d={self.d} degree={self.degree:.0f} "
            f"critical={self.critical_degree:.0f} ratio={self.ratio:.4f}\n  {self.regime}"
        )


def thouless_threshold(n: int, d: int = 2) -> tuple[float, float]:
    """
    Critical (radius, degree) for edge universality at n points in d dimensions.

        radius ~ n^(1/d - 1/6),  degree ~ n^(1 - d/6)

    d = 1 returns n^(5/6), recovering Sodin's threshold as a consistency check.
    """
    if n < 2 or d < 1:
        raise ValueError("need n >= 2, d >= 1")
    return float(n ** (1.0 / d - 1.0 / 6.0)), float(n ** (1.0 - d / 6.0))


def classify_regime(n: int, degree: float, d: int = 2) -> ThoulessRegime:
    """Where a given weights matrix sits relative to the edge-universality threshold."""
    radius_c, degree_c = thouless_threshold(n, d)
    return ThoulessRegime(
        n=n, d=d, degree=float(degree),
        critical_degree=degree_c, critical_radius=radius_c,
        ratio=float(degree) / degree_c,
    )


def mixing_time(n: int, bandwidth: float, d: int = 2) -> float:
    """n_mix ~ n^(2/d) / W^2 -- steps for the band walk to spread across the domain."""
    return float(n ** (2.0 / d) / bandwidth**2)


def edge_resolution_length(n: int) -> float:
    """n_edge ~ n^(1/3) -- walk length needed to resolve individual edge eigenvalues."""
    return float(n ** (1.0 / 3.0))


# --------------------------------------------------------------------------
# Reference laws
# --------------------------------------------------------------------------
def semicircle_density(x: np.ndarray, radius: float = 1.0) -> np.ndarray:
    """Wigner semicircle on [-radius, radius], normalised to integrate to 1."""
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    m = np.abs(x) <= radius
    out[m] = 2.0 * np.sqrt(radius**2 - x[m] ** 2) / (np.pi * radius**2)
    return out


def tracy_widom_edge_scale(n: int) -> float:
    """The n^(-2/3) soft-edge fluctuation scale."""
    return float(n ** (-2.0 / 3.0))


def subcritical_edge_scale(bandwidth: float) -> float:
    """
    The W^(-4/5) edge scale in the subcritical regime.

    Below threshold the walk has not mixed, so the effective system size is the
    diffusive reach W*sqrt(n) rather than n, and the edge is resolved at a different
    polynomial degree -- giving W^(-4/5) in place of n^(-2/3).
    """
    return float(bandwidth ** (-4.0 / 5.0))
