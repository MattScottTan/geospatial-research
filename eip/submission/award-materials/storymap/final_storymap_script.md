# Final StoryMap Script

Working title: **AI Compute Accessibility Atlas**  
Subtitle: **Where cloud compute is close, where it is far, and why that matters for cities**

This file is the authoritative StoryMap copy deck and block order for the EIP submission. Use the sections in this exact order.

---

## Story-wide notes

- Treat the StoryMap as the primary judged experience.
- Use short text blocks and let maps, charts, and comparisons do as much explanatory work as possible.
- Keep the causal boundary explicit but brief.
- Treat the bundle index as the main originality callout.
- Treat the four city modules as the place-based explanation layer rather than as a second methods section.

---

## 1. Hook

**Recommended block:** Sidecar (docked)

**Media:**
- Primary: `Global Compute Accessibility` web map
- Fallback: `outputs/figures/fig1_access_map.png`

**Copy:**

### Title
AI does not happen on a blank map.

### Body
Modern AI may feel virtual, but the infrastructure behind it is not. Cloud regions, datacenter capacity, and supporting network systems are built in specific places, which means cities do not all begin from the same position.

This atlas maps that hidden geography across **8,000 cities**. It shows which places sit close to major AWS, Azure, and Google Cloud regions, which remain much farther away, and why that difference may matter for observed AI opportunity.

---

## 2. Why this matters

**Recommended block:** Standard narrative section with one embedded image

**Media:**
- `outputs/figures/fig2_ai_map.png`

**Copy:**
Cities do not enter the AI economy with equal infrastructure conditions. Some sit inside dense compute corridors. Others are hundreds or thousands of kilometers farther from the same systems.

If compute access is part of the enabling environment for AI, those gaps matter. They shape who can scale quickly, who works with more friction, and which places may be left out of the current wave of visible AI activity.

This atlas is therefore more than a descriptive map. It is a public-interest screening tool for judges, planners, and readers who want to see where compute access is concentrated, where it is thin, and where those gaps overlap with weak observed AI activity.

**Emphasis line:**  
**The project treats cloud infrastructure as part of the geography of AI, not as invisible background plumbing.**

---

## 3. The question and the short answer

**Recommended block:** Heading + short paragraph + quote block

**Copy:**
This project asks a simple question: once city size and geography are taken into account, do cities that are farther from major cloud regions tend to show less observed AI research activity?

**Quote block:**  
**Short answer:** yes. In the rebuilt atlas, the median city in the full 8,000-city frame is about **657 km** from its nearest major cloud region, while the median AI-linked city is only about **237 km** away.

**Follow-up sentence:**  
That gap does not disappear once geography is modeled more carefully, although the project does **not** claim a definitive causal estimate.

---

## 4. How the atlas works

**Recommended block:** Sidecar with 4 slides

### Slide 1 — A global comparison frame
**Media:** `Global Compute Accessibility` web map  
**Copy:** The atlas begins with the world’s 8,000 largest cities. That broad frame makes it possible to compare AI-linked cities to the wider city system rather than focusing only on familiar tech hubs.

### Slide 2 — A map of deployed cloud infrastructure
**Media:** `Global Compute Accessibility` web map  
**Copy:** The infrastructure layer is built from public coordinates for major deployed cloud regions run by AWS, Azure, and Google Cloud. A region is treated here as a named cluster of datacenters rather than a full map of every facility.

### Slide 3 — One transparent access measure
**Media:** `outputs/figures/fig7_distance_hist.png`  
**Copy:** For each city, the atlas measures the great-circle distance to the nearest major cloud region. This is a proxy, not a full measure of latency, pricing, or GPU availability. Its value is that it is transparent and comparable across thousands of cities.

### Slide 4 — Then compare compute access to observed AI activity
**Media:** `outputs/figures/fig5_coef_compare.png`  
**Copy:** The final step overlays observed AI-related research activity from the delivered OpenAlex-derived files, then checks whether the distance pattern survives whole-map clustering diagnostics and two spatial models.

---

## 5. What the atlas found

**Recommended block:** Heading + lead paragraph + Sidecar + compact model-check block

**Lead paragraph:**
The atlas reveals a clear pattern. Major cloud infrastructure is not evenly distributed across the global city system, and cities linked to observed AI research occupy a much more compute-proximate part of that landscape.

### Slide 1 — AI-linked cities sit much closer to major cloud regions
**Media:** `outputs/figures/fig7_distance_hist.png`  
**Copy:** The clearest result is descriptive. The median city in the full 8,000-city frame is about **657 km** from its nearest cloud region. The median AI-linked city is only about **237 km** away.

### Slide 2 — The center of gravity is closer still
**Media:** `outputs/figures/fig8_ai_weighted_distance.png`  
**Copy:** When the overlay is weighted by observed AI works, the center of gravity moves even closer to major cloud infrastructure, to about **164 km**.

### Slide 3 — The pattern is spatial, not just anecdotal
**Media:** `outputs/figures/fig11_hotspot_map.png`  
**Copy:** The relationship is spatially organized rather than random. Hot spots and cold spots show that the geography of AI opportunity has structure, even if that structure is not uniform everywhere.

### Slide 4 — The atlas works as a screening tool
**Media:** `outputs/figures/fig12_priority_cities_map.png`  
**Copy:** The project flags **1,988 priority cities** that combine above-threshold compute distance with no observed AI works in the delivered overlay. This turns the atlas into a public-interest triage tool.

**Compact follow-up block:**
The descriptive pattern also survives two more formal spatial checks. In both models, greater distance remains negatively associated with observed AI activity, even though the estimated effect becomes smaller once geography is modeled more explicitly.

---

## 6. Beyond distance: the infrastructure bundle

**Recommended block:** Heading + short intro + Sidecar with 3 slides

