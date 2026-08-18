# SPEC — Papers 1 and 2, expository monographs

Immutable source of truth. Workers, verifiers, and the orchestrator may not weaken or
redefine anything here.

## Objective

Produce two self-contained, textbook-grade expository papers as compiled PDFs, each
presenting one original methodological finding about spatial weights matrices, written so
that a numerate reader with **no statistics background** can follow the complete argument
from first principles to conclusion.

Length is not a constraint. Clarity, completeness of exposition, and traceability of every
claim are the constraints. These are deliberately *not* conventional journal manuscripts:
they should read as lecture notes that happen to contain new results.

- **Paper 1 — Component structure and local spatial statistics.** Disconnection of the
  neighbour graph biases Getis-Ord Gi\* through a global-standardisation artifact, and
  largely spares Moran's I.
- **Paper 2 — Selective inference for weights-matrix selection.** Choosing the neighbour
  parameter by inspecting the result inflates the false-positive rate roughly threefold,
  and the correction is derivable.

## Deliverables

| ID | Deliverable |
|---|---|
| D-1 | `papers/paper1/paper1.pdf` — compiled, from committed LaTeX source |
| D-2 | `papers/paper2/paper2.pdf` — compiled, from committed LaTeX source |
| D-3 | `papers/shared/primer.tex` — shared from-first-principles primer, `\input` by both |
| D-4 | `papers/shared/refs.bib` — BibTeX corpus for all cited sources |
| D-5 | `papers/shared/annotated_bibliography.tex` — per-source annotation (see AC-004) |
| D-6 | `analysis/04_disconnection_prevalence.py` + committed outputs — Paper 1 evidence |
| D-7 | `analysis/05_selection_inflation.py` + committed outputs — Paper 2 evidence |
| D-8 | `papers/*/figures/*.pdf` + the scripts that generate them |
| D-9 | `papers/CLAIMS.md` — every numeric claim in both papers, mapped to the script and output field that produces it |
| D-10 | `papers/Makefile` — one command rebuilds both PDFs from source |

## Definition of Done

The project is complete only when **all** of the following are objectively true.

- [ ] Both PDFs compile from a clean checkout via `make` with zero LaTeX errors.
- [ ] Every number appearing in either paper is listed in `CLAIMS.md` with a script path
      and output field, and re-running that script reproduces it.
- [ ] Every technical term is defined at first use; the glossary in each paper lists every
      such term with its defining section.
- [ ] Every cited source appears in the annotated bibliography with what it does and what
      it contributes here.
- [ ] Every cited source has been retrieved and confirmed to support the claim made of it.
- [ ] Paper 1 reports disconnection prevalence across multiple `n` and `k`, not one case.
- [ ] Paper 2 reports Type I inflation across multiple selection rules and grids.
- [ ] Each paper has an explicitly marked section stating what is new.
- [ ] Each paper has an explicitly marked limitations section.
- [ ] The case-study dataset is attributed to the author's own prior published work.
- [ ] No figure is a screenshot; all are vector PDFs from committed scripts.

## Acceptance Criteria

**AC-001** Both `paper1.pdf` and `paper2.pdf` exist and compile from committed source with
zero errors and no unresolved references or citations.

**AC-002** Every quantitative claim in either paper is traceable: `CLAIMS.md` maps it to a
committed script and output field, and re-execution reproduces the stated value (exact for
deterministic quantities; within stated Monte Carlo error for simulated ones).

**AC-003** No term of art appears without a prior definition in plain language. This
includes at minimum: p-value, null hypothesis, permutation test, standard deviation,
z-score, matrix, eigenvalue, eigenvector, quadratic form, spatial weights matrix, connected
component, Moran's I, Getis-Ord Gi\*, Type I error, selective inference, multiple
comparisons. Each paper carries a glossary keyed to defining sections.

**AC-004** Every cited source has an annotation stating (a) what the source itself does,
(b) why it is credible or notable, and (c) precisely what this paper takes from it.
Bare citations without annotation are not acceptable.

**AC-005** Every cited source has been retrieved and verified to contain the claim
attributed to it. Sources that cannot be retrieved are removed or explicitly flagged as
unverified in the annotation.

**AC-006** Paper 1 establishes disconnection prevalence empirically across a range of
sample sizes and `k` values drawn from real geography, reporting the fraction of
configurations that silently disconnect.

