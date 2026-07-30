"""
Mantel and partial Mantel tests.

Generalised from fisher/analysis/step2_mantel.py and colonial_mantel.py.

Mantel r is a normalised inner product of two matrices,

    r = tr(A B) / sqrt(tr A^2 * tr B^2)

after centering, so like Moran's I it is a degree-2 spectral functional -- and equally
dependent on the joint spectra of its inputs for its null distribution. The permutation
scheme below jointly permutes rows and columns, which preserves each matrix's internal
structure and is the only defensible null for dependent dissimilarities.

Known caveat, worth stating wherever these are used: Mantel and especially partial
Mantel have documented Type I error inflation when the underlying data are spatially
autocorrelated -- which is the only setting anyone applies them in (Guillot & Rousset
2013; Legendre et al. 2015). Treat p-values as indicative, and prefer reporting effect
size across several codings, as the fisher submission's sensitivity panel does.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np


@dataclass(frozen=True)
class MantelResult:
    r: float
    p_one_sided: float
    p_two_sided: float
    n_objects: int
    n_pairs: int
    n_permutations: int
    controls: tuple[str, ...] = ()

    def as_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        c = f" | {', '.join(self.controls)}" if self.controls else ""
        return (f"Mantel r{c} = {self.r:+.4f}  p(1) = {self.p_one_sided:.4f}  "
                f"p(2) = {self.p_two_sided:.4f}  ({self.n_pairs} pairs)")


def _check_square(*mats: np.ndarray) -> int:
    n = mats[0].shape[0]
    for m in mats:
        if m.ndim != 2 or m.shape != (n, n):
            raise ValueError("all inputs must be square matrices of the same size")
    return n


def _offdiag(m: np.ndarray) -> np.ndarray:
    n = m.shape[0]
    iu = np.triu_indices(n, k=1)
    return m[iu]


def _pearson(a: np.ndarray, b: np.ndarray) -> float:
    a = a - a.mean()
    b = b - b.mean()
    d = np.sqrt((a @ a) * (b @ b))
    return float(a @ b / d) if d > 0 else 0.0


def _residualise(y: np.ndarray, X: np.ndarray) -> np.ndarray:
    """Residuals of y on [1, X] by least squares."""
    A = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    return y - A @ beta


def mantel(
    A: np.ndarray,
    B: np.ndarray,
    *,
    n_permutations: int = 9999,
    seed: int = 42,
) -> MantelResult:
    """Simple Mantel test between two dissimilarity matrices."""
    A, B = np.asarray(A, float), np.asarray(B, float)
    n = _check_square(A, B)
    a, b = _offdiag(A), _offdiag(B)
    observed = _pearson(a, b)

    rng = np.random.default_rng(seed)
    iu = np.triu_indices(n, k=1)
    ge_one = ge_two = 0
    for _ in range(n_permutations):
        p = rng.permutation(n)
        bp = B[np.ix_(p, p)][iu]
        r = _pearson(a, bp)
        if r >= observed:
            ge_one += 1
        if abs(r) >= abs(observed):
            ge_two += 1

    return MantelResult(
        r=observed,
        p_one_sided=(ge_one + 1) / (n_permutations + 1),
        p_two_sided=(ge_two + 1) / (n_permutations + 1),
        n_objects=n,
        n_pairs=len(a),
        n_permutations=n_permutations,
    )


def partial_mantel(
    A: np.ndarray,
    B: np.ndarray,
    controls: dict[str, np.ndarray] | list[np.ndarray],
    *,
    n_permutations: int = 9999,
    seed: int = 42,
) -> MantelResult:
    """
    Partial Mantel: correlation of A and B after removing one or more control matrices
    from both, by residualising the off-diagonal vectors.

    Permutation is applied to B's row/column order, then the same residualisation is
    recomputed -- so the null respects the control structure rather than treating the
    residuals as exchangeable data in their own right.
    """
    A, B = np.asarray(A, float), np.asarray(B, float)
    if isinstance(controls, dict):
        names, mats = tuple(controls.keys()), [np.asarray(m, float) for m in controls.values()]
    else:
        mats = [np.asarray(m, float) for m in controls]
        names = tuple(f"control{i+1}" for i in range(len(mats)))
    n = _check_square(A, B, *mats)

    iu = np.triu_indices(n, k=1)
    a, b = A[iu], B[iu]
    C = np.column_stack([m[iu] for m in mats])

    ra, rb = _residualise(a, C), _residualise(b, C)
    observed = _pearson(ra, rb)

    rng = np.random.default_rng(seed)
    ge_one = ge_two = 0
    for _ in range(n_permutations):
        p = rng.permutation(n)
        bp = B[np.ix_(p, p)][iu]
        r = _pearson(ra, _residualise(bp, C))
        if r >= observed:
            ge_one += 1
        if abs(r) >= abs(observed):
            ge_two += 1

    return MantelResult(
        r=observed,
        p_one_sided=(ge_one + 1) / (n_permutations + 1),
        p_two_sided=(ge_two + 1) / (n_permutations + 1),
        n_objects=n,
        n_pairs=len(a),
        n_permutations=n_permutations,
        controls=names,
    )


def spectral_overlap(A: np.ndarray, B: np.ndarray) -> dict:
    """
    Diagnostic for how much shared spectral structure two dissimilarity matrices have.

    Motivation: Mantel r is tr(AB)/sqrt(tr A^2 tr B^2), so its null depends on the
    joint spectra. Two matrices whose leading eigenvectors nearly coincide will
    produce a large r under an enormous range of arrangements, and the permutation
    null understates that. This reports the alignment directly.
    """
    A, B = np.asarray(A, float), np.asarray(B, float)
    _check_square(A, B)
    ea, va = np.linalg.eigh(0.5 * (A + A.T))
    eb, vb = np.linalg.eigh(0.5 * (B + B.T))
    top_a, top_b = va[:, -1], vb[:, -1]
    return {
        "leading_eigenvector_alignment": float(abs(top_a @ top_b)),
        "effective_rank_A": float(np.exp(_entropy(np.abs(ea)))),
        "effective_rank_B": float(np.exp(_entropy(np.abs(eb)))),
        "spectral_radius_A": float(np.abs(ea).max()),
        "spectral_radius_B": float(np.abs(eb).max()),
    }


def _entropy(w: np.ndarray) -> float:
    s = w.sum()
    if s <= 0:
        return 0.0
    p = w / s
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())
