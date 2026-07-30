# analysis

Research experiments. Distinct from `../eip/analysis/` and `../fisher/analysis/`, which
are frozen to what the submissions actually ran.

`data/` holds 40 KB of extracts from both submissions so experiments have a stable input
that does not move if a submission is revised. `outputs/` is gitignored.

## 01 — Weights sensitivity

```bash
python analysis/01_weights_sensitivity.py
```

Sweeps k ∈ {4, 6, 8, 12, 20, 40} against all four symmetry × transform combinations on
the 319 AI-linked cities, holding the data fixed.

The decomposition matters and the script does it explicitly: varying **k** changes the
estimand (a wider neighbourhood genuinely averages over more distant units, so I is
*expected* to decay), while varying symmetry/transform at fixed k does not change the
question and so any movement there is specification artifact.

**Result.** At fixed k, median relative spread is **21% for Moran's I and 64% for the
Gi\* flagged count**. At k = 8 specifically it is 8.6% vs 68%. The global statistic is
roughly stable under specification; the local classifications are not — consistent with
the prediction that a degree-2 spectral functional sits in the geometry-blind part of
the spectrum while extreme-value classifications do not.

**Incidental finding worth attention.** Moran's I over the k sweep is
0.0545, 0.0574, **0.0685**, 0.0373, 0.0195, 0.0053 for k = 4…40. The published k = 8 is
the arg-max. If k was chosen by looking at I, the reported p = 0.008 is a selective
p-value and the permutation null does not account for the selection. I have no evidence
the choice was made that way — k = 8 is also a common default, and the methods document
presents it as one — but the coincidence is the exact scenario that motivates the
selective-inference thread in `../theory`.

**Regime.** All tested k are subcritical for edge universality in d = 2 (critical degree
at n = 319 is ~47; k = 8 gives ratio 0.17).

## 02 — Band matrix: bulk vs eigenvectors

```bash
python analysis/02_band_matrix_edge.py
```

Periodic random band matrices at N = 512, bandwidths 2…255, 8 realisations each.
Measures L1 distance from the semicircle law against eigenvector occupancy (1/IPR).

**Result.** Over W ≥ 8 the semicircle error moves by 1.9× while eigenvector occupancy
moves by 4.4×. The bulk density is essentially converged by W = 8 and barely improves
after; occupancy climbs across the whole range. At W = 8 — the analogue of the k = 8
both submissions use — the spectral density is close to semicircle but eigenvectors
occupy only **7.7%** of the domain.

That is the concrete form of the ESF concern: a Moran eigenvector at this bandwidth is a
local bump, not a global spatial trend, so eigenvector spatial filtering at typical
weights settings is fitting local structure and labelling it a trend.

**Implementation check.** Occupancy saturates at 1/IPR → N/3 in the full-matrix limit,
the GOE value, confirming the ensemble generation and localisation measures are correct.

## Next

The obvious third experiment is the one neither of these does: vary n as well as k, and
test whether the d = 2 threshold exponent `n^(1 - d/6)` actually predicts where the Gi\*
classifications stabilise. Both datasets here are too small to see an asymptotic regime
(n = 319 and n = 20), so this needs either synthetic point processes or the full
8,000-city frame in `../eip/data/raw/worldcities.csv`.
