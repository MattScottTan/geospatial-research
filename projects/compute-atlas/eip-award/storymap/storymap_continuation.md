# StoryMap Continuation — Paste after Singapore section

---

## Dublin: Near compute / lower AI than infrastructure density suggests

**Distance: 0.0 km | Providers within 500 km: 3 | Cloud regions within 1,000 km: 13 | OpenAlex AI works: 179 | Bundle score: 85.3/100**

Dublin is almost the mirror image of Singapore on the infrastructure side — but not on the research-output side. It sits effectively on top of AWS eu-west-1, inside Azure North Europe, and within a dense UK–Benelux–Paris corridor that brings three providers and thirteen cloud regions within 1,000 km. On raw proximity alone, Dublin scores a perfect 100.

[INSERT: dublin_regional_context.png — caption below]

> Dublin: regional compute context. The map makes the cloud-density pattern visible: Dublin sits on AWS Ireland, Azure North Europe, and the wider UK–Benelux–Paris corridor. Distance rings at 500 km and 1,000 km show the extraordinary regional density. Nearby cities include London, Birmingham, Leeds, Paris, and Berlin — each surrounded by its own cluster of cloud regions.

[INSERT: dublin_local_ecosystem.png — caption below]

> Dublin: bundle scorecard. The scorecard shows how little the city trails the strongest global hubs on infrastructure while remaining more modest on institutional depth and urban scale. Green bars indicate where Dublin exceeds the top-100 median; the red bar on urban scale marks its one visible shortfall.

The scorecard tells a clear story. Dublin matches or exceeds the top-100 bundle median on proximity (100), provider diversity (100), and redundancy (97). But on urban scale it trails visibly (47 versus the reference of 61), and on institutional depth it sits modestly above the median (58 versus 38) — a gap that is far narrower than its infrastructure lead would suggest. Dublin City University is the sole leading anchor in the delivered overlay, with 179 AI works.

The mechanism is consistent with how Ireland built its technology economy. AWS confirms that eu-west-1 is the Ireland region, Microsoft places North Europe in Ireland, and Google's locations page shows a nearby European corridor anchored in London and Belgium rather than a Dublin-specific Google region. IDA Ireland markets the country as an English-speaking EU base with strong talent, infrastructure, and research linkages for multinational operations. That helps explain why Dublin is exceptionally strong as a hosting and service node: the infrastructure was attracted by regulatory and tax conditions, not solely by local research demand.

But hosting is not the same as producing AI research at the scale of London or Paris. Ireland does have a real research ecosystem. CeADAR describes itself as Ireland's Centre for Applied AI, Trinity College Dublin advertises broad AI research in computer science, and University College Dublin highlights machine learning and AI across multiple schools. The point is not that Dublin lacks AI capacity. It is that its cloud footprint is even larger than its scholarly footprint — and that asymmetry is exactly why Dublin belongs in the case set.

**Takeaway:** Dublin shows that compute proximity can be necessary and still not sufficient. A city can host the infrastructure more fully than it produces visible AI research. In the language of the bundle, Dublin has maximum infrastructure but more modest institutional mass — a reminder that the atlas measures opportunity conditions, not guaranteed outcomes.

---

## Ho Chi Minh City: Farther from compute / high AI

**Distance: 1,096.8 km | Providers within 1,000 km: 0 | Cloud regions within 1,500 km: 3 | OpenAlex AI works: 373 | Bundle score: 61.7/100**

Ho Chi Minh City is the clearest case in the atlas that beats the simple distance story. It sits 1,097 km from the nearest major cloud region — AWS ap-southeast-1 in Singapore — and has no providers or cloud regions inside the 1,000 km threshold. Yet the OpenAlex overlay records 373 recent AI works and two top institutional anchors. Its bundle score of 61.7 is well below Singapore or Dublin, but far above what a pure proximity ranking would predict. In the Gi* analysis, the city is classified as not significant rather than a hot spot — making it a quiet overperformer rather than a statistical anomaly.

[INSERT: Ho Chi Minh City regional compute context map — caption below]

> Ho Chi Minh City: regional compute context. The map shows the city's separation from the Singapore corridor. All major cloud regions — AWS, Azure, and GCP — cluster around Singapore and Jakarta, more than 1,000 km away. The 500 km and 1,000 km rings are empty. But the 1,500 km ring captures three regions, and submarine cable infrastructure connects Vietnam into the broader Southeast Asian network corridor.

