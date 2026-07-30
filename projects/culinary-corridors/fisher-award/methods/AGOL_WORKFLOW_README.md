# Interactive Map for Section 2 — ArcGIS Online Workflow

This is the complete workflow: upload one CSV to ArcGIS Online, build a web map, share it publicly, then add it to your StoryMap as a Map block. End-to-end, ~15 minutes.

## What's in this folder

```
agol_map/
├── README.md                        ← you're here
└── cuisine_anchors.csv              ← the only file you upload
```

The CSV has 20 rows (one per cuisine) with 14 columns: cuisine name, lat/lon, LISA classification + p-value, mean residual, bridge score and rank, and a pre-formatted "top 5 partners" string for the popup.

All values are v2 canonical, matching the static figures in your StoryMap. Filipino bridge score = 0.79 (rank 1). Russian LISA = LL at p = 0.0088 (significant outlier, not in top-10 bridges).

---

## Phase 1 — Upload the CSV (~3 minutes)

### Step 1.1 — Sign in to ArcGIS Online

Go to **arcgis.com** and click **Sign In** (top right). Use your **Harvard credentials** — the same account you'll publish the StoryMap from. The web map and StoryMap must live under the same account.

### Step 1.2 — Add the CSV as a hosted feature layer

1. Click **Content** in the top nav.
2. Click **New item** (top right of the Content page).
3. Click **Your device** in the popup.
4. Drag `cuisine_anchors.csv` into the upload zone (or click and browse).
5. The next screen asks **How do you want to add this CSV file?** — choose **Add and create a hosted feature layer**.
6. **Locate features by** → choose **Coordinates (latitude and longitude)**.
7. AGOL should auto-detect the `lat` column as Latitude and `lon` as Longitude. Verify both fields are correctly mapped. If they aren't, set them manually from the dropdowns.
8. Scroll down to the **fields** preview. Confirm field types: `lat`, `lon`, `mean_resid`, `local_I`, `p_sim`, `bridge_score`, `bridge_rank` should all be **Double** (numeric). The rest can stay as **String**.
9. Click **Next**.
10. Fill in:
    - **Title:** `Cuisine Anchors — Salt, Fat, Acid, Distance`
    - **Tags:** `cuisine`, `residual`, `LISA`, `bridge index`, `Fisher Prize`
    - **Summary:** `Twenty cuisine anchors with LISA classifications and v2 canonical bridge scores. Companion to the Fisher Prize StoryMap.`
11. Click **Save**.

The new feature layer's item details page opens. You should see "Cuisine Anchors — Salt, Fat, Acid, Distance" with 20 features.

---

## Phase 2 — Build the web map (~7 minutes)

### Step 2.1 — Open the layer in Map Viewer

On the feature layer's item details page, click **Open in Map Viewer** (top right of the page header). A new browser tab opens with Map Viewer, your 20 cuisine anchors visible as default-styled blue circles on a world basemap.

### Step 2.2 — Style the anchors by LISA classification

This colors the points so HH, LL, and NS cuisines are visually distinct.

1. In the **Layers** panel on the left, click the layer name to select it.
2. In the right toolbar, click the **Styles** icon (looks like a paintbrush).
3. Under **1. Choose attributes**, click **+ Field**.
4. From the field list, select **`lisa_classification`** and click **Add**.
5. Under **2. Pick a style**, choose **Types (unique symbols)** → click **Style options**.
6. You'll see five categories: HH, HL, LH, LL, NS. Click the colored circle next to each to set its color:
   - **HH** → orange or red (suggested: `#c45a2e`) — high-high clusters (Mexican, Jamaican)
   - **LL** → dark blue (suggested: `#1f5fa3`) — low-low cluster (Russian)
   - **HL** → light orange (suggested: `#e8a384`)
   - **LH** → light blue (suggested: `#7fa3c4`)
   - **NS** → grey (suggested: `#999999`) — not significant
7. Click **Done** to close style options.

### Step 2.3 — Size the anchors by mean residual

This makes the high-residual anchors visually larger.

1. Still in the Styles panel, click **+ Field** under **1. Choose attributes**.
2. Select **`mean_resid`** and click **Add**.
3. A new style row appears below the LISA-classification style. Choose **Counts and Amounts (size)** → click **Style options**.
4. Set the symbol size range from **8 px** (smallest) to **28 px** (largest).
5. Click **Done** twice to exit the styles panel.

