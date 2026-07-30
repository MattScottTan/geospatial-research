# ArcGIS Map Build — Exact Step-by-Step Instructions

> Uses your real field names. Total time: 3.5–5 hours.
>
> **Your ArcGIS Online URL:** harvard-cga.maps.arcgis.com
>
> **Layers already in your ArcGIS Online org:**
> - `ai_access_cities` — 8,000 cities (fields: city_ascii, population, dist_km_nearest_region, nearest_provider)
> - `cloud_regions` — 60+ regions (fields: provider, region, location_name)
> - `cities_with_hotspots` — 319 AI cities (fields: city_ascii, hotspot_class, gi_star_z, openalex_ai_works_recent, dist_km_nearest_region)
> - `priority_cities` — 1,988 cities (fields: city_ascii, priority_rank, population, dist_km_nearest_region, nearest_provider)
>
> **One new layer to upload:** `bundle_city_scores.csv` from Package Part 6

---

# STEP 0: Upload the Bundle Index Layer (15 minutes)

You need this before building Map C or the Consolidated Atlas.

1. On your computer, locate: `AI_Compute_Accessibility_Atlas_EIP_Submission_Package Part 6/final_submission/originality/final/bundle_city_scores.csv`

2. Open your browser. Go to **harvard-cga.maps.arcgis.com**. Log in.

3. Click **Content** in the top navigation bar.

4. Click the **+ New item** button (top left).

5. Click **Your device**. Navigate to `bundle_city_scores.csv`. Select it. Click **Open**.

6. ArcGIS shows a preview. It should say "Add bundle_city_scores.csv and create a hosted feature layer."
   - Make sure **"Add bundle_city_scores.csv and create a hosted feature layer"** is selected (not "Add bundle_city_scores.csv as a table").
   - Click **Next**.

7. ArcGIS asks which fields contain location:
   - **Latitude field:** Select **`lat`**
   - **Longitude field:** Select **`lng`**
   - Click **Next**.

8. Set the item details:
   - **Title:** `bundle_city_scores`
   - **Tags:** type `AI`, press Enter, type `bundle`, press Enter, type `compute`, press Enter
   - **Summary:** `Compute Opportunity Bundle Index for 8,000 cities`
   - Click **Create**.

9. Wait for upload to finish (may take 30–60 seconds for 8,000 rows).

10. Once created, click **Share** (on the item details page, right side) → check **Everyone (public)** → click **Save**.

**Verify:** Click **Open in Map Viewer**. You should see 8,000 points scattered across the globe. If you see nothing, the lat/lng fields weren't recognized — go back and check step 7.

---

# MAP A: Gi* Hot Spots / Cold Spots (25–35 minutes)

## A1. Create the map

1. Click **Map** in the top navigation bar. A new blank map opens.

2. In the left sidebar, click the **Layers** button (stack of layers icon, second from top).

3. Click **+ Add** → **Browse layers** → make sure **My Content** is selected in the dropdown at the top.

4. Find **`cities_with_hotspots`**. Click the **+** button next to it to add it.

5. Find **`cloud_regions`**. Click the **+** button next to it to add it.

6. Click the **←** back arrow to return to the Layers panel. You should see both layers listed.

## A2. Style the Gi* layer

1. In the Layers panel, click **`cities_with_hotspots`** to select it (it should become highlighted).

2. On the right side, the **Properties** panel opens. Click the **Styles** button (paintbrush icon on the right toolbar). If you don't see it, click the three dots **"..."** next to the layer name → **Style layer**.

3. Under **"Pick a style"**, look for the **"Choose an attribute"** dropdown. Click it. Scroll down and select **`hotspot_class`**.

4. ArcGIS should suggest **"Types (Unique symbols)"**. If it shows multiple options, click **"Types (Unique symbols)"**. Then click **"Style options"** underneath it.