[INSERT: Ho Chi Minh City bundle scorecard — caption below]

> Ho Chi Minh City: bundle scorecard. The scorecard shows how urban scale and institutional depth partly offset weaker proximity. The city trails the top-100 reference on proximity, provider diversity, and redundancy, but rises on scale and approaches the reference on institutional depth — a profile that distance alone would miss entirely.

The mechanism driving this overperformance is institutional and networked, not local-cloud based. Vietnam's national AI strategy for 2021–2030 sets an explicit goal of making the country an innovation and AI development centre in ASEAN and the world. VinAI, a leading Vietnamese AI research lab, places nearly 200 researchers and engineers across Hanoi and Ho Chi Minh City, and reports 88 top-tier publications in its first three years — including papers at CVPR, NeurIPS, ICML, and ICLR. VNU-HCM's institutional strategy likewise frames the university as a high-quality research and technology hub with AI among its priority areas.

The regional map explains why institutional build-out does not imply isolation. Vung Tau's cable landing stations sit roughly 125 km from Saigon, and Vietnam's national internet exchange infrastructure includes VNIX exchange points and root-server infrastructure in Ho Chi Minh City. The city is farther from hyperscaler regions in kilometres than it is from the wider Southeast Asian network corridor that connects Vietnam into Singapore and the broader region. In practice, a research team in Ho Chi Minh City can access Singapore-hosted cloud resources with tolerable latency — not ideal, but workable for training runs that do not require sub-millisecond response.

**Takeaway:** Ho Chi Minh City shows that institutional depth and regional network connectivity can offset weaker compute proximity, even when a city sits outside the atlas's core cloud corridor. It is the most important case for showing that the distance-activity relationship is real but not deterministic — and that the bundle framework captures nuance that a single-variable map cannot.

---

## Lagos: Far from compute / absent from the AI overlay

**Distance: 3,842.6 km | Providers within 1,000 km: 0 | Cloud regions within 1,500 km: 0 | OpenAlex AI works: 0 | Bundle score: 27.8/100**

Lagos is the stacked-disadvantage case — and the reason the priority-city screen exists. It is one of the largest and fastest-growing cities in the world, with a population exceeding 15 million, yet the current atlas places its nearest major cloud region in Madrid at 3,842.6 km. It has zero providers and zero cloud regions within 1,000 km, zero observed AI works in the delivered overlay, and no top-institution anchors. Because Lagos is absent from the AI-research overlay entirely, it does not receive a Gi* classification. The scorecard reads as a large market sitting outside the active compute corridor, not as a weak city per se.

[INSERT: Lagos regional compute context map — caption below]

> Lagos: regional compute context. The map makes the West Africa gap visible. The nearest cloud regions — GCP europe-southwest1 in Madrid, Azure South Africa North in Johannesburg — sit thousands of kilometres away. The 1,000 km and 2,000 km rings are empty. Only the 4,000 km ring captures any cloud infrastructure, and that infrastructure is in Europe and southern Africa. Kinshasa and Luanda, two of Africa's largest cities, face similar or worse isolation.

[INSERT: Lagos bundle scorecard — caption below]

> Lagos: bundle scorecard. Urban scale is the only component where Lagos resembles the top-100 bundle cities. Proximity, provider diversity, redundancy, and institutional depth all sit far below the reference profile. The scorecard makes the stacked nature of the disadvantage visible: this is not a city that is weak on one dimension and strong on others. Every infrastructure component trails simultaneously.

The mechanism is not simple absence of connectivity. Hyperscaler regions serving Africa remain concentrated far from West Africa: only South Africa hosts major cloud regions from all three providers. Nigeria faces a compounding infrastructure constraint that matters directly for compute — the World Bank describes the country's unreliable and often inaccessible power supply as a threat to economic growth. That combination — long compute distance plus weak electricity reliability — helps explain why local cloud depth has lagged.

