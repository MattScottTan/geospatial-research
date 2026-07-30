# Cloudy with a Chance of Compute — Final Submission Package

**Author:** Matthew Scott Tan, Harvard College
**StoryMap:** https://storymaps.arcgis.com/stories/744a1c433d554cef8b3861d72836fdd2
**Awards:** Harvard CGA EIP Student of the Year + Fisher Prize

---

## Directory Structure

### /data
Raw and processed data files:
- `bundle_city_scores.csv` — 8,000 cities with all five bundle component scores (the key analytical dataset)
- `city_access_ai.csv` — 328 AI-linked cities matched from OpenAlex
- `worldcities.csv` — raw city data from Natural Earth
- `cloud_regions_aws/azure/gcp.csv` — raw cloud region data by provider
- `openalex_ai_city_overlay.csv` — AI publication overlay data
- `openalex_ai_institutions_top.csv` — top AI research institutions
- `ne_110m_admin_0_countries.geojson` — country boundaries
- `cross_case_table.csv` — four case study comparison data

### /gis
GIS-ready layers for ArcGIS Online / ArcGIS Pro:
- `ai_access_cities.geojson` — 8,000 cities with distance-to-cloud (uploaded to ArcGIS Online)
- `cities_with_hotspots.geojson` — 319 AI cities with Gi* classifications (uploaded)
- `cloud_regions.geojson` — 111 cloud regions with provider info (uploaded)
- `priority_cities.geojson` — 1,988 priority cities (uploaded)
- `*.gpkg` — GeoPackage versions of the same layers

### /scripts
Python analysis pipeline:
- `pipeline.py` — main 3,369-line analysis pipeline generating all figures
- `build_prototypes.py` — bundle index and originality figure generation
- `build_case_maps.py` — case study map generation

### /figures
All pipeline-generated figures (fig1–fig14, bundle figures, Moran's I scatterplot, counterfactual analysis)

### /case_studies
Case study images: regional context maps and local ecosystem charts for Singapore, Dublin (Seoul in older version), Ho Chi Minh City, Lagos

### /documents
Project planning documents:
- `Cloudy_with_a_Chance_of_Compute.pdf` — latest StoryMap PDF (March 25, 2026)
- `AWARD_PLAYBOOK.md` — weighted rubric and submission checklist
- `WINNER_MATRIX.md` — 18 past EIP/Fisher winner analysis
- `SUBMISSION_GAP_ANALYSIS.md` — rubric scorecard and gap analysis
- `ARCGIS_FINAL_INSTRUCTIONS.md` — click-by-click ArcGIS map build instructions
- `PROOFREAD_AND_WRITING_FIXES.md` — all text edits with find/replace
- `SOURCES_CREDITS_TOOLS.md` — ready-to-paste sources section
- Plus: revision checklist, hero map instructions, spatial stats instructions, handoff docs

---

## ArcGIS Online Hosted Layers
- `ai_access_cities` — 8,000 cities, distance-colored
- `cloud_regions` — 111 cloud regions, diamond by provider
- `cities_with_hotspots` — 319 AI cities, Gi* hot/cold classification
- `priority_cities` — 1,988 underserved cities
- `bundle_city_scores` — 8,000 cities with bundle index scores

## ArcGIS Online Web Maps
- Global Compute Accessibility (hero map)
- AI Research Hot Spots and Cold Spots (Gi*)
- Priority Cities — AI Compute Access Gaps
- Compute Opportunity Bundle Index
- Cloudy with a Chance of Compute — Interactive Atlas (consolidated, multi-layer)

## Key Statistics
- 8,000 cities in frame, 328 AI-linked, 319 unique for spatial diagnostics
- 111 cloud regions across AWS, Azure, Google Cloud
- Moran's I = 0.066, z = 2.86, p = 0.008
- 7 Gi* hot spots, 33 cold spots
- 1,988 priority cities across 125 countries
- Bundle index: proximity (40%), provider diversity (15%), redundancy (15%), urban scale (15%), institutional depth (15%)
