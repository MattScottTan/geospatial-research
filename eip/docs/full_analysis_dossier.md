# Full Analysis Dossier

This dossier is the master reader guide for the full project bundle. It explains what each stage did, what it established, what it did **not** establish, and where the corresponding files live.

---

## 1. Narrative spine of the project

The project asks whether **compute accessibility** — operationalized as proximity to major hyperscaler cloud regions — is part of the geography of observed AI opportunity.

The mature conclusion after all analytical work is:

**Compute accessibility is a meaningful spatial correlate and diagnostic layer, but not a proven universal causal driver of city-level AI research output.**

That is why the final EIP-oriented framing pivots from “causal proof” to “hidden infrastructure bundle”: cloud proximity matters, but it sits alongside power, connectivity, institutions, and policy.

---

## 2. Core reader-facing documents and what they answer

### `report/main.pdf`
The revised main report. Read this first if you want the finished atlas narrative.

### `docs/concept_motivation_brief.pdf`
Answers:
- Why this question matters
- Why cloud compute is virtual but still not geography-free
- Why AI research was used as the initial measurable proxy
- What uncertainties needed to stay visible before any analysis began

### `docs/analysis_approach_stage1_brief.pdf`
Answers:
- What the first-level geospatial EDA is doing
- How the infrastructure inventory, nearest-region distance, and global comparison frame work
- Why AI-linked cities are descriptively closer to compute than the broader city system

### `docs/analysis_approach_stage2_brief.pdf`
Answers:
- Why the project moved from maps to spatial diagnostics
- What Moran’s I and local Gi* add
- Why the GP and CAR/GMRF models were used
- What priority-city screening and regional deep dives contribute

### `docs/analysis_approach_stage3_brief.pdf`
Answers:
- How Stages 1 and 2 combine into the full argument
- What the paper can say strongly
- What the paper should not say
- Why the project still matters despite the causal limit

### `docs/analysis_approach_stage4_brief.pdf`
Answers:
- What happens when you push the cross-sectional design harder toward causality
- What richer controls and within-country comparisons do to the coefficient
- Why the negative association weakens under stricter causal stress tests

### `docs/stage5_pilot_summary.md`
Answers:
- What the first city-year panel pilot tested
- What a local AWS-region opening event-study looked like in a small sample
- Why the pilot did not produce a stable causal result

### `docs/stage6_expanded_panel_summary.md`
Answers:
- What happened when the pilot was expanded to a broader selected-city panel
- Why staggered-adoption estimates remained heterogeneous and specification-dependent
- Why the project remains strongest as an atlas rather than a causal paper

### `docs/eip_case_study_matrix.md`
Answers:
- Which four cities best explain the pattern and the exceptions
- How the project should pivot for EIP from coefficient-centered analysis to place-based explanation

### `docs/final_map_spec_report.pdf`
Answers:
- What the final figure package should be
- What layers each map needs
- How the four comparative case studies should be mapped at regional and local scales

---

## 3. Stage-by-stage interpretation

### Stage 1 — descriptive geospatial EDA

**Goal:** establish that compute access has a real and measurable geography.

**What it did:**
- built the cloud-region point layer
- built the top-8,000-city comparison frame
- measured nearest-region distance for every city
- compared AI-linked cities against the full city system
- visualized access patterns, distance distributions, and raw scatter relationships

**What it established:**
- compute access is geographically uneven
- AI-linked cities are descriptively much closer to compute than the full city frame
- the bulk of observed AI activity is even more compute-proximate than simple AI-city presence alone suggests

**What it did not establish:**
- causality
- mechanism
- whether distance is proxying for something broader like institutions or national ecosystems

**Main files:**
- `docs/analysis_approach_stage1_brief.pdf`
- `outputs/figures/fig1_access_map.png`
- `outputs/figures/fig7_distance_hist.png`
- `outputs/figures/fig8_ai_weighted_distance.png`
- `outputs/figures/fig4_scatter_ai_vs_dist.png`

---

### Stage 2 — spatial diagnostics and controlled modeling

**Goal:** determine whether the descriptive pattern survives spatial dependence and broad geographic structure.

**What it did:**
- estimated global Moran’s I
- mapped local Gi* hot and cold spots
- screened for priority cities / AI deserts
- fit GP and CAR/GMRF model tracks to absorb spatial structure

**What it established:**
- the spatial pattern is not random
- compute distance remains part of the story even after spatial controls, but the effect attenuates
- certain cities and regions deserve targeted attention because they combine weak access and low observed AI activity

**What it did not establish:**
- that cloud-region proximity is the true causal mechanism
- that omitted infrastructure or institutional variables are irrelevant

**Main files:**
- `docs/analysis_approach_stage2_brief.pdf`
- `outputs/tables/morans_i_summary.csv`
- `outputs/figures/fig11_hotspot_map.png`
- `outputs/figures/fig12_priority_cities_map.png`
- `outputs/tables/model_gp_summary.json`
- `outputs/tables/model_car_summary.json`

