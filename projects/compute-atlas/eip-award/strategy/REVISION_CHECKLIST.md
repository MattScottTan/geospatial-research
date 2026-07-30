# REVISION_CHECKLIST.md — Section-by-Section Editing Guide

> This file is the reference checklist for revising the AI Compute Accessibility Atlas StoryMap.  
> Each time a section is submitted for review, check it against the relevant items below.  
> Mark items [x] as they are addressed. Add notes on what changed.

---

## Global Rules (apply to EVERY section)

### Prose Tightness
- [ ] **No repeated claims** — if a point was made in an earlier section, reference it, don't restate it. Key offenders to track:
  - "Compute is not destiny" → **max 2 occurrences total** (once in findings transition, once in conclusion)
  - Median distance comparison (657 km vs 237 km) → **state once with numbers, then reference as "the gap" thereafter**
  - "The project does not claim a definitive causal estimate" → **state once clearly, then use shorter phrasing like "as a correlate, not a cause"**
- [ ] **Figure captions must be additive** — never duplicate body text. Captions should add: data source, method detail, reading instruction, or a nuance the body doesn't cover.
- [ ] **Cut filler transitions** — phrases like "That is why…", "This matters because…", "In other words…" often introduce restated points. If the sentence after the transition says something the reader already knows, cut the whole paragraph.
- [ ] **Target prose reduction of ~25%** across the full StoryMap.

### Cartographic / Visual References
- [ ] **Every map referenced in text must have**: a readable legend, scale bar, source attribution, and a clear title stating what it shows analytically (not just the topic).
- [ ] **Name the map type and analytical purpose** when introducing a figure — e.g., "The hot spot map (Getis-Ord Gi*) identifies statistically significant clusters…" not just "the map shows clusters."

### Esri Technology Visibility
- [ ] **Name Esri tools explicitly** whenever a method is described — e.g., "using Hot Spot Analysis (Getis-Ord Gi*) in ArcGIS Pro" rather than just "hot spot analysis."
- [ ] This is an EIP judging criterion ("Implementation") and judges look for it.

### Markdown / Formatting
- [ ] **No raw markdown artifacts** in the live StoryMap (e.g., `**bold**` showing as asterisks instead of rendering).
- [ ] **Bold** used sparingly for key numbers and takeaway statements only — not for entire sentences.

---

## Section-Specific Checklists

### SECTION 1: Opening / Title / Hook (Pages 1–2)

**Current strengths:** "AI does not happen on a blank map" is a strong hook. Subtitle is clear.

- [ ] **Add author bio + professional photo** — EIP requires: short bio, professional picture, program/school, reason for applying. Place this near the top or as a sidecar.
- [ ] **Sharpen the first sentence** — consider leading with the most striking number: e.g., "The median city in the world's 8,000 largest urban areas is 657 km from its nearest cloud compute region. For cities producing AI research, that number drops to 237 km."
- [ ] **Fix markdown rendering** — page 1 shows `**8,000 cities**` with visible asterisks. Verify in live StoryMap.
- [ ] **Cut or tighten the second paragraph** (p.2, "Cities do not enter the AI economy…") — it restates the opening without adding new information. Either cut it or merge the strongest sentence into the opening.
- [ ] **The "public-interest screening tool for judges, planners, and readers" sentence** — this is excellent framing. Keep it, but move it closer to the opening so judges see it immediately.
- [ ] **"Short answer: yes"** block — this is great and matches the playbook template 4c. Keep it. But the qualifying clause at the end ("although the project does not claim a definitive causal estimate") feels like it arrives too early. State the finding confidently first; add the caveat in the methods section.
- [ ] **Figure on page 2** ("Recent AI research activity is concentrated…") — caption duplicates body text. Rewrite caption to add: data source (OpenAlex), matching method, or a reading instruction ("Each dot is one of 328 matched AI cities; color shows distance to the nearest cloud region").

**Revision targets for this section:**
- Reduce from ~2 pages to ~1.3 pages
- Bio added
- One striking number in the first sentence
- Caveat moved to methods

---

### SECTION 2: How the Atlas Works (Page 3)

**Current strengths:** Clear 3-step explanation (city frame → cloud regions → AI overlay). Good structure.

