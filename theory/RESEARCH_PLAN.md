# Research programme: the statistical consequences of weights-matrix specification

## The thesis of the programme

Every statistic in spatial analysis conditions on a weights matrix `W`. **`W` is not data.**
It is a modelling choice with at least five free parameters — neighbour rule (kNN vs
distance band vs contiguity), `k` or bandwidth, symmetrization, normalisation, and
distance metric — made by the analyst, usually by convention, and then treated as fixed
and known for the rest of the analysis.

The field manages this with informal robustness checks. There is no theory for:

| Question | Paper |
|---|---|
| What if the choice fragments the study area into disconnected pieces? | 1 |
| What do the objects derived from `W` actually mean at conventional settings? | 2 |
| Is inference still valid when the choice was tuned on the data? | 3 |
| When do the asymptotics everyone relies on apply at all? | 4 |

Four papers, one identity. Each ships a diagnostic or a correction, not only a critique.

---

## Paper 1 — Component structure and local spatial statistics

**Status: verified on real data. Start here.**

### Question
What happens to Getis-Ord Gi\* when the weights graph splits into disconnected components?

### Motivation
kNN weights at conventional `k` silently disconnect. On the 319-city AI dataset:
`k = 4` → 3 components, `k = 8` → 2, `k = 20` → still 2. It does not resolve by
increasing `k` into the normal range, and no standard tool reports it.

Gi\* standardises each unit's neighbourhood sum against the **global** mean and standard
deviation. When neighbourhoods are confined within components whose means differ, every
unit in a below-average component is systematically pushed toward "cold spot" — graded on
a curve calibrated on a population it is not part of.

Measured on the published k = 8 graph:

| component | n | cold spots | rate | hot spots |
|---|---|---|---|---|
| large | 252 | 19 | 7.5% | 7 |
| small | 67 | **14** | **20.9%** | **0** |

Uniform allocation would give ~7 cold spots in the small component; it has 14.

### Existing literature
- **Smith (2009), *Geographical Analysis*** — "Estimation Bias in Spatial Models with
  Strongly Connected Weight Matrices." Studies the *opposite* pathology: over-connected
  `W` biases the dependence parameter downward. Establishes that connectivity structure
  has inferential consequences — the precedent this paper extends to the fragmented end.
- **Islands** (units with zero neighbours) are handled in software: `spdep` warns, ArcGIS
  drops them. Multi-unit disconnected *components* are flagged by nothing.
- No work found on component structure and Gi\*/LISA.

### Contribution
1. Identify and quantify the component-level standardisation artifact in Gi\*.
2. **Component-aware Gi\***: standardise against within-component moments. One-line fix.
3. Prevalence study: how often does silent disconnection occur across real datasets and
   conventional `k`?
4. **A negative result worth reporting.** Global Moran's I is essentially unaffected —
   free vs within-component permutation gives p = 0.0085 vs 0.0080, identical null SD.
   Between-component variance here is only 0.8% of total. Telling practitioners where
   *not* to worry is half the value.

### Method and prerequisites
Block-diagonal decomposition of `z'Wz` (no cross terms when `W` is block-diagonal);
stratified permutation; empirical sweep over `k` and datasets.
**No random matrix theory.** Deliberately — this is the warm-up.

### Deliverable and venue
Short methods paper plus a diagnostic already implemented in `tools/`.
*Geographical Analysis*, *Spatial Statistics*, or a software-adjacent venue.

### Risk: **low**
Verified on one dataset. Main residual risk is prior discussion in grey literature or
software issue trackers, which a targeted search should settle.

### Timeline: 3–6 weeks

---

## Paper 2 — What Moran eigenvector maps actually are

**Gate resolved (Aug 2026): the theorem is largely gone; the applied paper survives and
sharpens.** See "Gate outcome" below. Reframed from "find the localisation threshold" to
"MEM's centering deletes the one extended mode, so ESF has no safe regime."

### Question
When are Moran eigenvectors global spatial trends, and when are they local bumps?

### Motivation
MEM / eigenvector spatial filtering is heavily used — `adespatial` and `spatialRF` in R,
a dedicated ArcGIS tool, thousands of applications across ecology, spatial econometrics
and epidemiology.

