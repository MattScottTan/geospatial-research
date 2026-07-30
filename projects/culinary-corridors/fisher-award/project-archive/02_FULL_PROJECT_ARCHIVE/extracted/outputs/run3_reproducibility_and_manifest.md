# Run 3 Reproducibility and Manifest

Created: 2026-04-29

## Run type

Run 3 is a packaging and polishing run. It does not redo the primary data acquisition, ingredient cleaning, similarity modeling, or residual computation from Run 2 / Run 2 v2. It preserves those outputs and creates final submission copies, captions, narrative files, appendices, and claim-audit materials.

## Environment assumptions

- File operations were performed from `/mnt/data`.
- Final artifacts were written to `submission/`, `figures/final/`, `docs/`, and `outputs/`.
- No API keys, credentials, or hosted StoryMap access were used.
- No original Run 2 or Run 2 v2 figures were overwritten.

## Figure-copy commands

```bash
mkdir -p /mnt/data/figures/final /mnt/data/submission /mnt/data/outputs /mnt/data/docs
cp /mnt/data/figures/run2v2_global_residual_corridor_map_filtered.png /mnt/data/figures/final/final_global_discovery_figure.png
cp /mnt/data/figures/run2_distance_decay_plot.png /mnt/data/figures/final/final_distance_or_residual_model_figure.png
cp /mnt/data/figures/run2v2_east_southeast_asia_case_map.png /mnt/data/figures/final/final_east_southeast_asia_case_figure.png
cp /mnt/data/figures/run2v2_residual_bridge_score_map.png /mnt/data/figures/final/final_geospatial_bridge_or_boundary_figure.png
cp /mnt/data/figures/run2v2_iberian_atlantic_case_map.png /mnt/data/figures/final/final_secondary_or_sensitivity_figure.png
cp /mnt/data/figures/run2v2_geospatial_method_comparison.png /mnt/data/figures/final/final_boundary_permeability_appendix_figure.png
```

## Final figure manifest

| Final figure | Source artifact | Role |
|---|---|---|
| `figures/final/final_global_discovery_figure.png` | `figures/run2v2_global_residual_corridor_map_filtered.png` | Global discovery screen. |
| `figures/final/final_distance_or_residual_model_figure.png` | `figures/run2_distance_decay_plot.png` | Distance baseline / residual logic. |
| `figures/final/final_east_southeast_asia_case_figure.png` | `figures/run2v2_east_southeast_asia_case_map.png` | Primary focused case. |
| `figures/final/final_geospatial_bridge_or_boundary_figure.png` | `figures/run2v2_residual_bridge_score_map.png` | Residual bridge scores, strongest geospatial-only insight. |
| `figures/final/final_secondary_or_sensitivity_figure.png` | `figures/run2v2_iberian_atlantic_case_map.png` | Secondary/diagnostic corridor hypothesis. |
| `figures/final/final_boundary_permeability_appendix_figure.png` | `figures/run2v2_geospatial_method_comparison.png` | Appendix/supporting boundary/permeability proxy. |

## Data dependencies reused

- `data/processed/run2v2_residual_culinary_corridors_filtered.csv`
- `data/processed/run2v2_focus_case_results.csv`
- `data/processed/run2v2_cuisine_residual_bridge_scores.csv`
- `data/processed/run2v2_boundary_permeability_results.csv`
- `data/processed/run2v2_path_connectivity_results.csv`
- `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`
- `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv`
- `data/crosswalks/run2v2_generic_ingredient_policy.csv`
- `data/crosswalks/cuisine_geo_crosswalk.csv`

## Prior scripts underlying reused outputs

- `scripts/01_acquire_or_stage_recipe_data.py`
- `scripts/02_clean_recipe_ingredients.py`
- `scripts/03_build_cuisine_matrix.py`
- `scripts/04_compute_similarity.py`
- `scripts/05_build_distance_pairs.py`
- `scripts/06_build_pair_model_table.py`
- `scripts/07_fit_distance_baseline.py`
- `scripts/08_test_overlay_covariate.py`
- `scripts/09_make_run2_figures.py`
- `scripts/10_run2v2_filter_ingredient_matrix.py`
- `scripts/11_run2v2_recompute_similarity_residuals.py`
- `scripts/12_run2v2_focus_case_models.py`
- `scripts/13_run2v2_path_connectivity_proxy.py`
- `scripts/14_run2v2_residual_bridge_scores.py`
- `scripts/15_run2v2_boundary_permeability_check.py`
- `scripts/16_run2v2_make_figures_and_summaries.py`

## Final submission artifacts

- `submission/storymap_outline.md`
- `submission/storymap_script.md`
- `submission/fisher_submission_report.md`
- `submission/abstract_and_pitch.md`
- `submission/technical_appendix.md`
- `submission/data_sources_and_limitations.md`
- `submission/references.md`
- `submission/pia_review_packet.md`
- `submission/final_submission_checklist.md`

## Final control artifacts

- `outputs/run3_setup_note.md`
- `outputs/run3_input_artifact_audit.csv`
- `docs/run3_final_scope_and_claims.md`
- `docs/run3_fisher_positioning_memo.md`
- `docs/run3_figure_selection_memo.md`
- `outputs/run3_pia_feedback_status.md`
- `outputs/run3_claim_audit_checklist.md`
- `outputs/run3_reproducibility_and_manifest.md`

## Known reproducibility caveats

- Run 3 final figures are copied/selected from Run 2 and Run 2 v2 outputs rather than regenerated.
- The distance/residual model figure is inherited from Run 2, while the final narrative cites Run 2 v2 filtered model metrics in text.
- Public StoryMap hosting was not attempted; the deliverable is StoryMap-ready prose and assets.
- Recipe-source permission review and Pia scientific review remain manual external steps.
