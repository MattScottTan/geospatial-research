# tools

Methods and ML techniques — the reusable machinery, kept separate from any one dataset.

The distinction from [`../code`](../code) is intent rather than language: `code/` is
project plumbing, `tools/` is a technique someone could lift and apply elsewhere.

Empty at present. Candidates already implemented inside the submissions and worth
promoting here once they need to be shared:

| Technique | Currently at |
|---|---|
| Global Moran's I / Getis-Ord Gi\*, multiple weighting schemes | `../eip/analysis/spatial_diagnostics_esda.py` |
| Mantel and partial Mantel with permutation inference | `../fisher/analysis/step2_mantel.py` |
| LISA and robustness panel | `../fisher/analysis/step3_lisa.py`, `step3b_lisa_robustness.py` |
| Bootstrap and permutation harnesses | `../fisher/analysis/bridge_bootstrap.py`, `top3_permutation.py` |

Promote by generalising away the dataset, not by copying the file — the submission copies
must keep reproducing their published numbers exactly.
