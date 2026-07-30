# BUNDLE SECTION — Replacement Text for StoryMap

> Replace everything from "Beyond distance: the infrastructure bundle" through
> "That is why the project does not treat compute distance as destiny..."
> with the text below. The figures (bundle map, scatter plot) stay as they are.

---

## Beyond distance: the infrastructure bundle

Distance to the nearest cloud region is the simplest access measure in the atlas, but it is not the whole story. Two cities can sit the same distance from a cloud region and still differ sharply in whether that proximity translates into practical AI opportunity — because the surrounding infrastructure differs.

To capture that wider context, the atlas constructs a Compute Opportunity Bundle Index that scores each city on five components:

**Proximity** (40% weight) — inverse distance to the nearest major cloud region, the core accessibility measure from Findings 1–5.

**Provider diversity** (15%) — number of distinct hyperscalers (AWS, Azure, Google Cloud) reachable within a threshold distance. A city near regions from all three providers has more competitive options and redundancy than one served by a single provider.

**Redundancy** (15%) — total number of cloud regions within reach, regardless of provider. More nearby regions mean more failover capacity and lower risk of service disruption.

**Urban scale** (15%) — city population, as a proxy for local market depth, labor availability, and demand for AI-adjacent services.

**Institutional depth** (15%) — presence of top-ranked AI research institutions (drawn from the OpenAlex institutional overlay), capturing whether a city has an established research base that can convert compute access into research output.

Each component is normalized to a 0–100 scale and combined as a weighted sum. The result is a single score that reflects not just how close a city is to compute, but how much of the surrounding infrastructure ecosystem supports turning that access into opportunity.

[KEEP THE BUNDLE MAP FIGURE HERE — no changes needed to the figure itself]

[KEEP THE EXISTING CAPTION: "The Compute Opportunity Bundle Index combines compute proximity with wider enabling conditions to show where cities sit inside a stronger or weaker infrastructure bundle."]

The scatter plot below compares each city's distance-only access score (x-axis) against its full bundle score (y-axis). If distance were the whole story, every city would sit on the diagonal. The spread away from it reveals where wider infrastructure conditions push cities above or below what distance alone would predict. Paris, London, and Beijing cluster at the top right — strong on both dimensions. Cities like Riyadh and Doha score high on distance-only access but drop when the full bundle is considered, reflecting thinner institutional and provider-diversity layers despite geographic proximity to cloud regions.

[KEEP THE SCATTER PLOT FIGURE HERE — no changes needed]

[REPLACE THE EXISTING CAPTION with:]
Bundle score vs. distance-only access score for the top 1,000 cities by population. If distance were the whole story, all cities would sit on the diagonal. Departures reveal where wider infrastructure — provider diversity, redundancy, institutional depth, and urban scale — pushes cities above or below their distance-only position. Sources: Natural Earth, hyperscaler documentation, OpenAlex. Analysis: Python (weighted composite). Visualization: matplotlib.

---

## What changed vs. the current version

| Current problem | How the replacement fixes it |
|---|---|
| Components never named — just "connectivity, institutional depth, and local infrastructure context" | All 5 components listed with exact weights |
| Method never named | "Weighted sum" stated explicitly |
| Data sources for bundle unclear | Each component's data source is named |
| The concept is stated 3 times ("extends beyond distance alone," "not a replacement," "depends on how compute access combines...") | Stated once, then the scatter plot does the work |
| Caption on scatter plot is generic | New caption explains the diagonal, names specific cities, lists sources |
| ~350 words of prose | ~280 words — tighter by ~20% |

---

## Notes for pasting into StoryMap

- The section header "Beyond distance: the infrastructure bundle" stays the same.
- The five components can be formatted as a bulleted list or as bold-lead paragraphs — whichever fits your StoryMap theme better.
- If you want to add a novelty callout box (recommended), insert it right after the five components:

> **What's new here:** This is the first global atlas to treat cloud compute infrastructure as a measurable layer of AI geography, combining proximity, provider diversity, redundancy, urban scale, and institutional depth across 8,000 cities and three hyperscaler networks.

- The phrase "compute is not destiny" should NOT appear in this section. Save it for the conclusion (max 2 occurrences total in the entire StoryMap).