- [ ] **Name Esri tools** — "maps major deployed cloud regions" should become "maps major deployed cloud regions using ArcGIS Pro and ArcGIS Online." "measures the distance" should specify the tool (Near analysis, geodesic distance, etc.).
- [ ] **Add a data callout** — this section should contain (or link to) the data sources: Natural Earth cities, hyperscaler region lists (AWS/Azure/GCP — specify how region locations were compiled), OpenAlex for AI works. Even a brief inline list helps; a full table goes in the closing section.
- [ ] **"spatial diagnostics and models"** — name them: "spatial diagnostics (Getis-Ord Gi* hot spot analysis) and models (spatial lag and spatial error regression in ArcGIS Pro)."
- [ ] **Figure caption** (p.3, "Distance from each city…") — currently duplicates the body text almost verbatim. Rewrite: add the data source, the number of cloud regions mapped, and a reading instruction.
- [ ] **This section is already tight** — minimal cutting needed. The main improvement is adding specificity (tool names, data sources).

**Revision targets:**
- Esri tools named at least 3 times
- Data sources mentioned inline
- Caption rewritten to be additive

---

### SECTION 3: What the Atlas Found — Main Descriptive Finding (Pages 3–4)

**Current strengths:** The 657 km vs 237 km comparison is powerful and clearly stated.

- [ ] **State the key numbers ONCE here** — then in all later sections refer to "the median distance gap" without re-quoting the numbers.
- [ ] **Histogram figure (p.4)** — the caption currently says "AI-linked cities sit much closer to major cloud regions than the broader city system. Histogram comparing…" This is purely descriptive. Rewrite to add: sample sizes (n=7,999 vs n=328), the log-distance axis note, and a reading instruction ("The orange distribution shifts sharply left, showing AI-linked cities cluster near compute").
- [ ] **"72% of AI cities are within 500 km"** — this stat is visible in the figure's "Quick read" box but not stated in the body text. Pull it into the prose — it's more vivid than the median alone.
- [ ] **The sentence "That means AI-linked cities are not just slightly more connected to compute"** — good emphasis. Keep.

**Revision targets:**
- Numbers stated once, with "the gap" used as shorthand after
- 72% stat pulled into body text
- Caption made additive

---

### SECTION 4: Weighted Concentration (Pages 4–5)

**Current strengths:** Weighted median (164 km) adds analytical depth. Good that it shows activity-weighted geography differs from simple city counts.

- [ ] **Tighten** — this section can be shortened. The point (weighted view shifts even closer to compute) can be made in 2–3 sentences rather than the current ~6.
- [ ] **Caption** (p.5, "When the overlay is weighted…") — again duplicates body text. Rewrite to add: what the cumulative share line shows, how weighting works.
- [ ] **Consider merging** this section with the main descriptive finding above — they make the same core point (AI activity concentrates near compute), just with different weightings.

**Revision targets:**
- Cut by ~40%
- Caption rewritten
- Possibly merge with Section 3

---

### SECTION 5: Spatial Organization / Hot Spots (Pages 5–6)

**Current strengths:** 7 hot spots and 33 cold spots — specific numbers that show rigor.

- [ ] **Name the method explicitly**: "Using Getis-Ord Gi* analysis in ArcGIS Pro, the atlas identifies 7 statistically significant hot spots and 33 cold spots at the 95% and 99% confidence levels."
- [ ] **Cut the restatement** — "This matters because it shows that the geography of AI opportunity has real spatial structure. The project is not simply highlighting a few famous tech hubs." The first sentence restates the section header; the second restates the opening. Cut both.
- [ ] **Hot spot map caption** — currently says "only a limited number of statistically strong clusters appear." Rewrite to add: confidence levels, what hot spot vs cold spot means in this context, Gi* method reference.
- [ ] **Add 1–2 specific hot spot names** in the body text — "Hot spots include [city/region], while cold spots are concentrated in [region]." This makes the abstract analysis concrete.

**Revision targets:**
- Esri tool named
- 2 restatement sentences cut
- Specific hot/cold spot names added
- Caption rewritten

---

### SECTION 6: Screening Tool / Policy Relevance (Pages 6–7)

**Current strengths:** 1,988 priority cities is a strong, specific number. Lagos example is well-placed.

- [ ] **This section is good** — relatively tight, clear audience (planners, innovation agencies). Minor tightening only.
- [ ] **"In the current build, the priority screen flags 1,988 cities"** — "In the current build" is hedging language. Cut it: "The priority screen flags 1,988 cities that…"
- [ ] **Lagos mention** — good that it appears here as a preview. Keep, but make sure the Lagos case study (later) doesn't restate this introduction.
- [ ] **Caption** (p.6) — duplicates body text. Rewrite to add: how "priority" is defined (zero AI works + distance above upper-quartile threshold), and what the color ramp encodes.

