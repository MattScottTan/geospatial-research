# Sources, Credits & Tools

> Ready-to-paste closing section for the "Cloudy with a Chance of Compute" StoryMap.
> Covers: Data Sources table, Tools & Software, Bibliography, Open Science, Acknowledgments, and Author bio placeholder.

---

## Data Sources

| Dataset | Provider | Date / Version | Coverage | Access |
|---------|----------|---------------|----------|--------|
| Populated places (cities) | Natural Earth | v5.1.1 (2022) | 8,000+ cities globally, with coordinates and population estimates | naturalearthdata.com |
| AWS cloud region locations | Amazon Web Services | Compiled from public documentation, current as of February 2026 | All deployed AWS regions worldwide | aws.amazon.com/about-aws/global-infrastructure |
| Azure cloud region locations | Microsoft Azure | Compiled from public documentation, current as of February 2026 | All deployed Azure regions worldwide | azure.microsoft.com/en-us/explore/global-infrastructure/geographies |
| Google Cloud region locations | Google Cloud Platform | Compiled from public documentation, current as of February 2026 | All deployed GCP regions worldwide | cloud.google.com/about/locations |
| AI research activity (publications) | OpenAlex | Queried for AI-classified works, 2020–2025, matched to cities by institutional affiliation | 328 matched AI-linked cities (319 unique) | openalex.org |
| Country boundaries | Natural Earth Admin 0 | ne_110m_admin_0_countries | Global | naturalearthdata.com |
| Basemaps | Esri (Light Gray Canvas) | 2026 | Global | ArcGIS Online |

**Notes on data construction:**
- Cloud region locations were compiled manually from each hyperscaler's public infrastructure documentation. Only deployed (live) regions were included; announced or planned regions were excluded. 60+ regions are mapped across the three providers.
- City-to-cloud distances are geodesic great-circle distances calculated in Python (GeoPy) and verified in ArcGIS Pro.
- OpenAlex AI-city matching uses institutional affiliation geocoding. A city is "AI-linked" if at least one institution in that city has recent AI-classified publications (2020–2025). Works are aggregated to unique cities for spatial diagnostics.
- The Compute Opportunity Bundle Index combines five components: proximity to nearest cloud region (40%), provider diversity within threshold distance (15%), redundancy / total cloud regions within reach (15%), urban scale / city population (15%), and institutional depth from the OpenAlex overlay (15%). Each component is normalized to a 0–100 scale and combined as a weighted sum.

---

## Tools & Software

