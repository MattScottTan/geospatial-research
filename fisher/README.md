# fisher — culinary corridors

Ingredient similarity vs. great-circle distance across 20 cuisines (190 pairs).
Published as the StoryMap "Salt, Fat, Acid, Distance" (May 2026).

## Why there are three versions

This project was assembled from three separately-downloaded packages, none of which is
marked as superseding the others. All are kept under `submission/versions/` rather than picking one,
because the relationship between them can be inferred but not confirmed.

| Directory | Contains | Apparent role |
|---|---|---|
| `versions/fisher-submission/` | `code/` — `figdata.py` + `build_fig01/03/05/06.py` (cartopy) | The figure-building code |
| `versions/storymap-v3-balanced/` | 18 StoryMap section copy blocks, readability and claim-safety audits, `WORK*.md` | The prose and QA layer |
| `versions/storymap-v5/` | v5 build instructions + `v4_01`–`v4_06` rendered PNGs | Newest instructions and the rendered figure set |

Best reading of the lineage: `fisher-submission/code/` generated the `v4_*.png` files now
sitting in `versions/storymap-v5/figures/`, and `storymap-v3-balanced` carries the text
that wrapped them. The version numbers disagree across packages (fisher code with no
number, storymap v3, figures v4, instructions v5), so treat that as a hypothesis.

`reports/` holds three report PDFs — `complete_final`, `committee`, `winner_aligned` —
also with no version markers and no stated precedence.

## Data

`data/raw/cuisine_ingredient_matrix.csv` is the only input dataset, and it was found
loose in `Downloads` with no README, citation, or licence. Its provenance is unresolved;
see [`../docs/DATA_PROVENANCE.md`](../docs/DATA_PROVENANCE.md).

## The analysis

`analysis/` holds the full statistical pipeline, recovered from the Fisher archives:
baseline verification, filter sweep, residual validation, Mantel and partial Mantel,
LISA and its robustness panel, case studies, and five extension analyses. `code/figure-builders/` holds
the figure builders. Working matrices and result JSONs are in `analysis/working_data/`.

It uses `esda` and `libpysal` with `seed = 42` and 9,999 permutations, and every statistic
published in the StoryMap reproduces from the shipped results — see the claim-by-claim
table in [`submission/award-materials/README.md`](submission/award-materials/README.md).

`submission/versions/fisher-submission/code/figdata.py` is a superseded early build helper that
hardcodes coordinates transcribed off earlier figures; use `analysis/` instead.
