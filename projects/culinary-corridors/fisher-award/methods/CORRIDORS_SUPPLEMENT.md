# Adding the Corridors Layer to Your AGOL Map

This is a supplement to the main `README.md` in this folder. The main README walks through uploading the **cuisine anchors** as points. This supplement walks through adding the **residual corridors** as lines, so your live map matches the static hero figure.

## The two files (use one or the other, not both)

| File | Geometry | When to use |
|---|---|---|
| `residual_corridors_curved.geojson` | Great-circle arcs (~60 vertices each) | **Recommended** — looks like the static figure, transoceanic lines curve naturally |
| `residual_corridors.geojson` | Straight Mercator segments (2 vertices each) | Fallback only if the curved file fails to upload |

Both contain the same 56 features (one per positive-residual cuisine pair) with the same properties: `pair`, `cuisine_a`, `cuisine_b`, `residual`, `distance_km`, `is_long_distance`. Only the geometry vertex density differs.

The curved file uses spherical interpolation along great-circle paths, with antimeridian-crossing lines split into MultiLineString geometries so AGOL renders them on both sides of the date line correctly (instead of dragging a horizontal line across the entire map). Six of the 56 corridors are antimeridian-split: Filipino–Jamaican, Filipino–Southern US, Indian–Mexican, Brazilian–Japanese, Mexican–Russian, and Russian–Southern US.

Top corridors (same in both files):

- Chinese–Korean (residual +0.44, regional)
- Irish–Southern US (residual +0.40, long-distance)
- Thai–Vietnamese (residual +0.40, regional)
- Filipino–Thai (residual +0.36, regional)
- Brazilian–Filipino (residual +0.32, long-distance — the Manila Galleon corridor)

## Step 1 — Upload the GeoJSON to AGOL

The workflow mirrors the CSV upload in the main README, but choose GeoJSON instead.

1. Go to **arcgis.com**, sign in, click **Content** → **New item** → **Your device**.
2. Drag **`residual_corridors_curved.geojson`** into the upload zone (the curved version is the recommended one).
3. AGOL detects the file as GeoJSON automatically. You may see a prompt asking whether to create a hosted feature layer — choose **Add and create a hosted feature layer**.
4. Fill in:
   - **Title:** `Residual Corridors — Salt, Fat, Acid, Distance`
   - **Tags:** `cuisine`, `residual`, `corridors`, `Fisher Prize`
   - **Summary:** `Fifty-six positive-residual cuisine corridor lines drawn as great-circle arcs, classified as regional or long-distance. Companion line layer to the cuisine anchors point layer.`
5. Click **Save**.

The new feature layer's item details page opens. You should see "Residual Corridors — Salt, Fat, Acid, Distance" with 56 features.

If the curved file fails to upload (unusual but possible if AGOL chokes on the file size or the MultiLineString features), fall back to `residual_corridors.geojson` instead. The straight-line version will render correctly but lose the curved geometry.

## Step 2 — Set sharing to public

1. Click **Share** (top right of the item details page).
2. Set sharing to **Everyone (public)**.
3. Save.

## Step 3 — Add the corridors layer to your existing web map

1. Go to **Content** → find **Salt, Fat, Acid, Distance — Interactive Anchors** (the web map you built in the main workflow).
2. Click it → click **Open in Map Viewer**.
3. The web map loads with your anchors layer visible.
4. In the left **Layers** panel, click **Add** (or the **+** icon).
5. Choose **Browse layers** → **My content**.
6. Find **Residual Corridors — Salt, Fat, Acid, Distance** and click **Add**.

The 56 corridor lines now render on the same map as your anchors. The default styling will probably be uniform thin gray lines — Step 4 makes them look like the static figure.

## Step 4 — Style the corridors

This styles them to match the static hero figure: orange for long-distance, blue for regional, line thickness scaled by residual magnitude.

### Step 4a — Color by long-distance flag

1. In the Layers panel, click the **Residual Corridors** layer to select it.
2. In the right toolbar, click **Styles**.
3. Under **1. Choose attributes**, click **+ Field** and select `is_long_distance`. Click **Add**.
4. Under **2. Pick a style**, choose **Types (unique symbols)** → click **Style options**.
5. You'll see two categories: **long-distance** and **regional**.
   - Click the **long-distance** symbol → set color to orange (suggested: `#c45a2e`).
   - Click the **regional** symbol → set color to blue (suggested: `#1f5fa3`).
