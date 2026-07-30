# tools

Methods generalised away from either dataset. The submissions keep frozen copies — those
must keep reproducing published numbers, so nothing here is imported by `../eip` or
`../fisher`.

```python
import sys; sys.path.insert(0, str(ROOT))
from tools.autocorrelation import global_morans_i, getis_ord_gi_star
from tools.geostatistics import empirical_variogram, fit_variogram, ordinary_kriging
from tools.crossval import leakage_report
```

---

## The landscape

Geospatial ML has three layers that are often confused. Sorting them out is most of the
battle when choosing a method.

### 1. Classical geostatistics — *model the covariance*

**Variogram + kriging** (Matheron, 1960s). Estimate how covariance decays with distance,
then predict by BLUP. Still the reference method, and the only common approach that
reports honest predictive *variance* — it grows away from data, which ML predictors
generally do not tell you.

Implemented: `geostatistics` — empirical variogram, four model families
(exponential, gaussian, spherical, Matérn), Cressie-weighted fitting, ordinary kriging.

Why it still matters here: kriging is kernel ridge regression with a covariance kernel,
so its behaviour is a statement about that kernel matrix's spectrum. The nugget is
ridge regularisation; sending it to zero is the interpolation limit where
benign-overfitting theory lives — and spatial designs violate the i.i.d. assumptions
that theory is proved under. `kernel_spectrum_diagnostics` is the entry point.

### 2. Spatial statistics / econometrics — *model the dependence*

**Autocorrelation tests** — Moran's I, Geary's C, Getis-Ord Gi\*, LISA. Diagnostic, not
predictive. `autocorrelation`.

**Lag and error models** — SAR, SEM, CAR, SARAR. One dependence parameter added to a
regression. `regression.sar_lag`, `sem_error`, `lm_tests`.

The distinction matters and is routinely botched: in **SAR** the lag term feeds back, so
β is no longer a marginal effect; in **SEM** dependence sits in the disturbance and β
keeps its usual meaning. `lm_tests` picks between them on OLS residuals rather than by
assertion.

**GWR** — let coefficients vary in space instead of adding a dependence parameter.
`regression.gwr`. Bandwidth is the whole ballgame; local *t*-statistics on GWR surfaces
are badly overconfident because each observation feeds many local fits. Exploratory only.

**Eigenvector spatial filtering (MEM/ESF)** — use eigenvectors of `MWM` as synthetic
predictors. `eigenvector_filtering`. Two problems the literature underplays, both
instrumented here: selection is on the response, so downstream *p*-values are selective;
and whether those eigenvectors are *global patterns at all* depends on the weights
matrix (`localisation_report`).

### 3. Machine learning on spatial data — *model the function*

**Where most spatial ML goes wrong is not the model, it is the validation.**
Random *k*-fold CV assumes held-out points are independent of training points. Under
autocorrelation they are not — a held-out point almost always has a near neighbour in
training, so the model interpolates and the score measures autocorrelation, not skill.
`crossval` implements block, buffered-LOO, and spatial *k*-means splitters plus
`leakage_report` to measure the gap. (Roberts et al. 2017; Ploton et al. 2020.)

**Gaussian processes** — kriging under a different name, with hyperparameters learned by
marginal likelihood. The eip pipeline uses sklearn's; `geostatistics` gives the
variogram view of the same object.

**Graph neural networks** — `graph_signal`. This is where the ML side meets the theory
directly. ChebNet (Defferrard et al. 2016) builds filters as Chebyshev polynomials of a
scaled graph Laplacian to get *K*-hop-localised filters without an eigendecomposition.
A *K*-th order filter has a *K*-hop receptive field, so whether it sees global geometry
or only local structure is a race between mixing time and filter depth — the Thouless
comparison. **Oversmoothing is what happens once the walk has mixed.**
`oversmoothing_curve` and `mixing_diagnostics` measure both sides.

**Tree ensembles with coordinate features** — common, cheap, and the biggest CV-leakage
offender, because trees can memorise location outright. Not implemented; use sklearn
with `crossval`'s splitters.

---

## What is implemented

| Module | Contents |
|---|---|
| `autocorrelation` | Global Moran's I, LISA, Getis-Ord Gi\*, hotspot classification |
| `matrix_correlation` | Mantel, partial Mantel, `spectral_overlap` |
| `geostatistics` | Variograms (4 families), fitting, ordinary kriging, kernel spectrum |
| `crossval` | Block / buffered-LOO / spatial *k*-means splitters, `leakage_report` |
| `regression` | SAR, SEM, LM tests, GWR + bandwidth selection, spatial-confounding diagnostic |
| `eigenvector_filtering` | MEM basis, selection, ESF regression, `localisation_report` |
| `graph_signal` | GCN/Laplacian operators, Chebyshev filters and trace coefficients, oversmoothing, mixing |

## Deliberately not implemented

- **Point-pattern statistics** (Ripley's K/L, *G*/*F* functions) — would be the natural
  next addition; relevant because the random-geometric-graph model underlying the theory
  assumes a point process whose properties these measure.
- **Spatial interpolation baselines** (IDW, natural neighbour) — trivial, and kriging
  dominates them wherever a variogram can be fitted.
- **Deep spatial models** (ConvLSTM, spatiotemporal transformers) — out of scope until
  there is a temporal dimension in either dataset.
- **Areal/lattice methods** (spatial scan statistics, BYM models) — both projects are
  point-referenced, not areal.

## Caveats that travel with these methods

Three that the docstrings state and that are easy to lose:

1. **Permutation nulls assume exchangeability**, which breaks when the weights matrix is
   tuned on the same data — the case whenever `k` or a bandwidth is selected.
2. **Gi\* p-values are uncorrected.** On 319 units at α = 0.05, expect ~16 false
   positives before adjustment — comparable to the count of genuine classifications in
   the eip result.
3. **Mantel and partial Mantel have documented Type I inflation** under spatial
   autocorrelation, which is the only setting they are used in (Guillot & Rousset 2013;
   Legendre et al. 2015). Prefer effect size across codings.

## Still to promote from the submissions

Bridge-index bootstrap and top-3 permutation harnesses (`../fisher/analysis/`), and the
LISA robustness sweep (`step3b_lisa_robustness.py`).
