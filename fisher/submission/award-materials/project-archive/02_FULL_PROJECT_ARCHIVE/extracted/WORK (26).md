# 0. Snapshot
- Job Type: Mixed — Writing/Exposition + Research/Synthesis + StoryMap/Submission Packaging + Claim/Sources QA.
- Run: Fisher Award **Run 6 v2 — Expanded Atlas-Style StoryMap Content** for the Culinary Corridors project.
- Primary Deliverables: expanded copy-paste-ready ArcGIS StoryMap script; atlas-style section outline; section-by-section paste blocks; comprehensive explanations for each figure/finding; cuisine-pair vignettes; expanded methods explainer; expanded limitations/sources section; figure/caption/callout/alt-text package; claim-safety audit; final build and QA checklist.
- Stakeholders / Audience: Matthew Tan; Harvard Center for Geographic Analysis / Fisher Prize reviewers; Prof. Pia Sorensen or other advisors reviewing the final project.
- Prior Inputs:
  - Guideline exemplar: `Cloudy with a Chance of Compute.pdf`, especially its long-form StoryMap structure: concrete opening contrast, “How the atlas works,” numbered findings, statistical/method explanation, case studies, conclusion, and sources.
  - Current concise Run 6 conversion artifacts under `submission/storymap_conversion/`, especially `storymap_copy_paste_script.md`, `storymap_build_order.md`, `storymap_figure_manifest.csv`, `storymap_callout_boxes.md`, `storymap_source_and_limitations_panel.md`, `storymap_final_qa_checklist.md`, and `storymap_one_page_submission_summary.md`.
  - Final report and figures, especially `report/final_complete/culinary_corridors_complete_final_report.pdf`, `submission/final_committee/final_committee_report.md`, `figures/final_revised/run4_hero_spatial_argument_figure.png`, `figures/final_revised/run4_method_or_model_figure.png`, `figures/final_revised/run4_primary_case_figure.png`, `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`, `figures/final_revised/run4_geospatial_insight_figure.png`, and `figures/final_revised/run4_secondary_or_limitations_figure.png`.
  - Run 5 specification/results, especially the rule that the Run 5 topographic/corridor map should be inserted after the East/Southeast Asia focused-case section and described as spatial/relief context, not a causal topographic model.
- Constraints:
  - This is a writing/conversion expansion run, not a new analysis run.
  - Do not redo data processing, statistical modeling, geospatial analysis, or figure generation.
  - Do not invent new numerical results. Any statistic, coefficient, count, rank, or pair result must be copied from an existing report/output or omitted/phrased qualitatively.
  - Preserve the final claim hierarchy: global = discovery; East/Southeast Asia = primary focused inference; Iberian/Atlantic-Pacific = secondary/diagnostic; topography = spatial context; residual bridge index = strongest geospatial-only insight.
  - Produce StoryMap-ready text that is comprehensive enough to stand alone without the PDF, but still visually paced and sectioned for ArcGIS StoryMaps.
  - Use the *Cloudy with a Chance of Compute* StoryMap only as a structural/depth model; do not copy its subject matter, wording, statistics, or citations.
  - Use cautious language. Do not claim causality from migration, trade, colonialism, terrain, maritime routes, or cuisine history unless the existing project explicitly supports and qualifies that claim.
  - Do not host or publish the StoryMap. Produce copy-paste materials only.
  - No secrets/API keys. No external credentials.

# 1. Goal
Create an expanded, atlas-style ArcGIS StoryMap content package for **Culinary Corridors** that is substantially more comprehensive than the current concise Run 6 copy-paste script. The final output should let Matthew build the StoryMap by copying and pasting section-by-section text into ArcGIS Online. It should follow the depth and explanatory rhythm of the provided *Cloudy with a Chance of Compute* example: opening hook, problem framing, staged methods, numbered findings, detailed figure explanations, focused case vignettes, limitations, sources, and final contribution. The expanded StoryMap should read as a complete Fisher submission on its own, with the PDF acting as technical backup.