The map should now show colored circles of varying sizes. Filipino, Brazilian, and Southern US should appear larger; Russian should appear smaller and dark blue.

### Step 2.4 — Configure the popup

This is what a judge sees when they click an anchor.

1. With the layer still selected, click the **Pop-ups** icon in the right toolbar (looks like a speech bubble).
2. Click **Title**. Clear the default and replace with:
   ```
   {cuisine_name}
   ```
3. Click **Fields list** (or **Edit fields list** depending on Map Viewer version).
4. You'll see all 14 fields listed. Click the gear icon next to each field to either hide it or rename its display alias.
5. **Hide these fields** (uncheck or click "hide"): `cuisine`, `cuisine_name`, `lat`, `lon`, `lisa_quadrant_raw`, `is_lisa_significant`. They're either redundant with the title or only useful for filtering, not popup display.
6. **Keep and alias these fields:**
   - `bridge_score` → display alias **"Bridge index score"**
   - `bridge_rank` → **"Bridge rank (1–10)"**
   - `in_bridge_top_10` → **"In top-10 bridges?"**
   - `lisa_classification` → **"LISA classification"**
   - `local_I` → **"Local Moran's I"**
   - `p_sim` → **"Permutation p-value"**
   - `mean_resid` → **"Mean residual"**
   - `top_5_partners` → **"Top 5 residual partners"**
7. Reorder them top-to-bottom so the most important info is highest: bridge_score, bridge_rank, lisa_classification, p_sim, top_5_partners, then the rest. Drag to reorder if Map Viewer supports it.
8. Click outside the panel — Map Viewer auto-saves popup configuration.

### Step 2.5 — Test the popups

Click any cuisine anchor on the map and confirm the popup renders.

- **Click Filipino** → should show *Bridge index score: 0.79 · Bridge rank: 1 · In top-10: yes · LISA: NS · p: 0.1493 · Top 5 partners: Thai (resid +0.36); Brazilian (resid +0.32); Vietnamese (resid +0.25); Jamaican (resid +0.13); Southern US (resid +0.06)*.
- **Click Russian** → should show *Bridge rank: 13 · LISA: LL · p: 0.0088*. The LL classification + p < 0.01 is the project's most distinctive single LISA finding.

If either is wrong, you've uploaded the wrong file. The CSV in this folder is the v2-canonical version.

### Step 2.6 — Set a good initial map view

What the StoryMap reader sees on first load is whatever zoom/pan the web map is saved with.

1. Pan and zoom so all 20 cuisine anchors are visible with a bit of margin.
2. A roughly **world view centered on (20°N, 60°E) at zoom level 2** works well — Asia, Europe, the Americas, and Australia all visible.
3. (Optional) On the basemap selector, switch to **Light Gray Canvas** or **Human Geography Map** for a less visually noisy backdrop than the default. Click the **Basemap** icon in the right toolbar to switch.

### Step 2.7 — Save the web map

1. In Map Viewer's **left** toolbar (not the right), click **Save and open** → **Save as**.
2. Fill in:
   - **Title:** `Salt, Fat, Acid, Distance — Interactive Anchors`
   - **Tags:** same as before
   - **Summary:** `Interactive map of 20 cuisine anchors with LISA classifications and bridge scores. Companion to the Fisher Prize StoryMap.`
3. Click **Save**.

The web map is now saved as a separate item in your AGOL **Content** (in addition to the underlying feature layer).

---

## Phase 3 — Set sharing to public (~1 minute)

You need to share **two** items: the feature layer AND the web map. Both must be public for the StoryMap embed to render for outside viewers.

### Step 3.1 — Share the feature layer

1. Go to **Content** in the top nav.
2. Find **Cuisine Anchors — Salt, Fat, Acid, Distance** in the list.
3. Click it to open item details.
4. Click **Share** (top right of the page header).
5. Set sharing to **Everyone (public)**.
6. Click **Save**. If a warning appears about sharing the underlying CSV file, accept it.

### Step 3.2 — Share the web map

1. Go back to **Content**.
2. Find **Salt, Fat, Acid, Distance — Interactive Anchors** in the list.
3. Click it to open item details.
4. Click **Share** → **Everyone (public)** → **Save**.

---

## Phase 4 — Add the web map to your StoryMap (~3 minutes)

### Step 4.1 — Open your StoryMap draft

Go to **storymaps.arcgis.com**, find your draft `Salt, Fat, Acid, Distance` story, and click **Edit**.

