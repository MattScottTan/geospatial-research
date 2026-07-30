# 0. Snapshot
- Job Type: Mixed — Research/Synthesis + Writing/Exposition + competition strategy/operations.
- Primary Deliverables: a Fisher Award strategy packet consisting of:
  - `outputs/fisher_award_playbook.md`
  - `outputs/feature_matrix.md`
  - `outputs/scoring_rubric.md`
  - `outputs/production_timeline.md`
  - `outputs/topic_scoring_template.md`
- Stakeholders / Audience:
  - Immediate audience: a worker agent executing this plan.
  - End user: a Harvard student preparing to maximize competitiveness for the Howard T. Fisher Prize in Geographic Information Science.
  - Final judge/audience proxy: Harvard Center for Geographic Analysis / Fisher Prize reviewers.
- Constraints:
  - Do not produce the actual Fisher submission poster, PDF, or StoryMap.
  - Markdown deliverables are required; tabular feature matrices may use Markdown tables and may also be structured so they can be exported later to CSV/Excel if needed.
  - Use the Fisher Prize rules and criteria provided by the user as authoritative baseline instructions.
  - Use the prior conversation’s summarized past-winner inventory as a seed list, but mark it preliminary until verified.
  - Where web access is available, verify Fisher criteria and past winners against official Harvard/CGA pages first; use public winner pages/profiles only for gaps.
  - Submission rules to preserve in the playbook: poster must be 42” x 36”, PDF format, no more than 350 words of descriptive text excluding legends/labels/title/citations/captions; alternatively a Story Map website may be submitted.
  - Deadline to preserve in the playbook: Sunday, May 3, 2026 at 11:59 p.m.
  - Registration/submission process to preserve in the playbook: register through Fisher page using HarvardKey; after registration confirmation, submit poster PDF or StoryMap URL by email to Jeff Blossom at `jblossom@cga.harvard.edu` before the deadline.
  - Official Fisher judging criteria to preserve exactly as the five core axes:
    1. Innovation and creativity of chosen topic
    2. Use of GIS in performing the project
    3. Data — complexity, relevance to topic, properly documented
    4. Analytical approach and execution
    5. Visualization / cartographic communication effectiveness

# 1. Goal
Create a competition-grade Fisher Award playbook and feature matrix that reverse-engineer publicly traceable past winners and the official Fisher criteria into an actionable strategy packet. The packet should help a future worker or student maximize award competitiveness by choosing or shaping a GIS project around spatial necessity, strong analytical execution, complex/relevant/documented data, and high-impact cartographic communication. The packet should not choose a topic or create the actual submission; it should provide the rules, scoring system, tactical playbook, production timeline, and reusable topic-evaluation template needed to guide winning-oriented execution.

## Definition of Done
- [ ] `outputs/fisher_award_playbook.md` exists and contains a competition-grade strategy for maximizing Fisher Prize competitiveness.
- [ ] `outputs/feature_matrix.md` exists and contains all required matrices: past-winner feature matrix, Fisher-criteria tactics matrix, winning-archetype matrix, and poster-vs-StoryMap format strategy matrix.
- [ ] `outputs/scoring_rubric.md` exists and contains a weighted internal scoring rubric that covers all five official Fisher criteria and includes gate checks for spatial necessity and compliance.
- [ ] `outputs/production_timeline.md` exists and back-schedules work to the May 3, 2026 11:59 p.m. deadline, including registration, review, QA, and submission checkpoints.
- [ ] `outputs/topic_scoring_template.md` exists and can be used later to evaluate candidate Fisher topics without needing additional structure.
- [ ] Every deliverable directly supports Fisher Prize competitiveness and avoids generic GIS advice.
- [ ] The five official Fisher criteria appear verbatim or near-verbatim in the packet and are operationalized into tactical checks.
- [ ] The packet includes the required submission constraints: 42” x 36” poster size, PDF format, 350-word descriptive text cap, StoryMap alternative, registration requirement, submission email, and deadline.
- [ ] Past-winner analysis includes every publicly traceable winner/year from the baseline inventory below, with source/confidence status for each row and explicit “unknown/unverified” labels where evidence is incomplete.
- [ ] The feature matrix identifies repeatable winner patterns and converts each pattern into concrete “upgrade moves.”
- [ ] The final packet includes no actual Fisher poster, StoryMap, or topic-specific selection.
- [ ] `WORK.md` is updated with completed tasks, Results, and Learnings after every iteration.

