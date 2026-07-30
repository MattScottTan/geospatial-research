# Prototype 2 note — Counterfactual Compute Siting Layer

## Objective
Rank candidate cities by how much one additional compute node at that location would reduce the log-population-weighted average nearest-cloud distance across the current 8,000-city frame.

## Baseline
Current weighted average nearest-cloud distance: **907.8 km**

## Why it is promising

- It turns the atlas into a policy/counterfactual planning tool.
- It is visually distinctive and more difficult to replicate casually than another descriptive map.
- It can create a strong “where next?” moment in the StoryMap.

## Risks / limits

- It is a simplified geodesic planning exercise, not a true network or business case model.
- It is hypothetical and may feel more speculative than the bundle index.
