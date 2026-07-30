# NOVELTY_METHODS_MEMO.md — Originality & Methods Scouting

> Ranked menu of Harvard-accessible data sources and ArcGIS/Esri spatial methods that could make the EIP + Fisher submission more original and harder to replicate.
>
> **Cross-references:** This memo supports `AWARD_PLAYBOOK.md` (Section 2e: Originality checklist, Section 3: Originality weight) and `SUBMISSION_GAP_ANALYSIS.md` (Section 3: Originality Score). Winner patterns drawn from `WINNER_MATRIX.md`.

---

## 1. Harvard-Accessible Data Sources

| # | Source / Dataset | Access Route | Relevance to Project | Novelty Payoff | Feasibility |
|---|-----------------|-------------|---------------------|---------------|-------------|
| 1 | **ArcGIS Living Atlas of the World** | Harvard AGOL (harvard-cga.maps.arcgis.com) — free with HarvardKey | Curated global layers: demographics, imagery, environment, boundaries. Required for Esri StoryMaps competition; strongly valued for EIP. | Medium — widely available, but creative layer combinations add value. Use as foundation + supplement with unique data. | `high` |
| 2 | **Esri Business Analyst Data** | CGA lab (CGIS Knafel K026), packages from 2006–present | Demographic, consumer spending, segmentation, business locations (US). Enables market/equity analysis unavailable elsewhere. | High — few student projects use this; enables economic/demographic overlays most competitors lack. | `high` |
| 3 | **ArcGIS StreetMap Premium (SMP)** | CGA license (10 seats, contact CGA) | High-quality street network for geocoding + routing analytics globally. Enables network analysis at scale. | High — unlimited local geocoding/routing; enables origin-destination, service area, and accessibility analyses that are expensive elsewhere. | `medium` (limited seats, must request) |
| 4 | **Harvard Geospatial Library (HGL)** | geodata.lib.harvard.edu — free with HarvardKey | Thousands of vector/raster layers: historical maps, census, land use, environmental. Unique historical GIS datasets. | Medium-High — historical layers enable temporal analysis most competitors can't access. | `high` |
| 5 | **Harvard Map Collection** | Pusey Library — physical access + digitized collections | Rare historical maps, atlases, aerial photographs. Can be georeferenced for historical GIS overlay. | High — unique archival assets; [FIS-2024-UG-1] won by combining archival + modern GIS. | `medium` (requires digitization/georeferencing time) |
| 6 | **CGA Geotweet Archive v2.0** | Contact CGA — ~10 billion geo-located tweets (2010–July 2023) | Enables sentiment analysis, mobility patterns, event detection at global scale. Unique Harvard resource. | Very High — this is a rare, large-scale social media geodataset that almost no other university can offer at this scale. | `medium` (requires data request + processing infrastructure) |
| 7 | **Esri Demographic and Lifestyle Data** | CGA lab (2011–current) | Updated US demographic data at block group level. Enables social vulnerability, equity, and access analyses. | Medium — enriches any US-focused project with detailed demographics. | `high` |
| 8 | **Harvard FASRC (Research Computing)** | rc.fas.harvard.edu — free for Harvard affiliates | High-performance computing cluster for large spatial datasets, raster processing, ML workflows. ArcGIS Enterprise on HPC available. | Medium — enables analyses at scales (millions of records, high-resolution rasters) that desktop GIS cannot handle. | `high` (account setup required) |
| 9 | **Sentinel/Landsat Imagery via Living Atlas** | ArcGIS Living Atlas + ArcGIS Pro Image Analyst | Multispectral satellite imagery for land cover, NDVI, change detection. Free and current. | Medium — common in remote sensing projects but strong when combined with ground-truth or socioeconomic data. | `high` |
| 10 | **OpenStreetMap (OSM) + Overture Maps** | Public — download via Overpass API, ohsome, or Overture | Detailed building footprints, road networks, POIs globally. Especially rich in urban areas. | Low-Medium — widely available but large-scale OSM analysis (e.g., completeness audits, building morphology) can be novel. | `high` |
| 11 | **ERDAS IMAGINE / ENVI** | CGA site license | Professional remote sensing: image classification, spectral analysis, LiDAR processing. | Medium — enables advanced remote sensing workflows beyond ArcGIS built-in tools. | `high` |
| 12 | **TerrSet (IDRISI)** | CGA site license | Land change modeling, ecosystem service valuation, climate change analysis. Includes Land Change Modeler. | Medium-High — land change modeling is a distinctive analytical capability judges notice. | `high` |

