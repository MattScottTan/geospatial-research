# 0. Snapshot
- Job Type: Mixed — Writing/Exposition + Research/Synthesis + Data/Visualization Packaging + Light Code.
- Run: Fisher Award food/geospatial project, Run 3 polished submission package.
- Primary Deliverables: final scope and claims memo; final Fisher-facing figure set; StoryMap-ready narrative; static report; methods appendix; data/source/limitations appendix; abstract and pitch; Pia review packet; final claim audit; submission checklist; reproducibility/package manifest.
- Stakeholders / Audience: Matthew Tan; Prof. Pia Sorensen as scientific mentor; Harvard Center for Geographic Analysis / Fisher Prize evaluators.
- Prior Inputs: completed Run 1, Run 2, and Run 2 v2 artifacts, especially `docs/run2v2_amended_prototype_interpretation.md`, `docs/run2v2_scope_lock_decision_memo.md`, `docs/run3_handoff_plan.md`, `figures/run2v2_*`, `data/processed/run2v2_*`, and `outputs/run2v2_*`.
- Final Scope: **Global discovery screen + East/Southeast Asia primary case + Iberian/Atlantic-Pacific secondary/diagnostic case**.
- Constraints: preserve Run 2 v2 scope discipline; do not widen into a new exploratory project; global results are discovery only; focused cases carry the main inference; no unsupported causal claims; no direct contact with Pia unless separately authorized; no secrets/API keys; no hosted ArcGIS StoryMap unless access is explicitly available; create StoryMap-ready copy and assets if hosting is unavailable; all factual claims and data claims must be cited or source-linked.

# 1. Goal
Convert the Run 2 v2 **Culinary Corridors** prototype into a polished Fisher Prize submission package. The final package should present food as spatial evidence: cuisines are represented as ingredient profiles, cuisine similarity is compared against geography, residual culinary corridors identify unexpectedly strong similarities, and focused geospatial cases show where spatial structure is clearest. The final argument must be ambitious enough for the Fisher Prize but conservative enough to withstand scrutiny: the global model screens for candidate corridors, while the East/Southeast Asia case and geospatial residual analyses support the strongest claims.

- Definition of Done:
  - `docs/run3_final_scope_and_claims.md` exists and separates strong conclusions, cautious hypotheses, and forbidden claims.
  - `outputs/run3_input_artifact_audit.csv` exists and confirms which Run 2 v2 artifacts are reused, superseded, excluded, or missing.
  - `docs/run3_figure_selection_memo.md` exists and selects the final Fisher figure set with rationale.
  - At least five final figures exist under `figures/final/`: global discovery, distance/residual model, East/Southeast Asia focused case, geospatial bridge/boundary insight, and secondary/sensitivity/limitations figure.
  - `figures/final/final_figure_captions.md` exists and gives data, method, interpretation, limitation, and role for each final figure.
  - `submission/storymap_script.md` exists and is ready to paste into an ArcGIS StoryMap or equivalent web-map-heavy submission.
  - `submission/fisher_submission_report.md` exists as a static report version for review/submission without StoryMap hosting.
  - `submission/technical_appendix.md` exists and documents the data pipeline, similarity methods, distance/residual model, focused cases, geospatial-only analyses, sensitivity checks, and reproducibility.
  - `submission/data_sources_and_limitations.md` exists and documents sources, license/usage risks, platform bias, cuisine-label limitations, mapping uncertainty, and non-causal interpretation.
  - `submission/abstract_and_pitch.md` exists with a 150–250 word abstract, 60–90 second oral pitch, and 2–3 sentence project description.
  - `submission/pia_review_packet.md` exists with targeted validation questions and exact scientific assumptions needing review. If Pia feedback is unavailable, final text must state that food-science interpretation is provisional.
  - `outputs/run3_claim_audit_checklist.md` exists and verifies that the final narrative does not overstate causality, representativeness, or cuisine-to-place precision.
  - `submission/final_submission_checklist.md` exists and lists all files, figures, appendices, blockers, and readiness status.
  - `outputs/run3_reproducibility_and_manifest.md` exists and lists scripts/data reused, figure inputs, package assumptions, and final artifact paths.
  - `WORK.md` Results and Learnings are updated after each worker iteration and at completion.
