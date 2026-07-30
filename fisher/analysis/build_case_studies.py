"""
Build case-study spotlight figures for Section 8 of the StoryMap.

For each of Filipino, Russian, Thai, Spanish, produce a two-panel figure:
  LEFT:  regional spotlight map showing the cuisine anchor, its top residual
         partners (great-circle lines colored by partner residual), and the
         broader regional context.
  RIGHT: scorecard panel with the cuisine's top residual partners as a bar
         chart, plus a summary box with mean residual, LISA classification,
         and bridge index value.

Following the case-study format used in Matthew's EIP submission Cloudy with a
Chance of Compute, where each city had a regional context map plus a
component-by-component scorecard.
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.feature import ShapelyFeature

# ---- Data ----
S = np.load('similarity_matrix.npy')
D = np.load('distance_matrix.npy')
R = np.load('residual_matrix.npy')
mean_resid = np.load('mean_resid.npy')
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f]
n = len(cuisines)
idx = {c: i for i, c in enumerate(cuisines)}

with open('lisa_results.json') as f:
    lisa_data = json.load(f)
lisa_by = {r['cuisine']: r for r in lisa_data['per_cuisine']}

ANCHORS = {
    'brazilian':(-14.24,-51.93), 'british':(55.38,-3.44), 'cajun_creole':(30.50,-91.20),
    'chinese':(35.86,104.20), 'filipino':(12.88,121.77), 'french':(46.23,2.21),
    'greek':(39.07,21.82), 'indian':(20.59,78.96), 'irish':(53.41,-8.24),
    'italian':(41.87,12.57), 'jamaican':(18.11,-77.30), 'japanese':(36.20,138.25),
    'korean':(35.91,127.77), 'mexican':(23.63,-102.55), 'moroccan':(31.79,-7.09),
    'russian':(61.52,105.32), 'southern_us':(33.00,-86.00), 'spanish':(40.46,-3.75),
    'thai':(15.87,100.99), 'vietnamese':(14.06,108.28),
}
DISPLAY = {
    'brazilian':'Brazilian','british':'British','cajun_creole':'Cajun-Creole',
    'chinese':'Chinese','filipino':'Filipino','french':'French','greek':'Greek',
    'indian':'Indian','irish':'Irish','italian':'Italian','jamaican':'Jamaican',
    'japanese':'Japanese','korean':'Korean','mexican':'Mexican','moroccan':'Moroccan',
    'russian':'Russian','southern_us':'Southern US','spanish':'Spanish',
    'thai':'Thai','vietnamese':'Vietnamese',
}
BRIDGE_SCORES = {
    'filipino': 0.87, 'russian': 0.84, 'southern_us': 0.69, 'jamaican': 0.68,
    'french': 0.65, 'spanish': 0.53, 'british': 0.51, 'irish': 0.44,
    'italian': 0.32, 'brazilian': 0.31,
}

# ---- Style constants matching v4_05 / v4_07 palette ----
LAND_COLOR  = '#f3e8ce'
OCEAN_COLOR = '#d3e3ec'
COAST_COLOR = '#5d6770'
BORDER_COLOR= '#a9b3bd'

POS_LINE = '#c45a2e'   # positive residual: warm orange
NEG_LINE = '#7a8aa0'   # negative residual: muted blue-grey
ANCHOR_COLOR_MAIN = '#1f5fa3'    # the focal cuisine
ANCHOR_COLOR_PART = '#c45a2e'    # partners (positive)
ANCHOR_COLOR_OTHR = '#bbbbbb'    # other corpus cuisines

NE_PATH = '/usr/local/lib/python3.12/dist-packages/pyogrio/tests/fixtures/naturalearth_lowres/naturalearth_lowres.shp'

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})

# ===== Per-case configuration =====
CASES = {
    'filipino': {
        'subtitle': 'Archetypal archipelagic bridge',
        'role': 'Pacific-archipelagic node',
        'top_partners': 5,
        'focal_label_offset': (10, 10),    # NE to clear all SE Asia partners
        'partner_label_suppress': set(),
        'partner_label_overrides': {
            'vietnamese': (-12, -8, 'right', 'top'),     # SW
            'thai':       (-12, 8, 'right', 'bottom'),   # NW
            'jamaican':   (5, -10, 'left', 'top'),       # SE of dot
            'southern_us':(5, 8, 'left', 'bottom'),      # NE of dot
            'brazilian':  (5, 1, 'left', 'center'),
        },
        'rationale': (
            "Filipino has the highest mean residual in the corpus (+0.055) and the\n"
            "highest bridge score (0.87). It connects East/Southeast Asian cuisines\n"
            "across the Pacific to Iberian/Atlantic cuisines through historical\n"
            "exchange. The Local Moran's I is the most negative of any cuisine in\n"
            "the corpus across all four spatial-weights schemes — the high-low\n"
            "spatial pattern of an isolated archipelagic bridge."
        ),
    },
    'russian': {
        'subtitle': 'Long-distance Eurasian bridge',
        'role': 'Eurasian continental anchor',
        'top_partners': 5,
        'focal_label_offset': (0, -8),    # straight south of the dot
        'partner_label_suppress': {'irish'},   # named in bar chart; map gets too crowded
        'partner_label_overrides': {
            'british':    (4, 12, 'center', 'bottom'),
            'french':     (4, -10, 'center', 'top'),
            'mexican':    (3, -3, 'left', 'top'),
            'southern_us':(3, 8, 'left', 'bottom'),
        },
        'rationale': (
            "Russian is the project's most spatially diagnostic cuisine. Its mean\n"
            "residual is mildly negative (−0.025), but its top residual partners\n"
            "(British, Irish, French, Italian) are 5,000–7,000 km west. The Local\n"
            "Moran's I is the only highly significant LL classification in the\n"
            "corpus (p = 0.009 across all four spatial-weights schemes) —\n"
            "geographic neighbors are low-residual cuisines, while bridge partners\n"
            "are far too distant to dominate the local spatial weights."
        ),
    },
    'thai': {
        'subtitle': 'Regional hub at the heart of the strongest corridor',
        'role': 'East/Southeast Asian regional hub',
        'top_partners': 5,
        'focal_label_offset': (-18, 10),   # NW of dot, well clear
        'partner_label_suppress': set(),
        'partner_label_overrides': {
            'vietnamese': (15, -12, 'left', 'top'),    # SE, well below
            'filipino':   (10, -22, 'left', 'top'),    # further SE, lower
            'chinese':    (-3, 10, 'right', 'bottom'),
        },
        'rationale': (
            "Thai is not a top-ten bridge cuisine, but it sits at the center of the\n"
            "strongest focused residual corridor in the corpus. Its link to\n"
            "Vietnamese (+0.395 in this reconstruction) is the highest single\n"
            "pairwise residual observed. Thai's residuals are dense and short-range\n"
            "rather than far-reaching — a hub, not a bridge. The HL spatial pattern\n"
            "is sign-consistent across all four spatial-weights schemes."
        ),
    },
    'spanish': {
        'subtitle': 'Iberian/Atlantic–Pacific node',
        'role': 'Long-distance Iberian/Atlantic bridge',
        'top_partners': 5,
        'focal_label_offset': (3, -8),   # SE of the dot
        'partner_label_suppress': set(),
        'partner_label_overrides': {
            'cajun_creole': (3, 8, 'left', 'bottom'),
            'mexican':      (-3, -3, 'right', 'top'),
            'southern_us':  (3, -3, 'left', 'top'),
            'french':       (3, 8, 'left', 'bottom'),
            'brazilian':    (3, -3, 'left', 'top'),
        },
        'rationale': (
            "Spanish anchors the Iberian/Atlantic interregional grouping (Finding 2,\n"
            "highest mean residual configuration in the corpus at +0.139). Its\n"
            "residual partners span the Atlantic and Pacific — Mexican, Filipino,\n"
            "Brazilian, Cajun-Creole, Jamaican. The Local Moran's I shows the HL\n"
            "spatial pattern across all four spatial-weights schemes: a high-residual\n"
            "European cuisine surrounded by lower-residual European neighbors,\n"
            "with its strong partners far across two oceans."
        ),
    },
}

def great_circle_path(lat1, lon1, lat2, lon2, n=80):
    """Generate a great-circle path between two anchors. Returns lon, lat arrays."""
    lat1r, lon1r = np.radians(lat1), np.radians(lon1)
    lat2r, lon2r = np.radians(lat2), np.radians(lon2)
    d = np.arccos(np.clip(
        np.sin(lat1r)*np.sin(lat2r) +
        np.cos(lat1r)*np.cos(lat2r)*np.cos(lon2r-lon1r),
        -1, 1))
    if d == 0:
        return np.array([lon1, lon2]), np.array([lat1, lat2])
    f = np.linspace(0, 1, n)
    A = np.sin((1-f)*d) / np.sin(d)
    B = np.sin(f*d) / np.sin(d)
    x = A*np.cos(lat1r)*np.cos(lon1r) + B*np.cos(lat2r)*np.cos(lon2r)
    y = A*np.cos(lat1r)*np.sin(lon1r) + B*np.cos(lat2r)*np.sin(lon2r)
    z = A*np.sin(lat1r) + B*np.sin(lat2r)
    lats = np.degrees(np.arctan2(z, np.sqrt(x*x+y*y)))
    lons = np.degrees(np.arctan2(y, x))
    return lons, lats


def build_case_figure(focal, cfg):
    """Build a two-panel case-study figure for a focal cuisine."""
    i = idx[focal]
    # Top residual partners (signed; we sort descending and keep top N)
    partner_resids = []
    for j in range(n):
        if j == i: continue
        partner_resids.append((cuisines[j], R[i, j]))
    partner_resids.sort(key=lambda x: -x[1])
    top_pos = partner_resids[:cfg['top_partners']]

    fig = plt.figure(figsize=(15.5, 7.5), facecolor='white')

    # === LEFT: regional spotlight map ===
    proj = ccrs.Robinson(central_longitude=ANCHORS[focal][1])
    ax_map = fig.add_axes([0.005, 0.10, 0.62, 0.78], projection=proj)
    ax_map.set_global()

    countries = ShapelyFeature(shpreader.Reader(NE_PATH).geometries(),
                               ccrs.PlateCarree(),
                               facecolor=LAND_COLOR, edgecolor=BORDER_COLOR, linewidth=0.3)
    ax_map.add_feature(countries)
    ax_map.set_facecolor(OCEAN_COLOR)
    ax_map.gridlines(linewidth=0.3, color='#aab4be', alpha=0.4, linestyle=':',
                     xlocs=range(-180,181,30), ylocs=range(-60,91,30))

    flat, flon = ANCHORS[focal]

    # Draw great-circle lines from focal to top partners
    max_resid = max(r for _, r in top_pos) if top_pos else 0.4
    for partner, res in top_pos:
        plat, plon = ANCHORS[partner]
        lons_path, lats_path = great_circle_path(flat, flon, plat, plon)
        # Line width 1 to ~5 by residual strength
        lw = 1.0 + 4.5 * (res / max_resid) if res > 0 else 0.8
        color = POS_LINE if res > 0 else NEG_LINE
        ax_map.plot(lons_path, lats_path,
                    color=color, linewidth=lw, alpha=0.85,
                    transform=ccrs.Geodetic(), zorder=4,
                    solid_capstyle='round')

    # Plot all corpus anchors as small grey dots (background context)
    for c, (lat, lon) in ANCHORS.items():
        if c == focal: continue
        if c in [p[0] for p in top_pos]: continue
        ax_map.scatter(lon, lat, s=22, color=ANCHOR_COLOR_OTHR,
                       edgecolor='white', linewidth=0.6,
                       transform=ccrs.PlateCarree(), zorder=5)

    # Plot top partner anchors prominently
    for partner, res in top_pos:
        plat, plon = ANCHORS[partner]
        sz = 90 + 220 * (res / max_resid) if res > 0 else 80
        ax_map.scatter(plon, plat, s=sz, color=ANCHOR_COLOR_PART,
                       edgecolor='white', linewidth=1.4,
                       transform=ccrs.PlateCarree(), zorder=6)

    # Plot focal anchor — biggest, distinct color
    ax_map.scatter(flon, flat, s=320, color=ANCHOR_COLOR_MAIN,
                   edgecolor='white', linewidth=2.0,
                   transform=ccrs.PlateCarree(), zorder=7)

    # Label focal cuisine — use per-case offset so it never collides with partners
    fdlon, fdlat = cfg.get('focal_label_offset', (0, -6))
    ax_map.text(flon + fdlon, flat + fdlat, DISPLAY[focal],
                fontsize=12, fontweight='bold', ha='center', va='center',
                color='#0d2f4d',
                transform=ccrs.PlateCarree(), zorder=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='#1f5fa3', linewidth=1.0, alpha=0.95))

    # Label partner cuisines — use per-case overrides where present
    overrides = cfg.get('partner_label_overrides', {})
    suppress = cfg.get('partner_label_suppress', set())
    for partner, res in top_pos:
        if partner in suppress:
            continue
        plat, plon = ANCHORS[partner]
        if partner in overrides:
            dlat, dlon, ha, va = overrides[partner]
        else:
            offset_lat = -5 if plat > 0 else 5
            ha, va = 'center', ('top' if plat > 0 else 'bottom')
            dlat, dlon = offset_lat, 0
        ax_map.text(plon + dlon, plat + dlat,
                    f"{DISPLAY[partner]}\n{res:+.2f}",
                    fontsize=9, fontweight='bold', ha=ha, va=va,
                    color='#7a3318', transform=ccrs.PlateCarree(), zorder=8,
                    bbox=dict(boxstyle='round,pad=0.22', facecolor='white',
                              edgecolor='none', alpha=0.85))

    ax_map.set_title(f"{DISPLAY[focal]} — top residual partners",
                     fontsize=12, fontweight='bold', pad=8)

    # === RIGHT: scorecard panel ===
    ax_bar = fig.add_axes([0.69, 0.42, 0.29, 0.40])

    # Build top-residual partner bar chart (oriented horizontally)
    labels = [DISPLAY[p] for p, _ in top_pos]
    values = [r for _, r in top_pos]
    y_pos = np.arange(len(labels))
    bars = ax_bar.barh(y_pos, values,
                       color=[POS_LINE if v > 0 else NEG_LINE for v in values],
                       edgecolor='white', linewidth=1.2, height=0.7)
    ax_bar.set_yticks(y_pos)
    ax_bar.set_yticklabels(labels, fontsize=10)
    ax_bar.invert_yaxis()
    ax_bar.axvline(0, color='#222', linewidth=0.8)
    for bar, val in zip(bars, values):
        ax_bar.text(val + 0.005 if val > 0 else val - 0.005,
                    bar.get_y() + bar.get_height()/2,
                    f'{val:+.3f}', va='center',
                    ha='left' if val > 0 else 'right',
                    fontsize=9.2, color='#111', fontweight='bold')

    ax_bar.set_xlabel('Residual (observed − predicted from distance)',
                      fontsize=9, color='#444', labelpad=8)
    ax_bar.set_xlim(0, max(values)*1.25 if max(values) > 0 else 0.5)
    ax_bar.grid(axis='x', linestyle=':', color='#bbb', alpha=0.6)
    ax_bar.set_axisbelow(True)
    for s in ('top','right','left'): ax_bar.spines[s].set_visible(False)
    ax_bar.spines['bottom'].set_color('#aaa')
    ax_bar.tick_params(left=False, colors='#333')
    ax_bar.set_title(f'Top {cfg["top_partners"]} residual partners',
                     fontsize=10.5, fontweight='bold', loc='left', pad=8)

    # === Stats summary box (below bar chart) ===
    ax_st = fig.add_axes([0.67, 0.04, 0.32, 0.24])
    ax_st.axis('off')

    L = lisa_by[focal]
    bs = BRIDGE_SCORES.get(focal, None)
    bs_str = f"{bs:.2f} (rank {sorted(BRIDGE_SCORES.values(), reverse=True).index(bs)+1} of 10)" if bs else "Not in top 10"

    sig_marker = ''
    if L['p_sim'] < 0.05: sig_marker = ' ***'
    elif L['p_sim'] < 0.10: sig_marker = ' *'

    summary_text = (
        f"Mean residual:        {L['mean_resid']:+.4f}\n"
        f"Bridge score:         {bs_str}\n"
        f"LISA classification:  {L['quadrant_raw']} (p = {L['p_sim']:.3f}){sig_marker}\n"
        f"Local Moran's I:      {L['local_I']:+.3f}\n"
        f"Role in network:      {cfg['role']}"
    )

    ax_st.text(0.0, 0.95, summary_text, transform=ax_st.transAxes,
               fontsize=9.4, ha='left', va='top', family='monospace', color='#222',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='#f7f7f4',
                         edgecolor='#bbb', linewidth=0.6))

    # === Title bar at top ===
    fig.suptitle(f"{DISPLAY[focal]} — {cfg['subtitle']}",
                 fontsize=14, fontweight='bold', y=0.965, color='#0d2f4d')

    # Caption / rationale at bottom
    fig.text(0.5, 0.02, cfg['rationale'], ha='center', va='bottom',
             fontsize=9, color='#444', linespacing=1.45,
             family='DejaVu Sans')

    out = f'/home/claude/v4_08_case_{focal}.png'
    plt.savefig(out, dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved {out}")
    return out

# Build all four
outputs = []
for focal, cfg in CASES.items():
    outputs.append(build_case_figure(focal, cfg))
print("\nAll case-study figures built:")
for o in outputs: print(f"  {o}")
