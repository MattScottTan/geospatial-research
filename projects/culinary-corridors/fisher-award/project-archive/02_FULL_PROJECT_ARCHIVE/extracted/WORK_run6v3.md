# 0. Snapshot
- Job Type: Mixed — Writing/Exposition + StoryMap/Submission Packaging + Claim/Sources QA.
- Run: Fisher Award **Run 6 v3 — Regional Balance and Non-Asia Diagnostic Expansion** for the Culinary Corridors project.
- Primary Deliverables: regionally rebalanced expanded StoryMap script; revised paste blocks; revised build order; mandatory non-Asia diagnostic section/vignette; “why Europe is diagnostic, not primary” explanation; updated figure/section manifest; revised claim-safety and readability audits; updated QA checklist and WORK.md log.
- Stakeholders / Audience: Matthew Tan; Harvard Center for Geographic Analysis / Fisher Prize reviewers; Prof. Pia Sorensen or other advisors reviewing the final StoryMap.
- Prior Inputs:
  - Current Run 6 v2 expanded StoryMap package under `submission/storymap_conversion_v2/`, especially `storymap_expanded_copy_paste_script.md`, `storymap_expanded_build_order.md`, `storymap_expanded_outline.md`, `storymap_expanded_figure_manifest.csv`, `storymap_case_vignettes.md`, `storymap_findings_sections.md`, `storymap_expanded_sources_and_limitations.md`, `storymap_expanded_final_qa_checklist.md`, and section paste blocks.
  - Current final figures, especially `run4_hero_spatial_argument_figure.png`, `run4_method_or_model_figure.png`, `run4_primary_case_figure.png`, `run5_east_se_asia_topographic_corridor_map.png`, `run4_geospatial_insight_figure.png`, and `run4_secondary_or_limitations_figure.png`.
  - Existing final reports and claim audits, especially the final complete PDF/report and Run 6 v2 claim/readability audits.
- Constraints:
  - This run is a StoryMap balance/revision run, not a new analysis run.
  - Do not create new statistics, figures, models, or external datasets unless an existing artifact is missing and a narrow documented fallback is necessary.
  - Preserve the approved claim hierarchy: global = discovery; East/Southeast Asia = primary focused inference; Iberian/Atlantic-Pacific = required secondary/diagnostic case; Europe/Atlantic-linked material = diagnostic/supporting, not a full inference case; topography = spatial context; residual bridge index = strongest geospatial-only insight.
  - Make the StoryMap feel less Asia-only while preserving the methodological reason East/Southeast Asia is the strongest focused case.
  - Do not claim a full Europe-specific regional analysis unless supported by existing outputs. Use “non-Asia diagnostic,” “Iberian/Atlantic-Pacific,” and “secondary comparison” language rather than overbuilding unsupported European claims.
  - Do not host, publish, or submit the StoryMap. Produce copy-paste revision materials only.
  - No secrets/API keys. No external credentials.

# 1. Goal
Revise the Run 6 v2 expanded StoryMap package so the final Fisher submission does not feel overly Asia-driven. The worker should preserve East/Southeast Asia as the strongest focused inference case, but rebalance the narrative by making the global discovery layer more substantive, renaming the Asia section to emphasize methodological selection, adding a mandatory non-Asia diagnostic section/vignette based on Iberian/Atlantic-Pacific residuals, explicitly explaining why Europe/Atlantic-linked material is diagnostic rather than the primary case, and updating build order, paste blocks, manifests, claim audits, and QA materials accordingly. The final result should read as a global GIS method with a focused Asian case and a credible non-Asia diagnostic comparison, not as an Asia-only cuisine project.

