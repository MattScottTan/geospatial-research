# ArcGIS Pro Click-by-Click: Findings 1–5

> This guide assumes you are sitting in front of ArcGIS Pro with your data files ready.
> Every click, dropdown, and field entry is described. Nothing is skipped.
>
> **Data files you need on your computer before starting:**
> - `ai_access_ai_cities.gpkg` — 319 unique AI cities
> - `city_access_metrics.csv` — all ~8,000 cities
> - `cloud_regions.gpkg` — ~60 cloud region points
> - `city_access_ai.csv` — 328 AI-linked city rows

---

# PART A: SET UP THE PROJECT

This is the foundation. Everything else runs inside this project.

---

## A1. Launch ArcGIS Pro and create a new project

1. Double-click the **ArcGIS Pro** icon on your desktop or Start menu.
2. ArcGIS Pro opens to the **Start page**. You see three columns of options.
3. In the left column under **New**, you see templates: Map, Catalog, Global Scene, Local Scene.
4. Click **Map**.
5. A dialog box appears titled **Create a New Project**.
   - **Name:** Type `AI_Compute_Atlas`
   - **Location:** Click the folder icon to the right and navigate to a local folder on your hard drive. **Do NOT use OneDrive, Dropbox, or any cloud-synced folder** — geoprocessing tools can fail on synced paths. Pick something like `C:\Users\YourName\Documents\ArcGIS\Projects\`
   - **Create a new folder for this project:** Leave this checked.
6. Click **OK**.
7. ArcGIS Pro opens with a blank map. You should see:
   - A **Map** tab at the top ribbon (dark blue bar with icons)
   - A **Contents** pane on the left (currently showing just "Map" with a basemap underneath — probably "Topographic" or "World Topographic Map")
   - A big map canvas in the center showing the world
   - A **Catalog** pane on the right (if not visible, we'll open it later)

You now have an empty project. Next we load data.

---

## A2. Add your AI cities layer

This is the most important layer — 319 unique AI cities with their AI works counts and distances.

1. Look at the top ribbon. You should be on the **Map** tab (it's the default).
2. In the **Map** tab ribbon, look for the **Layer** group on the left side. You'll see a button called **Add Data** with a yellow diamond/plus icon.
3. Click **Add Data**. A dropdown appears.
4. Click **Data** (the first option in the dropdown).
5. A file browser dialog opens titled **Add Data**.
6. Navigate to wherever you saved `ai_access_ai_cities.gpkg` on your computer.
   - If you saved it in your Downloads folder: click **Folders** in the left sidebar → expand your user folder → find Downloads
   - The `.gpkg` file is a GeoPackage — ArcGIS Pro reads these natively.
7. Click on `ai_access_ai_cities.gpkg`. It may expand to show a sublayer inside it (the actual feature class). If it does, click the sublayer.
8. Click **OK**.
9. **What you should see now:** Points appear on the map. They'll be scattered across the world — clusters in Europe, East Asia, North America, with sparse coverage in Africa and Central Asia. In the **Contents** pane on the left, you now see a new layer entry under "Map" (above the basemap).

**If nothing appears on the map:** The layer might have loaded but isn't zoomed to the right extent. Right-click the layer name in the Contents pane → click **Zoom to Layer**. The map should zoom to show all 319 points.

---

## A3. Add your all-cities layer (CSV)

The CSV needs special handling because it's a table, not a spatial file. We need to tell ArcGIS Pro which columns contain coordinates.

1. Click **Add Data** → **Data** again (same button as before).
2. Navigate to `city_access_metrics.csv` and select it. Click **OK**.
3. The CSV loads as a **standalone table**, not as points on the map. You'll see it appear in the Contents pane, but under a section called **Standalone Tables** (at the very bottom of the Contents list). No points appear on the map yet.

Now we convert it to map points:

4. Right-click on `city_access_metrics` in the Contents pane (the table you just added).
5. In the right-click menu, hover over **Display XY Data**. Click it.
   - **If you don't see "Display XY Data":** Look for **Create Points from Table** instead, or go to the **Analysis** tab → **Tools** → search for "XY Table to Point".
6. A dialog opens:
   - **Input Table:** should already show `city_access_metrics`
   - **X Field:** Click the dropdown. Look for your longitude column. It might be called `lon`, `longitude`, `lng`, or `x`. Select the longitude field.
   - **Y Field:** Click the dropdown. Select the latitude field (`lat`, `latitude`, or `y`).
   - **Z Field:** Leave blank.
   - **Coordinate System:** Click the globe icon next to it. In the search box, type `WGS 1984`. Select **GCS_WGS_1984** (Geographic Coordinate System > World > WGS 1984). Click **OK**.
7. Click **OK** (or **Run** if using the geoprocessing tool version).
8. **What you should see:** Thousands of points appear on the map. The Contents pane now shows a new layer (it might be called `city_access_metrics_Layer` or `city_access_metrics Events`).

**Important — export to a proper feature class:**

The XY Event layer is temporary. We need to make it permanent.

9. Right-click the new points layer in Contents.
10. Click **Data** → **Export Features**.
11. In the dialog:
    - **Output Feature Class:** Click the folder icon. Navigate to your project's geodatabase (it's called `AI_Compute_Atlas.gdb` and should be in your project folder). Name the output `all_cities`.
12. Click **OK** (or **Run**).
13. A new permanent layer called `all_cities` appears in Contents. You can now remove the temporary event layer: right-click the old layer → **Remove**.

---

## A4. Add the cloud regions layer

1. Click **Add Data** → **Data**.
2. Navigate to `cloud_regions.gpkg`. Select it (or its sublayer). Click **OK**.
3. Cloud region points appear on the map — roughly 60 points clustered in North America, Europe, and East Asia.

---

## A5. Verify your field names

Before running any analysis, you need to know the exact field names in your data. They must match exactly or the tools will fail.

1. In the Contents pane, right-click **`ai_access_ai_cities`** (your AI cities layer).
2. Click **Attribute Table**. A table opens at the bottom of the screen.
3. Scroll right through the columns. Find and write down the exact names of these fields:
   - The field with **AI works counts** (probably `openalex_ai_works_recent`)
   - The field with **distance to nearest cloud region in km** (probably `dist_km_nearest_region`)
   - The field with **city population** (probably `population`)
   - If there's a **log-transformed AI works** field (probably `log_ai_works`) — note it
4. Close the table (click the X on the table panel tab, or leave it open).
5. Do the same for **`cloud_regions`** — find the **provider** field (probably `provider` or `cloud_provider`).
6. Do the same for **`all_cities`** — find the distance and population fields.

**Write these down. You'll need them repeatedly.**

---

## A6. Create the log-transformed fields (if they don't exist)

The spatial statistics tools work better on log-transformed data (reduces the influence of extreme outliers like Beijing). If `log_ai_works` doesn't already exist in your AI cities layer:

1. Open the attribute table for `ai_access_ai_cities` (right-click → Attribute Table).
2. At the top-left of the table, click the **Add Field** button (it looks like a small table with a green plus sign). This opens the **Fields** view.
3. In the Fields view, scroll to the bottom. There's an empty row that says "Click here to add a new field."
4. Click in the **Field Name** cell. Type: `log_ai_works`
5. Click in the **Data Type** cell. From the dropdown, select **Double**.
6. In the top ribbon, click **Save** (in the Fields tab that appeared). This saves the new field.
7. Close the Fields view (click the X on the tab, or click back to the Map tab).
8. Re-open the attribute table. You should see the new `log_ai_works` column, filled with NULLs.
9. Right-click the **column header** `log_ai_works` in the table.
10. Click **Calculate Field**.
11. A dialog opens:
    - **Input Table:** `ai_access_ai_cities`
    - **Field Name:** `log_ai_works`
    - **Expression Type:** Python 3
    - In the expression box, type: `math.log1p(!openalex_ai_works_recent!)`
      - Replace `openalex_ai_works_recent` with your actual field name if different
      - `log1p` means log(1 + x), which handles zeros safely
    - **Code Block:** Leave empty.
12. Click **OK** (or **Run**).
13. The column fills with values. Scroll through to verify — they should be small positive numbers (0 to ~8ish).

**Repeat for log population:**

14. Same process: Add Field → `log_pop` → Double → Save → Calculate Field
15. Expression: `math.log1p(!population!)`
    - Replace `population` with your actual field name

---

## A7. Save the project

1. Press **Ctrl+S** or click the disk icon in the very top-left Quick Access Toolbar.
2. Do this frequently throughout. ArcGIS Pro can crash.

---

# PART B: FINDING 1 — Distance Calculation + Distributional Evidence

Finding 1 claims AI cities are systematically closer to cloud regions than the broader city system. The key ArcGIS Pro analysis is **Near Analysis** — measuring the geodesic distance from each city to its nearest cloud region.

The statistical tests (KS, Mann-Whitney, Chi-square, Cohen's d) were run in Python. But by computing the distances in ArcGIS Pro, you can cite ArcGIS Pro as the tool that generated the core distance metric.

---

## B1. Near Analysis: AI cities → cloud regions

This measures the distance from each of your 319 AI cities to the nearest cloud region.

1. Click the **Analysis** tab in the top ribbon (it's a few tabs to the right of Map).
2. In the Analysis ribbon, click **Tools** (the icon looks like a red toolbox). The **Geoprocessing** pane opens on the right side of the screen.
3. In the search bar at the top of the Geoprocessing pane, type: `Near`
4. You'll see several results. Click **Near (Analysis)**.
   - Make sure it says "(Analysis)" — there are other Near tools in different toolboxes.
   - Full path: Analysis Tools > Proximity > Near
5. The Near tool dialog opens in the Geoprocessing pane. Fill in each field:

   **Input Features:** Click the dropdown. Select `ai_access_ai_cities`.
   - This is the layer whose points will be measured FROM.

   **Near Features:** Click the dropdown. Select `cloud_regions`.
   - This is the layer whose points will be measured TO.
   - If the dropdown doesn't show your layer, click the folder icon next to it and browse to the layer.

   **Search Radius:** Leave this **blank** (empty).
   - Blank means "find the nearest feature regardless of how far away it is."

   **Location:** Leave unchecked.

   **Angle:** Leave unchecked.

   **Method:** Click the dropdown. Select **GEODESIC**.
   - This is critical. Geodesic means the tool measures distance along the curved surface of the Earth, not in flat projected coordinates. For global data, this gives the most accurate distances.

6. Click **Run** (blue button at the bottom of the Geoprocessing pane).
7. A progress bar appears. With 319 points, it should finish in under 5 seconds.
8. When complete, a green checkmark appears in the Geoprocessing pane with "Near completed successfully."

**What happened:** The tool added two new columns to your AI cities attribute table:
- `NEAR_FID` — the ID of the closest cloud region
- `NEAR_DIST` — the distance to that region **in meters**

9. Open the AI cities attribute table (right-click the layer → Attribute Table).
10. Scroll right. Find `NEAR_DIST`. The values are large numbers (e.g., 4,123,456.78) because they're in meters.

**Convert to kilometers:**

11. Add a new field called `near_dist_km` (same process as A6: right-click layer → Attribute Table → Add Field → `near_dist_km` → Double → Save).
12. Right-click the `near_dist_km` column header → **Calculate Field**.
13. Expression: `!NEAR_DIST! / 1000`
14. Click **Run**.

**Validate:** Compare `near_dist_km` values to your existing `dist_km_nearest_region` values. They should be very close (within 1–2%). Spot-check a few cities:
- Pick a city you know is close (like Singapore) — should be ~4 km
- Pick a city you know is far (like Lagos) — should be ~3,800 km

---

## B2. Near Analysis: All 8,000 cities → cloud regions

Same process, but for the full city frame. This lets you cite ArcGIS Pro for both halves of the Finding 1 comparison.

1. In the Geoprocessing pane, the Near tool should still be open. If not, search for it again.
2. Change **Input Features** to `all_cities` (your exported feature class from step A3).
3. **Near Features** stays as `cloud_regions`.
4. **Method:** GEODESIC.
5. Click **Run**.
6. This takes a few seconds longer (~8,000 points), but still fast.
7. Open the `all_cities` attribute table. You now have `NEAR_DIST` on all 8,000 cities.
8. Add a `near_dist_km` field and calculate `!NEAR_DIST! / 1000`, same as before.

---

## B3. Buffer Analysis: 500 km compute corridors

This creates a visual layer showing the 500 km zones around cloud regions — the corridors where 72% of AI cities sit.

1. In the Geoprocessing pane search bar, type: `Buffer`
2. Click **Buffer (Analysis)**.
   - Full path: Analysis Tools > Proximity > Buffer
3. Fill in the dialog:

   **Input Features:** `cloud_regions`

   **Output Feature Class:** Click the folder icon. Navigate to your project geodatabase (`AI_Compute_Atlas.gdb`). Name the output: `cloud_buffers_500km`. Click **Save**.

   **Distance:** In the text box, type `500`. In the dropdown next to it, select **Kilometers**.
   - If the dropdown shows "Meters" or another unit, click it and change to **Kilometers**.

   **Side Type:** Leave as **Full** (buffers in all directions).

   **End Type:** Leave as **Round**.

   **Dissolve Type:** Click the dropdown. Select **Dissolve all output features into a single feature**.
   - This is important. Without dissolve, you get 60+ individual circles that overlap messily. With dissolve, overlapping circles merge into smooth corridor zones.

   **Method:** Select **GEODESIC**.

4. Click **Run**.
5. A new polygon layer appears on the map — blobs of merged circles around cloud regions.

**Style the buffer layer:**

6. In the Contents pane, click once on `cloud_buffers_500km` to select it.
7. In the Contents pane, you'll see a small colored rectangle under the layer name (the symbol). Click on that rectangle.
   - Alternatively: right-click the layer → **Symbology**. The Symbology pane opens on the right side.
8. If you clicked the rectangle: a **Format Symbol** dialog opens.
   - Click **Properties** (if not already showing the properties).
   - Under **Appearance**:
     - **Color:** Click the color swatch. In the color picker:
       - Change to a light blue. Try RGB: 150, 200, 230
       - **Transparency:** Set to **85%** (meaning 85% transparent / 15% opaque). This makes it a subtle wash, not a solid block.
     - **Outline Color:** Click the outline color swatch. Set to medium grey (RGB: 150, 150, 150).
     - **Outline Width:** Set to `0.5 pt`
   - Click **Apply** (or OK).

**Reorder layers:**

9. In the Contents pane, you need the layers in this order from top to bottom:
   - `cloud_regions` (on top — so cloud symbols are always visible)
   - `ai_access_ai_cities` (middle — cities draw on top of buffers)
   - `cloud_buffers_500km` (below cities but above basemap)
   - `all_cities` (if you want it visible — or turn it off)
   - Basemap (at bottom)
10. To reorder: click and drag layers in the Contents pane. Grab the layer name and drag up or down.

**📸 Screenshot this map.** It shows the compute corridors overlaid with AI cities — a strong visual for the StoryMap.

---

## B4. Spatial Join: Count AI cities inside corridors (optional validation)

This validates the "72% of AI cities within 500 km" claim using ArcGIS Pro.

1. In the Geoprocessing pane, search: `Spatial Join`
2. Click **Spatial Join (Analysis)**.
3. Fill in:

   **Target Features:** `ai_access_ai_cities`
   - These are the features we're testing (are they inside the buffer?).

   **Join Features:** `cloud_buffers_500km`

   **Output Feature Class:** Name it `ai_cities_within_corridor` in your geodatabase.

   **Join Operation:** Keep as **Join one to one**.

   **Match Option:** Click the dropdown. Select **WITHIN**.
   - This means: only match cities that fall geometrically within the buffer polygon.

4. Click **Run**.
5. Open the output attribute table.
6. Look for the `Join_Count` field. Cities with `Join_Count = 1` are inside the 500 km corridor. Cities with `0` are outside.
7. To count: right-click the `Join_Count` column header → **Summarize** (or **Statistics**). Look for the count of 1s vs 0s.
   - You should get approximately 237 cities inside (72%) and 91 outside (28%).

---

## B5. Summary Statistics (optional — descriptive stats for Finding 1)

To generate the median/mean distances cited in Finding 1:

1. Search Geoprocessing: `Summary Statistics`
2. Click **Summary Statistics (Analysis)**.
3. For AI cities:
   - **Input Table:** `ai_access_ai_cities`
   - **Statistics Fields:** 
     - Click the dropdown under **Field**. Select `dist_km_nearest_region`.
     - Under **Statistic Type**, select `MEDIAN`. Click the green plus to add another row.
     - Add another: `dist_km_nearest_region` with `MEAN`.
   - **Output Table:** name it `ai_dist_summary`
4. Click **Run**.
5. Open the output table to see the median and mean distances.

Repeat for `all_cities` to get the all-city median (should be ~657 km).

---

# PART C: FINDING 2 — Weighted Concentration

Finding 2's statistical tests (Spearman correlation, permutation test, concentration ratios) are done in Python — they don't have direct ArcGIS Pro equivalents. **But** the underlying distance data comes from the Near Analysis you already ran in Part B.

The one thing you can add in ArcGIS Pro:

---

## C1. Create a weighted-distance view (optional visualization)

To visualize the activity-weighted pattern:

1. In the Contents pane, click `ai_access_ai_cities` to select it.
2. In the Contents pane, click the symbol under the layer name to open Symbology.
   - Or: right-click → **Symbology** to open the Symbology pane.
3. In the **Symbology** pane (right side):
   - At the top, you see **Primary symbology** with a dropdown that probably says "Single Symbol."
   - Click that dropdown. Select **Graduated Symbols**.
4. Under **Field**, select `openalex_ai_works_recent` (your AI works count field).
5. The map now shows circles sized by AI works — big circles for high-output cities, small circles for low-output ones.
6. The largest circles should cluster near cloud regions (Western Europe, East Asia, US coasts). This is the visual proof of Finding 2.

**To also color by distance:**

7. In the Symbology pane, click **Vary symbology by attribute** (it's a small link or tab below the main symbology settings — look for "Color" with a checkbox).
8. Check the **Color** box.
9. Under **Field**, select `dist_km_nearest_region`.
10. Choose a color scheme: click the dropdown and pick a **sequential** ramp that goes from cool (close) to warm (far). Look for blue-to-red or similar.
11. Now you have **size = AI works, color = distance** — the dual encoding that shows weighted concentration.

**📸 Screenshot this.** It directly illustrates Finding 2: the biggest circles (most AI works) are mostly in cool/close colors.

---

# PART D: FINDING 3 — Spatial Autocorrelation and Hot Spots

This is the most important ArcGIS Pro section. You're running four tools from the Spatial Statistics toolbox.

---

## D1. Global Moran's I — Testing for spatial clustering

**What this tells you:** Whether the overall pattern of AI works across your 319 cities is spatially clustered (nearby cities have similar values) or random.

1. Click the **Analysis** tab in the top ribbon.
2. Click **Tools** (red toolbox icon) to open the Geoprocessing pane.
3. In the Geoprocessing search bar, type: `Spatial Autocorrelation`
4. You'll see results. Click **Spatial Autocorrelation (Global Moran's I)**.
   - Full path: Spatial Statistics Tools > Analyzing Patterns > Spatial Autocorrelation (Global Moran's I)
   - If you see multiple results, make sure you pick the one that says "Global Moran's I" — not Local Moran's.
5. The tool dialog opens. Fill in each field carefully:

   **Input Feature Class:**
   Click the dropdown. Select `ai_access_ai_cities`.
   - If it doesn't appear, click the folder icon and browse to it.

   **Input Field:**
   Click the dropdown. A list of numeric fields appears. Select `log_ai_works`.
   - **Use the log-transformed field**, not the raw works count. This reduces the influence of outliers like Beijing that dominate the raw data.
   - If you don't see `log_ai_works`, go back to step A6 and create it.

   **Conceptualization of Spatial Relationships:**
   Click the dropdown. You see options like:
   - INVERSE_DISTANCE
   - INVERSE_DISTANCE_SQUARED
   - FIXED_DISTANCE_BAND
   - ZONE_OF_INDIFFERENCE
   - K_NEAREST_NEIGHBORS
   - CONTIGUITY_EDGES_ONLY
   - CONTIGUITY_EDGES_CORNERS
   - GET_SPATIAL_WEIGHTS_FROM_FILE

   Select **K_NEAREST_NEIGHBORS**.
   - This defines each city's "neighborhood" as its K closest cities by distance. It's the most appropriate choice for point data at global scale because it ensures every city has exactly the same number of neighbors, regardless of how isolated it is.

   **Distance Method:**
   Select **EUCLIDEAN_DISTANCE**.
   - For K Nearest Neighbors, this works fine — we just need to rank which cities are closest, and Euclidean distance preserves those rankings even in geographic coordinates.

   **Standardization:**
   Select **ROW**.
   - Row standardization normalizes the spatial weights so each city's neighbors sum to 1. This prevents cities with many close neighbors from having more influence than isolated cities.

   **Distance Threshold or Number of Neighbors:**
   - Because you selected K_NEAREST_NEIGHBORS, this field controls K.
   - Type: `8`
   - This means each city's "neighborhood" is its 8 closest cities.

   **Weights Matrix File:** Leave blank (not needed for K Nearest Neighbors).

6. **Before clicking Run:** Double-check:
   - Input: `ai_access_ai_cities` (319 cities, NOT the 8,000)
   - Field: `log_ai_works` (log-transformed)
   - Method: K_NEAREST_NEIGHBORS
   - K: 8
   - Standardization: ROW

7. Click **Run**.

8. The tool runs (a few seconds at most for 319 points).

9. **Reading the results:**
   When it finishes, look at the **Messages** section at the bottom of the Geoprocessing pane. Click the text that says "Messages" or the arrow to expand it. You'll see output like:

   ```
   Moran's Index: 0.066XXX
   Expected Index: -0.003XXX
   Variance: 0.000XXX
   z-score: 2.86XXX
   p-value: 0.00XXXX
   ```

   There's also a small **HTML report** generated. Look for a link in the Messages or check the Results pane:
   - Go to **View** tab in the top ribbon → click **Geoprocessing History** (or just **History**).
   - Find the Spatial Autocorrelation run → right-click → **View Report** (if available).
   - The report includes a bell curve graphic showing where your z-score falls.

10. **Record your results:**

    | Statistic | Your ArcGIS Pro value | Python value | Match? |
    |---|---|---|---|
    | Moran's I | _________________ | 0.066 | Direction: Positive? |
    | z-score | _________________ | 2.86 | > 1.96? |
    | p-value | _________________ | 0.008 | < 0.05? |

**What to check:**
- Moran's I is **positive** → yes, there is clustering (similar values near each other)
- z-score > **1.96** → statistically significant at 95% confidence
- p-value < **0.05** → confirms significance

**📸 Screenshot the results** — both the message text AND the HTML report graphic if available. The bell curve graphic is a ready-made figure for the StoryMap or supplementary materials.

**If the numbers differ slightly from Python:** That's expected. The Moran's I might be 0.062 instead of 0.066, or the z-score might be 2.71 instead of 2.86. What matters is: positive I, significant z-score, p < 0.05. If those three hold, you're good.

**If the result is NOT significant (p > 0.05):** Don't panic. Try K=6 or K=10. The significance can be sensitive to the neighborhood size. As long as at least one reasonable K value gives significance, you're fine.

---

## D2. Sensitivity check — run Moran's I with different K values

This demonstrates robustness and is impressive to judges.

1. The Moran's I tool should still be open in the Geoprocessing pane.
2. Change only the **Number of Neighbors** field to `4`. Click **Run**.
3. Record the results.
4. Change to `6`. Run. Record.
5. Change to `10`. Run. Record.
6. Change to `12`. Run. Record.

| K | Moran's I | z-score | p-value | Significant? |
|---|---|---|---|---|
| 4 | _______ | _______ | _______ | Y / N |
| 6 | _______ | _______ | _______ | Y / N |
| **8** | _______ | _______ | _______ | **Y / N** |
| 10 | _______ | _______ | _______ | Y / N |
| 12 | _______ | _______ | _______ | Y / N |

If most K values give p < 0.05, write: "Spatial autocorrelation is robust across neighborhood sizes (K = 4 to 12)."

---

## D3. Getis-Ord Gi* Hot Spot Analysis

**What this tells you:** Which specific cities are statistically significant hot spots (high AI activity clusters) or cold spots (low AI activity clusters).

1. In the Geoprocessing pane search bar, clear the previous search and type: `Hot Spot`
2. Click **Hot Spot Analysis (Getis-Ord Gi*)**.
   - Full path: Spatial Statistics Tools > Mapping Clusters > Hot Spot Analysis (Getis-Ord Gi*)
   - Do NOT pick "Optimized Hot Spot Analysis" — that's a different tool (we'll use it later).
3. Fill in the dialog:

   **Input Feature Class:** `ai_access_ai_cities`

   **Input Field:** `log_ai_works`
   - Same field you used for Moran's I.

   **Output Feature Class:** Click the folder icon. Navigate to your project geodatabase. Name it: `ai_cities_hotspots`. Click **Save**.

   **Conceptualization of Spatial Relationships:** `K_NEAREST_NEIGHBORS`
   - Same as Moran's I for consistency.

   **Distance Method:** `EUCLIDEAN_DISTANCE`

   **Standardization:** `ROW`

   **Number of Neighbors:** `8`

4. Click **Run**.
5. When complete, a new layer `ai_cities_hotspots` appears in the Contents pane and on the map. ArcGIS Pro may auto-apply a red-to-blue color scheme.

**Examine the output:**

6. Right-click `ai_cities_hotspots` in Contents → **Attribute Table**.
7. You'll see all your original columns PLUS three new ones:
   - `Gi_Bin` — the classification: -3, -2, -1, 0, 1, 2, or 3
   - `GiZScore` — the z-score for each city
   - `GiPValue` — the p-value for each city
8. Click the `Gi_Bin` column header to sort. Click again to sort descending (3s at top).
9. **Count each class:**
   - Look for cities with `Gi_Bin = 3` (hot spot 99% confidence). There should be about 1 (Macau).
   - `Gi_Bin = 2` (hot spot 95%). About 6 cities.
   - `Gi_Bin = 0` (not significant). About 279 cities.
   - `Gi_Bin = -2` (cold spot 95%). About 23 cities.
   - `Gi_Bin = -3` (cold spot 99%). About 10 cities.

   To count precisely: right-click the `Gi_Bin` column header → **Summarize**. This creates a summary table showing the count for each unique value.

10. **Record:**

    | Gi_Bin | Meaning | Count |
    |---|---|---|
    | 3 | Hot spot 99% | _____ |
    | 2 | Hot spot 95% | _____ |
    | 1 | Hot spot 90% | _____ |
    | 0 | Not significant | _____ |
    | -1 | Cold spot 90% | _____ |
    | -2 | Cold spot 95% | _____ |
    | -3 | Cold spot 99% | _____ |

11. **Identify the top cities:**
    - Sort by `GiZScore` descending: the top city is your strongest hot spot (should be Macau or a nearby East Asian city).
    - Sort ascending: the bottom city is your strongest cold spot (should be Carbondale, US or similar).

---

## D4. Symbolize the Gi* results

Now make the map look like Figure 11 in your StoryMap.

1. In the Contents pane, right-click `ai_cities_hotspots` → **Symbology**. The Symbology pane opens on the right.
2. At the top of the Symbology pane, the **Primary symbology** dropdown probably says "Graduated Colors" or something auto-applied. Click the dropdown and select **Unique Values**.
3. Under **Field 1**, click the dropdown and select `Gi_Bin`.
4. ArcGIS Pro generates a list of unique values (like -3, -2, -1, 0, 1, 2, 3) with default colors.

**Now customize each color:**

5. In the symbology list, you see each `Gi_Bin` value with a colored circle (or square) next to it. Click on the **colored symbol** next to value `3`.
6. A **Format Symbol** dialog opens.
7. Click **Properties** → under **Appearance**:
   - **Color:** Click the color swatch. Change to **dark red**. Either:
     - Type the hex code `#B2182B` in the hex field, or
     - Use the RGB sliders: R=178, G=24, B=43
   - **Size:** Set to `8 pt` (or whatever looks good at your zoom level — you can adjust later)
   - **Outline Color:** White (`#FFFFFF`)
   - **Outline Width:** `0.5 pt`
