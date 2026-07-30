# WORK.md

## 0. Snapshot
- Job Type: **Mixed (Research/Synthesis + Geospatial Design + Writing/Exposition + Submission Operations)**
- Primary Deliverables:
  - `WINNER_MATRIX.md` — evidence-backed feature extraction matrix for past **EIP + Fisher** winners and closely relevant official StoryMap exemplars.
  - `AWARD_PLAYBOOK.md` — actionable checklist + weighted scoring rubric + concrete StoryMap/report templates/snippets tuned to **EIP + Fisher** judging logic.
  - `NOVELTY_METHODS_MEMO.md` — ranked menu of **Harvard-accessible data sources** and **ArcGIS/Esri spatial methods** that could make the submission more original and harder to replicate.
  - `SUBMISSION_GAP_ANALYSIS.md` — scored comparison of the current project against the playbook, with exact remaining work needed to reach submission quality.
- Stakeholders / Audience:
  - Primary: **Harvard CGA EIP Student of the Year + Fisher Prize** committees.
  - Secondary: Harvard faculty, informed public-interest readers, StoryMap judges, and technically literate readers who expect methodological seriousness without dense exposition.
- Constraints:
  - Scope: prioritize **officially listed Harvard EIP + Fisher winners**, especially entries with public StoryMaps / project pages / judge comments / award pages.
  - Secondary benchmark set: official **Esri StoryMaps competition criteria** and, only if needed, a small number of directly relevant high-quality StoryMap exemplars.
  - Inputs: web retrieval first; if archived StoryMaps or winner pages are missing, record them as **BLOCKED** and proceed with metadata-only extraction.
  - Workflow: **4-pass** — (1) inventory + evidence capture; (2) synthesis into prize playbook; (3) novelty/originality scouting; (4) gap analysis against the current project.
  - Audience tradeoff to optimize: **public readability + strong geospatial reasoning + professional finish + visible originality**.

---

## 1. Goal

### Objective
Build a high-signal, evidence-backed **EIP + Fisher submission playbook** by analyzing past Harvard geospatial prize winners, official StoryMap judging criteria, and Harvard-accessible data/method resources. The playbook should distill (i) public-interest framing, (ii) StoryMap structure and section rhythm, (iii) cartographic and GIS implementation patterns, (iv) evidence and analysis packaging, and (v) originality mechanisms that recur in strong entries. It should then score the current project against that playbook and identify the exact remaining work needed to produce a competitive final submission.

### Definition of Done (verifiable)
- [ ] `WINNER_MATRIX.md` exists and includes:
  - [ ] A complete **inventory** of in-scope EIP + Fisher winners discoverable from official Harvard CGA sources, with year, title, author(s), award, official source link, StoryMap/project link, and artifact status.
  - [ ] A clear **artifact status** field for each entry: `storymap:<url>` / `project:<url>` / `metadata-only` / `missing (BLOCKED)`.
  - [ ] For **≥ 6 publicly accessible winning submissions or closely associated official artifacts** (or all accessible entries if fewer than 6 exist), a filled feature-extraction section with **evidence-backed notes** tied to sections, screenshots, captions, or page/slide locators.
  - [ ] A consistent **winner rubric** applied to each accessible entry.
- [ ] `AWARD_PLAYBOOK.md` exists and includes:
  - [ ] A **checklist** of features to emulate organized by: framing/problem choice, StoryMap architecture, GIS/cartography, evidence/analysis, originality, and packaging/polish.
  - [ ] A **weighted scoring rubric** explicitly tuned to EIP + Fisher priorities.
  - [ ] **Concrete templates/snippets** for the StoryMap opening, question/answer block, methods sidecar, results sequence, case-study section, interpretation section, and closing / sources block.
  - [ ] A **map kit** section specifying which map types a submission should include and what each one must prove.
  - [ ] A **watch-outs** section listing failure modes and how to detect/fix them before submission.
  - [ ] Cross-references to `WINNER_MATRIX.md` exemplars for every major recommendation.
