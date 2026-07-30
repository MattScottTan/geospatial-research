"""
spatialrmt -- spatial weights matrices treated as structured random matrices.

The connecting idea, from theory/README.md: the statistics spatial analysis relies on
are functionals of the spectrum of a sparse structured matrix, and a distance-band
weights matrix on a transect is the periodic random band matrix of Sodin's theorem.

    geodesy     lat/lon to unit-sphere coordinates, haversine distance
    weights     kNN and distance-band construction, all four symmetry/normalisation
                combinations, as sparse matrices
    spectral    empirical spectral distributions, moments, Chebyshev coefficients,
                eigenvector localisation
    bandmatrix  random band matrix ensembles and the Thouless threshold in d dimensions

Nothing here is specific to either prize submission. The submissions under ../eip and
../fisher keep their own frozen copies of whatever they published with.
"""

from . import bandmatrix, geodesy, spectral, weights

__all__ = ["geodesy", "weights", "spectral", "bandmatrix"]
__version__ = "0.1.0"