**Revision targets:**
- Minor tightening
- Remove "in the current build" hedge
- Caption rewritten

---

### SECTION 7: Model Check (Page 7)

**Current strengths:** Two spatial model specs with coefficient comparison. Honest about effect shrinkage.

- [ ] **Name the models explicitly**: "A spatial lag model (SLM) and a conditional autoregressive model (CAR) were estimated using [tool]." Currently the chart says "SP" and "CARSMM" which are abbreviations that readers may not follow.
- [ ] **Add confidence intervals or explain their absence** — the chart shows point estimates only. Either add error bars, or add a sentence: "Standard errors are available in the project pipeline but are omitted here for visual clarity; the directional sign is robust across both specifications."
- [ ] **"That is why the project treats compute access as a meaningful correlate and screening layer, rather than as a proven universal causal driver."** — This is the best statement of the caveat. If this is kept, the earlier caveat on page 2 can be cut.
- [ ] **Tighten** — the paragraph before the figure and after the figure both say essentially the same thing (distance coefficient is negative, shrinks with geography controls). State once.

**Revision targets:**
- Model names spelled out
- Confidence interval note added
- Duplicate paragraph merged into one
- This becomes the canonical location for the causal caveat

---

### SECTION 8: Beyond Distance — Infrastructure Bundle (Pages 7–9)

**Current strengths:** The bundle concept is the project's second big analytical contribution. The scatter plot (bundle score vs distance-only score) is a strong visualization.

- [ ] **CRITICAL: Specify the bundle components** — what variables go into "connectivity, institutional depth, and local infrastructure context"? List them. This is the single most important missing piece for judges evaluating "data complexity" and "analytical approach." E.g.: "The bundle index combines: (1) distance-only compute access score, (2) internet penetration rate, (3) tertiary education enrollment, (4) electricity reliability index, (5) [etc.]."
- [ ] **Name the method** — is the bundle a weighted overlay? PCA? Equal-weight composite? State it.
- [ ] **"Compute access matters most when it is reinforced by the rest of the infrastructure bundle"** — this is a key finding. State it more precisely: what's the correlation between bundle score and AI works? Is it stronger than distance alone?
- [ ] **Top Cities bar chart** (p.10) — good visualization. Caption should note: how many cities are shown, what the score range means, and which cities are surprising omissions or inclusions.
- [ ] **Scatter plot** (p.9) — effective visualization. Caption should add: what the diagonal represents, which cities deviate most and in which direction.
- [ ] **"In other words, the originality of this project is not just that it maps compute"** — this is a novelty statement but it's buried. Consider making it a **callout box** (template 4i) so judges can't miss it.
- [ ] **Cut repetition** — pages 8-9 restate the bundle concept 3 times ("extends the atlas beyond distance alone," "not a replacement for the original atlas," "depends on how compute access combines with the rest of the urban infrastructure system"). State once.

**Revision targets:**
- Bundle components listed
- Method named
- 3 restatements cut to 1
- Novelty callout box added
- Captions rewritten

---

### SECTION 9: Four City Case Studies (Pages 10–18)

**Current strengths:** The 2×2 typology (near/far compute × high/low AI) is analytically elegant. Each case has a clear role. Takeaway sentences at the end of each case are effective.

**Applies to ALL four cases:**
- [ ] **Fix the "Local Ecosystem" charts** — raw lat/lon axes are confusing. Replace with local-scale maps on a real basemap, or at minimum add "Latitude" / "Longitude" axis labels and a city boundary underlay.
- [ ] **Upgrade regional context maps** — add richer basemap (terrain or political), label surrounding major cities, make cloud region symbols larger and labeled with provider name + region name.
- [ ] **Cut the typology preview** (p.10, "one where the full bundle aligns strongly, one where the research overlay understates…") — by this point the reader is committed. Let each case speak for itself.
- [ ] **Each case should be ~30% shorter** — cut the setup paragraphs that re-explain why the case was chosen. The section header (e.g., "Singapore: Near compute / high AI") already tells the reader.

**Singapore (pp.11–12):**
- [ ] Tight and effective. Minor cuts only. The Regional Context map could use more labels.
- [ ] The takeaway sentence is strong. Keep.

