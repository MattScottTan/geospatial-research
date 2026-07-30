# Spatial Statistics in ArcGIS Pro — Click-by-Click Instructions

## Prerequisites
- ArcGIS Pro installed with Harvard CGA license
- Your `cities_with_hotspots.geojson` or `ai_access_ai_cities.gpkg` loaded as a layer
- The layer should contain unique AI cities (319 rows) with at least:
  - A field for AI works (e.g., `openalex_ai_works_recent` or `log_ai_works`)
  - Point geometry (lat/lon)

---

## Method 1: Global Moran's I — Spatial Autocorrelation

This tests whether the overall pattern of AI works across cities is clustered, 
dispersed, or random.

### Steps:

1. Open **ArcGIS Pro** and add your AI cities layer to a map.

2. In the top ribbon, click the **Analysis** tab.

3. Click **Tools** to open the Geoprocessing pane.

4. In the search bar, type **"Spatial Autocorrelation"** and select:
   **Spatial Autocorrelation (Global Moran's I)**
   - Found under: Spatial Statistics Tools > Analyzing Patterns

5. Configure the tool:
   - **Input Feature Class:** your AI cities layer
   - **Input Field:** select your AI works field (e.g., `log_ai_works` or `openalex_ai_works_recent`)
     - Recommendation: use `log_ai_works` (log-transformed) to reduce the influence of extreme outliers like Beijing
   - **Conceptualization of Spatial Relationships:** choose one of:
     - **K Nearest Neighbors** — recommended. This defines each city's "neighborhood" as its K closest cities by distance. Use K = 8 as a starting point (a common default).
     - **Fixed Distance Band** — alternative. You specify a distance threshold (e.g., 1000 km) and all cities within that radius are neighbors.
     - **Inverse Distance** — weights closer neighbors more heavily than distant ones.
   - **Distance Method:** **Euclidean Distance** (fine for global-scale point data)
   - **Number of Neighbors** (if using K Nearest Neighbors): **8**
   - **Standardization:** **Row** (recommended — normalizes weights so each city's neighbors sum to 1)

6. Click **Run**.

7. **Read the output** in the Geoprocessing Messages pane:
   - **Moran's Index:** should be ~0.066 (matching your Python result)
   - **z-score:** should be ~2.86
   - **p-value:** should be ~0.008
   - If the z-score is > 1.96 and p-value < 0.05, you have significant positive spatial autocorrelation.

8. **Screenshot the results** — the tool produces a summary graphic with the Moran's I value, z-score, and a normal distribution diagram showing where your result falls. This makes a good supplementary figure for the StoryMap or sources section.

### Notes:
- Results may differ slightly from your Python implementation depending on how the spatial weights matrix is constructed. Small differences in I (e.g., 0.062 vs 0.066) are normal and not a concern — the direction and significance are what matter.
- If you want to exactly replicate your Python results, you'll need to match the spatial weights specification exactly (same K or distance band, same row standardization).

---

## Method 2: Getis-Ord Gi* — Hot Spot Analysis

This identifies WHERE statistically significant clusters of high or low AI 
activity are located.

### Steps:

1. In the Geoprocessing pane, search for **"Hot Spot Analysis"** and select:
   **Hot Spot Analysis (Getis-Ord Gi*)**
   - Found under: Spatial Statistics Tools > Mapping Clusters

2. Configure the tool:
   - **Input Feature Class:** your AI cities layer
   - **Input Field:** select your AI works field (same one you used for Moran's I)
   - **Output Feature Class:** name it something like `ai_cities_hotspots`
   - **Conceptualization of Spatial Relationships:** use the same setting as Moran's I for consistency (e.g., **K Nearest Neighbors**)
   - **Number of Neighbors:** **8** (same as Moran's I)
   - **Distance Method:** **Euclidean Distance**
   - **Standardization:** **Row**

3. Click **Run**.

4. **The output layer** will be added to your map automatically. It contains new fields:
   - **Gi_Bin:** classification (-3, -2, -1, 0, 1, 2, 3)
     - 3 = hot spot at 99% confidence
     - 2 = hot spot at 95% confidence
     - 1 = hot spot at 90% confidence
     - 0 = not significant
     - -1 = cold spot at 90% confidence
     - -2 = cold spot at 95% confidence
     - -3 = cold spot at 99% confidence
   - **Gi_ZScore:** the z-score for each city
   - **Gi_PValue:** the p-value for each city

5. **Symbolize the results:**
   - Right-click the output layer > **Symbology**
   - Choose **Unique Values** on the **Gi_Bin** field
   - ArcGIS Pro may auto-apply a red-to-blue diverging scheme
   - Recommended colors:
     - 3 (hot 99%): dark red
     - 2 (hot 95%): orange/salmon
     - 0 (not significant): light grey
     - -2 (cold 95%): light blue
     - -3 (cold 99%): dark blue
   - This should match your existing Figure 11 color scheme

6. **Verify the counts** against your Python results:
   - Open the attribute table, sort by Gi_Bin
   - You should see approximately:
     - Hot spot 99%: 1 city (Macau)
     - Hot spot 95%: 6 cities
     - Not significant: ~279 cities
     - Cold spot 95%: ~23 cities
     - Cold spot 99%: ~10 cities
   - Small count differences (±1-2) are normal due to differences in spatial weights construction

7. **Export for StoryMap:**
   - Right-click the output layer > **Share** > **Share as Web Layer**
   - Or export as GeoJSON: right-click > **Data** > **Export Features**

---

## Method 3 (Optional): Optimized Hot Spot Analysis

ArcGIS Pro also offers an **Optimized Hot Spot Analysis** tool that 
automatically selects parameters. This can be useful as a robustness check.

### Steps:

1. Search for **"Optimized Hot Spot Analysis"** in the Geoprocessing pane.
   - Found under: Spatial Statistics Tools > Mapping Clusters

2. Configure:
   - **Input Feature Class:** your AI cities layer
   - **Analysis Field:** your AI works field
   - **Output Feature Class:** name it `ai_cities_hotspots_optimized`
   - Leave other settings at defaults — the tool auto-selects the distance band and aggregation method.

3. Click **Run**.

4. Compare the output to your manual Gi* results. If the same cities appear 
   as hot/cold spots, that's a robustness confirmation you can mention in the 
   StoryMap: "Results were confirmed using both manual and optimized 
   parameterizations of the Getis-Ord Gi* tool in ArcGIS Pro."

---

## Method 4 (Optional): Cluster and Outlier Analysis (Anselin Local Moran's I / LISA)

This is the alternative method mentioned in your Finding 3 text. It provides 
a local decomposition of Moran's I and distinguishes four types of clusters.

### Steps:

1. Search for **"Cluster and Outlier Analysis"** in the Geoprocessing pane.
   - Found under: Spatial Statistics Tools > Mapping Clusters

2. Configure:
   - **Input Feature Class:** your AI cities layer
   - **Input Field:** your AI works field
   - **Output Feature Class:** name it `ai_cities_lisa`
   - **Conceptualization of Spatial Relationships:** K Nearest Neighbors
   - **Number of Neighbors:** 8

3. Click **Run**.

4. The output contains a **COType** field with four categories:
   - **HH** — high value surrounded by high values (AI research cluster)
   - **LL** — low value surrounded by low values (AI research desert)
   - **HL** — high value surrounded by low values (spatial outlier — overperformer)
   - **LH** — low value surrounded by high values (spatial outlier — underperformer)

5. This could be a powerful supplementary figure showing which cities 
   outperform or underperform their neighborhoods — directly feeding into 
   your case study typology (Singapore = HH, Seoul = LH, Ho Chi Minh City = HL, 
   Lagos = LL).

---

## Which results to cite in the StoryMap

For the EIP submission, you want to be able to say:

"Spatial autocorrelation was assessed using Global Moran's I and local 
clustering was mapped using Getis-Ord Gi* Hot Spot Analysis, both 
implemented in the ArcGIS Pro Spatial Statistics toolbox."

This single sentence:
- Names two specific tools (judges score "Implementation")
- Names the toolbox (Spatial Statistics)
- Names the platform (ArcGIS Pro)
- Demonstrates breadth of GIS usage

If your Python results and ArcGIS Pro results are consistent (same direction, 
same significance, similar counts), note that in the methods:

"Results were validated across both Python (PySAL/scipy) and ArcGIS Pro 
implementations, with consistent cluster assignments."

This signals reproducibility — the quality that earned [FIS-2025-UG-1] 
the "open science" praise.

---

## Troubleshooting

**"The tool requires projected coordinates"**
- If your data is in WGS84 (EPSG:4326), some tools may warn about 
  geographic coordinates. You can either:
  - Project your data to a global equal-area projection first 
    (e.g., World Mollweide, EPSG:54009)
  - Or use the Geodesic distance option if available
  - For K Nearest Neighbors with Euclidean distance at global scale, 
    WGS84 typically works fine since neighbor rankings are preserved

**Counts don't exactly match Python**
- Small differences (±1-2 cities changing class) are expected when 
  spatial weights construction differs slightly between implementations.
- Report the ArcGIS Pro numbers in your StoryMap since that's the 
  tool you're crediting.

**Tool runs slowly**
- 319 points is a very small dataset for these tools. If it takes 
  more than a few seconds, check that you're not accidentally running 
  it on the full 8,000-city layer.
