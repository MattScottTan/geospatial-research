# PLAN — strategy for SPEC.md

Revisable if execution evidence shows the strategy is wrong. SPEC.md is not.

## Approach

Evidence first, then exposition, then audit.

The two papers rest on findings that are currently verified on **one dataset each**. The
user chose to close those gaps before writing, so the first milestone produces the missing
evidence. Only then is prose written, because the narrative of an expository paper is
built around its numbers and rewriting around changed numbers is more expensive than
waiting.

Three structural decisions shape the work:

1. **The primer is the largest single writing artifact.** "No statistics background" means
   defining p-values, permutation tests, z-scores, matrices, eigenvectors and quadratic
   forms from scratch. Written once, `\input` into both papers so each is standalone.
   Drafting it does not depend on any experiment, so it runs in parallel with M1.

2. **Sources are a work product, not a byproduct.** The user asked for sources to be
   "carefully detected and parsed." That is an annotated bibliography where each entry
   explains what the source does and what we take from it — which requires retrieving and
   reading sources, not just citing them. This is its own task, started early because it
   can invalidate a claim and force narrowing.

3. **Audit is separate from authoring.** A worker who wrote a section is a poor verifier of
   it. Numerical traceability, source verification, and jargon-freeness each get a
   dedicated pass against the finished PDFs.

## Milestones

**M1 — Evidence and sources complete.**
Prevalence study for Paper 1, selection-rule surface for Paper 2, and the verified source
corpus. Exit: every number either paper will claim exists in a committed script output,
and every source is retrieved and annotated.

**M2 — Scaffolding.**
LaTeX build system, shared primer, figure pipeline. Exit: `make` produces two stub PDFs
containing the primer and all figures, compiling cleanly.

**M3 — Paper 1 complete.**
Exit: `paper1.pdf` compiles, contains all sections, every number traceable.

**M4 — Paper 2 complete.**
Exit: as M3, for `paper2.pdf`.

**M5 — Audit and acceptance.**
Three independent audit passes plus a final Definition-of-Done check. Exit: every DoD box
ticked with evidence.

## Dependency Logic

- The prevalence study (T-002) and the selection surface (T-003) are independent of each
  other and of everything else. Run them in parallel and first — they are the long poles
  and they gate both manuscripts.
- The literature corpus (T-001) is independent and runs alongside. It gates the manuscripts
  but not the experiments.
- The primer (T-004) and build scaffold (T-005) depend on nothing. They can proceed during
  M1, which is why M2 is cheap in wall-clock terms.
- Figures depend on their paper's evidence plus the scaffold.
- Manuscripts depend on evidence, sources, primer, and figures.
- All three audits depend on both manuscripts and are mutually independent — run in
  parallel.
- Final acceptance depends on all audits.

Critical path: **T-002/T-003 → figures → manuscripts → audits → acceptance.**

## Risks and Mitigations

**Risk: the prevalence study finds disconnection is rare.**
Impact: high — Paper 1's contribution shrinks from "a widespread unreported problem" to "an
edge case." Detection: T-002 output. Mitigation: the paper's framing is set *after* T-002,
not before. If prevalence is low, the paper is reframed around the conditions that produce
disconnection (clustered geography, small `k`) and honestly scoped. Do not write the
introduction before this number exists.

**Risk: prior work exists for Paper 1's finding.**
Impact: high. Detection: T-001. Mitigation: narrow the claim per assumption A-5; the
component-aware correction and the prevalence data remain contributions even if the
artifact has been noted before. Search must include grey literature, `spdep`/`ArcGIS`
issue trackers and documentation, not only journals.

**Risk: Type I inflation proves highly sensitive to the candidate grid.**
Impact: medium — weakens "roughly threefold" into "it depends." Detection: T-003.
Mitigation: this is a finding, not a failure. Report the surface and identify which grids
are dangerous; that is more useful than a single number.

**Risk: LaTeX corruption via Bash heredocs.**
Impact: high, and already observed. Detection: compile failure with `Misplaced \noalign` or
similar. Mitigation: hard constraint in SPEC — `.tex` authored only via Write/Edit. Encoded
in MEMORY.md.

**Risk: the papers become unreadable through sheer length.**
Impact: medium. The brief invites length, which invites sprawl. Detection: T-012
accessibility audit. Mitigation: every section must open with a one-paragraph statement of
what it establishes and why the reader needs it; the audit checks for this.

**Risk: numbers drift between script output and prose.**
Impact: high — a paper stating a number its own code does not produce is the worst failure
mode available here. Detection: T-010. Mitigation: `CLAIMS.md` is maintained *while*
writing, not reconstructed after.

## Validation Strategy

| What | How |
|---|---|
| Compilation | `make` from clean; zero errors; no `??` references in output |
| Numerical claims | T-010 re-runs every script in `CLAIMS.md` and diffs against prose |
| Sources | T-011 retrieves each cited URL/DOI and confirms it supports the claim |
| Accessibility | T-012 extracts all technical terms from the PDF text, checks each has a prior definition and a glossary entry |
| Reproducibility | Fresh-clone run of `make` plus all analysis scripts |
| Structure | Table of contents contains a findable contribution section and limitations section in each paper |
| Honesty | T-010 confirms the null result (Moran's I unaffected) is present in Paper 1 |

Evidence is preferred over assertion throughout: an audit task that cannot point to a
command it ran and the output it saw has not validated anything.