## Definition of Done
- [ ] `outputs/run6v3_setup_note.md` exists and states why Run 6 v3 exists, what imbalance it corrects, what remains unchanged, and what must not be overclaimed.
- [ ] `outputs/run6v3_input_artifact_audit.csv` exists and confirms availability/reuse status for Run 6 v2 StoryMap artifacts, final figures, final PDF/report, secondary/limitations figure, claim audits, and paste blocks.
- [ ] `docs/run6v3_regional_balance_strategy.md` exists and states the revised presentation strategy: global screen is substantive, East/Southeast Asia is the primary focused case, Iberian/Atlantic-Pacific is mandatory diagnostic comparison, Europe is not elevated to unsupported primary inference.
- [ ] `submission/storymap_conversion_v3/storymap_balanced_outline.md` exists and updates the StoryMap section sequence, target word counts, figure placement, callouts, transitions, and required caveats.
- [ ] `submission/storymap_conversion_v3/storymap_balanced_copy_paste_script.md` exists and contains the full revised StoryMap text, ready to paste into ArcGIS StoryMaps, with exact headings, body text, figure placement notes, captions, callouts, and source/limitation notes.
- [ ] `submission/storymap_conversion_v3/storymap_section_paste_blocks/` exists with one Markdown file per section, each separating **PASTE TEXT** from **EDITOR NOTE / FIGURE INSTRUCTION**.
- [ ] The revised script includes a more substantive global discovery section that makes clear the project begins globally and uses East/Southeast Asia as a selected focused case, not as the entire project.
- [ ] The revised script renames/reframes the Asia section using language like **“From global screen to focused case: why East/Southeast Asia carries the strongest inference.”**
- [ ] The revised script includes a mandatory non-Asia diagnostic section using the Iberian/Atlantic-Pacific case, with careful language about hypothesis generation and data limitations.
- [ ] The revised script includes a direct paragraph or callout explaining why Europe/Atlantic-linked material remains diagnostic rather than becoming the main focused inference case.
- [ ] The revised script includes at least one mandatory non-Asia vignette, preferably Iberian/Atlantic-Pacific, Spanish–Brazilian, Spanish–Mexican, or another supported residual pattern from existing materials. If exact pair evidence is unavailable, the section must be phrased at the case-family level and marked as diagnostic.
- [ ] `submission/storymap_conversion_v3/storymap_balanced_figure_manifest.csv` exists and updates the figure manifest with revised section placement, captions, alt text, “what to notice,” source notes, and limitation notes.
- [ ] `submission/storymap_conversion_v3/storymap_balanced_build_order.md` exists and gives exact ArcGIS build instructions, block types, figure placement, and paste order for the rebalanced version.
- [ ] `submission/storymap_conversion_v3/storymap_balanced_callouts.md` exists and includes revised callouts for global discovery, methodological case selection, non-Asia diagnostic comparison, and Europe/Atlantic caution.
- [ ] `outputs/run6v3_claim_safety_audit.md` exists and verifies the revised text does not overclaim Europe-specific analysis, non-Asia causality, global representativeness, cuisine-to-place precision, or causal historical mechanisms.
- [ ] `outputs/run6v3_storymap_readability_audit.md` exists and checks whether the revised script feels balanced, explanatory, and navigable.
- [ ] `submission/storymap_conversion_v3/storymap_balanced_final_qa_checklist.md` exists and gives pre-submission checks for regional balance, figure order, captions, claim hierarchy, desktop/mobile display, PDF backup, and final form submission.
- [ ] `outputs/run6v3_reproducibility_and_manifest.md` exists and records reused inputs, generated outputs, manual steps, skipped/blocked items, and final artifact paths.
- [ ] `WORK.md` Results and Learnings are updated after every worker iteration and at completion.

## Non-goals
- Do not run new recipe/ingredient analysis.
- Do not create new model outputs or new maps unless required input files are missing and a narrow documented substitute is necessary.
- Do not invent Europe-specific findings or numerical results.
- Do not make Europe a second primary focused case unless existing artifacts already support it.
- Do not demote East/Southeast Asia from the primary focused case; instead, explain why it was selected methodologically.
- Do not add unsupported historical claims about trade, migration, empire, colonialism, maritime exchange, or food diffusion.
- Do not hide limitations or move them only to the end.
- Do not host, publish, or submit the StoryMap.

# 2. Acceptance Checks

