# SUBMISSION_GAP_ANALYSIS.md — AI Compute Accessibility Atlas vs. EIP + Fisher Playbook

> Scored comparison of the current StoryMap draft against the award playbook, with exact remaining work needed to reach submission quality.
>
> **Project:** AI Compute Accessibility Atlas  
> **Author:** Matthew Tan  
> **Artifact:** [StoryMap](https://storymaps.arcgis.com/stories/744a1c433d554cef8b3861d72836fdd2) (reviewed from 20-page print PDF)  
> **Cross-references:** Rubric from `AWARD_PLAYBOOK.md` Section 3. Winner patterns from `WINNER_MATRIX.md`. Originality packages from `NOVELTY_METHODS_MEMO.md`.

---

## 1. Current-Project Strengths

This is already a strong draft. Several elements match or exceed patterns seen in past winners:

| Strength | Evidence | Playbook Alignment |
|----------|----------|-------------------|
| **Exceptionally timely topic** | AI infrastructure geography is one of the most pressing tech-policy questions of 2025–2026. No past winner has touched this space. | Matches implicit priority #1 (timeliness). Judges praised timeliness in [EIP-2023-1] (Pakistan floods), [EIP-2021-1] (COVID). This topic is arguably *more* timely. |
| **Clear research question + short answer** | Page 2 states the question plainly and gives a quantitative short answer (657 km vs 237 km). This mirrors the hypothesis-to-conclusion structure judges praised in [FIS-2025-UG-1]. | Matches playbook template 4c. One of only a few student projects to do this so explicitly. |
| **Global scale with specificity** | 8,000-city frame is ambitious and gives the project analytical weight. It's not vague "global" — every city has a measurable distance value. | Exceeds typical scope. [EIP-2025-1] focused on one county; this covers the planet with a comparable indicator. |
| **Multiple analytical methods** | Distance measurement → descriptive histogram → weighted concentration → hot spot analysis (Getis-Ord Gi*) → spatial regression (2 model specs) → composite bundle index → case studies. This is a deep methods stack. | Matches implicit priority #3 (breadth of GIS spectrum). Judges praised [EIP-2025-1] for "much of the spectrum of GIS." This project hits even more methods. |
| **Statistical integration** | Two spatial model specifications with coefficient comparison. The project explicitly controls for city size and geography. | Matches implicit priority #6. Judges praised "robust statistical analysis" in [EIP-2025-1] and [FIS-2025-UG-1]. |
| **Intellectual honesty** | Repeatedly states "does not claim a definitive causal estimate," treats compute as "correlate and screening layer." This is mature epistemological positioning. | Rare in student work. Judges respect it — [FIS-2025-UG-1] was called "worthy of a scientific publication" partly for this quality. |
| **Four well-chosen case studies** | Singapore (confirms pattern), Seoul (exception — near compute, low AI), Ho Chi Minh City (beats pattern), Lagos (stacked disadvantage). This 2×2 typology is analytically elegant. | Matches playbook Map Kit M5 (case-study zoom). [FIS-2024-UG-1] won partly by drilling into specific locations. Having *four* strategic cases is stronger than most winners. |
| **Policy/screening tool** | 1,988 priority cities flagged. This transforms the atlas from description to actionable output. | Matches implicit priority #5 (policy relevance). [EIP-2024-1] won with "practical use to policy makers." |
| **Public-interest framing** | The narrative consistently addresses planners, innovation agencies, and public audiences, not just academics. | Matches the EIP criterion "potential impact" and the Fisher criterion "innovation and creativity of chosen topic." |

**Overall first impression:** This is already in the top tier of what I've seen in the winner corpus. The topic, analytical depth, and narrative maturity are competitive. The improvements below are about closing gaps that separate a *good* submission from one that makes judges say "professional level of quality from start to finish" ([EIP-2024-1]).

---

## 2. Rubric Scorecard

| Category | Weight | Score (1–5) | Rationale | What Would Raise It |
|----------|--------|-------------|-----------|-------------------|
| **Framing / Problem Choice** | 15% | **5** | Exceptionally timely, clearly geographic, specific audience named (planners, innovation agencies), quantified stakes (8,000 cities, 1,988 priority cities). This is as good as any winner in the corpus. | Already strong. Minor: the opening "AI does not happen on a blank map" is good but could be even punchier with a single striking statistic in the very first sentence. |
| **StoryMap Architecture** | 15% | **4** | Clear arc: hook → question/answer → methods → results → case studies → conclusion. However, the narrative is quite *text-heavy* for a StoryMap — many sections read like a report rather than a visual story. Some sections repeat the same point (e.g., the "compute is not destiny" refrain appears ~5 times). | Tighten prose by ~25%. Cut repeated framings. Use more sidecar blocks where text currently carries the weight. Add section headers that are more action-oriented (see specifics below). |
| **GIS / Cartography** | 25% | **3** | The maps are analytically sound but visually they appear as *static chart images* in the print PDF. It's unclear whether the live StoryMap has interactive web maps. The case-study maps (Singapore, Seoul, HCMC, Lagos regional context) are clean but basic — just point markers on a grey basemap. The "Local Ecosystem" scatter plots use lat/lon as axes, which is unconventional and may confuse readers. No visible legends on several maps. The color ramps (viridis-style) work but the maps lack cartographic polish compared to winners like [EIP-2024-1]. | **This is the biggest gap.** Add at least 1–2 embedded interactive web maps. Improve cartographic styling on case-study maps (add context layers, better basemaps). Fix or explain the Local Ecosystem charts. Add legends/annotations to every map. See detailed recommendations below. |
| **Evidence / Analysis** | 20% | **4** | Strong: multi-source data (AWS/Azure/GCP regions, OpenAlex, city population, infrastructure indicators), multiple methods, spatial diagnostics. Weak: no formal data sources table with provenance/dates/resolution. The composite "bundle index" components are not fully explained — what specific variables go into connectivity, institutional depth, local infrastructure? The spatial models mention "point estimates" and "stored summary JSON files" but don't show uncertainty intervals. | Add a data sources table. Specify bundle index components. Add confidence intervals or at least acknowledge their absence more prominently. Consider linking to code/data (open science). |
| **Originality** | 15% | **5** | This topic is entirely novel in the Harvard EIP/Fisher corpus. No past winner has mapped AI infrastructure geography. The combination of cloud-region distance + OpenAlex research overlay + composite bundle index + 4-city case typology is a unique analytical package. The project explicitly states its novelty ("treats cloud infrastructure as part of the geography of AI, not as invisible background plumbing"). | Already strong. The novelty is well-stated. Could be made even more visible with a dedicated callout box (template 4i). |
| **Packaging / Polish** | 10% | **3** | The print PDF reveals several polish issues: (1) Maps are visually plain — grey basemaps, minimal styling. (2) Some figure captions repeat the same text as the body prose verbatim. (3) The "Local Ecosystem" charts for case studies all use raw lat/lon coordinates as axes, which looks like a data artifact rather than a designed visualization. (4) No author bio or professional photo visible (required for EIP). (5) No sources/credits section visible. (6) Some markdown artifacts remain (**bold** markers visible in text on page 1). | Apply a custom theme. Add bio + photo. Add sources section. Fix duplicate captions. Restyle case-study charts. Remove markdown artifacts. |

### Weighted Score

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Framing | 15% | 5 | 0.75 |
| Architecture | 15% | 4 | 0.60 |
| GIS/Cartography | 25% | 3 | 0.75 |
| Evidence/Analysis | 20% | 4 | 0.80 |
| Originality | 15% | 5 | 0.75 |
| Packaging/Polish | 10% | 3 | 0.30 |
| **Total** | **100%** | | **3.95** |

**Assessment:** At 3.95, this is right at the competitive threshold (≥4.00). The framing and originality are exceptional — genuinely best-in-class. But the GIS/cartography and polish scores are dragging it below where it should be given the analytical strength. **Fixing the maps and polish could push this to 4.5+, which would be a very strong submission.**

---

## 3. Originality Score & Recommendation

**Originality score: 5/5** — This is the project's greatest strength. 

The topic (AI compute infrastructure geography) has no precedent in the EIP/Fisher winner corpus. The methodological chain (distance measurement → hot spot analysis → spatial regression → composite index → case-study typology) is sophisticated and hard to replicate casually.

**Recommendation:** The originality is already strong enough. Do *not* bolt on additional originality packages from `NOVELTY_METHODS_MEMO.md` — that would risk scope creep. Instead, make the existing originality more *visible* to judges by adding a callout box (template 4i) and ensuring the methods sidecar clearly names each Esri tool used.

---

## 4. Specific Gaps & Improvements

### GAP 1: Maps need significant cartographic upgrade (GIS/Cartography — highest priority)

**Current state:** The maps are analytically correct but visually underdeveloped. The case-study regional context maps show cloud regions as simple colored dots on grey basemaps with no context (country boundaries are faint, no city labels besides the focal city, no topographic context). The global maps use a viridis-style color ramp which is functional but not memorable.

**What winners do:** [EIP-2024-1] was praised for "engaging interactive maps." [FIS-2025-G-1] used a "strong mix of static and dynamic maps." [FIS-2022-G-1] earned praise for "effective cartographic techniques."

**Fix:**
- Add at least **2 embedded interactive web maps** to the live StoryMap — the global compute accessibility map (Figure 1) and the priority-city screening map (Figure 12) are the best candidates. Let readers click on a city to see its distance, bundle score, and AI works count.
- Upgrade the **4 case-study regional context maps**: add country borders, city labels for surrounding major cities, topographic/terrain basemap rather than plain grey, and cloud region labels.
- Add **clear legends** to every map — some maps in the PDF lack visible legends or have legends that are too small to read.
- Consider a **custom color scheme** that is consistent throughout — the current mix of viridis for global maps and different styling for case studies feels fragmented.

### GAP 2: "Local Ecosystem" scatter plots are confusing (GIS/Cartography)

**Current state:** The case-study "Local Ecosystem" charts (pages 12, 14, 16, 18) plot institutions on raw latitude/longitude axes. This means the chart is technically a map, but it looks like a scatter plot with axes labeled 103.6–104.1 (for Singapore). For a reader who doesn't realize these are coordinates, this is disorienting. For a reader who does, it's an unusual choice that doesn't clearly communicate what it's supposed to show.

**Fix:** Either:
- (a) Replace these with proper **local-scale maps** showing the city anchor, institutions, and cloud regions on a real basemap with streets/context, or
- (b) If keeping the scatter format, add axis labels "Longitude" / "Latitude" and overlay a light basemap or city boundary so readers immediately understand it's spatial.

### GAP 3: No data sources table or methods documentation (Evidence/Analysis)

**Current state:** The StoryMap mentions data sources in passing (AWS, Azure, Google Cloud regions; OpenAlex for AI works; city population data) but there is no structured table. The "How the atlas works" section (page 3) describes the approach in general terms but doesn't name specific Esri tools, software versions, or processing steps. The "Compute Opportunity Bundle Index" is introduced on page 7 but its components are not listed — what specific variables measure "connectivity, institutional depth, and local infrastructure context"?

**What winners do:** [EIP-2023-1] was praised for "relevant data with well documented sources." [FIS-2025-UG-1] linked to code and models.

**Fix:**
- Add a **data sources table** (template 4h) listing every dataset, its provider, date, and resolution.
- Name the **specific Esri tools** used: ArcGIS Pro, ArcGIS Online, which Spatial Statistics tools for hot spot analysis, etc. This is especially important for the EIP award, which requires demonstrating Esri technology use.
- Specify the **bundle index components** — list the exact variables and their weights/sources. The current description is too vague for judges evaluating "data complexity" and "analytical approach."
- Add **confidence intervals** or at least a note explaining why they're not shown for the spatial model coefficients (page 7 mentions "stored summary JSON files" and "the current pipeline stores point/SE means but not the uncertainty intervals needed for a full inferential comparison").

### GAP 4: Repetitive prose — tighten by ~25% (Architecture)

**Current state:** Several points are restated multiple times across the StoryMap:
- "Compute is not destiny" appears at least 5 times (pages 11, 18, 19, and variations throughout).
- The median distance comparison (657 km vs 237 km) appears on pages 2, 4 (and is paraphrased on pages 3, 5).
- The four-case-study typology is previewed on page 10, then each case restates the typology setup.
- Many figure captions repeat the body text verbatim (e.g., page 5: both the caption and the prose say "Hot spots and cold spots show that the relationship is spatially structured, not just anecdotal").

**What winners do:** Judges praise "concisely explained" ([FIS-2025-UG-1]) and "well organized" ([EIP-2023-1]). Repetition suggests the narrative isn't trusting the reader to follow.

**Fix:**
- State each key finding **once** in its main section, then cross-reference rather than restate.
- Make figure captions **additive** — they should note something the body text doesn't (data source, method detail, or interpretation nuance), not duplicate it.
- The "compute is not destiny" refrain can appear **twice** at most: once in the findings transition and once in the conclusion.
- Target cutting ~20-25% of the text — this will make the remaining prose feel more authoritative and the maps more prominent.

### GAP 5: Missing bio, credits, and sources section (Packaging — required for EIP)

**Current state:** The 20-page PDF has no author bio, professional photo, sources/credits section, or acknowledgments. The EIP submission requirements explicitly state: "Short bio and professional picture" and "Esri technology used."

**Fix:**
- Add an **opening bio block** with name, program (Harvard school), professional photo, and 2-sentence project description.
- Add a **closing section** with: data sources table, tools/software used (naming Esri products), acknowledgments, and contact information.
- If code/data can be shared, add an **open science sidebar** (template 4j) — this is rare and was explicitly praised when [FIS-2025-UG-1] did it.

### GAP 6: Markdown rendering artifacts (Polish)

**Current state:** Page 1 of the PDF shows `**8,000 cities**` with asterisks visible, suggesting the StoryMap may have raw markdown that isn't rendering properly in the live version. Page 2 shows `**Short answer:**` similarly.

**Fix:** Check the live StoryMap for any raw markdown that should be formatted as bold/italic. The print-to-PDF process may introduce artifacts, but if they appear in the live version, they hurt the professional impression.

### GAP 7: No explicit Esri technology callout (EIP-specific)

**Current state:** The project clearly uses ArcGIS (Esri basemaps visible, "Powered by Esri" in map footers, hot spot analysis likely run in ArcGIS Pro). But the StoryMap never explicitly names the Esri tools used. The EIP criteria include "Implementation" and the submission requirements state the project "must use Esri technology" with maps and Esri technology named.

**Fix:** Add a brief **"Tools used"** note in the methods section: "This analysis was conducted using ArcGIS Pro [version] for spatial statistics (Hot Spot Analysis, Spatial Regression) and ArcGIS Online for interactive web mapping and StoryMap publication." Name specific toolbox references — this signals to judges that you know the platform.

### GAP 8: No interactive maps visible in the print version (GIS/Cartography)

**Current state:** Every map in the 20-page PDF appears to be a static image. It's possible the live StoryMap has interactive maps that don't render in print, but the PDF is the best evidence available.

**What winners do:** [EIP-2024-1] was praised for "engaging interactive maps." The Esri StoryMaps competition guide explicitly recommends embedding dashboards, web maps, and apps.

**Fix:** The two highest-value interactive maps to add:
1. **Global compute accessibility map** (the 8,000-city view) — let users click a city to see its name, population, distance to nearest cloud region, number of AI works, and bundle score.
2. **Priority-city screening map** — let users explore which cities are flagged and why.

If these already exist in the live StoryMap, great — but they should be prominent and tested in incognito + mobile.

---

## 5. Prioritized Remaining Tasks

### Must-Do (submission depends on these)

- [ ] **Add author bio + professional photo** at the top of the StoryMap (EIP requirement).
- [ ] **Add a data sources & tools section** at the end: data table (template 4h) + explicit Esri tool names.
- [ ] **Embed at least 2 interactive web maps** (global accessibility + priority cities). Test in incognito browser + mobile.
- [ ] **Specify the bundle index components** — list the exact variables, weights, and data sources for the Compute Opportunity Bundle Index.
- [ ] **Fix or replace the "Local Ecosystem" charts** — either convert to real local-scale maps with basemap context, or add axis labels and a basemap underlay.
- [ ] **Cut repetitive prose** by ~25%: "compute is not destiny" to max 2 occurrences, median stats stated once, figure captions made additive rather than duplicative.
- [ ] **Add legends and annotations** to every map — several maps currently lack readable legends.
- [ ] **Fix markdown rendering artifacts** (check live StoryMap for raw `**bold**` markers).
- [ ] **Register for EIP** if not already done — the deadline page says March 15, 2026 (today).

### Strong Upgrades (materially improve competitiveness)

- [ ] **Apply a custom visual theme** — choose a consistent color palette that ties maps, charts, and text styling together.
- [ ] **Add a novelty callout box** (template 4i): "What's new here: This is the first global atlas to treat cloud compute infrastructure as a measurable layer of AI geography, covering 8,000 cities across three hyperscaler networks."
- [ ] **Upgrade case-study regional maps** — richer basemaps, surrounding city labels, country borders, topographic context.
- [ ] **Add confidence intervals** to the model coefficient chart (page 7) or add a methods note explaining why they're omitted and what the SE values are.
- [ ] **Add one non-map visual** for variety — a summary infographic, a methodology workflow diagram, or a "key numbers" callout panel.
- [ ] **Add open science links** — if code/data pipeline can be shared via GitHub or Harvard Dataverse, link it prominently (template 4j). This was the single rarest and most praised feature in the winner corpus.
- [ ] **Submit to Fisher Prize too** (deadline May 3, 2026) — this project is competitive for both awards and the Fisher poster format could showcase the global map + 4-case typology powerfully.

### Optional Polish (marginal gains)

- [ ] **Peer review** — have a non-GIS friend read the StoryMap and flag where they lose the thread or where maps are unclear.
- [ ] **Test on mobile devices** — StoryMaps render differently on phones. Ensure maps are legible at mobile width.
- [ ] **Add a "how to read this map" annotation** on the first global map for accessibility.
- [ ] **Shorten the title** — "AI Compute Accessibility Atlas" is good but long. Consider whether the subtitle "Where cloud compute is close, where it is far, and why that matters for cities" could be shortened for impact.

---

## 6. Summary Assessment

**Bottom line:** This is a genuinely excellent project with a novel question, strong analysis, and mature intellectual framing. It is *already competitive* with past winners on topic, originality, and analytical depth. The main risk is that the GIS/cartography and polish dimensions — which carry 35% of the rubric weight — are underdeveloped relative to the analytical content.

The fix is not more analysis. It's better maps, tighter prose, and submission-format compliance (bio, sources, Esri tool names). These are execution-level improvements that don't require new data or methods — just time and attention.

If the must-do items above are completed, this project should score in the 4.3–4.7 range, which would place it among the strongest submissions in recent years. The topic alone — AI infrastructure geography at global scale — is something no past winner has attempted, and judges have consistently rewarded timeliness and originality at exactly this level.
