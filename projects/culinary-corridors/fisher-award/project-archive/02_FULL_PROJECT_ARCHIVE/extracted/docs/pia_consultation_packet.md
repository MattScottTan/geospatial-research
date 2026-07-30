# Pia Sorensen Consultation Packet

## One-page project summary

**Working title:** Culinary Corridors: Mapping Food Similarity, Migration, Trade, and Flavor Chemistry

**Goal:** Build a Fisher Prize GIS project that treats food as spatial evidence. The project will represent cuisines as ingredient networks, compute similarity between places, and test whether similarity is explained by geographic proximity or by migration, trade, agricultural environment, language/colonial history, and flavor chemistry.

**Core question:** How does cuisine similarity vary across space, and when do migration, trade, agricultural environment, and flavor chemistry explain culinary resemblance better than geographic proximity?

**Planned GIS output:** A residual culinary-corridor map. First, model cuisine similarity as a function of geographic distance. Then map cuisine pairs whose similarity is higher than distance predicts. Finally, compare those corridors with migration, food trade, agriculture, and flavor chemistry.

**Why this needs food-science guidance:** Ingredient lists are not the same as flavor, and flavor compounds are not the same as perceived flavor. Cooking, fermentation, concentration, aroma thresholds, and cultural practice all matter. Pia’s guidance would help keep the science accurate and prevent overclaiming.

## Specific feedback needed from Pia

1. Which ingredient groupings are scientifically defensible for a cuisine-similarity model?
2. Which ingredients should never be collapsed, even if they look similar in text? Examples: butter/ghee, soy/miso/soy sauce, fish/fish sauce, fresh/fermented dairy.
3. Should spices, staples, oils/fats, and fermented ingredients be weighted differently?
4. Is it scientifically reasonable to compare cuisines using flavor-compound presence from databases such as FlavorDB or FooDB?
5. What caveats are necessary when treating flavor-molecule overlap as a proxy for sensory similarity?
6. How should cooking processes be handled when raw ingredients transform chemically during heating, browning, emulsification, or fermentation?
7. Which fermentation examples would best illustrate that food similarity can be driven by technique/substrate rather than geography?
8. Are there food-science datasets, papers, or course materials that would strengthen the flavor chemistry or fermentation layer?
9. What would be a scientifically accurate way to phrase the project’s thesis for a GIS audience?
10. What is the most compelling food-science “hook” for Fisher evaluators: flavor chemistry, fermentation, ingredient networks, or migration/trade of food techniques?
11. Are there known pitfalls in using online recipe datasets for scientific food analysis?
12. Which final visuals would be most credible from a science-of-food perspective?

## Scientific assumptions needing validation

- Cuisine ingredient vectors can approximate culinary similarity if limitations are made explicit.
- Ingredient co-occurrence networks can reveal meaningful culinary structure.
- Flavor-compound overlap can be used as a secondary similarity signal, but not as direct proof of perceived flavor similarity.
- Fermented foods may be structured by microbial ecology, substrate, and technique as much as geography.
- Ingredient categories and alias normalization require domain review.

## Candidate datasets/methods to ask about

- RecipeDB for global recipe/ingredient/cuisine data.
- FlavorDB / FlavorDB2 / FooDB / FSBI-DB for ingredient-compound mappings.
- Sourdough starter microbiome data and broader food microbiome atlases for fermentation sidebar.
- Ingredient taxonomy: spice, herb, staple, fat/oil, protein, dairy, fermented, condiment, vegetable/fruit.
- Chemical transformations: Maillard reactions, fermentation volatiles, acid/base effects, diffusion, emulsion, gelation, and texture.

## Draft email to Pia

Subject: Fisher Prize project idea: food geography, migration, and flavor chemistry

Dear Professor Sörensen,

I’m developing a possible Howard T. Fisher Prize GIS project and would be grateful for your advice on the food-science framing. The working idea is **Culinary Corridors: Mapping Food Similarity, Migration, Trade, and Flavor Chemistry**.

The project would represent cuisines as ingredient networks, compute similarity between regions, and then use GIS to test whether similarity is explained by geographic distance or by migration, trade, agriculture, language/colonial links, and flavor chemistry. The main map would show “culinary corridors”: places whose cuisines are more similar than geography alone predicts.

Where I especially need your guidance is on the science. I want to avoid treating ingredient overlap as if it automatically means flavor similarity. I’m considering using FlavorDB/FooDB-style ingredient-compound data as a secondary layer, and possibly a small fermentation sidebar showing how microbial practice or substrate can complicate simple geographic explanations.

Would you be willing to give feedback on a few questions?

1. Which ingredient groupings or normalizations are scientifically defensible?
2. Is flavor-compound overlap a reasonable secondary similarity measure if caveated carefully?
3. How should fermented ingredients and cooking transformations be handled?
4. Are there food-science datasets or papers you think I should use or avoid?
5. What would make this project scientifically credible rather than just a visually interesting map?

I can send a short project blueprint and dataset list before we meet. Thank you very much for considering it.

Best,
Matthew
