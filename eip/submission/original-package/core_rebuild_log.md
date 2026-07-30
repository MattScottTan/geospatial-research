# Core Rebuild Log

Date: 2026-03-14 12:00 PM America/New_York

## Command

```bash
python src/pipeline.py all
```

## Outcome

Status: **PASS**

The full core atlas pipeline completed successfully in the working repo and regenerated the baseline processed layers, tables, GIS outputs, surfaces, and figure package.

## High-signal rebuild facts

- Processed city frame: **8,000 cities**
- Cloud regions: **111**
- Matched AI-city rows: **328**
- Match-ok rate: **0.9817**
- Unique AI cities for spatial diagnostics: **319**
- Priority cities flagged: **1,988**
- Surface resolution: **1.0 degree**

## Selected regenerated outputs

- `data/processed/cities.gpkg`
- `data/processed/cloud_regions.gpkg`
- `outputs/tables/city_access_metrics.csv`
- `outputs/tables/city_access_ai.csv`
- `outputs/tables/morans_i_summary.csv`
- `outputs/tables/model_gp_summary.json`
- `outputs/tables/model_car_summary.json`
- `outputs/tables/priority_cities.csv`
- `outputs/gis/ai_access_cities.gpkg`
- `outputs/gis/ai_access_ai_cities.gpkg`
- `outputs/gis/ai_access_surface_distance.tif`
- `outputs/gis/ai_research_pred_gp.tif`
- `outputs/gis/ai_research_pred_car.tif`
- `outputs/figures/fig1_access_map.png`
- `outputs/figures/fig5_coef_compare.png`
- `outputs/figures/fig7_distance_hist.png`
- `outputs/figures/fig11_hotspot_map.png`
- `outputs/figures/fig12_priority_cities_map.png`

## Raw command tail

```text
{
  "prepare": {
    "cities_gpkg": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/data/processed/cities.gpkg",
    "regions_gpkg": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/data/processed/cloud_regions.gpkg",
    "n_cities": "8000",
    "n_regions": "111"
  },
  "access": {
    "city_access_metrics_parquet": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/city_access_metrics.csv",
    "cities_access_gpkg": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/ai_access_cities.gpkg",
    "cities_access_geojson": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/ai_access_cities.geojson"
  },
  "openalex": {
    "city_access_ai_parquet": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/city_access_ai.csv",
    "cities_ai_gpkg": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/ai_access_ai_cities.gpkg",
    "institutions_top_parquet": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/openalex_institutions_top.csv",
    "topics_used_json": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/openalex_topics_used.json",
    "n_ai_cities": "328",
    "match_ok_rate": "0.9817073170731707"
  },
  "spatial_outputs": {
    "morans_i_summary_csv": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/morans_i_summary.csv",
    "cities_with_hotspots_geojson": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/cities_with_hotspots.geojson",
    "priority_cities_csv": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/priority_cities.csv",
    "priority_cities_geojson": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/priority_cities.geojson",
    "n_unique_ai_cities": "319",
    "n_priority_cities": "1988"
  },
  "model_gp": {
    "model_gp_summary": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/model_gp_summary.json",
    "model_gp_predictions": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/model_gp_predictions.csv"
  },
  "model_car": {
    "model_car_summary": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/model_car_summary.json",
    "model_car_predictions": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/tables/model_car_predictions.csv"
  },
  "surfaces": {
    "dist_surface_tif": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/ai_access_surface_distance.tif",
    "gp_pred_tif": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/ai_research_pred_gp.tif",
    "car_pred_tif": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/gis/ai_research_pred_car.tif",
    "resolution_deg": "1.0"
  },
  "figures": {
    "figures_dir": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/outputs/figures",
    "report_figures_dir": "/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/report/figures"
  }
}

```
