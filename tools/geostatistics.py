"""
Classical geostatistics: variograms and kriging.

The oldest tools in the field (Matheron, 1960s) and still the reference point for
spatial prediction. They matter to this repo for a reason beyond tradition: kriging is
kernel ridge regression with a covariance kernel, so the kriging system's behaviour is
governed by the spectrum of that kernel matrix. `kernel_spectrum_diagnostics` exposes
that directly, which is the entry point for the benign-overfitting question in
../theory (does interpolating -- nugget to zero -- hurt on a spatial design?).

Variogram models follow the standard parameterisation: nugget + partial sill * shape(h/range).
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Callable, Literal

import numpy as np
from scipy.optimize import least_squares
from scipy.special import gamma, kv

ModelName = Literal["exponential", "gaussian", "spherical", "matern"]


# --------------------------------------------------------------------------
# Variogram models
# --------------------------------------------------------------------------
def exponential(h, nugget, sill, rng_):
    return nugget + sill * (1.0 - np.exp(-h / rng_))


def gaussian(h, nugget, sill, rng_):
    return nugget + sill * (1.0 - np.exp(-((h / rng_) ** 2)))


def spherical(h, nugget, sill, rng_):
    h = np.asarray(h, float)
    r = np.clip(h / rng_, 0, 1)
    return nugget + sill * (1.5 * r - 0.5 * r**3) * (h <= rng_) + sill * (h > rng_)


def matern(h, nugget, sill, rng_, nu=1.5):
    """
    Matern variogram. nu controls smoothness: 0.5 is exponential, large nu approaches
    gaussian. nu = 1.5 and 2.5 are the common choices because they give closed forms
    and correspond to once- and twice-differentiable fields.
    """
    h = np.atleast_1d(np.asarray(h, float))
    out = np.full_like(h, nugget + sill)
    m = h > 0
    if np.any(m):
        s = np.sqrt(2.0 * nu) * h[m] / rng_
        corr = (2.0 ** (1.0 - nu) / gamma(nu)) * (s**nu) * kv(nu, s)
        out[m] = nugget + sill * (1.0 - corr)
    out[~m] = nugget
    return out


MODELS: dict[str, Callable] = {
    "exponential": exponential,
    "gaussian": gaussian,
    "spherical": spherical,
    "matern": matern,
}


# --------------------------------------------------------------------------
# Empirical variogram
# --------------------------------------------------------------------------
@dataclass
class Variogram:
    lags: np.ndarray
    semivariance: np.ndarray
    counts: np.ndarray
    model: str | None = None
    params: dict | None = None

    def predict(self, h):
        if self.model is None:
            raise ValueError("no model fitted; call fit() first")
        return MODELS[self.model](h, **self.params)

    def __str__(self):
        s = f"Variogram: {len(self.lags)} lags, {int(self.counts.sum())} pairs"
        if self.model:
            p = ", ".join(f"{k}={v:.4g}" for k, v in self.params.items())
            s += f"\n  {self.model}({p})"
        return s


def empirical_variogram(
    coords: np.ndarray,
    values: np.ndarray,
    *,
    n_lags: int = 15,
    max_dist: float | None = None,
    distance: np.ndarray | None = None,
) -> Variogram:
    """
    Classical method-of-moments semivariogram.

        gamma(h) = (1 / 2N(h)) * sum over pairs at lag h of (z_i - z_j)^2

    Pass `distance` to supply a precomputed matrix (e.g. great-circle km) rather than
    letting Euclidean distance be computed on lat/lon, which is wrong at global scale.
    """
    z = np.asarray(values, float).ravel()
    n = len(z)
    if distance is None:
        c = np.asarray(coords, float)
        distance = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=-1)
    D = np.asarray(distance, float)
    if D.shape != (n, n):
        raise ValueError("distance matrix does not match values")

    iu = np.triu_indices(n, k=1)
    d, sq = D[iu], (z[iu[0]] - z[iu[1]]) ** 2
    if max_dist is None:
        max_dist = np.percentile(d, 50)  # half the max separation is the usual cutoff
    keep = d <= max_dist
    d, sq = d[keep], sq[keep]

    edges = np.linspace(0, max_dist, n_lags + 1)
    idx = np.clip(np.digitize(d, edges) - 1, 0, n_lags - 1)
    lags, semi, cnt = [], [], []
    for b in range(n_lags):
        m = idx == b
        if m.sum() >= 2:
            lags.append(d[m].mean())
            semi.append(0.5 * sq[m].mean())
            cnt.append(int(m.sum()))
    return Variogram(np.array(lags), np.array(semi), np.array(cnt))


def fit_variogram(vg: Variogram, model: ModelName = "exponential", *, nu: float = 1.5) -> Variogram:
    """
    Weighted least-squares fit, weighting each lag by its pair count -- the standard
    Cressie weighting, which stops sparse far lags dominating.
    """
    h, g, w = vg.lags, vg.semivariance, np.sqrt(vg.counts)
    sill0 = float(np.nanmax(g))
    rng0 = float(np.nanmax(h) / 3.0)
    p0 = [max(g[0] * 0.5, 1e-8), max(sill0, 1e-8), max(rng0, 1e-8)]

    fn = MODELS[model]

    def resid(p):
        nug, sill, r = np.abs(p)
        pred = fn(h, nug, sill, r, nu) if model == "matern" else fn(h, nug, sill, r)
        return w * (pred - g)

    sol = least_squares(resid, p0, method="trf")
    nug, sill, r = np.abs(sol.x)
    params = {"nugget": float(nug), "sill": float(sill), "rng_": float(r)}
    if model == "matern":
        params["nu"] = float(nu)
    vg.model, vg.params = model, params
    return vg


# --------------------------------------------------------------------------
# Kriging
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class KrigingResult:
    prediction: np.ndarray
    variance: np.ndarray

    def as_dict(self):
        return asdict(self)


def _cov_from_variogram(D, vg: Variogram) -> np.ndarray:
    total = vg.params["nugget"] + vg.params["sill"]
    return total - vg.predict(D)


def ordinary_kriging(
    coords: np.ndarray,
    values: np.ndarray,
    targets: np.ndarray,
    vg: Variogram,
    *,
    distance: np.ndarray | None = None,
    target_distance: np.ndarray | None = None,
) -> KrigingResult:
    """
    Ordinary kriging: BLUP with an unknown constant mean, enforced by a Lagrange
    multiplier on the weights summing to one.

    Returns predictions and kriging variance. The variance is the honest part of
    kriging and the reason it is still used -- it grows away from data in a way that
    machine-learning predictors generally do not report.
    """
    z = np.asarray(values, float).ravel()
    n = len(z)
    if distance is None:
        c = np.asarray(coords, float)
        distance = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=-1)
    if target_distance is None:
        c, t = np.asarray(coords, float), np.asarray(targets, float)
        target_distance = np.linalg.norm(t[:, None, :] - c[None, :, :], axis=-1)

    C = _cov_from_variogram(np.asarray(distance, float), vg)
    c0 = _cov_from_variogram(np.asarray(target_distance, float), vg)

    A = np.ones((n + 1, n + 1))
    A[:n, :n] = C
    A[n, n] = 0.0

    m = len(c0)
    pred, var = np.empty(m), np.empty(m)
    total = vg.params["nugget"] + vg.params["sill"]
    lu = np.linalg.pinv(A)
    for i in range(m):
        b = np.ones(n + 1)
        b[:n] = c0[i]
        sol = lu @ b
        w = sol[:n]
        pred[i] = w @ z
        var[i] = max(total - (w @ c0[i] + sol[n]), 0.0)
    return KrigingResult(pred, var)


def kernel_spectrum_diagnostics(distance: np.ndarray, vg: Variogram) -> dict:
    """
    Spectral condition of the kriging system.

    Kriging solves a linear system in the covariance matrix, so its stability is a
    statement about that matrix's spectrum. The nugget acts as ridge regularisation --
    it lifts the smallest eigenvalue off zero. Sending it to zero is exactly the
    interpolation limit where benign-overfitting theory applies, and where spatial
    designs violate the i.i.d. assumptions that theory is usually proved under.
    """
    C = _cov_from_variogram(np.asarray(distance, float), vg)
    ev = np.linalg.eigvalsh(0.5 * (C + C.T))
    ev = np.sort(ev)[::-1]
    pos = ev[ev > 0]
    return {
        "n": int(C.shape[0]),
        "condition_number": float(ev[0] / ev[-1]) if ev[-1] > 0 else float("inf"),
        "eigenvalue_max": float(ev[0]),
        "eigenvalue_min": float(ev[-1]),
        "effective_rank": float(np.exp(-np.sum((pos / pos.sum()) * np.log(pos / pos.sum())))),
        "nugget_fraction": float(vg.params["nugget"] / (vg.params["nugget"] + vg.params["sill"])),
        "negative_eigenvalues": int((ev < -1e-10).sum()),
    }