6. Click **Done**.

### Step 4b — Vary line thickness by residual

1. Still in the Styles panel, click **+ Field** to add a second attribute.
2. Select `residual` and click **Add**.
3. The new style row appears. Choose **Counts and Amounts (size)** → **Style options**.
4. Set the line width range from **1 px** (smallest residual) to **4 px** (largest residual).
5. Click **Done** twice.

### Step 4c — Adjust line opacity

Lines often look heavy on a busy basemap. Reduce opacity for clarity.

1. With the layer selected, in the Layers panel click the layer name's "..." menu → **Layer effects** (or directly in the Styles panel scroll to the **Effects** section).
2. Set **Transparency** to about 30–40%.

The corridors should now look like the static hero figure: orange long-distance lines crossing oceans, blue regional lines clustering in East/Southeast Asia, line thickness reflecting the residual magnitude, anchors visible underneath.

## Step 5 — Configure the corridor popup

1. With the corridors layer selected, click the **Pop-ups** icon in the right toolbar.
2. Set **Title** to:
   ```
   {pair}
   ```
   (Renders as e.g. *Chinese–Korean* or *Brazilian–Filipino*.)
3. Edit fields list. Hide `cuisine_a`, `cuisine_b`, `is_long_distance` (the title and color already convey them). Keep:
   - `residual` → alias **"Positive residual"**
   - `distance_km` → alias **"Geographic distance (km)"**

Test by clicking a line. Click the longest line (Brazilian–Filipino) — popup should show *Brazilian–Filipino*, residual +0.3246, distance 19318 km.

## Step 6 — Set layer order

In the Layers panel, drag layers so the **anchors layer is on top** and the **corridors layer is below**. This way clicking a point opens the cuisine popup (the primary interactive payload), and clicking empty space between points has the corridor lines available for inspection.

## Step 7 — Save the web map again

1. Click **Save and open** → **Save** (not "Save as," because you're updating the existing web map).
2. Confirm.

The web map now contains both layers. Your StoryMap's existing Map block automatically picks up the change — no need to re-add the map. Save and re-publish the StoryMap to push the updated map view to the public draft URL.

---

## Two failure modes and their fixes

**Failure 1: GeoJSON upload errors with "schema not recognized."** Some AGOL accounts default to assuming GeoJSON is a Web Map JSON file. If the upload wizard asks for a different item type, manually choose **GeoJSON** from the dropdown. If "GeoJSON" isn't an option, your account's role may not include hosted feature layer publishing — fall back to Option 2 below.

**Failure 2: The curved file errors but the straight one works.** If `residual_corridors_curved.geojson` fails to upload (file size or MultiLineString rejection), upload `residual_corridors.geojson` instead. The lines will render as straight Mercator segments, which is the standard AGOL rendering. The orange/blue color coding still distinguishes long-distance from regional, so the substantive information is preserved even with straight lines.

---

## Option 2 — Use the static figure as the corridor layer (fallback, ~2 minutes)

If both GeoJSON files fail or AGOL won't render lines at all:

1. Skip the corridors layer entirely.
2. Keep the cuisine anchors layer as the only interactive piece.
3. The static `v4_01_hero_world_corridors.png` figure already shows the lines in the StoryMap above the interactive map.

This is a perfectly reasonable composition. The static figure shows the network shape; the interactive map below it lets the reader explore individual cuisines. Two-pass design: argue with the static, explore with the live.

---

## My recommendation

**Try `residual_corridors_curved.geojson` first.** Upload, style with two attributes (color by `is_long_distance`, size by `residual`), set transparency to ~30%, configure popups, save. About five minutes if AGOL accepts the file cleanly.

If the curved file fails, fall back to `residual_corridors.geojson` (straight lines) — same workflow, same styling, just less visual fidelity to the static hero figure.

If both fail, skip the corridors layer entirely. The static hero figure already shows the network; the interactive layer can be anchors only without losing the project's argument.

The corridors are the *argument* (best made statically, even on a static figure). The anchors are the *exploration* (best made interactively). The two formats playing different roles is a feature, not a bug.
