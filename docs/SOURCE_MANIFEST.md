# Source manifest

Where every tracked file in this repo came from on the local machine, recorded so the
assembly is auditable and re-runnable. Both projects arrived as multiple overlapping
zip extractions in `~/Downloads`; neither existed as a single coherent tree.

`scripts/bootstrap_repo.ps1` performs the copies listed here.

## projects/compute-atlas

The AI compute atlas was split across six separately-downloaded "Part N" folders. No
single one is complete — the data is in Part 1, the build system in Part 2, and the
actual pipeline source in Part 4.

| Destination | Source |
|---|---|
| `src/` | `Downloads/AI_Compute_Accessibility_Atlas_EIP_Submission_Package Part 4/src/` |
| `data/raw/` | `Downloads/AI_Compute_Accessibility_Atlas_EIP_Submission_Package/data/raw/` |
| `data/processed/` | `…_Package/data/processed/` (untracked; `make prepare` regenerates) |
| `docs/` | `…_Package/docs/` |
| `extensions/` | `…_Package/extensions/` (stage4, stage5, stage6) |
| `deliverables/` | `…_Package/deliverables/` |
| `report/` | `…_Package Part 2/report/` |
| `Makefile`, `Makefile.local` | `…_Package Part 2/` |
| `requirements-extended.txt` | `…_Package Part 2/` |
| `submission/` | `…_Package Part 3/final_submission/` |
| `submission/originality/` | `…_Package Part 6/final_submission/originality/` |
| `openalex/` | `Documents/Projects/openalex_overlay/` (excluding `.venv`) |

### EIP award archives

`Downloads/EIP All Past Resources/` held seven zips (190 files, 34 unique documents) plus
four loose markdown files. Documentation from all of them is consolidated, one canonical
copy each, into `projects/compute-atlas/eip-award/` — see that directory's README for the
per-archive breakdown.

Two things came out of those archives beyond documentation:

- `src/analysis/distributional_tests.py` and `weighted_concentration_tests.py`, from
  `cloudy_compute_session_export.zip` — the previously-missing code for Findings 1 and 2.
- `Cloudy_with_a_Chance_of_Compute_Final_Package.zip` is a complete single tree:
  `pipeline.py` byte-identical to the Part 4 copy (127,697 bytes) but bundled with
  `data/`, `gis/`, 24 figures and the case studies. The bootstrap script now takes those
  four directories from it rather than from the six-part split, which remains the source
  for `extensions/`, `docs/`, `deliverables/`, `report/`, `submission/` and the Makefile.

Notes:

- `Documents/Projects/openalex_overlay/make_openalex_ai_city_overlay.py` is the script
  that produced `data/raw/openalex_ai_city_overlay.csv`. It lived outside the
  submission package entirely and is the only copy.
- `requirements-extended.txt` begins with `-r requirements.txt`, but **no
  `requirements.txt` exists in any Part**. The root `requirements.txt` in this repo
  was reconstructed from the actual import graph of `src/pipeline.py`.
- `Documents/Projects/EIP Project/` and `EIP Project V2/` are empty directories.
- `…_Package/extensions/eip_cases/EIP%20Project/` has a URL-encoded name; the
  bootstrap script quotes it rather than decoding, to preserve the original path.
- `.codex/` is gitignored — it holds local agent tool configuration, not project work.

## projects/culinary-corridors

Three overlapping packages, all retained under `versions/` with none designated
authoritative. See the project README for the inferred lineage.

| Destination | Source |
|---|---|
| `data/raw/cuisine_ingredient_matrix.csv` | `Downloads/cuisine_ingredient_matrix.csv` |
| `versions/fisher-submission/` | `Downloads/culinary_corridors_fisher_submission/culinary_corridors_fisher_submission/` (`code/`, README, BUILD_INSTRUCTIONS, WORK_completed) |
| `versions/storymap-v3-balanced/` | `Downloads/culinary_corridors_storymap_balanced_v3_package/` (`submission/`, `docs/`, `outputs/` → `audits/`, `WORK*.md`) |
| `versions/storymap-v5/` | `Downloads/files (2)/` (v5 BUILD_INSTRUCTIONS + `v4_01`–`v4_06` PNGs → `figures/`) |
| `reports/` | `Downloads/culinary_corridors_{complete_final,committee,winner_aligned}_report.pdf` |

Notes:

- `cuisine_ingredient_matrix.csv` sat loose in `Downloads`, not inside any package. It
  appears to be the only actual input dataset for this project.
- Three report PDFs exist with no version markers (`complete_final`, `committee`,
  `winner_aligned`). All three are kept; none is designated authoritative.
- `Downloads/files (2)/` is a generic download-folder name. Its contents are v5 build
  instructions plus six `v4_*` PNGs, which the `fisher-submission/code/` builders most
  likely produced — so `storymap-v5` is probably rendered output of `fisher-submission`
  rather than an independent version. Unconfirmed.
- `code/figdata.py` is not a data loader — see `REPRODUCIBILITY_GAPS.md`.

### Fisher award archives

`Downloads/Fisher All Past Resources/` held seven zips (424 files, 186 unique documents,
43 unique scripts). Documentation is consolidated into
`projects/culinary-corridors/fisher-award/` — see that directory's README for the
per-archive breakdown.

Beyond documentation, these archives supplied the entire missing statistical layer:

- `projects/culinary-corridors/analysis/` — 13 scripts (Mantel, LISA, robustness,
  case studies, five extensions) from `bridges_final_package.zip`
- `projects/culinary-corridors/analysis/working_data/` — distance, similarity and
  residual matrices plus all result JSONs
- `projects/culinary-corridors/tools/` — 10 figure builders

`culinary_corridors_MASTER.zip` is a full project archive rather than a submission
package; its tree is preserved verbatim under `fisher-award/project-archive/`.

## archive/ (untracked)

Superseded copies retained locally for provenance, excluded from git:

- `Downloads/culinary_corridors_storymap_balanced_v3_package.zip`
- `Downloads/culinary_corridors_complete_final_archive_all_materials.zip`
- `Downloads/culinary_corridors_fisher_submission.zip`
- `Downloads/files (2)/` — contains `culinary_corridors_storymap_v5_BUILD_INSTRUCTIONS.md`,
  a v5 that postdates the v3 package; relationship to the published StoryMap unverified
- `Downloads/AI_Compute_Accessibility_Atlas_EIP_Submission_Package*.zip` (Parts 2–4)
- `Downloads/01_AI_Compute_Accessibility_Atlas.pdf`,
  `02_AI_Research_Diffusion_Atlas.pdf` — early two-atlas framing, superseded

## Not migrated

- `Documents/food_projects/`, `Documents/geospatial_projects/` — empty before this repo
- `Downloads/.venv/`, `Downloads/receipt_collator_project/` — unrelated