## Non-goals
- Do not create the actual Fisher poster.
- Do not create a StoryMap.
- Do not select between the user’s two candidate topics.
- Do not invent unsupported past-winner facts; mark uncertain historical details as unknown, preliminary, or unverified.
- Do not assume HarvardKey access, registration completion, eligibility, or submission confirmation.
- Do not create files outside `outputs/` except updates to `WORK.md` unless a new atomic task is added first.

# 2. Acceptance Checks

## Research / Synthesis Checks
- The packet must use the user-provided Fisher rules and criteria as baseline source material.
- If web access is available, official Harvard/CGA sources must be checked before secondary sources for current Fisher rules and winner records.
- Any discrepancy between user-provided rules and official pages must be recorded in the relevant deliverable and in `WORK.md#6. Learnings`.
- Past-winner rows must include: year, winner(s), category when known, project title/topic when known, domain, likely GIS method, data complexity/relevance, analytical approach, visualization/cartographic angle, apparent winning feature, source type, confidence level, and “emulate/avoid” note.
- Source confidence levels must be one of: `Official`, `Public secondary`, `Profile/CV`, `Prior-summary only`, or `Unknown`.
- Claims about “what wins” must be tied either to Fisher criteria or to repeated patterns in the past-winner matrix.
- Novelty claims must be framed cautiously: recommend ways to create novelty rather than asserting that a topic is objectively novel unless evidence supports it.
- Missing historical data must be explicitly labeled; do not fill gaps with guesses.

## Writing / Exposition Checks
- Deliverables must be written in Markdown.
- Writing must be operational and concise: every section should help a worker make or improve a Fisher submission.
- The playbook must prioritize “spatial necessity”: the project should be difficult or impossible to execute convincingly without GIS.
- The playbook must include concrete examples drawn from past-winner patterns, not abstract strategy alone.
- The packet must be organized for worker execution: clear headings, checklists, rubrics, matrices, and upgrade moves.
- The tone should be strategic and competition-focused, not merely descriptive.

## Operations / Competition Checks
- The production timeline must include explicit checkpoints for:
  - registration confirmation
  - data freeze
  - analysis freeze
  - draft map/poster/StoryMap review
  - 350-word text audit if poster route is used
  - source/citation audit
  - export/format QA
  - submission email before deadline
- The scoring rubric must include a compliance gate before quality scoring.
- The final QA checklist must include failure modes that could cause rejection: wrong poster size, non-PDF poster, over-word-limit descriptive text, missing registration, late submission, undocumented data, weak GIS role, unclear cartography.
- The topic scoring template must make it possible to evaluate candidate topics later without rewriting the playbook.

# 3. Plan

## Approach Summary
- Build a self-contained strategy packet that translates Fisher’s five judging criteria into a practical winner-optimization system.
- Use prior past-winner analysis as a baseline inventory, then require verification and confidence labels rather than unsupported certainty.
- Treat the feature matrix as the core strategic artifact: it should reveal what winners have in common and convert those patterns into tactics.
- Build an aggressive competition strategy around judge-visible strengths: originality, spatial necessity, nontrivial GIS execution, data rigor, analytical clarity, and visual communication.
- Separate general award strategy from later topic-specific evaluation; the current packet should not choose a topic.
- Include deadline-driven operational planning so the eventual submission is compliant, reviewed, and submitted on time.

## Dependencies / Ordering Logic
1. Capture source rules and baseline winner inventory before creating scoring or strategy.
2. Build `feature_matrix.md` first because it supplies evidence and patterns for the playbook and rubric.
3. Build `scoring_rubric.md` after the feature matrix so weights and gates reflect both Fisher criteria and winner patterns.
4. Build `fisher_award_playbook.md` after the matrix and rubric so the advice is evidence-based and actionable.
5. Build `production_timeline.md` after the playbook so milestones reflect actual deliverables and deadline constraints.
6. Build `topic_scoring_template.md` last so it inherits the rubric, matrices, and playbook logic.
7. Finish by cross-checking all files against the Definition of Done and acceptance checks.

## Baseline Past-Winner Inventory to Verify
Use this as a preliminary seed list only. Verification and confidence tagging are required before relying on any row.

