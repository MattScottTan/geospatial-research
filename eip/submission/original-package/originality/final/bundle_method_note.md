# Prototype 1 note — Compute Opportunity Bundle Index

## Components and weights

| component                |   weight |
|:-------------------------|---------:|
| score_proximity          |     0.4  |
| score_provider_diversity |     0.15 |
| score_redundancy         |     0.15 |
| score_population         |     0.15 |
| score_institutions       |     0.15 |

## Reading

This prototype keeps raw cloud proximity central but adds three other layers visible in the current project data: provider diversity, regional redundancy, and institutional/market anchors.

## Why it is promising

- It operationalizes the project's mature claim that compute works as part of a broader bundle.
- It produces a strong global map plus interpretable comparison/outlier views.
- It can flow directly into the four-city case-study section.

## Risks / limits

- The institutional anchor signal comes from the project's OpenAlex-linked files, so it is not a fully independent external ecosystem measure.
- It is more original than distance alone, but less surprising than a full counterfactual siting analysis.