The field holds an explicit belief, stated in the
[adespatial tutorial](https://cran.r-project.org/web/packages/adespatial/vignettes/tutorial.html)
and [ArcGIS documentation](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/spatial-statistics/understanding-moran-eigenvectors.htm):
*leading eigenvectors are broad global patterns, later ones are localised.* Selection
targets the leading ones for exactly that reason.

**That belief fails at conventional settings.** Measured: at `k = 8`, `n = 319`, the
*leading* 20 eigenvectors occupy 13.8% of the domain (range 6.4%–24.7%). The band-matrix
simulation at the analogous bandwidth gives 7.7% occupancy, saturating at the GOE value
of `N/3` only in the full-matrix limit.

If the filters are localised, ESF is absorbing local structure and reporting it as a
spatial trend. The coefficient shift it produces (−0.0567 → −0.0451 in the AI data) is
then being interpreted as "controlling for spatial autocorrelation" when it is
controlling for something else.

### Existing literature
- **MEM/ESF methodology** — Griffith; Dray, Legendre & Peres-Neto; Borcard & Legendre.
  Descriptive and constructive; no spectral theory of what the eigenvectors are. Griffith
  (2017) assesses estimator robustness, not eigenvector structure. Recent work replaces
  ad-hoc selection with regularisation, but still never asks what the selected vectors are.
- **Eigenvector localisation on random geometric graphs** — **occupied, and recently.**
  [Localized and delocalized modes on RGGs in 1D](https://arxiv.org/pdf/2508.18936)
  (Phys. Rev. E, 2025) and [the 2D counterpart](https://arxiv.org/html/2603.29611) (2026).
  Both numerical.
- **Band matrix delocalisation** — Sodin; Bourgade, Erdős, Yau, Yin. The thesis.
- No connection between the applied and spectral literatures — this remains open.

### Gate outcome (searched Aug 2026)

The 2026 2D paper establishes numerically that **all adjacency eigenmodes localise for
sufficiently large systems**, while the **Laplacian retains system-spanning modes because
of a conservation law** — the uniform vector in its kernel. It also finds a percolation
threshold at mean degree ≈ 4.5 and notes that component size distribution shapes the
density of states.

So the ensemble-level spectral fact is done, in both dimensions, numerically. **The
threshold theorem is not available as originally conceived.** Three things survive:

1. **MEM does not use the adjacency or the Laplacian.** It uses `MWM` with
   `M = I − 11'/n`, which *explicitly deletes the constant vector* — precisely the
   conservation mode that keeps the Laplacian extended. By the 2026 paper's own logic,
   the MEM basis is the adjacency-like object with its one extended mode removed by
   construction. **Prediction: MEM eigenvectors localise, always, asymptotically.** That
   is sharper and more damaging to ESF than any threshold, and it is untested.
2. **Construction mismatch.** The physics uses distance-band RGGs; MEM in practice uses
   kNN, which has fixed degree and is asymmetric before symmetrisation.
3. **The entire applied translation is untouched.** Nobody in the MESF literature measures
   participation ratios or questions the global→local ordering.

### Contribution (revised)
1. Test the centering prediction: does `MWM` localise where the Laplacian does not?
2. Show the field's stated "leading = global" ordering fails at conventional settings —
   measured 13.8% occupancy for the leading 20 at `k = 8`, `n = 319`.
3. A computable diagnostic — participation ratio — reported alongside any ESF result.
4. Consequence for inference: what an ESF coefficient means when the filters are local.

### Method and prerequisites
`MWM` spectra on kNN and distance-band graphs; inverse participation ratio; simulation
across `(n, k, d)`; reanalysis of published applications. The thesis supplies intuition
rather than the proof engine now.

### Deliverable and venue
Applied methods paper. *Geographical Analysis*, *Spatial Statistics*, *IJGIS* — venues
where the physics literature is unknown and the consequence matters.

### Risk: **low-medium** (downgraded ceiling, downgraded risk)
No longer a theorem paper. The contribution is translation plus a specific untested
prediction plus applied consequence. Publishable and useful; not a flagship.

### Timeline: 4–6 months

---

## Paper 3 — Selective inference for weights-matrix selection

### Question
What is a valid p-value for Moran's I when `k` or the bandwidth was chosen by looking at
the data?

### Motivation
The field openly describes ad-hoc selection procedures that **maximise Moran's I**, and
there is a whole comparison literature on choosing "the most adequate weighting matrix."
No correction is ever applied — the reported permutation p-value treats `W` as fixed.

Measured: Moran's I over `k` ∈ {4, 6, 8, 12, 20, 40} is
{0.0545, 0.0574, **0.0685**, 0.0373, 0.0195, 0.0053}. The published `k = 8` is the
arg-max. That is very likely coincidence — `k = 8` is a standard default — but the
sensitivity is large enough that selection matters whenever anyone does look.

### Existing literature
- **Post-selection inference** — Lee, Sun, Sun & Taylor (2016); Fithian, Sun & Taylor
  (2014). The general machinery exists and is mature.
- **Weights selection** — treated as a model-choice problem (AIC-style criteria), never
  as an inference-validity problem.
- Nothing connecting the two.

### Contribution
1. Formalise `W`-selection as a selection event; derive the truncated null for Moran's I
   conditional on `{k̂ = k}`.
2. Quantify the inflation under realistic selection rules.
3. A valid procedure — conditional inference, or data splitting where conditioning is
   intractable.

### Method and prerequisites
Truncated distributions; the exact null of a ratio of quadratic forms via Imhof or
saddlepoint methods on the eigenvalues of `MW_sM`. Selection over a finite grid of `k` is
a finite union of events, which keeps the conditioning tractable.

### Deliverable and venue
Method plus software. *JASA*, *Biometrika*, *JRSS-B*.

### Risk: **medium**
Tractable, but the value depends on how often practitioners actually tune `k` — worth
establishing empirically as part of the paper rather than assuming.

### Timeline: 6–12 months

---

## Paper 4 — When do spatial asymptotics apply? *(optional, ambitious)*

### Question
Is there a bandwidth threshold below which the asymptotic theory underpinning spatial
inference does not hold?

### Motivation
The Thouless criterion transplanted to `d` dimensions predicts a critical degree
`~ n^(1 - d/6)`. At `d = 2`, `n = 319`, that is ~47 — while conventional `k` is 8.
Measured on the real graph: mixing time within the largest component is 424 steps against
`n^(1/3) ≈ 6.8` to resolve the spectral edge — a ratio of **62×**. The walk is nowhere
near mixed when the edge is resolved, so geometry survives into the edge statistics and
mean-field asymptotics do not apply.

### Existing literature
- **Sodin (2010)** — the 1D band matrix edge threshold `W ~ N^(5/6)`, covered in the thesis.
- **d-dimensional band matrices** — partial results only. The 1D proof's Fourier
  diagonalisation of the band walk does not extend. Genuinely open and hard.
- **Spatial asymptotics** — increasing-domain vs infill frameworks (Cressie; Lahiri) exist
  but do not ask this question.

### Contribution
Establish or numerically characterise the `d = 2` threshold, and identify which spatial
statistics are affected on which side of it.

### Risk: **high**
A hard open problem in RMT. Plausibly a chapter that never closes.

### Timeline: 18+ months, or never

---

## Sequencing (revised after the Paper 2 gate)

```
now         Paper 1 ──────────────► finished artefact, tooling, habit
            │
month 2     Paper 3 ──────────────► FLAGSHIP. Reuses Paper 1's permutation machinery.
            │                       Now the best theorem-shaped candidate: post-selection
            │                       inference for W is a statistics problem, unoccupied,
            │                       and not something physics will scoop.
            │
month 4     Paper 2 ──────────────► applied methods paper, runs alongside
                                    │
opportunistic                       └─ Paper 4, only if tractable
```

**The gate moved the centre of gravity.** Paper 2 was the flagship on the assumption it
carried a theorem; it does not. Paper 3 inherits that role — selective inference for
weights selection is squarely a statistics problem, the machinery to specialise exists,
and no adjacent field is working toward it.

Paper 1 still goes first because it finishes and builds the apparatus Paper 3 needs.

---

## What the programme gives the field

1. **A vocabulary.** "Weights specification" is currently a footnote in methods sections.
   This makes it a first-class object with named failure modes.
2. **Computable diagnostics** — component structure, participation ratio, regime
   classification — reportable alongside any spatial statistic, all already implemented
   in `tools/` and `code/spatialrmt/`.
3. **Corrections where needed** — component-aware Gi\*, selective p-values — and, equally
   useful, *demonstrations that no correction is needed* where the statistic turns out to
   be robust.
4. **A principled answer to "which W should I use?"**, currently answered by convention.

## Honest risks to the programme

- **Paper 2's underlying theory existed.** Checked Aug 2026: 1D (Phys. Rev. E 2025) and
  2D (arXiv 2603.29611, 2026) RGG localisation are both done numerically. Paper 2 was
  downgraded from flagship to applied methods paper, and Paper 3 promoted. This is what
  the gate was for; the cost of not checking would have been months.
- **Paper 1 may be known** in grey literature or software discussions.
- **Paper 4 may be too hard.** Treat as optional throughout.
- **The programme is critical in character** — "here is what is wrong with what you do."
  Reviewers in applied fields respond poorly to critique without remedy. Every paper must
  ship a fix or a diagnostic, not only a finding. This is why each entry above lists a
  deliverable artifact.
- **Two datasets is a thin empirical base** (n = 319 and n = 20), and neither is large
  enough to exhibit asymptotic behaviour. Papers 1 and 2 both need a wider set of real
  weights matrices — the 8,000-city frame in `../eip/data/raw/worldcities.csv` is the
  obvious first extension.
