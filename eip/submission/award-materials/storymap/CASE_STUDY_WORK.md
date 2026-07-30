# CASE_STUDY_WORK.md — Analysis Overhaul for Four City Cases

> **Cities:** Singapore, Dublin (replacing Seoul), Ho Chi Minh City, Lagos
> **Goal:** Replace thin, repetitive case studies with analytically grounded sections that convincingly explain why each city conforms to, departs from, or breaks the atlas pattern.

---

## PART 1: Weaknesses of the Existing Analysis

### 1.1 — The maps are spatially empty

**Problem:** Each case study currently has two figures — a "Regional Context" map and a "Local Ecosystem" chart. The regional context maps show the focal city, cloud region points, and dashed distance circles on a blank grey basemap. No country borders, no neighboring cities, no terrain, no transport links, no undersea cable routes, no data center clusters. They look identical in structure across all four cities — the only difference is which part of the world is centered. A judge sees four versions of the same grey map with colored dots.

**What winners do:** [FIS-2024-UG-1] (Finding Anfal) used layered archival maps, satellite imagery, and historical overlays to show the same geography at multiple time points. [FIS-2025-G-1] (Cool Walking Routes) mapped every street in Boston with thermal data. The case study maps need to carry analytical weight, not just show location.

**Fix:** Each regional context map must include at minimum:
- Country borders with labels
- Neighboring major cities (labeled, sized by population)
- Cloud region symbols labeled with provider name AND region code (e.g., "AWS ap-southeast-1")
- Submarine cable landing points or internet exchange points (IXPs) where available — these are the physical connectivity layer the atlas claims matters
- A richer basemap (terrain or political, not blank grey)

### 1.2 — The "Local Ecosystem" charts were confusing and may have been removed

**Problem:** The earlier version plotted institutions on raw latitude/longitude axes — technically a map but visually a scatter plot with axes labeled "103.6–104.1." The gap analysis flagged this. The current PDF doesn't clearly show whether these were fixed or removed, but either way the case studies lack a second analytical figure.

**Fix:** Replace with one of:
- (a) A proper local-scale map on a real basemap showing cloud regions, universities/research institutions, and data center locations within the city
- (b) A "city scorecard" comparing the focal city's bundle components against the quadrant median or global median — this directly connects the case study to the bundle analysis
- (c) A small-multiples comparison: the focal city vs. a peer city on 3–4 key metrics (distance, AI works, bundle score, institutional count)

### 1.3 — No external evidence supports the narrative

**Problem:** The current case studies rely entirely on the atlas's own data — distance, AI works count, bundle score. When the text says "Singapore has a national strategy that treats AI as an economic priority" or "Lagos has visible startup energy," these claims are unsupported by any citation. A judge evaluating "data complexity" and "properly documented" sources will notice. The project's earlier findings cite specific test statistics (KS D = 0.30, p < 0.001) but the case studies cite nothing.

**Fix:** Each case study needs 2–4 external sources that explain the mechanism — WHY this city conforms to or departs from the pattern. These are not decorative citations. They are the analytical glue between the atlas's quantitative findings and the city-level narrative.

### 1.4 — The text is repetitive and meta-commentary heavy

**Problem:** Each case study currently spends 1–2 paragraphs explaining why the case was chosen and what it demonstrates ("This makes Singapore the best example of..." / "That tension is exactly why it belongs in the StoryMap" / "This is the case that most clearly demonstrates why the project needs case studies"). The reader already knows this from the bridge section. Every sentence of meta-commentary is a sentence that could carry analytical content instead.

**Fix:** Cut all meta-commentary. The section header ("Singapore: Near compute / high AI") already tells the reader the case's role. Go straight into the evidence.

### 1.5 — No city-level data from the atlas is shown

**Problem:** The text says Singapore "sits extremely close to major cloud infrastructure" but never states the actual distance (4.1 km), the number of providers within reach (3), the number of cloud regions within 1,000 km, the AI works count, or the bundle score. These numbers exist in the data — they're just not in the narrative.

