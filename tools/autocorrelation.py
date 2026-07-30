"""
Global and local spatial autocorrelation.

Generalised from the two submissions' implementations. The eip pipeline hand-rolled
Moran's I and Gi* in numpy; the fisher pipeline used esda. Both are reproduced here
against a single explicit weights argument, so a result can never be reported without
its specification.

Cross-checked against esda in analysis/01_weights_sensitivity.py.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np
from scipy.sparse import csr_matrix, issparse
from scipy.stats import norm


@dataclass(frozen=True)
class MoranResult:
    I: float
    expected_I: float
    z_score: float
    p_value: float
    n: int
    n_permutations: int
    perm_mean: float
    perm_sd: float

    def as_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return (f"Moran's I = {self.I:.4f}  E[I] = {self.expected_I:.4f}  "
                f"z = {self.z_score:.2f}  p = {self.p_value:.4f}  (n={self.n})")


def global_morans_i(
    values: np.ndarray,
    W: csr_matrix,
    *,
    n_permutations: int = 999,
    seed: int = 42,
    two_sided: bool = True,
) -> MoranResult:
    """
    Global Moran's I with a permutation null.

        I = (n / S0) * (z' W z) / (z' z),   z = values - mean

    The permutation null conditions on the observed values and reshuffles their
    locations, so it tests spatial arrangement rather than distributional shape. It
    makes no normality assumption -- but it does assume exchangeability, which is
    what fails when the weights matrix is itself estimated from the same data.
    """
    x = np.asarray(values, float).ravel()
    n = x.size
    if n < 3:
        raise ValueError("need at least 3 observations")
    Wm = W.tocsr() if issparse(W) else csr_matrix(W)
    if Wm.shape != (n, n):
        raise ValueError(f"weights {Wm.shape} do not match {n} values")

    z = x - x.mean()
    denom = float(z @ z)
    s0 = float(Wm.sum())
    if denom <= 0 or s0 <= 0:
        raise ValueError("degenerate input: zero variance or empty weights")

    observed = float((n / s0) * (z @ np.asarray(Wm @ z).ravel()) / denom)

    rng = np.random.default_rng(seed)
    perm = np.empty(n_permutations)
    for i in range(n_permutations):
        p = rng.permutation(z)
        perm[i] = (n / s0) * (p @ np.asarray(Wm @ p).ravel()) / denom

    sd = float(perm.std(ddof=1))
    if two_sided:
        hits = np.count_nonzero(np.abs(perm) >= abs(observed))
    else:
        hits = np.count_nonzero(perm >= observed)

    return MoranResult(
        I=observed,
        expected_I=-1.0 / (n - 1),
        z_score=float((observed - perm.mean()) / sd) if sd > 0 else float("nan"),
        p_value=float((hits + 1) / (n_permutations + 1)),
        n=n,
        n_permutations=n_permutations,
        perm_mean=float(perm.mean()),
        perm_sd=sd,
    )


def local_morans_i(
    values: np.ndarray,
    W: csr_matrix,
    *,
    n_permutations: int = 999,
    seed: int = 42,
) -> dict:
    """
    Local Moran's I (LISA), one statistic per location, with conditional permutation.

    Returns local I, pseudo p-values, and the HH/HL/LH/LL quadrant of the
    Moran scatterplot. Quadrants are reported for every unit; significance is not,
    so filter on p before interpreting them.
    """
    x = np.asarray(values, float).ravel()
    n = x.size
    Wm = W.tocsr() if issparse(W) else csr_matrix(W)
    z = x - x.mean()
    m2 = float(z @ z) / n

    lag = np.asarray(Wm @ z).ravel()
    local_I = z * lag / m2

    rng = np.random.default_rng(seed)
    deg = np.diff(Wm.indptr)
    greater = np.zeros(n, dtype=int)
    for i in range(n):
        k = deg[i]
        if k == 0:
            continue
        pool = np.delete(z, i)
        w_i = Wm.data[Wm.indptr[i]:Wm.indptr[i + 1]]
        samples = rng.choice(pool, size=(n_permutations, k), replace=True)
        sim = z[i] * (samples @ w_i) / m2
        greater[i] = np.count_nonzero(np.abs(sim) >= abs(local_I[i]))

    quadrant = np.where(z > 0, np.where(lag > 0, "HH", "HL"), np.where(lag > 0, "LH", "LL"))
    return {
        "local_I": local_I,
        "spatial_lag": lag,
        "p_sim": (greater + 1) / (n_permutations + 1),
        "quadrant": quadrant,
    }


def getis_ord_gi_star(values: np.ndarray, W: csr_matrix, *, include_self: bool = True) -> dict:
    """
    Getis-Ord Gi* z-scores with the analytic normal null.

    `include_self=True` gives Gi* (the focal unit counts in its own neighbourhood);
    False gives plain Gi. The distinction shifts z-scores enough to move borderline
    units across the 1.96 cutoff.

    p-values here are two-sided and uncorrected. With one test per location, expect
    ~5% false positives at alpha = 0.05 before any multiple-comparison adjustment --
    on 319 units that is ~16 spurious classifications, comparable to the number of
    genuine ones in the eip result.
    """
    x = np.asarray(values, float).ravel()
    n = x.size
    Wm = (W.tocsr() if issparse(W) else csr_matrix(W)).copy()
    if include_self:
        Wm = Wm.tolil()
        Wm.setdiag(1.0)
        Wm = Wm.tocsr()

    mean_x = float(x.mean())
    std_x = float(x.std(ddof=1))
    if std_x == 0:
        raise ValueError("zero variance")

    sw = np.asarray(Wm.sum(axis=1)).ravel()
    sw2 = np.asarray(Wm.power(2).sum(axis=1)).ravel()
    numer = np.asarray(Wm @ x).ravel() - mean_x * sw
    denom = std_x * np.sqrt(np.maximum((n * sw2 - sw**2) / (n - 1), 0.0))
    z = np.divide(numer, denom, out=np.zeros(n), where=denom > 0)
    return {"z": z, "p": 2.0 * norm.sf(np.abs(z))}


def classify_hotspots(z: np.ndarray, *, levels=(1.96, 2.58)) -> np.ndarray:
    """Bin Gi* z-scores into the conventional hot/cold classes at 95% and 99%."""
    z = np.asarray(z, float)
    a, b = levels
    out = np.full(len(z), "not_significant", dtype=object)
    out[(z >= a) & (z < b)] = "hot_spot_95"
    out[z >= b] = "hot_spot_99"
    out[(z <= -a) & (z > -b)] = "cold_spot_95"
    out[z <= -b] = "cold_spot_99"
    return out


def hotspot_counts(labels: np.ndarray) -> dict:
    """Hot/cold totals from classify_hotspots output."""
    return {
        "hot": int(np.isin(labels, ["hot_spot_95", "hot_spot_99"]).sum()),
        "cold": int(np.isin(labels, ["cold_spot_95", "cold_spot_99"]).sum()),
        "hot_99": int((labels == "hot_spot_99").sum()),
        "cold_99": int((labels == "cold_spot_99").sum()),
        "not_significant": int((labels == "not_significant").sum()),
    }
