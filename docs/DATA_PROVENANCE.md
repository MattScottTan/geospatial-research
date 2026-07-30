# Data provenance and licensing

Checked before committing anything, because publishing a repo redistributes every input
in it. One file is excluded pending confirmation.

## projects/compute-atlas/data/raw

| File | Source | Licence | Committed |
|---|---|---|---|
| `cloud_regions_aws.csv` | AWS public infrastructure docs | factual data, compiled by hand | yes |
| `cloud_regions_azure.csv` | Azure geographies docs | factual data, compiled by hand | yes |
| `cloud_regions_gcp.csv` | Google Cloud locations docs | factual data, compiled by hand | yes |
| `ne_110m_admin_0_countries.geojson` | Natural Earth | public domain | yes |
| `openalex_ai_city_overlay.csv` | OpenAlex via `openalex/make_openalex_ai_city_overlay.py` | CC0 | yes |
| `openalex_ai_institutions_top.csv` | OpenAlex | CC0 | yes |
| `openalex_topics_used.json` | OpenAlex | CC0 | yes |
| `worldcities.csv` | SimpleMaps World Cities, Basic | CC BY 4.0 | yes |

### worldcities.csv — resolved

SimpleMaps releases this database in two forms. The free *Basic* edition is CC BY 4.0 and
may be redistributed with attribution; the paid *Pro* editions may **not** be
redistributed. The package recorded neither.

Settled by row count: the copy in `Cloudy_with_a_Chance_of_Compute_Final_Package.zip` has
**41,002 rows**, consistent with the Basic edition and far below the millions in Pro. It
is therefore CC BY 4.0 and safe to redistribute with attribution, and has been removed
from `.gitignore`.

Required attribution:

> City data © SimpleMaps (simplemaps.com/data/world-cities), Basic edition, CC BY 4.0.

### An attribution discrepancy in the published StoryMap

The StoryMap's Data Sources section states the city frame is "drawn from the Natural
Earth populated places dataset (v5.1.1)." No Natural Earth populated-places file exists in
any package — only `ne_110m_admin_0_countries.geojson`, which is country boundaries. The
only city table anywhere is `worldcities.csv`, and it is SimpleMaps.

So the published StoryMap appears to credit the wrong source for its central dataset. This
is now a correction to make rather than a question to investigate: confirm against
`src/pipeline.py`'s `prepare` stage, then add the SimpleMaps attribution above wherever
Natural Earth is currently credited for the city frame. Natural Earth remains correctly
credited for country boundaries.

## projects/culinary-corridors/data/raw

| File | Source | Licence | Committed |
|---|---|---|---|
| `cuisine_ingredient_matrix.csv` | **unknown** | **unknown** | pending |

This file sat loose in `Downloads` with no accompanying README, citation, or licence.
Cuisine–ingredient matrices in the literature usually derive from Ahn et al. (2011),
"Flavor network and the principles of food pairing" (*Scientific Reports*), whose
underlying recipe data came from commercial recipe sites with their own terms — or from
Yummly / RecipeNLG style datasets, several of which are research-use-only.

Until its origin is established, treat it as unclear to redistribute. It is small enough
that a public repo would republish it in full.

## Summary

Everything except `worldcities.csv` and `cuisine_ingredient_matrix.csv` is safe to
publish. Those two are the reason the repo defaults to private.