- Non-goals:
  - Do not redo Run 2 or Run 2 v2 from scratch.
  - Do not widen the project beyond the settled scope unless a required artifact is invalid or missing.
  - Do not build a production software package, CI workflow, or generalized reusable library.
  - Do not host an ArcGIS StoryMap unless credentials/access are explicitly available.
  - Do not centralize fermentation.
  - Do not centralize flavor chemistry unless fast validation and Pia review make it clearly defensible; otherwise treat it as future work or a brief sidebar.
  - Do not claim the recipe corpus is globally representative.
  - Do not claim migration, trade, colonialism, or maritime exchange caused observed similarities unless explicitly modeled and carefully qualified.
  - Do not overwrite Run 2 or Run 2 v2 artifacts; save final or revised outputs under `submission/`, `figures/final/`, or `run3_*` paths.

# 2. Acceptance Checks
- Writing/exposition checks:
  - Final narrative is award-facing, visually guided, and understandable to both GIS evaluators and a food-science mentor.
  - The project is framed as geospatial analysis, not a general food essay or decorative map project.
  - Global discovery is explicitly distinguished from focused inference.
  - Every major section connects to the central spatial question: when does cuisine similarity follow distance, and when does it follow corridors, bridges, regions, or boundaries?
  - Strong claims, cautious hypotheses, and forbidden claims are consistent across scope memo, StoryMap script, report, and appendices.
- Research/source checks:
  - All factual claims about Fisher, datasets, GIS methods, prior cuisine/food studies, or external data sources include source links or citation notes.
  - Dataset/license/platform-bias risks are explicit.
  - Novelty claims are conservative.
  - Pia-related claims are provisional unless user provides actual Pia feedback.
- Data/analysis checks:
  - Final analysis relies on existing Run 2 v2 outputs unless a documented defect requires a small correction.
  - Any new computation is limited to figure polishing, table extraction, caption support, or claim/summary generation.
  - Every final figure lists its input files and generation/manual-polish notes in `outputs/run3_reproducibility_and_manifest.md`.
  - The final figure set includes at least one insight that requires geospatial structure, such as residual bridge scores, focused spatial corridors, boundary/permeability, or path/connectivity proxy results.
- Code/visualization checks:
  - Any new or modified script runs from the project root using relative paths and writes only to `figures/final/`, `outputs/`, or `submission/` unless otherwise specified.
  - Figures are legible and consistently titled/captioned.
  - Original Run 2/Run 2 v2 figures are not overwritten.
  - No API tokens, credentials, or secrets appear in code, logs, markdown, or figures.
- Format/package checks:
  - The package is usable even without ArcGIS login: both `submission/storymap_script.md` and `submission/fisher_submission_report.md` are required.
  - All final deliverable paths listed in Results exist or are marked BLOCKED with exact missing input.
  - Final artifacts are Markdown/CSV/PNG and support files only; PDF/LaTeX is optional and must not block completion.

# 3. Plan
- Audit Run 2 v2 artifacts and lock the final evidence base before polishing.
- Freeze the final argument: global screen as discovery, East/Southeast Asia as primary inference, Iberian/Atlantic-Pacific as secondary/diagnostic, residual bridge/geospatial analysis as the key Fisher differentiator.
- Select and polish only the strongest figures; avoid noisy or redundant visuals.
- Build the submission narrative around: question → data representation → distance baseline → residual corridors → focused case → geospatial bridge/boundary insight → limitations.
- Prepare appendices so the main narrative stays readable while methods, data caveats, and reproducibility remain credible.
- Prepare a Pia review packet and a claim audit so food-science and causal language remain disciplined.
- Package the final materials for either ArcGIS StoryMap construction or static review.
- Dependencies / ordering logic: artifact audit precedes figure selection; scope/claims memo precedes narrative writing; final figures precede captions; captions precede StoryMap/report text; appendices precede final checklist; claim audit precedes completion.
- Risk & mitigation:
  - If final data-license status remains unclear, include a visible usage-risk note and recommend substitution or permission check before public posting.
  - If a figure is visually weak or noisy, demote it to appendix or exclude it.
  - If Pia feedback is unavailable, keep food-science claims provisional and include exact questions for later validation.
  - If ArcGIS StoryMap access is unavailable, deliver StoryMap-ready script and asset instructions.
  - If the final package feels too broad, prioritize East/Southeast Asia + residual bridge scores and use the global/secondary cases as supporting context.

