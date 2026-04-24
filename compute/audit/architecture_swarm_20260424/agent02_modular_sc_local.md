# Agent 02 -- Modular Swiss-Cheese Local Model Examiner

Owned path: `compute/audit/architecture_swarm_20260424/agent02_modular_sc_local.md`

## Verdict

Route A is viable only as a **formal-collision / local operadic model**. The live chapter already says this in its opening frame, but several theorem-strength statements still promote local data to global geometry. The three critical leaks are:

1. `Loc` is asserted to be an equivalence at genus `0` and faithful at `g >= 1`; this is stronger than formal completion supports.
2. Fay/Arnold identities are used to prove global operadic formality of `C_*(FM_k(Sigma_g))`; the displayed derivation does not establish that theorem.
3. Curved coderived recovery and curved-Dunn vanishing are downstreamed as consequences of Route A; they require the factorization/Riemann-Hilbert route and cannot be derived from local operadic Koszulity.

Status recommendation: keep Route A as `\ClaimStatusProvedHere` only for the genus-0 local `SC^{ch,top}` theorem and for associated-graded/formal-collision statements. Mark full genus-g modular homotopy-Koszulity and global formality `\ClaimStatusConjectured` with the condition stated in the theorem title/body until the factorization comparison theorem is inscribed.

## Source Anchors Checked

- Vol II doctrine: `CLAUDE.md`, `AGENTS.md`.
- Route specs: `.claude/specs/master.md`, `.claude/specs/route-a-modular-sc.md`.
- Route A live chapter:
  - `chapters/theory/modular_swiss_cheese_operad.tex:21`--`79` local/global framing.
  - `chapters/theory/modular_swiss_cheese_operad.tex:1048`--`1247` mixed product decomposition.
  - `chapters/theory/modular_swiss_cheese_operad.tex:1263`--`1445` extraction functor.
  - `chapters/theory/modular_swiss_cheese_operad.tex:1478`--`1889` modular homotopy-Koszul proof.
  - `chapters/theory/modular_swiss_cheese_operad.tex:1907`--`2462` genus-g formality theorem.
  - `chapters/theory/modular_swiss_cheese_operad.tex:2929`--`3074` consequences and curved non-corollary.
  - `chapters/theory/modular_swiss_cheese_operad.tex:3348`--`3407`, `3992`--`4052` curved-Dunn/MC leakage.
  - `chapters/theory/modular_swiss_cheese_operad.tex:4255`--`4556` K3/Hilbert-scheme supplement.
- Route A neighboring chapters:
  - `chapters/connections/line-operators.tex:64`--`278`, `224`--`325`.
  - `chapters/connections/bar-cobar-review.tex:1398`--`1655`, `1806`--`1878`, `3897`--`4247`.
  - `chapters/examples/rosetta_stone.tex:97`--`142`.
  - `chapters/connections/modular_pva_quantization_core.tex:14`--`33`, `142`--`201`, `451`--`525`, `641`--`720`, `1918`--`2065`.
- Vol I dependencies:
  - `~/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:581`--`662`: modular pre-Koszul data and MK1--MK3.
  - `~/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:6251`--`6275`: bar complex as algebra over the Feynman transform.
  - `~/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:194`--`248`: three differentials and curvature package.
  - `~/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:8467`--`8479`: Feynman involution.
  - `~/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2178`--`2203`, `2476`--`2539`, `2776`--`2798`: mixed blowups, Type III faces, and `d_mix`.

## ATTACK -> HEAL Cycles

### Cycle 1 -- Route A Scope Inflation

**ATTACK.** The chapter opening correctly says `SCmod` is a formal-disc approximation (`modular_swiss_cheese_operad.tex:31`--`39`), but the preceding sentence asserts that modular homotopy-Koszulity "ensures that bar-cobar duality lifts to all genera" (`:27`--`:29`). The same inflation reappears in the flat-model corollary: "For any logarithmic `SCmod`-algebra" the modular bar-cobar adjunction is a Quillen equivalence and "requires no factorization input" (`:2929`--`:2946`). That is too strong unless `SCmod` is explicitly the formal-collision object and the statement is restricted to the flat derived category.

**HEAL.** Replace the global wording by:

