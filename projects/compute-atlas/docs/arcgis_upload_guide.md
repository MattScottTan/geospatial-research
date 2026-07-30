# ArcGIS Online Upload Guide

This guide covers the repo-managed layers that should be uploaded to ArcGIS Online for the AI Compute Accessibility Atlas browser deliverables.

## Before you start

- Sign in to ArcGIS Online with privileges to create content and publish hosted feature layers.
- Create or pick a folder in `Content > My content` for this project. Recommended folder name: `AI Compute Accessibility Atlas`.
- Upload the local files from this repo root. The GeoJSON files below are all well under ArcGIS Online's 100 MB publish limit for local GeoJSON uploads.
- Expect ArcGIS Online to publish hosted layers in Web Mercator even though the source files in this repo are stored in `EPSG:4326`.

## Upload these layers

| ArcGIS title | Local file | Geometry | Rows | Why it matters |
| --- | --- | --- | ---: | --- |
| `ai_access_cities` | `outputs/gis/ai_access_cities.geojson` | points | 8,000 | Main global city accessibility layer |
| `cities_with_hotspots` | `outputs/gis/cities_with_hotspots.geojson` | points | 319 | AI research hot-spot / cold-spot diagnostics |
| `priority_cities` | `outputs/gis/priority_cities.geojson` | points | 1,988 | "AI desert" / priority-city candidates |
| `cloud_regions` | `data/processed/cloud_regions.gpkg` | points | 111 | AWS, Azure, and GCP region locations |

## Recommended upload order

1. `ai_access_cities`
2. `cities_with_hotspots`
3. `priority_cities`
4. `cloud_regions`

Uploading in this order makes it easier to reuse the same project folder, tags, and summary text.

## Click-by-click upload steps

Use this flow for each layer:

1. Open `Content > My content`.
2. Click `New item`.
3. Click `Your device`.
4. Browse to the local file listed above and select it.
5. Choose the option that creates a hosted feature layer.
   If ArcGIS Online shows `Feature layer > Upload a file > Your device` instead of the simpler `New item > Your device` flow, that is the same workflow.
6. Click `Next`.
7. Set the title exactly as listed in the table above.
8. Save the item into the `AI Compute Accessibility Atlas` folder.
9. Add tags such as `ai`, `compute`, `accessibility`, `atlas`, and `eip`.
10. Add a short summary, then click `Save`.
11. Wait for publishing to finish, then open the hosted layer and confirm the row count matches the table above.

## Layer-specific notes

### `ai_access_cities`

Use `outputs/gis/ai_access_cities.geojson`.

Key fields to keep in popups or tables:

- `city_id`: stable city identifier from the source city frame
- `city`
- `country`
- `iso2`
- `population`
- `dist_km_nearest_region`
- `access_score`
- `nearest_provider`
- `nearest_region`
- `nearest_location_name`

Use this layer for the baseline compute-access map. The most important symbology field is `dist_km_nearest_region`.

### `cities_with_hotspots`

Use `outputs/gis/cities_with_hotspots.geojson`.

Key fields:

- `city_id`
- `city`
- `country`
- `openalex_ai_works_recent`
- `gi_star_z`
- `gi_star_p`
- `hotspot_class`
- `hotspot_rank`
- `dist_km_nearest_region`
- `access_score`

Use this layer for the AI research clustering map. `hotspot_class` is the easiest field for categories; `gi_star_z` is the numeric intensity field.

### `priority_cities`

Use `outputs/gis/priority_cities.geojson`.

Key fields:

- `city_id`
- `city`
- `country`
- `population`
- `dist_km_nearest_region`
- `priority_rank`
- `observed_ai_works_recent`
- `priority_rule`
- `priority_distance_threshold_km`

Use this layer for the "AI deserts" / priority-city map. The main sort field is `priority_rank`.

### `cloud_regions`

Use `data/processed/cloud_regions.gpkg`.

ArcGIS Online can publish an OGC GeoPackage as a hosted feature layer. This file currently contains one spatial table, so it should publish as a single layer named `regions` inside the hosted item.

Key fields:

- `provider`
- `region`
- `location_name`
- `country_tld`
- `lat`
- `lon`

Use this layer as the reference overlay for all three web maps.

## Quick QA after each upload

Check these before moving on:

- The hosted layer opens in Map Viewer without errors.
- The feature count matches the row count listed in this guide.
- `city_id` appears on the three GeoJSON-derived layers.
- `dist_km_nearest_region` is numeric on `ai_access_cities`, `cities_with_hotspots`, and `priority_cities`.
- `provider` and `region` are present on `cloud_regions`.

## If something goes wrong

- If a GeoJSON upload fails, confirm you selected the hosted feature layer option rather than adding the file only as a raw item.
- If field names look wrong, delete the failed hosted layer and re-upload from the current repo outputs. The GeoJSON exports in this repo are already normalized for web use.
- If the GeoPackage upload is rejected, confirm you selected `data/processed/cloud_regions.gpkg` and not one of the raw provider CSVs.

## Checked against

- ArcGIS Online Help: Publish hosted feature layers
  - <https://doc.arcgis.com/en/arcgis-online/manage-data/publish-features.htm>
- ArcGIS Online Help: Add layers from files
  - <https://doc.arcgis.com/en/arcgis-online/create-maps/add-layers-from-file.htm>
