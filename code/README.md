# code

`spatialrmt` — spatial weights matrices treated as structured random matrices.

Import from a script in this repo with:

```python
import sys; sys.path.insert(0, str(ROOT / "code"))
from spatialrmt import weights, spectral, bandmatrix
```

## Modules

### `geodesy`
`to_unit_sphere`, `haversine_km`, `pairwise_haversine_km`, `chord_to_arc_km`.
The unit-sphere embedding matters: chordal distance is monotone in great-circle
distance, which is what makes a kd-tree a valid kNN search on the sphere.

### `weights`
`knn_weights`, `distance_band_weights`, `apply_transform`, `weights_summary`, `describe`.

Both constructors require `symmetrize` and `transform` as visible arguments rather than
defaults. That is a deliberate response to what happened in the eip submission, where
the published hot/cold map depended on two choices its methods document never stated.
`describe(W)` returns a one-line specification meant to be printed next to any statistic
computed from it.

Transforms: `binary`, `row`, `variance` (D^-1/2 W D^-1/2, spectrum in [-1,1]), `doubly`
(Sinkhorn, preserves symmetry).

### `spectral`
`spectrum`, `spectral_moments`, `chebyshev_coefficients`, `inverse_participation_ratio`,
`participation_number`, `resolvent`, `car_admissible_rho`, `stieltjes_transform`.

`spectrum(W, centered=True)` applies `M W M` with `M = I - 11'/n` — what Moran's I does
implicitly, and the step that removes the Perron eigenvalue of a non-negative weights
matrix, making mean-zero random matrix theory applicable.

`chebyshev_coefficients` computes `(1/N) tr U_n(W)` with second-kind Chebyshev
polynomials, which count non-backtracking walks rather than the backtracking clutter
dominating ordinary moments — the object that carries edge information.

`car_admissible_rho` returns the interval where `I - rho W` stays positive definite,
which is the CAR/SAR parameter range and a direct consequence of `Q^-1` being the
resolvent of `W` at `z = 1/rho`.

### `bandmatrix`
`periodic_band_matrix` (beta = 1 or 2), `band_adjacency`, `thouless_threshold`,
`classify_regime`, `mixing_time`, `edge_resolution_length`, `semicircle_density`,
`tracy_widom_edge_scale`, `subcritical_edge_scale`.

`thouless_threshold(n, d)` returns critical radius `n^(1/d - 1/6)` and degree
`n^(1 - d/6)`. At `d = 1` it returns `n^(5/6)`, recovering Sodin's threshold — the
consistency check that the d-dimensional extension is at least self-consistent. The
d > 1 exponents are the Thouless heuristic transplanted, not a theorem.

## Verified behaviour

`analysis/02_band_matrix_edge.py` recovers eigenvector occupancy `1/IPR → N/3` in the
full-matrix limit, which is the GOE value — an independent check that the ensemble
generation and localisation measures are correct.
