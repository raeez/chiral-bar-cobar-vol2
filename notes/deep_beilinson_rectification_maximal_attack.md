# Deep Beilinson Rectification — Maximally Adversarial Audit

**Author**: Raeez Lorgat. **Date**: 2026-04-17. **Scope**: Vol I + Vol II + Vol III.
**Posture**: Russian school (Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Kapranov,
Gaitsgory) attacking the programme at face value. Defense disabled. No commits.

The session map asserts Tier 1–7 inscribes nine Platonic theorems and ~20+
Tier-3 chapters as `\ClaimStatusProvedHere`. After file-by-file audit against
.tex ground truth, .md cache, and the Russian-school literature anchors, the
manuscript carries a thick layer of **scope inflation, hidden hypotheses, and
proof–statement gaps that the `\ClaimStatusProvedHere` tag conceals**. The ten
most serious weaknesses below are ranked by impact on the architecture of the
programme, not by file size or count of `FM` ID closures.

---

## Ranked weaknesses (1 = most serious)

### W1 (impact: existential). Theorem $A^{\infty,2}$ — properad lift via Hackney–Robertson is asserted, not proved.
**File**: `~/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex:235–385`.
**Defect**: Step 3 of the proof (lines 354–370) sketches the properad lift in
~17 lines of prose — "applying the left adjoint of the Hackney–Robertson
inclusion to each piece produces an $(\infty,2)$-categorical adjunction at
properad level". HR19 (`HackneyRobertson2019` Prop. 6.1) gives a model structure
on properads, **not** a left adjoint between operad and properad model
structures, and **not** the conilpotent-completeness preservation under
graph-wise extension. Three concrete gaps: (i) "left adjoint" is named without
construction; (ii) the radical filtration on properads at $(n,m)$-valence is
not equivalent to the bar-length filtration on operads under the "graph-wise
extension"; (iii) Mittag–Leffler at properad level is asserted, not derived.
**Ghost theorem**: A properad-level bar–cobar adjunction probably exists in the
Hackney–Robertson + Francis–Gaitsgory ambient. **Correction**: Restrict the
$\ClaimStatusProvedHere$ tag of `thm:A-infinity-2` to operad-level Step 1+2;
mark Step 3 (properad lift) as `\ClaimStatusConjectured` until a proper
construction is supplied. **FM-DBR-1**.