- 2025: Quinn Ewanchyna, undergraduate; Aanchal Chopra, graduate. Ewanchyna topic seed: “Fighting for Power: Natural Resources and Rebel Legitimacy …”. Chopra title unknown in baseline.
- 2024: Shane Rice, undergraduate; Dev Patel and Issam Azzam, graduate/co-winners. Topic seeds: Finding Anfal / Iraq-Kurdistan settlement destruction; Detecting Floods with machine learning and satellite data; Fragmentation / design and counter-design in Palestine.
- 2023: Beatrice Youd, undergraduate; Bora Ju, graduate. Topic seeds: conservation in Republic of Congo; pre/post-war Mariupol spatial change.
- 2022: Layal Merhi, Olivia Poston, Thanaporn Lam, Inkoo Kang. Topic seed: Cities [re]defined.
- 2021: Thandi Nyambose. Topic seed: Harlem, NYC African American Design Nexus.
- 2020: Emilio Sempris. Topic seed: World On Fire / top jurisdictions with wildfire.
- 2019: Longfeng Wu and Seung Kyum Kim. Topic seed: unequal access to urban green spaces.
- 2018: Jennifer Horowitz, undergraduate; Yousef Awaad Hussein, graduate. Topic seeds: Iraqi Marshes ecocide; Territory, Survey, Cartography.
- 2017: Melissa Balding; Oliver Curtis; Brian Ho. Topic seeds partly unknown; Curtis/Ho may relate to dry West/fire/ecosystem simulation.
- 2016: Heidi Mayer Hurst. Topic seed: FEMA Disaster Recovery Centers.
- 2015: Lydia Gaby, undergraduate; Nathanial Erb-Satullo, graduate. Topic seeds: storm surge risk in Lower East Side/Chinatown; ancient metal production in South Caucasus.
- 2014: Leif Estrada; Jake Sobstyl. Topic seeds: Alameda Island temporal morphology/sea-level rise; thermal energy audits.
- 2013: Tanya Petach. Topic seed: Earth History in Death Valley.
- 2012 / 2011–12: Dongsei Kim; Dustin Duncan. Topic seeds: Korean DMZ as urbanism; obesogenic neighborhood environments.
- 2009: Shubha Lakshmi Bhat; Alisha Holland. Topic seeds: iodized salt and child health in India; crime and Conservative Party politics in El Salvador.
- 2007: Corina Graif and possibly other winners. Topic seed: creative class and diversity in Chicago neighborhoods.
- 2006: Frances C. Moore. Topic seed: causal factors of Nepal’s Maoist insurgency.
- 2005: Lee T. Murray; Heather Joan Lynch. Topic titles unknown in baseline.
- 2000–01: Scott Bassett, graduate; Irina Harris, undergraduate. Topic seeds: San Pedro River Basin species richness/visual preference; archaeological GIS/3D visualization for Bezymiannaya, Ukraine.

## Risk & Mitigation
- Risk: Past-winner history is incomplete or inconsistently public.
  - Mitigation: Use confidence labels, source-type labels, and explicit unknowns in the matrix.
- Risk: The packet becomes generic GIS advice.
  - Mitigation: Require every tactic to map to a Fisher criterion or a past-winner pattern.
- Risk: Internal scoring overweights unofficial assumptions.
  - Mitigation: Keep official Fisher criteria visible and distinguish official criteria from internal optimization heuristics.
- Risk: Timeline is too compressed because deadline is May 3, 2026.
  - Mitigation: Timeline must include fast-track and minimum-viable compliance checkpoints.
- Risk: The playbook encourages sophisticated methods without feasibility checks.
  - Mitigation: Include data/method feasibility gates and “complexity with control” guidance.
- Risk: Later topic evaluation may be needed but topics are intentionally out of scope now.
  - Mitigation: Build a reusable `topic_scoring_template.md` instead of scoring actual topics.

# 4. Tasks

