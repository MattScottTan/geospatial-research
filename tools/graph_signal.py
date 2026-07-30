"""
Graph signal processing on spatial graphs: propagation operators and Chebyshev filters.

This is where the modern ML side meets the thesis directly. Spectral graph neural
networks (ChebNet, Defferrard et al. 2016) build filters as Chebyshev polynomials of a
scaled graph operator, precisely to get K-hop-localised filters without an
eigendecomposition. `chebyshev_filter` below is that construction.

The connection worth chasing: a K-th order Chebyshev filter on a geometric graph has a
receptive field of K hops, so whether it "sees" global geometry or only local structure
is a race between how fast the walk mixes and how many hops the filter has. That is the
Thouless comparison. Oversmoothing -- the well-known failure where deep GNNs make every
node representation identical -- is what happens once the walk has mixed and the
geometry has been washed out.

`oversmoothing_curve` measures that collapse directly, and `mixing_diagnostics` reports
the spectral gap that sets its rate.
"""

from __future__ import annotations

import numpy as np
from scipy.sparse import csr_matrix, diags, identity, issparse


def _sparse(W) -> csr_matrix:
    return W.tocsr() if issparse(W) else csr_matrix(np.asarray(W, float))


# --------------------------------------------------------------------------
# Operators
# --------------------------------------------------------------------------
def normalized_adjacency(W, *, add_self_loops: bool = True) -> csr_matrix:
    """
    D^-1/2 (W + I) D^-1/2 -- the GCN propagation operator (Kipf & Welling 2017).

    Self-loops keep a node's own signal in its update and shift the spectrum into
    roughly [-1, 1], which is what stops repeated application from exploding.
    """
    A = _sparse(W).astype(float)
    if add_self_loops:
        A = A + identity(A.shape[0], format="csr")
    deg = np.asarray(A.sum(axis=1)).ravel()
    deg[deg == 0] = 1.0
    d = diags(1.0 / np.sqrt(deg))
    return (d @ A @ d).tocsr()


def graph_laplacian(W, *, normalized: bool = True) -> csr_matrix:
    """L = D - W, or the symmetric normalised I - D^-1/2 W D^-1/2 with spectrum in [0, 2]."""
    A = _sparse(W).astype(float)
    deg = np.asarray(A.sum(axis=1)).ravel()
    if not normalized:
        return (diags(deg) - A).tocsr()
    d = deg.copy()
    d[d == 0] = 1.0
    dm = diags(1.0 / np.sqrt(d))
    return (identity(A.shape[0], format="csr") - dm @ A @ dm).tocsr()


def scale_laplacian(L, lmax: float | None = None) -> csr_matrix:
    """Rescale L to [-1, 1] as 2L/lmax - I, the domain Chebyshev polynomials need."""
    from scipy.sparse.linalg import eigsh
    if lmax is None:
        try:
            lmax = float(eigsh(L, k=1, which="LM", return_eigenvectors=False)[0])
        except Exception:
            lmax = 2.0
    return (2.0 / lmax * L - identity(L.shape[0], format="csr")).tocsr()


# --------------------------------------------------------------------------
# Chebyshev filtering
# --------------------------------------------------------------------------
def chebyshev_basis(L_scaled, x: np.ndarray, K: int) -> np.ndarray:
    """
    Chebyshev basis {T_0(L)x, ..., T_K(L)x} via the three-term recurrence
    T_k = 2 L T_{k-1} - T_{k-2}.

    Returns (n, K+1). Each column is exactly k hops of localisation, which is what
    makes this the standard way to get localised spectral filters without ever
    forming an eigendecomposition.
    """
    x = np.asarray(x, float).ravel()
    out = np.empty((len(x), K + 1))
    out[:, 0] = x
    if K >= 1:
        out[:, 1] = L_scaled @ x
    for k in range(2, K + 1):
        out[:, k] = 2.0 * (L_scaled @ out[:, k - 1]) - out[:, k - 2]
    return out


def chebyshev_filter(W, x: np.ndarray, coeffs: np.ndarray, *, lmax: float | None = None) -> np.ndarray:
    """Apply a spectral filter sum_k theta_k T_k(L_scaled) to a signal."""
    L = scale_laplacian(graph_laplacian(W, normalized=True), lmax)
    B = chebyshev_basis(L, x, len(coeffs) - 1)
    return B @ np.asarray(coeffs, float)


