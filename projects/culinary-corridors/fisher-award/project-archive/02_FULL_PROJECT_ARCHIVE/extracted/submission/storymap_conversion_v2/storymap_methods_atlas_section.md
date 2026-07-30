# How the Culinary Atlas Works — Standalone Methods Section

## PASTE TEXT

# How the culinary atlas works

The atlas is built in four stages.

**Stage 1: Build cuisine profiles.** The project starts with a cuisine-labeled recipe dataset derived from the What’s Cooking / Kaggle-Yummly family of data. The prototype retained 39,774 recipes, 428,249 recipe-ingredient rows, 20 cuisine labels, and 5,936 normalized ingredient labels. These figures describe prototype coverage, not population-level representativeness. Each cuisine is converted into a filtered ingredient profile: a vector that records how frequently normalized ingredients appear in that cuisine’s recipes.

**Stage 2: Measure cuisine similarity.** Cuisine profiles are compared using cosine similarity, with Jaccard similarity used as a robustness check. Cosine similarity asks whether two cuisine profiles point in a similar direction in ingredient space. Jaccard similarity asks how much overlap exists in the set of retained ingredients. Together, these metrics answer the non-spatial question: which cuisines share ingredient repertoires?

**Stage 3: Add geography.** Each cuisine label is assigned an approximate geographic anchor. These anchors are necessary for a global comparison, but they are not treated as exact nation-state locations. For each cuisine pair, the project calculates geographic distance and creates a dyadic table with cuisine pair, similarity, distance, and regional metadata.

**Stage 4: Model residual corridors.** Cuisine similarity is modeled against log geographic distance. The filtered distance model used 190 cuisine dyads and returned a negative log-distance coefficient of -0.1158 with an R-squared of 0.3553. This means distance explains a meaningful share of cuisine similarity, but not all of it. The unexplained part is the residual:

**Residual = observed cuisine similarity − distance-predicted cuisine similarity**

Positive residuals identify cuisine pairs that are more similar than distance alone predicts. These are the candidate culinary corridors. The global map identifies candidates; the focused East/Southeast Asia case provides the strongest spatial interpretation; the residual bridge index converts pairwise residuals into mapped place-level roles; and the Run 5 relief map adds topographic and coastal context for the strongest focused case.

The method is intentionally transparent. It does not try to infer hidden history from food data alone. It asks a narrower and more defensible question: where does food similarity exceed geographic expectation?

The staged design also protects the project from overinterpretation. At no point does the model jump directly from ingredients to historical explanation. It first asks a measurable spatial question, then uses the maps to decide where interpretation is reasonable. This is why the StoryMap can be comprehensive without becoming speculative.

## PASTE CALLOUT

> A cuisine pair becomes a candidate corridor only after ingredient similarity is compared with geographic distance.

The staged workflow is also designed to be auditable. Each stage creates an object that can be inspected: a cuisine-ingredient matrix, a similarity matrix, a distance-pair table, a residual-corridor table, and then a map. This matters for Fisher because the maps are not decorative outputs added after the analysis; they are the visible form of the spatial comparison.

## EDITOR NOTE

Recommended ArcGIS block: Long text section, preferably broken into four short subsections or a sidecar with four panels.
