# Fisher Award Playbook

## Packet Links
- [Fisher Award Playbook](fisher_award_playbook.md)
- [Feature Matrix](feature_matrix.md)
- [Scoring Rubric](scoring_rubric.md)
- [Production Timeline](production_timeline.md)
- [Topic Scoring Template](topic_scoring_template.md)


## Winning Thesis
A Fisher Prize submission should make a judge believe this sentence: **“The GIS work produced an insight that would be difficult or impossible to see without spatial analysis.”** The winning strategy is not to make the prettiest map or the most complicated model; it is to combine a high-stakes spatial question, documented data, defensible analysis, and cartography that makes the conclusion visible quickly. Past winners repeatedly use GIS to reveal hidden structure: destroyed settlements, disaster exposure, unequal access, territorial fragmentation, historical change, ecological risk, or spatial causes of political and social outcomes.

## Spatial Necessity

### Pass/fail tests
A project is spatially necessary when at least four statements are true:

- Removing the map/model removes the central evidence.
- The research question depends on **where**, **how far**, **which places changed**, **who is exposed**, **what is connected**, or **what overlaps**.
- The GIS workflow includes a nontrivial spatial operation: change detection, classification, overlay, network analysis, location-allocation, spatial statistics, 3D modeling, suitability/risk modeling, or temporal reconstruction.
- The data resolution and scale are intentionally chosen.
- The final map is evidence for the claim, not decoration after the claim.

### Strong examples from past-winner patterns
- **Flood detection / Mariupol urban change:** the answer depends on satellite classification and temporal comparison.
- **Storm surge risk:** the argument depends on overlap between hazard exposure and socioeconomic vulnerability.
- **Transportation-land use accessibility:** network GIS produces accessibility polygons that a non-spatial paper cannot replace.
- **South Caucasus archaeometallurgy:** spatial and chemical datasets are integrated across micrometer-to-kilometer scales.

### Fix if weak
Rewrite the topic from “I will map X” to one of these forms:

- “Where is X concentrated, and why there?”
- “Who gains or loses access because of spatial arrangement?”
- “What changed between time A and time B?”
- “Which places face the highest combined exposure and vulnerability?”
- “How does territory, infrastructure, or distance shape the outcome?”

## Topic Strategy

### Pick a judge-visible spatial problem
The strongest topics usually combine at least two of these qualities:

- Social, environmental, historical, or policy significance.
- A hidden or under-documented geography.
- A spatial pattern that can be measured rather than merely described.
- Multiple credible datasets that can be joined, compared, classified, or modeled.
- A cartographic output that will be immediately legible.