> The Feynman transform of the formal-collision operad `SCmod^loc` produces the flat modular Maurer-Cartan equation. Conditional on modular homotopy-Koszulity of this local object, the flat bar-cobar adjunction is a Quillen equivalence in the derived category. This does not assert curved coderived recovery or global factorization on `Ran(Sigma_g)`.

Status replacement:

- `thm:modular-hkoszul-SC`: keep `\ClaimStatusProvedHere` only for the genus-0 `SCchtop` specialization.
- Full all-genus `SCmod`: change to `\ClaimStatusConjectured` or split into `Local theorem / Global comparison conjecture`.
- `cor:flat-model-equiv`: `\ClaimStatusProvedHere` only after the theorem is narrowed to `SCmod^loc`; otherwise conditional.

### Cycle 2 -- Formal Completion Does Not Give Equivalence/Faithfulness

**ATTACK.** `prop:extraction-functor` asserts:

- genus-0 equivalence of categories on `P^1` (`modular_swiss_cheese_operad.tex:1361`--`1363`);
- faithfulness but not fullness at `g >= 1` (`:1364`--`:1370`);
- proof by "remove a point to obtain C", "formal neighbourhood is isomorphic to C", and "formal discs form a cofinal system in any Weiss cover" (`:1387`--`:1407`).

This is false at the stated level. A formal neighborhood is not the affine curve `C`; trivial fundamental group does not recover factorization data from one completed stalk; formal disks are local charts, not a cofinal global cover for monodromy, periods, or D-module extension data. The master spec explicitly says the operad is the local shadow and misses global D-module structure.

**HEAL.** Replace the proposition with a local essential-image statement:

> `Loc` sends a BD/HT factorization Swiss-cheese datum to its formal-collision `SCmod^loc` coalgebra by restricting to completed neighborhoods of collision strata. It records OPE residues, ordered open-sector data, and formal mixed collision maps. At genus `0`, for translation-invariant vacuum-generated data on the formal disk, `Loc` is an equivalence onto its essential image. No full faithfulness is asserted for factorization algebras on `P^1` or `Sigma_g`. At `g >= 1`, periods, monodromy, Arakelov corrections, and `kappa(A) omega_g` lie outside the image.

Status replacement:

- `prop:extraction-functor`: `\ClaimStatusProvedHere` only for construction and compatibility with restriction.
- Equivalence/faithfulness clauses: remove or mark `\ClaimStatusConjectured` under additional global reconstruction hypotheses.

### Cycle 3 -- Mixed Product Decomposition Contradicts the Open-Closed FM Model

**ATTACK.** `prop:mixed-product-decomposition` claims a homotopy equivalence
`C_*(FM_{k|m}(Sigma_g, partial)) ~= C_*(FM_k(Sigma_g)) tensor C_*(E_1(m))` (`modular_swiss_cheese_operad.tex:1048`--`1057`) and proves it by saying no mixed screens arise (`:1090`--`:1099`, `:1235`--`:1246`). Vol I's open-closed configuration-space chapter says the opposite: mixed blowups are part of the compactification (`configuration_spaces.tex:2178`--`2203`), Type III mixed bubbling faces are genuine (`:2476`--`:2539`), and they contribute the mixed differential `d_mix` (`:2776`--`:2798`). Vol II `modular_pva_quantization_core.tex:315`--`326` also lists mixed bubbling as a codimension-one degeneration.

**HEAL.** Replace product decomposition by an associated-graded statement:

> Filter the mixed open-closed compactification by mixed-bubbling depth. The associated graded for depth `0` splits as `C_*(FM_k(Sigma_g)) tensor C_*(E_1(m))`. The full complex contains Type III faces and a mixed differential `d_mix`; these are the local bulk-to-boundary operations, not contractible collar noise.

Status replacement:

- `prop:mixed-product-decomposition`: replace by `prop:mixed-associated-graded-decomposition; \ClaimStatusProvedHere`.
- `lem:operadic-kunneth`: retain only for the associated graded; its use in `thm:modular-hkoszul-SC` becomes conditional on controlling `d_mix`.

### Cycle 4 -- Fay/Arnold Derivation Is Overclaimed

