# EIP award submission materials

Documentation for the EIP award submission of "Cloudy with a Chance of Compute,"
consolidated from `Downloads/EIP All Past Resources/`.

That folder held seven zip archives plus four loose markdown files. The archives overlap
heavily — 190 files extracted, but only **34 unique documents** by content hash. The eight
core strategy and methods docs appear byte-identical in six or seven archives each.
This directory holds one canonical copy of each.

## Contents

### `strategy/` — award positioning
| File | What it is |
|---|---|
| `AWARD_PLAYBOOK.md` | Award strategy and framing |
| `WINNER_MATRIX.md` | Comparison against prior winning submissions |
| `SUBMISSION_GAP_ANALYSIS.md` | Self-assessment of submission weaknesses |
| `REVISION_CHECKLIST.md` | Pre-submission revision list |
| `CONTINUATION_WORK.md` | Planned follow-on work |
| `NOVELTY_METHODS_MEMO.md` | Methodological novelty argument |
| `WORK_EIP_FISHER_ADAPTED.md` | Work plan adapted for the Fisher submission |

### `methods/` — ArcGIS workflow
| File | What it is |
|---|---|
| `SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md` | **Records the spatial weights specification** — see below |
| `ARCGIS_PRO_MASTER_WORKFLOW.md` | Full ArcGIS Pro workflow |
| `ARCGIS_PRO_CLICK_BY_CLICK_FINDINGS_1_5.md` | Step-by-step reproduction of Findings 1–5 |
| `ARCGIS_FINAL_INSTRUCTIONS.md` | Final build instructions |
| `HERO_MAP_INSTRUCTIONS.md` | Hero map construction |
| `arcgis_handoff.md`, `webmap_specs.md` | Web map specs and handoff notes |

### `storymap/` — text and editorial
Final script, continuation sections, bundle-section replacement, case study text,
bibliography, sources/credits, captions and alt text, proofreading fixes, paste-ready
blocks, asset manifest, bio requirements, case study scorecard.

### `worklog/`
`WORK.md` (the 38 KB running work log) and `package_readmes/` — the five per-archive
READMEs, which differ from each other and are kept for provenance.

### `screenshots/`
16 PNGs of the live StoryMap captured during the bundle-index revision session.

### `reports/`
Five PDFs plus the LaTeX source (`main.tex`, `references.bib`). Note two different
StoryMap PDF exports exist (`storymap_export_final.pdf` 1.1 MB, `storymap_export_earlier.pdf`
413 KB) with no stated precedence, alongside `authoritative_final_report.pdf` (7.6 MB)
and `original_report.pdf` (2.2 MB).

## Two gaps these files close

**The spatial weights specification is recorded after all.**
`methods/SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md` specifies the Moran's I and Getis-Ord Gi\*
setup as **K Nearest Neighbors, K = 8, Row standardization**, Euclidean distance on WGS84.
The document also notes that exactly replicating the Python results requires matching that
specification — so the choice was deliberate and documented, just not in code.

**Findings 1 and 2 have code.** `cloudy_compute_session_export.zip` contained two analysis
scripts, now at `../src/analysis/`:

- `distributional_tests.py` — two-sample KS, Mann-Whitney U, chi-square on the 500 km threshold
- `weighted_concentration_tests.py` — activity-weighted distance distribution, Spearman rank correlation

Together these reproduce the reported D = 0.30, U = 786,844, χ² = 103.8, and the
Spearman −0.05. Neither imports `libpysal` or `esda`, so **Finding 3 (Moran's I = 0.066,
Getis-Ord Gi\*) still has no Python implementation** — it remains ArcGIS-only, now with
its parameters documented.

## Source archives

| Archive | Unique contribution |
|---|---|
| `Cloudy_with_a_Chance_of_Compute_Final_Package.zip` (24 MB, 79 files) | Complete single tree: `pipeline.py`, all data, `gis/`, 24 figures, case studies, `main.tex` |
| `cloudy_with_a_chance_of_compute_package.zip` (4.8 MB, 48 files) | `NOVELTY_METHODS_MEMO.md`, `final_storymap_script.md`, `build_prototypes.py` |
| `cloudy_compute_session_export.zip` (1.5 MB, 37 files) | The two analysis scripts, ArcGIS click-by-click docs, 16 screenshots |
| `cloudy_with_a_chance_of_compute_package_1.zip` (7.4 MB, 19 files) | `BIBLIOGRAPHY.md`, `storymap_continuation.md`, authoritative report PDF |
| `eip_project_package.zip` (1.9 MB, 15 files) | `worker_plan/WORK.md`, `original_report/main.pdf` |
| `Cloudy_Compute_Full_Package.zip` (266 KB, 18 files) | Paste-ready text blocks |
| `Cloudy_With_A_Chance_Of_Compute_Project_Files.zip` (56 KB, 9 files) | Nothing unique — subset of the core eight |

`Cloudy_with_a_Chance_of_Compute_Final_Package.zip` contains `scripts/pipeline.py`
byte-identical (127,697 bytes) to the copy in `…Submission_Package Part 4`, but bundles
the data and GIS layers alongside it. It supersedes the six-part split described in
`../../../docs/SOURCE_MANIFEST.md`.
