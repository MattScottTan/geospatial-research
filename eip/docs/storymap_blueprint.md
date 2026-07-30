# StoryMap Blueprint

This blueprint keeps the StoryMap aligned with the revised report narrative. The story should read like a public-interest atlas first and a technical methods piece second.

## Story-wide settings

- Working title: `AI Compute Accessibility Atlas`
- Subtitle: `Where cloud compute is close, where it is far, and why that matters for cities`
- Byline: project / team attribution used for the EIP submission
- Navigation: turn on story navigation and use the section headings from this blueprint
- Theme direction: clean, map-first, low-distraction layout with short text blocks

## Section order

1. Hook
2. Why this matters
3. The question and the short answer
4. How the atlas works
5. What the atlas found
6. What this means for EIP
7. Limits to keep in view
8. About and sources

## 1. Hook

### Recommended block type

- `Sidecar` with a docked layout

### Media placement

- Slide 1 media: web map `Global Compute Accessibility`
- Optional fallback image: `outputs/figures/fig1_access_map.png`

### Copy goal

Open with the simplest public-facing idea: AI is not placeless. The cloud depends on real infrastructure, and that infrastructure is uneven.

### Draft copy direction

- Opening line: `AI does not happen on a blank map.`
- Second line: major cities do not sit equally close to AWS, Azure, and Google Cloud regions.
- Third line: this atlas maps those access gaps and asks what they mean for observed AI activity.

## 2. Why this matters

### Recommended block type

- Standard narrative section with one embedded map or image

### Media placement

- Primary media: web map `Global Compute Accessibility`
- Supporting image option: `outputs/figures/fig2_ai_map.png`

### Copy goal

Explain the stakes in plain language:

- compute is part of the enabling environment for AI
- unequal access to compute may reinforce unequal opportunity
- the atlas is meant as a screening and communication tool for judges, planners, and public-interest readers

### Required wording

- make clear that proximity is a proxy, not a direct measure of latency, price, or GPU availability
- make clear that the atlas is diagnostic, not causal

## 3. The question and the short answer

### Recommended block type

- Short narrative section followed by a `Quote` block or emphasis block

### Copy goal

State the central question and answer early, mirroring the revised report:

- question: once city size and geography are taken into account, do cities farther from major cloud regions tend to show less observed AI research activity?
- short answer: yes, AI-linked cities are much closer to deployed cloud regions than the broader city system, and the negative relationship remains in two spatial models

### Tone guidance

- keep this section short and confident
- do not bury the answer in methodological caveats
- include the causal boundary in one sentence only

## 4. How the atlas works

### Recommended block type

- `Sidecar` with 4 slides

### Media placement

- Slide 1: `Global Compute Accessibility`
- Slide 2: `AI Research and Hot Spots`
- Slide 3: `outputs/figures/fig7_distance_hist.png`
- Slide 4: `outputs/figures/fig5_coef_compare.png`

### Slide plan

1. **Distance to the nearest cloud region**  
   Explain compute accessibility as straight-line distance from a city to its nearest AWS, Azure, or Google Cloud region.
2. **Observed AI overlay**  
   Explain that the OpenAlex layer shows where the delivered filter observed AI-related research activity, not every AI-active city in the world.
3. **Clustering checks**  
   Define Moran's I as a whole-map clustering check and local Gi* as a neighborhood hot-spot / cold-spot check.
4. **Two spatial models**  
   Explain the GP and CAR/GMRF tracks as two readable ways to account for geography.

### Plain-English constraints

- define `OpenAlex` the first time it appears
- define `Moran's I`, `Gi*`, `Gaussian Process`, and `CAR/GMRF` in one sentence each
- keep equations out of the StoryMap

## 5. What the atlas found

### Recommended block type

- Main `Sidecar` for the result sequence
- Optional `Swipe` block for comparison

### Media placement and order