## Regional Balance Checks
- The final StoryMap must not read as Asia-only. It must clearly communicate:
  - the project starts with a global residual screen;
  - East/Southeast Asia is a selected focused case because it is analytically strongest;
  - at least one non-Asia diagnostic case is discussed substantively;
  - Europe/Atlantic-linked material is included but treated cautiously.
- The global discovery section must do more than introduce the hero map. It must explain how the full cuisine set motivated case selection.
- The East/Southeast Asia section must be framed as a methodological narrowing from a global screen, not as the project’s preselected subject.
- The non-Asia diagnostic section must be mandatory, not optional.
- A direct explanation must address why Europe or Europe-linked residuals are not elevated to the same inferential status as East/Southeast Asia.

## Claim Safety Checks
- Strong claims may include: cuisine similarity is spatially structured; distance explains part but not all similarity; residuals identify candidate corridors; East/Southeast Asia is the strongest focused case; residual bridge scores require GIS/spatial residuals; the Run 5 relief map makes corridor geography legible.
- Cautious claims may include: Iberian/Atlantic-Pacific residuals are suggestive; selected non-Asia links are consistent with long-distance exchange or maritime/Atlantic-Pacific geographies; Europe/Atlantic-linked material generates hypotheses for future work.
- Forbidden claims must not appear: the model proves migration/trade/colonialism/topography caused similarity; the corpus represents all world cuisines; cuisine labels map cleanly to nation-states; residual links are historical routes; Europe has been fully analyzed as a focused regional case if the evidence is not present.
- Any claim about a specific non-Asia pair must be supported by existing outputs or softened to a case-family/diagnostic claim.

## StoryMap Structure Checks
- The revised StoryMap must preserve the approved expanded atlas-style rhythm:
  - opening hook;
  - problem framing;
  - research question;
  - how the atlas works;
  - global discovery;
  - distance/residual method;
  - focused case;
  - topographic/corridor context;
  - residual bridge index;
  - non-Asia diagnostic case;
  - limitations and claim discipline;
  - sources/PDF backup.
- Each major section must include what to look at, what it means, why it matters spatially, and what it does not prove.
- Text must remain copy-paste-ready and modular.

## Figure and Visual Checks
- The final required figure sequence must remain:
  1. `run4_hero_spatial_argument_figure.png`
  2. `run4_method_or_model_figure.png`
  3. `run4_primary_case_figure.png`
  4. `run5_east_se_asia_topographic_corridor_map.png`
  5. `run4_geospatial_insight_figure.png`
  6. `run4_secondary_or_limitations_figure.png`
- The secondary/limitations figure must be explicitly used to support the non-Asia diagnostic section or the limits of extending beyond the primary case.
- If the optional inset is used, it must not further increase Asia imbalance unless balanced by non-Asia text.

## Source and Operations Checks
- Use only existing source notes, final reports, outputs, and figure materials unless a new source is necessary for an editorial claim.
- If a needed statistic or pair ranking is not present in existing materials, do not invent it; use qualitative phrasing or mark `[SOURCE CHECK NEEDED]`.
- The build-order document must tell Matthew exactly what to paste where.
- The section paste blocks must be numbered and named in order.
- The QA checklist must include a specific “regional balance test.”

# 3. Plan
- Audit Run 6 v2 materials and identify where Asia emphasis is strongest.
- Write a short regional-balance strategy before editing so the revision is principled rather than cosmetic.
- Update the outline to make the global discovery section more substantive and make the non-Asia diagnostic case mandatory.
- Revise the full copy-paste script with four targeted changes:
  1. strengthen global-discovery framing;
  2. reframe East/Southeast Asia as a selected focused case;
  3. add/expand the Iberian/Atlantic-Pacific diagnostic section and vignette;
  4. add a “why not Europe as primary?” explanation.
- Update paste blocks, build order, figure manifest, and callouts to match the revised sequence.
- Run claim-safety and readability/regional-balance audits.
- Produce final QA checklist and manifest.

