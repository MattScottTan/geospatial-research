# Data Storybook

## Criterion definition

The Fisher data criterion rewards more than “having data.” The strongest accessible winners use data that are clearly relevant to the question, sufficiently complex to feel non-routine, and documented well enough that the reader can understand both provenance and fit.[P2][P3][P5][P8]

## Evaluation signals

- The artifact names data sources, sensors, boundaries, or collection types rather than treating data as invisible inputs.[P2][P5][P8]
- The chosen data are tightly aligned to the substantive question.[P1][P2][P3][P4][P5][P8]
- Multi-source integration serves the argument instead of creating complexity for its own sake.[P3][P8]
- The project exposes enough documentation that a reader can judge relevance, temporal frame, and likely limitations.[P5][P8]
- The data stack looks harder to fake or approximate than a standard classroom demo.[P2][P3][P8]

## Winner case studies

### Top-tier accessible cases

- **Emilio Sempris (5/5 in the current matrix):** Emilio is the clearest data-documentation model in the accessible set. The poster names 13.3 million ignition points, Global Fire Atlas / NASA MODIS, GADM boundaries, TNC terrestrial ecoregions, and NASA Visible Earth layers, while also exposing software tools directly on the artifact.[P8]
- **Shane Rice (5/5):** Shane’s StoryMap snippet signals a particularly rich historical imagery base by naming CORONA, GAMBIT, and HEXAGON. That makes the data feel both relevant and unusually complex.[P2]
- **Dev Patel (5/5):** Dev’s project combines satellite-based inundation measurement with survey and historical-infrastructure evidence, producing a multi-source dataset that matches both the measurement problem and the adaptation question.[P3]

### Strong 4/5 cases

- **Bora Ju (4/5):** Bora names the exact imagery source — Harmonized Sentinel-2 MSI Level-2A at 10–30m resolution — and ties it tightly to the classification task. The data are well matched and well described, even if the stack is narrower than Dev’s or Emilio’s.[P5]
- **Beatrice Youd (4/5):** Beatrice’s project appears to combine conservation geography with forest-loss and accessibility evidence. The current public snippet suggests a relevant spatial dataset, though not one documented as fully as the top-tier cases.[P4]

### More constrained case

- **Aanchal Chopra (3/5):** Aanchal’s accessible artifact clearly signals climate-condition inputs and walkability-index logic, but the current public snippet does not expose the data stack or documentation depth at the same level as Emilio, Shane, Dev, or Bora. `uncertain-inference`.[P1]

## Anti-patterns and omissions

- If the artifact does not name the data sources, the data criterion becomes hard to demonstrate even when the underlying work may be strong.[P1][P6][P7]
- Exact-title public artifacts can still remain `partial` if the indexed text never reveals the underlying data stack. That is a major current limitation for `CITIES [re]DEFINED` and `HARLEM, NYC`.[S7][P6][S1][P7]
- Archive snippets with truncated titles often preserve the existence of a project but not the data logic, which makes historical comparison difficult.[S1]

## Win tactics

- Name the core data sources directly in the public-facing artifact.
- Explain why each major dataset is necessary for the claim the project makes.
- Prefer data complexity that is legible: judges should be able to see why the dataset is unusually strong.
- Include at least one limitation or boundary note so the documentation reads as rigorous rather than merely promotional.[P5][P8]
- When using multiple datasets, show how they fit together analytically instead of listing them as credentials.[P3][P8]

## Future-submission checklist

- Are the core datasets named explicitly?
- Can a judge see the temporal, spatial, or sensor-level specificity of the data?
- Is the data complexity real and relevant, not ornamental?
- Does the artifact explain how the data support the question?
- Are limitations or resolution constraints acknowledged where they matter?

## Citations and notes

- Source IDs reuse the inventory in `fisher/feature-matrix.md`.
- The strongest data examples in the accessible set are concentrated in [P2], [P3], [P5], and [P8].