5. You should see 5 categories listed. For each one, click the colored circle/square next to its name to edit the symbol:

   **`hot_spot_99`** (1 city — Macau):
   - Click the symbol → **Shape:** circle → **Fill color:** click the color box → type **#d7191c** (dark red) → press Enter
   - **Size:** drag to **14 px** (or type 14)
   - **Outline color:** white → **Outline width:** 1 px
   - Click **Done** (the checkmark at the bottom of the symbol editor)

   **`hot_spot_95`** (6 cities):
   - Fill color: **#fdae61** (salmon/orange)
   - Size: **11 px**
   - Outline: white, 1 px
   - Click **Done**

   **`not_significant`** (279 cities):
   - Fill color: **#d9d9d9** (light grey)
   - Size: **6 px**
   - Outline: **#999999** (medium grey), 0.5 px
   - Click **Done**

   **`cold_spot_95`** (23 cities):
   - Fill color: **#74add1** (medium blue)
   - Size: **11 px**
   - Outline: white, 1 px
   - Click **Done**

   **`cold_spot_99`** (10 cities):
   - Fill color: **#2c7bb6** (dark blue)
   - Size: **14 px**
   - Outline: white, 1 px
   - Click **Done**

6. Click **Done** at the bottom of the Style options panel.
7. Click **Done** again to exit the Styles panel.

## A3. Style cloud regions

1. Click **`cloud_regions`** in the Layers panel.
2. Click **Styles** (paintbrush) on the right.
3. Choose attribute: **`provider`**.
4. Select **"Types (Unique symbols)"** → **Style options**.
5. For each provider, click the symbol:

   **`aws`:**
   - Shape: **diamond** (look in shape options — it may be listed as "diamond" or a rotated square)
   - Fill color: **#FF9900** (orange)
   - Size: **16 px**
   - Outline: white, 1.5 px
   - Click **Done**

   **`azure`:**
   - Shape: diamond
   - Fill color: **#00A4EF** (blue)
   - Size: **16 px**
   - Outline: white, 1.5 px
   - Click **Done**

   **`gcp`:**
   - Shape: diamond
   - Fill color: **#EA4335** (red)
   - Size: **16 px**
   - Outline: white, 1.5 px
   - Click **Done**

6. Click **Done** twice.

7. In the Layers panel, **drag `cloud_regions` above `cities_with_hotspots`** (click and hold the layer name, drag it up). Cloud regions should now draw on top.

## A4. Configure pop-ups

1. Click **`cities_with_hotspots`** in the Layers panel.

2. Click the **Pop-ups** button in the right toolbar (speech bubble icon). If you can't find it, click **"..."** next to the layer name → **Configure pop-ups**.

3. Pop-up configuration opens. Click the **Title** area and change it to: **`{city_ascii}`**
   - To insert a field: click in the title text box, then click **"+ Add field"** or type the field name in curly braces.

4. Below the title, you should see a **Fields list** block (or click **+ Add content** → **Fields list**).

5. Click the **Fields list** block to configure it. Click the pencil/edit icon.

6. You'll see all fields listed. Click the **"Select fields"** link or toggle to choose which fields appear. Select ONLY these:
   - `country` — rename display label to **Country**
   - `openalex_ai_works_recent` — rename to **AI Works**
   - `hotspot_class` — rename to **Cluster Type**
   - `gi_star_z` — rename to **Gi* Z-Score**
   - `dist_km_nearest_region` — rename to **Distance to Cloud (km)**
   - `population` — rename to **Population**

   Deselect everything else (city_id, iso2, iso3, admin_name, etc.).

7. Click **Done**.

8. Now configure cloud_regions pop-ups:
   - Click **`cloud_regions`** in the Layers panel.
   - Click **Pop-ups**.
   - Set title to **`{location_name}`**
   - In the fields list, show only: `provider` (rename to **Provider**), `region` (rename to **Region Code**)
   - Click **Done**.

## A5. Set basemap, save, share

1. Click the **Basemap** button in the left toolbar (the icon that looks like stacked layers/squares, usually 3rd from top).
2. Select **Light Gray Canvas**.