- [ ] `NOVELTY_METHODS_MEMO.md` exists and includes:
  - [ ] A ranked list of **Harvard-accessible data sources** relevant to originality, marked `high`, `medium`, or `low` feasibility.
  - [ ] A ranked list of **ArcGIS/Esri spatial analysis techniques** relevant to originality, each with required licenses/data and narrative payoff.
  - [ ] A shortlist of **3–5 originality packages** for the current project (each package = data + method + story payoff + risk).
  - [ ] A candid **do not chase** subsection listing impressive-but-misaligned ideas to avoid.
- [ ] `SUBMISSION_GAP_ANALYSIS.md` exists and includes:
  - [ ] A rubric-based score for the **current project** against the EIP + Fisher playbook.
  - [ ] A specific originality score and recommendation based on `NOVELTY_METHODS_MEMO.md`.
  - [ ] A prioritized list of **remaining submission tasks** grouped into: must-do, strong upgrades, optional polish.
  - [ ] A clear statement of what is already strong, what is weak, and what is missing.
- [ ] If any winner artifacts or licensed-source details are unavailable, the relevant deliverable contains a **BLOCKERS** subsection listing exactly what is missing and what access/input is needed.

### Non-goals (explicit)
- No claim that any single pattern or method **guarantees** a prize.
- No new large-scale causal analysis unless it is strictly required to fix a gap identified by the prize playbook.
- No broad expansion into non-geospatial Harvard prizes or discipline-specific thesis prizes.
- No full StoryMap build inside this job unless explicitly requested later; this job is the **prize-adaptation and submission-planning** layer.

---

## 2. Acceptance Checks

### Research / Synthesis checks
- [ ] Coverage check: inventory includes all reasonably discoverable official EIP + Fisher winners in scope, with official source links.
- [ ] Criteria alignment check: the rubric explicitly reflects official award / StoryMap judging language where available.
- [ ] Evidence discipline: each major feature claim in the matrix is tied to a specific artifact section, screenshot, caption, page, slide, or official judge comment.
- [ ] Public-interest check: playbook recommendations explicitly address problem framing, audience clarity, and practical significance.
- [ ] GIS check: playbook recommendations explicitly address geospatial design, map purpose, interaction, and data transparency.
- [ ] Originality check: novelty recommendations are grounded in accessible data/methods rather than vague “be more innovative” advice.

### Writing / Storytelling checks
- [ ] Playbook is actionable (checklists + templates + map specs, not just description).
- [ ] Rubric is usable: includes weights, score definitions, and what to fix when a score is low.
- [ ] No fluff: every major playbook section cites at least 2 exemplars from the matrix when possible.
- [ ] Readability check: recommendations explain how to keep the main narrative accessible while preserving technical credibility.

### Submission / Format checks
- [ ] All deliverables are valid Markdown, readable in GitHub renderer.
- [ ] Links work and IDs are consistent (`[EIP-YYYY-#]`, `[FIS-YYYY-UG-#]`, `[FIS-YYYY-G-#]`, etc.).
- [ ] Screenshots / quoted text stay brief and purpose-limited.
- [ ] `SUBMISSION_GAP_ANALYSIS.md` ends with a finite, ordered list of next actions.

---

## 3. Plan

### Approach summary (4-pass)
1) **Pass 1 — Winner inventory + evidence capture**  
   Build the official inventory of EIP + Fisher winners, collect accessible StoryMaps / project pages / award pages / judge comments, and extract recurring features using a structured template.
2) **Pass 2 — Synthesis into prize playbook**  
   Convert repeated patterns into a weighted rubric, checklist, StoryMap/report templates, map kit, and failure-mode library.
3) **Pass 3 — Novelty/originality scouting**  
   Inventory Harvard-accessible data sources and ArcGIS/Esri methods that could materially differentiate the project, then rank them by payoff and feasibility.
4) **Pass 4 — Gap analysis against the current project**  
   Score the current project against the playbook and convert gaps into a concrete finish plan.

### Dependencies / ordering logic
- Matrix scaffolding → official inventory → artifact acquisition status → winner feature extraction → playbook writing → novelty memo → current-project scoring → gap-analysis QA.

