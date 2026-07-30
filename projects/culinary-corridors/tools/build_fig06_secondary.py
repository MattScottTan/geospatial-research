"""
Improved secondary/limitations figure: residual cuisine similarity by
spatial grouping. Uses the exact values from the original
run4_secondary_or_limitations_figure (label, mean residual, n).
"""
import sys, os
sys.path.insert(0, '/home/claude/v4')
import figdata as D

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})

# data: (label, mean_residual, n)
groups = D.SPATIAL_GROUPING_RESIDUALS
# rebuild with shorter labels for display
display_labels = [
    'Iberian / Atlantic\ninterregional',
    'Same subregion',
    'Same region,\ncross-subregion',
    'East/SE Asia\ncross-subregion',
    'Other cross-region',
]
values = [v for _l, v, _n in groups]
ns = [n for _l, _v, n in groups]

# colors: positive bars warm, negative cool, with the headline (Iberian) highlighted
HEADLINE = '#c45a2e'
POSITIVE = '#e08a55'
NEGATIVE = '#9bb6c8'
colors = [HEADLINE, POSITIVE, NEGATIVE, NEGATIVE, NEGATIVE]

fig = plt.figure(figsize=(14, 7), facecolor='white')
ax = plt.axes([0.20, 0.18, 0.50, 0.60])

y_pos = np.arange(len(groups))
bars = ax.barh(y_pos, values, color=colors, edgecolor='white', linewidth=1.2,
               height=0.65)

ax.set_yticks(y_pos)
ax.set_yticklabels(display_labels, fontsize=10.5, color='#222')
ax.invert_yaxis()  # top-to-bottom matches narrative

# value labels at the END of each bar (always outside the bar)
for i, (bar, val, n) in enumerate(zip(bars, values, ns)):
    if val >= 0:
        x_pos = val + 0.005
        ha = 'left'
    else:
        x_pos = val - 0.005
        ha = 'right'
    fw = 'bold' if i == 0 else 'normal'
    ax.text(x_pos, bar.get_y() + bar.get_height()/2,
            f'{val:+.3f}',
            va='center', ha=ha, fontsize=10.5, color='#111',
            fontweight=fw)

# n labels in their own column, well to the right of the y-tick labels
for i, n in enumerate(ns):
    ax.text(-0.055, i, f'n = {n}',
            va='center', ha='right', fontsize=9, color='#666',
            family='monospace',
            transform=ax.transData)

# zero reference line
ax.axvline(0, color='#1d1d1d', linewidth=1.0, zorder=2)

ax.set_xlabel('Mean residual cuisine similarity (observed − predicted from distance)',
              fontsize=11, color='#333', labelpad=14)

ax.set_xlim(-0.07, 0.18)
ax.set_axisbelow(True)
ax.grid(axis='x', linestyle=':', color='#bbb', alpha=0.6)
for spine in ('top', 'right', 'left'):
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#aaa')
ax.tick_params(left=False, colors='#444')

# zero-line label below the axis
ax.text(0, -0.85, 'distance-only\nexpectation',
        ha='center', va='top', fontsize=8.5, color='#666', style='italic')

# Title
fig.text(0.5, 0.95,
         'Where does residual cuisine similarity concentrate?',
         ha='center', va='center',
         fontsize=15, fontweight='bold', color='#111')
fig.text(0.5, 0.915,
         'Mean residual by spatial grouping',
         ha='center', va='center',
         fontsize=10.5, color='#444', style='italic')

# Annotation callout for the headline bar — placed to the RIGHT of the chart, outside the data
ax_callout = fig.add_axes([0.74, 0.55, 0.24, 0.20])
ax_callout.axis('off')
ax_callout.set_xlim(0, 1); ax_callout.set_ylim(0, 1)
ax_callout.text(0.5, 0.5,
                "Highest mean residual\nin the prototype.\n\n"
                "This is the project's\nmandatory non-Asia\ndiagnostic case.",
                ha='center', va='center',
                fontsize=10, color='#7a3318',
                bbox=dict(boxstyle='round,pad=0.6', facecolor='#fff4e8',
                          edgecolor='#c45a2e', linewidth=1.2))
# arrow from callout into the headline bar
ax.annotate('', xy=(0.135, 0.0), xycoords='data',
            xytext=(0.18, 0.5), textcoords='data',
            arrowprops=dict(arrowstyle='->', color='#c45a2e', linewidth=1.4,
                            connectionstyle='arc3,rad=-0.3'),
            zorder=10)

# Reading note at bottom
fig.text(0.5, 0.045,
         'Positive values = average similarity exceeds distance-only expectation. Use as diagnostic evidence, not causal proof.',
         ha='center', va='center',
         fontsize=9.5, color='#444', style='italic')

out = '/home/claude/v4/figures/06_secondary_residuals_by_grouping.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {out}")
print(f"Size: {os.path.getsize(out)} bytes")
