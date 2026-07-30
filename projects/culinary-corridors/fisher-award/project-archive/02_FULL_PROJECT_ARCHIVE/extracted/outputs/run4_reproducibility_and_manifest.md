# Run 4 Reproducibility and Manifest

Created: 2026-04-29

## Strategy packet inputs
- `fisher_award_strategy_packet.zip`
- Extracted files under `_strategy_packet/outputs/`

## Core reused Run 2 v2 / Run 3 inputs
- `data/processed/run2v2_residual_culinary_corridors_filtered.csv`
- `data/processed/run2v2_focus_case_results.csv`
- `data/processed/run2v2_cuisine_residual_bridge_scores.csv`
- `data/processed/run2v2_boundary_permeability_results.csv`
- `data/crosswalks/cuisine_geo_crosswalk.csv`
- `submission/storymap_script.md`
- `submission/fisher_submission_report.md`
- `figures/final/*`
- `docs/run3_final_scope_and_claims.md`

## New script
- `scripts/17_run4_geospatial_upgrade.py`

## Commands / manual steps
- Extracted `fisher_award_strategy_packet.zip` into `_strategy_packet/`.
- Ran `python scripts/17_run4_geospatial_upgrade.py` from project root.
- Generated revised figures with Python/matplotlib using existing Run 2 v2 outputs.
- Created revised Markdown artifacts under `docs/`, `outputs/`, and `submission/revised/`.
- Compiled LaTeX in `report/revised/` using `pdflatex`.
- Rendered the revised PDF to page images under `report/revised/_renders/` for visual QA.

## New analysis output
- `data/processed/run4_geospatial_upgrade_results.csv`

## Revised figures
- `figures/final_revised/run4_hero_spatial_argument_figure.png`
- `figures/final_revised/run4_method_or_model_figure.png`
- `figures/final_revised/run4_primary_case_figure.png`
- `figures/final_revised/run4_geospatial_insight_figure.png`
- `figures/final_revised/run4_secondary_or_limitations_figure.png`

## Revised submission files
- `submission/revised/storymap_script.md`
- `submission/revised/fisher_submission_report.md`
- `submission/revised/abstract_and_pitch.md`
- `submission/revised/poster_text_350_word_draft.md`
- `submission/revised/pia_review_packet.md`
- `submission/revised/final_handoff_checklist.md`

## Revised report files
- `report/revised/culinary_corridors_winner_aligned_report.tex`
- `report/revised/culinary_corridors_winner_aligned_report.pdf` status: `found`
- `report/revised/culinary_corridors_winner_aligned_source_bundle.zip`
- `report/revised/latex_compile_log.txt`

## Caveats
- Figures are prototype-polished, not professionally designed.
- No hosted StoryMap was created.
- Data-license verification remains a manual pre-submission step.
