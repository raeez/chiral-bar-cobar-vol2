# Ambient Category Choice for Factorisation / Chiral Koszul Duality: Attack-Heal

Russian school + Beilinson-Drinfeld + Francis-Gaitsgory + Gaitsgory-Rozenblyum. Tests:
is the ambient category choice (D_X-mod, otimes^!) universally correct for the
programme's Koszul complementarity, or does Ran-ambient require refinement?

## Attack

Vol I Theorem A FORM-A (Sigma-coinvariant factorisation bar via FG12 + GR17 IV.5)
and FORM-B (ordered E_1 bar with R-matrix-twisted Sigma_n-descent on Ran(X)^ord)
both live on D_X-mod, but the programme also works through the BD chiral pseudo-
tensor structure (otimes^{ch}) and, downstream, through modules that are neither
D_X-holonomic nor bounded. Three concrete stressors:

(i) **otimes^! vs otimes^{ch}** on D_X-mod are DIFFERENT monoidal/pseudo-tensor
structures. FG12 uses the star-tensor otimes^* on Dmod(Ran(X)); BD uses the
chiral pseudo-tensor otimes^{ch} = j_*j^* Delta_*(-). Stating Theorem A with
"(D_X-mod, otimes^!)" simpliciter conflates three distinct things: otimes^!
(diagonal, genuinely symmetric monoidal on Dmod(X)); otimes^* (Ran-level
symmetric monoidal; this is the correct home for factorisation algebras); and
otimes^{ch} (pseudo-tensor, only OPERATIONS defined). FM56/FM69 already flag
that "symmetric monoidal category of chiral algebras" is category-theoretic
malpractice; the attack sharpens: the BD pseudo-tensor is not a bifunctor, yet
the Koszul complementarity (A, A^!) is written inside a symmetric monoidal
tensor product.

(ii) **Infinite-dimensional modules at infinite level.** At Kac-Moody at
k -> infinity, the inductive family { V_k(g-hat) }_k lives in Ind(Dmod(X)), not
Dmod(X). Koszul complementarity uses Verdier pairing A (x) A^! -> omega_X, but
omega_X is compact in Dmod(X) and NOT compact in Ind(Dmod(X)); the pairing need
not close. At critical level k = -h^v the mode algebra is Feigin-Frenkel centre,
infinite polynomial, unbounded. FM74 scope limitation (dim H^*(A,A) < infinity
EXCLUDES Virasoro, Yangian, critical KM) is a shadow of exactly this.

(iii) **Non-compact base + bulk-boundary.** For X = C non-compact or X = D* formal
punctured disc, Conf_n(C) is non-compact, factorisation global sections may
diverge, and Borel-Moore vs compact-support changes which Verdier duality pairs.
For SC^{ch,top}-algebras the open colour lives on (X, partial X) = (H, R), which
introduces a boundary: BD's original setup is pure closed curve; open-closed
factorisation needs pairs (X, partial X) and the otimes^* / otimes^! dichotomy
must be promoted to a coloured symmetric monoidal structure. The global formula
K_V = 2 dim(g) is proved for compact X; on C it is replaced by a relative /
Borel-Moore version.

## Three-step protocol

### (a) What "(D_X-mod, otimes^!)" gets RIGHT

1. For FORM-A on a COMPACT curve X with D_X-holonomic coefficients, the bar
complex B^{Sigma,ch}(A) is well-defined in Dmod(Ran(X)) under star-tensor
otimes^*, and Sigma_n-coinvariants are taken along the unordered-to-ordered Ran
quotient. Verdier pairing is nondegenerate on holonomic bounded objects by
GR17 IV.5; Koszul complementarity (A, A^!) closes as a Quillen equivalence
Pro(ConilFact(X)) <-> AugFact(X) (Francis-Gaitsgory Selecta 2012 Thm 6.3.2).

2. For classes G/L/C of the landscape (Heisenberg, affine KM, minimal-series
Virasoro), modules are D_X-coherent with bounded weight-graded pieces; the
holonomic-bounded locus is preserved by bar-cobar; otimes^! with the canonical
coherator equals otimes^* restricted to holonomic-bounded.

3. The Quillen-equivalence form of Theorem A (classical bar-cobar adjunction
on conilpotent augmented factorisation algebras) is exactly the statement
ambient (A) makes correctly. This is Theorem A at the level Beilinson-Drinfeld
proved; the (infty,2)-properad-level upgrade is what requires ambient (B).

### (b) What it gets WRONG

