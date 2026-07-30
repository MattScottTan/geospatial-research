# ArcGIS Pro Master Workflow — All Analyses in Execution Order

> Complete checklist for running every analysis in ArcGIS Pro so you can cite it as the primary platform.
> Python results serve as validation. ArcGIS Pro numbers go in the StoryMap.
>
> **Estimated time:** 3–5 hours total (319 points is tiny — tools run in seconds)
>
> **Why this matters for EIP:** The "Implementation" criterion rewards breadth of Esri toolbox use. By the end of this workflow you will have used **6+ distinct ArcGIS Pro tools** across **3 toolboxes**, plus ArcGIS Online for web mapping and StoryMap publishing. That's the "covers much of the spectrum of GIS" signal that won [EIP-2025-1] its award.

---

## Phase 0: Project Setup

### 0.1 — Create an ArcGIS Pro project

1. Open ArcGIS Pro → **New Project** → **Map**
2. Name: `AI_Compute_Atlas`
3. Save to a local folder (not OneDrive — geoprocessing tools can fail on cloud-synced paths)

### 0.2 — Load your data layers

Add these layers to the map (drag into the Contents pane or use **Add Data**):

| Layer file | Contents | Rows | Key fields |
|---|---|---|---|
| `ai_access_ai_cities.gpkg` | Unique AI cities | 319 | `openalex_ai_works_recent`, `log_ai_works`, `dist_km_nearest_region`, `population` |
| `city_access_metrics.csv` | All 8,000 cities | ~8,000 | `dist_km_nearest_region`, `population`, `lat`, `lon` |
| `cloud_regions.gpkg` | Cloud region points | ~60 | `provider` |
| `ne_110m_admin_0_countries.geojson` | Country boundaries | ~180 | `NAME` |

**For the CSV (all cities):** After adding, right-click → **Display XY Data** using the `lon` and `lat` fields. Set coordinate system to WGS 1984 (EPSG:4326). Export to feature class: right-click the event layer → **Data** → **Export Features** → save as `all_cities` in your project geodatabase.

### 0.3 — Verify field names

Open each layer's attribute table and confirm the field names match what the tools expect. Record the actual names here:

| Expected | Actual (fill in) |
|---|---|
| `openalex_ai_works_recent` | _________________ |
| `log_ai_works` | _________________ |
| `dist_km_nearest_region` | _________________ |
| `population` | _________________ |
| `provider` | _________________ |

If `log_ai_works` doesn't exist, create it:
- Open the AI cities attribute table → **Add Field** → name it `log_ai_works`, type Double
- Right-click the new field header → **Calculate Field**
- Expression: `math.log1p(!openalex_ai_works_recent!)` (Python 3)

### 0.4 — Set the coordinate system

Your data is in WGS 1984 (geographic coordinates). For spatial statistics with K Nearest Neighbors, this works fine — neighbor rankings are preserved. But if any tool warns about projected coordinates:

- Right-click the map in Contents → **Properties** → **Coordinate Systems**
- Search for **World Mollweide** (EPSG:54009) — a global equal-area projection
- Apply, then re-run the tool

**Checkpoint:** You should see 319 AI city points, ~60 cloud region points, and ~8,000 all-city points on the map. If any layer is empty or misplaced, check the coordinate fields.

---

## Phase 1: Distance Analysis

**Purpose:** Verify/replicate the distance-to-nearest-cloud-region calculation in ArcGIS Pro using the Near tool. This is the foundation of the entire project.

**Toolbox:** Analysis Tools > Proximity

### 1.1 — Near Analysis (AI cities → cloud regions)

1. **Geoprocessing** → search **"Near"** → select **Near (Analysis)**
2. Configure:
   - **Input Features:** `ai_access_ai_cities` (319 AI cities)
   - **Near Features:** `cloud_regions` (~60 regions)
   - **Search Radius:** leave blank (find nearest regardless of distance)
   - **Method:** **Geodesic** ← important for global data
3. Click **Run**
4. The tool adds two fields to your AI cities layer:
   - `NEAR_FID` — the ID of the nearest cloud region
   - `NEAR_DIST` — distance in **meters** (geodesic)
5. Convert to km: **Calculate Field** on a new field `near_dist_km`:
   - Expression: `!NEAR_DIST! / 1000`

