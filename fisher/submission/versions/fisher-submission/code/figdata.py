"""
Data extracted from the existing project figures (run4_*, run5_*).
This is NOT new analysis — these are coordinates and values reproduced
from what is already published in the project's figures, used to render
those same artifacts in a more cartographically appropriate form.
"""

# Cuisine anchors. Coordinates approximate the labeled points in the
# existing figures (run4_hero_spatial_argument_figure and
# run4_geospatial_insight_figure show the placements).
# Format: name -> (lat, lon)
ANCHORS = {
    # East/Southeast Asia focused-case cuisines (labeled in run4_primary_case_figure)
    'Chinese':     (35.86, 104.20),
    'Japanese':    (36.20, 138.25),
    'Korean':      (35.91, 127.77),
    'Thai':        (15.87, 100.99),
    'Vietnamese':  (14.06, 108.28),
    'Filipino':    (12.88, 121.77),

    # Other anchors confirmed from run4_geospatial_insight_figure (bridge map labels)
    'Russian':     (61.52, 105.32),
    'French':      (46.23,   2.21),
    'Spanish':     (40.46,  -3.75),
    'British':     (55.38,  -3.44),
    'Irish':       (53.41,  -8.24),
    'Southern_US': (33.00, -86.00),
    'Jamaican':    (18.11, -77.30),
    'Italian':     (41.87,  12.57),
    'Brazilian':  (-14.24, -51.93),

    # Additional anchors visible as unlabeled dots in run4_geospatial_insight_figure
    # (positions read from the figure; cuisine names inferred from context).
    'Mexican':     (23.63,-102.55),
    'Cajun_Creole':(30.50, -91.20),
    'Greek':       (39.07,  21.82),
    # These two appear as small grey dots in the geospatial insight map at
    # roughly these latitudes/longitudes; identity uncertain so we render
    # them un-named.
    'Anchor_A':    (20.59,  78.96),   # likely South Asia
    'Anchor_B':    (31.79,  35.21),   # likely Levant/Mediterranean
}

# E/SE Asia focused-case top residual links (from run5_east_se_asia_topographic_corridor_map)
FOCUSED_LINKS = [
    # (a, b, residual, link_type)
    ('Thai',     'Vietnamese', 0.359, 'mainland_adjacency'),
    ('Chinese',  'Korean',     0.306, 'regional_proximity'),
    ('Filipino', 'Vietnamese', 0.209, 'island_maritime'),
    ('Filipino', 'Thai',       0.219, 'island_maritime'),
    # Plus secondary E/SE Asia links visible in the primary-case figure
    ('Chinese',  'Japanese',   0.18,  'regional_proximity'),
    ('Korean',   'Japanese',   0.20,  'regional_proximity'),
    ('Filipino', 'Korean',     0.12,  'island_maritime'),
    ('Filipino', 'Chinese',    0.11,  'island_maritime'),
]

# Long-distance residual outliers explicitly labeled in run4_method_or_model_figure
# (points sitting above the regression line, named on the figure itself).
LONG_DISTANCE_OUTLIERS = [
    ('British',  'Southern_US'),  # ~0.66 observed sim
    ('British',  'Russian'),       # ~0.65
    ('Irish',    'Russian'),       # ~0.61
    ('French',   'Russian'),       # ~0.58
    ('Italian',  'Russian'),       # ~0.58
    ('Spanish',  'Russian'),       # implied by cluster
]

# Bridge-index top scores (from run4_geospatial_insight_figure right panel).
BRIDGE_SCORES = [
    ('Filipino',    0.87),
    ('Russian',     0.84),
    ('Southern_US', 0.69),
    ('Jamaican',    0.68),
    ('French',      0.65),
    ('Spanish',     0.53),
    ('British',     0.51),
    ('Irish',       0.44),
    ('Italian',     0.32),
    ('Brazilian',   0.31),
]

# Region tags for color coding (manual classification consistent with figures).
REGION = {
    'Chinese':'east_asia', 'Japanese':'east_asia', 'Korean':'east_asia',
    'Thai':'se_asia', 'Vietnamese':'se_asia', 'Filipino':'se_asia',
    'Russian':'eurasia', 'French':'w_europe', 'Spanish':'iberia',
    'British':'w_europe', 'Irish':'w_europe', 'Italian':'s_europe',
    'Greek':'s_europe',
    'Southern_US':'n_america', 'Cajun_Creole':'n_america', 'Mexican':'n_america',
    'Jamaican':'caribbean', 'Brazilian':'s_america',
    'Anchor_A':'other', 'Anchor_B':'other',
}

# Boundary/permeability check from run4_secondary_or_limitations_figure.
SPATIAL_GROUPING_RESIDUALS = [
    # (label, mean_residual, n)
    ('Iberian / Atlantic interregional', 0.139, 11),
    ('Same subregion',                   0.115, 11),
    ('Same region, cross-subregion',    -0.011, 32),
    ('E/SE Asia cross-subregion',       -0.014,  9),
    ('Other cross-region',              -0.020,127),
]

# Distance baseline from run4_method_or_model_figure inset annotation.
DISTANCE_BASELINE = {
    'intercept': 1.273,
    'slope': -0.116,
    'r_squared': 0.355,
}
