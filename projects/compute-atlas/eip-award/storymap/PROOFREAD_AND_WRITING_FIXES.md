# Proofread & Writing Fixes — Page-by-Page Edit List

> Every typo, grammar issue, and prose tightening fix identified in the March 15 PDF.
> Organized by page number. Make these changes in the live StoryMap editor.
> 
> Legend:
> - **TYPO** = spelling/punctuation error
> - **GRAMMAR** = grammatical fix
> - **CUT** = remove this text (redundant or filler)
> - **REWRITE** = replace with suggested text
> - **ADD** = insert new text

---

## Page 1 — Title / Cover

No issues. Title, subtitle, date, and author name are clean.

---

## Page 2 — Bio + Introduction (paragraphs 1–2)

### Fix 1 — TYPO (p.3 in the Introduction, but visible in the text flow from p.2)
**Find:** `Modern day AI systems`  
**Replace with:** `Modern-day AI systems`  
**Why:** "Modern-day" is a compound adjective before a noun and needs a hyphen.

### Fix 2 — GRAMMAR
**Find:** `In particular, the main players in the AI industry, Amazon, Microsoft and Google, operate data centers under Amazon Web Services (AWS), Azure and Google Cloud respectively.`  
**Replace with:** `The three dominant hyperscalers — Amazon Web Services (AWS), Microsoft Azure, and Google Cloud — operate data centers clustered in specific regions, concentrated primarily in North America, Europe, and parts of East Asia.`  
**Why:** The original sentence is awkward: it names the companies, then renames them as their cloud brands, and the sentence runs long. The rewrite consolidates and introduces all three brand names in one pass, which also lets you cut the next sentence ("These data centers are found in clusters in regions, concentrated in specific locations, primarily in North America, Europe, and parts of East Asia") since that information is now folded in.

### Fix 3 — CUT (if you adopt Fix 2)
**Find:** `These data centers are found in clusters in regions, concentrated in specific locations, primarily in North America, Europe, and parts of East Asia. This creates some geospatial meaning to the accessibility to AI, as the distance to these data centers affects network latency, data transfer costs, and the practical viability of running AI workloads at scale.`  
**Replace with:** `This geographic concentration gives the accessibility of AI a spatial dimension: distance to these regions affects network latency, data transfer costs, and the practical viability of running AI workloads at scale.`  
**Why:** "Creates some geospatial meaning to the accessibility to AI" is clunky phrasing. The rewrite is cleaner and shorter.

---

## Page 3 — Introduction (paragraphs 3–4) + Research Question