### Risks & mitigation
- **R1: Sparse or incomplete public archives for older winners.** Mitigate by tracking metadata-only entries and prioritizing fully accessible recent winners.
- **R2: Award criteria are partly implicit rather than formally published.** Mitigate by combining official criteria language with repeated winner-page/judge-comment patterns.
- **R3: Matrix becomes too descriptive and misses actionable build logic.** Mitigate by forcing every extracted feature to map to a concrete submission action.
- **R4: Overweighting writing and underweighting GIS implementation.** Mitigate by requiring a dedicated GIS/cartography lens and a map-kit deliverable.
- **R5: “Originality” becomes hand-wavy or infeasible.** Mitigate by ranking ideas by data access, software access, and story payoff.

---

## 4. Tasks (flat, atomic, verifiable)

- [ ] Create `WINNER_MATRIX.md` scaffold (root).  
  Done when: file contains (i) scope statement, (ii) inclusion rules, (iii) summary inventory table with defined columns, (iv) per-entry extraction template, (v) rubric section placeholder, (vi) BLOCKERS section placeholder.

- [ ] Create `AWARD_PLAYBOOK.md` scaffold (root).  
  Done when: file contains headings for (i) judging logic, (ii) feature checklist, (iii) weighted rubric, (iv) StoryMap/report templates, (v) map kit, (vi) failure modes, (vii) exemplar cross-reference convention.

- [ ] Create `NOVELTY_METHODS_MEMO.md` scaffold (root).  
  Done when: file contains headings for (i) Harvard-accessible sources, (ii) ArcGIS/Esri methods, (iii) originality packages, (iv) do-not-chase list, (v) blockers.

- [ ] Create `SUBMISSION_GAP_ANALYSIS.md` scaffold (root).  
  Done when: file contains headings for (i) current-project strengths, (ii) rubric scorecard, (iii) originality score, (iv) missing pieces, (v) prioritized next actions, (vi) blockers / assumptions.

- [ ] Define and write the **scope + inclusion rules** in `WINNER_MATRIX.md` (EIP winners, Fisher winners, official award pages, linked StoryMaps/projects, plus a small relevant benchmark set only if needed).  
  Done when: another reader could decide whether an entry belongs in scope without ambiguity.

- [ ] Populate official inventory: **EIP winners** (all publicly discoverable years) in the summary table.  
  Inputs: official Harvard CGA award/winner pages.  
  Done when: each entry has Award/Year/Author(s)/Title/Official-link/Artifact-link/Artifact-status.

- [ ] Populate official inventory: **Fisher winners** (all publicly discoverable years, undergraduate + graduate if applicable) in the summary table.  
  Inputs: official Harvard CGA award/winner pages.  
  Done when: same columns complete.

- [ ] Add a **criteria capture** section to `WINNER_MATRIX.md` summarizing the best-available official judging language for EIP/Fisher and relevant StoryMap criteria.  
  Done when: the file includes explicit criteria bullets with source links.

- [ ] Acquire accessible winner artifacts for **Batch 1 (3 entries)**, prioritizing recent winners with public StoryMaps/projects and visible judge comments. Update artifact-status fields.  
  Done when: 3 entries have accessible artifacts and any failures are logged in BLOCKERS.

- [ ] Complete feature extraction for **Batch 1 (3 entries)** in `WINNER_MATRIX.md`.  
  Done when: each entry has feature bullets across at least 6 lenses: framing, structure, GIS/cartography, evidence/analysis, originality, packaging/polish; and at least 6 evidence-backed notes.

- [ ] Acquire accessible winner artifacts for **Batch 2 (3 entries)** and update statuses.  
  Done when: statuses updated and blockers recorded.

- [ ] Complete feature extraction for **Batch 2 (3 entries)** in `WINNER_MATRIX.md`.  
  Done when: at least 6 entries total have full evidence-backed extractions, or all accessible entries are fully extracted if fewer than 6 exist.

- [ ] Write the **weighted EIP + Fisher rubric** into `AWARD_PLAYBOOK.md`.  
  Done when: rubric includes categories, weights, score definitions, and “if low, do this next” actions.

- [ ] Synthesize **framing + narrative architecture** recommendations in `AWARD_PLAYBOOK.md`, each backed by exemplars from `WINNER_MATRIX.md`.  
  Done when: recommendations cover hook, stakes, question/answer, methods reveal, results ordering, case studies, and conclusion.

