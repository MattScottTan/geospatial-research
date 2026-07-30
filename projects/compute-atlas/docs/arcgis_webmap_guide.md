# ArcGIS Web Map Guide

This guide turns the uploaded Atlas layers into the three web maps needed for the ArcGIS / StoryMap handoff:

1. `Global Compute Accessibility`
2. `AI Research and Hot Spots`
3. `AI Deserts and Priority Cities`

Build all three maps in ArcGIS Online Map Viewer.

## Common setup

Use this same setup pattern for every map:

1. Open Map Viewer.
2. Click `Add` and add layers from `My content`.
3. Use the `Layers` pane to set draw order exactly as listed in this guide.
4. For each selected layer, use the `Settings` toolbar for:
   - `Styles`
   - `Pop-ups`
   - `Labels`
   - `Properties`
5. Save the map with the exact title listed below.

## Shared layer roles

- `cloud_regions` is the reference overlay on all three maps.
- Use the same cloud-region popup everywhere:
  - `provider`
  - `region`
  - `location_name`
  - `country_tld`

## Map 1: Global Compute Accessibility

Save as: `Global Compute Accessibility`

### Layer order

Top to bottom:

1. `cloud_regions`
2. `ai_access_cities`

### Basemap

- `Light Gray Canvas`

### Symbology

`ai_access_cities`

- Style by `dist_km_nearest_region`
- Use `Counts and Amounts (Color)`
- Use 5 classes
- Reverse the color ramp if needed so lower distances read as better access and higher distances read as weaker access
- Set point transparency around 20 to 30 percent so dense corridors do not overpower the map

`cloud_regions`

- Use a single black or charcoal `X` or diamond marker
- Size about 8 to 10 px
- Keep the layer visually above the city layer

### Labels

- `ai_access_cities`: labels off
- `cloud_regions`: labels off at global scale; turn on `region` labels only if you need a zoomed-in presentation layer later

### Pop-up fields

`ai_access_cities`

- `city`
- `country`
- `iso2`
- `population`
- `dist_km_nearest_region`
- `access_score`
- `nearest_provider`
- `nearest_region`
- `nearest_location_name`
- `city_id`

`cloud_regions`

- `provider`
- `region`
- `location_name`
- `country_tld`

## Map 2: AI Research and Hot Spots

Save as: `AI Research and Hot Spots`

### Layer order

Top to bottom:

1. `cloud_regions`
2. `cities_with_hotspots`

### Basemap

- `Light Gray Canvas`

### Symbology

`cities_with_hotspots`

- Style by `hotspot_class`
- Use `Types (Unique symbols)`
- Assign the categories exactly as follows:
  - `hot_spot_99`: dark red
  - `hot_spot_95`: orange-red
  - `not_significant`: light gray with higher transparency
  - `cold_spot_95`: light blue
  - `cold_spot_99`: dark blue
- Make significant hot spots and cold spots slightly larger than `not_significant`

`cloud_regions`

- Use the same black or charcoal marker used in Map 1

### Labels

- `cities_with_hotspots`: labels off
- `cloud_regions`: labels off

### Pop-up fields

`cities_with_hotspots`

- `city`
- `country`
- `openalex_ai_works_recent`
- `openalex_ai_institution_count`
- `gi_star_z`
- `gi_star_p`
- `hotspot_class`
- `hotspot_rank`
- `dist_km_nearest_region`
- `access_score`
- `city_id`

`cloud_regions`

- `provider`
- `region`
- `location_name`

## Map 3: AI Deserts and Priority Cities

Save as: `AI Deserts and Priority Cities`

### Layer order

Top to bottom:

1. `cloud_regions`
2. `priority_cities`

### Basemap

- `Light Gray Canvas`

### Filter

Apply this filter to the map layer before styling:

- `priority_rank` is less than or equal to `100`

This keeps the map readable while still showing the highest-priority candidates.

### Symbology

`priority_cities`

- Style by `population`
- Use `Counts and Amounts (Size)`
- Keep one strong warning color such as dark orange or red-orange
- Add a thin white outline so overlapping points stay legible

`cloud_regions`

- Use the same marker as Maps 1 and 2

### Labels

- `priority_cities`: labels off in the default web map
- `cloud_regions`: labels off

### Pop-up fields

`priority_cities`

- `city`
- `country`
- `population`
- `dist_km_nearest_region`
- `priority_rank`
- `observed_ai_works_recent`
- `priority_rule`
- `priority_distance_threshold_km`
- `city_id`

`cloud_regions`

- `provider`
- `region`
- `location_name`

## Final QA before saving each web map

- Confirm the map title matches this guide exactly.
- Confirm the layer order matches this guide exactly.
- Confirm `cloud_regions` sits above the city layer.
- Open one popup and verify the listed fields are visible.
- Save the web map back into the same project folder used for the uploaded hosted layers.

## Checked against

- ArcGIS Online Help: Get started with Map Viewer
  - <https://doc.arcgis.com/en/arcgis-online/get-started/get-started-with-mv.htm>
- ArcGIS Online Help: Apply styles (Map Viewer)
  - <https://doc.arcgis.com/en/arcgis-online/create-maps/apply-styles-mv.htm>
- ArcGIS Online Help: Configure pop-ups (Map Viewer)
  - <https://doc.arcgis.com/en/arcgis-online/create-maps/configure-pop-ups-mv.htm>