## Dependencies / Ordering Logic
1. Setup note and input audit precede all writing.
2. Regional-balance strategy precedes outline and script changes.
3. Revised outline precedes full revised script.
4. Full revised script precedes paste-block generation.
5. Figure manifest/build order/callouts must match the revised script.
6. Claim-safety audit precedes final script revision.
7. Readability/regional-balance audit precedes final QA checklist.
8. Reproducibility manifest and WORK.md updates come last.

## Risk & Mitigation
- Risk: The revision falsely implies a full Europe analysis. Mitigation: required diagnostic language and claim audit.
- Risk: The StoryMap becomes too long. Mitigation: keep the non-Asia diagnostic section focused and modular.
- Risk: Asia remains visually dominant because of the topographic map. Mitigation: explain that the project is global by method and focused by inference, and place non-Asia diagnostic material after bridge scores.
- Risk: Non-Asia examples are under-supported. Mitigation: use “diagnostic,” “hypothesis-generating,” and “candidate” language, or mark `[SOURCE CHECK NEEDED]`.
- Risk: Multiple StoryMap versions become confusing. Mitigation: save all outputs under `submission/storymap_conversion_v3/` and create a clear build-order file.

# 4. Tasks
- [ ] [S01] Create `outputs/run6v3_setup_note.md` — Inputs needed: Run 6 v2 outputs, final figures, final PDF/report, and this `WORK.md`. Done when: the file states Run 6 v3’s purpose, the Asia-balance concern, inherited scope, non-goals, and main risks.
- [ ] [A01] Create `outputs/run6v3_input_artifact_audit.csv` — Inputs needed: Run 6 v2 StoryMap files, section paste blocks, final figures, final PDF/report, final claim/readability audits, and secondary/limitations figure. Done when: each required artifact is listed with path, exists/missing status, role, reuse/revise/exclude decision, and blocker note if missing.
- [ ] [R01] Create `docs/run6v3_regional_balance_strategy.md` — Inputs needed: Run 6 v2 expanded script, figure manifest, and current concern about Asia-heavy presentation. Done when: the file states the regional-balance problem, desired revised hierarchy, required editorial moves, forbidden moves, and final success criteria.
- [ ] [W01] Create `submission/storymap_conversion_v3/storymap_balanced_outline.md` — Inputs needed: R01, Run 6 v2 outline, build order, and figure sequence. Done when: the outline lists every final section with goal, figure, callout, target word count, transition, required caveat, and whether it is global, primary, diagnostic, or limitation.
- [ ] [W02] Create `submission/storymap_conversion_v3/storymap_balanced_copy_paste_script.md` — Inputs needed: Run 6 v2 expanded script, W01, R01, final report, and claim hierarchy. Done when: the full revised StoryMap script exists with exact headings, PASTE TEXT, EDITOR NOTE, figure placement notes, captions, and the required regional-balance changes.
- [ ] [W03] Create `submission/storymap_conversion_v3/storymap_section_paste_blocks/` — Inputs needed: W02. Done when: the directory contains one numbered Markdown file per StoryMap section, each with paste text and editor instructions.
- [ ] [W04] Create `submission/storymap_conversion_v3/storymap_non_asia_diagnostic_section.md` — Inputs needed: W02 and existing secondary/diagnostic materials. Done when: the file contains a standalone mandatory non-Asia diagnostic section and vignette, with careful diagnostic language and figure placement instructions.
- [ ] [W05] Create `submission/storymap_conversion_v3/storymap_why_not_europe_primary_note.md` — Inputs needed: W02, R01, existing limitations/source notes. Done when: the file contains a ready-to-paste paragraph/callout explaining why Europe/Atlantic-linked material is diagnostic rather than the primary focused inference case.
- [ ] [F01] Create `submission/storymap_conversion_v3/storymap_balanced_figure_manifest.csv` — Inputs needed: Run 6 v2 figure manifest and revised outline. Done when: the manifest lists every figure with revised section placement, caption, short caption, expanded caption, alt text, what-to-notice note, source note, limitation note, and regional role.
- [ ] [W06] Create `submission/storymap_conversion_v3/storymap_balanced_build_order.md` — Inputs needed: W01, W02, F01. Done when: the file gives exact ArcGIS build instructions, block types, figure placement, section ordering, optional/mandatory notes, and paste sequence.
- [ ] [W07] Create `submission/storymap_conversion_v3/storymap_balanced_callouts.md` — Inputs needed: W02, W04, W05, claim hierarchy. Done when: the file contains callouts for global discovery, focused-case selection, non-Asia diagnostic comparison, Europe/Atlantic caution, geospatial contribution, and final takeaway.
- [ ] [Q01] Create `outputs/run6v3_claim_safety_audit.md` — Inputs needed: W02, W04, W05, F01, and claim hierarchy. Done when: each major claim is classified as strong/cautious/unsafe; unsafe/ambiguous language is listed with required edits; Europe/non-Asia overclaiming is specifically checked.
- [ ] [W08] Revise `submission/storymap_conversion_v3/storymap_balanced_copy_paste_script.md` after Q01 — Inputs needed: Q01. Done when: all flagged overclaims or ambiguous phrases are corrected or explicitly justified.
- [ ] [Q02] Create `outputs/run6v3_storymap_readability_audit.md` — Inputs needed: revised W02, W01, and word counts if available. Done when: the audit checks section length, figure-led pacing, modularity, regional balance, and whether the non-Asia diagnostic material is sufficient.
- [ ] [F02] Create `submission/storymap_conversion_v3/storymap_balanced_word_counts.csv` — Inputs needed: revised W02 and paste blocks. Done when: approximate word count by section and total are recorded with a note on regional balance.
- [ ] [F03] Create `submission/storymap_conversion_v3/storymap_balanced_final_qa_checklist.md` — Inputs needed: W06, Q01, Q02, F01. Done when: the checklist gives exact pre-submission QA steps, including regional balance test, claim hierarchy test, figure display, captions, sources, PDF backup, mobile/desktop, incognito/private access, and final form submission.
- [ ] [F04] Create `outputs/run6v3_reproducibility_and_manifest.md` — Inputs needed: all Run 6 v3 outputs and reused inputs. Done when: the manifest records input artifacts, generated outputs, manual steps, skipped/blocked tasks, and final artifact paths.
- [ ] [Q03] Update `WORK.md` Results section with final Run 6 v3 artifact checklist — Inputs needed: all completed Run 6 v3 artifacts. Done when: Results lists every created artifact path, verification status, skipped/blocked tasks, final build order, and exact manual next steps.
- [ ] [Q04] Update `WORK.md` Learnings section with Run 6 v3 lessons and final recommendations — Inputs needed: all completed artifacts and any issues encountered. Done when: Learnings records regional-balance lessons, non-Asia diagnostic lessons, claim-safety lessons, StoryMap pacing lessons, and final recommendations.

