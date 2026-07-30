# Web Map Specs

These are the required ArcGIS Online web maps for the final StoryMap. Local analysis and figure generation can be completed without login, but the hosted-layer and web-map steps require ArcGIS Online access. A Harvard ArcGIS Online account is the expected path for manual publication.

## 1. Global Compute Accessibility

- **Purpose:** hero map for Hook and atlas methods
- **Required layers:** `cloud_regions`, `ai_access_cities`
- **Basemap:** Light Gray Canvas
- **Primary symbology:** `ai_access_cities` styled by `dist_km_nearest_region`
- **Popup fields:** city, country, population, distance to nearest region, nearest provider, nearest region
- **Legend intent:** shorter distance = stronger compute access
- **Login required for build/share:** Yes (ArcGIS Online)

## 2. AI Research and Hot Spots

- **Purpose:** show observed AI overlay and local clustering pattern
- **Required layers:** `cloud_regions`, `cities_with_hotspots`
- **Basemap:** Light Gray Canvas
- **Primary symbology:** `hotspot_class` unique values (`hot_spot_99`, `hot_spot_95`, `not_significant`, `cold_spot_95`, `cold_spot_99`)
- **Popup fields:** city, country, AI works, hotspot class, Gi* z-score, compute distance
- **Legend intent:** visible statistical structure, not all-or-nothing clustering
- **Login required for build/share:** Yes (ArcGIS Online)

## 3. AI Deserts and Priority Cities

- **Purpose:** screening-layer map for the policy-facing part of the story
- **Required layers:** `cloud_regions`, `priority_cities`
- **Basemap:** Light Gray Canvas
- **Primary symbology:** priority cities sized by population, optionally filtered to `priority_rank <= 100` for web readability
- **Popup fields:** city, country, population, distance to nearest region, priority rank, observed AI works
- **Legend intent:** large-city mismatch between urban scale and compute proximity
- **Login required for build/share:** Yes (ArcGIS Online)

## 4. Originality and case-study media

The originality section and the four case-study modules can be delivered as static images prepared locally. They do **not** require hosted web maps unless the user chooses to create optional interactive variants later.

## Manual-login note

A Harvard ArcGIS Online account should be sufficient for:
- hosted-layer upload
- web-map assembly in Map Viewer
- StoryMap assembly in ArcGIS StoryMaps
- public sharing configuration and signed-out QA

ArcGIS Pro, StreetMap Premium, and Business Analyst are optional enhancements, not required to publish the final StoryMap package prepared here.