**ATTACK.** The chapter claims "Fay trisecant implies the Arnold relation at genus g" (`modular_swiss_cheese_operad.tex:1516`--`1520`) and derives a global Arnold identity by declaring theta derivative remainders symmetric (`:1561`--`:1588`), then defining `S` as the same three-term expression (`:1589`--`:1597`), then proving symmetry by cyclic invariance and pair exchange (`:1598`--`:1606`). This does not prove full symmetry in four variables. Later, the symmetric remainder is killed by antisymmetric structure constants (`:1713`--`:1763`), which can justify a contracted Lie-type cancellation in a specific invariant projection, not an identity of forms on `Conf_k(Sigma_g)`.

There is also an analytic mismatch at genus `1`: the Weierstrass `zeta` function is quasi-periodic, not a globally defined elliptic function. The almost-holomorphic/KZB correction is precisely the missing global data. Thus "Fay is local" is correct only after formal completion or after the corrected holomorphic model has been specified with the required period/quasi-period terms.

**HEAL.** Replace the claim by:

> Fay's trisecant identity supplies the local collision identities for the prime-form/KZB propagator. On the formal screen of any collision stratum, the leading term reduces to the genus-0 Arnold relation. In Lie-type contractions, the symmetric Fay remainder vanishes after projection to the antisymmetric invariant tensor. At genus `1`, the statement uses the almost-holomorphic/KZB completion of the elliptic propagator. This proves the local cancellation needed for the corrected holomorphic differential; it does not by itself prove global operadic formality.

Status replacement:

- `eq:genus-g-arnold`: state as "contracted local Arnold/Fay cancellation", not as a global form identity.
- Fay-to-formality step: `\ClaimStatusConjectured` unless a primary theorem proves the operadic formality comparison.

### Cycle 5 -- Global Operadic Formality and Feynman Involutivity Are Not Established

**ATTACK.** `thm:genus-g-formality` claims the dg operad `{C_*(FM_k(Sigma_g))}` is formal for every smooth projective curve (`modular_swiss_cheese_operad.tex:1907`--`1927`). The proof constructs a Kontsevich-style integral map, but the quasi-isomorphism step says the linear part is the "identity inclusion `H_* -> C_*`" (`:2398`--`:2411`), which is not a canonical chain map. The independence-of-complex-structure argument invokes contractibility of the space of `L_infty` quasi-isomorphisms (`:2414`--`:2444`) without a cited obstruction calculation. Then Feynman involutivity and closed-colour Quillen equivalence are invoked from this formality (`:2465`--`:2499`), and the literature comparison says this is proved by Fay (`:2832`--`:2838`).

Vol I gives Feynman involution for modular operads satisfying Poincare duality (`higher_genus_foundations.tex:8467`--`8479`) and bar-as-Feynman-transform structure (`bar_cobar_adjunction_curved.tex:6251`--`6275`), but that does not prove the new genus-g operadic formality theorem here.

**HEAL.** Split the theorem:

> `Theorem` (local screen formality; `\ClaimStatusProvedHere`): on each formal collision screen the operation complex reduces to the genus-0 FM/Kontsevich local model; screen boundary cancellations are governed by Arnold/Fay.

> `Conjecture` (global genus-g operadic formality; `\ClaimStatusConjectured`): the full partially modular closed-colour operad `{C_*(FM_k(Sigma_g))}` is formal compatibly with stable-graph clutching and mixed operations.

Then make `thm:modular-hkoszul-SC` conditional on this conjecture, or replace `C_*(FM_k(Sigma_g))` by the formal-completion operation spaces where the local theorem actually applies.

### Cycle 6 -- Curved Equivalence Is Reintroduced After Being Disclaimed

**ATTACK.** The chapter correctly states the curved coderived equivalence is not a corollary (`modular_swiss_cheese_operad.tex:3002`--`3032`). But downstream claims re-import it:

- `thm:curved-dunn-bridge` asserts a quasi-isomorphism and `H^2 = 0` (`:3360`--`:3407`), with proof relying on references not checked in the local chapter.
- `thm:cross-genus-mc` is titled unconditional and uses `H^2(...)=0` "proved via the Fay trisecant formality" (`:4028`--`:4052`).
- `bar-cobar-review.tex` states curved `R`-factorization, a period-corrected `E_1` dg coalgebra, and coderived recovery (`bar-cobar-review.tex:3897`--`4133`, especially `:4021`--`:4025`).
- Canonicity language says the open color is a functor of the closed color and the modular homotopy type and `R`-factorization determine each other (`bar-cobar-review.tex:4220`--`4247`).