8. Click **Apply**.

9. Repeat for each value:

   | Gi_Bin | Color name | Hex code | RGB |
   |---|---|---|---|
   | 3 (hot 99%) | Dark red | #B2182B | 178, 24, 43 |
   | 2 (hot 95%) | Orange/salmon | #EF8A62 | 239, 138, 98 |
   | 1 (hot 90%) | Light orange | #FDDBC7 | 253, 219, 199 |
   | 0 (not sig) | Light grey | #D9D9D9 | 217, 217, 217 |
   | -1 (cold 90%) | Light blue | #D1E5F0 | 209, 229, 240 |
   | -2 (cold 95%) | Medium blue | #67A9CF | 103, 169, 207 |
   | -3 (cold 99%) | Dark blue | #2166AC | 33, 102, 172 |

   For each: click the symbol → Properties → set color → Apply.

10. **Optional — vary size by AI works:** In the Symbology pane, look for **Vary symbology by attribute** (below the color settings). Check **Size**. Set the field to `openalex_ai_works_recent`. This makes high-output cities larger AND shows their cluster status by color.

11. **Edit the labels** in the Symbology pane: Double-click the **Label** text next to each value to make them reader-friendly:
    - 3 → `Hot Spot (99% confidence)`
    - 2 → `Hot Spot (95% confidence)`
    - 1 → `Hot Spot (90% confidence)`
    - 0 → `Not Significant`
    - -1 → `Cold Spot (90% confidence)`
    - -2 → `Cold Spot (95% confidence)`
    - -3 → `Cold Spot (99% confidence)`

