# Fisher award submission materials

Documentation for the Fisher Prize submission of the culinary corridors project,
consolidated from `Downloads/Fisher All Past Resources/`.

Seven archives, 424 files extracted, deduplicating to **186 unique documents and 43
unique scripts**. `culinary_corridors_MASTER.zip` alone carries 145 of the unique
documents — it is a full project archive rather than a submission package, and its tree is
preserved under `project-archive/`.

Note the project appears under two titles: **"Bridges Across Cuisines"** in these archives,
**"Salt, Fat, Acid, Distance"** as published. Same analysis, later rename.

## This folder closed the project's biggest gap

Before these archives, the culinary project had no statistical code anywhere on the
machine — the Mantel tests and Local Moran's I existed only as numbers in the StoryMap.
The full pipeline was in `bridges_final_package.zip` and is now at
[`../analysis/`](../analysis), with its working matrices in `../analysis/working_data/`.

It uses `esda.moran` and `libpysal.weights` — real PySAL, not ArcGIS — with `seed = 42`
and 9,999 permutations throughout, so it is deterministic and rerunnable.

**Every published statistic reproduces from the shipped JSON:**

| StoryMap claim | Source file | Value |
|---|---|---|
| Mantel r = +0.630 | `mantel_results.json` | 0.6300775896 |
| Partial r = +0.512 (controlling subregion) | `mantel_results.json` | 0.5116466704 |
| Colonial partial Mantel r = +0.181, p = 0.022 | `colonial_mantel_results.json` → `partial_mantel_H2_main`, labelled "HEADLINE RESULT" | 0.18097, p = 0.0216 |
| Russian LL classification p = 0.009 | `lisa_results.json` | per-cuisine LISA |

The pipeline goes further than the StoryMap reports: `colonial_mantel_sensitivity.json`
carries four alternative colonial codings (r ranges 0.138–0.181; the Spanish-sphere-only
coding falls to p = 0.087), plus `russian_anchor_sensitivity.json`, `bridge_bootstrap.json`
and `top3_permutation.json`.

One thing to be aware of: `lisa_results.json` records **global Moran's I = 0.0912 with
p = 0.052**, which does not clear 0.05. The StoryMap reports only the local LISA
classifications and never claims the global statistic is significant, so nothing is
misstated — but a reader could reasonably assume a significant global test underpins the
local ones, and it does not.

## Contents

| Directory | What is in it |
|---|---|
| `strategy/` | Fisher award playbook, scoring rubric, feature matrix, topic scoring template, production timeline, prize entry description, scoring pass notes, rubric work |
| `criteria-storybooks/` | Six per-criterion storybooks (innovation, GIS use, data, analysis execution, visualisation/cartography, synthesis) plus the feature matrix |
| `methods/` | `BUILD_INSTRUCTIONS_v8.md` (85 KB), deployment guide, ArcGIS Online workflow, corridor geometry fixes and supplement, fallback hosting |
| `storymap/` | Paste script, submission README, `STORYMAP_CHANGES.md` |
| `qa/` | QA report, analysis extension notes, submission README |
| `worklog/` | Five work logs including the 36 KB final-pass log and the 34 KB master task log |
| `interactive/` | Two standalone interactive HTML builds, five corridor GeoJSON variants, cuisine anchors |
| `figures/` | 25 unique figures after deduplication |
| `reports/` | Four PDFs (`Bridges_Across_Cuisines`, `Salt__Fat__Acid__Distance`, full report, 9.2 MB StoryMap preview) plus `storymap_preview.tex` |
| `project-archive/` | The 149-file `culinary_corridors_MASTER` tree: version history, multiple submission and report generations, crosswalks, processed data |

## Source archives

| Archive | Files | Unique contribution |
|---|---|---|
| `culinary_corridors_MASTER.zip` (71 MB) | 282 | Full project archive — 145 unique docs, version history, all submission generations |
| `bridges_final_package.zip` (20 MB) | 73 | **The analysis pipeline and extensions**, reference inputs, QA documentation, `BUILD_INSTRUCTIONS_v8` |
| `bridges_across_cuisines_complete.zip` (11 MB) | 69 | Fisher criteria storybooks, LISA upgrade tree, original submission package |
| `fisher_prize_final_1.zip` (4.8 MB) | 30 | ArcGIS Online interactive workflow, corridor GeoJSONs, paste script |
| `fisher_bundle.zip` (9.5 MB) | 13 | Strategy packet (playbook, rubric, feature matrix, timeline) |
| `fisher_prize_final.zip` (3.2 MB) | 13 | `build_fig07_lisa_and_mantel.py`, case study builders |
| `salt_fat_acid_distance_bundle.zip` (855 KB) | 10 | Published `Salt__Fat__Acid__Distance.pdf` |

Files duplicating content already committed elsewhere in the repo — four `v4_*` figures,
three report PDFs, and two build/worklog documents — were dropped rather than stored twice.
