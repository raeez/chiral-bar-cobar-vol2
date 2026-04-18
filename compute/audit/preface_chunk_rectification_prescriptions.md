## Target chunk: chapters/frame/preface.tex:4000-4500

## Findings
- Severity: CRITICAL
- AP classification: AP152
- Line anchor: preface.tex:4275
- Issue: The `10.5` formality-bridge paragraph overreads Theorem~`\ref{thm:e1-formality-bridge}`. The cited theorem, as inscribed in `chapters/theory/e1_modular_koszul.tex:2173-2186`, gives a chain-model/cohomology comparison between ordered chiral chains on `D^\times` and the cyclic/topological Hochschild model for `E_\infty` input; it does not assert that the ordered bar and symmetric bar are equivalent as ordered objects, nor that the spectral `R`-matrix becomes trivial. This also contradicts the same preface at `preface.tex:1110-1114`, which already says the averaging map is lossy and kills the `R`-matrix profile.
- Proposed fix: Replace the paragraph by a scope-qualified statement: on the `E_\infty` locus the ordered and cyclic/symmetric models compute the same cohomology, but ordered-to-`\Sigma_n` descent remains lossy at the ordered-object level and still discards `R`-matrix/Yangian data.

- Severity: HIGH
- AP classification: AP153
- Line anchor: preface.tex:4351
- Issue: The Verlinde sentence compresses several load-bearing restrictions into a bare slogan. `prop:verlinde-from-ordered` is explicitly a positive-integer-level `\widehat{\mathfrak{sl}}_2` statement with root-of-unity truncation and TUY conformal-block output; as written, the preface reads as if generic ordered chiral homology itself already produces the full Verlinde invariant without the finite-level/symmetric-coinvariant step.
- Proposed fix: Add the integer-level/root-of-unity qualifier and say explicitly that ordered chiral homology provides the finite-level chain model whose symmetric coinvariants recover conformal blocks and hence the Verlinde dimensions.

## Ready-to-apply Edit prescriptions
- File: /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
- old_string:
```tex
For $\Einf$-chiral algebras (the entire standard landscape:
Heisenberg, Virasoro, affine Kac--Moody, $\cW_N$, and all
free-field algebras), the ordered and symmetric bars are
quasi-isomorphic:
$\barB^{\mathrm{ord}}(\cA)\xrightarrow{\sim}
\barB^\Sigma(\cA)$
(Theorem~\ref{thm:e1-formality-bridge}). The $R$-matrix is
trivial, the Yangian is cocommutative, and the averaging
map loses nothing. This is the regime in which the five
theorems of Sections~1--9 give a complete picture.
```
- new_string:
```tex
For $\Einf$-chiral algebras (the standard vertex-algebraic families
of the landscape), Theorem~\ref{thm:e1-formality-bridge} gives a
chain-model comparison, not a lossless identification of ordered and
symmetric objects:
$\cC_n^{\mathrm{ord}}(D^\times,\cA)\xrightarrow{\sim}
B_n^{\mathrm{cyc}}(\cA)$.
Thus the ordered and cyclic/symmetric models compute the same
cohomology on the $\Einf$ locus, but the ordered bar still carries the
spectral $R$-matrix and Yangian data, and the averaging map remains
lossy at the ordered-object level. This is the regime in which the
five theorems of Sections~1--9 capture the symmetric-lane invariants
completely, not the whole ordered structure.
```
- AP293-positive deliverable: sharpened hypothesis (formality bridge re-scoped to a chain-model/cohomology comparison, with explicit loss of ordered `R`-matrix data)

- File: /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
- old_string:
```tex
At integer level, the ordered chiral homology recovers the Verlinde
formula: $Z_g = \sum_j S_{0j}^{2-2g}$ arises as the dimension of ordered
chiral homology at level~$k$, with $n = k+2$
(Proposition~\ref{prop:verlinde-from-ordered}). Closed-form
polynomials $P_g(n) = n^{g-1}(n^2{-}1)\cdot R_{g-2}(n^2)$ are proved
through genus~$6$.
```
- new_string:
```tex
At positive integer level $k\ge 1$, where
$q=e^{2\pi i/(k+2)}$ is a root of unity, the ordered chiral homology of
$V_k(\mathfrak{sl}_2)$ supplies the finite-level chain model whose
symmetric coinvariants recover the TUY conformal blocks, and the
resulting dimensions satisfy the Verlinde formula
$Z_g = \sum_j S_{0j}^{2-2g}$
(Proposition~\ref{prop:verlinde-from-ordered}). Closed-form
polynomials $P_g(n) = n^{g-1}(n^2{-}1)\cdot R_{g-2}(n^2)$ are proved
through genus~$6$.
```
- AP293-positive deliverable: sharpened hypothesis (integer-level/root-of-unity scope made explicit in the Verlinde sentence)

## Attack-heal notes
- First draft tagged the primary defect as AP153, but the hostile reread showed AP152 is the tighter fit because the local cache explicitly says ordered-to-`\Sigma_n` descent is `R`-matrix twisted and naive quotient is only pole-free.
- I checked the cited theorem body before prescribing the replacement; the final edit now matches `thm:e1-formality-bridge` exactly as a chain/cohomology statement rather than a stronger ordered-object equivalence.
- I considered a larger rectification around `\SCchtop \xrightarrow{\sim} \mathsf{SC}`, but dropped it from this pass because it would require a second operad-identification rewrite and would blur the single highest-impact prescription.
- The first draft of the Verlinde fix was too weak because it still hid the finite-level truncation; I added the root-of-unity qualifier and TUY conformal-block step so the sentence no longer reads as a generic ordered-bar claim.
- Residual risk: line `preface.tex:1112-1114` still phrases the bridge more compactly than the corrected `10.5` paragraph. The two are compatible after this edit, but a later propagation sweep should harmonize the wording verbatim.