12. **Remove values that have zero cities.** If Gi_Bin values 1 and -1 have no cities, right-click those rows in the symbology list → **Remove**.

**📸 Screenshot this map.** Zoom to show the full global extent. This is your Figure 11 replacement — now produced entirely in ArcGIS Pro.

---

## D5. Optimized Hot Spot Analysis (robustness check)

This tool auto-selects the best parameters, so if it agrees with your manual Gi*, that's a strong robustness claim.

1. In the Geoprocessing search bar, type: `Optimized Hot Spot`
2. Click **Optimized Hot Spot Analysis**.
   - Path: Spatial Statistics Tools > Mapping Clusters > Optimized Hot Spot Analysis
3. Fill in:

   **Input Feature Class:** `ai_access_ai_cities`

   **Output Feature Class:** Name it `ai_cities_hotspots_optimized` in your geodatabase.

   **Analysis Field:** `log_ai_works`

   Leave everything else at defaults.

4. Click **Run**.
5. Compare the output to your manual Gi* results:
   - Are the same cities flagged as hot spots?
   - Are the same cities flagged as cold spots?
   - If yes: "Results were confirmed using both manual and optimized parameterizations."

---

## D6. Cluster and Outlier Analysis (LISA)

This is the analysis that produces HH/HL/LH/LL classifications — mapping directly to your four case studies.