- [ ] [R] Create the output directory. Done when: `outputs/` exists. Where: project root. Inputs needed: filesystem access.
- [ ] [R] Create the initial feature matrix shell. Done when: `outputs/feature_matrix.md` exists with headings for `Source Rules`, `Past-Winner Feature Matrix`, `Fisher-Criteria Tactics Matrix`, `Winning Archetype Matrix`, and `Poster vs StoryMap Strategy Matrix`. Where: `outputs/feature_matrix.md`. Inputs needed: `WORK.md`.
- [ ] [R] Add source rules to the feature matrix. Done when: `outputs/feature_matrix.md#Source Rules` defines source-type labels, confidence labels, and rules for unknown/unverified details. Where: `outputs/feature_matrix.md#Source Rules`. Inputs needed: `WORK.md#2. Acceptance Checks`.
- [ ] [R] Add Fisher rules and criteria to the feature matrix. Done when: `outputs/feature_matrix.md#Source Rules` or equivalent section includes deadline, submission format constraints, registration/submission process, and all five judging criteria. Where: `outputs/feature_matrix.md`. Inputs needed: user-provided Fisher instructions in `WORK.md#0. Snapshot`.
- [ ] [R] Verify current Fisher rules against official Harvard/CGA sources. Done when: `outputs/feature_matrix.md` records whether official Fisher criteria match the user-provided criteria and logs any discrepancy. Where: `outputs/feature_matrix.md#Source Rules`. Inputs needed: web access to official Harvard/CGA Fisher page; BLOCKED if web access is unavailable.
- [ ] [R] Build the past-winner feature matrix. Done when: `outputs/feature_matrix.md#Past-Winner Feature Matrix` contains one row for every baseline winner/year listed in `WORK.md#3. Plan`, including source type and confidence. Where: `outputs/feature_matrix.md#Past-Winner Feature Matrix`. Inputs needed: baseline inventory in `WORK.md#3. Plan`; official/public sources if available.
- [ ] [R] Add missing-data notes to the past-winner matrix. Done when: every unknown or unverified winner/title/method is explicitly labeled and no blank cells remain. Where: `outputs/feature_matrix.md#Past-Winner Feature Matrix`. Inputs needed: completed past-winner matrix.
- [ ] [R] Create the Fisher-criteria tactics matrix. Done when: `outputs/feature_matrix.md#Fisher-Criteria Tactics Matrix` maps each of the five official criteria to high-scoring evidence, low-scoring red flags, tactical upgrade moves, and relevant past-winner examples. Where: `outputs/feature_matrix.md#Fisher-Criteria Tactics Matrix`. Inputs needed: Fisher criteria and past-winner matrix.
- [ ] [R] Create the winning archetype matrix. Done when: `outputs/feature_matrix.md#Winning Archetype Matrix` identifies repeatable winner archetypes such as conflict/territory, climate/disaster/environmental risk, urban inequality/access, historical/archaeological reconstruction, and remote sensing/ML/computational GIS. Where: `outputs/feature_matrix.md#Winning Archetype Matrix`. Inputs needed: past-winner matrix.
- [ ] [R] Create the poster-vs-StoryMap strategy matrix. Done when: `outputs/feature_matrix.md#Poster vs StoryMap Strategy Matrix` compares both formats on compliance, visual storytelling, analytical depth, risk, timeline, and best-use cases. Where: `outputs/feature_matrix.md#Poster vs StoryMap Strategy Matrix`. Inputs needed: Fisher submission requirements.
- [ ] [W] Create the scoring rubric shell. Done when: `outputs/scoring_rubric.md` exists with headings for `Compliance Gate`, `Spatial Necessity Gate`, `Weighted Score`, `Tie-Breakers`, and `Interpretation Bands`. Where: `outputs/scoring_rubric.md`. Inputs needed: `outputs/feature_matrix.md`.
- [ ] [W] Add the compliance gate to the scoring rubric. Done when: `outputs/scoring_rubric.md#Compliance Gate` lists all submission conditions that must pass before quality scoring. Where: `outputs/scoring_rubric.md#Compliance Gate`. Inputs needed: Fisher submission requirements.
- [ ] [W] Add the spatial necessity gate to the scoring rubric. Done when: `outputs/scoring_rubric.md#Spatial Necessity Gate` defines pass/fail tests proving GIS is essential rather than decorative. Where: `outputs/scoring_rubric.md#Spatial Necessity Gate`. Inputs needed: feature matrix and Fisher GIS-use criterion.
- [ ] [W] Add the weighted internal score to the scoring rubric. Done when: `outputs/scoring_rubric.md#Weighted Score` assigns weights totaling 100 across the five Fisher criteria and explains why the internal weights maximize competitiveness. Where: `outputs/scoring_rubric.md#Weighted Score`. Inputs needed: Fisher criteria and tactics matrix.
- [ ] [W] Add tie-breakers and interpretation bands to the scoring rubric. Done when: `outputs/scoring_rubric.md` defines score bands, tie-breaker logic, and minimum recommended threshold for submission readiness. Where: `outputs/scoring_rubric.md#Tie-Breakers` and `#Interpretation Bands`. Inputs needed: weighted internal score.
- [ ] [W] Create the playbook shell. Done when: `outputs/fisher_award_playbook.md` exists with headings for `Winning Thesis`, `Spatial Necessity`, `Topic Strategy`, `GIS Method Strategy`, `Data Strategy`, `Analytical Execution`, `Visualization Strategy`, `Narrative Strategy`, `Review Protocol`, `Red Flags`, and `Final QA`. Where: `outputs/fisher_award_playbook.md`. Inputs needed: `outputs/feature_matrix.md` and `outputs/scoring_rubric.md`.
- [ ] [W] Write the winning thesis section. Done when: `outputs/fisher_award_playbook.md#Winning Thesis` states the central strategy for maximizing Fisher competitiveness in one concise section. Where: `outputs/fisher_award_playbook.md#Winning Thesis`. Inputs needed: feature matrix patterns and Fisher criteria.
- [ ] [W] Write the spatial necessity section. Done when: `outputs/fisher_award_playbook.md#Spatial Necessity` provides tests and examples for making GIS indispensable to the project argument. Where: `outputs/fisher_award_playbook.md#Spatial Necessity`. Inputs needed: scoring rubric spatial gate.
- [ ] [W] Write the topic strategy section. Done when: `outputs/fisher_award_playbook.md#Topic Strategy` explains how to shape a topic for innovation, creativity, social/scientific significance, and judge-visible originality without selecting an actual topic. Where: `outputs/fisher_award_playbook.md#Topic Strategy`. Inputs needed: Fisher innovation criterion and winning archetype matrix.
- [ ] [W] Write the GIS method strategy section. Done when: `outputs/fisher_award_playbook.md#GIS Method Strategy` gives a method escalator from weak mapping to stronger spatial analysis, with examples of upgrade moves. Where: `outputs/fisher_award_playbook.md#GIS Method Strategy`. Inputs needed: Fisher GIS-use criterion and past-winner method patterns.
- [ ] [W] Write the data strategy section. Done when: `outputs/fisher_award_playbook.md#Data Strategy` specifies how to demonstrate data complexity, relevance, documentation, provenance, preprocessing, and uncertainty. Where: `outputs/fisher_award_playbook.md#Data Strategy`. Inputs needed: Fisher data criterion.
- [ ] [W] Write the analytical execution section. Done when: `outputs/fisher_award_playbook.md#Analytical Execution` specifies what counts as strong execution, including reproducibility, validation, sensitivity checks, and defensible interpretation. Where: `outputs/fisher_award_playbook.md#Analytical Execution`. Inputs needed: Fisher analytical approach criterion.
- [ ] [W] Write the visualization strategy section. Done when: `outputs/fisher_award_playbook.md#Visualization Strategy` gives cartographic communication tactics for both poster and StoryMap routes. Where: `outputs/fisher_award_playbook.md#Visualization Strategy`. Inputs needed: Fisher visualization criterion and poster-vs-StoryMap matrix.
- [ ] [W] Write the narrative strategy section. Done when: `outputs/fisher_award_playbook.md#Narrative Strategy` includes a poster narrative structure that can fit within the 350-word descriptive-text cap and a StoryMap narrative alternative. Where: `outputs/fisher_award_playbook.md#Narrative Strategy`. Inputs needed: Fisher format constraints.
- [ ] [W] Write the review protocol section. Done when: `outputs/fisher_award_playbook.md#Review Protocol` defines how to run advisor/GIS mentor reviews using the rubric and matrices. Where: `outputs/fisher_award_playbook.md#Review Protocol`. Inputs needed: scoring rubric.
- [ ] [W] Write the red flags section. Done when: `outputs/fisher_award_playbook.md#Red Flags` lists common ways a Fisher submission can be weak or noncompetitive and the corresponding fixes. Where: `outputs/fisher_award_playbook.md#Red Flags`. Inputs needed: acceptance checks and scoring rubric.
- [ ] [W] Write the final QA section. Done when: `outputs/fisher_award_playbook.md#Final QA` contains a pre-submission checklist covering compliance, source documentation, GIS role, analysis, visuals, and submission logistics. Where: `outputs/fisher_award_playbook.md#Final QA`. Inputs needed: Fisher submission requirements and scoring rubric.
- [ ] [O] Create the production timeline shell. Done when: `outputs/production_timeline.md` exists with headings for `Deadline`, `Fast-Track Schedule`, `Review Checkpoints`, `Submission Checklist`, and `Contingency Plan`. Where: `outputs/production_timeline.md`. Inputs needed: Fisher deadline and submission requirements.
- [ ] [O] Add the fast-track schedule. Done when: `outputs/production_timeline.md#Fast-Track Schedule` back-schedules work from May 3, 2026 at 11:59 p.m. and includes data freeze, analysis freeze, draft review, final export, registration, and email submission steps. Where: `outputs/production_timeline.md#Fast-Track Schedule`. Inputs needed: deadline and current date; use April 28, 2026 unless the execution environment provides a different current date.
- [ ] [O] Add the contingency plan. Done when: `outputs/production_timeline.md#Contingency Plan` explains how to reduce scope while preserving compliance and competitiveness if time is limited. Where: `outputs/production_timeline.md#Contingency Plan`. Inputs needed: fast-track schedule.
- [ ] [W] Create the topic scoring template shell. Done when: `outputs/topic_scoring_template.md` exists with headings for `Topic Summary`, `Spatial Necessity`, `Data Feasibility`, `GIS Method`, `Analytical Plan`, `Visualization Plan`, `Winner-Archetype Fit`, `Rubric Score`, `Risks`, and `Upgrade Moves`. Where: `outputs/topic_scoring_template.md`. Inputs needed: scoring rubric and playbook.
- [ ] [W] Add reusable scoring prompts to the topic template. Done when: each section of `outputs/topic_scoring_template.md` contains fill-in prompts, scoring fields, and evidence requirements for future candidate topics. Where: `outputs/topic_scoring_template.md`. Inputs needed: scoring rubric and feature matrix.
- [ ] [W] Add cross-links across the strategy packet. Done when: each deliverable links to the other four deliverables where relevant. Where: all files in `outputs/`. Inputs needed: completed deliverables.
- [ ] [W] Run the Definition of Done audit. Done when: every Definition of Done item in `WORK.md#1. Goal` is checked against the created files and any gap is converted into a new atomic task or marked BLOCKED. Where: `WORK.md#1. Goal` and `WORK.md#4. Tasks`. Inputs needed: all deliverables.
- [ ] [W] Run the acceptance-check audit. Done when: every applicable acceptance check in `WORK.md#2. Acceptance Checks` is either satisfied or has a new atomic task/blocker recorded. Where: `WORK.md#2. Acceptance Checks` and `WORK.md#4. Tasks`. Inputs needed: all deliverables.
- [ ] [O] Record final results. Done when: `WORK.md#7. Results` lists the completed files, key decisions, known source gaps, and any remaining blockers. Where: `WORK.md#7. Results`. Inputs needed: completed audits.

