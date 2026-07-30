# Run 2 v2 Reproducibility Log

Created: 2026-04-29

## Environment assumptions

- Python 3 with pandas, numpy, and matplotlib.
- All scripts run from project root `/mnt/data` using relative paths.
- No API keys, credentials, or secrets were used.
- Existing Run 2 raw/processed data were reused; no new external datasets were downloaded.

## Commands run

```bash
cp '/mnt/data/WORK (18).md' /mnt/data/WORK.md
python scripts/10_run2v2_filter_ingredient_matrix.py
python scripts/11_run2v2_recompute_similarity_residuals.py
python scripts/12_run2v2_focus_case_models.py
python scripts/13_run2v2_path_connectivity_proxy.py
python scripts/14_run2v2_residual_bridge_scores.py
python scripts/15_run2v2_boundary_permeability_check.py
python scripts/16_run2v2_make_figures_and_summaries.py
```

## Notes on failures and recovery

- A broad all-in-one build helper was attempted and terminated by the execution environment. The run was completed by executing smaller task scripts individually and then producing summaries/figures in this script.
- Some earlier Run 2 v2 outputs were regenerated to ensure consistency with the final filtered residual table.

## Principal inputs

- `data/processed/cuisine_ingredient_long.csv`
- `data/processed/residual_culinary_corridors.csv`
- `data/crosswalks/cuisine_geo_crosswalk.csv`
- `data/crosswalks/run2v2_generic_ingredient_policy.csv`
- `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv`

## Principal outputs

- `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`
- `data/processed/run2v2_residual_culinary_corridors_filtered.csv`
- `data/processed/run2v2_focus_case_results.csv`
- `data/processed/run2v2_path_connectivity_results.csv`
- `data/processed/run2v2_cuisine_residual_bridge_scores.csv`
- `data/processed/run2v2_boundary_permeability_results.csv`
- `figures/run2v2_global_residual_corridor_map_filtered.png`
- `figures/run2v2_east_southeast_asia_case_map.png`
- `figures/run2v2_iberian_atlantic_case_map.png`
- `figures/run2v2_residual_bridge_score_map.png`
- `figures/run2v2_geospatial_method_comparison.png`
