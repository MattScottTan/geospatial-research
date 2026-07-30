# WORK.md — AI Compute Accessibility Atlas → EIP Award Submission

---

# 0. Snapshot

- **Job Type:** Mixed (Research/Synthesis + Code/Engineering + Writing/Exposition)
- **Primary Deliverables:**
  1. Improved `src/pipeline.py` with added spatial statistics (Moran's I, Getis-Ord Gi*, spatial accessibility indices)
  2. Rebuilt figure set with publication-quality cartography (exported as high-res PNGs + vector formats for StoryMap)
  3. Rewritten `report/main.tex` with policy-actionable framing, stronger research questions, and deeper regional case studies
  4. Full **ArcGIS StoryMap content blueprint** (section-by-section script with exact text, map specs, interactive element specs, and embed instructions)
  5. ArcGIS-ready data package: hosted feature layers (GeoJSON/CSV → ArcGIS Online), web maps, and dashboard spec
  6. Submission-ready StoryMap (published, public-sharing enabled, all required elements per EIP guidelines)
- **Stakeholders / Audience:** EIP judges (GIS professionals evaluating: potential impact, innovation, originality, implementation, organization)
- **Constraints:**
  - **Deadline:** Sunday March 15, 2026 at 11:59 PM EDT
  - **Format:** ArcGIS StoryMap (public, no NDA content)
  - **Required StoryMap elements:** Short bio + professional photo, description of achievement, project using Esri technology, maps/narrative/apps/video/graphics/charts
  - **Esri skill level:** Beginner — all Esri instructions must be step-by-step
  - **Pipeline:** `src/pipeline.py` runs end-to-end; worker can modify and rerun
  - **Time budget:** ~30+ hours across 5 days
  - **The ZIP file with full repo will be uploaded by user — worker should inspect it first**

---

# 1. Goal

Transform the existing AI Compute Accessibility Atlas from an academic LaTeX report with matplotlib figures into an award-winning EIP submission. This means: (a) strengthening the spatial analysis with Esri-native statistics alongside the existing GP/CAR models, (b) rebuilding all cartographic outputs to professional quality, (c) reframing the narrative around policy-actionable research questions with the "AI deserts" concept as the central hook, (d) packaging everything into a compelling ArcGIS StoryMap with interactive maps and a clear narrative arc. The project must demonstrate command of the Esri toolkit while preserving the analytical depth that is its core differentiator.

## Definition of Done (verifiable checklist)

- [ ] `src/pipeline.py` (or modular scripts) runs end-to-end and produces all new outputs
- [ ] Moran's I global spatial autocorrelation computed and reported for AI works distribution
- [ ] Getis-Ord Gi* hot spot analysis computed and mapped for AI research clusters
- [ ] At least one spatial accessibility index (e.g., distance-decay weighted, or 2SFCA-inspired) computed beyond raw great-circle distance
- [ ] Research questions rewritten: at least one explicitly policy-actionable (identifies priority cities for compute investment)
- [ ] "AI deserts" elevated to central narrative hook with dedicated analysis section
- [ ] At least 2 regional deep-dive case studies developed (Sub-Saharan Africa + one other)
- [ ] All figures (minimum 10) rebuilt with professional cartographic standards: consistent color palette, scale bars, north arrows, legends, projection-appropriate basemaps, no matplotlib defaults
- [ ] A "priority cities" recommendation layer exists: cities ranked by research capacity relative to compute isolation
- [ ] All data uploaded to ArcGIS Online as hosted feature layers (cities, cloud regions, AI overlay, mismatch quadrants, hot spots)
- [ ] At least 3 interactive web maps built in ArcGIS Online (global overview, AI deserts focus, hot spot clusters)
- [ ] StoryMap built and published with public sharing, containing: bio+photo placeholder, all narrative sections, embedded interactive maps, charts/graphics, Esri technology callouts
- [ ] StoryMap narrative follows hook → context → data → methods → results → implications arc
- [ ] References expanded: at least 3 new citations from GIS/spatial accessibility literature
- [ ] Limitations section updated to reflect new analysis
- [ ] `report/main.tex` updated to match StoryMap content (parallel deliverable)

## Non-goals

- We are NOT building a real-time dashboard or live data feed
- We are NOT performing causal inference — the project remains associational (but frames this as a feature, not a limitation)
- We are NOT replacing the GP/CAR models — we are supplementing them with Esri-native spatial statistics
- We are NOT creating a mobile app or custom web application beyond the StoryMap
- We are NOT collecting new primary data — all improvements use existing datasets

---

# 2. Acceptance Checks

## Research / Analysis
- [ ] Moran's I output includes: I statistic, z-score, p-value, and interpretation sentence
- [ ] Gi* hot spot map shows statistically significant clusters (90%, 95%, 99% confidence) with proper symbology
- [ ] Priority cities list is reproducible: clear methodology for ranking (e.g., composite score = normalized research capacity / normalized compute distance)
- [ ] All statistical claims in the narrative have supporting numbers (coefficients, p-values, descriptive stats)
- [ ] New accessibility index is documented: formula, inputs, interpretation, and comparison to raw distance

## Writing / Exposition
- [ ] Opening section of StoryMap hooks within first scroll: a striking "AI desert" statistic or city profile
- [ ] Every section of the StoryMap names at least one specific stakeholder who would use the finding
- [ ] Research questions appear early and are answered explicitly in the results
- [ ] Esri technologies used are named explicitly in at least 3 places in the narrative
- [ ] Tone is accessible to a policy audience, not just academics — no unexplained jargon
- [ ] The report does NOT read like a dry academic paper — it reads like a policy brief with a narrative arc
- [ ] "AI deserts" concept is introduced within the first 2 scrolls of the StoryMap
- [ ] At least 2 regional case studies have 3+ paragraphs each with region-specific maps

## Code / Engineering
- [ ] Pipeline produces all new outputs (Gi* results, Moran's I, priority scores, improved figures) without manual steps
- [ ] All GeoJSON/GeoPackage exports are ArcGIS Online compatible (WGS84, clean field names, no special characters)
- [ ] Figure exports are minimum 300 DPI PNG (for StoryMap embedding) with transparent or white backgrounds
- [ ] Color palette is consistent across ALL figures (same ramp for distance, same categorical scheme for quadrants)
- [ ] Every figure has: title, legend, scale bar (for maps), source attribution

## Esri / StoryMap
- [ ] All feature layers are hosted on ArcGIS Online and publicly shared
- [ ] Web maps have popups configured (city name, AI works, distance to compute, nearest provider, quadrant)
- [ ] StoryMap uses at least 3 different StoryMap block types (sidecar, swipe, map tour, embed, etc.)
- [ ] StoryMap is accessible at a public URL
- [ ] StoryMap includes required elements: bio, photo placeholder, project description, Esri tech used

---

# 3. Plan

## Approach Summary
1. **Inspect repo** — Audit all existing files, understand pipeline structure, identify what outputs exist
2. **Strengthen analysis** — Add Moran's I, Getis-Ord Gi*, spatial accessibility index, and priority city ranking to pipeline
3. **Reframe narrative** — Rewrite research questions, elevate AI deserts, develop case studies, add policy framing
4. **Rebuild figures** — Replace all matplotlib defaults with professional cartography (consistent palette, proper elements, high-res export)
5. **Prepare ArcGIS data** — Export clean GeoJSON/CSV for upload to ArcGIS Online, document upload steps
6. **Build StoryMap blueprint** — Section-by-section script with exact text, map specifications, and layout instructions
7. **Build StoryMap** — Upload data to ArcGIS Online, create web maps, assemble StoryMap (user executes with step-by-step guide)
8. **Polish and submit** — Final review pass against rubric, fix gaps, publish StoryMap, register

## Dependencies / Ordering Logic
- Tasks 1-2 (inspect + analysis) must happen before Tasks 4-5 (figures + ArcGIS data)
- Task 3 (narrative) can happen in parallel with Task 2 but must be finalized after analysis results are known
- Task 5 (ArcGIS data prep) must happen before Task 6-7 (StoryMap)
- Task 8 (polish) is always last
- **BLOCKER:** User must upload the ZIP repo before Task 1 can begin

## Risk & Mitigation
| Risk | Mitigation |
|------|-----------|
| Beginner Esri skills slow StoryMap build | Every Esri step has explicit click-by-click instructions; use ArcGIS Online (browser) over Pro where possible |
| Pipeline changes break existing outputs | Git commit before any changes; run full pipeline after each modification |
| Moran's I / Gi* requires spatial weights matrix that's hard to construct for global city data | Use k-nearest-neighbors (k=8) or distance-band weights; PySAL handles this |
| ArcGIS Online upload fails for large datasets | Pre-filter to essential columns; split if >1000 features per layer if needed |
| StoryMap takes longer than expected | Build minimum viable StoryMap first (3 sections, 3 maps), then add depth iteratively |
| Figures don't match between LaTeX report and StoryMap | Single figure-generation pipeline; export both PNG (StoryMap) and PDF (LaTeX) from same code |
| March 15 deadline crunch | Prioritize: StoryMap > figures > analysis > LaTeX report (the StoryMap IS the submission) |

---

# 4. Tasks

## Track A: Repo Inspection & Setup [BLOCKED until ZIP uploaded]

- [ ] **[A1] Inspect uploaded ZIP repo structure**
  - Unzip and catalog all files: `src/`, `outputs/`, `data/`, `report/`
  - Record: which scripts exist, what data files are present, what outputs are already generated
  - Done when: File tree documented in Learnings section below
  - Inputs: User-uploaded ZIP file

- [ ] **[A2] Run pipeline.py and verify all outputs regenerate**
  - Execute `src/pipeline.py` end-to-end
  - Verify outputs match what's described in the PDF (figures 1-10, tables 1-5, GIS exports)
  - Record any errors or missing dependencies
  - Done when: Pipeline runs cleanly OR all errors documented with fixes
  - Inputs: A1 complete

- [ ] **[A3] Audit existing data quality**
  - Check: How many cities in worldcities.csv? How many in OpenAlex overlay? Match rate?
  - Check: Cloud region coordinates — are all 111 regions (29 AWS + 47 Azure + 35 GCP) present?
  - Check: What CRS are GIS exports in? Are field names clean for ArcGIS Online?
  - Done when: Data quality summary written in Learnings
  - Inputs: A1 complete

## Track B: Statistical Analysis Improvements

- [ ] **[B1] Add Global Moran's I for AI works distribution**
  - Use PySAL (`esda.Moran`) or `libpysal` to compute Moran's I on log(1 + AI works) across the 328 AI-city overlay
  - Spatial weights: k-nearest-neighbors (k=8) using city coordinates
  - Output: I statistic, z-score, p-value, and a Moran scatterplot (saved as figure)
  - Save results to `outputs/tables/morans_i_summary.csv`
  - Done when: Moran's I computed, scatterplot saved, results interpretable (expect significant positive spatial autocorrelation)
  - Inputs: A2, A3 complete
  - **Implementation notes for worker:**
    ```python
    # Install: pip install esda libpysal splot
    from esda.moran import Moran
    from libpysal.weights import KNN
    import numpy as np
    
    # Build weights from city coordinates
    coords = np.column_stack([cities['lng'], cities['lat']])
    w = KNN.from_array(coords, k=8)
    w.transform = 'r'  # row-standardize
    
    # Compute Moran's I
    y = np.log1p(cities['ai_works'])
    mi = Moran(y, w)
    print(f"Moran's I: {mi.I:.4f}, z-score: {mi.z_sim:.4f}, p-value: {mi.p_sim:.4f}")
    
    # Moran scatterplot
    from splot.esda import moran_scatterplot
    fig, ax = moran_scatterplot(mi, aspect_equal=False)
    fig.savefig('outputs/figures/morans_i_scatterplot.png', dpi=300, bbox_inches='tight')
    ```

- [ ] **[B2] Add Getis-Ord Gi* Hot Spot Analysis**
  - Use PySAL (`esda.getisord.G_Local`) to compute local Gi* statistics for AI works
  - Spatial weights: distance-band (use median nearest-neighbor distance as bandwidth) or fixed k=8
  - Classify results into: hot spot (99%, 95%, 90%), not significant, cold spot (90%, 95%, 99%)
  - Save Gi* z-scores and p-values as new columns in the city GeoDataFrame
  - Export updated GeoJSON to `outputs/gis/cities_with_hotspots.geojson`
  - Done when: Gi* column added, classification column added, GeoJSON exported
  - Inputs: A2 complete
  - **Implementation notes for worker:**
    ```python
    from esda.getisord import G_Local
    
    # Gi* requires binary or distance weights
    w = KNN.from_array(coords, k=8)
    w.transform = 'b'  # binary for Gi*
    
    y = cities['ai_works'].values.astype(float)
    gi = G_Local(y, w, star=True, permutations=999)
    
    cities['gi_zscore'] = gi.Zs
    cities['gi_pvalue'] = gi.p_sim
    
    # Classify
    def classify_hotspot(z, p):
        if p <= 0.01 and z > 0: return 'Hot Spot (99%)'
        if p <= 0.05 and z > 0: return 'Hot Spot (95%)'
        if p <= 0.10 and z > 0: return 'Hot Spot (90%)'
        if p <= 0.01 and z < 0: return 'Cold Spot (99%)'
        if p <= 0.05 and z < 0: return 'Cold Spot (95%)'
        if p <= 0.10 and z < 0: return 'Cold Spot (90%)'
        return 'Not Significant'
    
    cities['hotspot_class'] = [classify_hotspot(z, p) for z, p in zip(gi.Zs, gi.p_sim)]
    ```

- [ ] **[B3] Compute enhanced spatial accessibility index**
  - Go beyond raw great-circle distance. Compute a distance-decay accessibility score:
    `A_i = Σ_j (capacity_j * f(d_ij))` where j = cloud regions, d_ij = distance, f() = inverse-power or Gaussian decay
  - Since we don't have capacity data, use a count-based proxy: number of cloud regions within distance bands (100km, 500km, 1000km) as a "compute density" measure
  - Also compute: minimum distance across ALL providers (existing), minimum distance PER provider (AWS, Azure, GCP separately), and number of distinct providers within 500km
  - Save as new columns in city GeoDataFrame
  - Done when: At least 3 new accessibility metrics computed and added to city data
  - Inputs: A2 complete

- [ ] **[B4] Build priority city ranking ("Compute Investment Priority Index")**
  - Create a composite score that identifies cities with HIGH research capacity but LOW compute access
  - Formula: `priority_score = normalized_ai_works * normalized_compute_distance`
    - Where normalized_ai_works = percentile rank of log(1+ai_works) among all cities with ai_works > 0
    - Where normalized_compute_distance = percentile rank of distance (higher distance = higher score)
  - Also create a variant for the full 8,000 city frame: `potential_score = normalized_population * normalized_compute_distance` (identifies large cities that are compute-isolated regardless of current AI output)
  - Rank and list top 20 for each
  - Save to `outputs/tables/priority_cities.csv`
  - Done when: Two ranked city lists produced, methodology documented, CSV exported
  - Inputs: A2 complete

- [ ] **[B5] Compute per-provider distance layers**
  - For each city, compute distance to nearest AWS region, nearest Azure region, and nearest GCP region separately
  - Identify which provider is nearest and by how much (the "provider gap": distance to 2nd nearest provider minus distance to nearest)
  - This enables a "provider diversity" analysis: some cities may be close to one provider but far from all others
  - Save as new columns in city GeoDataFrame
  - Done when: Three per-provider distance columns + provider gap column added
  - Inputs: A2 complete

## Track C: Narrative & Research Question Reframing

- [ ] **[C1] Rewrite research questions**
  - Replace current 4 questions with 5 revised questions that are policy-actionable:
    1. How uneven is compute accessibility across the global system of large cities, and which regions face the greatest infrastructure deficit?
    2. Are AI research hubs systematically closer to hyperscaler compute than other large cities, and how large is this proximity gap?
    3. After controlling for city size and spatial clustering, does distance to compute carry an interpretable negative association with AI research output?
    4. Where are the global "AI deserts" — cities where large populations, weak compute access, and low AI research output converge — and what characterizes them?
    5. Which cities represent the highest-priority candidates for new cloud infrastructure investment based on their research capacity relative to their compute isolation?
  - Done when: 5 questions written, each with a clear "who would use this answer" stakeholder identified
  - Inputs: None (can start immediately)
  - Where: `report/main.tex` Section 1.1 AND StoryMap blueprint

- [ ] **[C2] Write the "AI Deserts" narrative section**
  - This becomes the emotional and policy anchor of the project
  - Structure:
    - Open with a specific city profile (e.g., Lagos: 15M people, 3,843 km from nearest cloud region, zero AI papers in overlay)
    - Define "AI desert" precisely: a city in the bottom quartile of compute accessibility AND the bottom quartile of AI research output (or zero output)
    - List and map all AI desert cities from the data
    - Connect to broader digital divide literature
    - Frame the policy implication: these cities face compounding disadvantages
  - Done when: 4-6 paragraphs written, at least 5 specific cities profiled with data
  - Inputs: B4 complete (for priority rankings), A3 complete (for data verification)
  - Where: New section in report + StoryMap section 4 (see blueprint)

- [ ] **[C3] Develop Sub-Saharan Africa regional deep-dive**
  - Focus on: Lagos, Nairobi, Kinshasa, Dar es Salaam, Addis Ababa, Abidjan (all in Table 4)
  - Content:
    - Map of the region showing cloud region locations (nearest: South Africa North for most), city positions, and distance lines
    - The nearest cloud region for most of these cities is Azure South Africa North (Johannesburg) — but that's 2,400-3,900 km away
    - Discuss the "single point of access" problem: these cities depend on one region in one country
    - Note any announced datacenter investments (e.g., Google/AWS African expansion)
    - Connect to the broader narrative: Africa has ~1.4B people and minimal hyperscaler presence
  - Done when: 3-5 paragraphs + dedicated regional map spec written
  - Inputs: A3, web search for recent African cloud infrastructure announcements
  - Where: New subsection in report + StoryMap section 5

- [ ] **[C4] Develop Latin America regional deep-dive**
  - Focus on: Lima, Bogotá, and contrast with São Paulo (which likely has nearby compute)
  - Content:
    - Map showing cloud regions in South America (São Paulo region exists; most of continent is far)
    - The Andean and Central American corridor: compute isolation despite large urban populations
    - Contrast with the connected Southern Cone (Buenos Aires, Santiago)
  - Done when: 3-5 paragraphs + dedicated regional map spec written
  - Inputs: A3
  - Where: New subsection in report + StoryMap section 5

- [ ] **[C5] Rewrite Discussion section with policy-forward framing**
  - Structure:
    - Lead with the headline: "AI compute inequality is measurable, mappable, and concentrated in predictable ways"
    - State the 3 main findings as actionable insights (not hedged conclusions)
    - Name specific stakeholders: OECD, World Bank, national AI strategy offices, cloud providers doing expansion planning, development finance institutions
    - Frame the priority city ranking as a tool these stakeholders can use
    - THEN add the caveats (associational not causal, overlay limitations, distance ≠ latency)
    - End with a forward-looking paragraph: as sovereign compute initiatives expand, this atlas provides a baseline for measuring progress
  - Done when: Discussion rewritten, at least 3 specific stakeholder organizations named, caveats preserved but repositioned
  - Inputs: B4 complete
  - Where: `report/main.tex` Section 5 AND StoryMap section 7

- [ ] **[C6] Expand references with GIS / spatial accessibility literature**
  - Add at minimum:
    - Luo & Wang (2003) or Luo & Qi (2009) — two-step floating catchment area method (foundational spatial accessibility)
    - Grubesic (2006) or Prieger (2013) — digital divide / broadband access geography
    - Anselin (1995) — Local Indicators of Spatial Association (LISA) (foundational for Moran's I / Gi*)
    - At least one Esri-affiliated publication or methodology reference (e.g., Esri's documentation on hot spot analysis best practices)
    - At least one recent paper on AI infrastructure geography or sovereign compute (search for 2024-2025 publications)
  - Done when: At least 5 new references added to bibliography, each cited at least once in the text
  - Inputs: None (can start immediately)
  - Where: `report/main.tex` references + in-text citations

## Track D: Cartographic Improvement

- [ ] **[D1] Define master color palette and cartographic style guide**
  - Choose a professional color scheme — NOT matplotlib defaults. Recommendations:
    - **Distance ramp:** Sequential palette (e.g., viridis, or a custom blue-to-red diverging scheme for accessibility)
    - **AI works:** Sequential warm palette (e.g., YlOrRd) with size scaling
    - **Quadrant map:** 4-class qualitative (e.g., Tableau 10 or ColorBrewer Set2) — must be colorblind-safe
    - **Hot spots:** Standard hot/cold: red (hot) → white/gray (not sig) → blue (cold)
    - **Provider colors:** AWS = orange (#FF9900), Azure = blue (#0078D4), GCP = green (#34A853) — use actual brand colors
  - Define: font family (use a single sans-serif like Helvetica or Source Sans Pro), title style, legend position, figure size
  - Done when: Style guide documented as a Python dict/config that all figure scripts import
  - Inputs: None
  - Where: `src/style_config.py` (new file)

- [ ] **[D2] Rebuild Figure 1 (global distance-to-compute map)**
  - Use Natural Earth basemap (coastlines + country borders, light gray fill)
  - Plot cities as points colored by distance to nearest region (use sequential palette from D1)
  - Add: proper legend (continuous colorbar with labeled ticks in km), scale indicator, title, source attribution
  - Use an equal-area projection (Robinson or Mollweide) for global maps — NOT raw lat/lon plate carrée
  - Export: 300 DPI PNG (for StoryMap) + PDF (for LaTeX)
  - Done when: Figure exported, uses consistent style from D1, has all cartographic elements
  - Inputs: D1, A2 complete
  - Where: `outputs/figures/fig01_global_distance.png`

- [ ] **[D3] Rebuild Figure 2 (AI research overlay map)**
  - Same basemap and projection as D2 (consistency matters)
  - Cities as graduated symbols: size ∝ sqrt(ai_works), color from warm palette
  - Cloud regions plotted as small distinct markers (triangles or stars) with provider colors from D1
  - Add: legend showing symbol size scale, cloud region legend, title, source
  - Done when: Figure exported with consistent style
  - Inputs: D1, A2 complete
  - Where: `outputs/figures/fig02_ai_overlay.png`

- [ ] **[D4] Rebuild Figure 3 (distance distribution comparison)**
  - Histogram/KDE comparing all cities vs AI cities
  - Use the quadrant palette colors (or a simple 2-color scheme)
  - Add: median lines with labeled values, clear axis labels, legend, title
  - Remove matplotlib default gray background — use white background
  - Done when: Clean, professional histogram exported
  - Inputs: D1, A2 complete
  - Where: `outputs/figures/fig03_distance_distributions.png`

- [ ] **[D5] Rebuild Figure 4 (AI-weighted distance distribution)**
  - Same style as D4 for consistency
  - Add annotation showing weighted mean distance (297 km)
  - Done when: Figure exported
  - Inputs: D1, A2
  - Where: `outputs/figures/fig04_weighted_distance.png`

- [ ] **[D6] Rebuild Figure 5 (scatter: distance vs AI works)**
  - Use a cleaner scatter style: smaller points with alpha transparency, consistent color
  - Add: regression line with confidence band, labeled axes, annotation with GP/CAR coefficients
  - Consider coloring points by region (continent) to add analytical value
  - Done when: Scatter plot exported with regression line
  - Inputs: D1, A2
  - Where: `outputs/figures/fig05_scatter_distance_ai.png`

- [ ] **[D7] Rebuild Figure 6 (quadrant mismatch map)**
  - This is one of the most important figures — make it shine
  - Use the 4-class qualitative palette from D1
  - Make "Low AI / Low Access" (AI deserts) visually prominent: larger symbols or emphasized color
  - Same basemap and projection as D2
  - Add: clear legend with quadrant labels, title, annotation explaining the quadrant logic
  - Done when: Quadrant map exported with emphasis on AI desert cities
  - Inputs: D1, A2
  - Where: `outputs/figures/fig06_quadrant_map.png`

- [ ] **[D8] Create NEW Figure: Gi* Hot Spot map**
  - Map showing hot spot / cold spot classification from B2
  - Use the hot/cold palette from D1
  - Same global basemap as other maps
  - This is the primary new Esri-aligned analysis figure
  - Done when: Hot spot map exported
  - Inputs: B2, D1
  - Where: `outputs/figures/fig_hotspot_map.png`

- [ ] **[D9] Create NEW Figure: Priority Cities map**
  - Map showing top 20 priority cities from B4 (high research capacity, low compute access)
  - Use callout labels for top 10, graduated symbols for the rest
  - Cloud regions shown as background context
  - This is the key "recommendation" figure
  - Done when: Priority map exported with labeled cities
  - Inputs: B4, D1
  - Where: `outputs/figures/fig_priority_cities.png`

- [ ] **[D10] Rebuild regional deep-dive maps (Sub-Saharan Africa + Latin America)**
  - Two separate zoomed-in maps, one for each case study region
  - Show: cities (sized by population), cloud regions (with provider colors), distance lines connecting cities to nearest regions
  - Use inset showing position within global map
  - Done when: Two regional maps exported
  - Inputs: C3, C4, D1
  - Where: `outputs/figures/fig_region_africa.png`, `outputs/figures/fig_region_latam.png`

- [ ] **[D11] Rebuild Figure 7 (model coefficient comparison)**
  - Replace the current bar chart with a cleaner coefficient plot (dot + CI whiskers if available)
  - Show both GP and CAR coefficients side-by-side for distance and population
  - Professional styling from D1
  - Done when: Coefficient plot exported
  - Inputs: D1, A2
  - Where: `outputs/figures/fig07_model_coefficients.png`

- [ ] **[D12] Rebuild Figure 9 (1-degree distance surface) and Figure 10 (GP prediction surface)**
  - Use a proper cartographic colormap (not default viridis on raw raster)
  - Add coastline overlay, labeled key cities, colorbar with units
  - If possible, use a hillshade or semi-transparent approach for better readability
  - Done when: Both surface figures exported
  - Inputs: D1, A2
  - Where: `outputs/figures/fig09_distance_surface.png`, `outputs/figures/fig10_gp_surface.png`

## Track E: ArcGIS Data Preparation & Upload

- [ ] **[E1] Prepare ArcGIS-ready data exports**
  - From the pipeline outputs, create clean GeoJSON files with:
    - `cities_all.geojson` — all 8,000 cities with: name, country, population, lat, lng, distance_to_nearest_km, nearest_provider, nearest_region, quadrant_class
    - `cities_ai.geojson` — 328 AI overlay cities with all above + ai_works, ai_works_recent, gi_zscore, hotspot_class, priority_score
    - `cloud_regions.geojson` — 111 cloud regions with: provider, region_code, lat, lng
    - `ai_deserts.geojson` — filtered subset of cities classified as AI deserts
    - `priority_cities.geojson` — top 20 priority cities for compute investment
  - Ensure: WGS84 (EPSG:4326), field names ≤ 10 chars or clean camelCase, no null geometries, no special characters in string fields
  - Done when: All 5 GeoJSON files exported and validated (load in QGIS or geopandas to verify)
  - Inputs: B1-B5 complete (all new analysis columns), A2

- [ ] **[E2] Write ArcGIS Online upload instructions**
  - Step-by-step for beginner:
    1. Log into ArcGIS Online with Harvard credentials (arcgis.com → Harvard org)
    2. Go to Content → New Item → upload each GeoJSON
    3. Set sharing to "Everyone (public)"
    4. Configure popup templates for each layer (specify which fields to show)
  - Done when: Instructions written with screenshots/descriptions for each step
  - Inputs: E1 complete
  - Where: `docs/arcgis_upload_guide.md`

- [ ] **[E3] Write web map creation instructions**
  - Step-by-step to create 3 web maps in ArcGIS Online Map Viewer:
    - **Map 1: Global Compute Accessibility** — cities_all colored by distance, cloud_regions as markers
    - **Map 2: AI Research & Hot Spots** — cities_ai colored by hotspot_class, cloud_regions, sized by ai_works
    - **Map 3: AI Deserts & Priority Cities** — ai_deserts + priority_cities layers, labeled
  - Include: symbology specifications (which colors, which classification method, how many classes), popup config, basemap choice (Light Gray Canvas recommended)
  - Done when: Instructions written with exact symbology specs
  - Inputs: E2 complete
  - Where: `docs/arcgis_webmap_guide.md`

## Track F: StoryMap Blueprint & Assembly

- [ ] **[F1] Write complete StoryMap content blueprint**
  - A single document that contains the EXACT text, map references, and layout instructions for every section of the StoryMap
  - Structure:
    - **Cover:** Title ("AI Compute Accessibility Atlas: Mapping the Geography of AI Opportunity and Exclusion"), subtitle, author info, cover image (use the distance surface or a striking map)
    - **Section 1 — The Hook:** Open with an "AI desert" city profile. "Lagos, a city of 15 million people, is 3,843 km from the nearest cloud computing region. It has produced zero AI research papers in the most recent OpenAlex data." → Establish the stakes immediately.
    - **Section 2 — The Question:** Present the 5 reframed research questions. "This atlas asks: who has access to the physical infrastructure of AI, and who doesn't?"
    - **Section 3 — The Data & Approach:** Brief, visual explanation of data sources. Use a sidecar block: text on one side, map showing cloud region locations on the other. Name Esri technologies explicitly.
    - **Section 4 — Finding 1: Compute Access is Radically Uneven:** Interactive Map 1 (global distance). Key stats: median city is 657km from compute. Call out regional patterns.
    - **Section 5 — Finding 2: AI Research Clusters Near Compute:** Interactive Map 2 (AI overlay + hot spots). The 2.8× proximity gap. Moran's I result. Gi* hot spot clusters. Regional deep-dives (Africa, Latin America) as sidecar blocks.
    - **Section 6 — Finding 3: The AI Deserts:** Interactive Map 3 (AI deserts + priority cities). Table of top AI desert cities. "These are cities where millions of people live in places structurally excluded from the AI economy."
    - **Section 7 — The Models: Distance Matters, But It's Not Alone:** Coefficient comparison figure. GP vs CAR interpretation. "Compute proximity is one important part of an enabling environment."
    - **Section 8 — Implications: Where to Invest Next:** Priority cities ranking. Framing for OECD, cloud providers, development finance. "If you could site one new cloud region to maximize AI research equity, where would you put it?"
    - **Section 9 — Limitations & Next Steps:** Honest caveats, framed constructively. "This atlas is a first pass — here's what comes next."
    - **Section 10 — About & Methods:** Bio, photo, detailed methodology, Esri tech list, data sources, code repository link
  - Done when: Full blueprint written with exact text for every section + map embed specifications
  - Inputs: C1-C6 complete (all narrative content), D1-D12 complete (all figures), E1-E3 complete (all ArcGIS data)
  - Where: `docs/storymap_blueprint.md`

- [ ] **[F2] Write StoryMap assembly instructions**
  - Step-by-step for beginner:
    1. Go to storymaps.arcgis.com → New Story
    2. For each section in blueprint: what block type to use (sidecar, immersive, narrative, map, embed)
    3. How to embed web maps
    4. How to add images (reference figure file paths)
    5. How to configure navigation
    6. How to set sharing to Public
    7. How to get the public URL for submission
  - Done when: Complete assembly guide written
  - Inputs: F1, E3 complete
  - Where: `docs/storymap_assembly_guide.md`

- [ ] **[F3] Final review against EIP rubric**
  - Go through every acceptance check in Section 2 above
  - Go through the EIP-specific requirements:
    - [ ] Short bio and professional picture present?
    - [ ] Brief description about achievement / reason for applying?
    - [ ] Project uses Esri technology, presented in StoryMap format?
    - [ ] Maps, narrative, apps, video, graphics, charts included?
    - [ ] StoryMap shared with Public, no NDA content?
  - Go through the judging criteria with a score:
    - [ ] Potential impact: Is a specific stakeholder named? Is the output actionable?
    - [ ] Innovation: Is there a novel analytical approach? (Gi* + GP/CAR dual model + priority ranking)
    - [ ] Originality: Has anyone mapped AI compute accessibility at this scale before?
    - [ ] Implementation: Are 3+ Esri tools/technologies used and named?
    - [ ] Organization: Does the StoryMap narrative flow logically from hook to implication?
  - Done when: All checks passed or gaps documented with fix tasks added
  - Inputs: All other tracks complete
  - Where: Update this WORK.md with results

## Track G: LaTeX Report Update (parallel, lower priority than StoryMap)

- [ ] **[G1] Update report/main.tex with new research questions**
  - Replace Section 1.1 with the 5 new questions from C1
  - Done when: Questions updated in LaTeX source
  - Inputs: C1

- [ ] **[G2] Add new analysis sections to report**
  - Add Moran's I results subsection (after current 4.2)
  - Add Gi* hot spot results subsection
  - Add priority city ranking subsection
  - Add AI deserts section (from C2)
  - Done when: New sections added with figures and tables referenced
  - Inputs: B1-B4, C2

- [ ] **[G3] Add regional case study sections**
  - Add Sub-Saharan Africa deep-dive (from C3)
  - Add Latin America deep-dive (from C4)
  - Done when: Both case studies in report
  - Inputs: C3, C4

- [ ] **[G4] Update Discussion and References**
  - Replace Discussion with policy-forward version from C5
  - Add new references from C6
  - Done when: Discussion rewritten, 5+ new references in bibliography
  - Inputs: C5, C6

- [ ] **[G5] Replace all figures in report with rebuilt versions**
  - Update all `\includegraphics` paths to point to new figure files from Track D
  - Add new figures (hot spot map, priority cities, regional maps)
  - Done when: All figures in report are from the new figure set
  - Inputs: D2-D12

- [ ] **[G6] Rebuild LaTeX PDF and verify**
  - Compile `report/main.tex`
  - Verify: all figures render, all references resolve, no orphan labels
  - Done when: Clean PDF generated with no errors
  - Inputs: G1-G5

---

# 5. Worker Driver Prompt

```
You are a worker agent executing tasks from WORK.md for the AI Compute Accessibility Atlas project.

## Your loop:
1. Read WORK.md completely at the start of every iteration.
2. Identify the highest-priority UNBLOCKED task (check inputs/dependencies).
3. Execute that ONE task tightly — no scope creep, no bonus work.
4. After completing the task:
   a. Mark it [x] in Section 4.
   b. Add a brief entry to Section 7 (Results): what file changed, what was produced.
   c. Add any surprises or patterns to Section 6 (Learnings).
   d. If new atomic tasks emerged, add them to Section 4 in the appropriate track.
5. Save WORK.md.
6. Repeat from step 1.

## Priority order (when multiple tasks are unblocked):
Track A (inspect) → Track B (analysis) → Track D (figures) → Track C (narrative) → Track E (ArcGIS data) → Track F (StoryMap) → Track G (LaTeX)

## Rules:
- NEVER skip a task's "Done when" condition.
- NEVER modify files outside the task's specified "Where" location without creating a new task.
- If a task requires web search (e.g., recent African cloud announcements), use available tools.
- If a task is BLOCKED, record what's needed and move to next unblocked task.
- If you discover the pipeline structure differs from assumptions (e.g., different file paths), update WORK.md assumptions and adapt.
- All Python code changes should be tested by running the relevant script before marking done.
- All figure exports must be 300 DPI PNG minimum.
- Maintain the master color palette defined in D1 across ALL figures.
- When writing narrative content, maintain the voice of the original report: confident but intellectually honest, accessible to policy audiences, not overly academic.
- The StoryMap is the PRIMARY deliverable. If time runs short, prioritize: E1 → F1 → F2 over G1-G6.

## Acceptance checks to verify at the end:
After all tasks are complete, run through every checkbox in Section 2 of WORK.md and report pass/fail.

## Stop conditions:
- All tasks in Section 4 are marked [x] and all acceptance checks pass → DONE
- A task is BLOCKED and no other unblocked tasks remain → STOP and report what input is needed
- Definition of Done checklist in Section 1 is fully satisfied → DONE
```

---

# 6. Learnings

_(initially empty — worker fills this in during execution)_

---

# 7. Results

_(initially empty — worker fills this in during execution)_