### Step 4.2 — Find Section 2 and the spot for the map

Scroll to **Section 2 — The question**. The structure should currently be:

1. Heading: "The question"
2. Body text
3. Image: `v4_01_hero_world_corridors.png`
4. Caption
5. Separator

The interactive map block goes **between the static image (with its caption) and the section separator**.

### Step 4.3 — Add the Map block

1. Click in the gap between the static image's caption and the separator. A **+** button appears.
2. Click **+** to open the block menu.
3. Click **Map**. (Not **Embed**. The Map block is the AGOL-native choice.)
4. A panel opens listing your AGOL maps.
5. Choose **Salt, Fat, Acid, Distance — Interactive Anchors**.
6. Click **Place map**.

The map renders inline in your StoryMap.

### Step 4.4 — Configure the Map block

After placing, you may see options for:

- **Display size:** choose **Full** for edge-to-edge, **Standard** for column-width. **Full** is the right choice for a hero-position map.
- **Caption:** add a short caption below the map.

For the caption, paste:

```
Click any cuisine anchor to see its residual partners, LISA classification, and bridge score. Anchors are colored by LISA classification (orange for high-high Atlantic-rim clusters, blue for the low-low Russian outlier, grey for not significant). Marker size scales with mean residual.
```

(About 45 words. This adds to your visible word count — see "Word count adjustment" below.)

### Step 4.5 — Add a heading above the map

1. Click between the static image's caption and the new Map block. **+** appears.
2. Click **+** → **Heading (H3)**.
3. Paste:
   ```
   Trace the residual network yourself
   ```

---

## Word count adjustment

Adding the heading + caption costs about **52 visible words** (heading 5 + caption 47). Your current total is 992. With the additions you'd be at ~1,044, which is 44 over the 1,000-word cap.

The cleanest fix: **shorten the Section 2 body text**. The interactive map and its caption now do some of the work the prose used to do alone. Replace the long Section 2 body with this shorter version (about 95 words instead of 140):

```
Cuisines are anchored in geography, shaped by local crops, climates, and terrain, but they are also carried across distance by migration, trade, and colonial exchange, which means a single cuisine encodes both where it sits and where it has been connected to. Spatial analysis is the natural tool for pulling those two forces apart. After geographic distance is accounted for, which cuisines are still more similar than proximity predicts? This project compares 20 cuisine-labeled recipe profiles, computes great-circle distances between geographic anchors, and maps the residuals from a log-distance baseline.
```

That trim plus the additions lands you at roughly **990 visible words** — back under the cap with a 10-word margin.

---

## Phase 5 — Test and submit

### Step 5.1 — Save the StoryMap

In the StoryMaps editor, click **Save** (top right). Don't publish yet.

### Step 5.2 — Publish to a draft URL

Click **Publish** in the editor. The first publish creates the URL but you can keep sharing private.

### Step 5.3 — Test in incognito

1. Copy the published URL.
2. Open it in an **incognito/private browser window**.
3. If a sign-in prompt appears, sharing is still private. Go back to the editor's share menu and switch sharing to **Everyone (public)**, then re-test.
4. Scroll to Section 2.
5. Confirm: static hero figure renders → "Trace the residual network yourself" heading → interactive map renders → caption appears below → section separator → Section 3 begins.
6. Click any cuisine anchor in the live map. Confirm Filipino shows 0.79 / rank 1, Russian shows LL / p = 0.0088.

If the map shows an error or "you don't have access to this content," one of the two items isn't shared publicly. Re-check Phase 3.

### Step 5.4 — Submit

Once the StoryMap with the embedded map renders correctly in incognito and sharing is set to "Everyone (public)":

- **Email:** `jblossom@cga.harvard.edu`
- **Subject:** `Fisher Prize submission — Salt, Fat, Acid, Distance — Matthew Tan`
- **Body:** include the StoryMap URL.

Save a screenshot of the sent email and the StoryMap URL as your submission proof.

---

## Three sanity checks before final submit

1. **Filipino popup reads 0.79, rank 1.** If it reads 0.87 or rank 2, the wrong CSV was uploaded — re-upload from this folder.
2. **Russian popup reads LL, p = 0.0088, bridge rank 13.** Russian should NOT be in the top-10 bridges. If it shows rank 2, you uploaded an old version.
3. **Both items public.** The feature layer AND the web map need to be shared with Everyone. The most common embed-fails-in-incognito failure is the feature layer being private even when the web map is public.

If those three pass, you're done.