def chebyshev_trace_coefficients(W, degrees, *, n_probe: int = 64, seed: int = 42) -> np.ndarray:
    """
    Stochastic estimate of (1/n) tr T_k(L_scaled) by Hutchinson probing.

    The deterministic analogue of the thesis's mu(n) = (1/N) tr U_n(H), computed without
    an eigendecomposition so it scales to graphs where dense eigensolvers will not run.
    Uses first-kind T_k here; spatialrmt.spectral.chebyshev_coefficients gives the exact
    second-kind version for small matrices.
    """
    L = scale_laplacian(graph_laplacian(W, normalized=True))
    n = L.shape[0]
    rng = np.random.default_rng(seed)
    degrees = np.atleast_1d(np.asarray(degrees, int))
    dmax = int(degrees.max())

    acc = np.zeros(dmax + 1)
    for _ in range(n_probe):
        v = rng.choice([-1.0, 1.0], size=n)
        B = chebyshev_basis(L, v, dmax)
        acc += (v @ B) / n
    return (acc / n_probe)[degrees]


# --------------------------------------------------------------------------
# Oversmoothing
# --------------------------------------------------------------------------
def oversmoothing_curve(W, x: np.ndarray, max_steps: int = 32, *,
                        add_self_loops: bool = True) -> dict:
    """
    Repeatedly apply the GCN propagation operator and watch feature diversity collapse.

    Reports Dirichlet energy x'Lx (how much the signal varies across edges) and the
    coefficient of variation, both normalised to their starting values. Both decaying
    to zero is oversmoothing: every node ends up with the same representation.

    The decay rate is set by the spectral gap -- see `mixing_diagnostics`. Reading it
    as a mixing time is the bridge to the Thouless comparison: once the walk implied by
    the propagation depth has mixed, the graph's geometry is no longer visible in the
    representations.
    """
    A = normalized_adjacency(W, add_self_loops=add_self_loops)
    L = graph_laplacian(W, normalized=True)
    h = np.asarray(x, float).ravel().copy()

    e0 = float(h @ (L @ h))
    steps, energy, cv = [0], [1.0], [1.0]
    cv0 = float(h.std() / abs(h.mean())) if h.mean() != 0 else float(h.std())

    for s in range(1, max_steps + 1):
        h = A @ h
        e = float(h @ (L @ h))
        c = float(h.std() / abs(h.mean())) if h.mean() != 0 else float(h.std())
        steps.append(s)
        energy.append(e / e0 if e0 > 0 else np.nan)
        cv.append(c / cv0 if cv0 > 0 else np.nan)

    energy = np.array(energy)
    half = next((s for s, v in zip(steps, energy) if v < 0.5), None)
    return {
        "steps": np.array(steps),
        "dirichlet_energy": energy,
        "coefficient_of_variation": np.array(cv),
        "half_energy_step": half,
        "final_energy_fraction": float(energy[-1]),
    }


def mixing_diagnostics(W) -> dict:
    """
    Spectral gap of the propagation operator and the mixing time it implies.

    `mixing_time` here is 1/gap, the number of propagation steps for the walk to
    approach its stationary distribution. Compare it against the depth of a GNN, or
    against the walk length an edge statistic needs: if mixing is faster, geometry has
    already been washed out by the time the statistic is computed.
    """
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse.linalg import eigsh

    A = normalized_adjacency(W)
    n = A.shape[0]

    # Connectivity first. A disconnected graph has eigenvalue 1 with multiplicity equal
    # to the number of components, so the naive top-two gap is 0 and the implied mixing
    # time is infinite -- correctly, since a walk never leaves its own component. Report
    # the gap *within* the largest component instead, which is the meaningful quantity.
    n_comp, labels = connected_components(_sparse(W), directed=False)
    sizes = np.bincount(labels)
    largest = int(np.argmax(sizes))
    idx = np.flatnonzero(labels == largest)

    def _top(M, k):
        k = min(k, M.shape[0] - 1)
        if k < 1:
            return np.array([1.0])
        try:
            return np.sort(eigsh(M, k=k, which="LM", return_eigenvectors=False))[::-1]
        except Exception:
            return np.sort(np.linalg.eigvalsh(M.toarray()))[::-1][:k]

    ev_all = _top(A, 6)
    A_lc = normalized_adjacency(_sparse(W)[np.ix_(idx, idx)])
    ev_lc = _top(A_lc, 6)
    gap = float(ev_lc[0] - ev_lc[1]) if len(ev_lc) > 1 else np.nan

    return {
        "n": int(n),
        "n_components": int(n_comp),
        "largest_component": int(sizes[largest]),
        "isolated_or_small": int(n - sizes[largest]),
        "top_eigenvalues": ev_all.tolist(),
        "spectral_gap": gap,
        "mixing_time": float(1.0 / gap) if gap and gap > 0 else float("inf"),
        "note": (
            f"graph has {n_comp} components; gap and mixing time are computed within the "
            f"largest ({sizes[largest]} of {n} nodes). A walk cannot leave its component, "
            "so whole-graph mixing is undefined."
            if n_comp > 1 else "graph is connected"
        ),
    }
