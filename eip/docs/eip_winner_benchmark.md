# Harvard EIP winner benchmark (2023-2025)

This note benchmarks the current atlas against the standard signaled by official Harvard Center for Geographic Analysis (CGA) pages for the 2023, 2024, and 2025 Esri Innovation Program / Esri Innovation Prize winners.

## Official winner sources used

- 2023 EIP Award Winner - Harvard CGA  
  https://gis.harvard.edu/news/2023-eip-award-winner
- 2024 EIP Award Winner - Harvard CGA  
  https://gis.harvard.edu/news/2024-eip-award-winner
- 2025 EIP Award Winner - Harvard CGA  
  https://gis.harvard.edu/news/2025-eip-award-winner
- Awards overview page - Harvard CGA  
  https://gis.harvard.edu/awards

## What the winners suggest judges reward

### 1. The project solves a real public problem, not just a technical puzzle

The official winner titles themselves foreground concrete public-interest problems:

- 2023: flood risk and disaster vulnerability in Pakistan
- 2024: redevelopment of a 95-acre industrial parcel in Everett, Massachusetts
- 2025: livestock losses from large carnivore attacks in Laikipia, Kenya

**Implication for this repo:** the report and StoryMap should lead with the real-world problem of uneven AI infrastructure and why that matters for opportunity, not with models or statistical vocabulary.

### 2. The work is visibly useful to decision-makers

The official 2024 winner page includes a judges comment that the project's strength was its "practical use to policy makers" for Massachusetts and Everett.

**Implication for this repo:** the atlas should read as a decision-support tool. Priority cities, access gaps, and the meaning of the screening layer should be explained in terms that a judge can imagine a planner, policymaker, or public-interest organization using.

### 3. Professional finish matters

The official 2024 winner page describes the entry as a project completed with a "professional level of quality from start to finish."

**Implication for this repo:** the report should feel polished, coherent, and intentional. The opening, headings, figure callouts, and conclusion should feel submission-ready rather than like an internal technical memo.

### 4. Good evidence and documented sourcing stand out

The official 2023 winner materials praise "relevant data with well documented sources."

**Implication for this repo:** the report should clearly say what each dataset is, what it measures, and what it does not measure. Caveats around the OpenAlex overlay and the distance proxy should be easy to see, not buried.

### 5. Judges value robust, logical geographic analysis

The official 2023 winner materials praise "robust, logical geographic analysis."

**Implication for this repo:** the write-up should make the analysis feel orderly and intelligible. Each step should answer a plain-language question: where is compute, where is AI activity, how do the two line up, and what survives after basic controls for city size and geography.

### 6. Organization and visual readability are part of the quality bar

The official 2023 winner materials describe the project as presented in a "well organized, effective, visually pleasing manner."

**Implication for this repo:** the report should reduce dense academic prose, use clearer section purposes, and prepare readers before every major figure or table by telling them what to look for.

### 7. Engaging presentation matters, not just technical depth

The official 2025 winner page describes the work as geospatial analysis "presented in an engaging format."

**Implication for this repo:** the report should tell a readable story. The best order is: why this matters, what question is being asked, what the short answer is, how the atlas works, and what a judge should take away.

### 8. Breadth of GIS capability helps, but only when it serves the story

The official 2025 winner page highlights analysis that "covers much of the spectrum of GIS."

**Implication for this repo:** it is fine to retain the multi-layer structure of maps, hot spots, screening layers, and two model tracks, but the report should explain each layer as serving one clear purpose rather than showcasing technique for its own sake.

### 9. Strong projects connect rigor with accessible communication

Across the three winner pages, the repeated pattern is not just technical competence. The projects combine real stakes, credible evidence, polished presentation, and easy-to-grasp communication.

**Implication for this repo:** the report should keep the analysis disciplined while becoming much easier for a non-technical judge to follow. Accessibility should come from clearer framing and explanation, not from overstating the findings.

## Benchmark qualities to apply directly

For the current atlas, the strongest winner-aligned targets are:

1. **Lead with stakes.** Open with why AI infrastructure geography matters for who can participate in AI.
2. **Make the question obvious.** State the central research question and the short answer early.
3. **Sound useful.** Frame the atlas as a screening and decision-support tool, not just a descriptive exercise.
4. **Explain methods as tools.** Describe each method in terms of what it helps the reader learn.
5. **Protect trust.** Keep caveats visible so readability does not slide into overclaiming.
6. **Guide the eye.** Prepare readers for figures and tables with one-sentence takeaways.
7. **Close with public relevance.** End on what this atlas helps decision-makers see, while being explicit about what it does not prove.

## What this means for the rewrite

The revised report should move closer to the winner standard by doing all of the following:

- open like a public-interest project, not like a journal article
- explain the atlas as a tool for spotting infrastructure inequality and stacked disadvantage
- replace method-led transitions with question-led transitions
- define technical language the first time it appears
- separate findings, implications, and limits more cleanly
- keep the StoryMap blueprint aligned to the same hook, sequence, and public-value framing