# 4. Tasks
- [ ] [S01] Create `outputs/run3_setup_note.md` — Inputs needed: `docs/run2v2_amended_prototype_interpretation.md`, `docs/run2v2_scope_lock_decision_memo.md`, `docs/run3_handoff_plan.md`, and this `WORK.md`. Done when: the file states Run 3’s purpose, final scope, inherited evidence base, non-goals, and immediate risks.
- [ ] [A01] Create `outputs/run3_input_artifact_audit.csv` — Inputs needed: Run 2 v2 artifacts under `docs/`, `data/processed/`, `outputs/`, and `figures/`. Done when: each required input artifact is listed with path, exists/missing status, reuse/exclude/supersede decision, and notes.
- [ ] [R01] Create `docs/run3_final_scope_and_claims.md` — Inputs needed: `docs/run2v2_scope_lock_decision_memo.md` and `docs/run2v2_amended_prototype_interpretation.md`. Done when: the file defines final title, central research question, final scope, strong conclusions, cautious hypotheses, forbidden claims, and one-paragraph thesis.
- [ ] [R02] Create `docs/run3_fisher_positioning_memo.md` — Inputs needed: Run 1 award/winner brief if available, `docs/fisher_project_blueprint.md`, and Run 2 v2 outputs. Done when: the file explains why the project fits Fisher, emphasizing spatial necessity, GIS insight, visual clarity, interdisciplinarity, and credibility.
- [ ] [V01] Create `docs/run3_figure_selection_memo.md` — Inputs needed: all `figures/run2*.png`, `figures/run2v2*.png`, captions, and summaries. Done when: the file selects main figures, appendix figures, excluded figures, and gives a reason for each decision.
- [ ] [V02] Create `figures/final/final_global_discovery_figure.png` — Inputs needed: selected global heatmap/residual/distance figure source from V01 and underlying data if needed. Done when: a final global-discovery figure exists, is legible, and is labeled as discovery rather than proof.
- [ ] [V03] Create `figures/final/final_distance_or_residual_model_figure.png` — Inputs needed: Run 2 v2 filtered distance/residual outputs and original distance plot if reused. Done when: a final figure shows the distance baseline, residual logic, or observed-vs-predicted structure clearly.
- [ ] [V04] Create `figures/final/final_east_southeast_asia_case_figure.png` — Inputs needed: `figures/run2v2_east_southeast_asia_case_map.png`, `data/processed/run2v2_focus_case_results.csv`, and coordinate crosswalk. Done when: a final focused-case figure exists and highlights East/Southeast Asia as the primary inference case.
- [ ] [V05] Create `figures/final/final_geospatial_bridge_or_boundary_figure.png` — Inputs needed: `figures/run2v2_residual_bridge_score_map.png`, `figures/run2v2_geospatial_method_comparison.png`, and/or geospatial-only output tables. Done when: a final figure shows residual bridge scores, boundary/permeability, path/connectivity proxy, or another geospatial-only insight.
- [ ] [V06] Create `figures/final/final_secondary_or_sensitivity_figure.png` — Inputs needed: Iberian/Atlantic-Pacific case map, sensitivity summary, or data-quality outputs. Done when: a final secondary/diagnostic figure exists or the task is marked BLOCKED/excluded with a documented reason in V01.
- [ ] [V07] Create `figures/final/final_figure_captions.md` — Inputs needed: all completed final figures and original Run 2 v2 captions. Done when: every final figure has a polished caption with data, method, interpretation, limitation, and role in the argument.
- [ ] [W01] Create `submission/storymap_outline.md` — Inputs needed: `docs/run3_final_scope_and_claims.md`, `docs/run3_figure_selection_memo.md`, and final figure captions. Done when: the file gives StoryMap section order, each section’s purpose, intended figure placement, and transitions.
- [ ] [W02] Create `submission/storymap_script.md` — Inputs needed: `submission/storymap_outline.md`, final figures, captions, and scope/claims memo. Done when: the file contains complete StoryMap-ready prose with headings, body text, figure placement notes, captions, and callouts.
- [ ] [W03] Create `submission/fisher_submission_report.md` — Inputs needed: `submission/storymap_script.md`, final captions, and appendices if available. Done when: the file is a static report version with title, abstract placeholder, introduction, data, methods, results, focused cases, limitations, conclusion, and references/source notes.
- [ ] [W04] Create `submission/abstract_and_pitch.md` — Inputs needed: `submission/storymap_script.md` and `docs/run3_final_scope_and_claims.md`. Done when: the file includes a 150–250 word abstract, a 60–90 second oral pitch, and a 2–3 sentence ultra-short description.
- [ ] [M01] Create `submission/technical_appendix.md` — Inputs needed: Run 2/Run 2 v2 scripts, summaries, model outputs, and reproducibility logs. Done when: the appendix documents data preparation, ingredient normalization, cuisine-to-place mapping, similarity metrics, distance model, residual computation, focused cases, geospatial-only analyses, and sensitivity checks.
- [ ] [M02] Create `submission/data_sources_and_limitations.md` — Inputs needed: `data/run2_data_access_log.md`, `data/raw/recipe_source_manifest.md`, `data/run2v2_data_quality_audit.md`, and source manifests. Done when: the appendix documents datasets used, usage/license risks, data quality limitations, platform bias, cuisine-label caveats, mapping uncertainty, and what the project cannot claim.
- [ ] [M03] Create `submission/references.md` — Inputs needed: all source links from Run 1–Run 2 v2 artifacts and final narrative source notes. Done when: the file lists all cited datasets, methods sources, Harvard/Fisher sources, and relevant literature/source pages in a consistent format.
- [ ] [P01] Create `submission/pia_review_packet.md` — Inputs needed: final scope memo, top final figures, ingredient policy, final interpretation, and flavor-chemistry decision. Done when: the packet contains a one-page summary, figure list, food-science assumptions, 8–12 targeted questions for Pia, and a concise email draft the user can send.
- [ ] [P02] Create `outputs/run3_pia_feedback_status.md` — Inputs needed: `submission/pia_review_packet.md` and any user-provided Pia feedback. Done when: the file states whether Pia feedback was available, what was incorporated if available, and which claims remain provisional if feedback is unavailable.
- [ ] [Q01] Create `outputs/run3_claim_audit_checklist.md` — Inputs needed: `submission/storymap_script.md`, `submission/fisher_submission_report.md`, `docs/run3_final_scope_and_claims.md`, and limitations appendix. Done when: the checklist verifies each major claim as strong/cautious/forbidden-safe, flags overclaiming, and records required edits.
- [ ] [W05] Revise `submission/storymap_script.md` after claim audit — Inputs needed: `outputs/run3_claim_audit_checklist.md`. Done when: the script is updated so every flagged overclaim is corrected or justified.
- [ ] [W06] Revise `submission/fisher_submission_report.md` after claim audit — Inputs needed: `outputs/run3_claim_audit_checklist.md`. Done when: the report is updated so every flagged overclaim is corrected or justified.
- [ ] [F01] Create `submission/final_submission_checklist.md` — Inputs needed: all final submission artifacts and final figures. Done when: the checklist lists required deliverables, readiness status, unresolved blockers, recommended submission format, and exact next manual steps for the user.
- [ ] [F02] Create `outputs/run3_reproducibility_and_manifest.md` — Inputs needed: all Run 3 files, final figures, reused scripts, and data inputs. Done when: the file lists final artifacts, input dependencies, commands or manual steps used, package assumptions, and known reproducibility caveats.
- [ ] [Q02] Update `WORK.md` Results section with final Run 3 artifact checklist — Inputs needed: all completed Run 3 artifacts. Done when: Results lists every created artifact path, verification status, key final scope decision, blocked items, and exact missing inputs.
- [ ] [Q03] Update `WORK.md` Learnings section with Run 3 pitfalls and recommendations — Inputs needed: all completed artifacts and errors encountered. Done when: Learnings records claim discipline, figure selection lessons, source limitations, StoryMap/report packaging lessons, and final recommendations for submission.