- [ ] Synthesize **GIS/cartography + StoryMap implementation** recommendations in `AWARD_PLAYBOOK.md`, each backed by exemplars.  
  Done when: recommendations cover map purpose, interaction, sidecar usage, web-map choice, annotations, legends, accessibility, and data/source transparency.

- [ ] Produce the **template/snippet library** in `AWARD_PLAYBOOK.md`.  
  Done when: at least 10 reusable templates exist, including opening sidecar copy, “why this matters,” question/short answer block, methods sidecar, results sidecar, case-study module, interpretation block, and sources/credits close.

- [ ] Produce the **map kit** section in `AWARD_PLAYBOOK.md`.  
  Done when: it specifies the minimum map set for a competitive submission and states what each map must prove.

- [ ] Write the **watch-outs / failure modes** section in `AWARD_PLAYBOOK.md`.  
  Done when: at least 12 watch-outs exist, including overtechnical openings, weak map purpose, generic conclusions, hidden methods, underexplained outliers, and unfinished QA.

- [ ] Inventory **Harvard-accessible data sources** in `NOVELTY_METHODS_MEMO.md` (CGA/AGOL/Pro/Living Atlas/HGL/Map Collection/StreetMap Premium/Business Analyst/FASRC/NERC/CGA-developed datasets).  
  Done when: each source has access note, relevance, novelty payoff, and feasibility label.

- [ ] Inventory **ArcGIS/Esri methods** in `NOVELTY_METHODS_MEMO.md` (spatial statistics, space-time pattern mining, network/location-allocation, suitability analysis, predictive modeling, GeoAI/deep learning, 3D/CityEngine if relevant).  
  Done when: each method has required license/data, expected output, and narrative value.

- [ ] Propose **3–5 originality packages** for the current project in `NOVELTY_METHODS_MEMO.md`.  
  Done when: each package clearly states: what new question it answers, which data it needs, which tool/method it uses, why it is harder to replicate, and why it helps EIP/Fisher specifically.

- [ ] Score the **current project** against the rubric in `SUBMISSION_GAP_ANALYSIS.md`.  
  Inputs: current report, StoryMap blueprint, case-study plan, map spec, atlas outputs.  
  Done when: each rubric category has a score, rationale, and supporting evidence from current project artifacts.

- [ ] Convert the score into a **remaining-work plan** in `SUBMISSION_GAP_ANALYSIS.md`.  
  Done when: remaining tasks are split into `must-do`, `strong upgrade`, and `optional polish`, each with a clear rationale.

- [ ] QA pass: consistency + cross-links across all four deliverables.  
  Done when: all IDs resolve, criteria language matches, and no broken links or orphan recommendations remain.

- [ ] Final scope check: confirm inventory completeness and explicitly list unavailable winner artifacts or unavailable licensed-source details as BLOCKED.  
  Done when: the coverage limit of public discoverability/access is explicit and finite.

---

## 5. Worker Driver Prompt (job-specific)

You are the worker. Your job is to execute the Tasks in WORK.md in a tight loop until Definition of Done is satisfied.

Loop rules:
1) Read WORK.md at the start of every iteration.
2) Select the single highest-priority unblocked task.
3) Execute only what is needed for that task (no scope creep).
4) Update WORK.md immediately after execution:
   - Mark the task [x] only with evidence (file created/updated, links added, matrix entries filled, rubric sections written, etc.).
   - Append to **Results**: what changed + file paths + brief description.
   - Append to **Learnings**: any patterns, prize-fit insights, or process improvements discovered.
   - If new work is discovered, add only atomic tasks.

Tooling guidance:
- Use web browsing to retrieve official Harvard CGA award listings, winner pages, StoryMaps, relevant StoryMap judging criteria, and official/authoritative Harvard access pages for data/software.
- Prefer official sources first. If a referenced page is blocked or lacks detail, use the best-available authoritative secondary source and note that choice.
- When analyzing StoryMaps or project pages, cite precise sections, screenshots, captions, or visible textual locators.
- When evaluating novelty ideas, include a feasibility note and do **not** oversell anything as guaranteed to win.

Stop conditions:
- Stop when Definition of Done is fully satisfied, OR when progress is BLOCKED (and BLOCKERS clearly state what is needed from the user).

---

## 6. Learnings
- (empty)

---

## 7. Results
- (empty)
