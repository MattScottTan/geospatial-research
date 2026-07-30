# Scoring Pass Notes — Final Competitiveness Edits

**Subject:** Bridges Across Cuisines, Fisher Prize submission
**Pass type:** Framing + payoff visibility + caption hardening
**No changes to:** methodology, figures, bibliography, data sources

This document summarizes the nine substantive edits applied to `BUILD_INSTRUCTIONS_v8.md` per the Final Competitiveness Pass spec. Read this once, then open the PDF preview (`storymap_preview.pdf`) end-to-end, then paste into ArcGIS.

---

## What changed (summary)

| # | Task | What changed | Where | Risk if you skip the diff |
|---|---|---|---|---|
| 1 | 2.1 Title | New claim-title pair | Cover (lines 84–92) | Reverting to descriptive title costs ~0.5 visualization points |
| 2 | 2.2 Front-load | Question + hero map now appear before examples | Section 2 Introduction | Original was 280 words before the central question |
| 3 | 1.1 Payoff paragraph | New paragraph names Manila Galleon (1565–1815) | Section 10 Conclusion (before final pull-quote) | This is the actionable-payoff edit (tie-breaker #4) |
| 4 | 1.2 Payoff sentence | New 23-word sentence flagging testable hypotheses | Section 2 Introduction (after "Most analyses" paragraph) | Surfaces payoff to a 30-second skim of intro alone |
| 5 | 1.3 Audience callout | Manila Galleon, Iberian colonial, trans-polar Russian–Atlantic named explicitly | Section 10 Conclusion (food-systems sentence) | Makes the conclusion's "starting point for inquiry" concrete |
| 6 | 1.4 Audit | Verified intro→body→conclusion alignment (no overreach) | Document-wide | Ensures no "proves" in hypothesis-confirming sense |
| 7 | 2.3 Hero caption | Now opens with claim sentence | Figure 1 caption | First caption a judge reads — sets the tone |
| 8 | 2.4 Captions | Figures 4, 5, 6, 7 captions all open with claims | Sections 6, 7, 8 | Caption-as-micro-argument; methodological detail preserved |
| 9 | 2.5 Seam check | Intro→Section 3 transition still clean | Sections 2–3 boundary | No orphan sentences introduced by restructure |

---

## The new title pair (Task 2.1)

**Before:**
- Title: *Bridges Across Cuisines*
- Subtitle: *Mapping the residual geography of global ingredient similarity*

**After:**
- Title: *Cuisine resemblance has a shape that distance can't predict*
- Subtitle: *Mapping the residual network that connects archipelagos, peninsulas, and Atlantic shores*

Why this works: title is a sentence with a verb that asserts. Subtitle names the analytical object (residual network) and the three structural geographies the body delivers (archipelagos, peninsulas, Atlantic shores). A judge reading nothing else than these two lines knows what the project claims and what its evidence will look like.

---

## The new Introduction order (Task 2.2)

**Before:** author bio → three example pairs → puzzle paragraph → "Most analyses" paragraph → central question → hero map intro → hero map → outro.

**After:** author bio → puzzle paragraph → **central question** → hero map intro → **hero map** → three example pairs (now framed as evidence) → "Most analyses" paragraph → **payoff sentence** → outro.

A judge scrolling for 30 seconds now hits, in order: the puzzle, the question, the hero map. The three example pairs come *after* the hero map as evidence rather than buildup. All three pairs (Thai–Vietnamese, British–Russian, Filipino–Brazilian) are preserved verbatim — they're just relocated. Net word count is essentially flat (one new framing sentence: "Three pairs of cuisines illustrate the puzzle.").

---

## The new Conclusion payoff paragraph (Task 1.1)

Inserted immediately before the closing pull-quote. 100 words. Names Manila Galleon (1565–1815) as the cleanest example of a testable historical-exchange hypothesis the residual network produces, then generalizes to Russian (trans-polar) and Spanish (Iberian–Atlantic colonial) corridors. Uses hypothesis-generating language exclusively: *is consistent with the geography of, is testable against, hypothesis-generating cartography*. Avoids *proves, demonstrates, shows that*.

This is the tie-breaker #4 edit. The previous Conclusion ended on a methodological payoff ("the shape is invisible in any analysis that treats distance as the only spatial variable") — true but inward-facing. This pass surfaces an outward payoff (testable historical corridors) that a judge can name.

---

## The new Introduction payoff sentence (Task 1.2)

Inserted after the "Most analyses of food treat cuisine as a cultural object…" paragraph: *"What this analysis produces, beyond methodology, is a set of testable historical-exchange hypotheses anchored to specific cuisines and the corridors their residuals trace."*

23 words. Together with Task 1.1, this means a judge reading only the Introduction, the four cuisine portraits, and the Conclusion gets a coherent payoff arc: intro flags "testable historical-exchange hypotheses" → body supplies the mechanisms (Filipino/Manila Galleon, Spanish/Iberian colonial, Russian/trans-polar) → conclusion delivers the named corridors.

---

## The food-systems audience callout, sharpened (Task 1.3)

**Before:** *"For food-systems researchers, agricultural economists, and historians of exchange, the residual network is a starting point for more specific inquiry: which historical events, ecological conditions, or trade networks correspond with which residual links?"*

**After:** *"For food-systems researchers, agricultural economists, and historians of exchange, the residual network is a starting point for more specific inquiry: the Manila Galleon trade route, the broader Iberian colonial network, and a trans-polar Russian–Atlantic exchange geography stand out as the three corridors the residual structure most clearly flags for follow-up against trade, migration, and colonization records."*

The old version asked a generic question. The new one names three specific corridors. Tone preserved at "starting point for inquiry," not "proof of."

---

## Caption changes (Tasks 2.3 + 2.4)

All five claim-led captions, with original openings shown for comparison. Methodological detail (n, color encoding, link types) is preserved further into each caption — only the *first sentence* moved from label to claim.

**Figure 1 (hero):**
- Before: *Candidate residual cuisine corridors across the project corpus.*
- After: *Cuisines are connected here by ingredient resemblance distance cannot explain.*

**Figure 4 (Finding 2 spatial groupings):**
- Before: *Mean residual cuisine similarity by spatial grouping.*
- After: *Long-distance Iberian–Atlantic–Pacific pairs are more similar than distance predicts by a wider margin than even regional neighbors.*

**Figure 5 (Finding 3 bridge index):**
- Before: *Two-panel residual bridge index.*
- After: *The residual network is anchored by a small set of high-connectivity bridge cuisines whose geographies are distinct rather than redundant.*

**Figure 6 (Finding 4 regional case):**
- Before: *The East/Southeast Asia focused-case map shows the strongest regional residual cuisine links over real geography…*
- After: *East and Southeast Asia produce the corpus's cleanest regional corridor: a small network where mainland adjacency, peninsular geography, and archipelagic structure each contribute a different kind of strong residual link.*

**Figure 7 (Finding 4 relief):**
- Before: *The Run 5 relief map places the strongest East/Southeast Asia residual links over topographic, coastal, island, and maritime context.*
- After: *Adding shaded relief makes the corridor's geographic logic legible: the Tibetan plateau is the western barrier, the South China Sea is the connector rather than the gap, and the archipelagic ring (Filipino, Japanese) closes the loop on the mainland anchors.*

Note on Figure 7 specifically: per Task 3.3, the relief-map caption now opens on the *additional* information the relief context adds, not on what the figure is. This avoids Figure 7 reading as a replacement for Figure 6.

---

## What's not changed (constraints honored)

Verified by tool diff against the previous BUILD_INSTRUCTIONS_v8.md:

- **Section 4 (Finding 1) prose:** zero diffs. Methodology body untouched.
- **Section 5 (Finding 1.5) prose:** zero diffs. Mantel + LISA prose untouched.
- **Section 6 (Finding 2):** only the figure caption changed.
- **Section 7 (Finding 3):** only the figure caption changed.
- **Section 8 (Finding 4):** only the two figure captions changed.
- **Section 9 (Four cuisines):** zero diffs. All four case-study portraits unchanged.
- **Section 13 Bibliography:** 19 entries, unchanged.
- **All 11 figure references:** unchanged.

This pass adds zero re-export risk: every paste block remains a clean fenced code block. ArcGIS will see the same paste structure it's seen before.

---

## What you do next

The execution-order steps from the spec, items 11–17:

1. **Re-read the PDF preview end-to-end** (`storymap_preview.pdf`). Look specifically at the Introduction front-loading (page 1) and the new Conclusion payoff paragraph (pages 18–19). If anything reads wrong, fix it locally first — round-trips through the ArcGIS editor are failure surface.
2. **Open ArcGIS StoryMaps editor.** Paste in one session, top to bottom. The build doc is structured for this — every action marked with `> ➤`.
3. **Run cartographic checks 3.1–3.6 inside the editor.** These are editor-side: they verify hero-map placement, Moran scatterplot legibility, Figure 6/7 separation, color-legend consistency across the four cuisine portraits, mobile rendering of side panels, and corpus-coverage disclaimer legibility. The build doc captures the right caption text; the editor is where you verify the rendering.
4. **Save and publish.** Set sharing to public.
5. **Incognito test from a second device.** Verify URL accessibility, scroll order, figure rendering.
6. **Compose submission email** to `jblossom@cga.harvard.edu`. Use a project description from `PRIZE_ENTRY_DESCRIPTION.md` if the email asks for one — Variant C (medium description, 330 words) is the most likely fit.
7. **Send by 8:00 PM internal deadline.** Verify sent timestamp, URL still public, no bounce-back by 9:00 PM.

---

## Estimated rubric impact

Per the spec's own estimate:
- Innovation: +0.5 (sharper framing of the residual-network contribution)
- Visualization: +0.5 to +1.0 (claim-titles, claim-captions, first-impression hardening)
- Tie-breaker #4 (actionable payoff): the dimension most likely to swing a close call
- Net: 89 → ~91, into the Prize-contender band

The biggest single-edit lever is Task 1.1 (the Conclusion payoff paragraph). It's the edit that makes the actionable-payoff dimension visible to a 30-second judge scan.

---

## Hard stop reminder

The spec says: *"Stop editing at the local-save step. Re-read once. Then commit to the editor paste. Every edit after the paste is risk without gain."*

Follow that. Read the PDF, then paste. Don't edit live in ArcGIS unless the cartographic checks (3.1–3.6) flag a real problem.
