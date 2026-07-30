# tools

Methods generalised away from either dataset. The submissions keep their own frozen
copies — those must keep reproducing published numbers exactly, so nothing here is
imported by `../eip` or `../fisher`.

```python
import sys; sys.path.insert(0, str(ROOT))
from tools.autocorrelation import global_morans_i, getis_ord_gi_star
from tools.matrix_correlation import mantel, partial_mantel
```

## `autocorrelation`

| Function | Notes |
|---|---|
| `global_morans_i` | Permutation null, returns a `MoranResult` carrying I, E[I], z, p, and the permutation mean/sd |
| `local_morans_i` | LISA with conditional permutation; returns local I, p_sim, and HH/HL/LH/LL quadrants |
| `getis_ord_gi_star` | Analytic normal null; `include_self` toggles Gi* vs Gi |
| `classify_hotspots`, `hotspot_counts` | 95/99% binning and totals |

Two things the docstrings flag that are easy to forget. The permutation null assumes
exchangeability, which is exactly what breaks when the weights matrix is estimated from
the same data — the case whenever `k` or a bandwidth is tuned. And Gi\* p-values are
uncorrected: on 319 units at alpha = 0.05 you expect ~16 false positives before any
adjustment, which is comparable to the number of genuine classifications in the eip
result.

## `matrix_correlation`

| Function | Notes |
|---|---|
| `mantel` | Joint row/column permutation, the only defensible null for dependent dissimilarities |
| `partial_mantel` | Residualises both matrices on controls, recomputing residualisation inside the permutation loop |
| `spectral_overlap` | Leading-eigenvector alignment and effective rank of two dissimilarity matrices |

`spectral_overlap` exists because Mantel r is `tr(AB)/sqrt(tr A² tr B²)` — a degree-2
spectral functional whose null depends on the joint spectra. Two matrices with nearly
coincident leading eigenvectors produce a large r across a huge range of arrangements,
and the permutation null understates that. Reporting the alignment alongside r makes the
dependence visible.

Both Mantel variants carry the documented Type I inflation caveat under spatial
autocorrelation (Guillot & Rousset 2013; Legendre et al. 2015) — which is the only
setting anyone uses them in. Prefer effect size across several codings, as the fisher
submission's sensitivity panel does.

## Still to promote

Not yet generalised, still only in the submissions: the bridge-index bootstrap and
top-3 permutation harnesses (`../fisher/analysis/`), and the LISA robustness sweep
(`step3b_lisa_robustness.py`).