---

## 2. ArcGIS / Esri Spatial Analysis Techniques

| # | Method / Tool | Required License / Data | Expected Output | Narrative Value for Submission | Feasibility |
|---|--------------|------------------------|----------------|-------------------------------|-------------|
| 1 | **Hot Spot Analysis (Getis-Ord Gi*)** | ArcGIS Pro (Spatial Statistics toolbox) — included in Harvard license | Statistically significant clusters of high/low values | Demonstrates spatial statistics beyond basic mapping; judges reward "robust statistical analysis." [EIP-2025-1] | `high` |
| 2 | **Emerging Hot Spot Analysis** | ArcGIS Pro (Space Time Pattern Mining) | Space-time cubes showing where clusters are new, intensifying, persistent, or diminishing | Adds temporal dimension to spatial patterns; visually compelling animations; rare in student work. | `high` |
| 3 | **Optimized Hot Spot / Cluster and Outlier** | ArcGIS Pro (Spatial Statistics) | Automated identification of statistically significant patterns without parameter tuning | Quick analytical win that looks sophisticated; good for validating visual patterns. | `high` |
| 4 | **Network Analysis (Service Area, OD Matrix, Route)** | ArcGIS Pro Network Analyst + StreetMap Premium or OSM network | Accessibility zones, travel time matrices, optimal routes | Directly relevant to equity, planning, and access studies. [FIS-2025-G-1] analyzed "every street in Boston." | `high` (with SMP license) |
| 5 | **Suitability Analysis (Weighted Overlay)** | ArcGIS Pro Spatial Analyst | Composite suitability index maps | Clear, actionable output for planning/policy; [EIP-2019-1] used suitability for solar pump placement. | `high` |
| 6 | **Geographically Weighted Regression (GWR)** | ArcGIS Pro (Spatial Statistics) | Spatially varying coefficients showing where relationships are stronger/weaker | Sophisticated statistical-spatial integration; demonstrates that "one model doesn't fit everywhere." | `medium` (requires solid regression setup) |
| 7 | **Location-Allocation Analysis** | ArcGIS Pro Network Analyst | Optimal facility placement / resource allocation scenarios | Strong policy narrative: "where should X be located to serve the most people?" | `medium` (requires network dataset + demand data) |
| 8 | **3D Visualization / ArcGIS Urban / CityEngine** | ArcGIS Pro 3D Analyst; CityEngine (separate license via CGA) | 3D scenes, urban build-out scenarios, viewshed analysis | High visual impact; [EIP-2024-1] won with 3D build-out analysis. Judges noted it as a differentiator. | `medium` (CityEngine license availability) |
| 9 | **Image Classification (Supervised/Unsupervised)** | ArcGIS Pro Image Analyst or ERDAS | Land cover maps, change detection products | Demonstrates remote sensing skill; strong when combined with ground-truth validation. | `high` |
| 10 | **GeoAI / Deep Learning for Object Detection** | ArcGIS Pro (GeoAI toolbox) + GPU access (FASRC) | Automated feature extraction from imagery (buildings, damage, vegetation) | Cutting-edge; very few student projects use GeoAI. High originality signal but requires technical skill. | `low` (steep learning curve, GPU needed) |
| 11 | **Space-Time Pattern Mining (Space-Time Cube)** | ArcGIS Pro | Temporal trends in spatial data; animations showing change | Combines time + space in ways that static maps cannot. Visually compelling in StoryMaps. | `medium` (requires temporal data) |
| 12 | **Visibility / Viewshed Analysis** | ArcGIS Pro 3D Analyst + DEM data | Viewshed maps showing what is visible from given locations | Niche but powerful for landscape, planning, or conservation projects. | `high` |