# 5. Worker Driver Prompt
You are the worker for **Run 6 v3 — Regional Balance and Non-Asia Diagnostic Expansion** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition.

This is a StoryMap revision and balance run, not a new analysis run. Preserve all existing figures, analyses, reports, and the approved claim hierarchy. The objective is to make the expanded StoryMap feel less Asia-only while preserving East/Southeast Asia as the strongest focused inference case. Do this by strengthening the global discovery layer, reframing East/Southeast Asia as a selected focused case, making the Iberian/Atlantic-Pacific/non-Asia diagnostic case mandatory, and adding a clear explanation of why Europe/Atlantic-linked material remains diagnostic rather than primary.

Do not invent new numerical results or historical mechanisms. If a non-Asia pair or Europe-linked claim is not clearly supported by existing materials, use cautious case-family language or mark `[SOURCE CHECK NEEDED]` and list it in the claim audit. Do not claim a full Europe-specific analysis unless the existing artifacts support it.

After each iteration, immediately update `WORK.md`: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, outputs, and verification status; record Learnings with regional-balance decisions, claim decisions, figure-placement decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing file/input/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, list the exact files Matthew should open, the final ArcGIS build order, the section paste-block directory, how the non-Asia diagnostic section should be used, and the manual QA steps before submission.

# 6. Learnings

# 7. Results