**Intro copy:**
Distance is the right place to start, but it is too thin to finish with. Some cities are close to one cloud region but do not sit inside a deeper opportunity environment. Others combine proximity with redundancy, institutional strength, and greater overall opportunity.

### Slide 1 — A Compute Opportunity Bundle Index
**Media:** `final_submission/originality/final/fig_bundle_index_map.png`  
**Copy:** The final submission extends the atlas with a **Compute Opportunity Bundle Index** that combines cloud proximity, provider diversity, regional redundancy, institutional anchors, and city scale.

### Slide 2 — Distance alone and bundle opportunity are not the same thing
**Media:** `final_submission/originality/final/fig_bundle_vs_distance.png`  
**Copy:** The bundle index does not discard distance. It shows which cities rise or fall once a broader opportunity bundle is considered.

### Slide 3 — The top bundle cities are not just the nearest cities
**Media:** `final_submission/originality/final/fig_bundle_top_cities.png`  
**Copy:** The highest-scoring bundle cities are places where proximity, redundancy, and institutional depth reinforce one another. That makes the final submission more original and better aligned with its core claim.

**Originality line:**  
**This submission’s main originality is not only that it maps compute distance, but that it shows why distance alone is too thin.**

---

## 7. Four cities that explain the pattern

**Recommended block:** Heading + intro paragraph + four repeated city modules

**Intro copy:**
The atlas shows a broad relationship between compute proximity and observed AI activity, but that relationship is not deterministic. These four cities explain why. Together they show what alignment looks like, what a measurement-limit case looks like, what an outperforming city looks like, and what a stacked-disadvantage city looks like.

### 7A. Singapore — near compute / high AI
**Media:**
- `final_submission/case_studies/singapore/regional_context/singapore_regional_context.png`
- `final_submission/case_studies/singapore/local_ecosystem/singapore_local_ecosystem.png`

**Copy:**
Singapore is the alignment benchmark in the atlas. It is extremely close to major cloud infrastructure and also shows strong AI-linked institutional anchoring. It demonstrates what the full compute-opportunity bundle looks like when proximity, redundancy, and institutions reinforce one another.

**Takeaway line:**  
**Singapore shows what infrastructure alignment looks like.**

### 7B. Seoul — near compute / low AI in the delivered overlay
**Media:**
- `final_submission/case_studies/seoul/regional_context/seoul_regional_context.png`
- `final_submission/case_studies/seoul/local_ecosystem/seoul_local_ecosystem.png`

**Copy:**
Seoul is the strongest reminder that the delivered research overlay is not the whole AI economy. It is extremely compute-rich in the atlas, but relatively quiet in the delivered AI research filter. That makes it the project’s clearest overlay-limit exception.

**Takeaway line:**  
**Seoul shows that compute access can be strong even when the current overlay understates the broader AI ecosystem.**

### 7C. Ho Chi Minh City — far compute / high AI
**Media:**
- `final_submission/case_studies/ho_chi_minh_city/regional_context/ho_chi_minh_city_regional_context.png`
- `final_submission/case_studies/ho_chi_minh_city/local_ecosystem/ho_chi_minh_city_local_ecosystem.png`

**Copy:**
Ho Chi Minh City is the atlas’s clearest “beats-the-pattern” city. It remains far from major cloud regions, yet still shows strong visible AI activity in the delivered overlay. This is the best case for showing that distance matters without fully determining outcomes.

**Takeaway line:**  
**Ho Chi Minh City shows that cities can outperform what distance alone would predict.**

### 7D. Lagos — far compute / low AI
**Media:**
- `final_submission/case_studies/lagos/regional_context/lagos_regional_context.png`
- `final_submission/case_studies/lagos/local_ecosystem/lagos_local_ecosystem.png`

**Copy:**
Lagos is the stacked-disadvantage case. It is one of the largest cities in the atlas, yet it remains far from major cloud infrastructure and weak in the delivered overlay. This makes Lagos one of the clearest public-interest cases in the project.

**Takeaway line:**  
**Lagos shows how compute gaps can matter most when they stack together with weaker institutional anchoring and thinner opportunity conditions.**

**Cross-case close:**
Together, the four cities explain the project’s mature conclusion: compute is not destiny, but it is part of the infrastructure bundle that shapes AI opportunity.

---

## 8. What this means

**Recommended block:** Heading + short narrative + sidecar or image-led interpretation block

**Copy:**
The atlas is not a map of who can and cannot do AI. It is a map of one hidden infrastructure layer that helps shape the geography of AI opportunity.

Its main practical value is that it helps distinguish three different stories: places where compute access and visible AI activity align, places where the current overlay understates a broader AI ecosystem, and places where infrastructure gaps may still be part of a stacked disadvantage. That makes the atlas useful as a screening and communication tool for public-interest readers, not just as a technical exercise.

**Emphasis line:**  
**Compute is not destiny. But it is not irrelevant either.**

---

## 9. Limits, sources, and about the project

**Recommended block:** Closing narrative + credits + source list + bio block

**Copy:**
This project does not claim that cloud proximity alone determines whether a city succeeds in AI. It does not claim that every city far from compute is excluded, or that every city close to compute will become a major AI hub. It also does not present a definitive causal estimate.

Instead, it offers a disciplined spatial diagnosis: a way to see where compute access may be reinforcing advantage, where other factors are offsetting distance, and where infrastructure gaps may still matter.

**Source / credits block should include:**
- world city frame
- cloud-region layer (AWS, Azure, Google Cloud)
- OpenAlex-derived city overlay and institution anchors
- atlas outputs and final bundle-index outputs
- local notebooks/report package
- ArcGIS Online / StoryMaps assembly note

**Bio/photo placeholder:**  
Add submitter bio and headshot at final assembly time.