# 5. Worker Driver Prompt
You are the worker for **Run 3** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition.

This is a polishing and submission-packaging run, not another broad exploratory analysis. Preserve Run 2 and Run 2 v2 outputs unless a task explicitly creates a final copy under `figures/final/`, `submission/`, or a `run3_*` path. Do not widen the scope beyond global discovery + East/Southeast Asia primary case + Iberian/Atlantic-Pacific secondary/diagnostic case unless an input artifact is invalid and a narrow correction is necessary.

After each iteration, update `WORK.md` immediately: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, commands/manual steps, outputs, and verification status; record Learnings with pitfalls, source issues, figure decisions, claim decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing input/access/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If ArcGIS StoryMap access is unavailable, create StoryMap-ready script and asset instructions rather than attempting to host. If Pia feedback is unavailable, keep food-science validation provisional and record the exact questions for later review.

Use the acceptance checks for a Mixed writing/research/data/visualization job. All factual claims and dataset claims need source links or citation notes. All final figures need captions and documented inputs. All final interpretive language must be conservative: global results are discovery, focused cases support stronger but non-causal inference, and migration/trade/colonial/maritime interpretations remain hypotheses unless directly modeled.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, state whether the Fisher submission package is ready, which format is recommended, which figures should be used, which claims are safe, and what exact manual steps the user must take next.

# 6. Learnings

# 7. Results
