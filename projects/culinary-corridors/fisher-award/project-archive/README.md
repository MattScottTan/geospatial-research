# Culinary Corridors — Fisher Prize MASTER Archive

Everything from the Fisher Prize submission preparation, in one place. Organized so the submission-ready material is up front and the source archive sits behind it for reference.

## Folder layout

```
culinary_corridors_MASTER/
├── 01_SUBMIT_THIS/          ← the actual thing you'll publish
├── 02_FULL_PROJECT_ARCHIVE/ ← all source materials from your uploaded archive
├── 03_VERSION_HISTORY/      ← script iteration trail (v4 → v7 → BUILD_INSTRUCTIONS)
└── 04_EIP_REFERENCE/        ← your EIP-winning submission PDF, for voice comparison
```

---

## 01_SUBMIT_THIS/ — the ready-to-publish bundle

This is the folder to open first. It contains everything needed to build the StoryMap.

```
01_SUBMIT_THIS/
├── culinary_corridors_fisher_submission.zip   ← self-contained submission package (also unzipped below)
├── BUILD_INSTRUCTIONS.md                       ← canonical paste-by-paste ArcGIS build guide
├── WORK_completed.md                           ← record of bibliography assembly + verification
└── figures/                                    ← 6 PNGs in upload order
    ├── v4_01_hero_world_corridors.png
    ├── v4_02_method_residual_baseline.png
    ├── v4_03_primary_case_regional_map.png
    ├── v4_04_topographic_corridor_map.png
    ├── v4_05_bridge_index_map_and_chart.png
    └── v4_06_secondary_residuals_by_grouping.png
```

**How to use:** Open `BUILD_INSTRUCTIONS.md` in a markdown previewer, open ArcGIS StoryMaps in another window, and walk top to bottom pasting content and uploading the six figures in order. About 60–90 minutes.

The zip file in this folder is the same content packaged for standalone use — either the loose files or the zip works.

**Status:** ready to publish. Bibliography complete (16 verified references, all URLs live as of 2026-05-02), corpus named ("Yummly 'What's Cooking' Kaggle dataset, accessed via Zelený's anadat-r prepared version"), cuisine count stated (20 labels, 39,774 recipes, 6,714 raw ingredients). No `[TODO]` markers remain.

**One decision flagged.** Reference [3] Ahn et al. 2011 *Flavor Network* is not cited in your original LaTeX report. See `WORK_completed.md` for the reasoning behind adding it and instructions for removing it if you didn't consult it during the project.

---

## 02_FULL_PROJECT_ARCHIVE/ — source materials

Your uploaded comprehensive archive, extracted for direct browsing without unzipping.

```
02_FULL_PROJECT_ARCHIVE/
├── culinary_corridors_storymap_balanced_v3_package.zip  ← original v3 storymap package (backup)
└── extracted/
    ├── complete_archive_metadata/  ← manifest & provenance notes
    ├── data/
    │   ├── raw/                    ← recipe_source_manifest.md + raw data notes
    │   ├── processed/              ← cuisine_ingredient_long.csv (31 MB) + matrices
    │   └── crosswalks/             ← ingredient normalization tables
    ├── docs/                       ← project-internal documentation
    ├── figures/
    │   ├── final/                  ← final figures used in the committee report
    │   └── final_revised/          ← post-Run-5 revisions (topographic corridor map)
    ├── outputs/                    ← run6v3 audit + reproducibility notes
    ├── report/
    │   ├── final_complete/         ← the canonical final report (LaTeX + PDF + source bundle)
    │   ├── final_committee/        ← committee-focused version
    │   └── revised/                ← intermediate revision
    ├── scripts/                    ← analysis scripts referenced in the reports
    ├── storymap_step_by_step_package/  ← original block-by-block script (pre-EIP-voice rewrite)
    └── submission/
        └── storymap_conversion_v3/ ← v3 paste blocks that BUILD_INSTRUCTIONS.md was built from
```

**How to use:** Reach for this when you need to look up a specific value, verify a figure's origin, or point a reviewer to the underlying report. The most important single file is `extracted/report/final_complete/culinary_corridors_complete_final_report.pdf` — that's the 9.8 MB comprehensive technical report the StoryMap summarizes.

---

## 03_VERSION_HISTORY/ — the iteration trail

Six files showing how the script evolved:

```
03_VERSION_HISTORY/
├── culinary_corridors_storymap_v4_BUILD_INSTRUCTIONS.md   ← regional-balance refinement of v3
├── culinary_corridors_storymap_v5_BUILD_INSTRUCTIONS.md   ← figure rebuild w/ cartopy + Natural Earth
├── culinary_corridors_storymap_v6_BUILD_INSTRUCTIONS.md   ← full rewrite in EIP voice; overshot to "9-of-10 non-Asian"
├── culinary_corridors_storymap_v7_BUILD_INSTRUCTIONS.md   ← rebalanced framing (Pacific-archipelagic/Eurasian/Atlantic-rim)
├── WORK_initial_plan.md                                    ← planner-generated task plan
└── WORK_completed.md                                       ← executed plan with results & learnings
```

**How to use:** These are the intermediate versions. The current canonical is `01_SUBMIT_THIS/BUILD_INSTRUCTIONS.md` (which is v7 with the bibliography filled in). If you ever want to see what was tried and why a change was made, the version history + WORK files together tell the full story.

---

## 04_EIP_REFERENCE/ — voice benchmark

Your EIP-winning *Cloudy with a Chance of Compute* submission PDF. `BUILD_INSTRUCTIONS.md` is written in this same voice; keep this open when doing the voice consistency check in the QA checklist.

---

## Recommended pre-publish workflow

1. Skim `01_SUBMIT_THIS/BUILD_INSTRUCTIONS.md` end to end (about 15 minutes) to internalize the flow.
2. Decide whether to keep or drop reference [3] Ahn et al. (see `WORK_completed.md` for reasoning).
3. Open ArcGIS StoryMaps, start a new blank story, and walk the build guide top to bottom.
4. Run the 10-point QA checklist at the bottom of the build guide.
5. Set sharing to public, publish, verify in an incognito browser.
6. Submit before 11:59 p.m. Sunday May 3, 2026.

---

If anything looks off, `WORK_completed.md` and the version history together document every substantive decision.
