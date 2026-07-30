# Hero Map Improvement — ArcGIS Online Click-by-Click Instructions

## Prerequisites
- Logged into Harvard ArcGIS Online (harvard-cga.maps.arcgis.com)
- `ai_access_cities` hosted feature layer already uploaded
- `cloud_regions` hosted feature layer already uploaded
- Map Viewer open with both layers added

---

## 1. Color-encode cities by distance to nearest cloud region

This is the single most important change. Right now cities are all orange. After this, close cities will be dark blue/teal and far cities will be bright orange/red.

1. In the **Layers panel** (left sidebar), click on **`ai_access_cities`** to select it.
2. Click the **Styles** button (the paintbrush icon) in the right panel — or click **"Style layer"** if prompted.
3. Under **"Choose an attribute"**, click the dropdown and select **`dist_km_nearest_region`** (your distance field — the exact name may vary; look for whatever holds the distance-to-nearest-cloud-region value in km).
4. ArcGIS will suggest drawing styles. Select **"Counts and Amounts (Color)"**. Click **"Style options"** underneath it.
5. Under **Color ramp**, click the colored bar to open the ramp picker.
6. Choose a **sequential ramp** that runs from a cool color (close) to a warm color (far). Recommended: 
   - Click **"All"** in the ramp picker to see all options.
   - Look for a ramp that goes from **dark teal/blue → yellow → orange/red**. The "Viridis" or "Plasma" style ramps work well. Alternatively, choose a simple **blue → orange** diverging ramp.
   - If you want to match your PDF figures (which used viridis), pick the closest match.
7. **Flip the ramp if needed** — you want shorter distances = darker/cooler color, longer distances = warmer color. Click the **flip arrow** next to the ramp if it's backwards.
8. Under **Theme**, keep it on **"High to low"** (continuous).
9. Adjust the **histogram handles** if needed:
   - Drag the upper handle to around **3,000–4,000 km** so that the full range of your data is visible.
   - Drag the lower handle to **0 km**.
   - This ensures the color spread is meaningful — not all bunched at one end.
10. Click **"Done"** twice to apply.

### Also keep size by population:
11. While still in the Styles panel for `ai_access_cities`, click **"+ Add attribute"**.
12. Select your **population field** (e.g., `population`, `pop`, or whatever the column is named).
13. This should add a **"Counts and Amounts (Size)"** option. Select it.
14. You now have **color = distance, size = population** — which is what the PDF version had.
15. Click **"Done"** to apply.

---

## 2. Make cloud regions more prominent and color by provider

