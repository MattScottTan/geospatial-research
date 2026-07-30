# Report readability audit for EIP judges

This audit reviews the current `report/main.tex` and `report/main.pdf` against the winner qualities documented in `docs/eip_winner_benchmark.md`.

## Overall diagnosis

The current report is scientifically careful, but it still reads more like a strong internal technical memo than a winning EIP submission. The main friction points are not the analysis itself. They are the reading order, the density of the opening pages, the amount of jargon before the reader gets a plain answer, and the amount of report real estate spent on documentation rather than on the public-interest story.

In benchmark terms, the report already has evidence and seriousness, but it underperforms on four winner signals:

- **lead with a real public problem**
- **sound useful to decision-makers**
- **present the work in an engaging format**
- **feel polished and easy to follow from start to finish**

## High-level barriers

1. **The report delays its clearest pitch.**
   The first page opens with a dense abstract, then a glossary, then a table of contents. The reader does not reach the main narrative section until page 3. This weakens the hook and hides the short answer.
   - Benchmark links: qualities 1, 2, 7, 9

2. **The opening sounds scholarly before it sounds useful.**
   The report explains what the study is scientifically, but it does not quickly show what a judge should care about in practical terms.
   - Benchmark links: qualities 1, 2, 3

3. **Too much technical framing arrives before the reader has a mental map of the story.**
   Terms such as spatial dependence, Gaussian Process, CAR/GMRF, Gi*, and estimand appear early or prominently enough to raise the reading burden.
   - Benchmark links: qualities 5, 7, 9

4. **The report has duplicate or near-duplicate interpretive sections.**
   `Scientific interpretation and EIP implications`, `Conclusion`, `Limitations and extensions`, and `Atlas delivery assets` all do legitimate work, but the current sequence dilutes momentum late in the report.
   - Benchmark links: qualities 3, 6, 7

5. **Figure guidance is not strong enough for lay readers.**
   The figures are good, but the prose often introduces them as evidence rather than as visuals the reader is being guided through.
   - Benchmark links: qualities 2, 6, 7

## Section-by-section audit

### Title and subtitle

**What works now**
- The title clearly identifies the project.
- The subtitle signals geography, AI, and city-level screening.

**Barrier**
- The title package is descriptive, but not especially public-facing or urgent.

**Rewrite priority**
- Keep the title if needed for continuity, but make the first paragraph under it do the urgent public-interest work.

**Benchmark links**
- qualities 1, 2, 3

### Abstract

**What works now**
- Contains the central question, the answer, and the causal caution.

**Barrier**
- It is dense, multi-claim, and jargon-heavy.
- It reads like an academic abstract, not like an EIP opening pitch.
- A lay judge has to parse several technical phrases before they reach the basic message.

**Rewrite priority**
- Highest. Convert the abstract into a short executive summary voice: problem, question, short answer, why it matters.

**Benchmark links**
- qualities 1, 2, 3, 7, 9

### Key terms (plain English)

**What works now**
- Helpful content.

**Barrier**
- The glossary appears too early and interrupts the narrative hook.
- It asks the reader to learn vocabulary before they care about the story.

**Rewrite priority**
- High. Keep the definitions, but move most of this work inline to first use or compress it to a smaller box after the opening stakes.

**Benchmark links**
- qualities 6, 7, 9

### Table of contents

**What works now**
- Useful for a long technical report.

**Barrier**
- It takes a full early page in a submission that should hook judges quickly.

**Rewrite priority**
- Medium to high. Keep if needed, but only if the opening pages become much more compelling; otherwise consider a shorter front matter flow.

**Benchmark links**
- qualities 3, 6, 7

### Motivation and scientific question

**What works now**
- The content is intellectually strong.
- The causal boundary is already disciplined.

**Barrier**
- The section still opens in research prose rather than in concrete human or policy stakes.
- The short answer is implied rather than stated in a crisp, memorable way.
- The testable expectations list is accurate but still sounds like proposal language.

**Rewrite priority**
- Highest. This section should become the report's true landing zone for judges.

**Benchmark links**
- qualities 1, 2, 5, 7, 9

### Data

**What works now**
- Transparent about sources and caveats.
- Includes useful tables.

**Barrier**
- The data section arrives before the reader has been shown the payoff.
- The source descriptions are accurate but still read like documentation.

**Rewrite priority**
- Medium. Simplify and keep only what helps the reader trust the evidence.

**Benchmark links**
- qualities 4, 5, 9

### Methods

**What works now**
- Scientifically disciplined.
- The causal boundary is explicit.

**Barrier**
- This is the densest section in the report.
- The equation and model naming arrive before a lay reader has a settled understanding of the main empirical picture.
- Some subheads are researcher-facing rather than reader-facing.