## Definition of Done
- [ ] `outputs/run6v2_setup_note.md` exists and explains why Run 6 v2 exists, how it differs from Run 6, what the exemplar teaches, and what must not be changed.
- [ ] `outputs/run6v2_input_artifact_audit.csv` exists and confirms availability/reuse status for the exemplar PDF, current StoryMap package, final report, figures, captions, callouts, source notes, claim audits, and PDF backup.
- [ ] `docs/run6v2_exemplar_style_takeaways.md` exists and extracts 8–12 specific structural lessons from `Cloudy with a Chance of Compute.pdf` that should guide Culinary Corridors, including opening contrast, atlas-method section, findings, case vignettes, limitations, and sources.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_outline.md` exists and defines the final expanded StoryMap sequence with section goals, target word counts, figures, callouts, and transitions.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_copy_paste_script.md` exists and contains the full expanded StoryMap text, ready to paste into ArcGIS StoryMaps. It must include exact headings, body text, figure placement notes, captions, callouts, and source/limitation notes.
- [ ] `submission/storymap_conversion_v2/storymap_section_paste_blocks/` exists with one Markdown file per StoryMap section, each containing only the text and figure instructions for that section.
- [ ] `submission/storymap_conversion_v2/storymap_methods_atlas_section.md` exists and gives a comprehensive “How the culinary atlas works” section with staged explanations for recipe profiles, similarity, geography, residuals, focused cases, and topographic/corridor context.
- [ ] `submission/storymap_conversion_v2/storymap_findings_sections.md` exists and gives expanded finding-by-finding explanations for global discovery, distance/residual logic, East/Southeast Asia, topographic corridor context, residual bridge index, and secondary/diagnostic case.
- [ ] `submission/storymap_conversion_v2/storymap_case_vignettes.md` exists and contains at least three cuisine-pair vignettes: Thai–Vietnamese, Chinese–Korean, and Filipino maritime/island bridge; optional fourth Iberian/Atlantic-Pacific vignette if supported by existing materials.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_figure_manifest.csv` exists and lists each figure with upload order, section, role, display recommendation, expanded caption, alt text, “what to notice,” source note, and limitation note.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_callouts.md` exists and contains polished callouts for research question, method, key finding, caution, geospatial contribution, and final takeaway.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_sources_and_limitations.md` exists and gives a comprehensive but StoryMap-suitable source, methods, and limitations section.
- [ ] `submission/storymap_conversion_v2/storymap_pdf_backup_and_submission_note.md` exists and explains where to link or mention the PDF backup in the StoryMap and submission form.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_build_order.md` exists and gives precise ArcGIS StoryMap build instructions, including recommended block types, sidecar/panel use, figure placement, and copy-paste order.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_word_counts.csv` exists and reports approximate word counts by section and total, with a note on whether the final is appropriately comprehensive or too long.
- [ ] `outputs/run6v2_claim_safety_audit.md` exists and verifies that the expanded text does not overclaim causality, global representativeness, cuisine-to-place precision, or topographic mechanism.
- [ ] `outputs/run6v2_storymap_readability_audit.md` exists and checks whether sections are sufficiently explanatory but still navigable as a StoryMap.
- [ ] `submission/storymap_conversion_v2/storymap_expanded_final_qa_checklist.md` exists and gives exact pre-submission checks for figure order, captions, alt text, sources, PDF backup, desktop/mobile display, and submission-form readiness.
- [ ] `outputs/run6v2_reproducibility_and_manifest.md` exists and records reused inputs, generated outputs, manual steps, package assumptions, skipped/blocked items, and final artifact paths.
- [ ] `WORK.md` Results and Learnings are updated after every worker iteration and at completion.

## Non-goals
- Do not create new analysis, new figures, new models, or new data sources.
- Do not revise the project’s central thesis unless existing materials contain a contradiction that must be reconciled.
- Do not rewrite the project into a conventional paper; it must remain a StoryMap/atlas narrative.
- Do not copy language from `Cloudy with a Chance of Compute.pdf`; use it only as a structural/depth guide.
- Do not add unsupported historical claims about trade, migration, empire, colonialism, maritime exchange, or food diffusion.
- Do not hide limitations or move them only to the end; relevant caveats should appear near the methods and figures they qualify.
- Do not describe the Run 5 relief map as proving terrain, coastlines, or maritime routes caused cuisine similarity.
- Do not treat cuisine labels as exact countries or the recipe corpus as globally representative.
- Do not host, publish, or submit the StoryMap.

# 2. Acceptance Checks

## StoryMap Depth and Structure Checks
- The expanded StoryMap must be substantially more explanatory than the Run 6 script and closer in depth to the provided exemplar.
- The opening must include a concrete hook/contrast, not just an abstract thesis.
- The StoryMap must include a staged “How the culinary atlas works” section analogous in function to the exemplar’s method scaffold.
- The StoryMap must include numbered or clearly labeled findings, each with: method context, figure explanation, result, interpretation, limitation, and why the result is spatial.
- The StoryMap must include at least three short cuisine-pair vignettes that move from global/focused patterns to concrete examples.
- Each major figure must be explained in 300–700 words across body text + caption + “what to notice” callout, unless the section is intentionally brief.
- The final expanded script should target approximately 5,000–7,500 words total. If it exceeds that range, `outputs/run6v2_storymap_readability_audit.md` must justify why; if it is below 5,000 words, the audit must flag sections needing expansion.
- The final text must remain scannable with short paragraphs, section breaks, callouts, and figure-led pacing.

## Required Final Section Order
The expanded copy-paste script must include, at minimum, these sections:
1. Cover / title / subtitle / author note.
2. Opening contrast and introduction.
3. Research question and subquestions.
4. Why food can be treated as spatial data.
5. How the culinary atlas works.
6. Global discovery screen.
7. Finding 1: distance matters, but incompletely.
8. Finding 2: residuals reveal candidate culinary corridors.
9. Finding 3: East/Southeast Asia is the strongest focused case.
10. Finding 4: terrain, coastlines, islands, and maritime space make the corridor legible.
11. Finding 5: residual bridge scores identify spatial bridge roles.
12. Cuisine-pair vignettes: Thai–Vietnamese, Chinese–Korean, Filipino maritime/island bridge, and optional secondary diagnostic vignette.
13. Secondary / diagnostic case and sensitivity.
14. What this proves and what it does not prove.
15. Sources, methods, and reproducibility.
16. Conclusion and final contribution.
17. PDF backup / technical report note.

## Figure and Visual Checks
- The expanded figure manifest must include the approved final sequence:
  1. `run4_hero_spatial_argument_figure.png`
  2. `run4_method_or_model_figure.png`
  3. `run4_primary_case_figure.png`
  4. `run5_east_se_asia_topographic_corridor_map.png`
  5. `run4_geospatial_insight_figure.png`
  6. `run4_secondary_or_limitations_figure.png`
- Optional `run5_corridor_callout_or_inset.png` may be included only if it improves clarity and does not clutter the StoryMap.
- Every figure must have: expanded caption, brief caption option, alt text, “what to notice” notes, source/method note, limitation note, and placement recommendation.
- The Run 5 topographic map must be framed as relief/coastal/spatial context, not a causal route model.
- The residual bridge-index figure must be framed as the strongest geospatial-only insight.

## Claim Safety Checks
- Strong claims may include: cuisine similarity is spatially structured; distance explains part but not all similarity; residuals identify candidate corridors; East/Southeast Asia is the strongest focused case; residual bridge scores require GIS/spatial residuals; the Run 5 relief map makes corridor geography legible.
- Cautious claims may include: selected patterns are consistent with regional adjacency, exchange, maritime/coastal context, corridor plausibility, or historical movement, provided the language remains non-causal.
- Forbidden claims must not appear: the model proves migration/trade/colonialism/topography caused similarity; the corpus represents all world cuisines; cuisine labels map cleanly to nation-states; residual links are historical routes; the relief map is a least-cost/topographic causal model.
- The limitations must mention recipe-platform bias, cuisine-label coarseness, ingredient-normalization uncertainty, generic ingredient filtering, cuisine-to-place mapping uncertainty, non-causality, and topography-as-context.

## Source and Citation Checks
- All dataset and method claims must be backed by existing sources/notes from the final report or Run 6 package.
- If a claim lacks a source in existing materials, the worker must either remove it, weaken it, or mark `[SOURCE CHECK NEEDED]` in the copy-paste script and list it in the claim audit.
- The final sources section must include data sources, methods/tools, final PDF backup, and a brief note on AI/tool assistance if present in the existing project materials.
- Do not add new citations that were not checked or already present in existing materials unless they are from the provided PDF/sample or existing source files.

## Operations / ArcGIS Checks
- The build-order document must tell Matthew exactly what to paste where and which figures to upload in what order.
- Each section paste block must separate **PASTE TEXT** from **EDITOR NOTE / FIGURE INSTRUCTION** so it is easy to use.
- The expanded text must be modular: Matthew should be able to omit a vignette or optional figure without breaking the whole StoryMap.
- The QA checklist must include desktop/mobile view, incognito/private link test, figure readability, source links, PDF backup, claim discipline, and final submission-form check.

# 3. Plan
- Audit all required inputs and confirm the final figure sequence from Run 6/Run 5.
- Analyze the provided exemplar only for structure, pacing, depth, and section function; translate those lessons into a Culinary Corridors-specific expansion plan.
- Create an expanded outline that maps each StoryMap section to a figure, finding, callout, limitation, and target word count.
- Draft a full expanded copy-paste script that gives each figure and finding enough explanation to stand alone.
- Write standalone section paste blocks so Matthew can copy and paste one section at a time into ArcGIS Online.
- Add cuisine-pair vignettes to make the project more concrete and closer to the exemplar’s place-based case studies.
- Expand methods, limitations, and sources so the StoryMap is self-contained and not dependent on the PDF.
- Run claim-safety and readability audits; revise the copy-paste script if any overclaiming or under-explained sections are found.
- Package final build order, manifests, QA checklist, and reproducibility notes.

## Dependencies / Ordering Logic
1. Setup note and input artifact audit precede all writing.
2. Exemplar style takeaways precede expanded outline.
3. Expanded outline precedes full copy-paste script.
4. Figure manifest and build order precede section paste blocks.
5. Methods/finding/vignette drafts feed into the full copy-paste script.
6. Full script precedes claim-safety and readability audits.
7. Audits precede final revision and QA checklist.
8. Reproducibility manifest and WORK.md updates come last.

## Risk & Mitigation
- Risk: StoryMap becomes too long. Mitigation: use section word counts, callouts, and modular paste blocks; mark optional vignettes.
- Risk: Expanded narrative overclaims. Mitigation: claim-safety audit with strong/cautious/forbidden categories.
- Risk: New explanatory prose invents unsupported history. Mitigation: prohibit unsupported mechanism claims; use “consistent with,” “spatial context,” and “candidate.”
- Risk: Figures are repeated without added explanation. Mitigation: each figure requires “what to notice” and “why it matters spatially.”
- Risk: The text becomes PDF-like. Mitigation: use short paragraphs, story transitions, captions, sidebars, and section-specific paste blocks.
- Risk: Source notes become messy. Mitigation: centralize source/method language in an expanded sources section and avoid adding new unchecked citations.

# 4. Tasks
- [ ] [S01] Create `outputs/run6v2_setup_note.md` — Inputs needed: Run 6 outputs, Run 5 outputs, final PDF/report, exemplar PDF, and this `WORK.md`. Done when: the file states Run 6 v2’s purpose, target expansion level, inherited scope, non-goals, and main risks.
- [ ] [A01] Create `outputs/run6v2_input_artifact_audit.csv` — Inputs needed: all final figures, final PDF report, current Run 6 StoryMap package, exemplar PDF, Run 5 captions/insert, final claim audits, source/limitations notes. Done when: each input is listed with path, exists/missing status, role, reuse/revise/exclude decision, and blocker note if missing.
- [ ] [R01] Create `docs/run6v2_exemplar_style_takeaways.md` — Inputs needed: `Cloudy with a Chance of Compute.pdf`. Done when: the file extracts 8–12 concrete style/structure lessons from the exemplar and translates each into an instruction for Culinary Corridors.
- [ ] [W01] Create `submission/storymap_conversion_v2/storymap_expanded_outline.md` — Inputs needed: R01, current Run 6 build order, final report, final figure sequence. Done when: the outline lists every final section with goal, figure, callout, target word count, paste-block name, transition, and required caveat.
- [ ] [F01] Create `submission/storymap_conversion_v2/storymap_expanded_figure_manifest.csv` — Inputs needed: final figure files and Run 6 manifest. Done when: each final figure has upload order, section, required/optional status, caption, short caption, expanded caption, alt text, what-to-notice note, source note, limitation note, and display recommendation.
- [ ] [W02] Create `submission/storymap_conversion_v2/storymap_methods_atlas_section.md` — Inputs needed: final report methods, Run 6 script, source/limitations notes. Done when: the section explains the four-stage culinary atlas workflow with enough detail for a judge to understand data, similarity, geography, and residuals.
- [ ] [W03] Create `submission/storymap_conversion_v2/storymap_findings_sections.md` — Inputs needed: final report findings, final figures, figure manifest, claim hierarchy. Done when: each major finding has expanded prose covering method context, figure reading guide, result, interpretation, limitation, and spatial significance.
- [ ] [W04] Create `submission/storymap_conversion_v2/storymap_case_vignettes.md` — Inputs needed: East/Southeast Asia case outputs, Run 5 topographic map/interpretation, final report. Done when: the file includes Thai–Vietnamese, Chinese–Korean, Filipino maritime/island bridge, and optional secondary diagnostic vignette, each with what the pair shows, what the map adds, and what cannot be claimed.
- [ ] [W05] Create `submission/storymap_conversion_v2/storymap_expanded_sources_and_limitations.md` — Inputs needed: final report sources/limitations, Run 6 source panel, claim audits. Done when: the file gives a comprehensive StoryMap-ready sources/methods/limitations section with source categories and limitations explained in plain language.
- [ ] [W06] Create `submission/storymap_conversion_v2/storymap_expanded_callouts.md` — Inputs needed: expanded outline, findings, and claim hierarchy. Done when: the file contains polished callouts for research question, method, key finding, caution, geospatial contribution, and conclusion.
- [ ] [W07] Create `submission/storymap_conversion_v2/storymap_expanded_build_order.md` — Inputs needed: expanded outline and figure manifest. Done when: the file gives exact ArcGIS build instructions, block types, figure placement, section ordering, optional sidecar/panel notes, and paste sequence.
- [ ] [W08] Create `submission/storymap_conversion_v2/storymap_expanded_copy_paste_script.md` — Inputs needed: W01–W07. Done when: the file contains the complete expanded StoryMap text with exact headings, PASTE TEXT blocks, EDITOR NOTE blocks, figure placement notes, captions, callouts, and source/limitation notes.
- [ ] [W09] Create `submission/storymap_conversion_v2/storymap_section_paste_blocks/` — Inputs needed: expanded copy-paste script. Done when: the directory contains one Markdown file per StoryMap section, named in build order, and each file separates paste-ready text from editor instructions.
- [ ] [F02] Create `submission/storymap_conversion_v2/storymap_pdf_backup_and_submission_note.md` — Inputs needed: final PDF path, Run 6 PDF backup instructions, expanded script. Done when: the file explains how to place the PDF backup link, how to mention it in the StoryMap, and how to handle submission forms that allow only one URL/file.
- [ ] [F03] Create `submission/storymap_conversion_v2/storymap_expanded_word_counts.csv` — Inputs needed: expanded copy-paste script and section paste blocks. Done when: approximate word count by section and total word count are recorded, with a note on whether length is appropriate.
- [ ] [Q01] Create `outputs/run6v2_claim_safety_audit.md` — Inputs needed: expanded copy-paste script, sources/limitations, callouts, figure manifest. Done when: each major claim is classified as strong/cautious/unsafe; unsafe/ambiguous phrases are listed with required edits.
- [ ] [W10] Revise `submission/storymap_conversion_v2/storymap_expanded_copy_paste_script.md` after Q01 — Inputs needed: claim safety audit. Done when: every flagged overclaim or ambiguous phrase is corrected or explicitly justified.
- [ ] [Q02] Create `outputs/run6v2_storymap_readability_audit.md` — Inputs needed: revised expanded copy-paste script and word counts. Done when: the audit checks section length, figure-led pacing, modularity, clarity, and whether each major figure has sufficient explanation.
- [ ] [W11] Revise `submission/storymap_conversion_v2/storymap_expanded_copy_paste_script.md` after Q02 — Inputs needed: readability audit. Done when: under-explained or overly dense sections are adjusted while preserving claim safety.
- [ ] [F04] Create `submission/storymap_conversion_v2/storymap_expanded_final_qa_checklist.md` — Inputs needed: final expanded script, figure manifest, build order, claim audit, readability audit. Done when: the checklist gives exact pre-submission QA steps for StoryMap build, figure display, captions, sources, PDF backup, mobile/desktop, incognito/private access, and final form submission.
- [ ] [F05] Create `outputs/run6v2_reproducibility_and_manifest.md` — Inputs needed: all Run 6 v2 outputs and reused inputs. Done when: the manifest lists input artifacts, generated outputs, manual steps, package assumptions, skipped/blocked tasks, and final artifact paths.
- [ ] [Q03] Update `WORK.md` Results section with final Run 6 v2 artifact checklist — Inputs needed: all completed Run 6 v2 artifacts. Done when: Results lists every created artifact path, verification status, skipped/blocked tasks, final build order, and exact manual next steps.
- [ ] [Q04] Update `WORK.md` Learnings section with Run 6 v2 lessons and final recommendations — Inputs needed: all completed artifacts and any issues encountered. Done when: Learnings records expansion lessons, exemplar-style lessons, claim-safety lessons, StoryMap pacing lessons, and final recommendations.

# 5. Worker Driver Prompt
You are the worker for **Run 6 v2 — Expanded Atlas-Style StoryMap Content** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition.

This is an expansion/conversion run, not a new research run. Preserve all existing analysis, figures, reports, and the approved claim hierarchy. Use `Cloudy with a Chance of Compute.pdf` as a model for depth, pacing, and section structure, but do not copy its wording or topic. The main objective is to produce a comprehensive, atlas-style, copy-paste-ready ArcGIS StoryMap package that Matthew can use section by section.

Use the approved figure sequence: hero residual-corridor figure; residual/distance method figure; East/Southeast Asia focused-case figure; Run 5 topographic corridor map; residual bridge-index figure; secondary/limitations figure. Make sure global results are presented as discovery only, East/Southeast Asia as the main focused inference case, topography as spatial context, and residual bridge scores as the strongest geospatial-only insight.

Every major finding must explain: what data are being shown, how to read the figure, what the result suggests, why it is geospatial, and what it does not prove. Include short cuisine-pair vignettes for Thai–Vietnamese, Chinese–Korean, and Filipino maritime/island bridge. If adding a secondary diagnostic vignette, keep it cautious.

After each iteration, immediately update `WORK.md`: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, outputs, and verification status; record Learnings with expansion decisions, figure-placement decisions, claim decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing file/input/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If exact numerical values are missing from available files, do not invent them; use qualitative language or mark `[SOURCE CHECK NEEDED]` and list it in the claim audit.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, list the exact files Matthew should open, the final ArcGIS build order, the figure upload order, the paste-block directory, any optional sections, and manual QA steps before submission.

# 6. Learnings

# 7. Results
