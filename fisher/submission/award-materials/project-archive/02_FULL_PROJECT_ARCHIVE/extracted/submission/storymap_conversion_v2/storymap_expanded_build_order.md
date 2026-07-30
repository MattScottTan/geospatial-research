# Expanded ArcGIS StoryMap Build Order

Use this file as the operational build guide. Upload the figures first, then paste the section blocks in order.

## Figure upload order
1. `figures/final_revised/run4_hero_spatial_argument_figure.png` — Hero and global-discovery figure (required). Recommended display: Cover if crop works; otherwise full-width image after opening hook.
2. `figures/final_revised/run4_method_or_model_figure.png` — Method and residual-logic figure (required). Recommended display: Full-width image; enable expand image if possible.
3. `figures/final_revised/run4_primary_case_figure.png` — Primary focused inference map (required). Recommended display: Full-width image or sidecar media panel.
4. `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png` — Relief/coastal context figure (required). Recommended display: Full-width image; place immediately after primary case map.
5. `figures/final_revised/run4_geospatial_insight_figure.png` — Strongest geospatial-only insight (required). Recommended display: Full-width image; emphasize as key Fisher contribution.
6. `figures/final_revised/run4_secondary_or_limitations_figure.png` — Diagnostic and limitations figure (required). Recommended display: Full-width image or appendix-style image.
7. `figures/final_revised/run5_corridor_callout_or_inset.png` — Optional zoom/callout (optional). Recommended display: Sidecar or optional appendix image if layout has room.

## Section build order
1. **Cover / title / subtitle / author note** — paste block `storymap_section_paste_blocks/01_cover.md`. Recommended ArcGIS block: Cover. Keep the title large and use the subtitle exactly as written.
2. **Opening contrast and introduction** — paste block `storymap_section_paste_blocks/02_opening_contrast.md`. Recommended ArcGIS block: Text section with an emphasized quote/callout.
3. **Research question and subquestions** — paste block `storymap_section_paste_blocks/03_research_question.md`. Recommended ArcGIS block: Text block with bold research question.
4. **Why food can be treated as spatial data** — paste block `storymap_section_paste_blocks/04_food_as_spatial_data.md`. Recommended ArcGIS block: Text block. Use this section before methods to justify the project’s spatial premise.
5. **How the culinary atlas works** — paste block `storymap_section_paste_blocks/05_how_atlas_works.md`. Recommended ArcGIS block: Long text section, preferably broken into four short subsections or a sidecar with four panels.
6. **Global discovery screen** — paste block `storymap_section_paste_blocks/06_global_discovery.md`. Recommended ArcGIS block: Full-width image followed by explanation. This should feel like the first major map of the atlas.
7. **Finding 1: distance matters, but incompletely** — paste block `storymap_section_paste_blocks/07_finding1_distance.md`. Recommended ArcGIS block: Image plus explanatory text. This is the main methods/result bridge.
8. **Finding 2: residuals reveal candidate culinary corridors** — paste block `storymap_section_paste_blocks/08_finding2_residuals.md`. Recommended ArcGIS block: Text block after the method figure. Optional: reuse a cropped/global portion of the hero figure if the StoryMap needs visual pacing.
9. **Finding 3: East/Southeast Asia is the strongest focused case** — paste block `storymap_section_paste_blocks/09_finding3_east_se_asia.md`. Recommended ArcGIS block: Sidecar or full-width map with text. This should be one of the central StoryMap sections.
10. **Finding 4: terrain, coastlines, islands, and maritime space make the corridor legible** — paste block `storymap_section_paste_blocks/10_finding4_topography.md`. Recommended ArcGIS block: Full-width image. Place immediately after the East/Southeast Asia focused-case section.
11. **Finding 5: residual bridge scores identify spatial bridge roles** — paste block `storymap_section_paste_blocks/11_finding5_bridge.md`. Recommended ArcGIS block: Full-width image with an emphasized text callout. This is the strongest spatial-necessity section.
12. **Cuisine-pair vignettes** — paste block `storymap_section_paste_blocks/12_case_vignettes.md`. Recommended ArcGIS block: Scrolling text section after bridge-index figure, or sidecar with one panel per vignette. Optional diagnostic vignette may be omitted if the StoryMap feels long.
13. **Secondary / diagnostic case and sensitivity** — paste block `storymap_section_paste_blocks/13_secondary_case.md`. Recommended ArcGIS block: Image plus text. This section can be shortened if the StoryMap becomes too long, but keep the claim discipline.
14. **What this proves, and what it does not prove** — paste block `storymap_section_paste_blocks/14_proof_limits.md`. Recommended ArcGIS block: Text block with strong/cautious/forbidden claim callout.
15. **Sources, methods, and reproducibility** — paste block `storymap_section_paste_blocks/15_sources_methods.md`. Recommended ArcGIS block: Sources/methods text near the end. Include source hyperlinks if possible in ArcGIS.
16. **Conclusion and final contribution** — paste block `storymap_section_paste_blocks/16_conclusion.md`. Recommended ArcGIS block: Closing text. Consider repeating a small version of the bridge-index or hero figure only if the StoryMap feels visually sparse.
17. **PDF backup / technical report note** — paste block `storymap_section_paste_blocks/17_pdf_backup.md`. Recommended ArcGIS block: Final section with button/link to PDF if a public PDF URL is available.

## Optional layout guidance
- Use sidecars for the methods stages and cuisine-pair vignettes if you want a more atlas-like feel.
- Use full-width media for the method figure, primary case map, Run 5 topographic map, and bridge-index figure.
- Keep the optional Run 5 inset only if it improves clarity; omit it if the StoryMap feels crowded.
- Put the PDF backup note at the end as a button/link if a public PDF URL is available.
