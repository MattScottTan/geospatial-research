# Causal Audit

Date: 2026-03-14 12:01 PM America/New_York

## Scope audited

- `extensions/stage4/docs/analysis_approach_stage4_summary.md`
- `extensions/stage5/docs/stage5_pilot_summary.md`
- `extensions/stage6/docs/stage6_expanded_panel_summary.md`
- corresponding scripts and outputs in `extensions/stage4/`, `extensions/stage5/`, and `extensions/stage6/`

## What the causal extensions collectively test

### Stage 4
Stress-test the cross-sectional distance relationship using stronger geographic controls, country fixed effects, within-country demeaning, and treatment-style matching / weighting.

### Stage 5
Pilot a city-year panel with AWS launch timing and event-study / difference-in-differences logic using a top-institution city subset.

### Stage 6
Broaden the selected-city panel, increase treated/control coverage, and test staggered-adoption panel behavior across cohorts and windows.

## Main evidentiary pattern

### 1. The descriptive cross-sectional signal is real
The baseline negative association between greater distance and lower observed AI activity reappears in the simpler cross-sectional setup.

### 2. The signal does not stabilize as a causal estimate
When stronger within-country or panel comparisons are introduced, the sign and magnitude become unstable:
- country fixed effects weaken or reverse the simple cross-sectional sign,
- within-country demeaned relationships are close to zero,
- pilot DiD/event-study specifications are mixed,
- expanded panel estimates are specification-sensitive and heterogeneous across cohorts.

### 3. The strongest causal-friendly specifications do not converge on one clean story
The expanded panel contains one significant positive fixed-effects specification, but that result does not generalize across adjacent specifications or cohort/event-window approaches.

## Audit conclusion

The current project supports a **disciplined non-causal claim**:
- compute access is a meaningful spatial correlate and screening layer,
- the causal story remains unresolved,
- any effect of local cloud-region openings appears heterogeneous and context-dependent rather than universal.

## Submission implication

The causal extensions should inform the **limits/non-claim language** of the final report and StoryMap, not serve as the analytical centerpiece of the EIP submission.
