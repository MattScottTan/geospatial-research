# MEMORY

Durable execution knowledge. Would a fresh worker make a better decision knowing this?
If not, it does not belong here.

## Environment

- **Bash heredocs corrupt backslashes.** Git Bash here collapses `\\` to `\`, even in
  quoted heredocs. Write `.tex` and any backslash-heavy file with the Write/Edit tool.
- **LaTeX is MiKTeX 25.12** with `latexmk`. `amsmath, amssymb, booktabs, graphicx,
  hyperref, natbib, geometry` all verified working. MiKTeX installs missing packages on
  demand, so a first compile may be slow.
- **matplotlib must use the `Agg` backend** in scripts; `savefig('x.pdf')` yields vector
  output that `\includegraphics` embeds cleanly.
- **Windows `MAX_PATH`**: this repo has `core.longpaths true` set. Keep new paths short
  anyway.
- **Python is 3.14**, system install (not a venv). `libpysal` and `esda` were pip-installed
  into it during this work.

## Repository conventions

- `eip/` and `fisher/` are **frozen submissions**. Read-only. Nothing in the research track
  imports them.
- Research track is `theory/ code/ analysis/ tools/`. Reusable methods live in `tools/`,
  the importable library in `code/spatialrmt/`.
- Scripts add the library to path with
  `sys.path.insert(0, ROOT/"code")` and `sys.path.insert(0, ROOT)`.
- `analysis/outputs/` is gitignored — regenerate, do not expect it in a clean clone. Any
  output a paper cites must be committed somewhere else or regenerable by `make`.
- `analysis/data/` holds small committed extracts (40 KB) so experiments have a stable
  input independent of the submission trees.

## Domain gotchas

- **`esda.Moran` row-standardises by default.** Pass `transformation="O"` or it silently
  discards whatever weighting you built. This has already caused one wrong result.
- **Gi\* includes the focal unit** (`setdiag(1.0)`); plain Gi does not. The distinction
  moves borderline units across the 1.96 cutoff.
- **The 319-city k=8 graph has 2 components** (252 / 67). Whole-graph mixing is undefined;
  compute spectral gaps within the largest component.
- **Directed kNN row-standardisation is a no-op for Moran's I** — every row has degree
  exactly `k`, so the normalisation cancels. Only symmetrized graphs show a difference.
- **`worldcities.csv` is SimpleMaps Basic**, 41,001 rows, CC BY 4.0, attribution required
  if reproduced.

## Programme context

- Two prior claims were narrowed after literature checks (eigenvector localisation
  threshold; Ricci curvature on geographic networks). Search before building.
- The published atlas reports Moran's I = 0.066, p = 0.008, 7 hot and 33 cold spots at
  k = 8. These reproduce exactly from `eip/code/pipeline.py`; the papers correct their
  *interpretation*, not their arithmetic.