### Fix 4 — GRAMMAR
**Find:** `how it effects human populations`  
**(Note: this phrase appears in the CONTINUATION_WORK as a judge quote — check whether it's in your actual StoryMap text. If the word "effects" appears as a verb anywhere in your text, fix it.)**  
**Replace with:** `how it affects human populations`  
**Why:** "Affects" is the verb; "effects" is typically the noun.

### Fix 5 — REWRITE (minor polish)
**Find:** `There is a lack of attention to the physical infrastructure layer, where compute capacity is actually located, how far cities sit from it, and whether that distance corresponds with observable differences in AI activity.`  
**Replace with:** `Far less attention has gone to the physical infrastructure layer: where compute capacity is actually located, how far cities sit from it, and whether that distance corresponds with observable differences in AI activity.`  
**Why:** "There is a lack of attention to" is wordy. Active voice is stronger.

### Fix 6 — REWRITE (minor polish)
**Find:** `There is, to date, no systematic global mapping of how cloud compute proximity relates to the geographic distribution of AI research.`  
**Replace with:** `To date, no systematic global mapping connects cloud compute proximity to the geographic distribution of AI research.`  
**Why:** Eliminates another "There is" construction. More direct.

---

## Page 4 — Hero Map + Transition + "How the atlas works" start

### Fix 7 — TYPO
**Find:** `Beforee we begin, we first carry out someexploratory data analysis to understand the context.`  
**Replace with:** `Before we begin, we first carry out some exploratory data analysis to understand the context.`  
**Why:** Two typos: "Beforee" (extra e) and "someexploratory" (missing space).

### Fix 8 — REWRITE (stronger transition)
The sentence in Fix 7 is also a weak transition even after fixing the typos. Consider replacing the entire sentence:  
**Find:** `Before we begin, we first carry out some exploratory data analysis to understand the context.`  
**Replace with:** *Delete entirely.*  
**Why:** The next section header "How the atlas works" already transitions the reader. This sentence is filler — it says "before we begin, we begin." The paragraph before it ("The sections that follow describe how this atlas was constructed...") already serves as the structural preview.

---

## Page 5 — "How the atlas works" (Stages 1–3) + AI Overlay Description

### Fix 9 — GRAMMAR
**Find:** `The purpose of this is to allow for comparability across thousands of cities using a consistent methodology.`  
**Replace with:** `This allows direct comparison across thousands of cities using a consistent methodology.`  
**Why:** "The purpose of this is to allow for" is wordy. Just say what it does.

### Fix 10 — REWRITE (caption, p.5)
**Find:** `328 matched AI cities from the OpenAlex scholarly record, sized by recent AI works and colored by distance to the nearest cloud region.`  
**Replace with:** `328 AI-linked cities matched from the OpenAlex scholarly record (2020–2025, by institutional affiliation). Marker size encodes recent AI works; color encodes distance to the nearest major cloud region. Data: OpenAlex, Natural Earth, hyperscaler documentation.`  
**Why:** The current caption duplicates the body text. Adding the date range, matching method, and data sources makes it additive. Also specifies "marker size encodes" rather than the ambiguous "sized by."

### Fix 11 — GRAMMAR
**Find:** `while just 44 percent of all large cities in the 8,000-city frame.`  
**Replace with:** `compared to just 44 percent of all large cities in the 8,000-city frame.`  
**Why:** The sentence as written is a fragment. "While" needs a parallel clause, but there isn't one. "Compared to" completes the comparison.

---

## Page 6 — Finding 1

### Fix 12 — TYPO
**Find:** `The separation is immediate obvious.`  
**Replace with:** `The separation is immediately obvious.`  
**Why:** Missing -ly adverb.

### Fix 13 — REWRITE (tighten)
**Find:** `A two-sample Kolmogorov-Smirnov test was run, which measures the maximum vertical distance between two cumulative distribution functions. The results were that D = 0.30 (p < 0.001), confirming that the AI-linked and all-city distance distributions are drawn from different underlying populations.`  
**Replace with:** `A two-sample Kolmogorov-Smirnov test — which measures the maximum vertical distance between two cumulative distribution functions — returns D = 0.30 (p < 0.001), confirming that the two distributions are drawn from different underlying populations.`  
**Why:** "Was run" + "The results were that" is passive and wordy. The em-dash parenthetical is more compact.

### Fix 14 — REWRITE (tighten)
**Find:** `A one-sided Mann-Whitney U test was also implemented. This tests whether one distribution is systematically shifted below the other. The results confirmed that AI-linked cities are significantly closer to cloud regions than the broader city population (U = 786,844, p < 0.001).`  
**Replace with:** `A one-sided Mann-Whitney U test confirms that AI-linked cities are systematically closer to cloud regions than the broader city population (U = 786,844, p < 0.001).`  
**Why:** Three sentences doing the work of one. The reader doesn't need "was also implemented" or a separate sentence explaining what the test does — the result speaks for itself.

### Fix 15 — GRAMMAR
**Find:** `since by Cohen's d came out to be 0.74`  
**Replace with:** `with Cohen's d = 0.74`  
**Why:** "Since by Cohen's d came out to be" is garbled syntax. Clean it up.

---

## Page 7 — Finding 1 (continued) + Finding 2

### Fix 16 — REWRITE (Finding 1 closing, tighten)
**Find:** `Cities producing visible AI research do not simply sit somewhat closer to compute infrastructure on average. They concentrate inside the compute corridors, and are largely absent from the zones farthest from cloud regions.`  
**This is good.** Keep as-is — it's the strongest closing statement for Finding 1.

### Fix 17 — GRAMMAR (Finding 2 caption)
**Find:** `the teal cumulative line tracks total concentration.`  
**Replace with:** `the teal cumulative line tracks cumulative concentration.`  
**Why:** Minor — "total concentration" is slightly ambiguous; "cumulative concentration" matches the visual (a cumulative share line).

---

## Page 8 — Finding 2 (continued) + Finding 3 start

### Fix 18 — REWRITE (tighten the Spearman paragraph)
**Find:** `It is important to note what this finding does and does not show. It demonstrates that the cities with the highest research volume are disproportionately located near cloud infrastructure. A Spearman rank correlation between distance and research output within the AI-linked sample alone is weakly negative (correlation = −0.05, p = 0.40), indicating that once a city is already in the AI-producing set, additional proximity does not strongly predict higher output. The sharper concentration in the weighted view is driven primarily by the fact that the largest AI-producing hubs, cities with hundreds of matched publications, tend to coincide with the world's densest compute corridors, instead of by a smooth gradient within the AI-linked sample.`  
**Replace with:** `An important distinction: the Spearman rank correlation between distance and research output *within* the AI-linked sample alone is weakly negative (ρ = −0.05, p = 0.40), meaning that once a city is already in the AI-producing set, additional proximity does not strongly predict higher output. The sharper concentration in the weighted view is driven by the fact that the largest AI-producing hubs tend to coincide with the world's densest compute corridors, rather than by a smooth gradient within the sample.`  
**Why:** The opening two sentences ("It is important to note what this finding does and does not show. It demonstrates that...") are throat-clearing. Jump straight to the distinction. Also: use ρ (rho) instead of "correlation" for Spearman — it's the standard notation and you use proper notation elsewhere. Cut "instead of by" → "rather than by" for cleaner syntax. Cut "cities with hundreds of matched publications" — already implied by "largest AI-producing hubs."

---

## Page 8–9 — Finding 3

### Fix 19 — GRAMMAR
**Find:** `We chose these methods for several reason.`  
**Replace with:** `We chose these methods for several reasons.`  
**Why:** Missing plural "s" on "reason."

### Fix 20 — GRAMMAR
**Find:** `Spatial autocorrelation diagnostics are not commonly applied to AI infrastructure or research-output data — most studies in this domain rely on descriptive mapping, regression, or network analysis alone.`  
**Replace with:** `Spatial autocorrelation diagnostics are rarely applied to AI infrastructure or research-output data — most studies in this domain rely on descriptive mapping, regression, or network analysis alone.`  
**Why:** "Not commonly applied" → "rarely applied" is tighter. Minor.

### Fix 21 — CUT (p.9, "Why these methods" paragraph — tighten)
**Find:** `Third, both methods are implemented in the ArcGIS Spatial Statistics toolbox, making them reproducible within the Esri ecosystem that this project is built on.`  
**Replace with:** `Third, both are implemented in the ArcGIS Pro Spatial Statistics toolbox, ensuring reproducibility within the Esri ecosystem.`  
**Why:** Shorter, and specifies "ArcGIS Pro" (not just "ArcGIS") which is more precise for the EIP judges.

### Fix 22 — GRAMMAR
**Find:** `Alternative approaches such as LISA or kernel density estimation were considered but Gi* was selected for its more interpretable hot/cold classification for a public-interest audience.`  
**Replace with:** `Alternative approaches such as LISA and kernel density estimation were considered, but Gi* was selected for its more interpretable hot/cold classification for a public-interest audience.`  
**Why:** Missing comma before "but" in a compound sentence.

---

## Page 9–10 — Finding 4

### Fix 23 — REWRITE (tighten opening)
**Find:** `Findings 1–3 show that AI-linked cities are disproportionately close to cloud infrastructure and that this pattern is spatially structured. The natural follow-up question is: which cities are on the wrong side of both gaps, i.e. far from compute and absent from the AI research overlay?`  
**Replace with:** `The natural follow-up: which cities are on the wrong side of both gaps — far from compute and absent from the AI research overlay?`  
**Why:** The first sentence restates what the reader just finished reading. Cut it.

### Fix 24 — GRAMMAR
**Find:** `i.e. far from compute`  
**Replace with:** `i.e., far from compute`  
**Why:** Standard American English uses a comma after "i.e." (Though if you adopt Fix 23, this becomes moot since we replaced i.e. with an em dash.)

---

## Page 11 — Finding 4 (continued, map) + Finding 5 start

### Fix 25 — REWRITE (Finding 5 opening — cut restated findings)
**Find:** `Findings 1–4 show that AI-linked cities are closer to cloud infrastructure, that the concentration sharpens with research volume, that the pattern is spatially structured, and that nearly 2,000 cities sit on the wrong side of both gaps. But none of these findings account for the possibility that the distance-activity pattern is driven entirely by city size or broad continental geography.`  
**Replace with:** `None of the preceding findings account for confounding. A large city is more likely to host AI research *and* more likely to attract a nearby cloud region — population could drive both. Similarly, cities in Europe and North America may score high on both dimensions simply because of continental position, not because of a direct distance-activity link.`  
**Why:** The first sentence restates all four prior findings in a single clause — the reader just read them. Jump straight to the new analytical point (confounding). The second sentence from the original ("Logically, a large city...") is kept but tightened.

### Fix 26 — CUT (p.11, redundant with Fix 25)
**Find:** `Logically, a large city is more likely to host AI research and more likely to attract a nearby cloud region. This means population could be a confounding variable in this natural experiment. Similarly, cities in Europe and North America may score high on both dimensions simply because of their continental position, not because of a direct distance-activity link.`  
**Action:** If you adopt Fix 25, delete this paragraph since its content is absorbed into the rewrite above.

---

## Page 12 — Finding 5 (continued)

### Fix 27 — TYPO
**Find:** `The notabele feature across both models`  
**Replace with:** `The notable feature across both models`  
**Why:** "notabele" is misspelled.

### Fix 28 — TYPO
**Find:** `Intsead, these models confirm`  
**Replace with:** `Instead, these models confirm`  
**Why:** "Intsead" is misspelled.

### Fix 29 — REWRITE (tighten the caveat paragraph)
**Find:** `This is why the atlas treats compute accessibility as a meaningful spatial correlate of observed AI activity, rather than as a proven causal mechanism. The project does not claim that relocating a city closer to a cloud region would mechanically increase its AI research output. It claims that distance to compute infrastructure is one observable dimension of a broader geographic structure that corresponds with where AI activity is — and is not — currently concentrated.`  
**Replace with:** `This is why the atlas treats compute accessibility as a meaningful spatial correlate of observed AI activity, not a proven causal mechanism. It does not claim that relocating a city closer to a cloud region would mechanically increase its research output. Distance to compute infrastructure is one observable dimension of a broader geographic structure that corresponds with where AI activity is — and is not — currently concentrated.`  
**Why:** Minor tightening. "rather than as" → "not" is cleaner. "The project" → "It" avoids repetition. The third sentence drops "It claims that" — more assertive without it.

---

## Page 13 — Bundle Index

### Fix 30 — GRAMMAR
**Find:** `Western Europe and the US Northeast remain strong have strong compute`  
**Replace with:** `Western Europe and the US Northeast remain strong on compute`  
**Why:** "remain strong have strong compute" is a garbled duplicate. Looks like a failed edit — two versions of the sentence merged. Pick one.

### Fix 31 — GRAMMAR (bullet list formatting)
The five bundle components are presented as a bulleted list but the grammar is inconsistent. Here's a clean version for all five:

**Current (messy):**
> - Proximity to the nearest cloud region (40%): the core access measure and the atlas's primary variable.
> - Provider diversity represents the distinct hyperscalers reachable within threshold distance (15%): captures whether a city depends on a single provider or has competitive options.
> - Redundancy is represented by the total cloud regions within reach regardless of provider (15%): measures resilience and capacity depth.
> - Urban scale or city population (15%): proxies for market depth, labor availability, and demand concentration.
> - Institutional depth or presence of top-ranked AI research institutions from the OpenAlex overlay (15%): captures whether the local knowledge ecosystem supports AI activity.

**Replace with (parallel grammar):**
> - **Proximity to nearest cloud region (40%):** the core access measure and the atlas's primary variable.
> - **Provider diversity within threshold distance (15%):** the number of distinct hyperscalers reachable, capturing whether a city depends on a single provider or has competitive options.
> - **Redundancy — total cloud regions within reach (15%):** measures resilience and capacity depth regardless of provider.
> - **Urban scale — city population (15%):** proxies for market depth, labor availability, and demand concentration.
> - **Institutional depth — top AI research institutions from the OpenAlex overlay (15%):** captures whether the local knowledge ecosystem supports AI activity.

**Why:** The current list mixes grammatical structures — some items start with the component name, others start with a description ("Provider diversity represents..."). Making all five start with the bolded component name + weight, followed by a colon and description, creates parallel structure that's easier to scan.

---

## Page 14 — Bundle scatter plot text

### Fix 32 — REWRITE (minor, avoid "insightful")
**Find:** `But the most insightful zone is the middle`  
**Replace with:** `But the most revealing zone is the middle`  
**Why:** "Insightful" is slightly informal / self-congratulatory for analytical prose. "Revealing" is more neutral.

---

## Page 15 — Bundle bar chart + transition to case studies

No typos. Text is clean here.

---

## Page 16 — "Four cities that explain the pattern" intro

### Fix 33 — CUT (major — restated findings paragraph)
**Find:** `The atlas has established three things statistically. First, AI-linked cities occupy a fundamentally different part of the compute-access landscape than the broader city system — they are closer, and the difference is not an artifact of sample size (Finding 1). Second, that concentration sharpens when weighted by research volume: the highest-output cities sit disproportionately inside the densest compute corridors (Finding 2). Third, the pattern is spatially structured — not randomly scattered — with identifiable hot spots in East and Southeast Asia and cold spots across the Americas and peripheral Europe (Finding 3). A spatial regression confirms the relationship survives controls for city size and broad geography (Finding 5), and a priority screening layer identifies nearly 2,000 cities on the wrong side of both gaps (Finding 4).`  
**Replace with:** *Delete this entire paragraph.*  
**Why:** This paragraph re-summarizes all five findings the reader has just finished reading. It's a full paragraph of pure restatement. The next paragraph ("But statistical patterns describe populations, not places...") is a much stronger transition into the case studies and should open this section instead.

### Fix 34 — REWRITE (streamline the second transition paragraph)
**Find:** `But statistical patterns describe populations, not places. A Moran's I of 0.066 tells us that spatial clustering exists; it does not tell us what clustering looks like inside any particular city. A negative distance coefficient tells us the direction of the relationship; it does not explain why some cities beat the pattern while others conform to it. The bundle index begins to answer that question — it shows where compute access is reinforced or undermined by surrounding infrastructure — but even a composite score is a number, not a narrative. To understand how the atlas's global patterns actually play out, the analysis needs to move from indices to places.`  
**Replace with:** `Statistical patterns describe populations, not places. A Moran's I of 0.066 tells us that spatial clustering exists; it does not tell us what it looks like inside a particular city. The bundle index shows where compute access is reinforced or undermined by surrounding infrastructure — but even a composite score is a number, not a narrative. To understand how these patterns actually play out, the analysis moves from indices to places.`  
**Why:** Cut two sentences that restate the same point in parallel ("A negative distance coefficient tells us..." adds nothing after the Moran's I example already made the point). "The analysis needs to move" → "the analysis moves" is more assertive.

### Fix 35 — GRAMMAR
**Find:** `Ho Chi Minh Cit: farther from compute, high AI activity.`  
**Replace with:** `Ho Chi Minh City: farther from compute, high AI activity.`  
**Why:** Missing "y" in "City."

---

## Page 17 — Singapore case study

### Fix 36 — TYPO
**Find:** `OpenAlex AI works: 1,07`  
**Replace with:** `OpenAlex AI works: 1,077` (or whatever the correct number is — check your data)  
**Why:** Truncated number. Missing final digit(s).

---

## Page 18 — Singapore (continued) + Dublin header

### Fix 37 — GRAMMAR
**Find:** `The result is not just proximity to compute, but a broader system in which multiple enabling layers reinforce one another by design`  
**Replace with:** `The result is not just proximity to compute, but a broader system in which multiple enabling layers reinforce one another by design.`  
**Why:** Missing period at end of sentence.

### Fix 38 — CUT (minor — SGIX mentioned twice)
**Find (p.18, Singapore section):** `SGIX, one of Asia's largest open and neutral internet exchanges, adds a network layer that connects Singapore into broader regional and global routing infrastructure.`  
And later: `SGIX, one of Asia's largest open and neutral internet exchanges, adds the network layer [11].`  
**Action:** The SGIX description appears twice — once in the regional context paragraph and once in the local-scale paragraph. Delete the first occurrence (keep the one with the citation [11]).

---

## Page 19 — Dublin case study

### Fix 39 — GRAMMAR
**Find:** `Where Singapore converts infrastructure density into research output at every level, Dublin's cloud footprint outpaces its scholarly footprint.`  
**This is good.** Keep as-is — it's one of the strongest sentences in the case studies.

No other issues on this page.

---

## Page 20 — Ho Chi Minh City case study

### Fix 40 — GRAMMAR
**Find:** `VinAI, one of the country's flagship AI firms, places nearly 200 researchers and engineers across Hanoi and Ho Chi Minh City, reporting 88 top-tier publications — including papers at CVPR, NeurIPS, ICML, and ICLR — in its first three years [22, 23].`  
**This is good.** Keep as-is. Strong sentence.

No typos on this page.

---

## Page 21 — Lagos case study

No typos on the Lagos page. Text is clean.

---

## Page 22 — Conclusion

### Fix 41 — TYPO
**Find:** `Compute is not a source of predestintion`  
**Replace with:** `Compute is not a source of predestination`  
**Why:** "predestintion" is misspelled.

### Fix 42 — TYPO
**Find:** `and explainable on in a geospatial context.`  
**Replace with:** `and explainable in a geospatial context.`  
**Why:** Stray "on" — delete it.

### Fix 43 — CUT (major — duplicate "strongest contribution" sentence)
**Find (first occurrence):** `The strongest contribution of this project is not that it proves a universal causal effect of cloud-region placement. Rather, it unveils the hidden infrastructure layer of AI opportunity, making it visible, measurable, and explainable in a geospatial context.`  
**Find (second occurrence, 2 paragraphs later):** `The strongest contribution of this project is that it makes the infrastructure layer of AI opportunity visible, measurable, and geographically explicit across every region of the world.`  
**Action:** Delete the first occurrence entirely. Keep and strengthen the second. The second is the closing sentence and should land as the final statement.

### Fix 44 — REWRITE (conclusion structure)
The conclusion currently has four paragraphs. After applying Fix 43, the revised structure should be:

**Paragraph 1** (case study summary — keep, it's tight):
> Singapore, Dublin, Ho Chi Minh City, and Lagos each test the atlas against the complexity of a real urban system. [rest of paragraph as-is, with "predestination" typo fixed]

**Paragraph 2** (policy value — keep, tighten slightly):
> For planners, innovation agencies, and international development organizations, the atlas offers a concrete starting point. The priority-city screening layer identifies where infrastructure investment in cloud compute could address the starkest mismatches between urban demand and current supply. The bundle index identifies where proximity already exists but surrounding conditions have not yet caught up.

**Paragraph 3** (closing — merge and strengthen):
> Compute is not predestination, but it is not irrelevant either. The strongest contribution of this project is that it makes the infrastructure layer of AI opportunity visible, measurable, and geographically explicit — across every region of the world.

This gives you three paragraphs instead of four, with a strong final sentence.

---

## Pages 23–25 — Sources + Bibliography

### Fix 45 — GRAMMAR
**Find:** `This project draws on four primary data sources, processed and analyzed using ArcGIS Pro, ArcGIS Online, and Python`  
**Replace with:** `This project draws on four primary data sources, processed and analyzed using ArcGIS Pro, ArcGIS Online, and Python.`  
**Why:** Missing period at end of sentence.

### Fix 46 — ADD (Tools & Software section)
The current Sources section lists data sources but does not list the specific Esri tools used. Add after the data sources paragraph:

> **Tools & Software**
> 
> ArcGIS Pro: Spatial Autocorrelation (Global Moran's I) and Hot Spot Analysis (Getis-Ord Gi*) from the Spatial Statistics toolbox; data projection and spatial joins.
> 
> ArcGIS Online: Interactive web map authoring, hosted feature layers, Create Buffers analysis tool, and StoryMap publication.
> 
> Python: GeoPy (geodesic distance calculation), PySAL and SciPy (spatial weights and autocorrelation validation), GPyTorch and PyMC (spatial regression models), Pandas and NumPy (data processing), Matplotlib (figure generation).

**Why:** EIP judges specifically score "Implementation" and look for named Esri tools. The current sources section mentions ArcGIS Pro and ArcGIS Online in passing but doesn't name specific toolbox tools. This is a 2-minute addition that directly addresses the EIP criterion.

### Fix 47 — ADD (education limitation note)
In the Sources section, after the data sources list, add:

> **Scope note:** The institutional depth component of the bundle index captures research-active institutions from the OpenAlex record but does not directly measure broader educational infrastructure such as tertiary enrollment rates or STEM graduate pipelines. The case studies illustrate how this broader educational context shapes each city's AI trajectory beyond what the index alone captures.

**Why:** Your readers flagged education as a factor. This note acknowledges the limitation transparently without requiring new analysis. It shows intellectual honesty — the quality judges associate with publication-level work.

---

## Summary: All Typos at a Glance

| # | Location | Error | Fix |
|---|----------|-------|-----|
| 1 | p.2 | `Modern day AI systems` | `Modern-day AI systems` |
| 2 | p.4 | `Beforee we begin` | `Before we begin` (or delete sentence) |
| 3 | p.4 | `someexploratory` | `some exploratory` (or delete sentence) |
| 4 | p.5 | `while just 44 percent` (fragment) | `compared to just 44 percent` |
| 5 | p.6 | `immediate obvious` | `immediately obvious` |
| 6 | p.6 | `since by Cohen's d came out to be 0.74` | `with Cohen's d = 0.74` |
| 7 | p.9 | `for several reason` | `for several reasons` |
| 8 | p.12 | `notabele feature` | `notable feature` |
| 9 | p.12 | `Intsead, these models` | `Instead, these models` |
| 10 | p.13 | `remain strong have strong compute` | `remain strong on compute` |
| 11 | p.16 | `Ho Chi Minh Cit:` | `Ho Chi Minh City:` |
| 12 | p.17 | `AI works: 1,07` | `AI works: 1,077` (verify number) |
| 13 | p.18 | Missing period after `by design` | Add `.` |
| 14 | p.22 | `predestintion` | `predestination` |
| 15 | p.22 | `explainable on in` | `explainable in` |
| 16 | p.23 | Missing period after `Python` | Add `.` |

---

## Summary: Major Prose Cuts

These are the biggest tightening wins — paragraphs that restate earlier material:

| # | Location | What to Cut | Words Saved |
|---|----------|-------------|-------------|
| A | p.4 | "Before we begin..." filler sentence | ~20 |
| B | p.11 | Finding 5 opening restating Findings 1-4 | ~65 |
| C | p.16 | Full paragraph restating all 5 findings before case studies | ~110 |
| D | p.16-17 | Two transition sentences in case study intro (see Fix 34) | ~50 |
| E | p.18 | First SGIX mention (duplicate) | ~25 |
| F | p.22 | First "strongest contribution" sentence (duplicate of closing) | ~35 |
| **Total** | | | **~305 words** |

This represents roughly a 5% cut across a ~6,000-word document — enough to noticeably tighten the prose without losing any content.

---

## Summary: Key Additions (non-map)

| # | Location | What to Add | Effort |
|---|----------|-------------|--------|
| 1 | Sources section | Tools & Software paragraph naming specific Esri tools | 5 min |
| 2 | Sources section | Education/scope limitation note | 5 min |
| 3 | Bundle section (p.13) | Parallel-grammar rewrite of 5 component bullets | 10 min |