# 5. Worker Driver Prompt

You are executing a Fisher Award strategy-packet project. Start every iteration by reading `WORK.md` in full. Then pick the highest-priority unblocked task from `WORK.md#4. Tasks` and execute only that task. Do not create the actual Fisher poster, StoryMap, or submission. Do not choose the user’s candidate topic. Do not add broad scope beyond the strategy packet.

For each iteration:
1. Read `WORK.md`.
2. Select the highest-priority unchecked task that is not BLOCKED.
3. Execute that single task tightly.
4. Apply the acceptance checks relevant to the task type:
   - For research tasks, prioritize the user-provided Fisher rules, then official Harvard/CGA sources if accessible, then public secondary evidence for gaps; label confidence and unknowns.
   - For writing tasks, keep content strategic, concrete, Markdown-native, and directly tied to Fisher competitiveness.
   - For operations tasks, preserve exact deadline, format, registration, and submission constraints.
5. Update `WORK.md` before stopping the iteration:
   - Mark the completed task `[x]`.
   - Add a concise entry to `WORK.md#7. Results` describing what changed and the path/section changed.
   - Add a concise entry to `WORK.md#6. Learnings` for any pitfall, evidence gap, discrepancy, or pattern discovered.
   - Add new tasks only when necessary, and make each new task atomic, verifiable, and tied to a concrete file/path/section.
6. Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED.
7. If blocked, record the missing input, blocked task, and safest next action in `WORK.md#7. Results`.

Keep the work competition-focused: the goal is a practical playbook, feature matrix, rubric, timeline, and topic-scoring template that maximize Fisher Prize competitiveness under the official criteria.

# 6. Learnings


# 7. Results