1. In the **Layers panel**, click on **`cloud_regions`** to select it.
2. Click the **Styles** button (paintbrush icon).
3. Under **"Choose an attribute"**, select your **provider field** (e.g., `provider`, `cloud_provider`, or similar — the field that contains "AWS", "Azure", "GCP").
4. Select **"Types (Unique symbols)"** as the drawing style. Click **"Style options"**.
5. You should see three categories: AWS, Azure (or Microsoft), GCP (or Google). For each one:
   - Click the colored symbol next to the category name.
   - **For AWS:** Choose a circle or diamond shape, set fill color to **blue (#0073BB)** — AWS brand blue. Set size to **16–20 px**.
   - **For Azure:** Set fill color to **green (#00A4EF)** or teal. Same size.
   - **For GCP:** Set fill color to **red (#EA4335)** — Google red. Same size.
6. For all three, set the **outline** to white, 1–2 px, so they stand out against the basemap.
7. If you want to use **×** symbols instead of circles:
   - When editing each symbol, click **"Shape"** and choose the × or cross marker from the basic shapes panel.
   - Set size to **18–22 px** so they're clearly visible at global zoom.
8. Click **"Done"** twice to apply.

### Make cloud regions draw on top:
9. In the **Layers panel**, drag `cloud_regions` **above** `ai_access_cities` in the layer order. This ensures cloud region symbols are always visible on top of the city dots.

---

## 3. Add a visible legend

1. While viewing the map, look for the **Legend** button in the left toolbar (it looks like a small list/key icon, or find it under the ≡ menu).
2. In Map Viewer, the legend auto-generates from your symbology. If you've done steps 1–2 above correctly, the legend should now show:
   - **ai_access_cities:** a color ramp labeled with distance values (0 km → 4,000+ km) and size circles for population
   - **cloud_regions:** three colored symbols labeled AWS, Azure, GCP
3. When you embed this map in the StoryMap, the legend is accessible to viewers via the map's expand controls. To make sure it's visible by default:
   - When inserting the map into StoryMap, in the map configuration panel, check **"Show legend"** if that option is available.
   - Alternatively, consider adding a separate small legend image as a static PNG beneath the map for clarity.

---

## 4. Add 500 km buffer rings around cloud regions (optional but recommended)

This visually shows the "compute corridor" — 72% of AI-linked cities fall within this range.

### Option A — Create buffers in ArcGIS Online (no Pro needed):

1. In Map Viewer, click the **Analysis** button (the tools/wrench icon in the right toolbar).
2. Search for or navigate to **"Create Buffers"** (under "Use proximity" tools).
3. Configure:
   - **Input layer:** `cloud_regions`
   - **Distance:** `500` **Kilometers**
   - **Dissolve type:** **Dissolve** (this merges overlapping buffers into corridor zones, which looks much cleaner than 60+ individual circles)
   - **Result layer name:** `cloud_region_buffers_500km`
4. Click **Run**.
5. Once complete, the buffer layer will appear in your map.
6. Style it:
   - Click on the buffer layer → **Styles**.
   - Set fill to a **very light grey or light blue** with **low opacity (10–15%)**.
   - Set outline to **dashed line, medium grey, 1 px**.
   - This creates a subtle "zone" effect without overpowering the city dots.
7. In the **Layers panel**, drag this buffer layer **below** `ai_access_cities` but **above** the basemap. The layer order from top to bottom should be:
   - `cloud_regions` (on top)
   - `ai_access_cities`
   - `cloud_region_buffers_500km`
   - Basemap

### Option B — If you want to skip the analysis tool:

Just note the 500 km stat in the text instead: "72% of AI-linked cities in the atlas fall within 500 km of a major cloud region." This is less visual but still effective.

---

## 5. Strengthen country boundaries

1. Click on **Basemap** in the left toolbar (the layered-squares icon).
2. Your current basemap is **Light Gray Canvas**. You have two options:

### Option A — Keep Light Gray Canvas but add a reference layer:
- Light Gray Canvas already has a "Reference" sub-layer with labels. This should show country boundaries.
- If boundaries are too faint, you can add a separate **World Countries** layer:
  1. Click **"Add layer"** → search **"World Countries (Generalized)"** in the Living Atlas.
  2. Add it to the map.
  3. Style it: fill **transparent (0% opacity)**, outline **dark grey (#666666), 1 px solid**.
  4. Drag it below `ai_access_cities` but above the basemap.

### Option B — Switch to a slightly richer basemap:
- Try **"Light Gray Canvas [with labels]"** — make sure labels are enabled.
- Or try **"National Geographic"** for more geographic context — though this may clash with your city symbology.
- **Recommendation:** Stick with Light Gray Canvas + added country boundary layer for the cleanest look.

---

## 6. Save and test

1. Click **Save** (or Save As) in the top toolbar.
2. Name the map exactly as your spec requires: **`Global Compute Accessibility`**.
3. Click **Share** → set to **Everyone (public)**.
4. Open an **incognito/private browser window**.
5. Paste the map URL and confirm:
   - [ ] Map loads without login prompt
   - [ ] City colors show distance gradient (not all orange)
   - [ ] Cloud region symbols are visible and color-coded by provider
   - [ ] Legend is accessible
   - [ ] Popups work when clicking a city (should show: city name, country, population, distance, nearest provider)
   - [ ] Buffer zones visible (if added)
6. Test on **mobile** — open the map URL on your phone and check readability.

---

## Summary of final layer order (top to bottom)

1. `cloud_regions` — colored by provider (AWS blue, Azure green, GCP red), large symbols
2. `ai_access_cities` — colored by distance (blue→orange ramp), sized by population
3. `cloud_region_buffers_500km` — light grey/blue, 10–15% opacity, dashed outline (if created)
4. Basemap: Light Gray Canvas
5. (Optional) World Countries boundary layer — transparent fill, grey outline

---

## Quick-reference field names

Check your actual field names in the layer's attribute table. The instructions above assume:

| What I wrote | Your likely field name | Check by |
|---|---|---|
| `dist_km_nearest_region` | Could be `dist_km`, `distance_km`, `nearest_dist` | Open attribute table in Map Viewer: click layer → "..." → "Show table" |
| `population` | Could be `pop`, `population`, `city_pop` | Same |
| `provider` | Could be `cloud_provider`, `provider_name` | Check `cloud_regions` attribute table |

If field names differ, substitute your actual names wherever these appear above.
