from __future__ import annotations

import matplotlib as mpl

EXPORT_DPI = 300

FIGURE_SIZES = {
    "map_global": (12, 6),
    "map_feature": (13.5, 7.5),
    "chart_standard": (7, 5),
    "chart_wide": (12, 5),
    "chart_compact": (7, 3),
    "map_regional": (9, 6),
    "map_deep_dive": (10.5, 6.4),
    "chart_feature": (10.5, 6.2),
    "chart_feature_compact": (9.2, 5.0),
}

PALETTE = {
    "cloud_region": "#1f1f1f",
    "country_fill": "#fbfaf6",
    "country_edge": "#c7c7c7",
    "ai_fill": "#d55d3a",
    "ai_edge": "#6f2d1a",
    "priority_fill": "#c44536",
    "priority_edge": "#7f1d1d",
    "hot_spot_99": "#b2182b",
    "hot_spot_95": "#ef8a62",
    "cold_spot_95": "#67a9cf",
    "cold_spot_99": "#2166ac",
    "neutral": "#bdbdbd",
    "figure_bg": "#f3eee4",
    "panel_bg": "#fffdf8",
    "panel_edge": "#d9ceb9",
    "text_primary": "#1f1f1f",
    "text_muted": "#6b6358",
    "gridline": "#ddd4c6",
    "low_ai_low_access": "#5c7c9c",
    "low_ai_high_access": "#d8a23a",
    "high_ai_low_access": "#2f8f83",
    "high_ai_high_access": "#cb4f57",
    "chart_primary": "#5c7c9c",
    "chart_primary_fill": "#9cb7cb",
    "chart_secondary": "#d08f3b",
    "chart_secondary_fill": "#efc07f",
    "chart_tertiary": "#2f8f83",
    "chart_negative": "#a6493f",
}

ACCESS_CMAP = mpl.colors.LinearSegmentedColormap.from_list(
    "atlas_access",
    ["#4f0a6d", "#3c5d96", "#2f9f95", "#8ecf5b", "#f6dd32"],
)

PRIORITY_CMAP = mpl.colors.LinearSegmentedColormap.from_list(
    "atlas_priority",
    ["#5b0e2d", "#a51c30", "#d95f0e", "#f4a259", "#f7d08a"],
)

AI_SURFACE_CMAP = mpl.colors.LinearSegmentedColormap.from_list(
    "atlas_ai_surface",
    ["#17324d", "#33658a", "#2f8f83", "#8ecf5b", "#f6dd32"],
)

QUADRANT_COLORS = {
    "Low AI / Low access": PALETTE["low_ai_low_access"],
    "Low AI / High access": PALETTE["low_ai_high_access"],
    "High AI / Low access": PALETTE["high_ai_low_access"],
    "High AI / High access": PALETTE["high_ai_high_access"],
}

HOTSPOT_COLORS = {
    "hot_spot_99": PALETTE["hot_spot_99"],
    "hot_spot_95": PALETTE["hot_spot_95"],
    "not_significant": PALETTE["neutral"],
    "cold_spot_95": PALETTE["cold_spot_95"],
    "cold_spot_99": PALETTE["cold_spot_99"],
}

TYPOGRAPHY = {
    "title_family": "DejaVu Serif",
    "body_family": "DejaVu Sans",
    "kicker_size": 9,
    "title_size": 18,
    "subtitle_size": 10,
    "note_size": 8,
}

PANEL_BBOX = {
    "boxstyle": "round,pad=0.5,rounding_size=0.15",
    "facecolor": PALETTE["panel_bg"],
    "edgecolor": PALETTE["panel_edge"],
    "linewidth": 1.0,
}

RC_PARAMS = {
    "figure.dpi": EXPORT_DPI,
    "savefig.dpi": EXPORT_DPI,
    "savefig.facecolor": PALETTE["figure_bg"],
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "font.family": "DejaVu Sans",
}


def apply_matplotlib_style() -> None:
    mpl.rcParams.update(RC_PARAMS)