---

### Stage 3 — synthesis and interpretation

**Goal:** combine the evidence into the strongest justified claim.

**What it established:**
- compute accessibility is part of the explanation space for AI geography
- the project is best understood as an infrastructure atlas and spatial diagnosis
- the right interpretation is associational and policy-relevant, not triumphalist causality

**Main files:**
- `docs/analysis_approach_stage3_brief.pdf`
- `report/main.pdf`

---

### Stage 4 — causal stress tests within the cross-sectional frame

**Goal:** see whether the original negative relationship survives more demanding comparisons.

**What it did:**
- reproduced the baseline cross-sectional regression
- added richer geography controls
- added country fixed effects
- ran within-country demeaned checks
- tried treatment-style matching / weighting thresholds

**Main result:**
the original negative sign is not stable once the comparison gets closer to a causal read.

**Why this matters:**
it defined the project’s evidentiary boundary. The atlas remained useful, but the paper should not claim that cloud proximity has been causally identified.

**Main files:**
- `docs/analysis_approach_stage4_brief.pdf`
- `docs/analysis_approach_stage4_summary.md`
- `extensions/stage4/outputs/stage4/tables/stage4_model_summary.csv`
- `extensions/stage4/outputs/stage4/figures/fig_stage4_coef_stress_test.png`

---

### Stage 5 — pilot city-year panel and event study

**Goal:** move beyond snapshot cross-sections and test for treatment-like dynamics around AWS-region openings.

**What it did:**
- built a small selected-city panel from top-institution OpenAlex counts
- used local AWS-region launches as treatment timing
- estimated TWFE and event-study summaries

**Main result:**
the pilot did not deliver a stable or convincing positive treatment effect.

**Why this matters:**
the causal story still did not lock in even after moving to a panel.

**Main files:**
- `docs/stage5_pilot_summary.md`
- `extensions/stage5/outputs/tables/stage5_twfe_summary.csv`
- `extensions/stage5/outputs/tables/stage5_event_study_summary.csv`
- `extensions/stage5/outputs/figures/fig_stage5_event_study.png`

---

### Stage 6 — expanded selected-city panel

**Goal:** see whether a broader staggered-adoption panel changes the picture.

**What it did:**
- expanded the selected-city panel across several countries
- estimated broader TWFE, cohort-by-cohort DID, and stacked DID summaries

**Main result:**
the results remained heterogeneous and specification-dependent. One specification turned positive, but the broader evidence still did not line up behind a robust causal effect.

**Why this matters:**
the expanded panel sharpened the distinction between the project’s **descriptive strength** and its **causal limit**.

**Main files:**
- `docs/stage6_expanded_panel_summary.md`
- `extensions/stage6/outputs/tables/stage6_twfe_summary.csv`
- `extensions/stage6/outputs/tables/stage6_cohort_did_summary.csv`
- `extensions/stage6/outputs/tables/stage6_stacked_did_summary.csv`
- `extensions/stage6/city_url_map.csv`

---

## 4. Final EIP pivot

After Stage 6, the strongest EIP framing became:

**The atlas identifies a hidden infrastructure layer of AI opportunity. The case studies explain why some cities align with the pattern and why others depart from it.**

That is why the final product plan pivots to the four-city matrix:
- near compute / high AI
- near compute / low AI
- far compute / high AI
- far compute / low AI

These are not meant to replace the quantitative backbone. They are meant to explain the bundle of omitted spatial factors the regressions do not fully settle:
- power and data-center market conditions
- connectivity corridors, IXPs, and subsea cable geography
- university and research strength
- AI jobs, startups, patents, and adoption
- national or city-level AI strategy

**Main files:**
- `docs/eip_case_study_matrix.md`
- `docs/final_map_spec_report.pdf`

---

## 5. Frozen artifacts vs live rebuilds

### Frozen artifacts included in this bundle
- all main atlas outputs under `outputs/`
- revised report files under `report/` and `deliverables/`
- Stage 4 tables and figures
- Stage 5 pilot tables and figures
- Stage 6 summary tables

### Live rebuilds available
- `src/pipeline.py all` for the core atlas
- `extensions/stage4/src/stage4_causal_extension.py`
- `extensions/stage5/src/stage5_pilot_panel.py`
- `extensions/stage6/src/stage6_expanded_panel.py` for a **live** selected-city refresh from OpenAlex

The Stage 6 live rebuild may drift from the frozen outputs because the selected city-year counts are drawn from a live external source.

---

## 6. Best concise takeaway for later use

If you want one sentence to remember the whole project:

**The project maps an overlooked infrastructure layer of AI opportunity, shows that compute access is geographically uneven, and argues that compute is not destiny but part of a wider spatial bundle that shapes where AI activity concentrates.**