### ArcGIS Pro
- **Spatial Autocorrelation (Global Moran's I)** — Spatial Statistics toolbox > Analyzing Patterns. Used to test whether the global pattern of AI works across cities is clustered, dispersed, or random. Result: I = 0.066, z = 2.86, p = 0.008.
- **Hot Spot Analysis (Getis-Ord Gi*)** — Spatial Statistics toolbox > Mapping Clusters. Used to identify statistically significant spatial clusters of high and low AI research activity. Result: 7 hot spots, 33 cold spots.
- **Cluster and Outlier Analysis (Anselin Local Moran's I)** — Spatial Statistics toolbox > Mapping Clusters. Used as a supplementary diagnostic to classify cities into HH, LL, HL, and LH cluster types.
- Data projection, layer management, and spatial joins.

### ArcGIS Online
- Interactive web map authoring and publication (Map Viewer).
- Hosted feature layers: `ai_access_cities`, `cloud_regions`, `priority_cities`, `cities_with_hotspots`.
- Create Buffers tool (500 km buffer rings around cloud regions).
- StoryMap authoring and publication.

### ArcGIS StoryMaps
- Narrative design, sidecar layout, embedded interactive web maps, and public sharing.

### Python (data processing and validation)
- **GeoPy** — geodesic great-circle distance calculation for all city-to-cloud-region pairs.
- **PySAL** — spatial weights construction and spatial autocorrelation (Moran's I) as independent validation of ArcGIS Pro results.
- **SciPy** — Kolmogorov-Smirnov test, Mann-Whitney U test, chi-square test of independence.
- **NumPy / Pandas** — data wrangling, aggregation, and statistical computation.
- **Matplotlib** — static figure generation (histograms, scatter plots, bar charts, coefficient comparison plots).
- **GPyTorch / PyTorch** — Gaussian Process spatial regression model.
- **PyMC / ArviZ** — Conditional Autoregressive (CAR/GMRF) spatial regression model.
- **Geopandas** — geospatial data handling and GeoJSON/GeoPackage export.

**Validation approach:** Spatial statistics (Moran's I, Getis-Ord Gi*) were run in both ArcGIS Pro and Python (PySAL/SciPy), with consistent results across implementations. ArcGIS Pro is cited as the primary tool; Python served as independent validation.

---

## Bibliography

[1] McKinsey & Company. (2025). "Generative AI: The next S-curve for the technology sector?" *McKinsey Digital*.

[2] CSIS (Center for Strategic and International Studies). (2025). "The Global Data Center Buildout." *CSIS Strategic Technologies Program*.

[3] International Monetary Fund. (2024). "AI Will Transform the Global Economy. Let's Make Sure It Benefits Humanity." *IMF Blog*.

[4] International Monetary Fund. (2025). "Broadening the Gains from Generative AI: The Role of Fiscal Policy." *IMF Fiscal Monitor*, April 2025.

[5] United Nations Conference on Trade and Development (UNCTAD). (2024). *Technology and Innovation Report 2024*.

[6] World Economic Forum. (2025). "The Global Risks Report 2025." *WEF Insight Report*, 20th Edition.

[7] United Nations Conference on Trade and Development (UNCTAD). (2024). "Are developing countries missing the artificial intelligence boat?" *UNCTAD Policy Brief*.

[8] Smart Nation Singapore. (2023). *National AI Strategy 2.0: AI for the Public Good, for Singapore and the World*. Singapore Government.

[9] Infocomm Media Development Authority (IMDA). (2024). "Data Centre Call for Application." Singapore Government.

[10] Infocomm Media Development Authority (IMDA). (2024). "Green Data Centre Roadmap." Singapore Government.

[11] Singapore Internet Exchange (SGIX). (2025). "About SGIX." sgix.sg.

[12] National University of Singapore. (2024). "NUS Artificial Intelligence Institute Established." NUS News.

[13] Nanyang Technological University. (2025). "Artificial and Augmented Intelligence Research Cluster." NTU Research.

[14] Amazon Web Services. (2026). "AWS Global Infrastructure: Regions and Availability Zones." aws.amazon.com/about-aws/global-infrastructure.

[15] Microsoft Azure. (2026). "Azure Global Infrastructure: Geographies." azure.microsoft.com/en-us/explore/global-infrastructure/geographies.

[16] Google Cloud. (2026). "Google Cloud Locations." cloud.google.com/about/locations.

[17] IDA Ireland. (2025). "Technology, Media & Telecommunications." idaireland.com.

[18] CeADAR — Ireland's Centre for Applied AI. (2025). "About CeADAR." ceadar.ie.

[19] Trinity College Dublin. (2025). "AI and Data Science Research." tcd.ie.

[20] University College Dublin. (2025). "School of Computer Science: AI Research." ucd.ie.

[21] Government of Vietnam. (2021). *National Strategy on Research, Development, and Application of Artificial Intelligence to 2030*. Decision No. 127/QD-TTg.

[22] VinAI Research. (2025). "About VinAI." vinai.io.

[23] VinAI Research. (2025). "Publications." vinai.io/publications.

[24] Vietnam National University — Ho Chi Minh City (VNU-HCM). (2025). "Research Priorities." vnuhcm.edu.vn.

[25] Submarine Cable Networks. (2025). "Vietnam Submarine Cable Map." submarinecablemap.com.

[26] Vietnam Internet Network Information Centre (VNNIC). (2025). "VNIX and Internet Infrastructure in Vietnam." vnnic.vn.

[27] Amazon Web Services. (2026). "AWS Regions in Africa." aws.amazon.com/about-aws/global-infrastructure/regions_az (Africa).

[28] World Bank. (2024). "Nigeria: Improving Access to Reliable and Affordable Electricity." worldbank.org.

[29] Submarine Networks. (2025). "Google's Equiano Cable Lands at OADC Lagos." submarinenetworks.com.

[30] Internet Exchange Point of Nigeria (IXPN). (2025). "IXPN Annual Report." ixpn.org.ng.

[31] Partech Partners. (2025). *2025 Africa Tech Venture Capital Report*. partechpartners.com.

---

## ⚠️ BIBLIOGRAPHY NOTE

> **The references above are reconstructed from the in-text citations [1]–[31] in the StoryMap PDF. Please verify each entry against your original bibliography and correct any titles, dates, authors, or URLs before final submission.** If you have the original bibliography file, paste it in and I will reconcile it with the in-text citations.

---

## Open Science

The data processing pipeline, statistical tests, and spatial analysis code behind this atlas are available for review and replication:

- **Analysis pipeline:** Python scripts for distance computation, OpenAlex matching, distributional tests, spatial diagnostics, spatial regression, and bundle index construction.
- **Data outputs:** City-level datasets with computed distances, AI works counts, Gi* classifications, and bundle scores.
- **Reproducibility:** Spatial statistics results (Moran's I, Getis-Ord Gi*) were validated across both Python (PySAL/SciPy) and ArcGIS Pro implementations, with consistent cluster assignments.

*[INSERT LINK: GitHub repository or Harvard Dataverse DOI, if publishing]*

We believe reproducibility strengthens geographic research.

---

## Acknowledgments

*[To be completed — suggested template:]*

This project was developed as part of [COURSE / PROGRAM] at Harvard University. The author thanks [FACULTY ADVISOR] for guidance on spatial analysis methodology, the Harvard Center for Geographic Analysis (CGA) for access to ArcGIS Pro and the Esri Innovation Program, and [ANY OTHER ACKNOWLEDGMENTS — data providers, peer reviewers, etc.].

Cloud region data was compiled from public documentation maintained by Amazon Web Services, Microsoft Azure, and Google Cloud Platform. AI research activity data was sourced from OpenAlex, an open scholarly metadata index. City population and boundary data was sourced from the Natural Earth project.

---

## Author

**Matthew Scott Tan**
*[Program, Harvard School]*

*[40–80 word bio — suggested draft:]*

Matthew Tan is a [degree program] student at Harvard [School]. His research focuses on the spatial dimensions of technology infrastructure and digital inequality. "Cloudy with a Chance of Compute" grew from a question about whether the physical geography of cloud computing — where data centers are actually located — corresponds with observable patterns in AI research activity across the global city system. This project uses ArcGIS Pro, ArcGIS Online, and Python to map that relationship across 8,000 cities.

*[INSERT: Professional headshot]*

---

## How to Cite This Project

Tan, M. S. (2026). *Cloudy with a Chance of Compute: Mapping the hidden geography of AI compute across 8,000 cities — and who it leaves behind.* ArcGIS StoryMap. Harvard University. https://storymaps.arcgis.com/stories/744a1c433d554cef8b3861d72836fdd2
