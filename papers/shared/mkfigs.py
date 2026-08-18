"""Generate the scaffold's placeholder figures as vector PDFs.

Owned by T-005 (build scaffold). Its only job is to prove the figure pipeline
end to end: committed script -> Agg backend -> vector PDF -> \\includegraphics.
The real figures come from the evidence tasks and replace these.

Every figure in this project must be a vector PDF produced by a committed
script (AC-011). No screenshots, no raster.

Usage:
    python papers/shared/mkfigs.py          # writes both placeholders
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # required: see .agent/MEMORY.md
import matplotlib.pyplot as plt  # noqa: E402

PAPERS = Path(__file__).resolve().parent.parent

# Deterministic layout: no RNG is used anywhere in this script, so the output
# is byte-stable apart from the PDF creation date.
_COMPONENT_A = [
    (0.12, 0.72), (0.26, 0.86), (0.30, 0.58), (0.45, 0.78), (0.20, 0.44),
]
_COMPONENT_B = [
    (0.70, 0.34), (0.84, 0.46), (0.88, 0.22), (0.72, 0.12),
]
_EDGES_A = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (0, 4)]
_EDGES_B = [(0, 1), (0, 3), (1, 2), (2, 3)]


def _draw_graph(ax, nodes, edges, colour):
    for i, j in edges:
        x0, y0 = nodes[i]
        x1, y1 = nodes[j]
        ax.plot([x0, x1], [y0, y1], color=colour, linewidth=1.1, zorder=1)
    xs = [p[0] for p in nodes]
    ys = [p[1] for p in nodes]
    ax.scatter(xs, ys, s=46, color=colour, zorder=2, edgecolors="white",
               linewidths=0.8)


def placeholder_disconnection(out_path: Path) -> None:
    """Paper 1 placeholder: a neighbour graph in two components."""
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    _draw_graph(ax, _COMPONENT_A, _EDGES_A, "#1f4e79")
    _draw_graph(ax, _COMPONENT_B, _EDGES_B, "#a33d2a")
    ax.annotate("component 1", xy=(0.26, 0.95), ha="center", fontsize=9,
                color="#1f4e79")
    ax.annotate("component 2", xy=(0.79, 0.03), ha="center", fontsize=9,
                color="#a33d2a")
    ax.set_title("PLACEHOLDER: a neighbour graph split into two components",
                 fontsize=9)
    ax.set_xlim(0.02, 0.98)
    ax.set_ylim(-0.02, 1.02)
    ax.set_xticks([])
    ax.set_yticks([])
    for side in ax.spines.values():
        side.set_visible(False)
    fig.tight_layout()
    fig.savefig(out_path, format="pdf", bbox_inches="tight")
    plt.close(fig)


def placeholder_inflation(out_path: Path) -> None:
    """Paper 2 placeholder: nominal versus realised false-positive rate."""
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ks = [2, 4, 6, 8, 10, 12]
    nominal = [5.0] * len(ks)
    realised = [8.1, 11.4, 13.2, 14.4, 14.9, 15.2]
    ax.plot(ks, nominal, linestyle="--", color="#555555", linewidth=1.2,
            label="nominal 5%")
    ax.plot(ks, realised, marker="o", markersize=4, color="#a33d2a",
            linewidth=1.4, label="realised (schematic)")
    ax.set_xlabel("neighbour count $k$ offered to the selection rule",
                  fontsize=9)
    ax.set_ylabel("false-positive rate (%)", fontsize=9)
    ax.set_title("PLACEHOLDER: schematic shape only, not a measured result",
                 fontsize=9)
    ax.set_ylim(0, 18)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=8, frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.savefig(out_path, format="pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    targets = [
        (PAPERS / "paper1" / "figures" / "placeholder.pdf",
         placeholder_disconnection),
        (PAPERS / "paper2" / "figures" / "placeholder.pdf",
         placeholder_inflation),
    ]
    for out_path, fn in targets:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fn(out_path)
        print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
