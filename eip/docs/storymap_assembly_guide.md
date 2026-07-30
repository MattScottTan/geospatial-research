# StoryMap Assembly Guide

This guide explains how to assemble the ArcGIS StoryMaps deliverable so it matches the revised report narrative and the section order in `docs/storymap_blueprint.md`.

## Source docs

Use these repo files together:

- `docs/arcgis_upload_guide.md`
- `docs/arcgis_webmap_guide.md`
- `docs/storymap_blueprint.md`

## Before you start

Make sure these browser-side items already exist in ArcGIS Online:

- hosted layers:
  - `ai_access_cities`
  - `cities_with_hotspots`
  - `priority_cities`
  - `cloud_regions`
- web maps:
  - `Global Compute Accessibility`
  - `AI Research and Hot Spots`
  - `AI Deserts and Priority Cities`

Have these local files ready in case you want to upload them as StoryMap images or fallbacks:

- `outputs/figures/fig1_access_map.png`
- `outputs/figures/fig2_ai_map.png`
- `outputs/figures/fig5_coef_compare.png`
- `outputs/figures/fig6_sea_zoom.png`
- `outputs/figures/fig7_distance_hist.png`
- `outputs/figures/fig13_subsaharan_africa_deep_dive.png`
- `outputs/figures/fig14_latin_america_deep_dive.png`

## Create the story shell

1. Open ArcGIS StoryMaps.
2. Click `New story`.
3. Start with a blank story.
4. Set the title to `AI Compute Accessibility Atlas`.
5. Set the subtitle to `Where cloud compute is close, where it is far, and why that matters for cities`.
6. If you want a cover image, upload `outputs/figures/fig1_access_map.png`.
7. Open story settings and turn on story navigation.

## Build the story section by section

Follow the section order in `docs/storymap_blueprint.md` exactly.

### 1. Hook

1. Insert a `Sidecar`.
2. Choose a docked layout.
3. Add the web map `Global Compute Accessibility` as the first media item.
4. Use the hook copy from the blueprint: AI is not placeless, and the cloud depends on uneven physical infrastructure.

### 2. Why this matters

1. Add a standard narrative section after the hook.
2. Reuse the `Global Compute Accessibility` web map or insert `outputs/figures/fig2_ai_map.png` as support.
3. Keep this section focused on stakes:
   - compute is part of the enabling environment for AI
   - cities do not face equal proximity to that infrastructure
   - the atlas is diagnostic, not causal

### 3. The question and the short answer

1. Add a short narrative section.
2. Follow it with a `Quote` block or other visual emphasis block.
3. State the central question in one sentence.
4. State the short answer in one sentence.
5. Add only one caution sentence about causality so the section stays punchy.

### 4. How the atlas works

1. Add a `Sidecar` with 4 slides.
2. Use this media order:
   - `Global Compute Accessibility`
   - `AI Research and Hot Spots`
   - `outputs/figures/fig7_distance_hist.png`
   - `outputs/figures/fig5_coef_compare.png`
3. Keep the text short and plain-language.
4. Define these terms on first use:
   - `OpenAlex`
   - `Moran's I`
   - `Gi*`
   - `Gaussian Process`
   - `CAR/GMRF`
5. Do not include equations.

### 5. What the atlas found

1. Add the main results `Sidecar`.
2. Build the sequence in this order:
   - `Global Compute Accessibility`
   - `outputs/figures/fig7_distance_hist.png`
   - `AI Research and Hot Spots`
   - `AI Deserts and Priority Cities`
   - `outputs/figures/fig6_sea_zoom.png`
   - `outputs/figures/fig13_subsaharan_africa_deep_dive.png`
   - `outputs/figures/fig14_latin_america_deep_dive.png`
   - `outputs/figures/fig5_coef_compare.png`
3. Keep each slide focused on one takeaway only:
   - compute access is uneven
   - AI-linked cities cluster closer to compute
   - the pattern is spatially clustered but not all-explaining
   - priority cities show stacked disadvantage
   - regional stories differ
   - the models keep the same negative sign
4. Add a `Swipe` block if you want the comparison recommended in the blueprint:
   - left: `Global Compute Accessibility`
   - right: `AI Deserts and Priority Cities`

### 6. What this means for EIP

1. Add a short narrative section.
2. Follow with a bullet list or quote block.
3. Use the report-aligned framing:
   - compute accessibility looks like part of the story, not background noise
   - the atlas helps separate scarcity stories from concentration stories
   - some large cities appear to face stacked disadvantage in the delivered data

### 7. Limits to keep in view

1. Add a short narrative section or an `Accordion` block.
2. Keep the limits brief and highly legible:
   - distance is a proxy, not full compute quality
   - the OpenAlex layer is an observed delivered filter, not exhaustive ground truth
   - the model sample is smaller than the full city frame
   - the project does not estimate the causal effect of cloud-region openings

### 8. About and sources

1. Add a closing narrative section.
2. Include:
   - short methods recap
   - source list
   - repo / reproducibility note
   - team attribution
3. Add one short line that ArcGIS Online publication remains a browser workflow outside the local pipeline.

## Save and review

1. Let the story auto-save after each major section.
2. Use preview mode before publishing.
3. Confirm that every map and image loads.
4. Confirm the section order matches the blueprint:
   - hook
   - why this matters
   - the question and the short answer
   - how the atlas works
   - what the atlas found
   - what this means for EIP
   - limits to keep in view
   - about and sources

## Publish the story

1. Click `Publish` in the story builder header.
2. In the story card panel:
   - confirm the title
   - confirm the subtitle / summary
   - update the thumbnail if needed
3. In the sharing panel, choose the audience:
   - `Everyone (Public)` for the final public StoryMap
4. If you want search engines to index it, enable the web search option.
5. Publish the story.

ArcGIS StoryMaps will check whether the web maps and layers used in the story are shared broadly enough for the audience you selected.

## Public-sharing checklist

For a fully public StoryMap, all of these must be shared to `Everyone (Public)`:

- the StoryMap item itself
- `Global Compute Accessibility`
- `AI Research and Hot Spots`
- `AI Deserts and Priority Cities`
- the hosted layers behind those maps:
  - `ai_access_cities`
  - `cities_with_hotspots`
  - `priority_cities`
  - `cloud_regions`

If ArcGIS warns that a map or layer is not shared broadly enough, stop and fix the sharing on that item before publishing again.

## Final QA before handing off the public URL

- Open the published story in a signed-out browser window or private window.
- Confirm every map, image, and popup loads without an ArcGIS sign-in prompt.
- Confirm the social card title and summary look correct.
- Copy the final public URL into the project handoff notes once it is live.

## Browser-only status

These actions remain outside the local pipeline and must be completed manually in ArcGIS Online:

- hosted-layer upload
- web map creation
- StoryMap publication
- final public sharing / URL validation

## Checked against

- ArcGIS StoryMaps: Publish a story or briefing
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/publish-a-story.htm>
- ArcGIS StoryMaps: Add sidecars
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-sidecars.htm>
- ArcGIS StoryMaps: Add swipe blocks
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-swipes.htm>
- ArcGIS StoryMaps: Add story navigation
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-story-navigation.htm>