1. Web map `Global Compute Accessibility`
2. `outputs/figures/fig7_distance_hist.png`
3. Web map `AI Research and Hot Spots`
4. Web map `AI Deserts and Priority Cities`
5. `outputs/figures/fig6_sea_zoom.png`
6. `outputs/figures/fig13_subsaharan_africa_deep_dive.png`
7. `outputs/figures/fig14_latin_america_deep_dive.png`
8. `outputs/figures/fig5_coef_compare.png`

### Result sequence

#### Result 1: Compute access is uneven

- Message: large parts of the global city system remain far from major cloud regions
- Reader cue: focus on the broad corridor pattern, not on one city

#### Result 2: AI-linked cities sit much closer to compute

- Message: the AI-city distribution is shifted much closer to cloud regions than the full city frame
- Reader cue: use the histogram as the cleanest visual comparison

#### Result 3: The pattern is clustered, but not only because of a few hubs

- Message: hot spots and Moran's I show non-random clustering, but not an all-explaining single cluster story
- Reader cue: explain that the clustering is real but modest

#### Result 4: Priority cities surface stacked disadvantage

- Message: the priority layer highlights large cities with weak compute proximity and no observed AI works in the delivered overlay
- Reader cue: frame this as a screening layer, not a forecast

#### Result 5: The regional story changes by corridor

- Message: Southeast Asia looks like corridor concentration; Sub-Saharan Africa looks like scarcity; Latin America looks like concentration within partial coverage

#### Result 6: The models keep the same sign

- Message: distance stays negatively associated with observed AI activity in both spatial models, even though the magnitude shrinks under stronger local adjustment
- Reader cue: emphasize the sign first, then the attenuation

### Optional comparison block

- Block: `Swipe`
- Media:
  - left: `Global Compute Accessibility`
  - right: `AI Deserts and Priority Cities`
- Purpose: show how the access map becomes a policy-facing screening layer

## 6. What this means for EIP

### Recommended block type

- Narrative section followed by a short bullet list or quote block

### Copy goal

Translate the results into decision-facing language:

- compute accessibility looks like part of the story, not irrelevant background
- the atlas helps separate scarcity stories from concentration stories
- some large cities appear to face stacked disadvantage in the delivered data

### Closing sentence for this section

Use a line close to: `This atlas is stronger than a visual correlation and weaker than a causal estimate, which is exactly why it is useful as a screening tool.`

## 7. Limits to keep in view

### Recommended block type

- Short narrative section or `Accordion`

### Copy goal

Keep four limits visible without letting them take over the story:

- distance is a proxy, not the same thing as compute quality
- the OpenAlex layer is an observed delivered filter, not exhaustive ground truth
- the model sample is smaller than the full city frame
- the project does not estimate the causal effect of cloud-region openings

## 8. About and sources

### Recommended block type

- Standard narrative section with compact credits

### Include

- one-paragraph methods recap
- source list
- repo / reproducibility note
- note that ArcGIS Online publication is a browser workflow outside the local pipeline
- team attribution

## Asset placement summary

Use these local outputs as source media:

- `outputs/figures/fig1_access_map.png`
- `outputs/figures/fig2_ai_map.png`
- `outputs/figures/fig5_coef_compare.png`
- `outputs/figures/fig6_sea_zoom.png`
- `outputs/figures/fig7_distance_hist.png`
- `outputs/figures/fig13_subsaharan_africa_deep_dive.png`
- `outputs/figures/fig14_latin_america_deep_dive.png`

Use these web maps once they are available in ArcGIS Online:

- `Global Compute Accessibility`
- `AI Research and Hot Spots`
- `AI Deserts and Priority Cities`

## Checked against

- ArcGIS StoryMaps: Add sidecars
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-sidecars.htm>
- ArcGIS StoryMaps: Add swipe blocks
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-swipes.htm>
- ArcGIS StoryMaps: Add maps
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-maps.htm>
- ArcGIS StoryMaps: Add story navigation
  - <https://doc.arcgis.com/en/arcgis-storymaps/author-and-share/add-story-navigation.htm>
