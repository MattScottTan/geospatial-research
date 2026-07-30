"""
Spatial regression: global lag/error models and local (geographically weighted) fits.

Two classical answers to "OLS residuals are spatially autocorrelated":

  1. Model the dependence globally -- SAR (lag), SEM (error), or CAR. One coefficient
     per covariate, plus a dependence parameter.
  2. Let the coefficients vary in space -- GWR. No dependence parameter, but a
     coefficient surface instead of a number.

They answer different questions and disagreeing results are informative rather than
contradictory. What they share is a hazard: both can absorb the covariate's own signal
into the spatial term. That is spatial confounding, and it is why the eip submission's
GP and CAR distance coefficients differ by a factor of four (-0.207 vs -0.052). See
`spatial_confounding_diagnostic` and ../theory item 4.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.sparse import csr_matrix, identity, issparse
from scipy.stats import chi2, norm


def _dense(W):
    return np.asarray(W.todense() if issparse(W) else W, float)


def _design(X):
    X = np.atleast_2d(np.asarray(X, float))
    if X.shape[0] == 1 and X.shape[1] != 1:
        X = X.T
    return np.column_stack([np.ones(len(X)), X])


@dataclass
class SpatialRegressionResult:
    model: str
    beta: np.ndarray
    rho: float
    sigma2: float
    log_likelihood: float
    n: int
    k: int
    aic: float
    names: tuple[str, ...] = ()

    def as_dict(self):
        d = asdict(self)
        d["beta"] = self.beta.tolist()
        return d

    def __str__(self):
        names = self.names or tuple(["intercept"] + [f"x{i}" for i in range(1, len(self.beta))])
        lines = [f"{self.model}  n={self.n}  rho={self.rho:+.4f}  "
                 f"sigma2={self.sigma2:.4f}  logL={self.log_likelihood:.2f}  AIC={self.aic:.1f}"]
        lines += [f"    {n:<22s} {b:+.6f}" for n, b in zip(names, self.beta)]
        return "\n".join(lines)


# --------------------------------------------------------------------------
def sar_lag(y, X, W, *, names=()) -> SpatialRegressionResult:
    """
    Spatial autoregressive (lag) model:  y = rho W y + X beta + eps

    Fitted by concentrated maximum likelihood over rho. The lag term means a shock at
    one location propagates to its neighbours and back, so beta is no longer a
    marginal effect -- interpreting it as one is a standard error in applied work.
    """
    y = np.asarray(y, float).ravel()
    Xd, Wd, n = _design(X), _dense(W), len(y)
    Wy = Wd @ y
    ev = np.linalg.eigvals(Wd).real
    lo, hi = 1.0 / ev.min() + 1e-6, 1.0 / ev.max() - 1e-6

    def neg_ll(rho):
        e = y - rho * Wy
        b, *_ = np.linalg.lstsq(Xd, e, rcond=None)
        r = e - Xd @ b
        s2 = float(r @ r) / n
        sign, logdet = np.linalg.slogdet(np.eye(n) - rho * Wd)
        if sign <= 0 or s2 <= 0:
            return 1e12
        return -(logdet - n / 2.0 * np.log(2 * np.pi * s2) - n / 2.0)

    rho = float(minimize_scalar(neg_ll, bounds=(lo, hi), method="bounded").x)
    e = y - rho * Wy
    beta, *_ = np.linalg.lstsq(Xd, e, rcond=None)
    r = e - Xd @ beta
    s2 = float(r @ r) / n
    ll = -neg_ll(rho)
    k = len(beta) + 2
    return SpatialRegressionResult("SAR (lag)", beta, rho, s2, ll, n, k,
                                   2 * k - 2 * ll, names)


def sem_error(y, X, W, *, names=()) -> SpatialRegressionResult:
    """
    Spatial error model:  y = X beta + u,  u = lambda W u + eps

    Dependence is confined to the disturbance, so beta keeps its usual marginal
    interpretation. Prefer this when spatial structure is a nuisance rather than the
    mechanism of interest.
    """
    y = np.asarray(y, float).ravel()
    Xd, Wd, n = _design(X), _dense(W), len(y)
    ev = np.linalg.eigvals(Wd).real
    lo, hi = 1.0 / ev.min() + 1e-6, 1.0 / ev.max() - 1e-6

    def neg_ll(lam):
        A = np.eye(n) - lam * Wd
        ys, Xs = A @ y, A @ Xd
        b, *_ = np.linalg.lstsq(Xs, ys, rcond=None)
        r = ys - Xs @ b
        s2 = float(r @ r) / n
        sign, logdet = np.linalg.slogdet(A)
        if sign <= 0 or s2 <= 0:
            return 1e12
        return -(logdet - n / 2.0 * np.log(2 * np.pi * s2) - n / 2.0)

    lam = float(minimize_scalar(neg_ll, bounds=(lo, hi), method="bounded").x)
    A = np.eye(n) - lam * Wd
    beta, *_ = np.linalg.lstsq(A @ Xd, A @ y, rcond=None)
    r = A @ y - A @ Xd @ beta
    s2 = float(r @ r) / n
    ll = -neg_ll(lam)
    k = len(beta) + 2
    return SpatialRegressionResult("SEM (error)", beta, lam, s2, ll, n, k,
                                   2 * k - 2 * ll, names)


def lm_tests(y, X, W) -> dict:
    """
    Lagrange multiplier tests for which spatial model to use, run on OLS residuals.

    The standard decision rule: if only LM-lag is significant use SAR, if only LM-error
    use SEM, if both use whichever robust version is stronger. Reported here so the
    model choice can be justified rather than asserted.
    """
    y = np.asarray(y, float).ravel()
    Xd, Wd, n = _design(X), _dense(W), len(y)
    b, *_ = np.linalg.lstsq(Xd, y, rcond=None)
    u = y - Xd @ b
    s2 = float(u @ u) / n

    T = np.trace(Wd @ Wd + Wd.T @ Wd)
    lm_err = (float(u @ Wd @ u) / s2) ** 2 / T

    Wy = Wd @ y
    M = np.eye(n) - Xd @ np.linalg.pinv(Xd)
    j = (float(Wy @ M @ Wy) / s2 + T) / n
    lm_lag = (float(u @ Wd @ y) / s2) ** 2 / (n * j)

    return {
        "LM_error": float(lm_err), "LM_error_p": float(chi2.sf(lm_err, 1)),
        "LM_lag": float(lm_lag), "LM_lag_p": float(chi2.sf(lm_lag, 1)),
        "recommendation": _lm_recommend(chi2.sf(lm_err, 1), chi2.sf(lm_lag, 1)),
    }


def _lm_recommend(p_err, p_lag, alpha=0.05):
    e, l = p_err < alpha, p_lag < alpha
    if e and l:
        return "both significant -- compare robust LM variants, or fit SARAR"
    if e:
        return "SEM (spatial error)"
    if l:
        return "SAR (spatial lag)"
    return "no spatial dependence detected in residuals -- OLS may suffice"


# --------------------------------------------------------------------------
def gwr(y, X, coords, *, bandwidth: float, kernel: str = "gaussian",
        distance: np.ndarray | None = None) -> dict:
    """
    Geographically weighted regression: one weighted least-squares fit per location,
    weighting nearby observations more heavily.

    Returns a coefficient surface rather than a single beta. Bandwidth is the whole
    ballgame -- too small and you fit noise, too large and it collapses to OLS. Use
    `gwr_bandwidth_selection` rather than guessing.

    Caveat: local t-statistics on GWR surfaces are badly overconfident, because every
    observation contributes to many local fits. Treat the surface as exploratory.
    """
    y = np.asarray(y, float).ravel()
    Xd = _design(X)
    n, p = Xd.shape
    if distance is None:
        c = np.asarray(coords, float)
        distance = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=-1)
    D = np.asarray(distance, float)

    if kernel == "gaussian":
        Wt = np.exp(-0.5 * (D / bandwidth) ** 2)
    elif kernel == "bisquare":
        Wt = np.where(D <= bandwidth, (1 - (D / bandwidth) ** 2) ** 2, 0.0)
    elif kernel == "exponential":
        Wt = np.exp(-D / bandwidth)
    else:
        raise ValueError(f"unknown kernel {kernel!r}")

    beta = np.empty((n, p))
    fitted = np.empty(n)
    trace_S = 0.0
    for i in range(n):
        w = Wt[i]
        XtW = Xd.T * w
        try:
            inv = np.linalg.pinv(XtW @ Xd)
        except np.linalg.LinAlgError:
            beta[i] = np.nan; fitted[i] = np.nan; continue
        b = inv @ (XtW @ y)
        beta[i] = b
        fitted[i] = Xd[i] @ b
        trace_S += float(Xd[i] @ inv @ XtW[:, i])

    resid = y - fitted
    rss = float(resid @ resid)
    return {
        "beta": beta,
        "fitted": fitted,
        "residuals": resid,
        "bandwidth": float(bandwidth),
        "effective_parameters": float(trace_S),
        "rss": rss,
        "aicc": float(n * np.log(rss / n) + n * np.log(2 * np.pi)
                      + n * (n + trace_S) / (n - 2 - trace_S)),
        "r2": float(1 - rss / ((y - y.mean()) ** 2).sum()),
    }


def gwr_bandwidth_selection(y, X, coords, *, candidates=None, **kw) -> dict:
    """Golden-section-free grid search on corrected AIC. Returns the best bandwidth."""
    if kw.get("distance") is not None:
        D = np.asarray(kw["distance"], float)
    else:
        c = np.asarray(coords, float)
        D = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=-1)
        kw["distance"] = D
    if candidates is None:
        off = D[np.triu_indices(len(D), 1)]
        candidates = np.percentile(off, [5, 10, 20, 30, 50, 75])
    scores = []
    for bw in candidates:
        try:
            scores.append((float(bw), gwr(y, X, coords, bandwidth=float(bw), **kw)["aicc"]))
        except Exception:
            scores.append((float(bw), np.inf))
    best = min(scores, key=lambda t: t[1])
    return {"best_bandwidth": best[0], "best_aicc": best[1], "grid": scores}


# --------------------------------------------------------------------------
def spatial_confounding_diagnostic(x, W, *, n_components: int = 10) -> dict:
    """
    How much of a covariate lives in the low-frequency subspace a spatial prior wants
    to explain.

    Project x onto the leading eigenvectors of the doubly-centred weights matrix -- the
    smooth, large-scale spatial patterns. A covariate concentrated there is nearly
    collinear with the spatial random effect, so the fixed-effect estimate becomes
    unstable and depends on the prior rather than the data. That is the mechanism
    behind the eip GP-vs-CAR discrepancy.

    `low_frequency_share` near 1 is a warning; near 0 means the covariate carries
    information the spatial term cannot absorb.
    """
    x = np.asarray(x, float).ravel()
    Wd = _dense(W)
    n = len(x)
    M = np.eye(n) - np.ones((n, n)) / n
    A = M @ (0.5 * (Wd + Wd.T)) @ M
    ev, vecs = np.linalg.eigh(A)
    order = np.argsort(ev)[::-1]
    ev, vecs = ev[order], vecs[:, order]

    xc = x - x.mean()
    total = float(xc @ xc)
    proj = vecs.T @ xc
    share = float((proj[:n_components] ** 2).sum() / total) if total > 0 else np.nan
    return {
        "low_frequency_share": share,
        "n_components": int(n_components),
        "cumulative_share": (np.cumsum(proj**2) / total)[:n_components].tolist(),
        "leading_eigenvalues": ev[:n_components].tolist(),
        "interpretation": (
            "severe: covariate largely inside the spatial prior's subspace"
            if share > 0.5 else
            "moderate: some overlap with the spatial subspace"
            if share > 0.2 else
            "mild: covariate mostly orthogonal to the smooth spatial basis"
        ),
    }
