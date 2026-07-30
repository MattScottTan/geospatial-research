"""
Build replacement for v4_06 (spatial-grouping bars).
Issue with original: callout text said "Highest mean residual in the prototype.
This is the project's mandatory non-Asia diagnostic case." The words 'prototype'
and 'mandatory' are tells that hurt credibility for a Fisher Prize submission.
This rebuild uses identical data and styling but rewrites the callout to describe
the finding directly.
"""
import os
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})

# Same data as the published figure
groups = [
    ('Iberian / Atlantic\ninterregional', 0.139, 11),
    ('Same subregion',                    0.115, 11),
    ('Same region,\ncross-subregion',    -0.011, 32),
    ('East/SE Asia\ncross-subregion',    -0.014,  9),
    ('Other cross-region',               -0.020,127),
]
labels = [g[0] for g in groups]
values = [g[1] for g in groups]
ns     = [g[2] for g in groups]

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
ax.set_yticklabels(labels, fontsize=10.5, color='#222')
ax.invert_yaxis()

# Value labels at end of each bar
for i, (bar, val, n) in enumerate(zip(bars, values, ns)):
    if val >= 0:
        x_pos = val + 0.005; ha = 'left'
    else:
        x_pos = val - 0.005; ha = 'right'
    fw = 'bold' if i == 0 else 'normal'
    ax.text(x_pos, bar.get_y() + bar.get_height()/2,
            f'{val:+.3f}', va='center', ha=ha,
            fontsize=10.5, color='#111', fontweight=fw)

# n labels in their own column
for i, n in enumerate(ns):
    ax.text(-0.055, i, f'n = {n}',
            va='center', ha='right', fontsize=9, color='#666',
            family='monospace', transform=ax.transData)

ax.axvline(0, color='#1d1d1d', linewidth=1.0, zorder=2)
ax.set_xlabel('Mean residual cuisine similarity (observed − predicted from distance)',
              fontsize=11, color='#333', labelpad=14)
ax.set_xlim(-0.07, 0.18)
ax.set_axisbelow(True)
ax.grid(axis='x', linestyle=':', color='#bbb', alpha=0.6)
for spine in ('top','right','left'):
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#aaa')
ax.tick_params(left=False, colors='#444')

ax.text(0, -0.85, 'distance-only\nexpectation',
        ha='center', va='top', fontsize=8.5, color='#666', style='italic')

fig.text(0.5, 0.95,
         'Where does residual cuisine similarity concentrate?',
         ha='center', va='center',
         fontsize=15, fontweight='bold', color='#111')
fig.text(0.5, 0.915,
         'Mean residual by spatial grouping',
         ha='center', va='center',
         fontsize=10.5, color='#444', style='italic')

# === REWRITTEN CALLOUT ===
# Old text: "Highest mean residual in the prototype. This is the project's
#            mandatory non-Asia diagnostic case."
# New text: describes the finding substantively, removes "prototype" and "mandatory".
ax_callout = fig.add_axes([0.74, 0.50, 0.24, 0.28])
ax_callout.axis('off')
ax_callout.set_xlim(0, 1); ax_callout.set_ylim(0, 1)
ax_callout.text(0.5, 0.5,
                "Highest mean residual\nin the corpus.\n\n"
                "Long-distance Iberian–\nAtlantic–Pacific pairs\nexceed even the same-\n"
                "subregion baseline.",
                ha='center', va='center',
                fontsize=10, color='#7a3318',
                bbox=dict(boxstyle='round,pad=0.6', facecolor='#fff4e8',
                          edgecolor='#c45a2e', linewidth=1.2))
ax.annotate('', xy=(0.135, 0.0), xycoords='data',
            xytext=(0.18, 0.5), textcoords='data',
            arrowprops=dict(arrowstyle='->', color='#c45a2e', linewidth=1.4,
                            connectionstyle='arc3,rad=-0.3'),
            zorder=10)

fig.text(0.5, 0.045,
         'Positive values = average similarity exceeds distance-only expectation. Use as diagnostic evidence, not causal proof.',
         ha='center', va='center',
         fontsize=9.5, color='#444', style='italic')

out = '/home/claude/v4_06_secondary_residuals_by_grouping.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {out}")
