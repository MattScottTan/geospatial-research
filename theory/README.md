# theory

Theoretical work growing out of the two applied projects: spatial weights matrices
treated as random band matrices.

The connecting observation is that the statistics both StoryMaps rely on are functionals
of the spectrum of a structured sparse matrix —

- Moran's I = (n/S₀)·(z′Wz)/(z′z), a Rayleigh quotient in the weights matrix
- Getis-Ord Gi\*, local quadratic forms in the same W
- Mantel r = tr(D₁D₂)/√(tr D₁²·tr D₂²), a normalised matrix inner product
- CAR/SAR precision Q = (I − ρW)/τ², whose inverse is the resolvent of W at z = 1/ρ

— and that a distance-band spatial weights matrix on a 1D transect is exactly the
periodic random band matrix of Sodin's theorem.

## Open threads

1. **Thouless threshold in 2D.** Transplanting the mixing-vs-resolution argument to a
   d-dimensional torus gives threshold radius ~N^(1/d − 1/6), recovering N^(5/6) at
   d = 1 and predicting N^(1/3) at d = 2. Standard k-NN weights sit orders of magnitude
   below it. Heuristic only; the 1D proof's Fourier diagonalisation of the band walk
   does not carry over.
2. **Universal bulk, non-universal tail.** Low-order spectral moments are geometry-blind
   (semicircle holds for any W → ∞), but edge statistics need degree ~N^(1/3) and those
   walks feel the geometry. Suggests the normal approximation to Moran's I is safe while
   its tail is not — where every reported p-value lives.
3. **Eigenvector localisation and ESF.** Moran eigenvector maps regress on eigenvectors
   of MWM. Delocalised, those are global spatial trends; localised, they are local bumps.
   Which regime applies determines what eigenvector spatial filtering is doing.
4. **Spectral spatial confounding.** Decompose the covariate in the eigenbasis of Q and
   express the bias in β̂ via the limiting spectral distribution. Would explain the
   factor-of-four gap between the GP and CAR distance coefficients in
   `../eip`.

Nothing here is settled. Item 1's d = 2 case and item 3 are the ones with a clear
theorem shape.
