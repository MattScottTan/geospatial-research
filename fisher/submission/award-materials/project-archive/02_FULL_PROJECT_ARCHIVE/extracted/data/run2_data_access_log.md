# Run 2 Data Access Log

Created: 2026-04-28  
Date accessed for all sources below unless noted otherwise: 2026-04-28.

| Dataset / Source | Provider | URL | Date accessed | Access status | Local path | License / usage note | Reliability grade | Next action |
|---|---|---|---|---|---|---|---|---|
| What’s Cooking prepared long table | Zelený / anadat-r GitHub; original Kaggle/Yummly | https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_long.txt | 2026-04-28 | Downloaded | `data/raw/recipes_long.txt` | Public GitHub text file; original Kaggle/Yummly provenance creates redistribution/terms risk | B- | Use for prototype; verify final-use permissions in Run 3 |
| What’s Cooking cuisine × ingredient table | Zelený / anadat-r GitHub; original Kaggle/Yummly | https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_cuisines.txt | 2026-04-28 | Downloaded | `data/raw/recipes_cuisines.txt` | Same as above | B- | Use for cross-checking only |
| What’s Cooking cuisine counts | Zelený / anadat-r GitHub; original Kaggle/Yummly | https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_cuisines_count.txt | 2026-04-28 | Downloaded | `data/raw/recipes_cuisines_count.txt` | Same as above | B- | Use for sample-size checks |
| What’s Cooking documentation | Analysis of Community Ecology Data in R | https://www.davidzeleny.net/anadat-r/doku.php/en:data:recipes?rev=1683202162 | 2026-04-28 | Metadata verified | n/a | Documentation states Kaggle/Yummly source and describes the prepared files | B | Cite and use to explain source limitations |
| TheMealDB API | TheMealDB | https://www.themealdb.com/api.php | 2026-04-28 | Metadata verified; fallback only | n/a | Free test key for development/educational use; public release may require supporter key depending use | B | Keep as fallback or supplementary examples |
| CEPII GeoDist | CEPII | https://www.cepii.fr/cepii/en/bdd_modele/bdd_modele_item.asp?id=6 | 2026-04-28 | Metadata verified; country file downloaded | `data/external/geo_cepii.xls` | CEPII page lists Etalab 2.0 license; not parsed in this prototype because `.xls` support is not installed in the Python environment | A | Use as Run 3 candidate for official coordinates/language/colonial variables |
| Natural Earth | Natural Earth / NACIS | https://www.naturalearthdata.com/ | 2026-04-28 | Metadata verified; not downloaded | n/a | Public domain map data | A | Use in Run 3 for polished cartography |
| UN M49 regional classification | United Nations Statistics Division | https://unstats.un.org/unsd/methodology/m49/overview/ | 2026-04-28 | Metadata verified; manually joined for 20 cuisine-country labels | `data/crosswalks/cuisine_geo_crosswalk.csv` | Official UN country/area statistical classification | A | Use as the one Run 2 explanatory overlay |
| FlavorDB | IIIT-Delhi / CoSyLab | https://cosylab.iiitd.edu.in/flavordb/ | 2026-04-28 | Metadata verified; not downloaded | n/a | CC BY-NC-SA 3.0 listed on site; bulk access not confirmed | A- | Defer to Run 3 unless ingredient matching is validated |
| FooDB | Wishart/TMIC/University of Alberta ecosystem | https://foodb.ca/ | 2026-04-28 | Metadata verified; not downloaded | n/a | Freely accessible; commercial redistribution requires permission; CC BY-NC 4.0 shown | A- | Possible Run 3 backup for flavor chemistry |

