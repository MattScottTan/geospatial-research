# analysis

Research analyses — experiments, simulations, notebooks. One directory or script per
question.

Distinct from `../eip/analysis/` and `../fisher/analysis/`, which are frozen to what the
prize submissions actually ran. Reproducing a submission's numbers is their job; asking
new questions is this directory's.

Empty at present. The first natural entry is the weights-sensitivity experiment sketched
in [`../theory/README.md`](../theory/README.md) — hold the data fixed, vary the weights
specification, and watch the global statistic hold while local classifications collapse.
`../eip/analysis/spatial_diagnostics_esda.py` already does this for one dataset and is
the obvious starting point.