---

## 3. Originality Packages (5)

Each package = data + method + story payoff + risk.

### Package A: "Access Equity Mapper" — Network-based service access disparities

- **New question answered:** Where are the largest gaps in equitable access to [health/transit/education/green space] when measured by actual travel time rather than straight-line distance?
- **Data needed:** StreetMap Premium (Harvard CGA license) + demographic data (Esri Business Analyst or Census) + facility locations (POIs from Living Atlas or custom)
- **Tool / method:** Network Analyst (Service Area + OD Cost Matrix) → Getis-Ord hot spot analysis on access gaps → GWR to model demographic predictors of poor access
- **Why harder to replicate:** StreetMap Premium license enables unlimited local network routing that public AGOL credits can't match at scale. Multi-method chain (network + statistics + regression) is unusual.
- **Why it helps EIP/Fisher specifically:** Combines 3 GIS techniques (judged as "breadth of GIS spectrum"), produces policy-relevant output (judged as "practical use to policy makers"), and uses Esri technology explicitly (EIP criterion).
- **Risk / feasibility note:** Medium risk. Network analysis setup takes time but is well-documented. Feasibility: `high` with SMP license.

### Package B: "Temporal Pulse" — Emerging hot spot analysis of a dynamic phenomenon

- **New question answered:** How are spatial patterns of [crime/disease/environmental change/displacement] evolving over time, and where are new clusters emerging vs. fading?
- **Data needed:** Time-stamped point or polygon data (≥12 time steps) + contextual layers from Living Atlas
- **Tool / method:** Space-Time Cube → Emerging Hot Spot Analysis → space-time visualization in StoryMap (animation or slider)
- **Why harder to replicate:** Space-time pattern mining is rarely used in student projects; the animated output in a StoryMap is visually distinctive and analytically rigorous.
- **Why it helps EIP/Fisher specifically:** Demonstrates advanced Esri-specific capability (Space Time Pattern Mining toolbox); temporal analysis is praised in winners like [FIS-2023-G-1] (pre/post-war Mariupol).
- **Risk / feasibility note:** Medium risk. Requires well-structured temporal data. If data has <8 time steps, results may be statistically thin. Feasibility: `medium`.

### Package C: "Archive Overlay" — Historical GIS with Harvard Map Collection

- **New question answered:** How has [land use/urban form/environmental boundary/settlement pattern] changed over [decades/century] when measured by georeferencing archival maps against modern data?
- **Data needed:** Historical maps from Harvard Map Collection (georeferenced) + modern imagery/data from Living Atlas or HGL
- **Tool / method:** Georeferencing in ArcGIS Pro → change detection (raster difference or classification comparison) → swipe map in StoryMap
- **Why harder to replicate:** Harvard Map Collection is a unique institutional asset; the combination of archival + modern data won the 2024 Fisher UG prize ([FIS-2024-UG-1]).
- **Why it helps EIP/Fisher specifically:** Judges praised "impressive compilation of historic maps, images, and archival documents efficiently processed with modern GIS tools." This package directly replicates a winning formula.
- **Risk / feasibility note:** Medium risk. Georeferencing quality depends on map condition. Requires physical visit to Map Collection + digitization time. Feasibility: `medium`.

### Package D: "Social Sensing" — Geotweet Archive for spatial sentiment/mobility

- **New question answered:** How did public attention or mobility patterns shift spatially during/after [event/policy/disaster], as measured by geolocated social media?
- **Data needed:** CGA Geotweet Archive (2010–2023) + contextual layers
- **Tool / method:** Text/sentiment analysis (Python) → point-in-polygon aggregation → hot spot analysis → space-time cube for temporal evolution
- **Why harder to replicate:** The CGA Geotweet Archive is a unique Harvard resource (~10 billion tweets). No other student at another university can easily access this dataset.
- **Why it helps EIP/Fisher specifically:** Unique data access is the strongest originality signal. Combines novel data with established Esri spatial methods. Judges reward "innovation" and "originality" explicitly.
- **Risk / feasibility note:** Higher risk. Requires data access approval, significant processing (FASRC recommended), and NLP skills. Feasibility: `low-medium`.

