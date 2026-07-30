# AWARD_PLAYBOOK.md — EIP + Fisher Submission Playbook

> Actionable checklist, weighted scoring rubric, templates, and map specs tuned to Harvard CGA EIP Student of the Year + Fisher Prize judging logic.

---

## 1. Judging Logic Summary

*(Synthesized from official criteria language and recurring winner patterns. Source: `WINNER_MATRIX.md` criteria capture + winner feature extractions.)*

### 1a. Official Criteria Language

**EIP Student of the Year** (source: [CGA EIP page](https://gis.harvard.edu/event/edc-student-year-award)):  
Five named criteria: Potential impact · Innovation · Originality · Implementation · Organization.  
Submission format: ArcGIS StoryMap with bio, project description, Esri technology used, maps/narrative/apps/video/graphics/charts. Must be shared publicly.

**Fisher Prize** (source: [CGA Fisher page](https://gis.harvard.edu/event/fisher-prize-award-competition)):  
Five named criteria: Innovation and creativity of chosen topic · Use of GIS in performing the project · Data (complexity, relevance, documentation) · Analytical approach and execution · Visualization/cartographic communication effectiveness.  
Submission format: Poster (42"×36" PDF, ≤350 words) OR StoryMap URL.

**Key overlap:** Both awards prize innovation/originality, GIS implementation quality, and effective communication. The EIP explicitly values "potential impact" and Esri technology use; Fisher explicitly values data documentation and analytical execution.

### 1b. Implicit Priorities (inferred from 6 winner extractions, 2019–2025)

1. **Timeliness and real-world stakes** — Nearly every winner addresses a pressing global or local issue (flood risk, climate, conflict, urban development, conservation). Judges consistently reward "timely and important" topics. *Exemplars: [EIP-2023-1], [EIP-2021-1], [FIS-2023-G-1]*
2. **Logical, documented analysis chain** — Winners demonstrate a clear problem → data → method → results → interpretation arc. Judges praise "robust, logical geographic analysis" and "well documented sources." *Exemplars: [EIP-2023-1], [FIS-2025-UG-1], [EIP-2019-1]*
3. **Breadth of GIS spectrum** — The strongest entries use multiple GIS techniques (spatial statistics + overlay + network + visualization). Judges reward projects that "cover much of the spectrum of GIS." *Exemplars: [EIP-2025-1], [FIS-2023-G-1]*
4. **Professional-quality finish** — Judges use phrases like "professional level of quality from start to finish." Visual polish, organization, and completeness matter. *Exemplars: [EIP-2024-1], [EIP-2023-1]*
5. **Policy or practical applicability** — Projects with a clear audience beyond academia score higher. "Practical use to policy makers" was an explicit differentiator. *Exemplars: [EIP-2024-1], [FIS-2025-G-1]*
6. **Statistical integration with GIS** — Entries that combine spatial analysis with robust statistical methods are explicitly noted as standing out. *Exemplars: [EIP-2025-1], [FIS-2025-UG-1]*
7. **Open science and reproducibility** — At least one winner ([FIS-2025-UG-1]) was praised for linking to code and models, a rare and valued practice.

---

## 2. Feature Checklist

Organized by submission dimension. Each item should be verifiable before submission.

### 2a. Framing / Problem Choice
- [ ] Topic addresses a pressing, real-world issue with clear geographic dimensions. *[EIP-2023-1], [EIP-2025-1]*
- [ ] Problem statement is concise and understandable to a non-specialist in ≤2 paragraphs.
- [ ] Explicit statement of why the problem matters now (timeliness hook). *[EIP-2023-1], [FIS-2023-G-1]*
- [ ] Clear identification of who benefits from the analysis (policy makers, communities, researchers). *[EIP-2024-1]*
- [ ] The geographic scope is specific and justified (not vaguely "global"). *[EIP-2025-1], [FIS-2025-G-1]*

### 2b. StoryMap / Report Architecture
- [ ] Opening hook in the first screen: image + compelling one-sentence framing. *[Esri competition advice]*
- [ ] Hypothesis or research question stated within the first 3 sections. *[FIS-2025-UG-1]*
- [ ] Narrative follows: Context → Question → Data → Methods → Results → Interpretation → Conclusion. *[FIS-2025-UG-1], [EIP-2019-1]*
- [ ] Each section has a clear purpose; no filler sections. *[EIP-2024-1]*
- [ ] Sidecar blocks used for map-intensive sections; scrolling narrative for context. *[Esri competition advice]*
- [ ] Reader can understand the main finding without scrolling past the midpoint. *[Esri advice: "save deep GIS for later"]*
- [ ] Conclusion includes a specific takeaway or call to action. *[Esri competition criteria]*

### 2c. GIS / Cartography
- [ ] At least 3 distinct map types (e.g., choropleth, point density, 3D, network, heat map). *[EIP-2025-1], [EIP-2024-1]*
- [ ] Each map has a stated analytical purpose (not decorative). *[FIS-2025-UG-1]*
- [ ] At least one interactive web map embedded in the StoryMap. *[EIP-2024-1], [FIS-2025-G-1]*
- [ ] Mix of static (publication-quality) and dynamic (explorable) maps. *[FIS-2025-G-1]*
- [ ] Legends, scale bars, and source attributions visible on every map.
- [ ] Esri technology explicitly identified and purposefully used (for EIP). *[EIP-2024-1]*
- [ ] At least one spatial analysis beyond simple mapping (overlay, statistics, network, suitability). *[EIP-2025-1], [FIS-2022-G-1]*

### 2d. Evidence / Analysis
- [ ] Data sources are explicitly listed with provenance and date. *[EIP-2023-1]*
- [ ] Multiple data layers are combined in the analysis. *[FIS-2024-UG-1], [EIP-2023-1]*
- [ ] At least one quantitative/statistical method complements the spatial analysis. *[EIP-2025-1], [FIS-2025-UG-1]*
- [ ] Results are testable or reproducible; methodology is described precisely enough to replicate.
- [ ] Outliers or surprising results are explicitly discussed, not hidden. *[implied by "robust, logical" praise]*
- [ ] Open science: code, data links, or model documentation provided where feasible. *[FIS-2025-UG-1]*

### 2e. Originality
- [ ] The project does something that hasn't been done before at this scale, for this geography, or with this method combination.
- [ ] The novelty is stated in ≤2 sentences (judges need to see it quickly). *[FIS-2025-G-1], [FIS-2021-UG-1]*
- [ ] Methodology or data combination is harder to replicate casually (not just "I made a map of X").
- [ ] The innovation serves the research question (not innovation for its own sake).

### 2f. Packaging / Polish
- [ ] Custom visual theme (colors, fonts) that is consistent throughout. *[Esri competition winners]*
- [ ] Professional-quality images, no blurry screenshots or pixelated maps. *[EIP-2024-1]*
- [ ] No dead links, broken embeds, or login prompts in the StoryMap.
- [ ] Bio and professional photo included (EIP requirement).
- [ ] Sources/credits section is complete and accurate.
- [ ] Proofread for grammar, spelling, and consistency.
- [ ] Tested on mobile and multiple browsers. *[Esri submission rules]*

---

## 3. Weighted Scoring Rubric

Weights derived from frequency and emphasis of judge comments across 6 extracted winners, cross-referenced with official criteria.

| Category | Weight | 5 (Excellent) | 3 (Adequate) | 1 (Weak) | If Low, Do This |
|----------|--------|---------------|---------------|----------|-----------------|
| **Framing / Problem Choice** | 15% | Timely, compelling, clearly scoped geographic problem with identified beneficiaries. Reader immediately understands why it matters. | Reasonable topic but generic framing; no urgency or audience specified. | Topic is vague, not clearly geographic, or lacks real-world relevance. | Rewrite opening to name the specific problem, who is affected, and why now. Add a "why this matters" block within the first 3 sections. |
| **StoryMap Architecture** | 15% | Clear hypothesis-to-conclusion arc; each section earns its place; sidecars and narrative blocks purposefully deployed; conclusion has a takeaway. | Sections exist but feel like a list rather than an argument; some filler; no clear takeaway. | Disorganized; reader can't find the question or the answer; no conclusion. | Outline the 7-section arc (see templates 4a–4h) before building. Delete any section that doesn't advance the argument. |
| **GIS / Cartography** | 25% | Multiple map types, each with stated purpose; interactive + static mix; spatial analysis beyond basic mapping; Esri tech well-integrated. | Maps present but mostly one type; limited interaction; analysis is basic overlay or buffer. | Few or no maps; maps are decorative; no spatial analysis evident. | Add at least one analytical map (hot spot, suitability, network). Convert one static map to an interactive web map. Label each map with its analytical purpose. |
| **Evidence / Analysis** | 20% | Documented multi-source data; quantitative + spatial methods combined; results are reproducible; outliers discussed. | Data sourced but not documented; single method; results stated without interpretation. | Data undocumented; no clear method; results unsupported. | Add a data sources table. Describe methodology step-by-step in a methods sidecar. Run at least one statistical test to complement the GIS. |
| **Originality** | 15% | Clearly novel question, method, or data combination; novelty is stated and demonstrated; hard to replicate casually. | Some novelty but not clearly articulated; could be a class project anyone might do. | No discernible novelty; standard thematic map of a common topic. | Identify one "only I could do this because…" element: unique data access, novel method combination, or unusual geographic/temporal scope. State it explicitly. |
| **Packaging / Polish** | 10% | Professional finish; consistent theme; no broken elements; tested on mobile; bio/credits complete. | Generally clean but some inconsistencies; occasional formatting issues. | Broken links; inconsistent styling; missing credits; not tested beyond desktop. | Do a full QA pass: check all links, test on mobile, apply a custom theme, proofread. |

**Scoring:** Multiply each category score (1–5) by its weight. Maximum = 5.00. A competitive submission should target ≥ 4.00.

---

## 4. StoryMap / Report Templates & Snippets

### 4a. Opening Sidecar Copy
> **Purpose:** Hook the reader in the first screen. Left panel = emotional/contextual frame; right panel = study area or striking map.

```
[LEFT PANEL]
Title: [Compelling, specific title — consider a pun or framing device]
Subtitle: [One-line analytical summary]

In [PLACE], [STAKEHOLDERS] face [SPECIFIC PROBLEM]. [ONE SENTENCE on scale/severity].
This project uses [GIS METHOD] to [VERB: identify / map / analyze / reveal] [WHAT], 
offering [WHOM] a clearer picture of [OUTCOME].

[RIGHT PANEL: full-bleed map or striking image of the study area]
```

*Exemplars: [EIP-2025-1] uses a creative title + subtitle formula; [FIS-2025-G-1] frames from the pedestrian's perspective.*

### 4b. "Why This Matters" Block
> **Purpose:** Establish urgency and audience within the first 3 sections.

```
## Why This Matters

[PROBLEM] affects [NUMBER] people / [AREA] km² / [ECONOMIC VALUE] annually.
[ONE SENTENCE on trend: getting worse / underexplored / contested].

For [SPECIFIC AUDIENCE — e.g., urban planners, conservation managers, policy makers],
understanding [GEOGRAPHIC DIMENSION] of this problem is essential because 
[REASON: decisions are spatial / interventions need targeting / resources are limited].
```

*Exemplars: [EIP-2024-1] connects to Everett/MA policy makers; [EIP-2023-1] ties to the 2022 Pakistan floods.*

### 4c. Question / Short-Answer Block
> **Purpose:** State the research question and preview the answer.

```
## The Question

[CLEAR, SPECIFIC RESEARCH QUESTION — geographic, testable, scoped]

## The Short Answer

[2–3 sentences summarizing the main finding. Include one number or spatial pattern.]
The rest of this story shows how we arrived at this answer and what it means for [AUDIENCE].
```

*Exemplar: [FIS-2025-UG-1] follows a "hypothesis to conclusion" structure praised by judges.*

### 4d. Methods Sidecar
> **Purpose:** Explain methodology without breaking narrative flow. Sidecar: left = text, right = workflow diagram.

```
[LEFT PANEL]
## How We Did It

**Data:** [LIST sources, date ranges, spatial resolution. Link to open data where possible.]
**Tools:** [Esri products used — ArcGIS Pro, ArcGIS Online, Spatial Analyst, etc.]
**Approach:**
1. [Step 1: data acquisition and cleaning]
2. [Step 2: spatial analysis method]
3. [Step 3: statistical validation or secondary analysis]

[RIGHT PANEL: workflow diagram, data model, or screenshot of analysis in ArcGIS Pro]
```

*Exemplars: [EIP-2023-1] praised for "well documented sources"; [FIS-2025-UG-1] links to code and models.*

### 4e. Results Sidecar / Sequence
> **Purpose:** Present findings map-by-map, each with a "what this shows" statement.

```
[For each key result, use a sidecar panel:]

[LEFT PANEL]
## Finding [#]: [One-sentence finding]

[2–3 sentences explaining what the map reveals.
Highlight the most important spatial pattern.
Note any surprising or counterintuitive results.]

[RIGHT PANEL: thematic map, chart, or interactive web map]
```

*Exemplar: [EIP-2025-1] praised for maps that are "very well done" with integrated statistical analysis.*

### 4f. Case-Study Module
> **Purpose:** Zoom into one specific location that illustrates the broader pattern.

```
## Case Study: [PLACE NAME]

[LEFT PANEL]
[3–4 sentences telling a micro-story about this specific location.
Why did we zoom in here? What does this case reveal that the overview map doesn't?
Include a human or policy dimension if possible.]

[RIGHT PANEL: zoomed-in map, before/after comparison, or photo + map overlay]
```

*Exemplar: [FIS-2024-UG-1] uses historic maps and archival images to illustrate specific destruction at named locations.*

### 4g. Interpretation / "So What" Block
> **Purpose:** Connect findings back to the problem and the audience.

```
## What This Means

[2–3 sentences interpreting the key findings in plain language.]

For [AUDIENCE], these results suggest [SPECIFIC IMPLICATION]:
- [Implication 1: e.g., "Priority areas for intervention are concentrated in X"]
- [Implication 2: e.g., "Current policies miss Y, which our analysis reveals"]

[Optional: comparison with prior work or expected patterns. 
Note any limitations honestly — judges respect intellectual honesty.]
```

*Exemplar: [EIP-2024-1] praised for "practical use to policy makers."*

### 4h. Sources / Credits Close
> **Purpose:** Demonstrate data rigor and give credit.

```
## Data Sources & Methods Documentation

| Dataset | Source | Date | Resolution | Access |
|---------|--------|------|------------|--------|
| [Dataset 1] | [Provider] | [YYYY] | [spatial res] | [URL or "Harvard Dataverse"] |

## Tools & Software
[ArcGIS Pro X.X, ArcGIS Online, Spatial Analyst, etc.]

## Code & Reproducibility
[Link to GitHub/Dataverse if applicable — see [FIS-2025-UG-1] for model]

## Acknowledgments
[Faculty advisor, CGA staff, data providers, etc.]

## Author
[Name, program, Harvard school, professional photo, contact]
```

### 4i. "Novelty Statement" Callout
> **Purpose:** Make your innovation visible to judges who may skim.

```
[CALLOUT BOX or highlighted text]
What's new here: [ONE SENTENCE describing the novel contribution — 
new data combination, new method application, new geographic scope, 
or new question that couldn't be answered before this analysis.]
```

*Exemplar: [FIS-2025-G-1] — judges explicitly called the approach "novel."*

### 4j. "Open Science" Sidebar
> **Purpose:** If you've shared code/data, highlight it. This is rare and rewarded.

```
[SIDEBAR]
Open Science: The code, data, and models behind this analysis are available at [LINK].
We believe reproducibility strengthens geographic research.
```

*Exemplar: [FIS-2025-UG-1] — judges praised "open science with links to code and models."*

---

## 5. Map Kit

> Minimum map set for a competitive EIP + Fisher submission and what each map must prove.

| Map # | Type | Purpose / What It Must Prove | Required Layers | Interaction | Exemplars |
|-------|------|------------------------------|-----------------|-------------|-----------|
| M1 | **Study Area Overview** | Orient the reader; establish geographic scope and context. | Basemap + study boundary + key reference features | Static or light interactive (zoom/pan) | All 6 extracted winners |
| M2 | **Thematic / Choropleth** | Show the spatial distribution of the core variable (risk, density, access, etc.). | Classified data layer + legend + basemap | Static (publication-quality) | [EIP-2023-1], [FIS-2019-G-1] |
| M3 | **Analytical Result Map** | Demonstrate a spatial analysis output (hot spots, clusters, suitability, network). | Analysis output layer + input layers for context | Interactive (click for details) | [EIP-2025-1], [FIS-2022-G-1] |
| M4 | **Multi-variable / Overlay** | Show how 2+ variables interact spatially (overlay, bivariate, composite index). | ≥2 data layers with clear visual encoding | Static or interactive | [FIS-2024-UG-1], [EIP-2024-1] |
| M5 | **Case-Study Zoom** | Drill into one location that exemplifies the broader finding. | Subset of M2–M4 layers at larger scale | Static with annotations | [FIS-2024-UG-1], [FIS-2021-G-1] |
| M6 | **Temporal / Change Map** (optional but powerful) | Show change over time (before/after, time series, animation). | Multi-temporal data | Swipe, slider, or animation | [FIS-2023-G-1] (pre/post-war) |
| M7 | **3D / Scene** (optional, high impact for EIP) | Add dimensionality for urban, terrain, or volumetric data. | 3D scene layers or CityEngine output | Interactive 3D viewer | [EIP-2024-1] (3D build-out) |

**Minimum for competitiveness:** M1 + M2 + M3 + M5 = 4 maps.  
**Strong submission:** All of M1–M5 plus at least one of M6 or M7 = 6–7 maps.

---

## 6. Watch-Outs / Failure Modes

| # | Failure Mode | How to Detect | How to Fix | Exemplar Reference |
|---|-------------|---------------|------------|-------------------|
| 1 | **Overtechnical opening** — first screen is jargon-heavy, no hook | Read the first 50 words aloud to a non-GIS friend. If they tune out, it's too technical. | Move context/methods after the hook. Lead with a human story, a striking statistic, or a provocative question. | [EIP-2025-1] leads with a compelling title; [FIS-2025-G-1] frames from a pedestrian's POV. |
| 2 | **Decorative maps** — maps present but don't prove anything | For each map, state in one sentence what it proves. If you can't, it's decorative. | Replace with an analytical map or remove. Every map earns its place by answering a sub-question. | [FIS-2025-UG-1] uses maps to "communicate the interplay" between variables. |
| 3 | **Single-method analysis** — only one GIS technique used | Count your distinct spatial analysis methods. If it's just one buffer or overlay, it's thin. | Add a spatial statistics method (hot spot, clustering) or a different analytical approach (network, suitability). | [EIP-2025-1] praised for covering "much of the spectrum of GIS." |
| 4 | **Undocumented data** — data sources not listed or dated | Check: can a reader find and download every dataset you used? | Add a data sources table (template 4h) with provenance, date, resolution, and access link. | [EIP-2023-1] praised for "well documented sources." |
| 5 | **Missing conclusion / no takeaway** — story ends with "here are the maps" | Read the last section. Does it answer "so what?" | Add an interpretation block (template 4g) and a specific recommendation or call to action. | [EIP-2024-1] praised for "practical use to policy makers." |
| 6 | **Generic topic with no geographic angle** — "climate change is bad" | Ask: does this project do something that only spatial analysis can reveal? | Sharpen the research question to require a geographic answer (where, how far, which areas). | All winners have place-specific, geographically scoped questions. |
| 7 | **Broken embeds / login prompts** — interactive maps fail for external viewers | Test the StoryMap URL in an incognito browser on desktop + mobile. | Re-share all embedded web maps and apps as "public." Remove layers requiring authentication. | [Esri rules: "Suddenly getting a login prompt is a big no-no."] |
| 8 | **No interactive maps** — all maps are static images | Count your interactive (clickable, explorable) maps. If zero, the StoryMap feels like a PDF. | Convert at least one key result map to an ArcGIS Online web map and embed it. | [EIP-2024-1] praised for "engaging interactive maps." |
| 9 | **No statistical complement to GIS** — spatial analysis alone | Check: did you run any statistical test, regression, or quantitative validation? | Add one statistical method (regression, spatial autocorrelation, chi-square) that validates or extends the GIS findings. | [EIP-2025-1] praised for "integration of geospatial analysis with robust statistical analysis." |
| 10 | **Wall-of-text sections** — long prose blocks without visual breaks | Scroll through the StoryMap. Any section > 3 paragraphs without a visual? | Break long text into sidecar format with maps/images on the paired panel. | [Esri advice on purposeful block usage.] |
| 11 | **Hidden originality** — the novel contribution isn't stated | Search your text for "novel," "new," "first," "unique." If absent, judges may miss it. | Add a novelty statement callout (template 4i) in the methods or results section. | [FIS-2025-G-1] — judges called the approach "novel" because the author made it visible. |
| 12 | **No bio or professional photo** (EIP) | Check the opening for a short bio and headshot. | Add a brief author bio with photo, program, and school per EIP requirements. | [EIP submission requirements.] |
| 13 | **Inconsistent visual theme** — mismatched colors, fonts, or styling | Compare the first and last sections visually. Do they look like the same document? | Apply a custom theme in ArcGIS StoryMaps builder. Choose a palette complementing your map symbology. | [Esri competition: "nearly every winner in 2024 used a custom theme."] |
| 14 | **Overloaded maps** — too many layers, unclear symbology | Show each map to someone unfamiliar with GIS. If they can't ID the main pattern in 5 seconds, it's overloaded. | Simplify: one main layer per map, clear legend, minimal basemap detail. Use annotations to guide the eye. | Judges praise "effective cartographic techniques" ([FIS-2022-G-1]). |
| 15 | **No multimedia variety** — only maps and text | Count content types: maps, charts, images, diagrams, video. If ≤2, the StoryMap may feel monotonous. | Add at least one non-map visual (chart, photo, diagram) to break the rhythm. | [FIS-2021-G-1] praised for combining "GIS with historic maps, photos, audio, and video." |

---

## 7. Exemplar Cross-Reference Convention

All recommendations in this playbook reference entries in `WINNER_MATRIX.md` using the ID convention `[EIP-YYYY-#]`, `[FIS-YYYY-UG-#]`, `[FIS-YYYY-G-#]`, or `[BM-YYYY-#]`.

> **Rule:** Every major recommendation must cite ≥ 2 exemplars from the matrix when possible.

**Cross-reference summary (IDs used in this playbook):**

| ID | Short Title | Award | Year | Key Playbook Contributions |
|----|------------|-------|------|---------------------------|
| [EIP-2025-1] | Livestock & Livelihoods, Kenya | EIP | 2025 | GIS breadth, statistical integration, creative title |
| [FIS-2025-UG-1] | Natural Resources & Rebel Legitimacy | Fisher UG | 2025 | Hypothesis-to-conclusion structure, open science, publication quality |
| [FIS-2025-G-1] | Cool Walking Routes, Boston | Fisher G | 2025 | Novel approach, pedestrian framing, static+dynamic mix |
| [EIP-2024-1] | Everett Express, MA | EIP | 2024 | Professional polish, policy relevance, 3D analysis, interactive maps |
| [FIS-2024-UG-1] | Finding Anfal, Kurdistan | Fisher UG | 2024 | Archival+modern data fusion, historical GIS, vivid visualization |
| [EIP-2023-1] | Flood Risk, Pakistan | EIP | 2023 | Data documentation, timeliness, visual organization |
