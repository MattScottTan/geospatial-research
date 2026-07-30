# Fisher Award Internal Scoring Rubric

## Packet Links
- [Fisher Award Playbook](fisher_award_playbook.md)
- [Feature Matrix](feature_matrix.md)
- [Scoring Rubric](scoring_rubric.md)
- [Production Timeline](production_timeline.md)
- [Topic Scoring Template](topic_scoring_template.md)


## Purpose
This rubric is an internal optimization tool. It preserves the five official Fisher criteria but weights them for a competition strategy that emphasizes judge-visible spatial necessity, analytical rigor, data credibility, and cartographic communication.

## Compliance Gate
A submission should not receive quality scoring until every applicable compliance item is marked `PASS`.

| Gate item | PASS condition | FAIL / risk condition | Evidence to record |
|---|---|---|---|
| Eligibility | Student is Harvard undergraduate or graduate, enrolled in the academic year, and in good standing. | Eligibility unknown or not documented. | Status confirmed by student/advisor. |
| Group entry | If group project, it is submitted as one entry. | Multiple conflicting submissions for same group work. | Named group members and one submission plan. |
| Registration | Fisher registration form submitted using HarvardKey. | Registration incomplete or not confirmed. | Registration confirmation saved. |
| Deadline | Submitted before Sunday, May 3, 2026 at 11:59 p.m. | Any uncertainty about timestamp or late email. | Sent email timestamp + confirmation. |
| Poster format | Poster is 42” x 36” and exported as PDF. | Wrong size, non-PDF, unreadable export. | PDF properties checked. |
| Poster word count | Descriptive text <=350 words; legends, labels, title, citations, captions excluded as allowed. | Over cap or unclear distinction between text/captions. | Word-count audit. |
| StoryMap format | StoryMap URL works, is public/accessible to judges, and showcases the work. | Broken/private URL or missing maps. | Tested URL from non-editing browser. |
| Submission channel | Poster PDF or StoryMap URL emailed to Jeff Blossom at `jblossom@cga.harvard.edu` after registration confirmation. | Sent to wrong address or before registration if confirmation required. | Sent email screenshot/copy. |

## Spatial Necessity Gate
The project should pass at least **4 of 5** tests before competing seriously.

| Test | PASS | FAIL |
|---|---|---|
| GIS changes the answer | Removing GIS would remove the core finding. | GIS only illustrates a result found another way. |
| Spatial operation is nontrivial | Workflow uses classification, network analysis, overlay/modeling, change detection, spatial statistics, suitability/risk modeling, 3D reconstruction, location-allocation, or equivalent. | Points or polygons are merely displayed. |
| Geography explains something | The spatial pattern helps explain exposure, access, control, risk, destruction, change, or difference. | The map is descriptive but not explanatory. |
| Scale is intentional | The project justifies neighborhood/city/regional/global scale and resolution. | Scale is accidental or inherited from available data. |
| Map is evidence | A judge can point to the map/model output as evidence for the claim. | The claim lives mostly in text. |

## Weighted Score
Internal weights total **100**. They are not official Fisher weights; they are designed to maximize competitiveness under the official criteria.

| Official Fisher criterion | Weight | 5 = excellent | 3 = adequate | 1 = weak | Evidence required |
|---|---:|---|---|---|---|
| Innovation and creativity of chosen topic | 18 | Fresh, precise, high-stakes spatial thesis; surprising geography/data combination; avoids generic framing. | Interesting topic but familiar method or broad framing. | Common topic with no clear original angle. | Research question, novelty note, archetype fit. |
| Use of GIS in performing the project | 25 | GIS is indispensable and methodologically substantive; output cannot be produced by non-spatial analysis. | GIS supports the project but is not the main engine. | GIS is mainly display. | Workflow, geoprocessing steps, method outputs. |
| Data — complexity, relevance to topic, properly documented | 20 | Multi-source relevant data; provenance, preprocessing, CRS/resolution/time alignment, and uncertainty documented. | Good data but limited documentation or complexity. | Unclear source, scale mismatch, or weak relevance. | Data table, source notes, preprocessing log. |
| Analytical approach and execution | 20 | Defensible workflow, validation/sensitivity check, transparent parameters, limitations handled. | Reasonable analysis with some gaps. | Conclusions outrun method; little validation. | Workflow diagram, parameter table, validation or robustness check. |
| Visualization / cartographic communication effectiveness | 17 | Hero map + supporting maps communicate the claim quickly; clear hierarchy, legends, captions, sources. | Legible maps but weak hierarchy or narrative. | Cluttered, confusing, or decorative visuals. | Draft poster/StoryMap review, visual QA. |

### Score calculation
- For each criterion, assign 1–5.
- Convert to weighted score: `(criterion score / 5) * weight`.
- Total score = sum of all weighted criterion scores.
- Do not calculate total until Compliance Gate passes and Spatial Necessity Gate is acceptable.

## Tie-Breakers
Use these when two topics or drafts have similar scores.

1. **Stronger spatial necessity wins.** The project where GIS is most indispensable should advance.
2. **Cleaner evidence beats more complexity.** A simpler workflow with validated data beats an ambitious but opaque workflow.
3. **Better cartographic first impression wins.** Judges should grasp the central spatial claim within 30 seconds.
4. **Actionable or interpretive payoff wins.** The result should change how someone understands the place/problem.
5. **Documented uncertainty beats false precision.** Explicit limits signal rigor.

## Interpretation Bands

| Total score | Readiness band | Meaning | Action |
|---:|---|---|---|
| 90–100 | Prize-contender | Strong across all criteria and visibly spatial. | Polish visuals, captions, and submission QA. |
| 80–89 | Competitive | Good chance if weak areas are upgraded. | Fix lowest-weighted gaps before visual polish. |
| 70–79 | Borderline | May be a solid class project but not award-optimized. | Add spatial method, data documentation, or sharper thesis. |
| 60–69 | Weak | Meets some criteria but lacks winning distinctiveness. | Reframe topic or rebuild method around spatial necessity. |
| <60 | Not ready | Too risky for Fisher competition. | Do not submit without major redesign. |

## Minimum Recommended Thresholds
- Compliance Gate: all `PASS`.
- Spatial Necessity Gate: at least 4/5 `PASS`.
- Weighted score: **85+** before final polish; **90+** target by submission.
- No individual official criterion below 3/5.

## Reviewer Scoring Form

| Review item | Score / status | Reviewer evidence | Required fix |
|---|---|---|---|
| Compliance Gate | PASS / FAIL |  |  |
| Spatial Necessity Gate | 0–5 passes |  |  |
| Innovation and creativity | 1–5 |  |  |
| Use of GIS | 1–5 |  |  |
| Data | 1–5 |  |  |
| Analytical approach | 1–5 |  |  |
| Visualization/cartography | 1–5 |  |  |
| Overall weighted score | 0–100 |  |  |
| Biggest risk | Text |  |  |
| Highest-value upgrade | Text |  |  |