3. Zoom the map out to show the entire world.

4. Click **Save** in the left toolbar (floppy disk icon, near the top).
5. If it says **"Save"** vs **"Save as"**: click **Save as** (or if this is a new map, it will prompt you).
6. Fill in:
   - **Title:** `AI Research Hot Spots and Cold Spots`
   - **Tags:** `AI`, `hot spots`, `Getis-Ord`, `spatial statistics`
   - Click **Save**.

7. Click **Share** (the person+ icon near Save) → check **Everyone (public)** → click **Save**.

## A6. Test

1. Open a **new incognito/private browser window** (Ctrl+Shift+N in Chrome).
2. Paste the map URL from the address bar.
3. Check:
   - [ ] Map loads without asking you to log in
   - [ ] You see red dots (hot spots), blue dots (cold spots), grey dots (not significant)
   - [ ] Diamond shapes for cloud regions are visible on top
   - [ ] Clicking a city shows the pop-up with City name, Country, AI Works, Cluster Type, Z-Score, Distance
   - [ ] Clicking a cloud region shows Provider and Region Code

---

# MAP B: Priority Cities (25–35 minutes)

## B1. Create the map

1. Click **Map** in top nav → this opens a new map (or click the hamburger menu → **New map** if you're already in Map Viewer).
2. **Add** → **Browse layers** → **My Content**.
3. Add **`priority_cities`**.
4. Add **`cloud_regions`**.

## B2. Style priority cities

1. Click **`priority_cities`** in the Layers panel.
2. Click **Styles** (paintbrush).
3. Choose attribute: **`dist_km_nearest_region`**.
4. Select **"Counts and Amounts (Color)"** → **Style options**.
5. Click the color ramp bar to open the ramp picker.
   - Click **"All"** to see all ramp options.
   - Pick a **yellow → dark red** sequential ramp (or **yellow → orange → red**).
   - The logic: farther distance = darker red = more underserved.
6. Adjust the **histogram handles**:
   - Drag the lower handle to **1,252** (your threshold).
   - Drag the upper handle to **5,000**.
7. Click **Done**.

8. Add size by population:
   - Click **"+ Add attribute"** → select **`population`**.
   - ArcGIS adds size encoding. Adjust the size range so bigger cities get bigger dots (roughly **4–16 px**).
9. Click **Done** twice.

## B3. Filter to top 100 (recommended)

1. Click **`priority_cities`** in the Layers panel.
2. Click the **Filter** button (funnel icon in the right toolbar).
3. Click **"+ Add expression"**.
4. Set: **`priority_rank`** → **is less than or equal to** → type **`100`**.
5. Click **Save** (or **Apply**).

Now only the 100 highest-priority cities display.

## B4. Style cloud regions

Same as Map A step A3. Diamond shapes, colored by provider (AWS orange, Azure blue, GCP red).

## B5. Configure pop-ups

1. Click **`priority_cities`** → **Pop-ups**.
2. Title: **`{city_ascii}`**
3. Fields to show (rename labels):
   - `country` → **Country**
   - `population` → **Population**
   - `dist_km_nearest_region` → **Distance to Cloud (km)**
   - `nearest_provider` → **Nearest Provider**
   - `observed_ai_works_recent` → **AI Works (should be 0)**
   - `priority_rank` → **Priority Rank**
4. Click **Done**.

## B6. Save and share

1. Basemap: **Light Gray Canvas**.
2. Zoom to world view.
3. **Save as:** `Priority Cities — AI Compute Access Gaps`
4. Tags: `AI`, `priority`, `infrastructure gaps`
5. **Share** → **Everyone (public)**.

## B7. Test in incognito

Same checks as Map A step A6. Verify clicking a city shows rank, distance, and that AI Works shows 0.

---

# MAP C: Bundle Index (30–40 minutes)

**Prerequisite:** You completed Step 0 (uploaded `bundle_city_scores`).

## C1. Create the map

1. New map in Map Viewer.
2. **Add** → **Browse layers** → **My Content**.
3. Add **`bundle_city_scores`**.
4. Add **`cloud_regions`**.

## C2. Filter to top 1,000 cities

The layer has 8,000 cities. For the bundle map, show only the top 1,000 by population.

1. Click **`bundle_city_scores`** in Layers panel.
2. Click **Filter** (funnel icon).
3. Click **"+ Add expression"**.
4. Set: **`population`** → **is greater than or equal to** → type a value that gives you roughly 1,000 cities. Try **`1000000`** (1 million). 
   - If too many cities appear, raise it to `1500000`.
   - If too few, lower to `500000`.
   - The exact threshold doesn't matter — you want roughly 1,000 dots that aren't too cluttered.
5. Click **Save**.

## C3. Style by bundle score

1. Click **`bundle_city_scores`** in the Layers panel.
2. Click **Styles** (paintbrush).
3. Choose attribute: **`bundle_score`**.
4. Select **"Counts and Amounts (Color)"** → **Style options**.
5. Click the color ramp bar → **All** → find a **purple → yellow** ramp (looks like "Viridis" or "Plasma").
   - Low score (0) = dark purple
   - High score (100) = bright yellow
   - **Flip the ramp** if needed (click the flip arrows) so purple = low, yellow = high.
6. Set histogram handles: lower = **0**, upper = **100**.
7. Click **Done**.

8. Add size by population:
   - Click **"+ Add attribute"** → select **`population`**.
   - Adjust size range: **4–20 px**.
9. Click **Done** twice.

## C4. Style cloud regions

Same diamond symbols as before.

## C5. Configure pop-ups — THE KEY PART

This is what makes the bundle map valuable. Readers click a city and see the five-component breakdown.

1. Click **`bundle_city_scores`** → **Pop-ups**.

2. Title: **`{city_ascii}`**

3. Click on the default content block (or **+ Add content** → **Text**). Type:
   ```
   Bundle Score: {bundle_score}/100
   Country: {country}
   ```

4. Click **+ Add content** → **Fields list**.

5. Select and rename these fields:
   - `score_proximity` → **Proximity (40%)**
   - `score_provider_diversity` → **Provider Diversity (15%)**
   - `score_redundancy` → **Redundancy (15%)**
   - `score_population` → **Urban Scale (15%)**
   - `score_institutions` → **Institutional Depth (15%)**
   - `dist_km_nearest_region` → **Distance to Cloud (km)**
   - `population` → **Population**
   - `ai_works_recent` → **AI Works**
   - `providers_within_1000` → **Providers within 1,000 km**
   - `regions_within_1000` → **Cloud Regions within 1,000 km**

   Deselect all other fields.

6. **Important:** The score fields (score_proximity etc.) are on a 0–1 scale in the CSV, not 0–100. The pop-up will show values like "0.999" instead of "99.9". To fix:
   - In the Fields list configuration, look for **Format** options next to each score field.
   - If you can set format to **Percentage** or multiply by 100, do so.
   - If not, it's still readable — just note that 1.0 = 100% and 0.0 = 0%.

7. Click **Done**.

## C6. Save and share

1. Basemap: **Light Gray Canvas**.
2. Zoom to world.
3. **Save as:** `Compute Opportunity Bundle Index`
4. **Share** → **Everyone (public)**.

## C7. Test in incognito

Click Paris — should show bundle_score ~93.6. Click Lagos — should show ~27.8. Check that all five component scores appear.

---

# MAP D: Case Study Regional Views (10–15 min each × 4 = 40–60 min)

These are zoomed web maps. You make four of them using the same layers, just zoomed differently.

## General method (repeat for each city)

1. New map in Map Viewer.
2. **Add** **`cloud_regions`** and **`cities_with_hotspots`**.
3. Style both layers the same way as Map A (Gi* colors for cities, diamond by provider for cloud regions).

4. **Turn on labels for cloud regions:**
   - Click **`cloud_regions`** in the Layers panel.
   - Click the **Labels** button in the right toolbar (the **"Aa"** icon). If you can't find it, click **"..."** → **Create labels**.
   - ArcGIS opens the label configuration. Set:
     - **Label field:** **`location_name`**
     - **Font size:** **9 pt**
     - **Font color:** **dark grey (#333333)**
     - **Halo:** check "enable halo" → color **white**, size **1 px**
   - Click **Done** or **Apply**.

5. **Zoom** to the correct region (see specific coordinates below).
6. **Save as** the map name given below.
7. **Share** → **Everyone (public)**.

## D1. Singapore

- **Zoom to:** Southeast Asia. Frame should show Singapore, Malaysia, Indonesia, Philippines, Vietnam.
- Approximate extent: lat **-5° to 20°**, lon **95° to 125°**.
- **Save as:** `Case Study — Singapore Regional Context`

## D2. Dublin

- **Zoom to:** Western Europe. Frame: Ireland, UK, France, Netherlands, Germany.
- Approximate extent: lat **45° to 60°**, lon **-12° to 15°**.
- The key visual: the dense cluster of 13 cloud region diamonds within 1,000 km.
- **Save as:** `Case Study — Dublin Regional Context`

## D3. Ho Chi Minh City

- **Zoom to:** Vietnam + surrounding Southeast Asia. Frame: Vietnam, Thailand, Cambodia, Singapore, southern China.
- Approximate extent: lat **-2° to 25°**, lon **95° to 120°**.
- The key visual: the nearest cloud regions are in Singapore, 1,097 km south.
- **Save as:** `Case Study — Ho Chi Minh City Regional Context`

## D4. Lagos

- **Zoom to:** Africa-wide view. Frame: West Africa through South Africa.
- Approximate extent: lat **-35° to 20°**, lon **-20° to 50°**.
- The key visual: the ONLY cloud region diamonds are clustered at the southern tip (Cape Town/Johannesburg). The entire West African coast is empty.
- **Save as:** `Case Study — Lagos Regional Context`

---

# THE CONSOLIDATED ATLAS (45–75 minutes)

This is the single most important map. It IS the atlas.

## Step 1. Create map and add all layers

1. New map in Map Viewer.
2. **Add** → **Browse layers** → **My Content**. Add these one by one:
   - `cloud_regions`
   - `ai_access_cities`
   - `cities_with_hotspots`
   - `priority_cities`
   - `bundle_city_scores`
3. You should now see 5 layers in the Layers panel.

## Step 2. Create 500 km buffer rings

1. Click the **Analysis** button in the right toolbar (wrench/tools icon — may say "Run analysis" or just show a wrench).
2. A panel opens. Search for **"Create Buffers"** in the search box at the top. Click it.
3. Configure:
   - **Input layer:** `cloud_regions`
   - **Size / Distance:** type **500**
   - **Units:** select **Kilometers**
   - **Overlap policy** or **Dissolve type:** select **Dissolve** or **Overlap** (if you see "Dissolve", choose that — it merges overlapping buffers into clean corridor zones)
   - **Result layer name:** `cloud_buffers_500km`
4. Click **Run Analysis** (or **Estimate credits** → **Run**). Wait 1–2 minutes.
5. The buffer layer appears on the map. Now style it:
   - Click the buffer layer in Layers → **Styles**.
   - It should default to **"Location (Single symbol)"**. Click **Style options**.
   - Click the symbol → set fill color to **#d4e6f1** (light blue) → set **Opacity** to **10%** (drag the opacity slider way down).
   - Set outline: **dashed line** if available (look for a line style option), color **#999999** (grey), width **1 px**.
   - Click **Done** twice.

## Step 3. Style each layer

**`ai_access_cities` (8,000 cities):**
1. Click it → **Styles** → attribute: **`dist_km_nearest_region`**.
2. "Counts and Amounts (Color)" → Style options → pick a **blue → yellow → orange** ramp (or match your hero map).
3. Histogram handles: lower = 0, upper = 3,500.
4. Click Done → **"+ Add attribute"** → **`population`** → size encoding (4–20 px).
5. Done twice.
6. **Hide this layer by default:** Click the **eye icon** (👁) next to `ai_access_cities` in the Layers panel to toggle it OFF. The reader can turn it on.

**`cities_with_hotspots` (Gi* layer):**
- Same styling as Map A (step A2). Color by `hotspot_class`.
- **Leave visible (eye ON)** — this is the default analytical view.

**`priority_cities`:**
- Same styling as Map B (step B2). Color by distance, size by population.
- Filter to top 100 (Map B step B3).
- **Hide by default (eye OFF).**

**`bundle_city_scores`:**
- Same styling as Map C (steps C2–C3). Color by `bundle_score`, size by population. Filter to population ≥ 1,000,000.
- **Hide by default (eye OFF).**

**`cloud_regions`:**
- Same diamond styling as before.
- **Leave visible (eye ON).**

**`cloud_buffers_500km`:**
- Already styled in Step 2.
- **Leave visible (eye ON).**

## Step 4. Set layer order

In the Layers panel, drag to this order (top to bottom):

1. **`cloud_regions`** ← top (always visible, draws over everything)
2. **`cities_with_hotspots`** ← default analytical view (eye ON)
3. **`priority_cities`** ← hidden by default (eye OFF)
4. **`bundle_city_scores`** ← hidden by default (eye OFF)
5. **`ai_access_cities`** ← hidden by default (eye OFF)
6. **`cloud_buffers_500km`** ← bottom, subtle context (eye ON)

## Step 5. Rename layers

For each layer, click **"..."** next to its name → **Rename**:

- `cloud_regions` → **Cloud Regions (AWS / Azure / GCP)**
- `cities_with_hotspots` → **AI Research Clusters (Gi* Hot/Cold Spots)**
- `priority_cities` → **Priority Cities (Top 100 Underserved)**
- `bundle_city_scores` → **Compute Opportunity Bundle Index**
- `ai_access_cities` → **All 8,000 Cities (Distance to Cloud)**
- `cloud_buffers_500km` → **500 km Compute Corridor**

## Step 6. Configure pop-ups for all layers

For each layer, set up pop-ups the same way you did for the individual maps:
- `cities_with_hotspots` → same as Map A step A4
- `priority_cities` → same as Map B step B5
- `bundle_city_scores` → same as Map C step C5
- `ai_access_cities` → Title: `{city_ascii}`, show: country, population, dist_km_nearest_region, nearest_provider
- `cloud_regions` → same as Map A step A4 (cloud section)

## Step 7. Save and share

1. Zoom to show the entire world.
2. **Save as:** `Cloudy with a Chance of Compute — Interactive Atlas`
3. Summary: `Interactive atlas of AI compute accessibility across 8,000 cities. Toggle layers to explore spatial clusters, priority cities, and the Compute Opportunity Bundle Index.`
4. Tags: `AI`, `compute`, `atlas`, `cloud infrastructure`, `spatial analysis`, `Harvard`
5. **Share** → **Everyone (public)**.

## Step 8. Test thoroughly

Incognito browser. Check:
- [ ] Default view: cloud diamonds + Gi* colored cities + light blue buffer corridor
- [ ] Click a Gi* city → pop-up shows city name, AI works, cluster type, z-score, distance
- [ ] Toggle OFF "AI Research Clusters", toggle ON "Priority Cities" → see red priority dots
- [ ] Toggle ON "Bundle Index" → see purple-to-yellow dots, click one → five component scores appear
- [ ] Toggle ON "All 8,000 Cities" → dense global view with distance coloring
- [ ] Cloud regions stay visible on top through all toggles
- [ ] Legend shows your renamed layer names
- [ ] **Test on phone** — open the URL on your mobile browser

---

# EMBED EVERYTHING IN THE STORYMAP (30–45 minutes)

## Open the StoryMap editor

1. Go to: https://storymaps.arcgis.com/stories/744a1c433d554cef8b3861d72836fdd2
2. Click **Edit** (pencil icon, top right).

## Embed 1: Gi* map → Finding 3

1. Scroll to **Finding 3** ("The pattern is spatially structured").
2. Find the static Gi* map image.
3. Click on it. Look for a **replace** or **swap** button, or delete the image block and add a new one:
   - Click the **"+"** button → select **"Map"** (or **"ArcGIS"** → **"Map"**).
   - A search panel opens. Search for **`AI Research Hot Spots and Cold Spots`**.
   - Select it → click **Add** or **Insert**.
4. The interactive map replaces the static image.

## Embed 2: Priority Cities map → Finding 4

1. Scroll to **Finding 4** ("1,988 priority cities").
2. Replace the static priority cities image with the **`Priority Cities — AI Compute Access Gaps`** web map. Same process as Embed 1.

## Embed 3: Bundle Index map → Bundle section

1. Scroll to **"Beyond Distance: The Infrastructure Bundle"**.
2. Replace the static bundle map image with the **`Compute Opportunity Bundle Index`** web map.

## Embed 4: Consolidated Atlas → after Finding 5

1. Scroll to the end of **Finding 5** (after the regression coefficient chart), BEFORE the Bundle section.
2. Click the **"+"** between sections to add a new block.
3. Add a **Text** block. Type:

   > **Explore the Atlas**
   >
   > The interactive map below brings the atlas's analytical layers together. Use the layer toggle (click the layers icon in the map toolbar) to switch between views: spatial clusters, the priority-city screening layer, and the Compute Opportunity Bundle Index. Click any city for details.

4. Below the text, click **"+"** → **Map** → search for **`Cloudy with a Chance of Compute — Interactive Atlas`** → add it.
5. Set its display size to **Large** or **Full** (click the map block, look for size options at the top of the block).

## Embeds 5–8: Case study regional maps

For each case study (Singapore, Dublin, HCMC, Lagos):

1. Scroll to that city's section.
2. Look for the existing image/chart in the section (scorecard bar chart or regional context image).
3. There are two approaches:

   **Option A — Replace the existing image:**
   - Delete the current image → add a **Map** block → search for the case study map (e.g., `Case Study — Singapore Regional Context`) → insert.

   **Option B — Add the map as a second slide (keeps scorecard + adds map):**
   - If the section uses a **sidecar** layout (text on left, media on right), click the media panel on the right.
   - Look for **"+ Add"** or **"+ Add slide"** at the bottom of the media panel.
   - Add a new slide → set its content to the regional web map.
   - Now the reader scrolls through slides: first the scorecard, then the regional map.

## Embed 9: Consolidated Atlas → end of Conclusion

1. Scroll to the end of the **Conclusion**, before the Sources section.
2. Add a **Text** block:

   > **Explore the Full Atlas**
   >
   > Toggle between analytical layers to explore the geography of AI compute access across 8,000 cities.

3. Below it, add another **Map** block → insert the **`Cloudy with a Chance of Compute — Interactive Atlas`** again.

## Save and publish

1. Click **Preview** (eye icon at top) to see how it looks to a reader.
2. Scroll through the entire StoryMap checking every embedded map loads.
3. Click **Publish** (or **Save** if already published).
4. **Final test:** Open the StoryMap URL in an incognito browser on desktop AND on your phone.

---

# TIME SUMMARY

| Task | Time |
|------|------|
| Step 0: Upload bundle CSV | 15 min |
| Map A: Gi* Hot Spots | 25–35 min |
| Map B: Priority Cities | 25–35 min |
| Map C: Bundle Index | 30–40 min |
| Map D: 4× Case Study Regional | 40–60 min |
| Consolidated Atlas | 45–75 min |
| Embed all in StoryMap | 30–45 min |
| **TOTAL** | **3.5–5 hours** |

**Do them in this order:** Step 0 → Map A → Map B → Map D (×4) → Map C → Atlas → Embeds