**Fix:** Each case study should open with a "data card" — either as a visual element or as the first sentence — showing:
- Distance to nearest cloud region (km)
- Nearest provider and region code
- Providers within 1,000 km
- Cloud regions within 1,000 km
- AI works count (from OpenAlex overlay)
- Bundle score (0–100)
- Bundle rank (out of top 1,000)

### 1.6 — The Dublin case doesn't exist yet

**Problem:** Seoul is being replaced with Dublin. The Dublin section needs to be written from scratch, including new maps, a new narrative, and external sources.

---

## PART 2: Data to Pull from Your Existing Files

Before doing any external research, extract these numbers from your own data for each city. This is the foundation.

### 2.1 — From `city_access_ai.csv` and `city_access_metrics.csv`

For each of the four cities, record:

| Metric | Singapore | Dublin | Ho Chi Minh City | Lagos |
|---|---|---|---|---|
| Distance to nearest cloud region (km) | ~4 | ~0 (hosts regions) | _______ | ~3,800 |
| Nearest provider | AWS (ap-southeast-1) | AWS (eu-west-1) | _______ | _______ |
| Providers within 500 km | _______ | _______ | _______ | _______ |
| Providers within 1,000 km | 3 | 3 | _______ | _______ |
| Cloud regions within 500 km | _______ | _______ | _______ | _______ |
| Cloud regions within 1,000 km | _______ | _______ | _______ | _______ |
| Population | _______ | _______ | _______ | _______ |
| AI works (openalex_ai_works_recent) | _______ | _______ | _______ | _______ |
| log_ai_works | _______ | _______ | _______ | _______ |
| Bundle score (0–100) | _______ | _______ | _______ | _______ |
| Bundle rank (of top 1,000) | _______ | _______ | _______ | _______ |

### 2.2 — From `cities_with_hotspots` or Gi* output

| Metric | Singapore | Dublin | Ho Chi Minh City | Lagos |
|---|---|---|---|---|
| Gi_Bin (hot/cold spot class) | _______ | _______ | _______ | _______ |
| Gi_ZScore | _______ | _______ | _______ | _______ |
| LISA COType (if available) | Expect: HH | Expect: not sig or LH | Expect: HL | Expect: LL or not sig |

### 2.3 — From `cloud_regions.gpkg`

For each case city, list the cloud regions within 500 km and 1,000 km:

**Singapore:**
- Within 500 km: [list provider, region code, distance]
- Within 1,000 km: [list]

**Dublin:**
- Within 500 km: [list — likely multiple AWS, Azure, GCP Ireland/UK regions]
- Within 1,000 km: [list — probably includes London regions too]

**Ho Chi Minh City:**
- Within 500 km: [list — may be sparse]
- Within 1,000 km: [list — Singapore regions may be within reach]

**Lagos:**
- Within 500 km: [list — likely zero]
- Within 1,000 km: [list — likely zero or very few]
- Nearest region: [South Africa? ~3,800 km?]

---

## PART 3: External Sources to Find

For each city, you need sources that explain the MECHANISM — why distance alone does or doesn't predict AI output here. Search for these specific things.

### 3.1 — Singapore (confirms the pattern)

The narrative: everything aligns — proximity, providers, institutions, government strategy. Sources should show the full stack.

**Search for:**
1. **National AI strategy:** Singapore's National AI Strategy 2.0 (NAIS 2.0), launched 2023. Search: `Singapore National AI Strategy 2.0`. This is the policy layer — government deliberately investing in AI as economic priority.
2. **Data center density:** Singapore is one of the world's densest data center markets. Search: `Singapore data center market 2025 2026`. Look for total capacity in MW, number of facilities, moratorium history (Singapore paused new data center builds 2019–2022 due to energy constraints, then selectively reopened — this is a nuanced detail that shows you understand the infrastructure).
3. **Research institutions:** NUS (National University of Singapore) and NTU (Nanyang Technological University) are both top-50 globally in AI/CS. Search: `NUS NTU AI research ranking`. This is the institutional depth component.
4. **Regional connectivity:** Singapore is a major submarine cable landing hub. Search: `Singapore submarine cable hub` or `Singapore internet exchange`. Multiple cables connect to Japan, Australia, India, and Southeast Asia. This explains why the regional context map should show cable routes.

