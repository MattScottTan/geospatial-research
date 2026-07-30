# Bridges Across Cuisines — Final Project Package

**Project:** Matthew Tan's submission to the Howard T. Fisher Prize in GIS at Harvard CGA.
**Packaged:** May 3, 2026 — after the final geospatial follow-on analysis pass.

This package contains everything the project produced: writeup, PDF preview, figures, code, data, and documentation. Folders are numbered for logical reading order.

---

## Folder guide

### 01_writeup/ — the paste source
- `BUILD_INSTRUCTIONS_v8.md` — the ArcGIS StoryMaps paste script. Walk through top-to-bottom in the ArcGIS editor. Every action marked with `> ➤ Click +`. This is the single file that becomes the published StoryMap.
- `bridges_interactive.html` — Leaflet-based interactive corridor visualization that can embed inside the StoryMap.

### 02_pdf_preview/ — read-first-before-pasting preview
- `storymap_preview.pdf` — 23-page rendered preview of the full StoryMap content. Read end-to-end to verify flow, sequencing, and figure placement before opening the ArcGIS editor.
- `storymap_preview.tex` — XeLaTeX source. Recompile with `xelatex storymap_preview.tex` (twice, for cross-references) if you need to tweak typography.

### 03_figures/ — all 11 final figures
Production PNGs used in the StoryMap. Mapping to sections:
- `v4_01_hero_world_corridors.png` → Section 2 (Introduction hero map)
- `v4_02_method_residual_baseline.png` → Section 4 (Finding 1)
- `v4_07_lisa_and_mantel.png` → Section 5 (Finding 1.5)
- `v4_06_secondary_residuals_by_grouping.png` → Section 6 (Finding 2)
- `v4_05_bridge_index_map_and_chart.png` → Section 7 (Finding 3)
- `v4_03_primary_case_regional_map.png` → Section 8 (Finding 4)
- `v4_04_topographic_corridor_map.png` → Section 8 (Finding 4, second figure)
- `v4_08_case_filipino.png`, `v4_08_case_russian.png`, `v4_08_case_thai.png`, `v4_08_case_spanish.png` → Section 9 (four case studies)

### 04_analysis_extension/ — the geospatial follow-on work (most recent)
The final analytical pass added three new hypothesis tests to the project. Everything reproducible with seed = 42.
- `README.md` — describes each script and reproduces the ranking table.
- `colonial_crosswalk.csv` — 190 cuisine pairs coded 0/1/2 (colonial administration) with per-pair rationale.
- `colonial_mantel.py` + `colonial_mantel_results.json` — main partial Mantel test (**r = +0.181, p = 0.022, 9999 perm**).
- `colonial_mantel_sensitivity.py` + `colonial_mantel_sensitivity.json` — sensitivity across 4 codings (r ∈ [+0.14, +0.18], 3 of 4 p < 0.05).
- `russian_anchor_sensitivity.py` + `russian_anchor_sensitivity.json` — Moscow vs Siberian centroid comparison (LL sign robust; significance fragile).
- `bridge_bootstrap.py` + `bridge_bootstrap.json` — 2000-iteration bootstrap CIs on bridge index (wide at n=20; Filipino top-3 frequency 47%).
- `top3_permutation.py` + `top3_permutation.json` — permutation test on published top-3 {Filipino, Russian, Southern U.S.} (**p = 0.0001**, 0 matches in 9999 shuffles).
- Copies of `mantel_results.json` and `lisa_results.json` for scripts that need them as inputs.

### 05_analysis_pipeline/ — original development scripts (in execution order)
The step-by-step Python that built the residual matrix, the Mantel tests, and the LISA results.
- `step1_verify_baseline.py` — distance-similarity regression.
- `step1b_filter_sweep.py` — ingredient-filter parameter sweep.
- `step1c_validate_residuals.py` — residual validation and top-pair inspection.
- `step2_mantel.py` — Mantel + partial Mantel infrastructure (uses SUBREGION mapping shared by the extension scripts).
- `step3_lisa.py` — Local Moran's I with inverse-distance weights, permutation testing.
- `step3b_lisa_robustness.py` — LISA across four spatial-weights schemes.
- `step4d_final_figure.py` — preview builder for Finding 1.5 figure.
- `build_case_studies.py` — case-study spotlight figure builder. **Important:** contains the hardcoded BRIDGE_SCORES dict (Filipino 0.87, Russian 0.84, ...). Those values are constants here, not computed. See known limitations.

### 06_reference_inputs/ — precomputed analytical matrices
Drop-in inputs for any re-analysis.
- `cuisines.txt` — 20 cuisine labels in matrix order.
- `cuisine_ingredient_matrix.csv` — 20 × 1434 source matrix.
- `similarity_matrix.npy` — cosine similarity, filtered.
- `distance_matrix.npy` — great-circle km between cuisine anchors.
- `residual_matrix.npy` — observed similarity minus distance-predicted.
- `mean_resid.npy` — per-cuisine mean residual.
- `mantel_results.json`, `lisa_results.json`, `lisa_robustness.json` — published test outputs.

