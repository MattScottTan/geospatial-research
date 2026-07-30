# Interactive Hero Map — Hosting & Embed Instructions

This document walks through hosting the interactive HTML on a public URL and embedding it into your StoryMap. Two routes are described. Pick whichever matches the workflow you used for your EIP submission.

## What's in this folder

```
interactive_hero/
├── README.md                                       ← you're here
└── salt_fat_acid_distance_interactive.html         ← the file to host
```

The HTML is a single self-contained Leaflet map. It loads Leaflet from a public CDN (unpkg.com) but bundles all the cuisine data inline — no separate data files needed. Total size: 37 KB.

**Bridge scores in this file are the v2 canonical values (Filipino 0.79, not the old 0.87) so they match the static figures in your StoryMap.**

---

## Route A — GitHub Pages (recommended, ~10 minutes)

GitHub Pages is the most reliable host for a custom HTML file. It gives you a clean public URL that ArcGIS Embed blocks render without sign-in friction.

### Step A1 — Create a public repo (or use an existing one)

1. Go to **github.com** and sign in.
2. Click the **+** in the top right → **New repository**.
3. **Repository name:** something like `salt-fat-acid-distance` (any name works).
4. Set it to **Public**.
5. Tick **Add a README file** (gives you a default branch to enable Pages on).
6. Click **Create repository**.

If you already have a public repo you'd rather use, skip this step.

### Step A2 — Upload the HTML file

1. On the repo page, click **Add file** → **Upload files**.
2. Drag `salt_fat_acid_distance_interactive.html` into the upload zone.
3. Scroll down to the commit message field. Default text is fine.
4. Click **Commit changes**.

### Step A3 — Enable GitHub Pages

1. In the repo, click **Settings** (top right tabs).
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment** → **Source**, select **Deploy from a branch**.
4. Under **Branch**, select **main** and **/ (root)**, then click **Save**.
5. Wait 30–60 seconds. The page will show a green box with a URL like:

   ```
   https://YOUR-USERNAME.github.io/salt-fat-acid-distance/
   ```

6. The HTML file is then accessible at:

   ```
   https://YOUR-USERNAME.github.io/salt-fat-acid-distance/salt_fat_acid_distance_interactive.html
   ```

### Step A4 — Test the URL

1. Open the URL above in an **incognito/private browser window**.
2. The interactive map should load with no sign-in prompt.
3. Click any cuisine anchor (try Filipino) and confirm:
   - The popup shows **bridge score 0.79 (rank 1)** — not 0.87.
   - The top 5 residual partners are Thai, Brazilian, Vietnamese, Jamaican, Southern US.
4. Click Russian and confirm:
   - LISA classification reads **LL ★★★** (the stars indicate p < 0.05).
   - Bridge score reads **"not in top 10"**.

If both checks pass, the file is ready to embed. **Save the URL — you'll need it in Step E1.**

---

## Route B — ArcGIS Online (mirrors your EIP workflow)

Use this route if you have a working pattern from the EIP submission you'd rather replicate.

### Step B1 — Sign in to ArcGIS Online

