# Claim integrity check for revised report

This note maps the revised report's major substantive claims to existing repo outputs. It is designed to keep the lay-language rewrite faithful to the delivered evidence.

## Claim-to-evidence map

| Major claim in revised report | Support in repo | Notes / discipline check |
|---|---|---|
| Compute access is highly uneven across the 8,000-city comparison frame. | `report/figures/fig1_access_map.png`; `report/figures/fig9_distance_surface.png`; `outputs/tables/city_access_metrics.csv` | Safe as a descriptive claim. The report avoids implying that distance alone captures full access quality. |
| The median city in the 8,000-city frame is about 657 km from its nearest cloud region. | `report/main.tex` existing numeric carry-forward; `outputs/tables/city_access_metrics.csv` | Safe if phrased as a frame-level descriptive statistic. |
| AI-linked cities are systematically closer to cloud regions than the broader city system. | `report/figures/fig2_ai_map.png`; `report/figures/fig7_distance_hist.png`; `outputs/tables/city_access_ai.csv` | Safe and central. The report presents it as a descriptive comparison, not a causal result. |
| The median AI city is about 237 km from its nearest cloud region, versus 657 km for the broader frame. | `outputs/tables/city_access_ai.csv`; `report/main.tex` existing numeric carry-forward | Safe as long as the report keeps the comparison tied to the delivered overlay sample. |
| About 72% of AI cities are within 500 km of a cloud region, compared with 44% of the full frame. | `outputs/tables/city_access_ai.csv`; frame-level accessibility table used in the original report text | Safe as a descriptive share comparison. |
| When weighted by observed AI works, the weighted median distance falls to about 164 km. | `report/figures/fig8_ai_weighted_distance.png`; `outputs/tables/city_access_ai.csv` | Safe if kept as a weighted descriptive result, not a causal interpretation. |
| The matched AI-city pattern is spatially clustered, but the clustering is modest rather than overwhelming. | `report/figures/fig11_hotspot_map.png`; `report/figures/morans_i_scatterplot.png`; `outputs/tables/morans_i_summary.csv` | Safe. The report correctly says Moran's I is positive but small. |
| The unique-city diagnostic reports 7 hot spots and 33 cold spots. | `outputs/gis/cities_with_hotspots.geojson`; hotspot counts used in original report text | Safe as a restored spatial-diagnostic count. |
| The priority-city screen identifies 1,988 cities that combine zero observed AI works in the delivered overlay with above-threshold compute distance. | `report/figures/fig12_priority_cities_map.png`; `outputs/tables/priority_cities.csv` | Safe if the report preserves the screening-rule language and avoids treating the list as a forecast. |
| Cities such as Bangkok, Lagos, Kinshasa, and Lima are illustrative high-priority cases in the delivered screen. | `outputs/tables/priority_cities.csv`; `report/tables/underserved_cities.tex` | Safe as examples, not as exhaustive or normative rankings. |
| In both spatial models, the distance coefficient remains negative while the population coefficient remains positive. | `report/tables/model_coefs.tex`; `outputs/tables/model_gp_summary.json`; `outputs/tables/model_car_summary.json`; `report/figures/fig5_coef_compare.png` | Safe and central. The report should continue to describe this as an association. |
| The GP distance coefficient is about -0.206 per additional 1,000 km; the CAR/GMRF coefficient is about -0.052. | `outputs/tables/model_gp_summary.json`; `outputs/tables/model_car_summary.json`; `report/tables/model_coefs.tex` | Safe if rounded and described as model-dependent magnitude, not as a transportable causal effect. |
| Compute accessibility is a robust spatial correlate of observed AI activity. | Supported jointly by `fig7_distance_hist.png`, `fig8_ai_weighted_distance.png`, `fig11_hotspot_map.png`, `fig5_coef_compare.png`, `outputs/tables/model_gp_summary.json`, and `outputs/tables/model_car_summary.json` | Safe as the headline conclusion because it matches the evidence and does not claim causality. |
| The report does not prove that opening a cloud region would create an AI hub. | Methodological boundary supported by the observational design documented in `report/main.tex` and by the non-experimental outputs above | Keep this limitation explicit. It is a methodological statement, not a numerical claim. |

## Claims that were deliberately kept weaker in the rewrite

1. **No claim that absent cities are true zero-AI cities.**  
   The report keeps the phrase "not observed in this delivered filter" because the repository does not preserve a complete query-timing provenance for the overlay.

2. **No claim that distance is the same thing as compute quality.**  
   The report keeps the proxy warning: distance is not latency, price, GPU availability, or service breadth.

3. **No claim of causal impact from cloud-region openings.**  
   The revised report keeps the causal boundary in the abstract, opening, methods, implications, and conclusion.

4. **No claim that every flagged priority city is underserved in a normative sense.**  
   The report describes the layer as a screening rule that highlights stacked disadvantage in the delivered data.

## Final check

The revised report's major claims stay inside the evidence already present in the repo. The readability rewrite changes framing and explanation, not the underlying empirical scope.