**Validation:** Compare `near_dist_km` to your existing `dist_km_nearest_region`. They should be very close (within 1–2%). Small differences come from great-circle vs. geodesic calculation methods.

### 1.2 — Near Analysis (all 8,000 cities → cloud regions)

Repeat the same process with `all_cities` as the input. This lets you say the distance calculation was done in ArcGIS Pro.

### 1.3 — Generate Near Table (optional — for multi-provider analysis)

If you want to show distance to each provider separately (not just the nearest):

1. Search **"Generate Near Table"**
2. **Input Features:** AI cities
3. **Near Features:** cloud regions
4. **Maximum Number of Closest:** `3` (one per provider)
5. **Method:** Geodesic
6. This produces a table showing each city's distance to AWS, Azure, and GCP separately — useful for the bundle index's "provider diversity" component.

**Screenshot:** None needed for the StoryMap. This is a validation step.

**Tools used so far:** Near (Analysis), Generate Near Table (Analysis)

---

## Phase 2: Buffer Analysis — Compute Corridors

**Purpose:** Create the 500 km buffer rings around cloud regions that visually show the "compute corridor" — 72% of AI cities fall within this zone. This is a strong visual for the hero map.

**Toolbox:** Analysis Tools > Proximity

### 2.1 — Create Buffers

1. Search **"Buffer"** → select **Buffer (Analysis)**
2. Configure:
   - **Input Features:** `cloud_regions`
   - **Output Feature Class:** `cloud_buffers_500km`
   - **Distance:** `500` **Kilometers**
   - **Dissolve Type:** **Dissolve all** ← merges overlapping buffers into corridor zones
   - **Method:** **Geodesic**
3. Click **Run**

### 2.2 — Style the buffers

1. Right-click `cloud_buffers_500km` → **Symbology**
2. Set:
   - Fill: light blue or light grey, **10–15% opacity**
   - Outline: dashed, medium grey, 1 px
3. In the **Drawing Order** (Contents pane), drag this layer **below** AI cities but **above** the basemap

### 2.3 — Spatial Join: count AI cities inside corridors (optional validation)

1. Search **"Spatial Join"**
2. **Target Features:** `ai_access_ai_cities`
3. **Join Features:** `cloud_buffers_500km`
4. **Match Option:** `WITHIN`
5. Open the output attribute table. Count rows where the join succeeded — this should be ~237 cities (72%)

**Validation:** 237 of 328 AI cities (72.3%) should fall within 500 km. If you get a slightly different number, it's because the buffer polygon boundary doesn't perfectly match a pure distance threshold — this is fine.

**Screenshot:** The buffer overlay on the hero map is a strong visual for the StoryMap.

**Tools used so far:** Near, Generate Near Table, Buffer, Spatial Join

---

## Phase 3: Spatial Statistics — The Core Analyses

This is the most important phase for the EIP submission. You want to be able to write:

> "Spatial autocorrelation was assessed using Global Moran's I and local clustering was mapped using Getis-Ord Gi* Hot Spot Analysis, both implemented in the ArcGIS Pro Spatial Statistics toolbox. Results were validated using Cluster and Outlier Analysis (Anselin Local Moran's I) and Optimized Hot Spot Analysis."

**Toolbox:** Spatial Statistics Tools > Analyzing Patterns + Mapping Clusters

### 3.1 — Global Moran's I (Spatial Autocorrelation)

**What it tests:** Whether the overall pattern of AI works across cities is clustered, dispersed, or random.