### Package E: "Predictive Landscape" — Suitability + statistical validation for site selection

- **New question answered:** Where are the optimal locations for [renewable energy/conservation corridors/emergency facilities/urban greening] based on multi-criteria spatial analysis validated by statistical modeling?
- **Data needed:** Multiple environmental/demographic/infrastructure layers from Living Atlas + HGL + Esri demographic data
- **Tool / method:** Weighted overlay (Suitability Analyst) → logistic regression or GWR validation → sensitivity analysis → location-allocation optimization
- **Why harder to replicate:** The three-step chain (suitability → statistical validation → optimization) is more rigorous than typical student suitability studies. Adding statistical validation lifts it from "GIS exercise" to "analytical contribution."
- **Why it helps EIP/Fisher specifically:** Directly mirrors the EIP criteria ("potential impact," "innovation," "implementation"). [EIP-2019-1] won with a suitability analysis for solar pumps; this package adds statistical rigor.
- **Risk / feasibility note:** Low-Medium risk. Well-documented workflows exist. Feasibility: `high`.

---

## 4. Do-Not-Chase List

> Impressive-sounding ideas that are **misaligned** with the EIP + Fisher judging priorities or **infeasible** within the project timeline.

| # | Idea | Why It Looks Tempting | Why to Avoid |
|---|------|----------------------|-------------|
| 1 | **Full deep learning / GeoAI pipeline** | Cutting-edge; sounds impressive in abstract | Steep learning curve; GPU access needed; if the model doesn't converge or validate, you have nothing. Judges value "appropriate" methods ([EIP-2024-1]), not necessarily the most complex. A failed ML model scores worse than a clean suitability analysis. |
| 2 | **Building a custom web app from scratch** | Shows coding skill | EIP/Fisher judge GIS and cartography, not web development. A clean ArcGIS StoryMap with embedded web maps is more aligned than a buggy custom app. Time spent coding is time not spent on analysis. |
| 3 | **Massive global-scale analysis** | "I analyzed every country" sounds impressive | Judges prefer specific, well-scoped projects. [EIP-2025-1] focused on one Kenyan county; [FIS-2025-G-1] on one city. Global analyses risk being superficial and losing the human-scale narrative judges reward. |
| 4 | **Drone data collection** | Original data = maximum novelty | Regulatory, scheduling, and processing overhead is enormous. If the drone flight fails or weather is bad, the project stalls. Use existing high-resolution imagery instead. |
| 5 | **VR/AR integration** | Immersive, cutting-edge | ArcGIS StoryMaps don't natively support VR. Judges evaluate what's in the StoryMap/poster, not a separate VR experience. Misaligned with submission format. |
| 6 | **Esoteric data sources requiring multi-month access approvals** | "No one else has this data" | If the approval takes longer than your timeline, you have no data. Prefer Harvard-accessible sources with established access routes. |
| 7 | **Pure remote sensing without ground truth or context** | Satellite imagery looks professional | Judges want to see data "relevance to topic" and "properly documented" context. A land cover classification without any socioeconomic or policy framing will score low on Framing and Interpretation. |

---

## 5. BLOCKERS

| # | What Is Missing | What Is Needed |
|---|----------------|----------------|
| 1 | Current project topic and existing analysis artifacts not yet reviewed in this memo. | User to provide current project description, StoryMap draft, and existing analysis outputs so that originality packages can be tailored and ranked specifically for the submission. |
| 2 | CGA Geotweet Archive access status unknown. | Confirm with CGA whether archive access is available and what the request timeline is. |
| 3 | StreetMap Premium license availability for current year. | Confirm with CGA that SMP licenses are renewed for 2025–2026 and a seat is available. |
