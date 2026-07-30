# WORK.md — EIP + Fisher Submission: Continuation State

## Project
**Title:** Cloudy with a Chance of Compute  
**Subtitle:** Mapping the hidden geography of AI compute across 8,000 cities — and who it leaves behind  
**Author:** Matthew Tan  
**StoryMap:** https://storymaps.arcgis.com/stories/744a1c433d554cef8b3861d72836fdd2  
**Target Awards:** Harvard CGA EIP Student of the Year + Fisher Prize  
**EIP Deadline:** March 15, 2026 (passed — confirm registration status)  
**Fisher Deadline:** May 3, 2026

---

## Context Files Available

These files were uploaded in the previous session and should be re-uploaded for continuation:

### Data files
- `city_access_metrics.csv` — all 8,000 cities with distance to nearest cloud region
- `city_access_ai.csv` — 328 AI-linked city rows (319 unique by ID)
- `cloud_regions.gpkg` — cloud region locations
- `openalex_institutions_top.csv` — top AI institutions
- `ne_110m_admin_0_countries.geojson` — country boundaries
- `ai_access_cities.geojson` / `ai_access_cities.gpkg` — city layers for ArcGIS
- `ai_access_ai_cities.gpkg` — AI city layer

### Scripts
- `pipeline.py` — main analysis pipeline (3,369 lines), generates all figures
- `build_prototypes.py` — generates bundle index and originality figures
- `distributional_tests.py` — Finding 1 statistical tests (KS, Mann-Whitney, chi-square, Cohen's d)
- `weighted_concentration_tests.py` — Finding 2 statistical tests (Spearman, permutation, concentration ratios)

### Project spec files
- `final_storymap_script.md` — original StoryMap copy deck
- `webmap_specs.md` — ArcGIS Online web map specifications
- `arcgis_handoff.md` — manual assembly instructions
- `captions_and_alt_text.md` — original captions
- `bio_and_photo_requirements.md` — bio placeholder

### Deliverables from previous session
- `WINNER_MATRIX.md` — 18 inventoried EIP+Fisher winners with 6 full feature extractions
- `AWARD_PLAYBOOK.md` — weighted rubric, 35-item checklist, 10 templates, 7-map kit, 15 failure modes
- `NOVELTY_METHODS_MEMO.md` — 12 data sources, 12 methods, 5 originality packages
- `SUBMISSION_GAP_ANALYSIS.md` — rubric scorecard (3.95/5.00), 8 specific gaps, prioritized task list
- `REVISION_CHECKLIST.md` — section-by-section editing guide with 11 section checklists
- `HERO_MAP_INSTRUCTIONS.md` — ArcGIS Online click-by-click for hero map
- `SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md` — ArcGIS Pro click-by-click for Moran's I and Gi*

---

## Current Rubric Score: 3.95 / 5.00

| Category | Weight | Score | Notes |
|----------|--------|-------|-------|
| Framing / Problem Choice | 15% | 5 | Revised introduction is strong |
| StoryMap Architecture | 15% | 4 | Findings restructured; some sections still need revision |
| GIS / Cartography | 25% | 3→3.5 | Hero map upgraded; other maps still need work |
| Evidence / Analysis | 20% | 4→4.5 | Statistical tests added to Findings 1-2; methods named |
| Originality | 15% | 5 | Topic is unique in winner corpus |
| Packaging / Polish | 10% | 3 | Bio missing; captions partially updated; theme not yet customized |

---

## Completed Revisions

### Text sections revised (use these, not the original script)

#### Title + Subtitle ✅
**Old:** AI Compute Accessibility Atlas / Where cloud compute is close, where it is far, and why that matters for cities  
**New:** Cloudy with a Chance of Compute / Mapping the hidden geography of AI compute across 8,000 cities — and who it leaves behind

#### Introduction / Problem Statement ✅
Fully rewritten. Four paragraphs:
1. Singapore 4km vs Lagos 3,800km contrast → infrastructure position differs
2. Why distance matters: latency (50-150ms), data transfer costs, real-time inference viability
3. Scale of imbalance: $600B capex, Africa <1% of data center capacity, IMF/WEF warnings, Global North adoption 2× faster
4. Gap in existing discourse + research question

Key sources cited: IMF, WEF, CSIS, UNCTAD, McKinsey, hyperscaler documentation.

#### Hero Map Transition Text ✅
**Old:** "Cities do not enter the AI economy with equal infrastructure conditions..." (restated introduction)  
**New:** Teaches reader how to read the map — what colors mean, what diamonds represent, names the visible corridors and gaps, previews structure of what follows.

#### Figure 2 Transition ✅
**Old:** Separate "Why this matters" + "Question/short answer" sections (redundant with new intro)  
**New:** Single paragraph introducing Figure 2 with the 72%/44% comparison and 237/657 median stats. Three-stage structural preview (methods → results → case studies). Research question and short answer absorbed into introduction.

#### "How the Atlas Works" (Methods) ✅
Fully rewritten as three numbered stages:
- Stage 1: 8,000 cities from Natural Earth
- Stage 2: 60+ cloud regions from AWS/Azure/GCP, geodesic great-circle distance
- Stage 3: OpenAlex AI overlay (328 cities), Getis-Ord Gi*, Global Moran's I, GP + CAR/GMRF regression
- Names ArcGIS Online, ArcGIS Pro, and Python throughout

#### Finding 1: Distributional Difference ✅
- Header: "AI-linked cities occupy a fundamentally different part of the compute-access landscape"
- Teaches reader how to read the histogram
- Statistical tests added: KS (D=0.30, p<0.001), Mann-Whitney (U=786,844, p<0.001), chi-square (χ²=103.8, p<0.001), Cohen's d=0.74
- 72% vs 44% comparison in body text
- Medians in caption only (not restated)
- Uses n=328 to match Figure 7

#### Finding 2: Weighted Concentration ✅
- Header: "The concentration sharpens when weighted by research volume"
- Weighted median 164km, concentration ratios (62%/81%/93% at 250/500/1000km)
- Spearman correlation reported honestly (ρ=−0.05, p=0.40 — not significant within AI sample)
- Explains that main signal is between AI and non-AI cities, not within AI set
- Uses n=328 to match Figure 8

#### Finding 3: Spatial Structure ✅
- Header: "The pattern is spatially structured, not randomly distributed"
- Explains why spatial autocorrelation analysis is needed
- Moran's I explained from first principles (I=0.066, z=2.86, p=0.008)
- Getis-Ord Gi* explained: 7 hot spots, 33 cold spots, Macau top hot spot, Carbondale top cold spot
- "Why these methods" paragraph: not common in this domain, two complementary scales, ArcGIS toolbox
- Alternatives discussed: KDE, DBSCAN, LISA — why Gi* was chosen
- Recommends running in ArcGIS Pro as primary, Python as validation

#### Finding 4: Priority Cities ✅
- Header: "The atlas identifies 1,988 priority cities where compute distance and absent AI activity converge"
- Screening methodology made explicit: zero AI works + distance > 1,252km upper quartile
- Geographic breakdown: Africa 468 cities (median 2,676km), Latin America 704 cities (median 1,298km)
- Named cities: Lagos, Kinshasa, Khartoum, Lima, Bogotá
- Policy audience named: planners, innovation agencies, international development organizations
- "In the current build" hedge removed

#### Finding 5: Spatial Regression ✅
- Header: "The distance-activity relationship survives spatial regression controls"
- Explains why regression is needed (confounding: city size, continental geography)
- GP model explained: smooth spatial field, distance coeff −0.207, population +0.279
- CAR/GMRF explained: neighborhood structure, distance coeff −0.052, population +0.309
- Attenuation interpreted as expected (more aggressive spatial control)
- Key result: directional consistency — sign doesn't flip
- THIS is the canonical causal caveat location — all earlier caveats should be cut
- Specific closing: "does not claim that relocating a city closer would mechanically increase output"

### Maps revised

#### Hero Map (Global Compute Accessibility) ✅
- Cities colored by distance to nearest cloud region (blue→yellow ramp, upper handle at ~2,500-3,500km)
- Cities sized by population (4-25px range)
- Cloud regions as diamonds colored by provider (AWS=orange, Azure=green, GCP=red)
- Cloud regions layer drawn on top
- Legend visible with renamed layers: "Cloud Regions" and "City Compute Accessibility"
- Published in ArcGIS Online, shared publicly

---

## Remaining Work (Priority Order)

### MUST-DO — Text Revisions

- [ ] **Bundle Index section** — rewrite "Beyond distance: the infrastructure bundle" (pages 7-9). Needs: specify the 5 bundle components and weights (proximity 40%, provider diversity 15%, redundancy 15%, population 15%, institutions 15%), name the method (weighted composite), add novelty callout box. Current text repeats the concept 3× without specifying components.

- [ ] **Four City Case Studies** — rewrite Singapore, Seoul, Ho Chi Minh City, Lagos sections (pages 10-18). Needs: fix/replace "Local Ecosystem" lat/lon scatter charts, upgrade regional context maps, cut each case by ~30%, remove meta-commentary ("That tension is exactly why it belongs in the StoryMap"), fix Lagos map "???" artifact. Cut the typology preview paragraph on p.10.

- [ ] **Conclusion** — rewrite "What this means" (pages 19-20). Needs: cut restatements of earlier findings, add forward-looking policy sentence, end on strongest sentence, cut the four-case restatement that duplicates page 18.

- [ ] **Sources / Credits section** — MISSING, must add. Needs: data sources table (Natural Earth, hyperscaler docs, OpenAlex — with dates, resolution, access links), tools used (ArcGIS Pro, ArcGIS Online, Python with specific packages), code/reproducibility links, acknowledgments.

- [ ] **Author bio + professional photo** — MISSING, required for EIP. Needs: name, program, school, 40-80 word bio, headshot.

### MUST-DO — Maps & Figures

- [ ] **Run Moran's I and Gi* in ArcGIS Pro** — replicate Python results using Spatial Statistics toolbox. Report ArcGIS Pro as primary tool, Python as validation. Instructions in `SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md`.

- [ ] **Fix "Local Ecosystem" case study charts** — replace raw lat/lon scatter plots with proper local-scale maps on real basemaps, or add axis labels + city boundary underlay.

- [ ] **Fix Lagos regional context map** — remove "Middle East (Israel) - ???" rendering artifact.

- [ ] **Upgrade case study regional context maps** — add richer basemaps, surrounding city labels, country borders.

- [ ] **Build the two remaining web maps** per `webmap_specs.md`:
  - "AI Research and Hot Spots" — `cities_with_hotspots` layer styled by Gi* class
  - "AI Deserts and Priority Cities" — `priority_cities` layer styled by priority rank

### STRONG UPGRADES

- [ ] **Custom StoryMap theme** — consistent color palette tying maps, charts, and text. Nearly every 2024 Esri competition winner used a custom theme.

- [ ] **Add 500km buffer rings** to hero map — visually shows compute corridors, connects to the 72% stat.

- [ ] **Add open science links** — publish code/data to GitHub or Harvard Dataverse. [FIS-2025-UG-1] was explicitly praised for this.

- [ ] **Add Moran's I scatterplot** (already generated as `morans_i_scatterplot.png`) alongside or after the hot spot map in Finding 3.

- [ ] **Add Sub-Saharan Africa deep dive** (Figure 13) and **Latin America deep dive** (Figure 14) as supplementary regional views in the priority cities section.

- [ ] **Consider running LISA** (Cluster and Outlier Analysis) in ArcGIS Pro — produces HH/LL/HL/LH categories that map directly onto the four case studies (Singapore=HH, Lagos=LL, HCMC=HL, Seoul=LH).

- [ ] **Mobile testing** — check the full StoryMap on a phone in incognito mode.

### OPTIONAL POLISH

- [ ] **Peer review** — non-GIS friend reads through and flags confusion points.
- [ ] **Sensitivity analysis** on screening threshold (what happens at 1,000km vs 1,252km vs 1,500km?).
- [ ] **Workflow diagram** in methods sidecar showing the analysis pipeline visually.

---

## Verified Numbers (use these — they match the pipeline's n=328)

| Statistic | Value | Source |
|-----------|-------|--------|
| All cities in frame | 8,000 (7,999 with dist>0) | city_access_metrics.csv |
| AI-linked cities (raw) | 328 | city_access_ai.csv |
| AI-linked cities (unique by ID) | 319 | aggregate_ai_city_matches() |
| Median distance, all cities | 657 km | pipeline fig7 |
| Median distance, AI cities (n=328) | 237 km | pipeline fig7 |
| Median distance, AI cities (n=319) | 248 km | pipeline spatial diagnostics |
| Weighted median (n=328) | 164 km | pipeline fig8 |
| AI cities within 500km | 237 (72.3%) | n=328 |
| All cities within 500km | 3,485 (43.6%) | n=7,999 |
| KS test | D=0.30, p<0.001 | n=328 vs n=7,999 |
| Mann-Whitney U | U=786,844, p<0.001 | n=328 vs n=7,999 |
| Chi-square (500km) | χ²=103.8, df=1, p<0.001 | n=328 vs n=7,999 |
| Cohen's d | 0.74 (medium-large) | n=328 vs n=7,999 |
| Spearman within AI sample | ρ=−0.047, p=0.40 | n=328 |
| Moran's I | I=0.066, z=2.86, p=0.008 | n=319 unique |
| Gi* hot spots | 7 (1 at 99%, 6 at 95%) | n=319 unique |
| Gi* cold spots | 33 (10 at 99%, 23 at 95%) | n=319 unique |
| Top hot spot | Macau (99%) | Gi* |
| Top cold spot | Carbondale, US (99%) | Gi* |
| GP distance coefficient | −0.207 | spatial regression |
| CAR distance coefficient | −0.052 | spatial regression |
| GP population coefficient | +0.279 | spatial regression |
| CAR population coefficient | +0.309 | spatial regression |
| Priority cities | 1,988 across 125 countries | screening layer |
| Priority threshold | >1,252 km + zero AI works | upper quartile |
| Africa priority cities | 468, median 2,676 km | fig13 |
| Latin America priority cities | 704, median 1,298 km | fig14 |
| Bundle index weights | proximity 40%, diversity 15%, redundancy 15%, population 15%, institutions 15% | build_prototypes.py |

---

## Key Decisions Made

1. **Title:** "Cloudy with a Chance of Compute" — creative, memorable, mirrors winning title patterns
2. **n=328 for body text** — matches Figures 7 and 8; n=319 used only for spatial diagnostics (Moran's I, Gi*, regression)
3. **ArcGIS Pro as primary cited tool** — Python as validation backup. EIP requires Esri technology demonstration.
4. **Causal caveat stated once** — in Finding 5 (spatial regression), not repeated elsewhere
5. **Statistical tests added** — KS, Mann-Whitney, chi-square, Cohen's d for Finding 1; Spearman + concentration ratios for Finding 2. Fills the methodological gap between description and modeling.
6. **Honest reporting** — Spearman within-sample correlation is not significant; reported transparently with interpretation

---

## Learnings from Winner Analysis

- **Judge comment patterns:** Judges consistently reward timeliness, documented data, breadth of GIS methods, professional finish, policy relevance, and statistical integration
- **EIP specifically rewards:** Esri technology use, innovation, potential impact, organization
- **Fisher specifically rewards:** data complexity and documentation, analytical execution, cartographic communication
- **Title creativity matters:** [EIP-2025-1] used a pun title and won; Esri competition guide explicitly encourages creative approaches
- **Open science is rare and praised:** only [FIS-2025-UG-1] did it, was explicitly rewarded
- **"Professional level of quality from start to finish"** was the strongest endorsement in the corpus ([EIP-2024-1])
- **Intellectual honesty strengthens credibility:** reporting non-significant results and explaining why shows maturity judges associate with publication-quality work
