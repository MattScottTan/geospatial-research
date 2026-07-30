# Bridges Across Cuisines — Fisher Prize submission package

**Status: ready to publish.** Bibliography complete, corpus named, cuisine count filled in. No `[TODO]` markers anywhere in the build script.

## What's in this zip

```
culinary_corridors_fisher_submission/
├── README.md                 — this file
├── BUILD_INSTRUCTIONS.md     — paste-by-paste ArcGIS build guide (the main deliverable)
├── WORK_completed.md         — record of how the bibliography was assembled and verified
├── figures/                  — six PNG figures, named in upload order
│   ├── v4_01_hero_world_corridors.png
│   ├── v4_02_method_residual_baseline.png
│   ├── v4_03_primary_case_regional_map.png
│   ├── v4_04_topographic_corridor_map.png
│   ├── v4_05_bridge_index_map_and_chart.png
│   └── v4_06_secondary_residuals_by_grouping.png
└── code/                     — Python source for the rebuilt figures (reference / regeneration)
    ├── figdata.py            — coordinates, residual values, bridge scores, spatial groupings
    ├── build_fig01_hero.py   — generates v4_01 (Robinson world map of residual corridors)
    ├── build_fig03_primary.py — generates v4_03 (East/SE Asia regional map)
    ├── build_fig05_bridge.py — generates v4_05 (bridge index world map + bar chart)
    └── build_fig06_secondary.py — generates v4_06 (boundary/permeability bar chart)
```

## Build flow

1. **Open `BUILD_INSTRUCTIONS.md`** in a markdown previewer (VS Code `Cmd/Ctrl-Shift-V`, Typora, Obsidian, or a browser markdown extension). The rendered preview is much easier to follow than raw markdown.

2. **In a second window, open ArcGIS StoryMaps** at storymaps.arcgis.com → sign in → **+ New story → Start from scratch**.

3. **Walk top to bottom through `BUILD_INSTRUCTIONS.md`.** Each section tells you which `+`-button block to add (Heading, Text, Image, Quote, Separator), gives you the exact text to paste, and provides the caption and alt text for each image upload. The figures live in `figures/` — upload them in the order numbered (v4_01 first, v4_06 last).

4. **Run the 10-point QA checklist** at the bottom of the build instructions. The most important: voice consistency, bridge-finding placement, atlas-word absence (zero hits expected), number consistency, image alt text, and the bibliography pre-flight.

5. **Set sharing to public.** Top-right of the editor → Share → Everyone (public). Without this, the Fisher reviewer can't open the link.

6. **Publish** (top-right). Open the public URL in a private/incognito browser window to verify it loads without sign-in.

7. **Submit.** Paste the StoryMap URL into the Fisher form. If the form requires a PDF upload, attach your technical report and put the URL in the description.

Estimated time for a careful first pass: 60–90 minutes.

## What's already filled in (you don't need to do anything for these)

- **Section 11 (Data sources)** names the corpus exactly: *"Yummly 'What's Cooking' Kaggle dataset, accessed via the prepared version in David Zelený's anadat-r repository [1, 2]"* and states the counts: 39,774 recipes, 20 cuisine labels, 6,714 distinct raw ingredient names.
- **Section 12 (Bibliography)** has 16 numbered references in EIP-style format, all with verified URLs as of 2026-05-02.
- **Section 3 (How the analysis works)** has inline `[N]` citations after the recipe corpus, after cosine similarity, and after GeoPy's great-circle method.

## One decision flagged for you

Reference **[3] Ahn, Ahnert, Bagrow, Barabási (2011) *Flavor network and the principles of food pairing*** is **not** cited in your original LaTeX final report. It was added as a single methodological-context citation because your project's analytical move (cuisine-by-ingredient matrices, similarity, regional comparison) sits squarely in the literature this paper founded.

**If you actually consulted it during the project: keep [3] as is.** Nothing more to do.

**If you did not consult it and prefer not to cite it:** delete entry [3] from Section 12, then renumber entries 4–16 down by one, and replace the inline `[3]` in Section 3 (after "cosine similarity on the ingredient frequency vectors") with `[6, 7]` (referring to scikit-learn + pandas as the cosine implementation). Everything else stays.

`WORK_completed.md` documents the reasoning for adding [3] and the verification status of every reference, in case you want to audit before publishing.

## About the figures

Four of the six figures were generated from scratch using cartopy + Natural Earth basemap data — Python source in `code/`. Two figures (`v4_02_method_residual_baseline.png` and `v4_04_topographic_corridor_map.png`) are unchanged originals from your project's run4/run5 outputs and were renamed for upload-order consistency.

If you want to regenerate any of the four rebuilt figures (to tweak colors, add a label, change a residual value):

```bash
# from the code/ directory
pip install matplotlib cartopy numpy
# also need Natural Earth shapefiles — see notes inside build_fig01_hero.py
python build_fig01_hero.py     # → 01_hero_world_corridors.png
python build_fig03_primary.py  # → 03_primary_case_regional_map.png
python build_fig05_bridge.py   # → 05_bridge_index_map_and_chart.png
python build_fig06_secondary.py # → 06_secondary_residuals_by_grouping.png
```

The scripts hard-code a path to a Natural Earth shapefile checkout (`/home/claude/ne_repo`). If regenerating locally, point them at your own Natural Earth data directory.

`figdata.py` is the single source of truth for all numerical values used in the rebuilt figures: cuisine anchor coordinates, focused-case residual values, bridge scores, spatial-grouping mean residuals, and the distance-baseline regression coefficients. Edit values there to propagate them through all four figure scripts at once.

## What's in the build instructions

`BUILD_INSTRUCTIONS.md` is written in the same voice as your EIP-winning *Cloudy with a Chance of Compute* submission, with these structural elements:

- **Cover** (Section 1) — Minimal layout, text only
- **Introduction** (Section 2) — Author bio + opening contrast across three cuisine pairs + research question + hero figure
- **How the analysis works** (Section 3) — Three-stage methodology with inline `[N]` citations
- **Findings 1–4** (Sections 4–7) — Numbered analytical findings with statistics embedded in prose
  - Finding 1: distance baseline (R² = 0.355)
  - Finding 2: spatial-grouping inversion (Iberian/Atlantic > same-subregion)
  - Finding 3: bridge cuisines and three structural geographies (Pacific-archipelagic, Eurasian continental, Atlantic-rim)
  - Finding 4: East/SE Asia focused corridor (regional + relief)
- **Four cuisines** (Section 8) — Filipino, Russian, Thai, Spanish — each illustrating one structural role; balanced 2 Asian + 2 non-Asian
- **Conclusion** (Section 9)
- **Sources** (Section 10) — methodology and tools in prose
- **Data sources** (Section 11) — corpus, anchors, basemaps, with inline citations
- **Bibliography** (Section 12) — 16 numbered references in EIP format

## Pre-publish checklist

- [ ] Set the cover date to your actual submission date (or leave blank if you've added one)
- [ ] Decide whether to keep or drop reference [3] (see "One decision flagged" above)
- [ ] Run the 10-point QA checklist at the bottom of `BUILD_INSTRUCTIONS.md`
- [ ] Publish, set public sharing, verify with incognito browser
- [ ] Submit to the Fisher form before 11:59 p.m. on Sunday May 3, 2026

---

If anything in the build instructions is unclear, the QA checklist and `WORK_completed.md` together cover most of the gotchas.