**Key insight to build into the narrative:** Singapore didn't get close to compute by accident. The government deliberately attracted cloud providers through policy (tax incentives, energy infrastructure, data protection laws), and that deliberate strategy is part of why proximity, institutions, and connectivity all reinforce each other here. The atlas pattern holds because the factors are correlated by design, not by chance.

### 3.2 — Dublin (near compute / lower AI than expected)

The narrative: Dublin literally hosts cloud regions for all three hyperscalers but its research footprint doesn't match. Hosting ≠ producing.

**Search for:**
1. **Cloud region locations:** Confirm that AWS eu-west-1 (Ireland), Azure Ireland (Dublin), and GCP europe-west1 (or nearby) are all in or near Dublin. Search: `AWS eu-west-1 location Dublin` / `Azure Ireland region Dublin` / `GCP europe-west1 location`. This establishes the "distance = 0" fact.
2. **Why Ireland hosts so many data centers:** Tax incentives (Ireland's 12.5% corporate tax rate attracted tech multinationals), cool climate (natural cooling reduces energy costs), EU data residency rules, English-speaking workforce. Search: `why Ireland data center hub` or `Ireland data center boom reasons`. This explains the hosting side.
3. **Why research output is lower:** Ireland's total AI research output is smaller than UK, France, Germany. Trinity College Dublin and UCD are good but not top-20 in AI. Search: `Ireland AI research output comparison Europe` or `Trinity College Dublin AI research ranking`. The university system is strong but small — Ireland's population is under 5.3 million.
4. **The hosting ≠ producing distinction:** Look for any analysis that distinguishes between data center hosting locations and AI research production locations. Search: `data center location vs AI research production` or `cloud infrastructure location research output disconnect`. Even if nothing perfect exists, you can cite the fact that Ireland's tech sector is dominated by operations/services (Apple, Google, Meta European HQs) rather than R&D.
5. **IDA Ireland / enterprise strategy:** Ireland's Industrial Development Authority actively recruits tech multinationals for operations, not necessarily R&D. Search: `IDA Ireland tech sector operations vs research`. This is the policy mechanism that explains the disconnect.

**Key insight:** Dublin is the atlas's most powerful exception because it proves that compute proximity is necessary but not sufficient. You can sit on top of the infrastructure and still not produce proportional AI research — if the institutional and research ecosystem isn't scaled to match. The hosting decision was driven by tax and energy economics, not by research capacity. This is the "hosting ≠ producing" insight that only the atlas can surface.

### 3.3 — Ho Chi Minh City (farther from compute / high AI)

The narrative: outperforms distance prediction. Institutional capacity and regional connectivity offset weaker proximity.

**Search for:**
1. **AI research institutions:** Vietnam National University Ho Chi Minh City (VNU-HCM) has growing CS/AI programs. Search: `VNU-HCM AI research` or `Vietnam AI research universities`. Also check for private tech company R&D labs (VinAI, FPT Software).
2. **VinAI Research:** Vietnam's most prominent AI lab, founded by VinGroup. Published at NeurIPS, ICML, CVPR. Search: `VinAI Research Vietnam publications`. This is a specific, citable institutional anchor that explains research output.
3. **Vietnam national digital strategy:** Vietnam has a National Strategy on AI Development (2021–2030). Search: `Vietnam AI strategy 2030`. This parallels Singapore's NAIS but from a more developing-economy position.
4. **Regional connectivity:** HCMC connects to Singapore's submarine cable system. Search: `Vietnam submarine cable` or `Ho Chi Minh City internet connectivity Southeast Asia`. The city isn't as far from compute as raw distance suggests because it sits inside the broader Southeast Asian digital corridor.
5. **FPT Software and tech sector:** FPT is one of Southeast Asia's largest IT services companies, headquartered in Vietnam. Search: `FPT Software AI Vietnam`. This is the industry layer that complements the university layer.

**Key insight:** HCMC beats the distance pattern because it has invested in institutional capacity (VinAI, VNU-HCM, FPT) and sits inside a regional connectivity corridor that partially offsets its physical distance from cloud regions. The atlas's distance metric captures geographic location but not network topology — HCMC is farther in kilometers but not as disconnected as those kilometers suggest.

### 3.4 — Lagos (far from compute / absent from AI overlay)

The narrative: stacked disadvantage — distance, infrastructure constraints, institutional gaps compound.

**Search for:**
1. **Nearest cloud regions:** Confirm that the nearest major hyperscaler regions to Lagos are in South Africa (~3,800 km). Check whether any new AWS/Azure/GCP announcements have been made for West Africa. Search: `AWS Azure GCP West Africa region 2025 2026`. If a new region has been announced but not yet deployed, that's relevant — it shows the gap is recognized but not yet closed.
2. **Power reliability:** Nigeria's grid is notoriously unreliable. Data centers require stable power. Search: `Nigeria power grid reliability 2025` or `Lagos electricity supply data center`. Power instability is a major barrier to data center investment. This is the "stacked constraint" — not just distance, but the infrastructure needed to host local compute doesn't yet exist at scale.
3. **Internet connectivity:** Lagos has submarine cable connections (MainOne, ACE cable, 2Africa/Meta's cable). Search: `Lagos submarine cable internet connectivity`. This is important because it shows Lagos is NOT completely disconnected — there is bandwidth, but it terminates at the coast and doesn't translate into local cloud compute.
4. **Nigeria AI ecosystem:** There IS a growing tech ecosystem (Andela, Flutterwave, Paystack, various AI startups). Search: `Nigeria AI startup ecosystem Lagos` or `Lagos tech hub AI`. The point is that demand exists but the infrastructure supply doesn't match.
5. **Africa data center gap:** The broader context: Africa has <1% of global data center capacity despite 18% of global population. Search: `Africa data center capacity 2025 2026` or `Africa cloud computing gap`. You already cite this in the introduction — the case study should close the loop.

**Key insight:** Lagos tests the bottom-left quadrant of the atlas, but it's not a simple absence. There IS tech activity (startups, talent, demand), connectivity (submarine cables), and growing policy attention. What's missing is the local compute infrastructure to translate those assets into the kind of AI research production that shows up in OpenAlex. The constraints stack: distance to cloud regions, unreliable power supply, limited data center capacity, and an institutional research ecosystem that is growing but not yet at the scale of the top-tier hubs. This is what the priority screening layer is designed to surface.

---

## PART 4: New Figures to Create

### 4.1 — City Scorecard (one per city)

Create a small comparison graphic for each city showing its bundle components vs. a reference. Format options:

**Option A — Radar/spider chart:**
Five axes (proximity, diversity, redundancy, urban scale, institutions), one line for the focal city, one line for the global top-100 median. Shows which components are strong and which are weak.

**Option B — Horizontal bar chart:**
Five bars per city, each showing the component score vs. the global median. Color bars green if above median, red if below.

**Option C — Comparison table embedded in text:**
| Component | Singapore | Top-100 Median |
|---|---|---|
| Proximity | 99 | 85 |
| Provider diversity | 100 | 67 |
| Redundancy | 95 | 55 |
| Urban scale | 72 | 68 |
| Institutional depth | 90 | 45 |
| **Bundle score** | **92** | **64** |

Option C is the fastest to implement and works well in StoryMap. Option A is the most visually striking but requires a new figure.

### 4.2 — Upgraded Regional Context Maps

For each city, the regional context map should include:

| Layer | Source | Purpose |
|---|---|---|
| Country borders | Natural Earth | Geographic context |
| Neighboring major cities (labeled) | Natural Earth cities | Shows urban context |
| Cloud regions (labeled with provider + code) | cloud_regions.gpkg | Shows the compute landscape |
| 500 km / 1,000 km distance rings | Calculated | Shows accessibility thresholds |
| Submarine cable routes (optional) | TeleGeography free map | Shows physical connectivity |
| Terrain basemap | Esri or OpenStreetMap | Replaces blank grey |

These can be built in Python (matplotlib/cartopy) or in ArcGIS Online. Python is faster if you already have the pipeline.

### 4.3 — Dublin-specific figures

Since Dublin is new, you need:
1. A regional context map showing Ireland, UK, Western Europe, and ALL the cloud regions within 1,000 km (there will be many — Ireland, UK, Netherlands, France, Germany all have regions). This density makes the "hosting ≠ producing" insight visually obvious: Dublin is drowning in cloud regions.
2. A local-scale map or scorecard showing Dublin's bundle components — high on proximity/diversity/redundancy, lower on institutional depth.

---

## PART 5: Revised Case Study Structure Template

Each case study should follow this structure (aim for ~250–350 words per city, down from ~500+ currently):

```
## [City]: [Quadrant label]

[DATA CARD — 1-2 sentences with key numbers from the atlas]
Distance: X km. Providers within 1,000 km: X. AI works: X. Bundle score: X/100 (rank #X).

[WHAT THE ATLAS SHOWS — 1 paragraph]
What the atlas's distance metric, Gi* classification, and bundle score say about this city.
Cite the specific numbers. Reference the specific figures.

[WHY — 1-2 paragraphs with external evidence]
The mechanism that explains why this city conforms to / departs from the pattern.
Cite 2-3 external sources. Name specific institutions, policies, or infrastructure.
This is where the web search results go.

[REGIONAL CONTEXT MAP]
Caption: names the layers, sources, and what to look for.

[CITY SCORECARD or LOCAL MAP]
Caption: compares bundle components to reference.

[TAKEAWAY — 1 sentence, bold]
What this city demonstrates about the atlas's central question.
```

---

## PART 6: Execution Checklist

### Data extraction (from your CSVs)
- [ ] Pull all metrics from Part 2.1 for Singapore, Dublin, HCMC, Lagos
- [ ] Pull Gi* and LISA classifications from Part 2.2
- [ ] List cloud regions within 500 km and 1,000 km for each city from Part 2.3
- [ ] Record all numbers — these go into the data cards

### External research (web search)
- [ ] Singapore: NAIS 2.0, data center market, NUS/NTU rankings, submarine cables
- [ ] Dublin: Cloud region confirmations, Ireland data center reasons, Trinity/UCD research output, IDA Ireland strategy, hosting vs producing
- [ ] HCMC: VNU-HCM, VinAI publications, Vietnam AI strategy 2030, FPT Software, submarine cables
- [ ] Lagos: Nearest cloud regions, power reliability, submarine cables, Nigeria AI ecosystem, Africa data center gap

### New figures
- [ ] City scorecard for each city (Option A, B, or C from Part 4.1)
- [ ] Upgraded regional context map for Singapore
- [ ] New regional context map for Dublin
- [ ] Upgraded regional context map for HCMC
- [ ] Upgraded regional context map for Lagos
- [ ] Fix Lagos map "Middle East (Israel) - ???" artifact

### Writing
- [ ] Singapore case study — rewrite using template from Part 5
- [ ] Dublin case study — write from scratch using template
- [ ] HCMC case study — rewrite using template
- [ ] Lagos case study — rewrite using template
- [ ] Four-case summary paragraph (keep existing, minor edits for Dublin)
- [ ] Remove ALL meta-commentary sentences ("This is why it belongs in the StoryMap" etc.)
- [ ] "Compute is not destiny" appears max 1 time in case study section (in the summary, not in individual cases)

### Validation
- [ ] Each case study has a data card with atlas numbers
- [ ] Each case study cites 2–3 external sources
- [ ] Each case study has 2 figures (regional map + scorecard/local map)
- [ ] No case study exceeds 350 words of prose
- [ ] All four cases together span 4 continents (Asia, Europe, SE Asia, Africa)
- [ ] Dublin section has the "hosting ≠ producing" insight clearly stated