### W2 (impact: existential). Chiral Higher Deligne — Stage 2 strict $E_3$ via Sugawara is wrong at chain level.
**File**: `~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex:451–476`.
**Defect**: The proof of Theorem H upgrade reads (line 461): "Dunn additivity …
the $E_2$-chiral action and the $E_1$-topological action along $\R$ combine
into an $E_3$ action," and (lines 466–468): "$L_0$ acts chain-level strictly as
a derivation. Hence Dunn's theorem for chain-level factorisation algebras
yields a strict $E_3$-chiral action." This conflates **two distinct claims**:
(a) Dunn additivity for *operads* on disjoint-cube products $E_2 \otimes E_1
\xrightarrow{\sim} E_3$ — Lurie HA 5.1.2.2, valid; (b) Dunn-type composition of
*algebras* via factorisation along $\R$ when one factor is non-formal — open.
For class M with quartic OPE poles (FM82), $L_0$-derivation strictness fails
at chain level because the brace structure has nontrivial Stasheff
$d_{\mathrm{ch}}$-exact terms (the chapter's own Prop 3.4 admits this). The
"strict" $E_3$-chiral action is at most $E_3$-up-to-coherent-homotopy. The
chapter's own Remark `rem:chd-associator-discipline` (lines 508–522) admits
chain-level associator dependence — inconsistent with "strict" two paragraphs
prior. **Ghost theorem**: $E_3$-chiral action exists up to associator-fixed
strictification (the honest CHD statement). **Correction**: Edit line 468 to
"strict-up-to-coherent-homotopy", or downgrade `thm:chiral-higher-deligne`
from "$E_3$-chiral" to "$E_3$-chiral-up-to-Drinfeld-associator". **FM-DBR-2**.

### W3 (impact: existential). DS–Hochschild bridge proof — Step 3 (HPL) skips the OPE convergence check.
**File**: `~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex:690–705`.
**Defect**: "The HPL transfer applies chain-level because Arakawa's
$C_2$-cofiniteness ensures the retract data are defined on each
conformal-weight stratum (no infinite-dimensional pathology in the contracting
homotopy)." Two missing inputs: (i) Arakawa Ann. Math. 2015 (arXiv:1004.1554)
gives $C_2$-cofiniteness for *generic* $k$ and *principal* $f$; for
*hook-type* $f$, $C_2$-cofiniteness is conjectural in general (Kac–Roan–
Wakimoto 2003 gives the BRST for arbitrary good gradings but NOT the
cofiniteness); (ii) the contracting homotopy $h$ in Crainic perturbation must
be Sigma-equivariant when $\cW_k(\fg, f)$ has nontrivial outer automorphisms
— missing for $\fsl_3$ + $f_{\min}$ (BP), where the residual $\fsl_2$ acts on
$G^\pm$. The proof claims `closes FM126/FM185/FM186/FM214` but the hook-type
generalisation is conditional on Arakawa $C_2$-cofiniteness for non-principal,
which is itself open. **Ghost theorem**: principal-only DS–Hoch bridge is
correct. **Correction**: Restrict `thm:chd-ds-hochschild` to principal $f$;
hook-type extension `\ClaimStatusConditional` on Arakawa $C_2$-non-principal.
**FM-DBR-3**.

### W4 (impact: structural). Universal Holography functor — Move 4 invokes
"Koszul duality of reduction and factorization homology" without citation.
**File**: `~/chiral-bar-cobar-vol2/chapters/connections/universal_holography_functor.tex:393–417`.
**Defect**: Line 411–412 reads "DS applied to the Costello–Gaiotto bulk is, by
the Koszul duality of reduction and factorization homology (Gaiotto–Witten,
Sugawara-type reduction of the bulk), the Costello–Gaiotto bulk of the
$\cW$-theory." No paper of Gaiotto–Witten proves this; Costello–Gaiotto 2018
(arXiv:1804.06460) and 2021 (arXiv:2103.01042) construct the bulk DS reduction
**at the level of factorization algebras on $X \times \R$**, not as a
chain-level identity of $E_3$-chiral algebras. The "compose chain-level
equalities" sentence (lines 414–416) is unjustified. **Ghost theorem**: the
class-M chain-level identification reduces to (i) class-L bulk identification
(CFG), (ii) DS bulk reduction (CG18/CG21), (iii) DS–Hoch chain-level bridge
(W3). Each step is its own theorem. **Correction**: Replace the prose with an
explicit three-step proof, citing CFG arXiv:2602.12412, CG arXiv:1804.06460,
and `thm:chd-ds-hochschild`; spell out the chain-level vs. cohomological
distinction at each step. **FM-DBR-4**.

### W5 (impact: structural). $K_W$ universal "exponent formula" propagation gap.
**Files**: `notes/kw_universal_formula_g2_attack_heal.md` (correct);
`notes/kw_rho_rho_vee_universal_lie_invariant.md` (correct);
`notes/universal_koszul_complementarity_kv_kw_all_simple.md` (HAS THE WRONG
FORMULA). The G2 note proves $K_W(G_2) = 388$, $K_W(F_4) = 2648$ via the
universal Lie invariant $K_W(g) = 2\,\mathrm{rank} + 12 \sum_i m_i(m_i+1)$
(Shapiro–Steinberg–Kostant). The companion universal-Koszul-complementarity
note still carries the **falsified** simply-laced-only $K_W = 2\,\mathrm{rank}
+ 4 h^\vee \dim$ at line 172 and the **falsified** lacing variant
$K_W = 2\,\mathrm{rank}\cdot(1 + 2h^\vee + 2(h^\vee)^2/r_g)$ at line 203 / 370.
**Ghost theorem**: Universal $K_W$ via exponents is correct. **Correction**:
Edit `universal_koszul_complementarity_kv_kw_all_simple.md` to delete the SL
formula and lacing variant; install the exponent-theoretic form at one canonical
location. **FM-DBR-5**.

### W6 (impact: structural). $K_V(g) = 2\dim(g)$ super-extension fails at h^∨ = 0.
**File**: `notes/kv_super_lie_algebras_attack_heal.md`.
**Defect**: The super-extension table claims $\mathrm{D}(2,1;\alpha)$ has
$h^\vee = 0$ for ALL $\alpha$. This is **FALSE**: $\mathrm{D}(2,1;\alpha)$ has
$h^\vee = 0$ only at the three degenerate points $\alpha \in \{-1, 0, \infty\}$
where the algebra collapses to a direct sum of simpler pieces. At generic
$\alpha$, $h^\vee = -1 - \alpha \cdot$(normalising constant) is nonzero, so
Sugawara is well-defined and $K_V$ extends. The note's blanket "UNDEFINED at
generic $\alpha$" is wrong. **Ghost theorem**: $K_V = 2\,\mathrm{sdim}$ for
basic classical superalgebras with non-degenerate Killing supertrace AND
$h^\vee \ne 0$ (a generic codimension-3 condition). **Correction**: Replace
the row for $\mathrm{D}(2,1;\alpha)$ with "$h^\vee = h^\vee(\alpha) \ne 0$ at
generic $\alpha$; degenerate at $\alpha \in \{-1, 0, \infty\}$"; restrict the
"UNDEFINED" verdict to those three points. **FM-DBR-6**.

### W7 (impact: architectural). BP $K_W = 196$ vs. universal $K_W$ exponent formula — incompatibility.
**File**: `~/chiral-bar-cobar-vol2/chapters/theory/bp_chain_level_strict_platonic.tex:732–745`.
**Defect**: The chapter installs $K_W(\mathrm{BP}) = 196$ as the polynomial
identity $\kappa(\mathrm{BP}_k) + \kappa(\mathrm{BP}_{-k-6}) = 196$. The
universal $K_W$ formula via exponents (W5) gives $K_W(\fsl_3, f_{\mathrm{prin}}) =
2\cdot 2 + 12\cdot(1\cdot 2 + 2\cdot 3) = 100$, NOT 196. The two formulas
disagree because BP is **not** the principal $\cW$-algebra — BP is the
*minimal* $\cW$-algebra $\cW^k(\fsl_3, f_{\min})$. The universal
$K_W(g, f)$ = $K_W(g) - $ (correction depending on Bala–Carter label of $f$).
For BP, the correct formula is $K_{\cW(g, f_{\min})} = K_V(g) - 2\,\mathrm{rank}
+ \mathrm{ghost~contribution}$. The chapter says (line 743) "the universal BP
Koszul conductor, matching Vol I `thm:koszul-conductor-bp` (AP140/B52/C31/FM22)"
— a Vol I theorem the audit cannot locate verbatim. **Ghost theorem**: each
$\cW(g, f)$ has its own conductor depending on $f$. **Correction**: name the
$f$-dependence explicitly; demonstrate that the universal exponent formula does
not apply at non-principal $f$ but is replaced by a Bala–Carter-dependent
formula whose BP value is 196. **FM-DBR-7**.

### W8 (impact: architectural). FF chain-level (Tier 4) — three "obstructions collapse" arguments are sketches, not proofs.
**File**: `notes/ff_tier_4_chain_level_attack_heal.md`.
**Defect**: The note claims (in summary): "the three obstructions identified by
the prior agent all reduce to computable classes that either (i) match between
LHS and RHS (obstruction a → part of the answer), or (ii) collapse under
existing tier-3 theorems (obstruction b), or (iii) vanish at critical level
(obstruction c)." Each "collapse" is asserted in 2–3 lines without proof:
obstruction (a) "MATCHES the T*Op DG model on the oper side" — needs
explicit $E_\infty$-quasi-iso, not "matches"; (b) "FG 2004 + AG 2015" prove
the singular-support equivalence at the **derived module category** level, not
at the **endomorphism algebra** level (the FF–chain question is about the
algebra, not its modules — see FF tier 3 vs tier 4 distinction in the
companion `feigin_frenkel_centre_categorification_attack_heal.md`); (c) the
"integer Cartan matrix kills GRT_1 torsor" sentence applies to OPE between
screening currents but NOT to the Tamarkin formality on the bar complex of
$\cV_{-h^\vee}(\fg)$ itself, which has its own GRT_1-torsor. **Ghost theorem**:
A chain-level FF quasi-iso PROBABLY exists via semi-infinite cohomology +
Voronov $E_\infty$. **Correction**: Honestly mark FF tier 4 as conjectural,
not "closable with one Voronov compatibility check". The companion note
correctly tags it tier-4-OPEN. **FM-DBR-8**.

### W9 (impact: structural). Heptagon edge (3)↔(4) torsor count.
**File**: `notes/heptagon_edge_34_grt_equivariant_heal.md`,
`notes/heptagon_edge_34_associator_independent_attack_heal.md`,
`~/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex`.
**Defect**: The associator-independent attack note correctly identifies edge
(3)↔(4) as $\mathrm{GRT}_1(\Q)^{\oplus 2}$-torsor (closed-sector + mixed-sector
copies). The "GRT-equivariant heal" then upgrades this to a 7-vertex × 21-edge
torsor structure with **independent** $\mathrm{GRT}_1^{\mathrm{cl}}$ and
$\mathrm{GRT}_1^{\mathrm{mix}}$ actions on each face. The independence claim
is unsupported: Willwacher's $H^0(GC_2) \cong \mathfrak{grt}_1$ uses the
**closed** graph complex; the **mixed** graph complex $GC^{\mathrm{SC,mix}}_2$
is conjectured (Willwacher's mixed-Swiss-cheese paper, in preparation as of
2026-04-17) to have $H^0$ = $\mathfrak{grt}_1$ AS WELL but the action on the
closed sector is via the same generators (Willwacher 2015 Conjecture 6.3 is
NOT a published theorem). **Ghost theorem**: The two-copy torsor structure
exists at the level of *partial* graph-complex computations; its independence
is conjectural. **Correction**: Mark the "two independent GRT_1 copies" claim
as `\ClaimStatusConjectured`, citing Willwacher Conjecture 6.3 as the open
input. The single-copy torsor (closed only) is unconditional. **FM-DBR-9**.

### W10 (impact: meta-structural). Independent verification protocol — 0 / 1134 + 0 / 2275 coverage gap remains.
**Files**: `compute/lib/independent_verification.py` (infrastructure);
`compute/tests/` (no `@independent_verification` decorators installed); .tex
catalogue admits FM224 (Vol II) and FM-equivalent in Vol I.
**Defect**: The mechanical-invariant protocol declared in CLAUDE.md and
installed in `compute/lib/` is operational, but **zero claims are decorated**
in Vol I or Vol II. The session map says "T7: 5–10 decorators per session";
audit count: **186 decorators in Vol II compute/, 282 in Vol I compute/** — but
the grep `@independent_verification` returns these counts **inside the
infrastructure stubs** (FRAME_SHAPE_DATA-style hardcoded test scaffolds), not
on actual ProvedHere claims. The HZ-IV protocol's own "tautological detection"
guard is unenforced because there are no decorator-targets to audit.
**Ghost theorem**: 100% mechanical verification is achievable with effort.
**Correction**: Top-5 decorator-install priorities are listed in CLAUDE.md
(thm:E3-topological-km, thm:E3-topological-DS-general, thm:E3-topological-free-PVA,
thm:global-triangle-boundary-linear, thm:modular-bar). The Tier-7 plan asks for
5–10 per session; without these, the "Universal Holography proved" headline
rests on uncovered ProvedHere claims. **FM-DBR-10**.

---

## Summary table

| W# | Domain | File:line | Severity | Repair path |
|----|--------|-----------|----------|-------------|
| W1 | Theorem A^{∞,2} properad | theorem_A_infinity_2.tex:354–370 | EXISTENTIAL | Cite HR19 with explicit left adjoint OR downgrade properad lift to Conjectured |
| W2 | CHD strict E_3 | chiral_higher_deligne.tex:466–468 | EXISTENTIAL | Replace "strict" with "strict-up-to-Drinfeld-associator" |
| W3 | DS–Hoch hook-type | chiral_higher_deligne.tex:692–704 | EXISTENTIAL | Restrict to principal f; hook-type Conditional on Arakawa C_2 |
| W4 | UH Move 4 citation | universal_holography_functor.tex:411–417 | STRUCTURAL | Replace with explicit 3-step CFG + CG18 + W3 |
| W5 | K_W cross-volume sync | universal_koszul_complementarity_kv_kw_all_simple.md:172/203/370 | STRUCTURAL | Single-source the exponent formula; delete falsified variants |
| W6 | K_V super D(2,1;α) | kv_super_lie_algebras_attack_heal.md | STRUCTURAL | Generic α has h^∨ ≠ 0; restrict UNDEFINED to {-1,0,∞} |
| W7 | BP K_W = 196 | bp_chain_level_strict_platonic.tex:743 | ARCHITECTURAL | Spell out non-principal Bala–Carter formula |
| W8 | FF tier 4 closable | ff_tier_4_chain_level_attack_heal.md | ARCHITECTURAL | Mark tier 4 OPEN; do not promote sketch to closure |
| W9 | Heptagon GRT^{⊕2} | heptagon_edge_34_grt_equivariant_heal.md | STRUCTURAL | Cite Willwacher Conj 6.3 as open input; mark independence Conjectured |
| W10 | HZ-IV decorator coverage | compute/tests/ all | META-STRUCTURAL | Install top-5 decorators; bridge between protocol and ProvedHere claims |

---

## Cross-volume FM additions to `appendices/first_principles_cache.md`

- **FM240 (= W1)** Theorem A^{∞,2} properad lift via HR19: 17-line prose-sketch in
  `theorem_A_infinity_2.tex:354–370`. Three concrete gaps. Counter: cite explicit
  HR19 left adjoint OR downgrade.
- **FM241 (= W2)** CHD Stage 2 conflates Dunn-of-operads with Dunn-of-algebras for
  non-formal class M. Counter: rewrite "strict" → "strict-up-to-Φ".
- **FM242 (= W3)** DS–Hoch hook-type closure presumes Arakawa C_2 for non-principal,
  which is conjectural. Counter: restrict scope.
- **FM243 (= W4)** UH Move 4 cites a Gaiotto–Witten theorem that does not exist as
  written. Counter: explicit 3-step bibliography.
- **FM244 (= W5)** K_W universal formula propagation gap: 1 of 3 cross-volume
  sources still carries the falsified SL-only and lacing variants.
- **FM245 (= W6)** D(2,1;α) h^∨ varies in α; "h^∨ = 0 always" is wrong.
- **FM246 (= W7)** BP K_W = 196 ≠ universal-K_W(sl_3) = 100 because BP is non-
  principal (hook = minimal); conductor is f-dependent.
- **FM247 (= W8)** FF tier 4 "closable" is sketch, not proof; cite tier-3 paper for
  module-category equivalence; mark tier 4 OPEN.
- **FM248 (= W9)** Heptagon (3)↔(4) two-copy GRT torsor structure depends on
  Willwacher Conj 6.3 (mixed graph complex H^0 = grt_1).
- **FM249 (= W10)** HZ-IV decorator coverage: 0 / 1134 (Vol II) and 0 / 2275 (Vol I)
  installed; the protocol is in place but the campaign has not begun.

---

## Closing assessment

The session map's nine Platonic theorems land at three genuine levels:
**operad-level adjunction theorems** that are honest (Tier 1 on operads);
**chain-level / properad-level upgrades** that are sketches (Tier 1 on properads,
Tier 3 on class M, FF tier 4); and **universal cross-family formulas** that
mix correct statements (universal K_W exponent formula) with falsified
variants still circulating in companion notes. The HZ-IV protocol is
infrastructure-complete but campaign-empty.

The strongest honest target — articulated in HEAL-SWEEP and PLATONIC
RECONSTITUTION sections of CLAUDE.md — remains achievable, but the present
manuscript over-tags `\ClaimStatusProvedHere` for several theorems whose
proofs are sketches. Without honest tag downgrades or honest proof completions
(W1–W4), the "Universal Holography proved unconditionally on the Koszul locus"
headline rests on conditional inputs (Arakawa C_2 hook-type, CG18/CG21
chain-level lift, FF tier 4) that the manuscript itself elsewhere admits are
open.

The Russian-school posture is satisfied by the following honest statement:

> The programme defines the right objects, names the right targets, and
> sketches the right proofs. The Tier-1 properad lift, the CHD strict E_3,
> the DS–Hoch hook-type, and the UH class-M chain-level identification each
> require ~5–20 pages of additional construction to promote sketch to proof.
> Until those constructions are written, the corresponding `\ClaimStatusProvedHere`
> tags are over-stated; honest tags are `\ClaimStatusProvedHereConditional` or
> `\ClaimStatusConjectured` per W1–W4.

No commits made. No .tex edits made. Findings reported in this note for
operator review.
