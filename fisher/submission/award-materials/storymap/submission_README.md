# Salt, Fat, Acid, Distance — Fisher Prize Submission Bundle

Everything you need to build the StoryMap, publish it, and submit. Three files plus eight figures.

## What's in this bundle

```
salt_fat_acid_distance_submission/
├── README.md          ← you're here
├── PASTE_SCRIPT.md    ← the full paste-ready ArcGIS StoryMap script
└── figures/           ← 8 PNG files referenced by the paste script
    ├── v4_01_hero_world_corridors.png         (Section 2)
    ├── v4_02_method_residual_baseline.png     (Section 3)
    ├── v4_07_lisa_and_mantel.png              (Section 4)
    ├── v10_validation_stats.png               (Section 4)
    ├── v4_05_bridge_index_map_and_chart.png   (Section 5)
    ├── v10_robustness_panel.png               (Section 5)
    ├── v4_03_primary_case_regional_map.png    (Section 6)
    └── v4_08_case_filipino.png                (Section 7)
```

## The submission, in five steps

### Step 1 — Open both files side by side

Open `PASTE_SCRIPT.md` in any markdown viewer (or just a text editor — the formatting is meant to be human-readable raw too). In another window, open ArcGIS StoryMaps and start a new story.

### Step 2 — Paste the cover

The first block of `PASTE_SCRIPT.md` is the cover. Three fields:

- **Title:** *Salt, Fat, Acid, Distance*
- **Subtitle:** *Where culinary resemblance exceeds what geographic distance predicts*
- **Byline:** *Matthew Scott Tan — Fisher Prize submission*

### Step 3 — Work through Sections 2 through 8

Each section has the same pattern in `PASTE_SCRIPT.md`:

1. An **Action** line tells you what to click in the StoryMap editor (e.g., "Click `+` → Heading (H2)").
2. A fenced code block contains the exact text to paste.

**Don't paste the action lines themselves** — only what's inside the triple-backticks. For images, upload from the `figures/` folder; the script names each PNG explicitly.

There are two new-for-v10 elements that didn't appear in any earlier draft:

- **Section 3 — data table.** A 4-column × 7-row table (1 header + 6 rows) listing the project's datasets. The script provides the cell values; build the table using the StoryMap editor's Table block tool. If the editor offers a "header row" toggle, turn it on.
- **Section 8 — references list.** Five numbered citations after the quote block. Pastes as plain text in a single block.

### Step 4 — Save, publish to draft, test

Once everything is pasted:

1. **Save** (don't publish yet).
2. **Scroll top to bottom** as a layout pass. Watch for: cover renders correctly, each section has heading → body → image → caption in order, both new figures appear (Section 4 has *two* images, Section 5 has *two* images), Section 8 has heading → body → quote → references.
3. **Publish to draft URL** (sharing initially set to private or unlisted).
4. **Test in incognito.** Open the URL in a private/incognito browser window. If a sign-in prompt appears, sharing is still private — go back and switch to "Everyone (public)." Re-test until it loads cleanly.
5. **Save the public URL.** You'll need it for the email.

### Step 5 — Submit

Send the StoryMap URL to:

- **Email:** `jblossom@cga.harvard.edu`
- **Subject:** `Fisher Prize submission — Salt, Fat, Acid, Distance — Matthew Tan`

Attach (or save) a screenshot of the sent email and the published StoryMap URL as your submission proof.

## What the eight figures show, in case you want to spot-check

| Figure | Section | What's in it |
|---|---|---|
| `v4_01_hero_world_corridors` | 2 | World map, cuisine anchors, residual corridors. Blue = E/SE Asia case, orange = long-distance positive residuals. |
| `v4_02_method_residual_baseline` | 3 | Scatter plot: cuisine-pair similarity vs. log distance with regression line and residual examples. |
| `v4_07_lisa_and_mantel` | 4 | Composite figure — Mantel statistics + Local Moran's I categories overlaid on the cuisine network. |
| `v10_validation_stats` *(new)* | 4 | Three-panel stats dashboard. Mantel test, LISA results for Russian / Mexican / Jamaican, colonial partial Mantel. |
| `v4_05_bridge_index_map_and_chart` | 5 | Bridge index map + bar chart. Filipino 0.79 first; Southern US, French, Cajun-Creole, Brazilian, Thai follow. |
| `v10_robustness_panel` *(new)* | 5 | Bootstrap CIs for top-6 bridges (left) + Russian-anchor sensitivity (right, Siberian vs. Moscow). |
| `v4_03_primary_case_regional_map` | 6 | E/SE Asia regional zoom showing the strongest mainland + archipelagic residual links. |
| `v4_08_case_filipino` | 7 | Filipino case-study scorecard map showing residual links to Thai, Brazilian, Vietnamese, Jamaican, Southern US. |

If a judge asks "which test gave you that number?" — the answer is in `v10_validation_stats`. If they ask "is the bridge ranking reliable?" — it's in `v10_robustness_panel`. Those two figures are the project's strongest rigor signals.

## Three small things to watch for during paste

1. **Em-dashes and Unicode minus.** The script uses real em-dashes (—) and Unicode minus sign (−) in places like *slope −0.124*. ArcGIS handles both correctly. If your text editor strips them to plain `--` or `-`, that's still fine — the StoryMap renders either acceptably.

2. **Section 3 data table.** ArcGIS StoryMaps' table block may not render the markdown table directly if you paste it as text. Use the editor's Table block tool to build the grid manually with the cell values from `PASTE_SCRIPT.md`. Six body rows + 1 header.

3. **Two images in Sections 4 and 5.** This is intentional and is the v10 winner-style upgrade over v9. The first image is the original v4 figure; the second image is the new v10 panel. Both belong, in that order.

## The submission package, in one paragraph

Eight figures, one paste script, eight visible sections, 992 visible words against the 1,000-word cap. The project asks where cuisine resemblance exceeds what distance predicts. It answers: at six bridge cuisines anchored in geographically distinct regions, with a residual network whose spatial structure passes Mantel, LISA, and colonial partial-Mantel tests, and whose bridge ranking is bootstrap-stable in cluster. The Filipino case study connects the Southeast Asian corridor to Atlantic and Gulf cuisines through a partial-Mantel-supported colonial-administration signal. That is the whole submission.

Good luck.