This conflicts with the Route A hierarchy. Curved data is global; it requires factorization and chiral Riemann-Hilbert comparison. Directionality forbids open-to-closed operations; it does not imply the open color is a functor of the closed color.

**HEAL.** Keep only the local/flat statement in Route A:

> The local operadic model supplies the flat formal-collision side of the comparison. Curved coderived recovery, curved-Dunn vanishing, and cross-genus MC solvability are conditional on the factorization route plus the Riemann-Hilbert bridge. They are not consequences of `thm:modular-hkoszul-SC`.

Status replacement:

- `thm:curved-dunn-bridge`: `\ClaimStatusConjectured` with the factorization/Riemann-Hilbert condition stated in the theorem title/body unless the cited curved-Dunn chapter is already a checked proof in the integration pass.
- `thm:cross-genus-mc`: remove "unconditional"; replace by "conditional on curved-Dunn `H^2` vanishing and the factorization comparison".
- `bar-cobar-review.tex:4021`--`4025`: "curved quasi-isomorphism" should cite a precise Vol I theorem and be marked coderived/factorization, not Route A.

### Cycle 7 -- K3 / Hilbert-Scheme Supplement Does Not Belong to Route A Local Model

**ATTACK.** The local operadic chapter ends with global K3/Siegel/Hilbert-scheme material (`modular_swiss_cheese_operad.tex:4255`--`4556`): K3 bi-based factorization, `1/Phi_10`, M5 punctures, and `\ClaimStatusProvedHere` stabilization through `SC^{mod}`. These are not local-collision consequences of Route A. Some entries are marked conjectural, but others are proved-here theorem statements (`:4489`--`:4556`) whose proof depends on global geometric representation theory, stable envelopes, and K3 factorization bases, not the local operadic theorem.

**HEAL.** Move or demote:

> Keep only a short pointer remark in Route A: "Global K3/Siegel examples require the factorization route and are treated in the K3 synthesis surface." The detailed K3/Hilbert-scheme claims should live in an examples/frontier chapter with their own source audit.

Status replacement:

- K3/Hilbert-scheme `\ClaimStatusProvedHere` inside Route A: demote to `\ClaimStatusConjectured` or move out of the local chapter.
- `1/Phi_10` partition-function claim can remain `\ClaimStatusConjectured`, but it should not be presented as a closed-colour operation of the local `SCmod` without the global factorization base theorem.

## Exact Replacement Package

Recommended minimal replacements for the integration thread:

1. Rename `SCmod` in the local theorem statements to `SCmod^{loc}` or explicitly define `SCmod` as the formal-completion/collision model. If the symbol is kept, every theorem using it must say "formal-collision".
2. Replace `prop:mixed-product-decomposition` by `prop:mixed-associated-graded-decomposition`.
3. Replace `prop:extraction-functor` by `con:formal-collision-extraction` plus an essential-image proposition; delete full faithfulness/equivalence unless extra hypotheses are added.
4. Split `thm:genus-g-formality` into local-screen theorem and global-formality conjecture.
5. Make `thm:modular-hkoszul-SC` conditional on the global-formality conjecture, or restrict it to the formal local model.
6. Replace every downstream "curved equivalence follows" sentence by "requires factorization Koszul duality and chiral Riemann-Hilbert comparison".
7. Move the K3/Hilbert-scheme supplement out of the Route A local chapter or demote theorem statuses.

## Commands Run

- `wc -l` on required Vol II files.
- `git status --short`, `git diff --stat`.
- `sed -n` / `nl -ba` on `CLAUDE.md`, `AGENTS.md`, `.claude/specs/master.md`, `.claude/specs/route-a-modular-sc.md`, and the requested chapter anchors.
- `rg -n` for `Fay`, `Arnold`, `curved`, `formal`, `Loc`, `mixed`, `d_mix`, `SCmod`, and Vol I labels.
- `nl -ba` on Vol I modular Koszul anchors listed above.

No build was run. No shared TeX was edited.

## Files Changed

- Added this report only: `compute/audit/architecture_swarm_20260424/agent02_modular_sc_local.md`.