1. **otimes^! vs otimes^* collision.** The Verdier otimes^! on Dmod(X) is
diagonal-based, whereas the Ran-level otimes^* used by FG12 is disjointness-
based. They are NOT equal on Dmod(Ran(X)): otimes^! gives the monoidal
structure descending from coherent sheaves; otimes^* gives the structure
computing Ran-level factorisation. CLAUDE.md preface phrasing "(D_X-mod,
otimes^!)" for Theorem A FORM-A is a notational slip: the theorem uses otimes^*
on Dmod(Ran(X)), NOT otimes^! on Dmod(X). Same bifunctor symbol, different
functor. The foundations.tex Remark B already writes
"(Dmod(Ran(X)), otimes^*)" correctly at L244, 293, 508, 565.

2. **BD pseudo-tensor otimes^{ch} is NOT a bifunctor.** For Koszul
complementarity inside "(D_X-mod, otimes^{ch})" as a symmetric monoidal
category, the claim fails at the category-theoretic level: BD 3.4.10 defines
n-ary chiral OPERATIONS (pseudo-tensor), NOT a bifunctor with unit. Statements
"the pair (A, A^!) lives in (D-mod, otimes^{ch})" are technically malformed.
FM56 + FM69 explicit. The repair is to state the duality inside Fact(X) subset
Dmod(Ran(X)) under the star-tensor, where symmetric monoidality IS honest
(FG12, GR17 IV.5). FORM-A is a theorem about objects of Fact(X) under otimes^*,
not objects of ChirAlg under otimes^{ch}.

3. **Ind-completion omitted.** For classes M (Virasoro, W_N, Yangian,
critical KM) modules are NOT D_X-coherent bounded; Verdier pairing uses
Borel-Moore duality in Ind(Dmod(Ran(X))), not Verdier duality on Dmod(X).
Theorem A at generic central charge, critical level, or c = -2 (class M)
requires Ind(Dmod(Ran(X))) as ambient. The Pridham-Lurie formal moduli
correspondence used in the physics-bridge FMP proof also requires the
Ind-completion (Lurie HA 7.3.4). foundations.tex L481-489 assigns exactly this
role to ambient (B) = IndCoh(Ran(X)).

4. **Non-compact X.** K_V = 2 dim(g) is the pairing signature on H^{dR}(X,
End(Bar(A))) for COMPACT X. On C one gets K_V = 2 dim(g) from the Borel-Moore
version H^{BM}(C, End(Bar(A))); the two are equal for A with sufficient decay
(evaluation-generated core, AP47), but for the full Yangian (infinite-rank
level data) one must distinguish compact-support from Borel-Moore. The formula
as stated is correct on the eval-generated core, which suffices for all FM47
downstream applications; outside it the formula takes a modified form with
a boundary correction on Conf_n(C) - closure.

### (c) Correct relationship (heal)

The programme uses a TRIPLE ATLAS on Dmod(Ran(X)), each ambient canonical for
a class of theorems, bridged by explicit functorial equivalences:

- **(A) (Dmod(Ran(X)), otimes^*) [BD04]** = FORM-A Sigma-coinvariant bar;
classical Quillen-form Theorem A on conilpotent-complete locus; pseudo-
tensor Koszul duality (FG12). DEFAULT ambient.

- **(B) IndCoh(Ran(X)) [GR17 IV.5, V]** = Theorem A^{infty,2} (properad-level,
(infty,2)-categorical); Ind-completion required for Virasoro / Yangian /
critical KM and for Pridham-Lurie formal moduli. Convolution dg-Lie
g^SC_X controlling logarithmic SC^{ch,top}-algebras lives here.

- **(C) D^b_c(Ran(X)) + MHM [BBD + Saito]** = modular bootstrap, Theorem D
tensor-Arakelov class, multi-weight (obs_g)^2 = 0, MHM-purity route to
Koszulness. Weight filtration + ESV vanishing live here.

Bridges: Dmod(Ran(X)) <-> IndCoh(Ran(X)) on the bounded holonomic /
factorisation locus (Gaitsgory equivalence); D^b_c(Ran(X)) -> Dmod(Ran(X)) via
regular-holonomic Riemann-Hilbert. On the regular holonomic factorisation
locus (A), (B), (C) compute the same Ext-groups; bar-cobar and Koszul-duality
statements are ambient-independent on this locus.

BD pseudo-tensor otimes^{ch} is NOT an ambient for the Koszul complementarity;
it is an OPERAD acting on objects of Fact(X). Koszul complementarity (A, A^!)
is a statement about Fact(X) under otimes^*, with chiral OPERATIONS generated
by the BD pseudo-tensor inside this ambient. FM56/FM69 repair: never write
"symmetric monoidal category of chiral algebras" or "(D-mod, otimes^{ch})";
write "Fact(X) subset Dmod(Ran(X)) under otimes^*", and say chiral algebras
form a pseudo-tensor structure WITH operations generated by otimes^{ch} INSIDE
this ambient.