### 07_tools/ — figure builders and the LaTeX converter
- `figdata.py` — centralized cuisine anchor coordinates. **Known bug:** Moroccan longitude is 35.21 (should be −7.09). The residual matrix uses the correct value; only figdata.py has the bug. Any figure regenerated from this file may inherit the artifact.
- `build_fig01_hero.py` through `build_fig08_case_studies.py` — production figure builders (hero, primary case, bridge index, secondary, LISA + Mantel, case studies).
- `build_v4_02.py`, `build_v4_06.py` — simplified regeneration scripts for the residual scatter and spatial-groupings chart (standalone from the ingredient matrix).
- `build_latex.py` — converts `BUILD_INSTRUCTIONS_v8.md` to a LaTeX preview document.

### 08_documentation/ — narrative documents
Read in this order for context:
1. `SUBMISSION_README.md` — the original submission package overview.
2. `DEPLOYMENT_GUIDE.md` — steps to publish the StoryMap in ArcGIS.
3. `PRIZE_ENTRY_DESCRIPTION.md` — four length variants of the project description for the submission email.
4. `QA_REPORT.md` — pre-submission quality audit (Moroccan-longitude bug, v4_01 hero pixel artifact, other known issues).
5. `SCORING_PASS_NOTES.md` — the framing/competitiveness pass (claim title, front-loaded question, payoff paragraph, claim-led captions).
6. `ANALYSIS_EXTENSION_NOTES.md` — the geospatial follow-on pass (what's in `04_analysis_extension/`, how it integrates into the writeup, known limitations).
7. `WORK_completed_final_pass.md` — full worker tracking from the geospatial follow-on session, including per-task Results and Learnings.

---

## Headline analytical results

| Test | Result | Where documented |
|---|---|---|
| Distance-similarity regression | R² = 0.40, slope = −0.124 per log-km | Finding 1 |
| Mantel test (190 pairs, 9999 perm) | r = +0.63, p < 0.001 | Finding 1.5 |
| Partial Mantel \| same-subregion | r = +0.51, p < 0.001 | Finding 1.5 |
| Partial Mantel \| colonial admin | **r = +0.18, p = 0.022** | Finding 1.6 (NEW) |
| Sensitivity (4 codings) | r ∈ [+0.14, +0.18]; 3 of 4 p < 0.05 | Finding 1.6 |
| Global Moran's I | +0.091, p ≈ 0.05 | Finding 1.5 |
| Significant LISA | Mexican HH, Jamaican HH, Russian LL | Finding 1.5 |
| Russian LL under Moscow anchor | Sign robust; significance weakens | Russian case study |
| Top residual pairs | Chinese-Korean +0.435, Irish-Southern_US +0.395, Thai-Vietnamese +0.395 | Finding 4 |
| Published top-3 bridge cuisines | Filipino 0.87, Russian 0.84, Southern_US 0.69 | Finding 3 |
| Bridge-bootstrap top-3 frequency | Filipino 47%; wide CIs at n=20 | Finding 1.6 |
| Top-3 permutation test | **p = 0.0001** (0/9999 matches) | Finding 1.6, Conclusion |

## Known limitations

- **n = 20 corpus** underrepresents Africa, most of South Asia, the Middle East, Oceania.
- **Russian anchor** at Siberian centroid by default (61.52°N, 105.32°E). Moscow alternative preserves LL sign but weakens significance.
- **Bridge-index values are hardcoded** in `05_analysis_pipeline/build_case_studies.py`, not reproducible from the descriptive formula alone. Independent reimplementations qualitatively match the ranking.
- **PySAL vs independent LISA** — published p = 0.009 (PySAL); independent implementation gives p ≈ 0.08 for Russian LL. Local I value matches; permutation-distribution construction differs.
- **Moroccan longitude bug** in `07_tools/figdata.py` (35.21 should be −7.09). Residual matrix correct; only figdata.py wrong.

---

## Reproduce anything

### Rebuild the PDF preview
```
cd 02_pdf_preview
cp -r ../03_figures ./figures
xelatex storymap_preview.tex
xelatex storymap_preview.tex
```

### Re-run the analysis extension
```
cd 04_analysis_extension
cp ../06_reference_inputs/{residual_matrix.npy,distance_matrix.npy,cuisines.txt} .
python3 colonial_mantel.py
python3 colonial_mantel_sensitivity.py
python3 russian_anchor_sensitivity.py
python3 bridge_bootstrap.py
python3 top3_permutation.py
```

All scripts: seed = 42, 9999 permutations (Mantel + permutation tests), 2000 iterations (bootstrap). Outputs deterministic given inputs.

### Re-run the original pipeline
```
cd 05_analysis_pipeline
cp ../06_reference_inputs/* .
python3 step1_verify_baseline.py
python3 step1b_filter_sweep.py
python3 step1c_validate_residuals.py
python3 step2_mantel.py
python3 step3_lisa.py
python3 step3b_lisa_robustness.py
python3 step4d_final_figure.py
```

### Regenerate a figure
Figure builders in `07_tools/` require the working directory plus Natural Earth shapefiles. `build_v4_02.py` and `build_v4_06.py` are standalone and only need `cuisine_ingredient_matrix.csv`.