**Seoul (pp.13–14):**
- [ ] **Tighten significantly** — Seoul's section takes almost 2 pages but the core insight ("near compute but low in delivered research overlay; broader ecosystem is stronger than the overlay suggests") can be stated in half the space.
- [ ] **"That tension is exactly why it belongs in the StoryMap"** — this is meta-commentary. Cut. Let the reader feel the tension from the data.
- [ ] The local ecosystem chart shows only 1 top-institution anchor (Myongji University) and 10 AI works. Consider noting this is an undercount — Seoul has KAIST, SNU, etc. that may not appear in the OpenAlex match.

**Ho Chi Minh City (pp.14–16):**
- [ ] Good case. Tighten the setup — the reader already understands the typology.
- [ ] **"This is the case that most clearly demonstrates why the project needs case studies alongside the atlas"** — meta-commentary. Cut.

**Lagos (pp.16–18):**
- [ ] Strong case with public-interest weight. Keep the "stacked disadvantage" framing.
- [ ] **The regional context map shows "Middle East (Israel) - ???"** — this looks like a rendering artifact or unfinished label. Fix immediately.
- [ ] Local ecosystem chart shows 0 AI works and 0 top-institution anchors. This is a powerful data point — make sure the prose emphasizes it rather than softening it.
- [ ] **Cut** "Lagos is not a marginal city. It is one of the largest urban markets in Africa" — this was already stated on page 6. Reference it: "As noted above, Lagos is one of the largest urban markets globally but…"

**Case study summary (p.18):**
- [ ] The four-sentence summary paragraph is effective. Keep.
- [ ] **"The result is a more mature conclusion"** — cut "more mature." Just say "The conclusion: compute is not destiny, but it is part of the infrastructure bundle that shapes AI opportunity."

**Revision targets:**
- All 4 Local Ecosystem charts fixed or replaced
- All 4 Regional Context maps upgraded
- Each case ~30% shorter
- Lagos map artifact fixed
- Meta-commentary sentences cut

---

### SECTION 10: What This Means / Conclusion (Pages 19–20)

**Current strengths:** The conclusion is well-framed and avoids overclaiming. "Compute is not destiny. But it is not irrelevant either." is a strong closing line.

- [ ] **This is where "compute is not destiny" should appear for the final time** — cut all earlier occurrences except one in the findings transition.
- [ ] **Cut redundancy** — the conclusion restates the four-case summary from page 18 almost verbatim. Cut the restatement and instead add a **forward-looking sentence**: "For planners and innovation agencies, the atlas provides a starting point for identifying where compute-access investments could have the greatest impact on AI opportunity."
- [ ] **The "quadrant" map (p.19)** is a strong closing visual — High AI/High access, High AI/Low access, etc. Make sure the caption explains the quadrant definitions clearly.
- [ ] **The final paragraph about screening tool** (p.20) restates earlier material. Cut or merge into the policy sentence above.
- [ ] **Add a sources/credits close** after this section (see Section 11 below).
- [ ] **End with the strongest sentence**, not a restatement. Current ending trails off into the four-case restatement. Better: end with the practical forward-looking statement.

**Revision targets:**
- Cut restatements from earlier sections
- Add forward-looking policy sentence
- Reorder so the strongest sentence is last
- Add sources section after

---

### SECTION 11: Sources / Credits / Close (MISSING — must add)

- [ ] **Data sources table** — list every dataset with provider, date, spatial resolution, and access link:
  - City frame: Natural Earth + [source for population data]
  - Cloud regions: AWS/Azure/GCP — how compiled (public documentation? specific URL?)
  - AI works: OpenAlex — query parameters, date range, matching methodology
  - Bundle index components: list each variable and its source
  - Basemaps: Esri, TomTom, USGS, FAO, NOAA (already credited in map footers)
- [ ] **Tools & Software**: ArcGIS Pro [version], ArcGIS Online, specific toolbox references (Spatial Statistics, Network Analyst if used), Python/R if used for data processing
- [ ] **Code & Reproducibility**: link to GitHub/Harvard Dataverse if available
- [ ] **Acknowledgments**: faculty advisor, CGA staff, data providers
- [ ] **Author bio**: name, program, Harvard school, professional photo, contact

---

## Tracking Log

| Date | Section Reviewed | Items Addressed | Notes |
|------|-----------------|-----------------|-------|
| *(to be filled as sections are submitted)* | | | |