Infinite-dim / non-compact / bulk-boundary each have an explicit heal:

- **Infinite-dim (Virasoro, Yangian, critical KM):** promote ambient (A) to
(B) = IndCoh(Ran(X)); Koszul complementarity closes in Ind-completion via
Pro(ConilFact)^{Ind} <-> Aug(Fact)^{Ind}; FM74's finiteness-hypothesis
artefact vanishes.

- **Non-compact X = C:** replace Verdier duality with Borel-Moore duality on
Conf_n(C); K_V = 2 dim(g) holds on the eval-generated core (AP47); full non-
compact formula has an explicit boundary correction on Conf_n(C) closure,
compatible with AP47 scope.

- **Bulk-boundary SC^{ch,top}:** promote Fact(X) to coloured Fact(X, partial X)
under the coloured star-tensor; open-closed factorisation is a SYMMETRIC
MONOIDAL refinement compatible with (A); Koszul complementarity runs in
coloured form with two-colour Verdier duality omega_X oplus omega_{partial X}.

**One-line answer.** (Dmod(Ran(X)), otimes^*) - NOT (D_X-mod, otimes^!) and
NOT (D-mod, otimes^{ch}) - is the correct classical ambient. The (infty,2)-
categorical, Ind-completion, and mixed-Hodge refinements sit in the two
companion ambients (IndCoh and D^b_c); all three agree on the regular
holonomic factorisation locus. The programme's current architecture already
assigns the three ambients correctly in foundations.tex; stray phrasings
"(D-mod, otimes^!)" or "(D-mod, otimes^{ch})" in preface/narration are
notational slips to repair against the canonical triple atlas.

## Decorator + (H1)-(H4) implications

Under the triple atlas the four standing hypotheses (H1)-(H4) become derived
properties per ambient:

- (H1) pseudo-tensor closure: TAUTOLOGY in (A), proved via star-tensor
flatness.
- (H2) unit existence: FAILS in raw Dmod(X); HOLDS in Fact(X) under otimes^*
(unit = trivial factorisation algebra omega_Ran). FM70 repair.
- (H3) config-space flatness: TAUTOLOGY in (B) from IndCoh ULA.
- (H4) recognition: THEOREM in (A) from FG12 Thm 6.3.2; upgrades to (infty,2)
form in (B) from GR17 V.1.

Once the triple-atlas assignment is explicit, (H1)-(H4) are not axioms but
ambient-dependent theorems.

## Consequences ledger

Under correct ambient selection:

1. FORM-A is a theorem in ambient (A); Theorem A^{infty,2} in ambient (B);
MHM-purity-route Koszulness in ambient (C). No cross-ambient claim without
explicit bridge citation.

2. FM56 (sym mon cat of chiral algs) and FM69 (LV12 Thm 11.4.1 misapplied),
FM70 (unit functor missing in chiral pseudo-tensor), FM72 (Val16 projective-
model citation), FM73 (HTT SDR verbatim lift), FM74 (dim H^* < infinity
hypothesis) ALL reduce to the single ambient-assignment discipline.

3. The programme's "(D_X-mod, otimes^!)" phrasings in narration are replaced
system-wide by "(Dmod(Ran(X)), otimes^*) for factorisation statements" or
"(Dmod(X), otimes^!) for pure diagonal statements on the curve", whichever
is intended per site.

4. No downgrade of any theorem is required. Every result survives at full
strength in the ambient that honestly supports it; the repair is the
ambient-assignment table, not the claim strength.

## Verdict

(D_X-mod, otimes^!) is NOT universally correct. The programme needs the TRIPLE
ATLAS already implicitly present in foundations.tex L460-551: default ambient
is (Dmod(Ran(X)), otimes^*) [BD04 + FG12], with IndCoh(Ran(X)) [GR17] for
(infty,2)/Ind regime and D^b_c(Ran(X)) [BBD+MHM] for weight data. otimes^{ch}
is never an ambient - it generates operations inside Fact(X). Ind-completion
is mandatory for classes M and critical level; non-compact X replaces Verdier
with Borel-Moore on the eval-generated core; bulk-boundary promotes Fact(X) to
coloured Fact(X, partial X). Phrasings "(D-mod, otimes^!)" or "(D-mod,
otimes^{ch})" in narration are notational slips; the rigorous ambients are the
three listed with explicit bridges between them.