1. **Geoprocessing** → search **"Spatial Autocorrelation"** → select **Spatial Autocorrelation (Global Moran's I)**
   - Path: Spatial Statistics Tools > Analyzing Patterns
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities` (319 unique cities)
   - **Input Field:** `log_ai_works`
   - **Conceptualization of Spatial Relationships:** **K Nearest Neighbors**
   - **Distance Method:** **Euclidean Distance**
   - **Number of Neighbors:** **8**
   - **Standardization:** **Row**
3. Click **Run**
4. Read the **Messages** pane for results

**Expected results (from Python):**

| Statistic | Python value | ArcGIS Pro should be close to |
|---|---|---|
| Moran's I | 0.066 | 0.05–0.08 |
| z-score | 2.86 | 2.5–3.2 |
| p-value | 0.008 | < 0.05 |

Small differences are normal and expected — what matters is:
- [x] Moran's I is **positive** (clustered, not dispersed)
- [x] z-score is **> 1.96** (significant at 95%)
- [x] p-value is **< 0.05**

**📸 Screenshot the results panel** — ArcGIS Pro produces a graphic with the Moran's I value, z-score, p-value, and a normal distribution diagram showing where your result falls. This is a ready-made figure for the StoryMap.

### 3.2 — Sensitivity check: run Moran's I with different K values

To demonstrate robustness, run the same tool with K = 4, 6, 10, 12:

| K | Moran's I | z-score | p-value | Significant? |
|---|---|---|---|---|
| 4 | _______ | _______ | _______ | Y / N |
| 6 | _______ | _______ | _______ | Y / N |
| **8** | _______ | _______ | _______ | Y / N |
| 10 | _______ | _______ | _______ | Y / N |
| 12 | _______ | _______ | _______ | Y / N |

If the result is significant across most K values, you can write: "Results are robust to the choice of neighborhood size (K = 4 to 12)."

### 3.3 — Getis-Ord Gi* Hot Spot Analysis

**What it tests:** WHERE statistically significant clusters of high or low AI activity are located.

1. Search **"Hot Spot Analysis"** → select **Hot Spot Analysis (Getis-Ord Gi*)**
   - Path: Spatial Statistics Tools > Mapping Clusters
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities`
   - **Input Field:** `log_ai_works` (same as Moran's I for consistency)
   - **Output Feature Class:** `ai_cities_hotspots`
   - **Conceptualization of Spatial Relationships:** **K Nearest Neighbors**
   - **Number of Neighbors:** **8**
   - **Distance Method:** **Euclidean Distance**
   - **Standardization:** **Row**
3. Click **Run**

**Output fields added:**
- `Gi_Bin`: -3 (cold 99%) to +3 (hot 99%)
- `Gi_ZScore`: z-score per city
- `Gi_PValue`: p-value per city

**Expected counts (from Python):**

| Gi_Bin | Meaning | Python count | ArcGIS should be ±2 |
|---|---|---|---|
| 3 | Hot spot 99% | 1 (Macau) | 1 |
| 2 | Hot spot 95% | 6 | 5–7 |
| 1 | Hot spot 90% | ≈0 | 0–2 |
| 0 | Not significant | ~279 | 275–282 |
| -1 | Cold spot 90% | ≈0 | 0–2 |
| -2 | Cold spot 95% | 23 | 21–25 |
| -3 | Cold spot 99% | 10 | 8–12 |

**Validation steps:**
1. Open attribute table → right-click `Gi_Bin` column → **Sort Descending**
2. Check: Is Macau (or a nearby East Asian city) the top hot spot?
3. Check: Is Carbondale, US among the strongest cold spots?
4. Count each Gi_Bin class — record in the table above

### 3.4 — Symbolize Gi* results

1. Right-click `ai_cities_hotspots` → **Symbology**
2. Choose **Unique Values** on `Gi_Bin`
3. Color scheme:
   - 3 (hot 99%): **dark red** (#B2182B)
   - 2 (hot 95%): **orange/salmon** (#EF8A62)
   - 1 (hot 90%): **light orange** (#FDDBC7)
   - 0 (not significant): **light grey** (#D9D9D9)
   - -1 (cold 90%): **light blue** (#D1E5F0)
   - -2 (cold 95%): **medium blue** (#67A9CF)
   - -3 (cold 99%): **dark blue** (#2166AC)
4. Set marker size to scale with `openalex_ai_works_recent` or keep uniform
5. This produces the Figure 11 equivalent

**📸 Screenshot this map** — it's a key figure for the StoryMap.

### 3.5 — Optimized Hot Spot Analysis (robustness check)

1. Search **"Optimized Hot Spot Analysis"**
   - Path: Spatial Statistics Tools > Mapping Clusters
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities`
   - **Analysis Field:** `log_ai_works`
   - **Output Feature Class:** `ai_cities_hotspots_optimized`
   - Leave all other settings at defaults
3. Click **Run**
4. Compare output to your manual Gi* results

**If the same cities appear as hot/cold spots:** Write in the StoryMap:
> "Results were confirmed using both manual and optimized parameterizations of the Getis-Ord Gi* tool in ArcGIS Pro."

### 3.6 — Cluster and Outlier Analysis (LISA / Anselin Local Moran's I)

**What it tests:** Distinguishes four types of spatial clusters — directly maps to your case study typology.

1. Search **"Cluster and Outlier Analysis"**
   - Path: Spatial Statistics Tools > Mapping Clusters
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities`
   - **Input Field:** `log_ai_works`
   - **Output Feature Class:** `ai_cities_lisa`
   - **Conceptualization of Spatial Relationships:** **K Nearest Neighbors**
   - **Number of Neighbors:** **8**
   - **Distance Method:** **Euclidean Distance**
   - **Standardization:** **Row**
3. Click **Run**

**Output fields:**
- `COType`: HH, HL, LH, LL, or blank (not significant)
- `LMiZScore`: local Moran's z-score
- `LMiPValue`: local Moran's p-value

**Why this matters:** The LISA categories map directly to your four case studies:

| COType | Meaning | Case study |
|---|---|---|
| **HH** | High AI surrounded by high AI (cluster) | Singapore |
| **LH** | Low AI surrounded by high AI (underperformer) | Seoul |
| **HL** | High AI surrounded by low AI (overperformer) | Ho Chi Minh City |
| **LL** | Low AI surrounded by low AI (desert) | Lagos |

**Check:** Do Singapore, Seoul, HCMC, and Lagos fall into the expected categories? If yes, this is a powerful analytical confirmation of your case study selection. If not, note the actual categories — the data may tell a more nuanced story.

**📸 Screenshot the LISA map** — symbolize by COType with:
- HH: red
- HL: light red / pink
- LH: light blue
- LL: dark blue
- Not significant: grey

This could be a strong supplementary figure showing which cities outperform or underperform their neighborhoods.

**Tools used so far:** Near, Generate Near Table, Buffer, Spatial Join, Global Moran's I, Hot Spot Analysis (Gi*), Optimized Hot Spot Analysis, Cluster and Outlier Analysis (LISA)

---

## Phase 4: Regression Analysis

**Purpose:** Test whether the distance–AI activity relationship survives controls for population and spatial structure. Your Python pipeline ran a GP and CAR/GMRF model. ArcGIS Pro offers OLS and GWR — running at least OLS gives you an ArcGIS-cited regression result.

**Toolbox:** Spatial Statistics Tools > Modeling Spatial Relationships

### 4.1 — Ordinary Least Squares (OLS)

1. Search **"Ordinary Least Squares"** → select **OLS (Ordinary Least Squares)**
   - Path: Spatial Statistics Tools > Modeling Spatial Relationships
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities`
   - **Unique ID Field:** your object ID or city ID field
   - **Output Feature Class:** `ai_cities_ols`
   - **Dependent Variable:** `log_ai_works`
   - **Explanatory Variables:** select BOTH:
     - `dist_km_nearest_region` (or your distance field)
     - `population` (or log-population if you have it)
3. Click **Run**

**What to check in the output:**
- **Distance coefficient:** should be **negative** (farther = less AI works)
- **Population coefficient:** should be **positive** (bigger city = more AI works)
- **R²:** overall model fit
- **Jarque-Bera p-value:** tests whether residuals are normally distributed
- **Koenker (BP) p-value:** tests for heteroscedasticity

**Create log-population field first** (if not already present):
- Add field `log_pop`, type Double
- Calculate: `math.log1p(!population!)`
- Use `log_pop` instead of raw `population` in the regression — this matches your Python pipeline

**Expected result direction (from Python):**

| Variable | Python GP coeff | Python CAR coeff | ArcGIS OLS should be |
|---|---|---|---|
| Distance | −0.207 | −0.052 | **Negative** |
| Population | +0.279 | +0.309 | **Positive** |

The OLS coefficients won't match the GP/CAR values exactly (different model specifications), but the **signs should be the same**. That's the directional consistency check.

**📸 Screenshot the OLS summary report** — ArcGIS Pro produces a diagnostic report with coefficients, p-values, and diagnostic statistics. This is citation-ready.

### 4.2 — Exploratory Regression (optional — impressive for EIP)

1. Search **"Exploratory Regression"**
   - Path: Spatial Statistics Tools > Modeling Spatial Relationships
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities`
   - **Dependent Variable:** `log_ai_works`
   - **Candidate Explanatory Variables:** add ALL potentially relevant fields:
     - `dist_km_nearest_region` (or log version)
     - `log_pop`
     - Any bundle index components you have as fields
   - **Maximum Number of Explanatory Variables:** 3–4
3. Click **Run**

This tool automatically tests all variable combinations and reports which produce the best-fitting, best-specified models. It's an excellent tool to name in the StoryMap:

> "Exploratory Regression in ArcGIS Pro was used to identify the strongest model specifications from candidate variables."

### 4.3 — Geographically Weighted Regression (GWR) (optional — strong upgrade)

GWR estimates local coefficients — the distance effect might be stronger in some regions than others. This would be a significant analytical addition.

1. Search **"Geographically Weighted Regression"**
   - Path: Spatial Statistics Tools > Modeling Spatial Relationships
2. Configure:
   - **Input Feature Class:** `ai_access_ai_cities`
   - **Dependent Variable:** `log_ai_works`
   - **Explanatory Variables:** `dist_km_nearest_region`, `log_pop`
   - **Output Feature Class:** `ai_cities_gwr`
   - **Kernel Type:** **Adaptive**
   - **Bandwidth Method:** **AICc** (auto-selects optimal bandwidth)
3. Click **Run**

**Output:** Each city gets local coefficient estimates. You could map the local distance coefficient to show WHERE the distance effect is strongest — e.g., is it strongest in Africa? Southeast Asia?

**📸 If you run GWR:** Map the local distance coefficient. Cities where it's strongly negative = distance matters most there. This would be a powerful supplementary figure and an impressive tool to cite.

**Tools used so far:** Near, Generate Near Table, Buffer, Spatial Join, Global Moran's I, Gi*, Optimized Gi*, LISA, OLS, Exploratory Regression, GWR

---

## Phase 5: Priority City Screening in ArcGIS Pro

**Purpose:** Replicate the priority-city identification (1,988 cities with zero AI works + distance > 1,252 km) using ArcGIS Pro selection tools.

### 5.1 — Select by Attributes

1. In the Contents pane, right-click `all_cities` → **Attribute Table**
2. Click **Select by Attributes** (top of table)
3. Build the query:
   ```sql
   dist_km_nearest_region > 1252 AND (openalex_ai_works_recent = 0 OR openalex_ai_works_recent IS NULL)
   ```
   (Adjust field names to match your actual fields. If AI works aren't in the all-cities layer, you'll need a join first — see 5.2.)
4. Click **Apply**
5. Check the selection count — should be approximately **1,988**

### 5.2 — If AI works aren't in the all-cities layer

You may need to join AI works onto the all-cities layer first:

1. Right-click `all_cities` → **Joins and Relates** → **Add Join**
2. Join from `ai_access_ai_cities` on a shared key (city name + country, or a unique ID)
3. After the join, cities with no match will have NULL for AI works — these are your "zero AI works" cities
4. Then run the selection query from 5.1

### 5.3 — Export priority cities

1. With the selection active, right-click `all_cities` → **Data** → **Export Features**
2. Save as `priority_cities` in your project geodatabase
3. This gives you a standalone layer of 1,988 priority cities

### 5.4 — Symbolize priority cities

1. Right-click `priority_cities` → **Symbology**
2. **Graduated Symbols** on `population` — larger cities get larger dots
3. **Color** by `dist_km_nearest_region` — darker = farther
4. Or rank by priority (population first, distance second) and color by rank

---

## Phase 6: Web Map Publishing

**Purpose:** Create the interactive web maps that judges can click on in the StoryMap.

### 6.1 — Share Gi* results as a web layer

1. Right-click `ai_cities_hotspots` → **Sharing** → **Share as Web Layer**
2. Configure:
   - **Name:** `AI Cities Hot Spot Analysis`
   - **Layer Type:** Feature
   - **Share with:** Everyone (public)
   - **Tags:** AI, compute, hot spot, Getis-Ord
3. Click **Publish**

### 6.2 — Share priority cities as a web layer

Same process with `priority_cities`:
- **Name:** `AI Compute Priority Cities`
- Share publicly

### 6.3 — Share LISA results as a web layer (if you ran it)

Same process with `ai_cities_lisa`:
- **Name:** `AI Cities Cluster and Outlier Analysis`
- Share publicly

### 6.4 — Build web maps in ArcGIS Online

1. Go to harvard-cga.maps.arcgis.com → **Map Viewer**
2. Add your published layers
3. Configure popups for each layer:
   - **AI cities:** city name, country, population, distance, AI works, Gi_Bin
   - **Priority cities:** city name, country, population, distance, priority rank
4. Save and share publicly
5. Embed in the StoryMap

---

## Phase 7: Validation Summary

After completing all analyses, fill in this table. This becomes your methods documentation.

| Analysis | ArcGIS Pro Result | Python Result | Match? |
|---|---|---|---|
| Moran's I | I = ______, z = ______, p = ______ | I = 0.066, z = 2.86, p = 0.008 | ☐ Direction ☐ Significance |
| Gi* hot spots (99%) | ______ cities | 1 city (Macau) | ☐ |
| Gi* hot spots (95%) | ______ cities | 6 cities | ☐ |
| Gi* cold spots (95%) | ______ cities | 23 cities | ☐ |
| Gi* cold spots (99%) | ______ cities | 10 cities | ☐ |
| Top hot spot city | ______________ | Macau | ☐ |
| Top cold spot city | ______________ | Carbondale, US | ☐ |
| OLS distance coeff | ______ (sign: +/−) | GP: −0.207, CAR: −0.052 | ☐ Negative |
| OLS population coeff | ______ (sign: +/−) | GP: +0.279, CAR: +0.309 | ☐ Positive |
| Cities within 500km buffer | ______ (____%) | 237 (72.3%) | ☐ |
| Priority cities selected | ______ | 1,988 | ☐ |

**If everything matches in direction and significance:** Write in the StoryMap:

> "Results were validated across both Python (PySAL/scipy) and ArcGIS Pro implementations, with consistent cluster assignments and coefficient directions."

**If small count differences exist (e.g., 6 vs 7 hot spots):** This is normal. Report the ArcGIS Pro numbers as primary and note:

> "Small count differences between implementations reflect differences in spatial weights construction and are expected."

---

## Citation Language for the StoryMap

### Methods section — tools paragraph

> This analysis was conducted using **ArcGIS Pro** (version [X.X]) and **ArcGIS Online**. Compute accessibility was measured using **Near Analysis** (geodesic distance from each city to its nearest cloud region). Spatial autocorrelation was assessed using **Global Moran's I** (Spatial Statistics toolbox > Analyzing Patterns) and local clustering was mapped using **Getis-Ord Gi* Hot Spot Analysis** (Spatial Statistics toolbox > Mapping Clusters). Cluster types were identified using **Cluster and Outlier Analysis (Anselin Local Moran's I)**. The distance–activity relationship was tested using **Ordinary Least Squares regression** (Spatial Statistics toolbox > Modeling Spatial Relationships)[, with local variation assessed using **Geographically Weighted Regression**]. Compute corridors were visualized using **Buffer Analysis** (Analysis toolbox > Proximity). Results were validated against an independent Python implementation (scipy, PySAL) with consistent findings. Interactive maps were published through **ArcGIS Online** and embedded in this **ArcGIS StoryMap**.

### Tool inventory for judges

| # | Tool | Toolbox | Purpose |
|---|---|---|---|
| 1 | Near | Analysis > Proximity | Distance to nearest cloud region |
| 2 | Buffer | Analysis > Proximity | 500 km compute corridors |
| 3 | Spatial Join | Analysis > Overlay | Count cities within corridors |
| 4 | Global Moran's I | Spatial Statistics > Analyzing Patterns | Spatial autocorrelation test |
| 5 | Hot Spot Analysis (Gi*) | Spatial Statistics > Mapping Clusters | Local cluster identification |
| 6 | Optimized Hot Spot Analysis | Spatial Statistics > Mapping Clusters | Robustness check |
| 7 | Cluster and Outlier (LISA) | Spatial Statistics > Mapping Clusters | HH/HL/LH/LL typology |
| 8 | OLS Regression | Spatial Statistics > Modeling | Distance–activity relationship |
| 9 | Exploratory Regression | Spatial Statistics > Modeling | Variable selection |
| 10 | GWR | Spatial Statistics > Modeling | Local coefficient variation |
| 11 | Select by Attributes | — | Priority city screening |
| 12 | Share as Web Layer | Sharing | Interactive web maps |
| 13 | ArcGIS Online Map Viewer | — | Web map configuration |
| 14 | ArcGIS StoryMaps | — | Final publication |

That's **10+ distinct geoprocessing tools** across **2 major toolboxes** plus the web mapping and StoryMap platform. This is the "covers much of the spectrum of GIS" signal.

---

## Execution Order Checklist

Run these in order. Each phase depends on the previous one.

### Phase 0: Setup
- [ ] Create ArcGIS Pro project
- [ ] Load all 4 data layers
- [ ] Verify field names
- [ ] Create `log_ai_works` field if missing
- [ ] Create `log_pop` field if missing

### Phase 1: Distance
- [ ] Run Near (AI cities → cloud regions) — geodesic
- [ ] Run Near (all cities → cloud regions) — geodesic
- [ ] Validate distances against Python values
- [ ] (Optional) Generate Near Table for multi-provider distances

### Phase 2: Buffers
- [ ] Run Buffer (cloud regions, 500 km, dissolve)
- [ ] Style buffer layer (light, translucent)
- [ ] (Optional) Spatial Join to count cities within corridor

### Phase 3: Spatial Statistics ← MOST IMPORTANT
- [ ] Run Global Moran's I (K=8, Row standardization)
- [ ] 📸 Screenshot Moran's I results graphic
- [ ] Record: I = ______, z = ______, p = ______
- [ ] (Optional) Run Moran's I sensitivity (K = 4, 6, 10, 12)
- [ ] Run Hot Spot Analysis (Gi*) (K=8, Row standardization)
- [ ] Symbolize Gi* results (red–grey–blue)
- [ ] 📸 Screenshot Gi* map
- [ ] Record counts per Gi_Bin class
- [ ] Run Optimized Hot Spot Analysis
- [ ] Compare to manual Gi* — same top cities?
- [ ] Run Cluster and Outlier Analysis (LISA)
- [ ] Check: Singapore=HH? Seoul=LH? HCMC=HL? Lagos=LL?
- [ ] 📸 Screenshot LISA map

### Phase 4: Regression
- [ ] Run OLS (log_ai_works ~ dist_km + log_pop)
- [ ] Record: distance coeff = ______ (sign: ___), pop coeff = ______ (sign: ___)
- [ ] 📸 Screenshot OLS report
- [ ] (Optional) Run Exploratory Regression
- [ ] (Optional) Run GWR — map local distance coefficient

### Phase 5: Priority Cities
- [ ] Select by Attributes (distance > 1252 AND works = 0/NULL)
- [ ] Export to `priority_cities` feature class
- [ ] Record count: ______ cities (should be ~1,988)
- [ ] Symbolize by population + distance

### Phase 6: Web Publishing
- [ ] Share Gi* results as web layer (public)
- [ ] Share priority cities as web layer (public)
- [ ] (Optional) Share LISA results as web layer
- [ ] Build interactive web maps in ArcGIS Online
- [ ] Configure popups
- [ ] Test in incognito browser
- [ ] Embed in StoryMap

### Phase 7: Validation
- [ ] Fill in the validation summary table
- [ ] All directions match? ☐
- [ ] All significance levels match? ☐
- [ ] Screenshot all results for documentation

---

## Troubleshooting Quick Reference

| Problem | Fix |
|---|---|
| "Tool requires projected data" | Set map to World Mollweide (EPSG:54009), or ignore if using K Nearest Neighbors |
| Gi* counts don't match Python | ±1–2 cities is normal. Report ArcGIS Pro numbers. |
| OLS coefficients differ from GP/CAR | Expected — different model types. Check signs match, not magnitudes. |
| Near distances differ by 1–2% | Great-circle vs geodesic method difference. Both are valid. |
| Tool runs on wrong layer | Check you're using 319 AI cities, not 8,000 all-cities |
| Moran's I comes back negative | Check you're using `log_ai_works`, not raw distance field |
| "Field does not exist" error | Open attribute table and check actual field name spellings |
| Web layer won't share publicly | Check Harvard CGA org sharing settings; may need admin approval |
