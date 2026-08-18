# DECISIONS

Durable decisions future workers must respect. Not a history log.

## D-001 — Output is LaTeX compiled to PDF

**Decision:** Both papers are LaTeX source compiled to PDF. No Markdown deliverable.
**Reason:** User selection. Equation-heavy expository text with tables and floats needs
real typesetting; the toolchain is present and verified.
**Consequences:** All prose is authored as `.tex`. Figures must be vector PDF. Bibliography
via BibTeX. Reviewing requires compiling.
**Related:** AC-001, AC-011, D-005.

## D-002 — Evidence is completed before prose is written

**Decision:** The prevalence study (T-002) and inflation surface (T-003) finish before the
manuscripts start.
**Reason:** User selection. An expository paper's narrative is built around its numbers;
both findings currently rest on a single dataset. Rewriting a built narrative around
changed numbers costs more than waiting.
**Consequences:** M1 is the critical path. Do not draft either introduction before the
corresponding evidence exists — in particular, Paper 1's framing depends on whether
disconnection turns out to be common or rare.
**Related:** AC-006, AC-007, T-002, T-003.

## D-003 — Audience assumes no statistics background

**Decision:** A numerate reader is assumed — algebra, reading a graph. Nothing statistical.
Every term of art is defined from scratch.
**Reason:** User selection. The brief is textbook/lecture-notes accessibility.
**Consequences:** The shared primer is a major artifact, not a preliminary. Length is
expected and acceptable. Any worker tempted to write "recall that" or "it is well known
that" about a statistical concept must instead define it.
**Related:** AC-003, T-004, T-012.

## D-004 — The case study is attributed to the author's own prior work

**Decision:** The compute-accessibility atlas is named as the author's own published
StoryMap wherever used, and the correction to its results is stated plainly.
**Reason:** User selection. Self-correction reads as integrity, avoids any appearance of
attacking a third party, and the data and code are already public in this repo.
**Consequences:** Paper 1 states directly that roughly a third of its own previously
published cold spots are artifacts. No euphemism, no passive voice hedging.
**Related:** AC-009.

## D-005 — `.tex` files are authored with Write/Edit, never Bash heredocs

**Decision:** Hard prohibition on generating LaTeX through shell heredocs in this
environment.
**Reason:** Verified failure. Git Bash on this machine collapses `\\` to `\`, silently
corrupting tabulars and line breaks; a smoke test failed with `Misplaced \noalign` before
the cause was found.
**Consequences:** Any worker writing `.tex` uses the Write or Edit tool. Python scripts
that *generate* `.tex` fragments must be written via Write and then executed, not piped
through a heredoc.
**Related:** AC-001, T-005, and every authoring task.

## D-006 — Two standalone PDFs sharing one primer source

**Decision:** `paper1.pdf` and `paper2.pdf` are separately readable. The primer is written
once in `papers/shared/primer.tex` and `\input` into both.
**Reason:** The papers address different findings and different readers may want only one.
Duplicating primer *source* would guarantee drift.
**Consequences:** The primer must not assume either paper's specific context. Paper-specific
background belongs in the paper, not the primer.
**Related:** A-1, T-004.

## D-007 — Claims are traced while writing, not reconstructed afterwards

**Decision:** `papers/CLAIMS.md` is updated as each number enters the prose.
**Reason:** Reconstructing provenance after the fact is where numbers silently drift from
the code that produced them — the most damaging failure available in this project.
**Consequences:** Writing tasks are not complete until their CLAIMS.md rows exist. T-010
audits against this file rather than building it.
**Related:** AC-002, T-008, T-009, T-010.

## D-008 — Findings are narrowed rather than sources suppressed

**Decision:** Where the literature check surfaces prior work that partially preempts a
claim, the claim is narrowed and the prior work cited prominently.
**Reason:** Programme precedent. Two claims have already been narrowed this way after
searching (the eigenvector localisation threshold, and Ricci curvature on geographic
networks). Both were better for it.
**Consequences:** T-001 may force scope changes in T-008 or T-009. That is an expected
outcome, not a failure, and must be recorded here when it happens.
**Related:** A-5, AC-005, T-001.

## D-009 — Null and negative results are reported

**Decision:** Paper 1 reports that Moran's I is essentially unaffected by disconnection,
with the same prominence as the positive Gi\* finding.
**Reason:** Telling practitioners which of their tools to keep trusting is half the
contribution, and omitting it would misrepresent the scope of the problem.
**Consequences:** Any draft of Paper 1 that presents disconnection as breaking spatial
statistics generally is wrong and must be corrected.
**Related:** AC-002, T-008, T-010.

## D-010 — Paper 1's "silent disconnection" premise is withdrawn

**Decision:** Paper 1 may not claim that graph disconnection goes unreported by software, or
that the problem is unnoticed. It must instead claim the narrower and defensible thing: the
tools warn that disconnection *happened*, but nothing tells the user what it *does to a
Getis-Ord hot-spot map*.

**Reason:** Prior-art check (T-001, partial) found the premise false on three counts.
`spdep` raises warnings such as "neighbour object has 2 sub-graphs", ships `n.comp.nb` to
count disjoint subgraphs, and carries a dedicated CRAN vignette, *No-neighbour observation
and subgraph handling*. `libpysal` prints a disconnected-component warning by default. The
spdep documentation even notes that disconnection "occurs frequently with point support",
so the qualitative prevalence observation is known too. Bivand's vignette states the
conceptual point memorably: "The ripples in one pond cannot cross into a separate pond if
they are not connected."

**What survives, verified against that vignette:** it does *not* discuss consequences for
Getis-Ord Gi\*, LISA, or Moran's I; it does *not* propose within-component standardisation
or any correction; it does *not* quantify prevalence. Its remedies are practical — increase
`snap`, handle singleton units, `adjust.n`. So the contribution is now:

1. the specific Gi\* global-standardisation artifact and its size,
2. the within-component standardisation fix,
3. quantified prevalence (39.4% of 1,764 configurations; full n x k table),
4. the negative result that Moran's I is essentially unaffected,
5. the framing that a warning about *occurrence* is not a warning about *consequence*.

**Consequences:** Any draft asserting the problem is invisible, silent, unreported or
unnoticed is wrong and must be rejected in verification. `spdep`'s vignette and `libpysal`'s
warning must be cited prominently and early, not buried. The motivation section argues from
"warned but not informed", not from "nobody knows".

**Related:** AC-006, AC-009, D-008, T-001, T-008.