1. Go to **arcgis.com** and sign in with your Harvard credentials (the same account you'll use for the StoryMap).

### Step B2 — Add the HTML as an item

1. Click **Content** in the top nav.
2. Click **New item** → **Your device**.
3. Drag in `salt_fat_acid_distance_interactive.html`.
4. When asked for **Item type**, choose **HTML page**. (If "HTML page" isn't offered, choose **File** as the fallback.)
5. **Title:** `Salt, Fat, Acid, Distance — Interactive Residual Network`.
6. **Tags:** `cuisine`, `residual`, `LISA`, `bridge index` (any tags work).
7. **Summary:** `Interactive companion to the Fisher Prize StoryMap. Click any cuisine anchor to see its residual partners, LISA classification, and bridge score.`
8. Click **Save**.

### Step B3 — Set sharing to public

1. On the new item's page, click **Share**.
2. Set sharing to **Everyone (public)**.
3. Save.

### Step B4 — Get the direct content URL

The URL you want is the **direct file URL**, not the item details page. Look for a "View" or "Open" or "URL" field on the item page — that's the URL that loads the HTML directly. It typically takes the form:

```
https://www.arcgis.com/sharing/rest/content/items/<ITEM_ID>/data
```

If only the item-details URL (`/home/item.html?id=...`) is available and not the direct content URL, **switch to Route A (GitHub Pages)**. ArcGIS StoryMaps Embed blocks need a URL that loads the HTML directly without going through an item-details intermediate page.

### Step B5 — Test the URL

Same incognito test as Step A4 above. Confirm Filipino reads 0.79, Russian reads LL with stars and "not in top 10."

---

## Step E — Embed in your StoryMap

Once you have a working public URL from Route A or Route B, embed it in your StoryMap.

### Step E1 — Open your draft StoryMap and find Section 2

You should already have Section 2 ("The question") populated with:
- Heading: "The question"
- Body text
- Image: `v4_01_hero_world_corridors.png` with caption + alt text

The interactive embed goes **immediately after** the static hero image and its caption, **before** the section separator.

### Step E2 — Add the Embed block

1. Click between the static-image caption and the section separator. A **+** button appears.
2. Click **+** → scroll the block menu to find **Embed** (sometimes labeled "Embed external content" or shown with a globe/code icon).
3. Paste the public URL from Step A4 or B5.
4. The editor will fetch and preview the embed.
5. Choose the **Card** or **Auto** display option (whichever the editor offers — both work). **Avoid "Link" mode**, which only shows a link rather than rendering the page.
6. If the editor offers a **height** slider, set it to roughly **640 pixels**. The Leaflet map renders at 580 px internal height; 640 px gives breathing room for the title bar and stats panel above it.

### Step E3 — Add a header above the embed

Above the embed block, click **+** → **Heading (H3)** and paste:

```
Trace the residual network yourself
```

### Step E4 — Add a caption below the embed

Below the embed block, click **+** → **Text block** and paste:

```
This interactive companion shows the same residual network as the static hero map above. Click any cuisine anchor to see its top residual partners, LISA classification, and bridge score, with the option to filter by LISA quadrant or scale anchors by mean residual.
```

This adds about 45 visible words to your section. Your overall total goes from 992 to roughly 1,037 words, which is 37 over the 1,000-word cap.

### Step E5 — Trim to restore the word cap

The cleanest place to trim 40+ words is the Section 2 body itself — the embed and its caption are now doing some of the work the prose used to do alone. Replace the long Section 2 body with this shorter version (about 95 words instead of ~140):

```
Cuisines are anchored in geography, shaped by local crops, climates, and terrain, but they are also carried across distance by migration, trade, and colonial exchange, which means a single cuisine encodes both where it sits and where it has been connected to. Spatial analysis is the natural tool for pulling those two forces apart. After geographic distance is accounted for, which cuisines are still more similar than proximity predicts? This project compares 20 cuisine-labeled recipe profiles, computes great-circle distances between geographic anchors, and maps the residuals from a log-distance baseline.
```

That trim drops the *"defined as observed similarity minus distance-predicted similarity"* parenthetical and the *"shaped by archipelagos, peninsulas, Atlantic shores, and long-range exchange"* closing clause — both ideas are still carried by the figures and the interactive embed. The static hero image plus the interactive companion plus this shorter prose is a cleaner three-part composition than long prose plus static image.

Net visible word count after the trim: ~995, back under cap.

### Step E6 — Save and re-test in incognito

1. Save the StoryMap.
2. Re-publish to your draft URL.
3. Open the draft URL in incognito and scroll to Section 2.
4. Confirm:
   - The static hero image renders.
   - The "Trace the residual network yourself" heading appears below it.
   - The interactive map renders below the heading.
   - The map is interactive (clicking anchors opens popups with cuisine data).
   - The closing caption appears below the embed.

If the embed shows a blank box or an error, the most common causes are: (1) the URL requires sign-in, (2) the URL points to an item-details page rather than the direct content URL, or (3) the host blocks iframe embedding. In any of those cases, switch to Route A (GitHub Pages) — it's reliable for Embed blocks.

---

## Three things to spot-check before final publish

When the embed is live in your draft StoryMap, click around to verify the v2 canonical data is showing correctly:

1. **Filipino's popup shows bridge score 0.79 (rank 1)** — not the old 0.87. If you see 0.87, you've embedded the wrong file. Use `salt_fat_acid_distance_interactive.html` from this folder, not the older `bridges_interactive.html`.
2. **Russian's popup shows LISA = LL with three stars and "bridge: not in top 10"** — Russian dropped from the top-10 in v2. If you see "rank 2" or "0.84," you've embedded the wrong file.
3. **The popup title bar reads "Salt, Fat, Acid, Distance — Interactive Residual Network"** — not "Bridges Across Cuisines." If you see the old title, you've embedded the wrong file.

If any of these three fails, replace the hosted file with the one from this folder and re-publish.

---

## After the embed: submission

Once the StoryMap with the embed renders correctly in incognito and sharing is set to "Everyone (public)," send the StoryMap URL to:

- **Email:** `jblossom@cga.harvard.edu`
- **Subject:** `Fisher Prize submission — Salt, Fat, Acid, Distance — Matthew Tan`

Include the StoryMap URL in the email body. Save a screenshot of the sent email as your submission proof.