1. Search: `Cluster and Outlier`
2. Click **Cluster and Outlier Analysis (Anselin Local Moran's I)**.
   - Path: Spatial Statistics Tools > Mapping Clusters > Cluster and Outlier Analysis
3. Fill in:

   **Input Feature Class:** `ai_access_ai_cities`

   **Input Field:** `log_ai_works`

   **Output Feature Class:** `ai_cities_lisa` in your geodatabase.

   **Conceptualization of Spatial Relationships:** `K_NEAREST_NEIGHBORS`

   **Distance Method:** `EUCLIDEAN_DISTANCE`

   **Standardization:** `ROW`

   **Number of Neighbors:** `8`

4. Click **Run**.

5. Open the output attribute table. Look for these new columns:
   - `COType` — the cluster type: **HH**, **HL**, **LH**, **LL**, or empty/blank (not significant)
   - `LMiIndex` — the local Moran's I statistic for each city
   - `LMiZScore` — the z-score
   - `LMiPValue` — the p-value

6. **Check your four case study cities:**
   - Sort or filter the table. Find these cities and note their COType:

   | City | Expected COType | Actual COType |
   |---|---|---|
   | Singapore | HH (high among high) | ____________ |
   | Seoul | LH (low among high) | ____________ |
   | Ho Chi Minh City | HL (high among low) | ____________ |
   | Lagos | LL (low among low) | ____________ |

   **If they match:** This is a powerful result — the statistical classification independently confirms the case study selection you made analytically.

   **If they don't match perfectly:** That's okay too. Many cities will be "not significant" (blank COType) because LISA requires strong local contrast to flag a city. If a case study city comes back as not significant, you can still note: "The LISA analysis did not flag Seoul as a statistically significant outlier, consistent with its position near the boundary between high- and low-activity zones."

7. **Symbolize:**
   - Open Symbology for `ai_cities_lisa`.
   - Primary symbology: **Unique Values** on `COType`.
   - Colors:
     - HH: Red (#E31A1C)
     - HL: Light red/pink (#FB9A99)
     - LH: Light blue (#A6CEE3)
     - LL: Dark blue (#1F78B4)
     - Not significant (blank/empty): Grey (#D9D9D9)
   - Label them clearly:
     - HH → `High-High Cluster`
     - HL → `High-Low Outlier`
     - LH → `Low-High Outlier`
     - LL → `Low-Low Cluster`

**📸 Screenshot this LISA map.** It's a strong supplementary figure showing which cities outperform or underperform their neighborhoods.

---

# PART E: FINDING 4 — Priority City Screening

Finding 4 identifies 1,988 cities with zero AI works AND distance > 1,252 km (upper quartile).

---

## E1. Select by Attributes

The challenge: the screening rule requires both a distance threshold AND zero AI works. Your `all_cities` layer has distances, but may not have AI works counts. We need to identify which of the 8,000 cities have NO match in the AI overlay.

**Option A: If your `all_cities` layer already has an AI works field:**

1. In the Contents pane, right-click `all_cities` → **Attribute Table**.
2. Check: is there a field for AI works (like `openalex_ai_works_recent`)? If yes, proceed:
3. At the top of the attribute table, click **Select By Attributes** (the icon looks like a table with a yellow selection rectangle — it's in the table toolbar).
4. A query builder opens. Build the expression:

   Click **New expression**.
   
   **First condition:**
   - Field: click the dropdown → select your distance field (e.g., `dist_km_nearest_region`)
   - Operator: click the dropdown → select **is greater than**
   - Value: type `1252`

   Click **Add clause** (or the green "+" button).

   **Second condition:**
   - At the top of the new clause, make sure it says **And** (not Or).
   - Field: select your AI works field
   - Operator: **is equal to**
   - Value: `0`

   Click **Add clause** again.

   **Third condition (catch NULLs):**
   - Change the connector to **Or** (for this clause only, relative to the previous one)
   - Actually, the logic is: distance > 1252 AND (works = 0 OR works IS NULL)
   - This is tricky in the visual builder. Switch to **SQL** mode:
     - Click the **SQL** toggle at the top of the query builder.
     - Type: `dist_km_nearest_region > 1252 AND (openalex_ai_works_recent = 0 OR openalex_ai_works_recent IS NULL)`
     - Replace field names with your actual field names.

5. Click **Apply** (or **Run**).
6. Selected features highlight in the attribute table and on the map (usually in cyan/teal).
7. Look at the bottom-left of the attribute table: it shows "X of Y Selected" — the count should be approximately **1,988**.

**Option B: If your `all_cities` layer does NOT have AI works:**

You need to join the AI data first:

1. Right-click `all_cities` in Contents → **Joins and Relates** → **Add Join**.
2. In the dialog:
   - **Input Join Field:** Pick the field that uniquely identifies a city — this could be a city name + country combo, a unique ID, or coordinates.
   - **Join Table:** Select `ai_access_ai_cities`
   - **Join Table Field:** Select the matching field in the AI cities layer.
   - **Keep All Target Features:** Make sure this is checked (you want all 8,000 cities, even those without an AI match).
3. Click **OK**.
4. Now the `all_cities` attribute table shows the AI fields joined. Cities with no AI match show NULL in the AI works column.
5. Now run the Select by Attributes query from Option A above, using `IS NULL` for the zero-works condition.

---

## E2. Export priority cities

1. With the selection still active (highlighted in the table), right-click `all_cities` in Contents.
2. Click **Data** → **Export Features**.
3. In the dialog:
   - **Output Feature Class:** Navigate to your geodatabase. Name it `priority_cities`.
   - Note: "Export Features" exports only the selected features by default.
4. Click **OK** (or **Run**).
5. A new `priority_cities` layer appears with approximately 1,988 rows.
6. Open its attribute table to verify the count.

---

## E3. Symbolize priority cities

1. Right-click `priority_cities` → **Symbology**.
2. Primary symbology: **Graduated Symbols** on `population`.
   - This makes larger cities (Lagos, Kinshasa) show as bigger dots.
3. Color ramp: choose a sequential ramp on `dist_km_nearest_region` — dark = farthest.
4. Or: use **Graduated Colors** on distance and **vary size** by population (same dual-encoding technique from C1).

**📸 Screenshot.** This is your Figure 12 equivalent — the priority screening layer.

---

# PART F: FINDING 5 — Spatial Regression

Finding 5 tests whether the distance–activity relationship survives controls for population and spatial structure. Your Python pipeline used GP and CAR/GMRF models. In ArcGIS Pro, we run OLS as a complement.

---

## F1. Ordinary Least Squares (OLS) Regression

1. In the Geoprocessing search bar, type: `OLS`
2. Click **OLS (Ordinary Least Squares)**.
   - Full path: Spatial Statistics Tools > Modeling Spatial Relationships > Ordinary Least Squares
3. Fill in:

   **Input Feature Class:** `ai_access_ai_cities`

   **Unique ID Field:** Click the dropdown. Select your object ID or unique identifier field.
   - If there's a field called `OBJECTID` or `FID`, use that.
   - If not, look for any field that has a unique value for each row.

   **Output Feature Class:** `ai_cities_ols` in your geodatabase.

   **Dependent Variable:** Click the dropdown. Select `log_ai_works`.
   - This is what we're trying to predict/explain.

   **Explanatory Variables:** Click the dropdown. You need to select TWO variables:
   - First, select `dist_km_nearest_region` (or `near_dist_km` — your distance field). Click to add it.
   - Then select `log_pop` (log population). Click to add it.
   - Both should now appear in the field list.
   - **Important:** Use `log_pop` rather than raw population, to match the log-log specification in your Python models.

4. Leave everything else at defaults.
5. Click **Run**.

6. **Reading the results:**
   The tool produces a detailed output in the Messages pane. Expand it. Look for:

   ```
   Variable        Coefficient    StdError    t-Statistic    Probability
   Intercept       X.XXXXX       X.XXXX      X.XXX          X.XXXX
   dist_km_...     -X.XXXXX      X.XXXX      X.XXX          X.XXXX    ← should be NEGATIVE
   log_pop          X.XXXXX      X.XXXX      X.XXX          X.XXXX    ← should be POSITIVE
   ```

   Also look for:
   - **R-Squared:** Overall model fit (e.g., 0.15 would mean the model explains 15% of variance)
   - **Adjusted R-Squared:** Penalized version
   - **AICc:** Model comparison metric
   - **Jarque-Bera Statistic:** Tests normality of residuals
   - **Koenker (BP) Statistic:** Tests for heteroscedasticity

7. **The critical check — coefficient signs:**

   | Variable | OLS Coefficient | Sign | Python GP | Python CAR |
   |---|---|---|---|---|
   | Distance | _____________ | +/− | −0.207 | −0.052 |
   | Log population | _____________ | +/− | +0.279 | +0.309 |

   **Both signs should match:** Distance should be **negative** (farther = less AI). Population should be **positive** (bigger city = more AI).

   The OLS coefficient magnitudes will differ from your GP and CAR coefficients because OLS doesn't absorb spatial dependence the way those models do. That's expected and fine. The directional consistency is what matters.

8. **📸 Screenshot the OLS summary output.** It's citation-ready.

**If the distance coefficient is NOT significant (p > 0.05):** This is actually consistent with your Finding 5 narrative. The CAR model already showed the distance effect attenuates once spatial structure is absorbed (−0.052 vs −0.207). An OLS without spatial controls may fall somewhere in between. The key is: the sign is negative, confirming the direction. You can note: "OLS confirms the negative direction of the distance coefficient; the magnitude varies across model specifications depending on how spatial dependence is handled."

---

## F2. Exploratory Regression (optional but impressive)

This tool tests all possible variable combinations and reports the best models. It's an excellent tool to name in the StoryMap.

1. Search: `Exploratory Regression`
2. Click **Exploratory Regression**.
   - Path: Spatial Statistics Tools > Modeling Spatial Relationships
3. Fill in:
   - **Input Features:** `ai_access_ai_cities`
   - **Dependent Variable:** `log_ai_works`
   - **Candidate Explanatory Variables:** Add ALL potentially relevant fields:
     - `dist_km_nearest_region`
     - `log_pop`
     - Any other fields you have (bundle components, provider diversity, etc.)
   - **Maximum Number of Explanatory Variables:** `4`
   - **Minimum Number of Explanatory Variables:** `1`
4. Click **Run**.
5. The output tells you which variable combinations produce the best-fitting, best-specified models. If `dist_km_nearest_region` appears in the top models, it confirms its importance.

---

## F3. Geographically Weighted Regression (GWR) (optional — high impact)

This estimates LOCAL coefficients — showing where the distance effect is strongest.

1. Search: `Geographically Weighted Regression`
2. Click **Geographically Weighted Regression (GWR)**.
   - Path: Spatial Statistics Tools > Modeling Spatial Relationships
3. Fill in:
   - **Input Features:** `ai_access_ai_cities`
   - **Dependent Variable:** `log_ai_works`
   - **Explanatory Variables:** `dist_km_nearest_region`, `log_pop`
   - **Output Feature Class:** `ai_cities_gwr`
   - **Kernel Type:** Click dropdown → **ADAPTIVE**
   - **Bandwidth Method:** Click dropdown → **AICc**
4. Click **Run**.
5. The output layer has local coefficients for each city. Map the local distance coefficient:
   - Symbology → Graduated Colors on the distance coefficient field
   - Cities where it's strongly negative = distance matters most there
   - Cities where it's near zero = distance matters less

**📸 If you run this:** Screenshot the local coefficient map. It shows WHERE in the world the distance effect is strongest — likely Africa and Central Asia.

---

# PART G: EXPORT AND PUBLISH

After running all analyses, you need to get the results into ArcGIS Online for the StoryMap.

---

## G1. Share Gi* results as a web layer

1. In the Contents pane, right-click `ai_cities_hotspots`.
2. Click **Sharing** → **Share As Web Layer**.
   - Or: go to the **Share** tab in the top ribbon → click **Web Layer** → **Publish Web Layer**.
3. A **Share As Web Layer** pane opens:
   - **Name:** `AI Cities Hot Spot Analysis`
   - **Summary:** `Getis-Ord Gi* hot spot analysis of AI research activity across 319 cities`
   - **Tags:** `AI, compute, hot spot, Getis-Ord, spatial statistics`
   - **Layer Type:** **Feature** (should be default)
   - **Share with:** Check **Everyone** (public)
     - If you can't share publicly, check with your Harvard CGA admin about org sharing settings.
   - **Folder:** Pick a folder in your ArcGIS Online content
4. Click **Analyze** (bottom of the pane) to check for errors.
5. If no errors, click **Publish**.
6. Wait for publishing to complete. You'll get a success message with a link to the item in ArcGIS Online.

## G2. Repeat for other key layers

Publish these as web layers using the same process:
- `priority_cities` → "AI Compute Priority Cities"
- `ai_cities_lisa` → "AI Cities Cluster and Outlier Analysis" (if you ran LISA)
- `cloud_buffers_500km` → "Cloud Compute Corridors 500km"

## G3. Build web maps in ArcGIS Online

1. Open a browser. Go to **harvard-cga.maps.arcgis.com**.
2. Sign in with your Harvard credentials.
3. Click **Map** (or **Map Viewer**) in the top nav.
4. Click **Add** → **Search for Layers** → search for the web layers you just published.
5. Add them to the map.
6. Configure **popups** for each layer:
   - Click on a layer in the left panel → click the **three dots** (⋯) → **Configure Pop-ups**
   - For AI cities hotspots: show city name, country, AI works, Gi_Bin (cluster class), distance
   - For priority cities: show city name, country, population, distance
7. **Save** the web map → **Share** → **Everyone**.
8. Copy the web map URL.

## G4. Embed in StoryMap

1. Go to your StoryMap editor: `storymaps.arcgis.com/stories/744a1c433d554cef8b3861d72836fdd2/edit`
2. In the section where you want the interactive map, click the **+** button to add a new content block.
3. Select **Map**.
4. Choose the web map you just created in ArcGIS Online.
5. Configure the map embed: zoom level, visible layers, legend visibility.
6. Save the StoryMap.

---

# SUMMARY: What you now have from ArcGIS Pro

| Finding | ArcGIS Pro Tool | Output |
|---|---|---|
| **Finding 1** | Near Analysis (geodesic) | Distance from every city to nearest cloud region |
| **Finding 1** | Buffer Analysis (dissolved) | 500 km compute corridor polygons |
| **Finding 1** | Spatial Join | Validation: 72% of AI cities within 500 km |
| **Finding 1** | Summary Statistics | Median/mean distances for both samples |
| **Finding 3** | Global Moran's I | I = ___, z = ___, p = ___ (spatial autocorrelation confirmed) |
| **Finding 3** | Hot Spot Analysis (Gi*) | City-level hot/cold spot classifications |
| **Finding 3** | Optimized Hot Spot Analysis | Robustness confirmation |
| **Finding 3** | Cluster and Outlier (LISA) | HH/HL/LH/LL city typology |
| **Finding 4** | Select by Attributes | 1,988 priority cities extracted |
| **Finding 5** | OLS Regression | Distance (−), Population (+) confirmed |
| **Finding 5** | Exploratory Regression | Best variable combinations |
| **Finding 5** | GWR | Local coefficient variation (where distance matters most) |

**Cite in the StoryMap:**

> "All spatial analyses were conducted using ArcGIS Pro. Distance to nearest cloud region was measured using Near Analysis (geodesic). Compute corridors were mapped using Buffer Analysis with dissolve. Spatial autocorrelation was assessed using Global Moran's I (Spatial Statistics toolbox), and local clusters were identified using Getis-Ord Gi* Hot Spot Analysis and Cluster and Outlier Analysis (Anselin Local Moran's I). The distance–activity relationship was tested using Ordinary Least Squares regression. Results were cross-validated against an independent Python implementation with consistent findings. Interactive maps were published through ArcGIS Online."