### Strong topic archetypes
Use the [Winning Archetype Matrix](feature_matrix.md#winning-archetype-matrix) to shape the topic.

- **Conflict/territory:** destruction, control, displacement, borders, political violence.
- **Climate/disaster/environmental risk:** flood, fire, sea-level rise, recovery, hazard exposure.
- **Urban inequality/access:** green space, transit, services, health exposure, redistricting.
- **Historical/archaeological reconstruction:** lost landscapes, field evidence, 3D terrain, archival maps.
- **Remote sensing/computational GIS:** classification, image change, ML, large-scale monitoring.
- **Critical cartography/design:** cartography as argument about power, territory, or landscape.

### Make novelty defensible
Do not claim “no one has ever studied this.” Instead, frame novelty as:

- a new spatial scale;
- a new data combination;
- a new temporal comparison;
- a new method applied to a known geography;
- a new visualization of an under-seen pattern;
- a decision-relevant metric not previously mapped in the project context.

## GIS Method Strategy

### Method escalator

| Level | Method | Fisher competitiveness |
|---|---|---|
| 1 | Plot points / simple choropleth | Weak unless the data itself is exceptionally novel. |
| 2 | Overlay and thematic comparison | Acceptable if tied to a clear question. |
| 3 | Accessibility, buffers, service areas, spatial joins | Competitive when assumptions are justified. |
| 4 | Network analysis, location-allocation, suitability/risk modeling, classification, spatial statistics | Strong; GIS is visibly doing work. |
| 5 | Multi-source spatiotemporal modeling, remote sensing/ML with validation, 3D reconstruction, cross-scale integration | Prize-contender if clearly communicated and not overcomplicated. |

### Tactical method upgrades
- Replace Euclidean buffers with network travel distance when access matters.
- Replace “before/after screenshots” with classified change detection.
- Replace “risk map” with exposure × vulnerability × uncertainty.
- Replace “many layers” with a transparent weighted model and sensitivity check.
- Replace “nice 3D terrain” with 3D terrain + field/archival evidence + interpretation.
- Replace “ML result” with model output + accuracy assessment + error examples.

## Data Strategy

### Required data discipline
Every project should include a compact data table with:

- dataset name;
- source / URL;
- date accessed;
- spatial resolution or unit;
- temporal coverage;
- coordinate reference system / projection if applicable;
- preprocessing performed;
- why the dataset is relevant;
- known limitations.

### Complexity with control
The data stack should be complex enough to impress but controlled enough to trust. A winning data stack often has:

- one core outcome layer;
- one or more explanatory/exposure layers;
- one contextual layer;
- one validation or comparison source.

### Documentation moves that signal rigor
- Note projection and scale choices.
- Explain temporal alignment if comparing years.
- Disclose missing data and uncertainty.
- Use one sensitivity check when weights/thresholds matter.
- Cite base maps and data providers without using the 350-word descriptive text budget if poster route permits citations outside the cap.

## Analytical Execution

### Strong execution checklist
- The workflow is reproducible enough that another GIS user could understand it.
- Parameters are listed: thresholds, buffers, classification classes, weights, model settings.
- The analysis has at least one internal check: validation sample, comparison to known event, sensitivity test, or manual review of a subset.
- Results are quantified, not just shown visually.
- Interpretation stays within what the data can support.
- Limitations are acknowledged briefly and strategically.

### Workflow pattern
Use this structure in poster/StoryMap methods:

1. **Data ingestion:** sources, coverage, preprocessing.
2. **Spatial operation:** classification, overlay, network model, change detection, etc.
3. **Validation/check:** accuracy, sensitivity, manual sample, external comparison.
4. **Result metric:** area affected, population exposed, access differential, change magnitude, risk ranking, cluster pattern.
5. **Interpretation:** why the spatial result matters.

## Visualization Strategy

### Poster route
A winning poster should be understandable in three passes:

1. **10 seconds:** title and hero map reveal the spatial thesis.
2. **30 seconds:** supporting panels show method and result.
3. **2 minutes:** captions, data notes, and limitations convince the judge it is rigorous.

Recommended layout:

- Claim-title at top.
- One hero map occupying the largest visual space.
- 2–4 supporting maps/charts: method, temporal comparison, validation, or ranked result.
- Compact data/method panel.
- Minimal prose, strong captions.
- Visible source/citation panel.

### StoryMap route
A winning StoryMap should be a guided spatial argument, not a website dump.

Recommended sequence:

1. Hook: one map or image that shows the stakes.
2. Spatial question: one paragraph.
3. Data and method: concise, with workflow graphic.
4. Map sequence: each map answers one sub-question.
5. Result synthesis: quantified takeaway.
6. Limitation and implication: concise, credible close.

### Cartographic tactics
- Use a claim-based title: “Flood risk concentrates where recovery capacity is weakest,” not “Flood Map.”
- Use small multiples for time or comparison.
- Use inset maps for orientation.
- Use annotations sparingly to point at the decisive pattern.
- Avoid color ramps that imply false precision.
- Make legends legible from poster-viewing distance.
- Keep captions as micro-arguments.

## Narrative Strategy

### Poster narrative within 350 descriptive words
Suggested allocation:

| Component | Word target | Purpose |
|---|---:|---|
| Problem / question | 35–50 | Establish stakes and spatial question. |
| Data | 45–65 | Show complexity and relevance. |
| Method | 70–90 | Explain what GIS did. |
| Results | 80–110 | State quantified spatial finding. |
| Implication | 35–55 | Explain why it matters. |
| Limitation | 15–30 | Signal rigor without weakening the claim. |

Captions, labels, title, legends, and citations are excluded from the cap per the user-provided rules, but run a conservative audit anyway.

### StoryMap narrative alternative
Use scroll sections as argument steps:

- **Why this geography matters**
- **What data makes it measurable**
- **What GIS operation reveals**
- **What changed / who is affected / where risk concentrates**
- **What the result implies**

## Review Protocol

### Three-reviewer system
1. **GIS/method reviewer:** checks workflow, data, parameters, and validation.
2. **Cartography reviewer:** checks visual hierarchy, legend clarity, map readability, and medium fit.
3. **Naïve reader:** checks whether the spatial thesis is understood in 30 seconds.

### Review script
Ask each reviewer:

- What is the central spatial claim?
- What map or result convinced you?
- Where did you get confused?
- Which Fisher criterion is weakest?
- What one change would most improve competitiveness?

Score each draft using [scoring_rubric.md](scoring_rubric.md). Do not polish aesthetics until compliance, spatial necessity, data documentation, and analytical clarity pass.

## Red Flags

| Red flag | Why it hurts | Fix |
|---|---|---|
| GIS is only used to make a final map | Fails “Use of GIS in performing the project.” | Add a spatial operation central to the conclusion. |
| Topic is broad | Weak innovation; hard to judge. | Narrow by geography, group, hazard, period, or decision problem. |
| Data sources are undocumented | Directly violates data criterion. | Add data provenance table and preprocessing notes. |
| Method is a black box | Weak analytical execution. | Add workflow diagram, parameters, and validation/sensitivity check. |
| Too many maps | Dilutes visual communication. | Keep hero map + few supporting panels. |
| Technical method lacks interpretation | Judges may not see why it matters. | Tie every metric to a spatial implication. |
| Poster exceeds word cap or wrong size | Can cause rejection. | Run compliance QA before final visual polish. |
| StoryMap link is private or broken | Submission may fail. | Test in a non-editing browser before email submission. |
| Cartography is beautiful but unsupported | Design cannot replace data rigor. | Add sources, uncertainty, and method transparency. |

## Final QA

### Compliance QA
- [ ] Student eligibility confirmed.
- [ ] Registration submitted through Fisher page using HarvardKey.
- [ ] Registration confirmation saved.
- [ ] Poster route: PDF exported at 42” x 36”.
- [ ] Poster route: descriptive text <=350 words.
- [ ] StoryMap route: public/accessible URL tested.
- [ ] Submission email addressed to `jblossom@cga.harvard.edu`.
- [ ] Submission sent before Sunday, May 3, 2026 at 11:59 p.m.

### Competitiveness QA
- [ ] Central spatial claim visible in title/hero map.
- [ ] GIS method is indispensable.
- [ ] Data table documents source, resolution, temporal coverage, preprocessing, and limitations.
- [ ] Workflow is clear enough to reproduce conceptually.
- [ ] Result is quantified.
- [ ] At least one validation or sensitivity check is present.
- [ ] Visual hierarchy works from a distance.
- [ ] Captions state conclusions, not just labels.
- [ ] Lowest Fisher criterion score has been upgraded.

### Failure modes to actively prevent
Wrong poster size, non-PDF poster, over-word-limit descriptive text, missing registration, late submission, undocumented data, weak GIS role, unclear cartography, broken StoryMap URL, unsupported novelty claims.
