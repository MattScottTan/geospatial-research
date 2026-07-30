# 7. Finding 1: distance matters, but incompletely

## PASTE TEXT

# Finding 1: distance matters, but incompletely

A raw cuisine-similarity matrix can show that two cuisines share ingredients, but it cannot tell us whether that similarity is surprising. For that, the project needs a geographic baseline.

The distance model asks whether cuisine similarity changes as geographic distance increases. If nearby cuisines tend to be more similar, then distance explains part of the pattern. If some distant pairs remain highly similar, or some nearby pairs are less similar than expected, those differences become analytically important.

The model is intentionally simple. It estimates cuisine similarity as a function of log geographic distance. The goal is not to produce a final causal model of cuisine formation. The goal is to create a transparent baseline so the project can ask which similarities exceed spatial expectation.

This is where the residual logic begins. For each cuisine pair, the model produces a predicted similarity based on distance. The observed similarity is then compared to the predicted value. Positive residuals identify pairs that are more similar than distance alone predicts. Negative residuals identify pairs that are less similar than expected.

The figure in this section explains that logic visually. It shows the distance baseline and the gap between expected and observed similarity. That gap is the core of the atlas. Without it, the project would only rank similar cuisines. With it, the project can map spatial surprise.

The finding is modest but important: geography matters, but geography does not explain everything. That incomplete relationship is exactly what makes residual corridors meaningful.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_method_or_model_figure.png`. Recommended ArcGIS block: Image plus text. This is the key methods/result bridge.

## PASTE CAPTION

The residual method compares observed ingredient similarity with similarity predicted from geographic distance. Positive residuals are cuisine pairs that are more similar than the distance baseline predicts. The project maps those positive residuals as candidate culinary corridors.

## PASTE CALLOUT

> The model does not explain cuisine history. It creates a spatial expectation against which cuisine similarity can be compared.
