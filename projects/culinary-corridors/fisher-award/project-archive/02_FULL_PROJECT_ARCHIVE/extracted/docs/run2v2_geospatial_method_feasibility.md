# Run 2 v2 Geospatial Method Feasibility

Created: 2026-04-29

## Purpose

Run 2 already used great-circle distance. Run 2 v2 adds geospatial-only analyses so that the Fisher insight depends on spatial structure, not only ingredient vectors.

## Candidate method 1: path/connectivity-aware distance proxy

**Ideal version:** least-cost or network distance using ports, historical routes, shipping lanes, migration corridors, or land/sea cost surfaces.  
**Run 2 v2 feasibility:** partial. No trusted route network or cost surface is staged in the prototype, and adding one would widen the run too much.  
**Implemented proxy:** classify cuisine pairs by same subregion, same region/cross-subregion, long-distance interregional, East/Southeast Asia cross-subregion, and Iberian/Atlantic long-distance corridor candidate. Add a spatial-surprise score defined as residual multiplied by log-distance.  
**Status:** implement as exploratory proxy, with true least-cost/network routing reserved for Run 3.

## Candidate method 2: residual bridge scores

**Method:** aggregate pairwise positive residuals into place-level scores: positive residual degree, mean positive residual, long-distance positive degree, and residual-weighted long-distance bridge score.  
**Why geospatial:** a cuisine becomes a spatial bridge if it has unusually strong residual links across distance and region boundaries. This cannot be inferred from ingredient vectors alone because it depends on pair geography and distance.  
**Status:** implement in Run 2 v2. This is the strongest geospatial-only method for the prototype.

## Candidate method 3: boundary/permeability check

**Method:** group dyads by same UN subregion, same region/cross-subregion, East/Southeast Asia cross-subregion, Iberian/Atlantic interregional, and other interregional boundaries; compare mean residuals and positive-residual shares.  
**Why geospatial:** the unit of analysis becomes boundaries and spatial grouping, not cuisines alone.  
**Status:** implement as a simple prototype. It should be framed as a boundary/permeability diagnostic rather than a definitive border model.

## Selected Run 2 v2 methods

1. **Residual bridge scores** — strongest and most Fisher-ready.
2. **Boundary/permeability check** — useful support for focused cases.
3. **Path/connectivity proxy** — exploratory; include only with explicit caveats.

## Run 3 upgrade path

If time and data access permit, replace the proxy with a real path-aware model using a staged base map, maritime/port network, land/sea cost raster, or a documented historical route dataset. Until then, avoid claiming that the proxy proves actual trade or migration routes.