**AC-007** Paper 2 establishes Type I error inflation across at least three selection
rules (e.g. arg-max of I, min p-value, first-significant) and at least two candidate
grids, reporting inflation as a surface rather than a point.

**AC-008** Each paper contains a clearly marked section — titled so it is findable from
the table of contents — stating the novel contribution and distinguishing it from prior
work.

**AC-009** Where the compute-accessibility atlas is used as a case study, it is attributed
to the author's own prior published work, and the correction to its results is stated
plainly rather than euphemistically.

**AC-010** Each paper contains a limitations section stating which claims rest on a single
dataset, which are simulation-based, and what would falsify them.

**AC-011** Every figure is a vector PDF produced by a committed script; figure scripts are
listed in `CLAIMS.md`.

**AC-012** Each paper's structure separates exposition from contribution so a reader can
locate the new result without reading linearly — enforced via a labelled section scheme
and a table of contents.

## Constraints

- **Output format:** LaTeX source compiled to PDF. No Markdown deliverable.
- **Authoring constraint:** `.tex` files MUST be written with the Write/Edit tools. Bash
  heredocs corrupt backslash sequences in this environment (verified: `\\` collapses to
  `\`, breaking tabulars). This is not optional.
- **Audience:** numerate reader, no statistics background assumed. Algebra and reading a
  graph may be assumed; nothing else.
- **Attribution:** the case-study atlas is named as the author's own prior work.
- **Reproducibility:** every number from a committed script. No hand-computed values.
- **Determinism:** all simulations carry an explicit seed.
- **Existing code:** reuse `tools/` and `code/spatialrmt/`; do not fork or duplicate them.
- **Submissions untouched:** `eip/` and `fisher/` are frozen. Read only.
- **Honesty:** negative and null results are reported, not omitted. Specifically, Paper 1
  must report that Moran's I is essentially unaffected.

## Non-goals

- Journal submission, formatting to a specific journal's style, or cover letters.
- Papers 3 and 4 from the research plan.
- Any differential-privacy material.
- Correcting or republishing the StoryMaps themselves.
- New spatial statistics methodology beyond the two findings specified.
- Proving the d = 2 Thouless threshold.

## Approved Assumptions

- **A-1** Two separate self-contained PDFs, not one combined monograph. The shared primer
  is written once and `\input` into both, so each reads standalone.
- **A-2** Papers live under `papers/` at repo root, outside both submission trees.
- **A-3** `natbib` with an author-year style; `booktabs` tables; `hyperref` with a
  navigable table of contents.
- **A-4** Simulation replicate counts sized so reported rates have Monte Carlo standard
  error below 0.5 percentage points (≥ 20,000 replicates for the inflation study).
- **A-5** Where the literature check finds prior work that partially preempts a claim, the
  claim is narrowed in the paper rather than the source omitted.

## Environment

Verified in this session:

- **LaTeX:** MiKTeX 25.12, pdfTeX 4.23, latexmk 4.87. Compiles `amsmath`, `amssymb`,
  `booktabs`, `graphicx`, `hyperref`, `natbib`, `geometry`. Confirmed by smoke test.
- **matplotlib** 3.10.8 exports vector PDF that embeds cleanly via `\includegraphics`.
- **pandoc** 3.8.3 available but not required by the chosen format.
- **Stats stack:** numpy 2.3.5, scipy 1.17.0, pandas 2.3.3, libpysal 4.15.0, esda 2.10.0,
  geopandas 1.1.4.
- **Data on hand:** `analysis/data/ai_cities_319.csv` (319 matched cities);
  `eip/data/raw/worldcities.csv` (41,001 cities) available for the prevalence scale-up.
- **Existing verified results** (already computed, in `analysis/outputs/`): component split
  252/67; cold-spot rates 20.9% vs 7.5%; mean Gi\* z −0.566 vs +0.142; within-component
  fix moves cold spots 33→25 and 14→3 in the small component; Moran's I p 0.0085 (free)
  vs 0.0080 (stratified); Moran's I by k = {0.0545, 0.0574, 0.0685, 0.0373, 0.0195,
  0.0053}; Type I inflation 14.4% vs 5.0% nominal over a six-value grid at 20,000
  replicates; mean inter-k correlation 0.605.
