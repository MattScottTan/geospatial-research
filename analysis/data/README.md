# analysis/data

Small reference extracts, derived from the two submissions so the research track has a
stable empirical input that does not move if a submission is revised. Total 40 KB — the
full datasets stay in `../../eip/data/` and `../../fisher/analysis/working_data/`.

| File | Contents | Derived from |
|---|---|---|
| `ai_cities_319.csv` | 319 unique AI-linked cities: id, name, country, lat/lon, summed AI works, `log_works`, distance to nearest cloud region, population | `eip/data/raw/city_access_ai.csv`, aggregated from 328 matches by the same `groupby("id").sum()` the eip pipeline uses |
| `cuisine_matrices.npz` | 20 cuisine labels plus the 20×20 `distance`, `similarity` and `residual` matrices | `fisher/analysis/working_data/*.npy` |

Regenerate with the extraction block in the commit that added this directory, or read
straight from the submissions — they are unchanged.

These are the two real spatial configurations available for testing the band-matrix
predictions: one moderately large and irregular (n = 319, global), one small and dense
(n = 20, matrices already built). Neither is large enough to see an asymptotic regime,
which is the honest limitation — they are for checking that a method behaves sensibly,
not for confirming a scaling law.