Yet Lagos is not disconnected from the digital economy. Multiple submarine cables land in Nigeria, including Google's Equiano cable at OADC Lagos, and the Internet Exchange Point of Nigeria (IXPN) reports significant gains from local peering. Nigeria also remains one of Africa's densest startup markets: Partech's 2025 Africa Tech report recorded the continent's second-highest equity deal count in Nigeria. The point is not that Lagos lacks demand or digital activity. It is that bandwidth, startup energy, and urban scale have not yet been matched by local hyperscaler compute infrastructure.

This is exactly what the priority screen is designed to surface. Lagos is not an edge case — it is the archetype of the pattern identified in Finding 4. A large, fast-growing city with real digital activity, but where compute distance and other infrastructure frictions compound in the same place.

**Takeaway:** Lagos shows what stacked disadvantage looks like on the ground — and why the atlas's priority-city layer matters for public-interest infrastructure geography. The absence from the AI overlay is not a verdict on the city's potential. It is a signal that the infrastructure conditions for AI participation are currently least favorable where urban demand may be growing fastest.

---

## What the four cases show together

Together, the four cases do the explanatory work that regression coefficients alone cannot do.

**Singapore** shows full-stack alignment — what happens when proximity, redundancy, institutions, and national strategy reinforce one another by design.

**Dublin** shows the hosting–producing distinction — that a city can sit on top of cloud infrastructure and still not translate that into proportional AI research output.

**Ho Chi Minh City** shows that institutional depth and network corridors can lift a city well above what its raw distance position would predict — the most important evidence that the relationship is real but not deterministic.

**Lagos** shows why the priority screen matters — a large city with genuine digital activity where every infrastructure dimension trails simultaneously.

That is why the atlas's final claim is about bundles rather than single causes. Distance matters, but it is not destiny. What matters more is the broader infrastructure environment — proximity, diversity, redundancy, institutional depth, and scale — and whether those conditions reinforce one another or leave gaps that distance alone cannot explain.

---

## Conclusion: Compute is not destiny, but it shapes the map

This atlas began with a simple observation: the cloud is not placeless. It is built from datacenter regions, network capacity, and supporting institutional ecosystems that are unevenly distributed across the world's cities. The analysis that followed tested whether that unevenness corresponds with observable differences in AI research activity — and found that it does.

Across the 8,000-city global frame, AI-linked cities sit much closer to major cloud infrastructure than the broader city system. The median AI-linked city is 237 km from its nearest cloud region; the median large city is 657 km away. The concentration sharpens when weighted by research volume: 81 percent of all observed AI works fall within 500 km of a major cloud region. The pattern is spatially structured, not randomly distributed. And the relationship survives two spatial regression specifications that control for city size and geographic dependence.

The priority-city screen identifies 1,988 cities across 125 countries where zero observed AI works and above-threshold compute distance converge — including some of the world's largest and fastest-growing urban centres. The Compute Opportunity Bundle Index then extends the analysis beyond raw distance, showing that the cities with the strongest AI research environments are not simply close to one cloud region, but sit inside broader ecosystems where proximity, provider diversity, redundancy, institutional depth, and urban scale reinforce one another.

The four case studies translate these patterns into place-based narratives. Singapore confirms the bundle. Dublin complicates it. Ho Chi Minh City challenges the distance story. Lagos shows what the atlas is ultimately for: making visible the places where the infrastructure conditions for AI participation are currently least favorable — and where that gap may matter most.

This project does not claim that compute proximity alone determines whether a city succeeds in AI. It does not claim that every city far from compute is excluded, or that every city near compute will become an AI hub. What it does claim — with evidence from 8,000 cities, spatial diagnostics, regression controls, a composite index, and four detailed cases — is that cloud compute infrastructure is a meaningful and underappreciated part of the geography of AI opportunity. Ignoring it leaves part of the map invisible.

For planners, innovation agencies, and international development organisations, the atlas offers a practical starting point: a screening tool that identifies where infrastructure investment could address the starkest mismatches between urban scale and compute accessibility. For researchers, it offers a reproducible framework for studying how physical infrastructure shapes digital opportunity. And for anyone asking where AI is headed next, it offers a reminder that the answer depends in part on where the cloud actually is.

---

## Data and methods summary

**City frame:** 8,000 largest cities globally (Natural Earth / SimpleMaps worldcities.csv)

**Cloud infrastructure:** 111 regions — 29 AWS, 47 Azure, 35 Google Cloud (public documentation, early 2026)