**Rewrite priority**
- Highest. The methods need to become tool explanations: what each step does, why it was used, and what question it answers.

**Benchmark links**
- qualities 5, 7, 8, 9

### Results

**What works now**
- Strong structure and real evidence.
- Good figure variety.

**Barrier**
- The prose sometimes states findings in technical terms before translating them.
- Some subsections are longer than they need to be for a judge audience.
- The reader does not always get an upfront sentence telling them what to look for in the next figure.

**Rewrite priority**
- Highest. The results are the core of the submission and need clearer pacing and takeaways.

**Benchmark links**
- qualities 2, 3, 6, 7, 9

### Scientific interpretation and EIP implications

**What works now**
- Valuable policy framing.

**Barrier**
- The section title signals academic interpretation more than applied consequence.
- It overlaps with what the conclusion is also doing.

**Rewrite priority**
- High. Keep the substance, but retitle and streamline so it feels like the report's public-value section.

**Benchmark links**
- qualities 1, 2, 3, 7

### Conclusion

**What works now**
- Clear about what the project found and did not prove.

**Barrier**
- Some content repeats earlier interpretation.
- The next-step paragraph is useful, but the close could end more directly on what judges should remember.

**Rewrite priority**
- Medium to high.

**Benchmark links**
- qualities 2, 3, 7, 9

### Atlas delivery assets

**What works now**
- Useful for handoff.

**Barrier**
- This is operational repo information inside the main narrative. It weakens the end of the report as a judged piece of communication.

**Rewrite priority**
- High. Compress heavily or reposition so it does not interrupt the story's ending.

**Benchmark links**
- qualities 3, 6, 7

### Limitations and extensions

**What works now**
- Good scientific discipline.

**Barrier**
- The limitations are excellent, but they come after the conclusion and after the delivery-assets section, which makes the ending feel fragmented.

**Rewrite priority**
- Medium. The content should stay, but the sequence should feel tighter.

**Benchmark links**
- qualities 4, 5, 9

### Reproducibility

**What works now**
- Valuable provenance.

**Barrier**
- This is useful archive material, but not core judged narrative.

**Rewrite priority**
- Medium. Keep brief and tuck it into a closing note rather than letting it compete with the story.

**Benchmark links**
- qualities 3, 4, 6

## Ranked rewrite plan

### Priority 1: Rebuild the opening around stakes, question, short answer, and usefulness

**Why this matters most**
This is the single biggest gap between the current report and the winner benchmark. Judges should understand within the first page what the project is about, what it found, and why it matters for public decision-making.

**Actions**
- Rewrite the abstract/opening into a more direct, executive-summary style.
- Make the central question explicit in one sentence.
- Add a one-sentence short answer early.
- Explain why uneven compute access matters in public-interest terms.

**Benchmark links**
- qualities 1, 2, 3, 7, 9

### Priority 2: Convert methods from research exposition to reader guidance

**Why this matters most**
The current methods are defensible, but the reading burden is too high for judges.

**Actions**
- Replace researcher-first transitions with plain-language tool explanations.
- Keep the equation only if the surrounding prose makes it easy to interpret.
- Define technical terms on first use and then return to plain English.

**Benchmark links**
- qualities 5, 7, 8, 9

### Priority 3: Rewrite results around what the reader should notice

**Why this matters most**
The figures can do more work if the prose guides the reader through them.

**Actions**
- Add one-sentence previews before each major figure/table.
- Start each results subsection with the substantive takeaway, then provide evidence.
- Translate statistical language into plain-English implications before naming the method.

**Benchmark links**
- qualities 2, 3, 6, 7, 9

### Priority 4: Tighten the back half so the report ends with impact, not administration

**Why this matters most**
A winning submission should land on what the project helps people see and do.

**Actions**
- Reduce duplication between implications and conclusion.
- Compress operational documentation sections.
- Keep limits visible, but arrange them so the ending still feels decisive and useful.

**Benchmark links**
- qualities 2, 3, 6, 7, 9

### Priority 5: Make every section title and transition judge-facing

**Why this matters most**
Even when the evidence stays the same, reader-facing headings and transitions make the report feel more polished and easier to follow.

**Actions**
- Prefer headings that answer a question or name a takeaway.
- Replace technical transition sentences with directional ones.
- Use short framing sentences before tables and figures.

**Benchmark links**
- qualities 3, 6, 7, 9

## Rewrite guardrails

To stay inside scope while improving readability:

- do not change the underlying analysis or numbers unless wording currently overstates the evidence
- do not introduce new datasets or model variants
- keep causal limitations explicit
- simplify prose without collapsing the distinction between correlation, spatial robustness, and causality
