# Run 5 Reproducibility and Manifest

Created: 2026-05-01

## Commands run from project root

```bash
python scripts/19_run5_topographic_corridor_visuals.py
```

## Inputs reused
- `data/processed/run4v2_east_se_asia_accessibility_metrics.csv`
- `data/crosswalks/cuisine_geo_crosswalk.csv`
- `figures/final_revised/run4v2_topographic_corridor_map.png`
- `submission/revised/storymap_script.md`
- `submission/final_committee/final_committee_report.md`
- `outputs/run4v2_topographic_corridor_summary.md`

## Relief/geodata inputs
- Basemap local relief file: `/opt/pyvenv/lib/python3.13/site-packages/mpl_toolkits/basemap_data/etopo1.jpg`
- Basemap local coastline/country boundary drawing via `Basemap(...).drawcoastlines()` and `drawcountries()`.
- No API keys, private map services, or external downloads were used.

## New Run 5 outputs
- `outputs/run5_setup_note.md`
- `outputs/run5_input_artifact_audit.csv`
- `docs/run5_topographic_visual_strategy.md`
- `data/run5_topographic_geodata_manifest.md`
- `scripts/19_run5_topographic_corridor_visuals.py`
- `data/processed/run5_east_se_asia_topographic_links_selected.csv`
- `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`
- `figures/final_revised/run5_corridor_callout_or_inset.png`
- `figures/final_revised/run5_figure_captions.md`
- `outputs/run5_topographic_corridor_interpretation.md`
- `submission/final_committee/run5_storymap_insert.md`
- `submission/final_committee/run5_report_insert.md`
- `submission/final_committee/run5_must_do_list.md`
- `outputs/run5_claim_and_visual_audit.md`
- `outputs/run5_reproducibility_and_manifest.md`

## Package assumptions
- Python with pandas, numpy, matplotlib, Pillow, and mpl_toolkits.basemap is available.
- Basemap data package includes `etopo1.jpg`.
- The map is generated from existing project outputs and does not require internet access.

## Reproducibility caveats
- The relief background is a contextual image, not a numeric DEM used for terrain modeling.
- The figure uses existing proxy metrics from Run 4 v2; it does not recompute cuisine similarity.
- Exact label placement and line curvature are cartographic choices, documented in the script.
