# 4. Why food can be treated as spatial data

## PASTE TEXT

# Why food can be treated as spatial data

Food is local, mobile, ecological, social, and historical. Ingredients are grown in environments, moved through markets, adapted through technique, and written into recipes that circulate through platforms. That makes food a rich but complicated spatial signal.

This project does not claim that a recipe corpus captures everything about a cuisine. A cuisine is not a country, and a cuisine label is not a precise polygon. “Chinese,” “Mexican,” “Brazilian,” or “Southern U.S.” are broad culinary labels, not exact spatial units. The project therefore treats cuisine labels as approximate cultural-geographic anchors, not as exact representations of nations or communities.

The spatial question emerges because similarity is not evenly distributed. Some similarities are unsurprising: neighboring cuisines may share crops, markets, climate zones, techniques, or regional histories. Other similarities are less expected, especially when two cuisines are distant or separated by water, terrain, or subregional boundaries. The goal is not to explain every similarity historically. The goal is to build a spatial screen that shows where similarity is expected and where it becomes interesting.

The data pipeline makes this possible. Recipes are grouped by cuisine label. Ingredients are normalized so that related ingredient strings can be compared. Generic pantry terms are removed or downweighted so that common recipe vocabulary does not dominate the result. Each cuisine is then represented as a vector of ingredient frequencies.

At that stage, the project has a food dataset. It becomes a GIS project only when the ingredient profiles are connected to geography: cuisine anchors, pairwise distances, residuals, corridor maps, focused cases, boundary diagnostics, topographic context, and bridge roles.

## EDITOR NOTE

Recommended ArcGIS block: Text section. Consider a side note titled “Scope note” with the cuisine-label caveat.

## PASTE CALLOUT

> Scope note: cuisine labels are approximate cultural-geographic anchors, not exact countries.