**AI research overlay:** OpenAlex scholarly record (2020–2025), filtered by three AI topic IDs (NLP Techniques, ML in Bioinformatics, Neural Networks and Applications), matched to city frame within 75 km; 328 matched cities, 319 unique geometries

**Access measure:** Great-circle geodesic distance from each city to its nearest cloud region

**Spatial diagnostics:** Global Moran's I (I = 0.066, z = 2.86, p = 0.008); Getis-Ord Gi* hot spot analysis (7 hot spots, 33 cold spots)

**Regression specifications:** Gaussian Process model (distance β = −0.207, population β = +0.279); CAR/GMRF model (distance β = −0.052, population β = +0.309)

**Bundle index:** Weighted composite of proximity (40%), provider diversity (15%), redundancy (15%), urban scale (15%), institutional depth (15%); scored 0–100

**Priority screen:** Zero observed AI works + distance ≥ 75th percentile (1,252 km); flags 1,988 cities across 125 countries

**Tools:** ArcGIS Online, ArcGIS Pro, Python (spatial analysis and data processing)

---

## References

[1] McKinsey & Company. (2025). Data center investments: The rising cost of hyperscaler infrastructure.

[2] Synergy Research Group. (2025). Hyperscale data center capex.

[3] International Monetary Fund. (2024). AI and the Economy.

[4] International Monetary Fund. (2025). Technology access and economic divergence.

[5] Stanford HAI. (2025). AI Index Report 2025.

[6] OECD. (2023). A Blueprint for Building National Compute Capacity for Artificial Intelligence.

[7] United Nations Conference on Trade and Development. (2024). Digital Economy Report.

[8] Smart Nation Singapore. National AI Strategy 2.0. https://www.smartnation.gov.sg/initiatives/national-ai-strategy/

[9] Singapore EDB. Singapore pilots sustainable way to grow data centre capacity. https://www.edb.gov.sg/

[10] IMDA. Singapore's Green Data Centre Roadmap. (2024).

[11] Singapore Internet Exchange. About SGIX. https://www.sgix.sg/about-us-2/

[12] NUS Artificial Intelligence Institute. https://ai.nus.edu.sg/about-us/

[13] NTU. Artificial & Augmented Intelligence Cluster. https://www.ntu.edu.sg/research/

[14] AWS. Regions and Availability Zones. https://docs.aws.amazon.com/global-infrastructure/

[15] Microsoft Learn. List of Azure regions. https://learn.microsoft.com/en-us/azure/reliability/regions-list

[16] Google Cloud. Global Locations. https://cloud.google.com/about/locations

[17] IDA Ireland. https://www.idaireland.com/

[18] CeADAR. Who We Are. https://ceadar.ie/who-we-are/

[19] Trinity College Dublin. AI Research — School of Computer Science. https://www.tcd.ie/scss/research/

[20] University College Dublin. Data Science, ML & AI. https://www.ucd.ie/cs/research/

[21] Government of Vietnam. National Strategy on R&D and Application of AI Until 2030. (2021).

[22] VinAI. Company Profile. (2024). https://www.vinai.io/

[23] VNU-HCM. Institutional Strategy. https://vnuhcm.edu.vn/

[24] Submarine Networks. Vung Tau Cable Landing Station. https://www.submarinenetworks.com/

[25] VNNIC. VNIX-NOG 2020. https://vnnic.vn/

[26] Google Cloud Blog. New region in Johannesburg. (2024).

[27] World Bank. Nigeria Development Update. (2023).

[28] Submarine Networks. Nigeria. https://www.submarinenetworks.com/en/stations/africa/nigeria

[29] Internet eXchange Point of Nigeria. https://ixp.net.ng/

[30] Partech. 2025 Africa Tech Venture Capital Report. https://partechpartners.com/africa-reports/

[31] OpenAlex. https://openalex.org/

[32] SimpleMaps / condwanaland. worldcities dataset. https://github.com/condwanaland/worldcities/

[33] Natural Earth. https://www.naturalearthdata.com/

[34] Rasmussen & Williams. Gaussian Processes for Machine Learning. MIT Press, 2006.

[35] Besag. Spatial interaction and the statistical analysis of lattice systems. JRSS-B, 1974.

[36] OECD. Measuring Domestic Public Cloud Compute Availability for AI. (2025).
