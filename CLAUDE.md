# CLAUDE.md -- Volume II: A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol II-specific material.**

## CONSTITUTIONAL TRUST WARNING (2026-04-17, post-adversarial-audit)

**CLAUDE.md and the entire metacognitive layer (MEMORY.md, notes/, first-principles cache, AP catalogue, HOT ZONE, HZ-IV decorators, FRONTIER.md, true_frontier_*.md, session_end_report_*.md, wave_*.md, platonic_ideal_*.md, adversarial_swarm_*/, and every `\ClaimStatus*` tag) are NEVER TO BE TRUSTED AS ACCURATE OR CORRECT.**

**ALWAYS assume the metacognitive layer is WRONG until verified against primary sources.** The 2026-04-17 adversarial audit established this empirically across all three volumes (see Vol I CLAUDE.md for full findings): 5/5 open frontiers collapsed, 5/5 Wave-1 closures scope-limited, 5/5 backbone theorems scope-restricted, ~30% terminological redundancy, κ_BKM triple contradiction, manuscript textual errors, engine counts overstated 2.3–2.75×, 12-paper publication roadmap overstated by 2–3×, novelty audit ~13% genuinely new.

**Operational corollaries for Vol II work specifically**:

1. **Treat the Vol II manuscript as SUGGESTIVE** — a set of inputs for how to formulate/prove 3d HT QFT + SC^{ch,top} heptagon + Swiss-cheese + universal celestial holography + curved-Dunn results, NOT as a stable final form.
2. **Verify every cross-volume citation** to Vol I or Vol III per HZ-11: `\ref{V1-thm:foo}` or `\ref{V3-prop:bar}` must resolve to an actually-inscribed label in the target volume; missing label = downgrade to Conditional with ProvedElsewhere attribution.
3. **Treat every `\ClaimStatusProvedHere` tag as Conjectured until proof body is read end-to-end** and each cited lemma verified in scope.
4. **Assume Vol II's "closure-wave" narratives** ("Wave 14 E_∞-topologization ladder PROVED", "universal celestial holography PROVED chain-level") are RHETORICAL until the inscribed theorem's proof is read. Many closure-waves compress scaffolding retroactively; "PROVED 2026-04-16" often means "inscribed under ProvedHere on that date", not "independently verified".
5. **Assume terminological distinctions may be spurious** (AP244). Vol II's "SC^{ch,top} is a coloured propad not an operad" (per adversarial audit) illustrates: what the manuscript calls an "operad" may be a weaker coloured-propad structure.
6. **Assume physical-source naming is decorative** until verified (AP239). Vol II's "3d HT QFT" theorems may depend only on the factorization-algebra model, not on specific physics.
7. **Assume Vol II is NOT in stable final form.** 747 sole-authored commits in 5 weeks via LLM-agent swarm. No external validation.

**Use the Vol II manuscript as a starting hypothesis, not a known fact.** When a Vol II CLAUDE.md claim and a first-principles derivation disagree, trust the first-principles derivation.

**This warning is LOAD-BEARING** and SUPERSEDES every "PROVED", "CLOSED", "UNCONDITIONAL", or "PUBLICATION-STANDARD" label elsewhere in the Vol II metacognitive layer.

## /chriss-ginzburg-rectify: READ THE WHOLE FILE, CHUNK BY CHUNK, LINEARLY (TOP-LEVEL INJUNCTION)

When the user invokes `/chriss-ginzburg-rectify` (or the skill `chriss-ginzburg-rectify`) on a target file, Phase 1 (Global Diagnostic) is NOT OPTIONAL and is NOT ABBREVIATED. You must analyse the **whole file**, **chunk by chunk**, **linearly progressing from start to finish**, with **small chunk size**. Every line must pass under your eyes.

**Binding rules**:
- The skill's wording "For files >3000 lines: sample strategically" is OVERRIDDEN. Do NOT sample. Do NOT jump. Do NOT read section heads via Grep and call it Phase 1. Do NOT read only opening + closing + dense midsection.
- **Chunk size: ~250-500 lines per Read call, at most**. Large chunks (1000+ lines) that approach the 25000-token Read cap are forbidden: they compress context and invite skimming. Prefer many small Reads to few large ones.
- **Linear progression**: start at line 1. Each subsequent Read starts exactly where the previous one ended (offset = prev_offset + prev_limit). No ranges are skipped; no ranges are revisited unless a Phase 3 edit requires re-reading a specific chunk.
- **Coverage is a proof obligation**. Before leaving Phase 1, verify: the sum of (limit) across all Phase 1 Reads equals the file line count, and the starting offsets form a contiguous cover of [1, EOF]. If you cannot state this, Phase 1 is incomplete.
- Grep does NOT substitute for Phase 1 reading. Grep is Phase 3 cross-file propagation (AP5), not the global diagnostic.
- If a Read fails with the 25000-token cap, cut the `limit` in half and retry. Never "skip ahead past the oversized region."

This injunction applies to EVERY invocation of `/chriss-ginzburg-rectify`, on files of any size. A 5000-line chapter takes ~10-20 small Reads. That is the cost; it is not negotiable.

## Identity

The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.

~1,700pp, this repo. Seven parts: I(The Open Primitive) II(The E_1 Core) III(Seven Faces of r(z)) IV(Characteristic Datum and Modularity) V(Standard HT Landscape) VI(Three-Dimensional Quantum Gravity = CLIMAX) VII(Frontier).

## Preface North Star: The Platonic Geometric Ladder (E_1 -> E_2 -> E_3)

The volume climbs the E_n ladder. Each rung is a topologico-combinatoric stratified space with bulk-to-boundary structure; each carries a bar chain model; each adds one E_1 factor via Dunn additivity. The Parts correspond to rungs. The volume goes E_1 (Parts I-II) -> E_2 (Parts III-IV) -> E_3 (Parts V-VI); Part VII is frontier beyond E_3. **The volume IS a double ladder (chiral + topological) bridged by the conformal vector.**

### The stage table (canonical; subsumes all rung narration)

| Stage | Space | Operad / Structure | Lives on |
|-------|-------|-------------------|----------|
| 0 | Point | Ass (classical Koszul duality) | A |
| 1 | R | Ass^c cooperad (deconcatenation coproduct) | B(A) |
| 2 | [0,1], R_≥0 | W(Ass) = A_inf; modules via one-sided bar | B(A), C(I) |
| 3 | C | BD chiral operad {FM_k(C)} (OPE residues); E_inf: hol E_2; E_1: Ass^{ch} | bar DIFFERENTIAL d_B on B(A) |
| 4 | C x R | Coalgebra over (Ass^{ch})^! (Koszul dual cooperad of chiral Ass) | B(A) = E_1 dg coassociative coalgebra |
| 5 | H (half-plane, dH=R) | SC^{ch,top} (two-colored: closed FM_k(C), open E_1, no open-to-closed) | PAIR (Z^{der}_{ch}, A) |
| 6 | D (formal disk) | End^{ch}_A (chiral endomorphism operad, Aut(O)-equivariant) | VA = local model on D |
| 7 | Annulus, Sigma_g | SC^{ch,top}_mod (partially modular); curvature d^2 = kappa*omega_g | Theta_A, genus tower |
| 8 | Drinfeld center | E_2-chiral Gerstenhaber (chiral Deligne-Tamarkin) | Z^{der}_{ch}(A) = C^bullet_{ch}(A,A) |
| 9 | Topologization | E_3-TOPOLOGICAL (Sugawara + conformal vector; Dunn: E_2^top x E_1^top) | Z^{der}_{ch}(A) |

Rung-by-rung pointers (each subsumed by table row; listed for indexing):
- **Rung 1 (Parts I-II, E_1-topological)**: Point/R/[0,1]/[0,∞)/S^1 → OPE seed, E_1-algebra, B(A)=k⊗_A^L k (Koszul duality), one-sided B(A,M) (line ops, branes), cyclic bar HH_*(A) / Z(A) / genus-1 curvature / modular group.
- **Rung 2 (Parts III-IV, E_2-chiral)**: Formal disk / curve X / half-plane H / disk+S^1 / annulus. R-matrix is the E_1→E_2 coherence datum (for E_inf: derived from OPE; for genuine E_1: independent). Z(A)=HH*(A) carries E_2 via Deligne conjecture. E_2 lives on Z(A)/Mod_A, NEVER on A. Quantum groups E_1; Rep(U_q(g)) E_2 in Cat. R-matrix / YBE (Stokes on FM_3(C)) / braided line category / spectral Drinfeld strictification are E_2 phenomena.
- **Rung 3 (Part IV cont., modular)**: M_{g,n} stratified by stable graphs; curved bar d^2 = kappa*omega_g; shadow obstruction tower {F_g}; G/L/C/M. Curved Dunn genus 1: PROVED (twisted Künneth, prop:genus1-twisted-tensor-product). Genus ≥ 2: OPEN (H² obstruction). Modular operad composition/equivariance/unitality PROVED (KZ pentagon + quasi-triangularity + vacuum axiom). Sole gap: composition at generic non-integral level, genus ≥ 1 (Stokes regularity).
- **Rung 4 (Parts V-VI = CLIMAX, E_3)**: X×R (slab), X×[0,1], X×S^1. E_3 = E_2 × E_1 via Dunn (E_2 = holomorphic braided structure on X; new E_1 = transverse R). The climax: 3d quantum gravity = E_3-chiral = derived center of boundary + transverse E_1. CFG (arXiv:2602.12412): filtered E_3 from BV-quantised CS; factorisation homology trace = RT link invariant (perturbative E_3 at genus 0).

### The missing rung: E_1-chiral quantum groups and the modular operad
E_2-to-E_3 step requires:
1. Modular operad governing A_inf-algebras in E_1-chiral algebras (Definition def:modular-operad-ainf-chiral: genus-0 proved = SC × E_1^tr; clutching via B^{ann} + R-matrix monodromy; genus ≥ 2 operadic verification open).
2. Chiral coproduct Δ: A → A⊗A on the E_1-chiral algebra (not visible in shadow tower; EXTERNAL comparison points: Gaiotto-Rapcak-Zhou arXiv:2309.16929 (type A only), Jindal-Kaubrys-Latyntsev arXiv:2603.21707 (ADE quivers only); THIS programme's chiral coproduct is the Drinfeld coproduct via bar-cobar, not CoHA).
3. Curved Dunn additivity (genus 1 PROVED, genus ≥ 2 OPEN).

An E_1-chiral quantum group is: E_1-chiral algebra A + chiral coproduct Δ + R-matrix R(z) + quasi-triangularity + antipode, such that Mod_A is braided monoidal (E_2 in Cat).

### The E_N definition ladder: CHIRAL vs TOPOLOGICAL (LOAD-BEARING — DO NOT DELETE)

CRITICAL: E_N-CHIRAL ≠ E_N-TOPOLOGICAL. Chiral depends on complex structure; topological does not. The conformal vector T(z) (Sugawara) enables TOPOLOGIZATION. Without it: stuck at chiral. With it, at non-critical level: can topologize. All six definitions are in the manuscript (session 2026-04-12):

- **E_1-chiral** (def:e1-chiral-algebra, axioms.tex): E_1-algebra in D-modules on X. Ordered OPE data. Bar complex B^{ord}(A). DONE.
- **E_1-topological** (def:e1-topological-algebra, axioms.tex): E_1-algebra (just associative, no holomorphic dependence). DONE.
- **E_2-chiral** (def:E2-chiral-algebra, spectral-braiding-core.tex): E_2 on Z^{der}_{ch}(A), NOT on A. R-matrix R(z) with spectral parameter. DONE.
- **E_2-topological** (def:E2-topological-algebra, spectral-braiding-core.tex): requires conformal vector to topologize. DONE.
- **E_3-chiral** = E_2-chiral × E_1-top: HT bulk. Holomorphic on X, topological on R. NOT AUTOMATIC from chiral algebra. Requires a 3d HT theory whose boundary is A. KM: proved (holomorphic CS from 6d, Costello-Li/CFG). W-algebras via DS (incl. Virasoro): Costello-Gaiotto provides the 3d HT theory; T_DS = [Q_tot, G'] gap NOW CLOSED (thm:E3-topological-DS, thm:E3-topological-DS-general — improvement always Cartan currents). For chiral algebras without gauge-theoretic origin: quantizing PV model (hard; Khan-Zeng covers ALL freely-generated PVAs with conformal vector, not just gauge-theoretic). Conjectural only for non-freely-generated VAs (Monster).
- **E_3-topological** = E_2-top × E_1-top = full TQFT. Independent of complex structure. Requires BOTH a 3d HT theory AND a conformal vector at non-critical level. This is Chern-Simons (CFG).

Topologization per level:
- E_1: trivial.
- E_2: conformal vector T(z) via Sugawara trivializes complex-structure dependence up to homotopy.
- E_3: E_3-chiral + conformal vector = E_3-topological.

Without conformal vector: stuck at E_3-chiral (SC^{ch,top}, two colours distinct). With conformal vector at non-critical level: E_3-topological. At critical level k=-h^v: Sugawara degenerates, topologization fails, stuck at E_2-chiral = Feigin-Frenkel center.

Stage 9 E_3-TOPOLOGICAL is the POINT OF THE VOLUME. Sugawara at non-critical: T(z) = {Q,G(z)}, so C-translations are Q-exact, two colours of SC^{ch,top} collapse in cohomology.

### SC^{ch,top} as first-class object (GENERIC case)

E_3-topological is a SPECIAL CASE requiring conformal vector; SC^{ch,top} is what MOST chiral algebras carry on their derived center pair. Examples stuck at SC^{ch,top}: critical level KM V_{-h^v}(g), E_1-chiral algebras (Yangians), CY functor outputs lacking conformal vectors. NOTE: Heisenberg H_k (k≠0) and lattice VOAs are NOT stuck — abelian Sugawara T=(1/(2k)):JJ: (c=1), reach E_3-topological via abelian holomorphic CS (same proof as KM).

SC^{ch,top} has five presentations (PENTAGON of equivalences 1↔2↔3↔4↔5↔1 must ALL be proved):
1. **Operadic**: generators (codim-1 boundary strata FM_k(C)×Conf_m(R)), relations (codim-2).
2. **Koszul dual**: (SC^{ch,top})^! = (Lie, Ass, shuffle-mixed); NOT self-dual (Com↔Lie, Ass self-dual); W(SC^{ch,top}) = cofibrant replacement.
3. **Factorization**: Z^{der}_{ch}(A) = E_2-chiral center acting on A via universal brace.
4. **BV/BRST**: Obs(U) = logarithmic SC-algebra; QME = open/closed MC equation.
5. **Convolution**: g^{SC}_T = L_inf convolution from bar cooperad B(SC^{ch,top}).

VOLUME MUST: (1) present SC^{ch,top} concretely (Parts I-IV); (2) prove the pentagon redundantly; (3) for algebras with conformal vector, prove topologization at chain level (Parts V-VI); (4) prove failure at critical level; (5) verify on V_k(g), Virasoro, Heisenberg, W_3.

### Critical strata with dedicated bar chain models (non-obvious specifics)

- **Punctured disk D\* = D\{0}**: Homotopy-equiv to S^1. HOMOLOGY: H^ch_*(D*,A) = HH_*(A). CHAIN: C^ch_*(D*,A) carries full holomorphic/chiral structure (OPE poles, spectral params, E_2 data); C^top_*(S^1,A) carries only topological/cyclic (E_1). **Chain-level D\* vs S^1 IS the E_2-E_1 gap.** Load-bearing for E_1-to-E_2 step.
- **Annulus A_{r1,r2}**: Two E_1 structures (one per boundary circle) → bimodule; B^{ann}(A) computes sewing/propagator; int_{S^1×[0,1]} A = Hochschild bimodule; τ-dependence at chain level, not at homology; pinching → pair of pants → multiplication. **Annulus is the GEOMETRIC HOME of Hochschild.**
- **Nodal curves (strata of Mbar_{g,n})**: Each stable graph Γ — vertices=smooth components, edges=nodes. Bar restricted to stratum = tensor of component bars, sewn at nodes via B^{ann} in thin-annulus limit. **Curvature d^2=kappa*omega_g LIVES on nodal boundary strata; smooth locus has d^2=0.** Genus tower {F_g} computed stratum-by-stratum.
- **Pair of pants (genus-0, 3 circles)** = P^1\{0,1,∞}: **Multiplication cobordism.** Bar chain model = chain-level avatar of chiral product on HH_*.

### Key corrections (2026-04-12)
- B(A) ≠ ∫_R A (that equals A). B(A) = ∫_{[0,1]}^{k,k} A (interval with augmentation boundary).
- Quantum groups E_1; Rep(U_q(g)) E_2 in Cat; E_2 lives on Mod_A/Z(A), NEVER on A.
- Dunn additivity: Z(A) (bulk), NOT A (boundary).
- Chiral coproduct Δ: A → A⊗A is on A itself, NOT the deconcatenation on B(A).
- r-matrix from collision residues = CLASSICAL SHADOW. Full chiral QG needs coproduct + full R(z) + quasi-triangularity + antipode.
- Bar chain models indexed by topologico-combinatoric stratifications with bulk-to-boundary structure, not manifolds.

## Standing Hypotheses

Algebraic framework unconditional. (H1)-(H4) no longer axioms: (H1)-(H2) conditions of physics bridge theorem, (H3) theorem of config space geometry, (H4) recognition theorem (proved). Homotopy-Koszulity of SC^{ch,top}: PROVED (Kontsevich formality + transfer).

## Scope of `/chriss-ginzburg-rectify` (author directive, 2026-04-17)

**When the user invokes `/chriss-ginzburg-rectify` on a chapter or standalone, the ENTIRE file must be analysed, chunk by chunk, linearly progressing from start to finish, with SMALL CHUNK SIZE (50-100 lines).** No abbreviation of the pass. The skill's five-phase programme (global diagnostic, Platonic restructuring, linear reconstitution loop with five gates, parallel re-audit, final convergence) applies to every chunk in file order. A V2-AP40 sweep is a necessary subset of Gate 5 but NOT a substitute for Gates 1-4 (mathematical truth, define-before-use, concept motivation, physical realization) and NOT a substitute for the linear chunk sweep across the whole file. Skipping to "the leak sites" or "the obvious chunks" is a shortcut the directive forbids. The loop discipline is the load-bearing element: every chunk passes all five gates before the cursor advances.

## Independent Verification Protocol (cross-volume, 2026-04-16)

**STANDALONE.** Motivated by the 2026-04-16 Vol III adversarial audit finding `\ClaimStatusProvedHere` theorems backed by tautological tests (engines hardcoded `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` with verified identity `weight := c_0/2` built into the row; "99-test cross-validation" = `Fraction(10,2)==5` against the same table). Failure propagates: tex paraphrase → hardcoded engine target → arithmetic-identity test → CLAUDE.md paraphrase → next session reads CLAUDE.md not .tex. Rules ("always verify", "never hardcode") proved ineffective. Protocol is a mechanical invariant.

### Mechanical invariant
Every test for a ProvedHere theorem declares:
- `derived_from`: canonical names of data/papers/conventions the formula came from.
- `verified_against`: canonical names of independent data/papers/conventions for the expected value.
- One-sentence `disjoint_rationale`.
If `derived_from ∩ verified_against` is nonempty (case/whitespace-insensitive), the test module fails to import. Tautology = audit failure, not silent pass.

### Decorator API (use verbatim)

```python
from compute.lib.independent_verification import independent_verification

@independent_verification(
    claim="thm:phi-k3-explicit",                   # label in .tex
    derived_from=[
        "HKR isomorphism on D^b(Coh(K3))",
        "Hodge diamond of K3",
    ],
    verified_against=[
        "Mukai 1984 lattice rank 24 for H^*(K3, Z)",
        "Classical Betti numbers b_0 + b_2 + b_4 = 24",
    ],
    disjoint_rationale=(
        "HKR reconstructs total_dim via polyvector cohomology on K3; "
        "Mukai/Betti gives the rank as a topological invariant from "
        "the K3 lattice without any HH_* or chiral construction. "
        "Independent derivations."),
)
def test_total_dimension_24():
    ...
```

Decorator registers test, checks disjointness at import, no-op on pass.

### Enforcement
- `make verify-independence` — summary audit
- `make verify-independence-verbose` — lists every uncovered claim

Scrapes `chapters/`, `appendices/`, `notes/`, `working_notes.tex` for `\ClaimStatusProvedHere`; imports test modules; reports ProvedHere count, coverage, tautological decorations (should be 0; fail at import), orphans (labels not actually ProvedHere). Exit 0/2. Coverage % is metric, not gate.

### Three healings when honest decoration fails
1. **Find a disjoint source.** Best (e.g. HKR rank 24 ↔ Mukai rank 24).
2. **Restrict scope.** Replace theorem with proposition qualified by scope; note general case conjectural.
3. **Downgrade status.** Replace `\ClaimStatusProvedHere` with `\ClaimStatusConjectured`.

Audit surfaces the choice, does not choose.

### Protocol for new theorems
Before writing `\ClaimStatusProvedHere`: (1) name independent verification source; (2) if none, restrict or use Conjectured; (3) write test with `@independent_verification(...)` day one; (4) run `make verify-independence` before commit.

### Files (cross-volume, identical code)
- `compute/lib/independent_verification.py` — decorator + registry + disjointness check
- `compute/scripts/audit_independent_verification.py` — lint
- `compute/tests/test_independent_verification_infra.py` — 7-test self-test
- `notes/INDEPENDENT_VERIFICATION.md` — protocol doc

Coverage snapshot (2026-04-16): Vol I 0/2275; Vol II 0/1134; Vol III 2/283. Close through GENUINE independent verification or explicit downgrade, never tautological decoration.

## Vol II-Specific Pitfalls

- B(A) is NOT an SC^{ch,top}-coalgebra (AP165). B(A) is E_1 chiral coassoc coalgebra. SC^{ch,top} emerges in chiral derived center pair (C^bullet_{ch}(A,A), A). See Vol I AP165/B54-B56.
- WHICH Hochschild: ALWAYS chiral C^bullet_{ch}(A,A) via End^{ch}_A with spectral parameters from FM_k(C). NEVER topological HH = RHom_{A^e}(A,A) (gives E_2 center from Deligne, not chiral bulk).
- SC directionality: Open-to-closed EMPTY. Bulk → boundary only.
- PVA is (-1)-shifted: lambda-bracket on H*(A,Q) has shifted parity.
- R-matrix provenance: R(z) from bulk-boundary composition, NOT universal R-matrix (agree on eval locus = DK-0).
- Formality failure at d'=1: NOT a defect; non-vanishing A-inf operations IS curved bar d^2=kappa*omega_1.
- Bulk = derived CENTER of boundary. NOT bulk=boundary. Boundary-linear proved; global triangle conjectural.
- Spectral Drinfeld strictification: PROVED all simple Lie. Frontier: Kac-Moody root mult > 1.
- Self-dual ≠ critical: c*=13 (Koszul) ≠ c_crit=26 (matter-ghost). W_N: c*=alpha_N/2, c_crit=alpha_N. NEVER conflate.
- Pole-order dichotomy: Double poles → class L (formal SC). Quartic → class M (infinite A-inf). DS transports L→M.

## The E_1/E_inf Locality Hierarchy (canonical statement + V2-AP1-24 register)

**Canonical statement (subsumes V2-AP1, V2-AP5-16).** E_1 vs E_inf is about LOCALITY, not poles. E_inf = LOCAL = Sigma_n-equivariant; E_1 = NONLOCAL. OPE poles are compatible with E_inf. Three-tier picture WITHIN E_inf: (i) pole-free (R=tau, e.g. BD "commutative chiral algebra" — STRICT SUBCLASS of E_inf); (ii) VA with poles (R≠tau but DERIVED from local OPE); (iii) genuinely E_1 (R≠tau, independent input). Tiers (i)+(ii) BOTH E_inf. **KM, Virasoro, Heisenberg, W-algebras are ALL E_inf** — poles do not break E_inf. Discriminant E_1 vs E_inf is PROVENANCE of R(z), not its value. BD do NOT study E_1; E_1-chiral algebra is a NEW concept of THIS manuscript.

**Bar complex variants (V2-AP3, V2-AP4).** Three bars: B^FG (zeroth pole only) ≠ B^Sigma (all poles + coinvariants) ≠ B^ord (all poles + ordering). Maps: B^ord → B^Sigma (coinvariants), gr(B^Sigma) → B^FG (filtration). Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.

**Heisenberg (V2-AP7).** R-matrix = exp(k·ℏ/z), NOT trivial. Collision residue k/z. Monodromy exp(-2πik).

**Trigger phrases to NEVER say** (V2-AP5, V2-AP8, V2-AP9, V2-AP10, V2-AP11, V2-AP13, V2-AP14, V2-AP15):
| # | Forbidden | Why |
|---|-----------|-----|
| V2-AP5 | "E_inf = no OPE poles" | BD commutative is strict subclass |
| V2-AP8 | "E_inf (= BD commutative = no poles)" | Restrictive parenthetical narrows term |
| V2-AP9 | "VA is not E_inf" | KM/Vir/Heis/W are ALL E_inf |
| V2-AP10 | "E_inf implies R(z)=tau" | Only for POLE-FREE E_inf |
| V2-AP11 | Equating E_inf with BD "commutative" | BD commutative = pole-free subclass |
| V2-AP13 | Trusting agent "VAs are not E_inf" | Exact error caused cascading damage |
| V2-AP14 | Oscillating conventions within session | — |
| V2-AP15 | Editing E_1/E_inf language without author confirmation | — |

**Other process guards.** V2-AP17: never revert file on false premise (surgical only). V2-AP18: author's explicit statements override agent literature searches. V2-AP19: never batch-propagate unverified corrections — ONE edit, verify, THEN propagate. V2-AP20: never add "in the sense of [reference]" without verification.

**Distinct facts (kept separately):**
- **V2-AP21**: PVA ≠ P_inf-chiral. PVA = classical shadow (descend to cohomology). P_inf = homotopy intermediate. Opposite directions.
- **V2-AP22**: Full hierarchy: Comm assoc < PVA < E_inf-chiral < P_inf-chiral < E_1-chiral. Bar/Koszul at E_inf and E_1 levels.
- **V2-AP23**: Chromatic: classical theory is height 0. L_{K(n)}(B(A))=0 for n≥1. Pole order ≠ chromatic height.
- **V2-AP24**: S-transform (closed, complex structure) ≠ Wick rotation of R (open, E_1 ordering). Different algebraic data.

### Empirical V2-APs (from error archaeology)

- **V2-AP25**: Complex-analytic sign. Im(f)=(f-fbar)/(2i); ∂bar Im(f) = (i/2)·∂bar(fbar), NOT 1/(2i). Identity -1/(2i)=i/2 is common confusion. Verify at EACH propagation site.
- **V2-AP26**: NEVER hardcode Part/chapter numbers — always `\ref{part:...}`. 24+ stale refs after 10→7 Part restructuring.
- **V2-AP27**: Duplicated content across files FORBIDDEN. Use `\input{}`/`\ref{}`, never copy-paste theorem envs.
- **V2-AP28**: Test expected values from 2+ independent sources with documented derivation. Engine+test from same mental model share error. **lambda_3=1/82944 was WRONG (correct: 31/967680)** because both used same faulty computation.
- **V2-AP29**: AI slop cleanup mandatory post-gen: grep for moreover, additionally, notably, crucially, remarkably, "it is worth noting", em dashes, "We now", passive "can be shown." 3 cleanup commits prove aspirational instructions insufficient.
- **V2-AP30**: After architecture restructuring: `grep -rn "Part~[IVXL]" chapters/`; also `grep -rn "\\ref{part:"` to verify targets.
- **V2-AP31**: AP4 at write time. Before `\begin{proof}`, verify preceding env is theorem/prop/lemma with ProvedHere. Conjecture → `\begin{remark}[Evidence]`. 25-instance fix.
- **V2-AP32**: Standalone-document artifact leak. Chapter files `\input{}`'d into main.tex MUST NOT contain `\title{}`, `\begin{abstract}`, `\tableofcontents`, `\date{}`, `\author{}`. Silent artifacts.
- **V2-AP33**: RECTIFICATION-FLAG must NOT become permanent. Zero tolerance at session end.
- **V2-AP34**: Divided-power convention in λ-brackets. Vol II uses {T_λ T} = (c/12)·λ^3 (divided power). OPE mode T_{(3)}T = c/2 → (c/2)/3! = c/12. EVERY λ-bracket MUST use divided powers. `grep c/2.*lambda^3` — if found, almost certainly wrong (should be c/12). **W3: c/3·λ^5 wrong, correct c/360.**
- **V2-AP35**: Unresolved logical connectives. After correcting a formula, audit ALL "therefore"/"hence"/"it follows" within 5 lines. Dangling connective = non-sequitur worse than the original error.
- **V2-AP36**: Terminology rename atomicity. Enumerate ALL variant forms; grep all 3 volumes incl. compute/, audit/, *.md; complete replacements in SINGLE commit; verify zero residual. "shadow Postnikov tower" → "shadow obstruction tower" needed 5 commits (114+27+4+1+1 files).
- **V2-AP37**: Arakelov form normalisation. Canonical: omega_1 = i/(2 Im(tau)) dz∧dz-bar (integral=1). Arakelov kernel: omega_Ar = -(π/Im(tau)) dz∧dz-bar (integral=-1). **omega_1 = -omega_Ar/(2π)**. Same error fixed THREE times. Verify fundamental-domain integral before writing.
- **V2-AP38**: Phantom label retirement. After chapter migration, track each phantom with retirement path. 366 phantoms across 2 commits after Vol I → Vol II migration.
- **V2-AP39**: Macro portability. After migrating chapter Vol I → Vol II: compile, grep for "Undefined control sequence", add `\providecommand` for each. 7 macros needed adding across 2 commits. Never assume Vol I macros available.
- **V2-AP40**: **NO ANTIPATTERN TAGS OR METADATA LEAKAGE INTO THE MANUSCRIPT OR STANDALONE PAPERS PROPER.** (Author directive, 2026-04-17.) Author-side bookkeeping tokens MUST NOT appear in any `.tex` file that compiles into the monograph PDF or any standalone paper PDF. This covers, at minimum:
  - **AP identifiers**: `AP\d+`, `V2-AP\d+`, `AP-CY\d+`, `AP-OC`, `AP-RMATRIX`, `AP-SC-NOT-SELFDUAL`, `AP-SC-BAR`, named APs (`MP1`, `HZ-\d+`, etc.).
  - **FM identifiers**: `FM\d+` (EXCEPT the bibkey `\cite{FM94}` = Fulton-MacPherson 1994, and the math-object subscript `$\FM_n(\C)$`).
  - **Session codes**: `C\d+:`, `B\d+:`, `C4`, `B18`, `C9`, `HZ-\d+`, `RS-\d+`, `W\d+`, `WAVE-\d+`, `AAP`.
  - **Commit hashes**: `commit \texttt{<sha>}`, naked 7-40 hex SHAs in prose.
  - **Meta-stamps**: `Beilinson-rectified`, `HEAL-SWEEP`, `HEAL-MODE`, `UPGRADE-SWEEP`, `Platonic reconstitution` (as session event, not as a theorem), `PLATONIC ANCHOR BLOCK`, `(cached confusion \#\d+)`, `, NEW` tags on Part/Section headers.
  - **Working-note labels**: `working note \texttt{...}` references to author-side drafts.
  - **Session dates in body prose**: `2026-04-\d\d` or similar unless quoting a published paper's year.
  - **Visible-label leaks**: `\texttt{(thm|prop|lem|def|cor|rem|conj):...}` where `\ref{...}` or `\cref{...}` was intended.
  - **Error-ledger structures inside the manuscript**: `\begin{remark}[AP###: ...]`, `\label{rem:AP###-...}`, `\index{AP###!...}`, `\hyperref[AP##]{AP##}`, `\section{Anti-pattern register: ...}`, `\begin{convention}[AP###: ...]`, or enumerated `\item \textbf{FM###.}` catalogue pages. Sections, labels, indices, hyperrefs, and conventions must not be named after ledger tokens.

  **Scope**: every `.tex` file under `chapters/`, every standalone in `standalone/`, every frontier/preface/appendix file that is `\input{}`-chained from `main.tex` or is itself a buildable document. Excluded: `.md` files (CLAUDE.md, README, AGENTS.md, `notes/first_principles_cache_comprehensive.md`, `notes/`), files under `compute/`/`audit/`, and `working_notes.tex` (author-side draft not shipped).

  **The error ledger** (this file, `CLAUDE.md`, and `notes/first_principles_cache_comprehensive.md`) is where AP/FM tokens live. `.tex` prose is mathematics. A reader of the compiled PDF should never encounter "AP165", "FM81", or `commit \texttt{a5640de}`.

  **Mechanical detection grep** (run against `chapters/` and `standalone/` before every `.tex` commit):
  ```
  grep -nE 'AP[0-9]+|FM[0-9]+|\(AP-CY[0-9]+|commit \\texttt|cached confusion|Beilinson-rectified|working note|RS-[0-9]|HZ-[0-9]|\bC[0-9]+:|\bB[0-9]+:|AP-RMATRIX|AP-OC|HEAL-(SWEEP|MODE)|UPGRADE-SWEEP|PLATONIC ANCHOR|WAVE-[0-9]+' chapters/ standalone/
  ```
  Also grep for `\\texttt\{(thm|prop|lem|def|cor|rem|conj):` (visible-label leaks) and `2026-0[1-9]-[0-3][0-9]` (session dates in body, excluding `\cite` contexts).

  **Counter at write time**: before committing a chunk, run the greps above. If any match that is not a bib citation (`\cite{FM94}`) or a math-mode subscript (`$\FM_k$`), restate the content as a declarative mathematical sentence carrying the substance of the ledger token without the token itself. "The correct expression is $H_N - 1$, not $H_{N-1}$, since $H_{N-1} \ne H_N - 1$ in general" beats "(C4: at $N=2$, $H_2-1=1/2$ recovers $\kappa=c/2$, not $H_{N-1}$; AP136)". "The curvature is Cartan-current $Q_{\mathrm{CS}}$-exact in the 3d bulk regardless of the nilpotent orbit (\\ref{thm:E3-topological-DS-general})" beats "(FM57; AP143)". The reader should never need to consult the error ledger to parse a sentence.

  **Session evidence**: Vol II preface chunks 41-57 removed 30+ leaks (2026-04-17). Vol II introduction linear sweep (chunks 58-80) removed 19 more and surfaced a Gate-1 math finding (see V2-AP41 below). A comprehensive audit 2026-04-17 identified ~530 additional leaks across 58 chapter/connection/standalone files — a systemic registry-leak pattern from earlier error-cataloguing work that embedded AP/FM tokens into theorem decorators, section titles, index entries, and hyperrefs. All require surgical rectification. Until that sweep completes, V2-AP40 remains the single most cross-file-violated invariant in the manuscript proper.

  **Subclause V2-AP40a: bibkey-named-after-ledger-token.** A subtle form of V2-AP40 leaks is when a `.bib` entry's key is itself a ledger token, e.g. `\cite{Vol2-FM81-platonic}` — the compiled bibliography and every in-text `\cite{...}` then surface `FM81` to the reader. Forbidden. `.bib` keys must be content-named: `Vol2-fractional-ghost-platonic` or similar. Session evidence: `bp_chain_level_strict_platonic.tex` carried `\cite{Vol2-FM81-platonic}` at 10+ call sites (2026-04-17 audit). Counter: atomic rename of the bib entry across `.tex` + `.bib`, single commit.

  **Subclause V2-AP40b: label-named-after-ledger-token.** A `\label{...}` whose identifier is an AP/FM token — e.g. `\label{rem:AP172-A-koszul-SC-not-SC}`, `\label{cor:FM134-healed}`, `\label{rem:chapter-retracted-2026-04-17}` — propagates the token through the PDF's link graph and through every `\ref{...}` that targets it. Forbidden. Labels must be content-named. Counter: rename both the `\label{}` and every `\ref{}` atomically; verify compilation. Session evidence (2026-04-17 audit): ~25 label-and-index AP/FM leaks across `unified_chiral_quantum_group.tex`, `y_algebras.tex`, `topologization_class_m_original_complex_platonic.tex`, `foundations.tex`, `axioms.tex`.

  **Subclause V2-AP40c: index-entry or hyperref anchor named after ledger-token.** `\index{AP###!...}` and `\hyperref[AP##]{AP##}` lift the token into the compiled index and the in-text navigation. Forbidden. Session evidence: `e_infinity_topologization.tex` carried `\index{FM47!healed}`, `\index{FM48!healed}`, `\index{FM81!healed}`, `\index{FM82!healed}`, `\index{FM215!resolved}` (2026-04-17 audit). `examples-complete-proved.tex` carried `\hyperref[AP67]{AP67}`, `\hyperref[FM106]{FM106}`, `\hyperref[FM120]{FM120}`, `\hyperref[FM132]{FM132}`, `\hyperref[FM105]{FM105}` through `\hyperref[FM110]{FM110}` (worst class of leak: reader clicks on the index/hyperref and lands on the AP/FM anchor target in the manuscript). Counter: delete index entries and hyperrefs outright; rephrase surrounding prose to state the mathematical content directly.

  **Subclause V2-AP40d: theorem-environment title named after ledger-token.** `\begin{remark}[AP172: Koszul dual is an SCchtop^! -algebra]`, `\begin{convention}[AP159: layers ...]`, `\begin{remark}[FM179 discipline: coideal vs sub-dg-module]`, and the five-way pattern `\section{Anti-pattern register: AP171, AP172, AP174, slab-bimodule}` are the structural analogue: ledger tokens as environment titles or section titles. The compiled PDF's table of contents and every theorem-environment header displays `AP###` or `FM###` to the reader. Forbidden. Counter: retitle each environment by content ("Koszul-dual operadic scope", "Level prefix on the RTT kernel", "Coideal vs sub-dg-module distinction"), delete Anti-pattern register sections. Session evidence: 20+ instances across `unified_chiral_quantum_group.tex`, `shifted_rtt_duality_orthogonal_coideals.tex`, `line-operators.tex`, `grt_parametrized_seven_faces.tex`, `dnp_identification_master.tex`, `foundations.tex`, `equivalence.tex`, `dg_shifted_factorization_bridge.tex`, `ordered_associative_chiral_kd_core.tex`, `bar-cobar-review.tex`, `typeA_baxter_rees_theta.tex`, `thqg_gravitational_yangian.tex` (2026-04-17 audit).

  **Subclause V2-AP40e: monospaced filename or label as cross-chapter pointer.** Using `\texttt{e_infinity_topologization.tex}`, `\textsf{unified_chiral_quantum_group.tex}`, `\texttt{chap:universal-conductor}`, or similar `\texttt{...}`/`\textsf{...}` of a filesystem basename or an undeclared chapter anchor, as a reader-facing pointer to content living elsewhere in the monograph. The compiled PDF then displays source-tree filenames in monospace, leaking author-side file organisation into the published object and breaking the reader's parse (they cannot click a `.tex` filename, and the target of the pointer is not a proper `\label`). Forbidden whenever the target admits a proper `\label{...}`. Counter: replace `\texttt{e_infinity_topologization.tex}` by `Theorem~\ref{thm:e-infinity-topologization-ladder}` (anchoring on the actual label inside that chapter), and replace `\texttt{chap:universal-conductor}` by "the Volume~I universal-conductor chapter" or, when the chapter does carry a real `\label{chap:universal-conductor}`, by `\cref{chap:universal-conductor}`. Session evidence: `grt_parametrized_seven_faces.tex` (2026-04-17 sweep, removed 7 monospace-filename pointers).

  **Subclause V2-AP40f: math-mode label leak.** A rarer, more insidious variant of V2-AP40e: a `\label{...}` identifier pasted into math mode with manual spacing, e.g.\ `$\mathrm{conj}{:}\mathrm{periodic\text{-}cdg}$`, or `$\mathrm{thm}{:}\mathrm{universal\text{-}holography}$`. The leak is dressed up as mathematics (upright-roman text with a tiny `{:}` colon and `\text{-}` hyphen) but the tokens `conj`/`thm`/`lem` and the identifier body are source-code organisational labels, not mathematical symbols. Extra hazardous because it bypasses the standard `\texttt{...}` detection grep. Forbidden: the target either has a real `\label{...}` (use `\ref{...}`) or it does not (use prose). Counter: replace `$\mathrm{conj}{:}\mathrm{periodic\text{-}cdg}$ (Vol~II frontier \#3) asserts \dots` by `the periodic-CDG conjecture asserts \dots` or, when a pointer is needed, `the periodic-CDG conjecture (Remark~\ref{rem:periodic-cdg-mechanism}) asserts \dots`. Session evidence: `hochschild.tex:997` (2026-04-17 sweep) carried one such math-mode label pointer that survived the five-pattern grep and surfaced only when the prose was re-read for coherence.

- **V2-AP41**: Internal theorem-statement-vs-proof formula inconsistency. A main theorem states one formula in its hypothesis or case split, but the immediate proof-detail paragraph or a companion remark cites a different formula that diverges at boundary cases. Example (Vol II introduction, chunk 18, 2026-04-17): the Programme Climax theorem stated Arnold coupling $\beta_{W_N} = (N+1)(N+2)/2$ for principal $W_N$ in the Banach-completion case split, then immediately afterwards the Stirling-dominance pillar proof cited the proved closed form $\beta_N = 12(H_N - 1)$ (`thm:beta-N-closed-form-proved-all-N`). The two expressions agree at $N = 2$ (both 6) and $N = 3$ (both 10) but diverge at $N \ge 4$: $(5)(6)/2 = 15$ vs $12(H_4 - 1) = 12 \cdot 13/12 = 13$. The incorrect value would widen the Banach radius $\rho_* = |c|/\beta_{\cA}$ and forgive spurious convergence. The naive candidate is the Fateev-Lukyanov asymptotic; the proved closed form is the harmonic sum. First-principles check: compute both at $N = 4$ and compare.
  **Counter at write time**: when a theorem's case-split table cites a formula that admits a closed form elsewhere in the chapter, either use the closed form uniformly or scope-split ("agrees through $N = 3$; overestimates at $N \ge 4$ where the closed form is the correct value"). The theorem statement must be consistent with the proof it governs. Grep heuristic: after any commit that touches a β, κ, c, or structural-constant table, grep the surrounding chapter for the same symbol and verify per-row agreement at the first boundary case ($N = 4$, $d = 3$, $g = 2$, etc.).

### Structural/Scope APs (AP150-AP158)

- **AP150**: Agent confabulation of mathematical structures — agents stitch disparate results at different categorical levels. Counter: verify each arrow against .tex; if any arrow conjectural, the whole structure is. [Echoes AP-CY related confabulation patterns; see unified merged table below for FM40-FM57 restatement.]
- **AP151**: Convention clash within single file. Two ℏ definitions cascade into wrong q (real instead of root of unity). Counter: grep all ℏ definitions after any formula. [= FM24 — see below.]
- **AP152**: "Ordered" ambiguity (labeled-on-curve vs time-ordered-on-R). Bar complex is mixed (holomorphic diff from OPE on C + topological coprod from deconcat along R). Counter: specify which "ordered."
- **AP153**: E_3 scope inflation. HDC route: E_3 only for E_inf (B-bar^Sigma must exist); E_1 gets only E_2. Counter: specify E_inf vs E_1.
- **AP154**: Two E_3 structures. (a) Algebraic E_3: HDC on E_2 bar coalgebra, no Sugawara. (b) Topological E_3: Sugawara required. Identification as families over ℏ·H^3(g)[[ℏ]] is CONJECTURAL (conj:e3-identification). Topological (b): PROVED affine KM at non-critical (thm:topologization); CONJECTURAL general chiral with conformal (conj:topologization-general, conj:E3-topological-climax). Cohomological proof; for class M, chain-level E_3 may fail. Counter: specify which E_3 and whether Sugawara.
- **AP155**: "New invariant" overclaiming. Framework recovers KZB (Bernard 1988), elliptic R (Felder 1994), Verlinde (BD). Novelty is ARCHITECTURAL not COMPUTATIONAL. Counter: check Bernard/Felder/Etingof-Varchenko/Calaque-Enriquez-Etingof.
- **AP156**: Weierstrass wp_1 convention. (a) θ_1'/θ_1 — periodic under z→z+1, quasi-per z→z+τ with increment -2πi. (b) ζ_τ = (a) + 2η_1·z — quasi-per under BOTH. DIFFERENT monodromy. Always specify.
- **AP157**: Degeneration-dependent "invariants." Separating degeneration of genus-2 contains ZERO genuinely genus-2 info (everything determined by genus-0 S-matrix + genus-1 R-matrix eigenvalues); non-separating carries new data. Counter: specify degeneration type + whether independence proved.
- **AP158**: Shallow correction without first-principles investigation **[= AP-CY61 in Vol III, AP186 in Vol I — ONE canonical statement]**. When a claim is challenged, do NOT swap labels ("averaging"→"right adjoint"). Investigate first principles: (1) what claim gets RIGHT (ghost of true theorem), (2) what it gets WRONG (precise conflation), (3) correct statement. Examples: "categorified averaging" wrong but factorization E_1 →^Z E_2 →^{Sym} E_inf is real; "CoHA = bar complex" wrong but coincidence = Schiffmann-Vasserot CoHA = Y^+; "Omega-background is the physical face" true for toric, false general CY (two independent E_1 mechanisms: operadic vs equivariant). Counter: before any correction, write the first-principles analysis. If you cannot state the correct theorem, you do not understand the error.

## Unified Error Catalogue (FM + related APs, 2026-04-12 session, 55+ agents)

FM24 base fact: B-cycle i^2 error — q = e^{2·πi·πi/(k+2)} is **real (e^{-2π²/(k+2)}), not root of unity**; propagates silently because q still "looks like" a parameter. Counter: substitute a specific integer k, verify |q|=1. [= AP151 = Vol I FM24.]

Merged table (FM40-FM57 ↔ AP150-AP157, Vol II pitfalls on coproduct conflation):

| ID(s) | Wrong claim | Correct relationship | Counter |
|-------|-------------|---------------------|---------|
| FM40 | Dunn on A ("E_1⊗E_1=E_2") | Dunn applies to Z(A) (bulk) or Mod_A, NEVER to A | Before any Dunn claim, verify target is Z(A) or Mod_A |
| FM41 | R-matrix promotes A from E_1 to E_2 | R-matrix makes Mod_A braided (E_2 in Cat). A stays E_1. U_q(g) E_1; Rep(U_q(g)) E_2 in Cat | E_2 lives one categorical level up from A |
| FM42 | YBE = A_inf associativity | YBE = COMPATIBILITY of two E_1 structures (braiding coherence). A_inf = coherence of SINGLE E_1 | Separate single-E_1 associativity from pair compatibility |
| FM43 | B(A) = ∫_R A | ∫_R A = A (trivial). B(A) = k⊗_A^L k = ∫_{[0,1]}^{k,k} A | Factorisation homology of contractible bdryless mfd = algebra itself |
| FM44 | "Bar complex = chain model for factorisation cohomology" | B(A) is a factorisation COALGEBRA; chiral homology = derived global sections (separate op). Bar : chiral homology :: sheaf : cohomology | Never conflate local (coalg) with global (cohom) |
| FM45, Vol II pitfall on coproduct | Deconcatenation = chiral coproduct | Deconcat on B(A) is STRUCTURAL (exists for any bar). Chiral Δ: A→A⊗A is independent Hopf-type structure on A | Specify WHICH coproduct and on WHICH object |
| FM46 | r-matrix sufficient for quantum group | r-matrix = classical shadow. Full QG needs Δ + full R(z) + quasi-triangularity + antipode. Δ NOT visible in shadow tower | "r-matrix necessary but not sufficient" |
| FM47 | E_inf → E_3-chiral automatic | E_2 on Z(A) automatic (Deligne). E_3-chiral needs 3d HT theory. KM proved; general VAs: quantizing PV model (hard) | Nothing beyond E_2 on Z(A) is automatic |
| FM48 | E_3-top from E_inf alone | Conformal vector is ADDITIONAL structure; E_3-top needs BOTH 3d HT theory AND conformal vector at non-critical | E_3-top needs two independent inputs |
| **FM49** | Y_ℏ → Y_z^ℏ rename (531 occurrences) | **Algebra Y_ℏ(g) does NOT depend on z. z lives on Δ_z, R(z), T(z), ev_z (structures ON the algebra, not algebra itself). Reverted.** | NEVER put spectral parameter in algebra symbol |
| FM50 | Ordered config spaces = geometric R⊂X | E_1 ordering is ALGEBRAIC (operations depend on sequence). Does NOT require embedding R into X | E_1 operadic/algebraic, not geometric |
| FM51 | "Emergent 3rd dimension" from bar degree | Bar degree is a grading. E_1 needs operations, coherences, A_inf | Grading ≠ operadic structure |
| FM52 | Within-surface SC = holographic bulk-boundary | SC governs within-surface structure (R⊂C restriction). Holography goes through derived center (circle/Hochschild) | SC within-surface; holography via Hochschild |
| FM53 | Two "independent" E_1 structures | They are Koszul dual via Hom: C*(A,A) = Hom(B(A),A). A_inf-coalg on B(A) and A_inf-alg on C*(A,A) determine each other | Koszul dual, not independent |
| FM54 | Spectral R(z) = categorical braiding | Spectral R(z) = family with parameter z; E_2 braiding = single nat transform. Relationship in D-module enriched setting needs proof | Spectral ≠ categorical — needs theorem |
| FM55 | RT invariants = unordered E_1 chiral homology | RT = E_inf factorisation homology (CFG's E_3 trace on BV-quantised CS) | RT = E_inf fact homology trace |
| FM56 | "Symmetric monoidal category of chiral algebras" | Chiral algebras form PSEUDO-TENSOR (BD), NOT symmetric monoidal. Correct ambient: sym mon dg cat of D-modules on X | Say "D-modules on X" / "factorisation algebras on X" |
| FM57 | Costello-Gaiotto does not yet provide 3d HT for Virasoro (manuscript "quantizing PV is hard") | UPDATED 2026-04-12: T_DS = [Q_tot,G'] gap CLOSED (thm:E3-topological-DS). Improvement always Cartan currents (thm:E3-topological-DS-general) | — |

### Meta-Patterns (error-catalogue abstractions)
- **MP1 CATEGORICAL LEVEL CHECK**: before any E_n/Dunn claim, verify level (Algebra E_1 / Mod_A E_2 in Cat / Center E_2).
- **MP2 AUTOMATIC vs REQUIRES CONSTRUCTION**: E_2 on Z(A) automatic (Deligne); above E_2 needs specific construction. Never say "automatic" above E_2.
- **MP3 DISTINGUISH SIMILAR OBJECTS**: deconcat vs chiral coproduct; spectral vs categorical braiding; algebraic vs geometric ordering.
- **MP4 NOTATION CHANGES NEED JUSTIFICATION**: before bulk notation change, verify (a) mathematically correct, (b) literature-consistent, (c) no conflict. **Y_z^ℏ disaster: 531 changes, wrong, reverted.**
- **MP5 GRADING ≠ OPERADIC STRUCTURE**: filtration/grading is Z-indexed decomposition; E_n needs config-space operations.
- **MP6 SINGLE vs PAIR**: verify property is intrinsic to ONE structure or governs TWO. YBE = pair. A_inf = single. Deconcat = single coalg. Chiral Δ requires two copies.
- **MP7 STATUS-TAG IS THE INVARIANT; PROSE IS NARRATION**. Before any theorem/proof/remark body says "is", "equals", "proved", the `\ClaimStatus` tag must already exist and match. Tag governs prose; prose does not upgrade the tag. Prevents scope-inflation cluster: FM75, FM79, FM80, FM81, FM82, FM108, FM185, FM186, FM208, FM214, FM215, FM222.
- **MP8 LABEL IS A SERIALIZATION, NOT A CONTAINER**. Each `\label{...}` points to ONE canonical statement with ONE proof. Overloaded labels (Thm H dual-binding), dual-labeled theorems across volumes with different content (thm:complete-strictification-v1 vs thm:complete-strictification), labels named after ledger tokens (`rem:AP172-...`), phantom labels cited 3+ times with 0 `.tex` hits — all four are forms of one container/pointer conflation. Prevents FM78, FM87, FM93, FM111, FM155, FM173, FM213, FM247, V2-AP40b-c subclause set.
- **MP9 METADATA FILES NEVER SPEAK FOR THEMSELVES**. CLAUDE.md / AGENTS.md / ROADMAP_85_TO_100.md / README.md advertise status but NEVER define it; ground truth is `.tex` + `make verify-independence`. Any metadata↔tex drift is a metadata bug (fix the metadata), unless the `.tex` carries an explicit downgrade. Before relying on a CLAUDE.md bridge-table row, grep the `.tex` for (a) `\ClaimStatus` tag, (b) `\begin{theorem}` environment, (c) actual `\begin{proof}` body. Prevents FM87, FM111, FM126, FM213, FM224 metadata drift cluster.
- **MP10 HEAL BEFORE DOWNGRADE, ALWAYS**. When a claim is challenged, the first three instincts are: (1) find a disjoint verification source; (2) rewrite in the stronger honest form; (3) supply the missing construction / lemma / citation. Only if all three fail does "Downgrade to Conjectured" enter the option space. Technical malpractice (wrong citation, missing lemma, ambient mis-specification, circular proof) is grounds for FIXING the proof, not weakening the claim. HEAL-SWEEP (2026-04-16) inverted ~60 attack-mode "Counter:" fields from downgrade-first to heal-first; this MP institutionalizes the reflex. See Vol II CLAUDE.md "HEAL-MODE DIRECTIVE" + "HEAL-SWEEP" + "UPGRADE-SWEEP" sections.
- **MP11 SCOPE QUALIFIER IS PART OF THE STATEMENT, NOT A RESCUE CLAUSE**. Every universal quantifier ("all W", "every genus", "any simple g") carries its exclusion list IN the theorem statement. First-class: "On the non-critical non-resonant locus with κ ≠ 0, for freely-generated PVAs of classes G, L, C, the functor Φ_hol is ...". Second-class: "... for all chiral algebras A. (Remark: subject to non-critical level, non-resonant, κ ≠ 0, freely-generated, class ≠ M.)" The remark-form downgrades prose reliability because readers take statements at face value. Prevents FM75-82 cluster, FM108, FM186, FM214, FM215.
- **MP12 CROSS-VOLUME CITATION GATE**. Before any `\ref{...}` to a Vol I/II/III label: grep-verify the label exists in the target volume. Before any `\cite{...}`: grep-verify the bib entry exists and its key is content-named (not a ledger token, V2-AP40a). Before any "see Vol X Part Y" in prose: verify the current Part number matches the restructuring state. Three-volume grep is the invariant; declaring a fix done after correcting only the primary site creates a distributed inconsistency. Prevents FM87, FM157 (Liv06 × 7 files), FM207 (fabricated Vol I citation), FM213 (phantom file), V2-AP26, V2-AP30, V2-AP38.
- **MP13 INDEPENDENT VERIFICATION DECORATOR AT WRITE TIME**. Before writing `\ClaimStatusProvedHere` for any theorem, IMMEDIATELY install `@independent_verification(claim="thm:...", derived_from=[...], verified_against=[...], disjoint_rationale="...")` in the test suite. `disjoint_rationale` explains why the two derivation paths cannot share a common error. No ProvedHere without decorator. Pre-existing ProvedHere theorems grandfathered; campaign ongoing. Current snapshot (2026-04-16): Vol I 0/2275, Vol II 0/1134, Vol III 2/283; target 100%. Prevents FM224-229, FM237, V2-AP28 tautology-in-test.
- **MP14 CHAIN-LEVEL VS COHOMOLOGY VS ∞-CATEGORICAL DISTINCTION IS LOAD-BEARING**. Three distinct notions of "equivalent": (a) chain-level quasi-iso on a canonical model; (b) quasi-iso of cohomology; (c) ∞-categorical equivalence. Every claim must specify which. "Equal" / "is" / "≃" unqualified is forbidden. "Chain-level" and "rational" collapse under Kontsevich formality but NOT always; "algebraic E_3" and "topological E_3" are two DIFFERENT theorems; "chiral Hochschild" has three models (geometric FM, algebraic bar/operadic, Gel'fand-Fuchs) that agree only on the logarithmic locus. Prevents FM54, FM60, FM91, FM92, FM126 class M chain-level, AP-CY6, AP-CY11, AP-CY14, AP-CY33, AP-CY62-67 cluster.
- **MP15 NARRATION ≠ CONSTRUCTION**. "The R-matrix acts as a braiding" without explicit σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)} formula is narration, not construction. "Koszul dual gives the Yangian" without explicit isomorphism Y(g)^! ≃ Y(g^∨)^{ℏ → -ℏ r_g} (Finkelberg-Tsymbaliuk, Frenkel-Hernandez) is narration. "Chiral higher Deligne is proved" without writing down the E_3 action on Z^{der}_{ch} is narration. Every ProvedHere carries a construction / formula / proof body, never a declarative sentence. Prevents FM155-156, FM240, FM246, FM254, FM256, FM257, AP-CY57.
- **MP16 DOWNSTREAM PROPAGATION ATOMIC WITH FIX**. After correcting any formula, label, scope qualifier, or citation: IMMEDIATELY three-volume grep all variant forms (`grep -rn "..."` across `chapters/`, `appendices/`, `notes/`, `compute/`, `audit/`, `*.md` as appropriate per V2-AP40 scope); batch propagation in a SINGLE commit; verify zero residual. Declaring a fix done after correcting only the primary site creates distributed inconsistency. The propagation-batch discipline is the load-bearing element. Prevents V2-AP19, V2-AP26, V2-AP36, V2-AP38, FM157 (Liv06 × 7 files, 5 commits of churn), FM207 (fabricated citation survived prior correction pass), V2-AP40 audit cluster (530+ leaks).
- **MP17 DUAL-CONVENTION CO-EXISTENCE REQUIRES EXPLICIT LABELING EVERY APPEARANCE**. When two normalizations for the same object co-exist — omega_1 = i/(2 Im τ) dz∧dz-bar (integral = +1) vs omega_Ar = -(π/Im τ) dz∧dz-bar (integral = -1); 13-c Koszul involution vs 26-c matter-ghost critical central charge; PT level vs Yangian level k vs (k+h^v); kappa vs kappa_ch vs kappa_BKM vs kappa_cat vs kappa_fiber; `∼` (asymptotic/OPE leading order) vs `=` (formal power series equality) — EVERY use must subscript or qualify. Bare occurrences that "look fine" in isolation are exactly where the error plants and propagates. Grep bare symbols before every commit. Prevents V2-AP37 (omega_1 vs omega_Ar, same error fixed 3 times), FM99 (Ω_tr vs Ω Casimir rescaling), FM115 (FF duality nonlinear vs operadic linear scalar flip), FM119 (κ(K3) subscript clash), FM253 (13-c vs 26-c conflation), AP113 (bare kappa forbidden Vol III), AP126/AP141 (level-stripped r-matrix, 42+ instances), AP156 (wp_1 convention), and the entire AP113+AP126+AP141 "forty-plus-instance" class.
- **MP18 CIRCULAR SELF-CONSISTENCY ≠ THEOREM TEST**. A test that reads the same dictionary the engine reads, then asserts their consistency, is a dictionary self-check — regardless of how authoritative the docstring citation sounds. The Vol III `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` with verified identity `weight := c_0/2` built into the row, then 99-test cross-validation `Fraction(10,2) == 5` against the same table, is the load-bearing counter-example: the engine, the test, and the docstring share one mental model; the "independent verification" is tautology. Every ProvedHere test must have genuinely disjoint `derived_from` / `verified_against` sources documented in the `@independent_verification` decorator; `disjoint_rationale` explains why two paths cannot share a common error. Prevents FM225, FM226, FM228, FM237, V2-AP28 (lambda_3 = 1/82944 was WRONG because engine+test used same faulty computation), AP-CY49 tautology-in-test cluster.
- **MP19 FORBIDDEN-TRIGGER-PHRASE LIST MUST BE AUTO-GREPPED**. Scope inflation enters through trigger phrases that look innocuous in isolation but collectively encode scope violations: "VA is not E_inf", "E_inf = no OPE poles", "automatic" (used above E_2), "only language", "complete" (used for non-exhaustive enumeration), "fourteen equivalent" (for scoped biconditionals), "IS the" (for boundary-linear scoped equalities), "proves", "every", "all W", "every genus", "exactly", "uniquely". Maintain the forbidden list as a pre-commit grep; each occurrence must be justified by local scope or rephrased. The forbidden-list discipline is mechanical and prevents authorial drift through prose. Prevents V2-AP5, V2-AP8-V2-AP15 cluster (E_inf vs E_1 locality hierarchy), FM75-82 "generic c/k" cluster, FM83 "fourteen equivalent" headline, FM100 F1 ⇔ F4 "bijection" (injection), FM198 "ten unconditional", FM214 universal IS-claim, FM218 "only" universal quantifier, FM223 triple "complete strictification" repetition.
- **MP20 TYPOGRAPHY IS SEMANTICS — THE COMPILED PDF IS THE PUBLICATION**. `\texttt{e_infinity_topologization.tex}` renders a filesystem basename in monospace to the reader (V2-AP40e). `$\mathrm{conj}{:}\mathrm{periodic\text{-}cdg}$` is a `\label{}` pointer disguised as math mode with manual spacing (V2-AP40f). `\label{rem:AP172-...}` names the ledger token in the compiled PDF's link graph and every `\ref{...}` (V2-AP40b). `\index{FM47!healed}` lifts the token into the compiled index (V2-AP40c). `\begin{remark}[AP159: ...]` displays the token in the theorem-environment header (V2-AP40d). `\section{Anti-pattern register: AP171, AP172, ...}` displays the token in the table of contents. Each of these is a TYPOGRAPHIC channel through which author-side bookkeeping leaks into the reader-facing published object. The reader should never encounter AP/FM/C-prefix tokens; the compiled PDF's visual surface IS the publication. Prevents V2-AP40 and all six subclauses V2-AP40a (bibkey), V2-AP40b (label), V2-AP40c (index/hyperref), V2-AP40d (env title/section title), V2-AP40e (monospace filename), V2-AP40f (math-mode label leak).
- **MP21 AUTHOR STATEMENT PRIMACY OVER AGENT LITERATURE SEARCH**. Agents' literature searches are shallow — they return the first-match paraphrase, not the canonical source-verified statement. When an agent says "actually the literature shows X", the author's explicit statements in CLAUDE.md / AGENTS.md / the chapter proper SUPERSEDE any agent-found source until the agent has cited a specific section/theorem number and the author has confirmed. The agent is the retrieval mechanism, not the authority. Prevents V2-AP13 (trusting agent "VAs are not E_inf"), V2-AP18 (author's explicit statements override agent literature searches), V2-AP20 (never add "in the sense of [reference]" without verification).
- **MP22 AGENT REPORT VERIFICATION IS MANDATORY**. An agent's summary describes what it INTENDED to do, not necessarily what it did. When an agent commits code / writes .tex / edits prose, every claim in its report must be verified: git log --oneline for commits; grep for the claimed string presence; diff review; compile + test pass. "Trust but verify" is the discipline; a 400-word clean-sounding report can hide: (a) an unrelated file being touched, (b) a phantom label that the agent thinks it wrote but actually didn't, (c) a downgrade-instead-of-heal that violates MP10, (d) a V2-AP40 leak that was created rather than removed. Prevents false-done cascades across sessions where a later session reads the agent report rather than the .tex.
- **MP23 BUILD REGRESSION GATING IS NON-NEGOTIABLE**. Every .tex-affecting commit runs `make` (LaTeX build) and verifies PASS. Every compute/-affecting commit runs `make test` (Vol I/II) or `pytest` (Vol III) and verifies PASS. Commits that break build are catastrophic regressions that propagate across sessions; a broken build in main means the next session reads `e86901a` style emergency-fix commits rather than genuine work. The pre-commit hook enforces the rule; the discipline is to never bypass with `--no-verify`. Pre-commit hook messages surface the gate; skipping them is malpractice. Prevents Vol I emergency recovery cluster (e86901a + 0b18bfa style "fix my own commit" sequences).

### Cache Entries (high-trafficked facts; full cache in `notes/first_principles_cache_comprehensive.md`)

These entries are deliberately terse — 1-2 lines each — so the reader can scan them before a write. Each entry names the formula, the correct form, and the FM/AP it prevents. When a session starts to write a formula that matches a cache topic, verify against the cache FIRST.

- **CACHE[κ(W_N) harmonic]**: κ(W_N) = c·(H_N - 1) where H_N = Σ_{j=1}^{N} 1/j. H_{N-1} ≠ H_N - 1 (at N=2: H_1 = 1 but H_2 - 1 = 1/2). Source w_algebras.tex:2307; verified N=2 → c/2 (w_algebras.tex:2327). Prevents AP136, V2-AP34.
- **CACHE[ω normalization, Arakelov vs unit-integral]**: ω_1 = (i / (2 Im τ)) dz ∧ d\bar z has ∫ = +1; Arakelov kernel ω_Ar = -(π / Im τ) dz ∧ d\bar z has ∫ = -1; identity ω_1 = -ω_Ar / (2π). Same sign error fixed 3 times per V2-AP37. Verify fundamental-domain integral before any curvature formula.
- **CACHE[Liv06 is pre-Lie rigidity, NOT Swiss-cheese Koszulity]**: Livernet JPAA 207 (2006) "A rigidity theorem for pre-Lie algebras". For SC^{ch,top} homotopy-Koszulity cite Hoefel arXiv:0809.4623 or Hoefel-Livernet arXiv:1207.2307. Vol II carries 7 mis-bindings at line-operators.tex:88,205; modular_swiss_cheese_operad.tex:1501; bar-cobar-review.tex:1726; introduction.tex:1468; preface.tex:801; concordance.tex:100. Prevents FM157.
- **CACHE[level-stripped r-matrix]**: Affine KM at level k: r(z) = k·Ω / z, NOT Ω / z. 42+ instances across three volumes. After any r-matrix, verify k = 0 ⇒ r = 0. Prevents AP126/AP141 (THE MOST VIOLATED AP), FM98/FM99 (Gaudin level-shift by k + h^v is distinct from Yangian level-stripped, both in GRT^fin gauge orbit).
- **CACHE[B(A) is interval bar, not ∫_R A]**: B(A) = k ⊗_A^L k = ∫_{[0,1]}^{k,k} A (interval with augmentation boundaries). ∫_R A = A trivially (factorisation homology of contractible boundaryless manifold). Prevents FM43.
- **CACHE[Dunn on Z(A), never A]**: Dunn additivity applies to bulk Z(A) or Mod_A. Algebra A itself stays E_1 under R-matrix; Mod_A becomes braided (E_2 in Cat). U_q(g) is E_1; Rep(U_q(g)) is E_2 in Cat. Prevents FM40, FM41, AP-CY54.
- **CACHE[κ=0 gives class FF, not classification failure]**: Classification G/L/C/M requires κ ≠ 0. At κ = 0 (critical-level KM V_{-h^v}(g), Vir_0) classification fails; fifth class FF (Feigin-Frenkel) takes over — ChirHoch^0 = Feigin-Frenkel center, infinite-dim polynomial algebra on opers. Per Infinite Fingerprint Classification (Platonic Reconstitution). Prevents FM77.
- **CACHE[V^♮ Z/2 Leech orbifold anomaly vanishes]**: Kapustin-Saulina α = sign(det(1 - σ|_Λ)) · ε|_{Λ^σ}. For Leech Λ + Z/2 involution σ: Λ^σ = 0 (Conway: Leech has no roots), det(1 - σ|_Λ) = 2^24 > 0 ⇒ sign = +1; ε|_{Λ^σ} = ε(0,0) = 1 on trivial sublattice; α = (+1) · 0 = 0. Anchored at chapters/connections/monster_chain_level_e3_top_platonic.tex. Closes FM66 / FM120 / FM128.
- **CACHE[class M E_3 bar = 6^g, NOT (1+t)^{3g}]**: Class M E_3 bar dims = 6^g chain-level (Künneth; d_4 survives → 6 = 2·3 per handle; g=1 gives bar profile [0,3,3,0]). NEVER (1+t)^{3g} for class M. Per AP-CY21/38. Prevents Vol III bar-dim errors.
- **CACHE[κ_ch vs χ(O_X) scope]**: κ_ch = χ(O_X) PROVED only at CY_d d = 2 with h^{1,0} = 0 (e.g. K3: κ_ch = χ(O_K3) = 2). At odd d, χ(O_X) = 0 by Serre duality; κ_ch generally ≠ 0. Dimension-stratified conjecture at d = 3 (76-test engine). Per AP-CY34/AP-CY44. Prevents "all CY_d" overclaims.
- **CACHE[kappa_BKM = c_N(0)/2 universal]**: Borcherds weight theorem: κ_BKM = c_N(0) / 2 unconditionally for Borcherds-Kac-Moody denominator identity. Coincidence κ_BKM = κ_ch + κ_cat is FALSE in general — fails 7/8 diagonal Siegel orbifolds. Per AP-CY37.
- **CACHE[Heisenberg κ = k, NOT k/2]**: κ(Heis_k) = k (not k/2); Vir is the only family where κ = S_2 / 2 = c/2. KM κ = dim(g)(k + h^v) / (2h^v). Per AP39. Prevents the "κ = S_2 / 2 = c/2 looks universal" trap.
- **CACHE[Heisenberg OPE has double pole, NOT pole-free]**: α(z) α(w) ~ k / (z - w)^2. Heisenberg is E_∞ ("abelian-R scalar" tier) but NOT pole-free. Only pole-free E_∞ is BD-commutative. Per V2-AP5, FM230. Prevents "E_∞ = no OPE poles" trigger phrase.
- **CACHE[divided-power λ-bracket convention]**: Vol II uses {T_λ T} = (c / 12) · λ^3 (divided power). OPE mode T_{(3)} T = c/2 → (c/2) / 3! = c/12. Grep `c/2.*lambda^3` — if found, almost certainly wrong (should be c/12). W_3 correct form: c/360 · λ^5 (not c/3 · λ^5). Per V2-AP34.
- **CACHE[harmonic number notation trap]**: H_{N-1} = Σ_{j=1}^{N-1} 1/j ≠ H_N - 1 = Σ_{j=2}^{N} 1/j. At N = 2: H_1 = 1 but H_2 - 1 = 1/2. Different values; different conventions. Prevents AP136 (recurring confusion).
- **CACHE[self-dual central charges differ from critical]**: Koszul-dual self-duality c* (Vir c* = 13; W_N c* = α_N / 2) ≠ matter-ghost critical c_crit (Vir c_crit = 26; W_N c_crit = α_N). Never conflate. Per AP8, FM253.
- **CACHE[Chriss-Ginzburg voice recipe]**: theorem stated before proof with full scope (locus, level, family); hypotheses explicit and load-bearing; proofs cite precise geometric inputs (Springer resolution, Kähler quotient, nilpotent orbits, D-module operations); BV-BRST realization where physical; no marketing adjectives ("completely", "remarkably", "it is clear that"); Russian-school rigor (Etingof, Kazhdan, Gelfand, Kapranov, Bezrukavnikov) + mathematical-physics realization (Costello, Gaiotto, Witten). Prevents V2-AP29 (AI-slop cleanup), AP109 (list-before-prove).
- **CACHE[Y_ℏ(g), NOT Y_z^ℏ(g)]**: Algebra Y_ℏ(g) does NOT depend on z. z is a spectral parameter that lives on Δ_z, R(z), T(z), ev_z — structures ON the algebra, not the algebra itself. The 531-instance rename Y_ℏ → Y_z^ℏ was MATHEMATICALLY WRONG and was reverted. Per FM49. Prevents spectral-parameter-in-algebra-symbol violations.
- **CACHE[three chiral Hochschild models, agree on logarithmic locus only]**: (i) C^*_{ch,geom}(A) over FM_{n+1}(X) with log forms (geometric); (ii) C^*_{ch,alg}(A) = Prod_n End^ch_A(n+1)[-n] (algebraic bar/operadic); (iii) H*_GF(Lie(A)) = Gel'fand-Fuchs continuous cohomology. Quasi-iso for logarithmic chiral algebras. AT CRITICAL LEVEL k = -h^v: ChirHoch* becomes infinite-dim (FF center); HH*(A_mode) stays finite — the only regime of GENUINE difference. Always specify which model. Prevents AP-CY62, AP-CY64, FM182, FM183, FM190, FM191.
- **CACHE[Deligne-Tamarkin chain-level requires associator]**: Classical Deligne conjecture gives E_2 action on HH* COHOMOLOGY. Chiral Deligne-Tamarkin at CHAIN level requires a fixed Drinfeld associator Φ_KZ (∞-morphism, not strict). Kontsevich formality is zigzag of ∞-operads. "φ is an operad map" is WRONG without associator qualifier. Prevents FM158, FM184, FM219.
- **CACHE[kappa(K3) double-valued depending on channel]**: κ_ch(K3) = 2 (modular bar route, κ = χ(O_K3)); κ_fiber(K3) = 24 (fiber bundle rank, χ_top(K3)); κ_cat(K3) = 24 (Mukai lattice rank); κ_BKM varies by identification. Bare κ(K3) is AMBIGUOUS. Subscripts are mandatory. Prevents FM119, AP113.
- **CACHE[Heisenberg R-matrix is NOT trivial]**: Heisenberg R(z) = exp(k·ℏ/z) with monodromy exp(-2πik). Collision residue k/z. Heisenberg is E_∞ (abelian-R scalar tier) but NOT R=τ pole-free. Per V2-AP7, FM230. Prevents Heisenberg classification errors.
- **CACHE[DS class L → class M is universal in f]**: DS reduction transports class L → class M via quartic pole generation in T^W × T^W, INDEPENDENTLY of nilpotent f chosen (principal, subregular, minimal, etc.). The mechanism is Kazhdan-Roan-Wakimoto grading intrinsic to DS; T^W involves ghost bilinears with quartic divergence. Not "only principal" per FM81 naive reading. Per AP108, FM108, Unified Chiral Quantum Group Theorem. Prevents "DS only principal" overclaim.
- **CACHE[chiral coproduct is on A itself, NOT on B(A)]**: Chiral Δ: A → A ⊗ A is on A (Hopf-type structure). Deconcatenation on B(A) is structural — exists for any bar, unrelated. Do not conflate. Per Vol II pitfall, FM45. Prevents WHICH-coproduct confusion.
- **CACHE[BD pseudo-tensor is NOT symmetric monoidal]**: Chiral algebras form PSEUDO-TENSOR (BD), NOT symmetric monoidal. BD 3.4.10 defines chiral OPERATIONS; there is no bifunctor (D-mod(X), ⊗^{ch}) and no unit object for ⊗^{ch}. Correct ambient for Theorem A: factorization algebras on Ran(X) under ⋆-tensor (GR17 IV.5). Prevents FM56, FM69, FM70, FM252.

### Session 2026-04-12 FMs (FM58-FM68)

- **FM58**: Cauchy on formal series. R(z) ∈ End(V⊗V)((z)) is FORMAL; Cauchy requires CONVERGENT. Counter: use FLATNESS of connection + homotopy invariance of monodromy (algebraic/topological).
- **FM59**: Non-holomorphic retraction preserves log forms. ρ_t(z) = (1-t)z + tz/|z| involves |z|=√(zz̄), so ρ_t*(dz) has dz̄ components. Counter: algebraic de Rham / local-system argument.
- **FM60**: lem:operadic-kunneth chain-level iso. B(SC_mix) = B_mod(P_1) ⊗ B(P_2) with d_B = d_cl⊗id + id⊗d_op WRONG at chain level — open-edge contractions between mixed vertices produce cross-terms d_mix involving μ_1. Correct: on ASSOCIATED GRADED w.r.t. closed-input-excess filtration. Pentagon theorem does NOT depend on this lemma (direct Koszul duality suffices).
- **FM61**: Modular operad (iii) proved by abstract D²=0. thm:modular-bar proves D²=0 for abstract modular bar datum; concrete O^{A_∞-ch} clutching composition is different statement. Iterated B^{ann} sewing with R-matrix monodromy = OPEN (non-sequitur).
- **FM62**: "Stuck at SC^{ch,top}" for Heisenberg/lattice VOAs — WRONG. H_k has Sugawara T=(1/(2k)):JJ: (c=1); abelian CS provides 3d HT. **Heisenberg and lattice VOAs reach E_3-topological.**
- **FM63**: T_imp sign inconsistency. General formula minus; sl_2 specialization plus. Standard (FF, Kac-Roan-Wakimoto): T_imp positive. Verify sign against sl_2 before committing.
- **FM64**: Khan-Zeng scope. Covers ALL freely-generated PVAs with conformal vector, not just gauge-theoretic. conj:E3-topological-general open only for non-freely-generated (Monster VOA).
- **FM65**: R=PT meromorphicity ≠ convergence. Level-by-level rationality (each R^{(N)} rational in h_i) does NOT imply full meromorphicity. Gap: λ_min(G_N) bounds on principal series — Kac determinant growth insufficient (det ≠ smallest eigenvalue). Distinguish fixed-level rationality from level-sum convergence.
- **FM66 [CLOSED 2026-04-17]**: Monster orbifold route. V^♮ = V_Leech^+ (Z/2 orbifold). PROVED chain-level E_3-topological via `thm:monster-chain-level-e3-top` (`chapters/connections/monster_chain_level_e3_top_platonic.tex`, commit 549f881). The DW anomaly α_orb ∈ H^3(BZ/2; U(1)) is EXPLICITLY 0 via Kapustin-Saulina formula: sign(det(1-σ|_Λ)) = +1 from 2^24 > 0 (Conway: Leech has no roots, Λ^σ = 0); ε|_{Λ^σ} = ε(0,0) = 1 on trivial sublattice; α = (+1)·0 = 0. Closes FM66 + FM120 + FM128. The earlier "anomaly vanishes by modular invariance" rationale is superseded by the explicit cocycle-level computation + FLM twisted Jacobi + Dong-Mason uniqueness. Extension to remaining 70 Schellekens c=24 VOAs CLOSED unconditionally via three-stratum classification (24+1+46, `thm:schellekens-71-all-alpha-zero`, commit b0d59e0) with vELMS 2021 level-matching (commit 694730c).
- **FM67**: Curved Dunn two-complex distinction. TWO H² obstructions: (a) modular-bootstrap complex (H²=0 PROVED, every Ob_g exact), (b) curved-Dunn twisting-cochain complex (OPEN, no H²=0 proof). Bridge (a)↔(b) is the precise frontier; if bridged, curved Dunn at all genera follows.
- **FM68**: Modular operad (iii) proved ≠ abstract D²=0. Concrete axioms: composition via KZ pentagon + KL regularity (thm:affine-composition-associativity); equivariance via quasi-triangularity + YBE (prop:qt-equivariance); unitality via vacuum axiom (prop:modular-operad-unitality). Sole gap: Stokes regularity at generic non-integral level.

### Session 2026-04-16 Adversarial Campaign — Waves 1-6 (FM69-FM118)

Six-wave ~18-agent attack surface scan. Findings categorized: ambient/foundations (FM69-74), quantification/scope (FM75-83), modular/genus (FM84-90), operadic (FM91-96), physics bridges (FM97-104), classification (FM105-110), metadata (FM111-118). All with file:line anchors in `notes/first_principles_cache_comprehensive.md` entries 166-239.

**Ambient & foundations:**
- **FM69**: chiral_koszul_pairs.tex:5818-5824 claims (D-mod(X), ⊗^{ch}) is symmetric monoidal via BD 3.4.10. BD 3.4.10 defines chiral OPERATIONS (pseudo-tensor); no bifunctor, no unit object. LV12 Thm 11.4.1 mis-applied. Counter: split Thm A into FORM-A (Σ-coinvariant factorization bar via FG12+GR17 IV.5, valid) and FORM-B (ordered E_1 bar, needs independent proof).
- **FM70**: lem:operadic-koszul-transfer Step 2 invokes a "unit functor k-Mod → D-mod(X)" — D-mod(X) has no unit for ⊗^{ch}. Counter: use factorization ambient with ⊗^*, not chiral pseudo-tensor.
- **FM71**: ex:heisenberg-e1-duality:5838-5848 admits Heisenberg's actual bar is Σ-coinvariant (unordered), contradicting "E_1 ordered" headline. Counter: state R-twisted descent theorem explicitly; do not advertise ordered-bar result that only holds for symmetric bar.
- **FM72**: Vallette Thm 2.1 cited "specialized to the chiral operad" (bar_cobar_adjunction_curved.tex:6301-6343) — Val16 is for Ch(k) projective model, not D_X-module enriched. Counter: cite Francis-Gaitsgory-Rozenblyum model structure on factorization coalgebras.
- **FM73**: HTT SDR contraction (appendices/homotopy_transfer.tex:68-172) lifts k-Mod splitting to D-mod(X) verbatim — D-modules have nontrivial Ext^1, direct-sum decomposition fails. Counter: use Cousin/Koszul resolution fibrewise, or restrict to associated-graded formality.
- **FM74**: nilpotent_completion.tex:115-144 hypothesis "dim H*(A,A) < ∞" EXCLUDES motivating targets (Virasoro, Yangian, critical KM have unbounded HH). Counter: weaken to truncation-wise finiteness with conformal-weight control.

**Quantification & scope:**
- **FM75**: "Generic c/k" as euphemism (five_theorems_modular_koszul.tex:735-766, bar_cobar_adjunction_inversion.tex:1693-1707 excludes minimal-model + admissible loci but standalone does not). Counter: replace "generic" with "outside minimal-model ∪ admissible loci"; each family has its own countable exclusion.
- **FM76**: Vir_{c_{p,q}} classified class M via S_4 = 40/49 at c=1/2 (landscape_census.tex:306) but simple quotient fails PBW in bar range (l.1141). Counter: "universal algebra class M; simple quotient class OPEN when PBW fails."
- **FM77**: kappa=0 scope hole. classification.tex prop:depth-gap-standalone requires kappa≠0; critical KM V_{-h^v}(g) and Vir_0 fall OUTSIDE the G/L/C/M classification. classification_trichotomy.tex:422-427 derives S_3 as 2κ/κ — 0/0 at c=0. Counter: state classification requires κ≠0; critical/degenerate cases need separate analysis.
- **FM78**: Theorem H label overloads thm:main-koszul-hoch (Koszul-duality identity) and thm:hochschild-polynomial-growth (concentration {0,1,2}). Counter: disambiguate across every cross-reference.
- **FM79**: "Theorem H has BV-BRST origin; Proved" in bridge table. bv_brst.tex:184-197 Thm:bv-bar-geometric is \ClaimStatusProvedElsewhere[CG17]; rem:qme-bar-cobar:291 is \ClaimStatusHeuristic. Counter: split bridge row into Koszul origin (Proved) / BV-BRST reading (Heuristic).
- **FM80**: Thm H concentration proved on chirally Koszul locus only; minimal-model Vir, critical KM, W(p) triplet EXCLUDED but Vol II/bridge tables cite unconditionally. Counter: every cross-reference "(chirally Koszul, non-critical)".
- **FM81**: thm:E3-topological-DS-general overclaims to non-principal nilpotents — fractional-weight ghost bilinears (BP, min sl_4) are NOT Cartan-only. Counter: restrict to good-integer-graded (principal + selected minimal) or verify ghost cancellation example-by-example.
- **FM82**: thm:E3-topological-free-PVA "all class M" is wrong — class M by definition has infinite-depth shadows from quartic poles, incompatible with polynomial λ-brackets required by Khan-Zeng. Counter: scope to freely-generated PVAs (class G/L/C), strike class M and matter-coupled claims.
- **FM83**: "Fourteen equivalent characterizations of Koszulness" — actually 10 biconditional + 4 scoped implications (standalone:350-366 admits this; headline elides). Counter: "ten unconditionally equivalent + four scoped."

**Modular & genus:**
- **FM84**: W_3 genus-2 formula (c+204)/(16c) has three inconsistent decompositions (higher_genus_foundations.tex:6054-6068 uses four graphs; w_algebras.tex:5731-5739 table uses three; prose at 5749 reintroduces fourth). Counter: single canonical derivation, fix table.
- **FM85**: AP37 sign reconciliation left in proof. higher_genus_foundations.tex:3449-3495 reconciles -2π²i vs +2πi via in-proof rescaling with no independent derivation. Counter: provide Deligne-pairing or Fay-based derivation.
- **FM86**: AP32 UNIFORM-WEIGHT leak in cor:mumford-multiplicative (higher_genus_foundations.tex:5285). (obs_g)² = 0 for ALL-WEIGHT inherited from UNIFORM-WEIGHT proof without killing δF_g^cross cross-term. Counter: downgrade all-genera nilpotence for multi-weight or add cross-term vanishing proof.
- **FM87**: rem:curved-dunn-additivity / phantom label prop:genus1-twisted-tensor-product cited across CLAUDE.md, AGENTS.md, ROADMAP_85_TO_100.md — ZERO .tex hits (only conj:curved-dunn-additivity exists). Counter: delete phantom label everywhere; metadata must match .tex ground truth.
- **FM88**: Cross-genus MC equation DΘ+½[Θ,Θ]=0 proved only genus-wise via Gauss-Manin; cross-genus composition needs curved-Dunn H²=0 at g≥2, distinct from modular-bootstrap H²=0 (FM67 repeat with sharper file locations). Counter: state genus-wise flat; cross-genus conjectural.
- **FM89**: Separating vs non-separating degeneration at g=2. δF_2 boundary-stratum sum (w_algebras.tex:5706-5742) is boundary-only; no degeneration-independence check. Separating degeneration carries zero genuinely g=2 info (AP157). Counter: add degeneration-independence lemma.
- **FM90**: AP156 ζ_τ quasi-periodicity. higher_genus_foundations.tex:3477 writes ζ_τ(z)dz = dz/z + (smooth) treating jump 2η₁ across B-cycle as smooth. Counter: include 2η₁ term explicitly.

**Operadic:**
- **FM91**: Kan-complex "proof" of modular operad composition (3d_gravity.tex:6088-6112). Source Kan-ness of StGraph does NOT imply target composition coherence. Inversion of implication. Counter: delete remark; only KZ/KZB proves concrete composition.
- **FM92**: thm:convolution-d-squared-zero (abstract D²=0) cited as proof of concrete O^{A∞-ch} sewing associativity (3d_gravity.tex:5691-5699). Non-sequitur (FM61 repeat with sharper anchors). Counter: separate abstract convolution from concrete sewing in every citation.
- **FM93**: Dual-labeled ProvedHere across volumes: thm:complete-strictification-v1 (Vol I + appendix) vs thm:complete-strictification (Vol II bridge) — different proofs, same name, Vol II version has unproved generalization. Counter: merge labels; single canonical proof; delete "-v1" aliases.
- **FM94**: "Coproduct rigidity" invoked 4× in dg_shifted_factorization_bridge.tex without lemma/definition. Only thm:ngon-rigidity exists (path-sector only); non-path case asserted without proof. Counter: define coproduct rigidity as named lemma OR restrict theorems to path-sectors.
- **FM95**: "dim coefficient = 1 ⇒ H³ = 0" (rem:root-mult-one-hero in bridge:1907-1955). Scalar coefficients do NOT imply cohomology vanishing; complex structure matters. Counter: add lem:spectral-H3-vanishing computing the cohomology directly, not the coefficients.
- **FM96**: Filtered twist convergence (bridge:1066-1069) "in completed filtered algebra" — no topology stated on dg-shifted Yangian. Counter: state (u^{-1})-adic completeness argument explicitly.

**Physics bridges & seven faces:**
- **FM97**: Seven faces "chain F1⇔…⇔F7" is star graph: F1 hub, six spokes; plus external F5⇔F6 (Drinfeld-STS, 1983-85). No complete 7-way equivalence. Counter: present as "F1 + six hub identifications"; avoid "seven equivalent."
- **FM98**: F5 (Yangian, level-independent) vs F7 (Gaudin, level-shifted by k+h^v) conflated (seven_faces.tex:394-399). At k=0: Yangian r(z) ≠ 0; Gaudin r(z) = Ω/h^v ≠ 0; level-stripped r = 0. Three different objects. Counter: declare normalization per face; state the (k+h^v) conversion explicitly.
- **FM99**: Chained equality k·Ω_tr/z = Ω/((k+h^v)z) in landscape_census.tex:230,447. False as rational functions of k (linear zero vs pole structure differ). Counter: state as two normalizations related by Casimir rescaling, not one function.
- **FM100**: F1 ⇔ F4 bijection claimed; actually INJECTION. r(z) determines KZ 1-form hence Gaudin Hamiltonians, but Drinfeld associator Φ_KZ has MZV (ζ(2), ζ(3), …) coefficients invisible to r(z). Counter: state injection; higher-order associator data separate.
- **FM101**: Face F7 underdetermined. Canonical (seven_faces.tex): Gaudin generator = simple-pole k=1 truncation. Folklore (CLAUDE.md): top A_∞ operation. For class M (k_max≥3 in W_N), these differ: Gaudin is strict subset of r(z); top A_∞ is strict superset. F7 = r(z) only for k_max=1 (G, L). Counter: define F7 precisely once.
- **FM102**: Celestial Weinberg "proof" imports Mellin dictionary. thqg_soft_graviton_theorems.tex:641-706: algebraic Ward identity is ProvedHere but celestial match treats Mellin/bilinear identification as free. Counter: split theorem — Ward identity Proved, Weinberg match ProvedElsewhere[HMPS15] conditional.
- **FM103**: Higher-r soft factors r≥4 claimed ProvedHere (thqg_soft_graviton_theorems.tex:1547-1598). Actual higher-soft (Hamada-Shiu, Li-Strominger) involves angular momentum + stress-tensor insertions not derived. Counter: downgrade r≥4 to Conjectured.
- **FM104**: "Class C = quartic BMS" (thqg_soft_graviton_theorems.tex:2172-2240). No celestial-literature counterpart. Counter: structural analogy, not theorem.

**Classification:**
- **FM105**: Trichotomy vs quaternitomy filename/content divergence. standalone/classification_trichotomy.tex abstract: "three invariants and four shadow classes." "Trichotomy" refers to k_max ∈ {0,1,≥3} operator-order, NOT G/L/C/M. Counter: rename file classification_three_invariants.tex or explicit disambiguation.
- **FM106**: Symplectic boson (class G per Z_2-symmetry killing Q) vs symplectic fermion (class C per landscape_census.tex:296). Same Z_2 structure, different class — logical inversion. Counter: single coherent assignment via explicit OPE computation.
- **FM107**: "Pole-order dichotomy" Vol II CLAUDE.md pitfall is CORRELATION not BIJECTION. Heisenberg p_max=2 class G; affine KM p_max=2 class L; beta-gamma p_max=1 class C. Prop 3.3 in trichotomy proves (p_max, r_max) independence. Counter: "class assignment requires full shadow tower (AP-CY12); pole order does not determine class."
- **FM108**: DS L→M bridge presented universally. classification.tex conj:ds-shadow-escalation — Proved for f_prin, type-A low-rank verified for non-principal, general UNVERIFIED. Counter: "(proved principal; conjectural non-principal)".
- **FM109**: Class C rank-one vs multi-sector. classification.tex:828-834 notes d_alg=2 is multi-sector artefact; rank-one Riccati only gives {0,1,∞}. Counter: present as (i) rank-one trichotomy on each primary line, (ii) multi-sector refinement yielding quaternitomy.
- **FM110**: d_alg vs r_max mapping implicit. Both standalones use {0,1,2,∞} and {2,3,4,∞} for the same classification without stating d_alg = r_max − 2. Counter: name this as a proposition.

**Metadata, labels, narration:**
- **FM111**: AGENTS.md AP178 ("modular operad (iii) NOT proved; even g=1 clutching CONJECTURAL") vs CLAUDE.md FM68 ("composition PROVED all genera integrable"). Three authoritative files disagree. Counter: .tex is ground truth; reconcile metadata to per-family, per-level, per-genus table.
- **FM112**: "Holographic codes" = metaphor, not construction (holographic_codes_koszul.tex). No HaPPY tensor-network; chapter title outruns proofs. Counter: rename Thm G12 to "algebraic bar-cobar reconstruction"; holographic reading in Remark.
- **FM113**: Code distance d=2 conflates bar homological degree with Knill-Laflamme error-correction weight (holographic_codes_koszul.tex:683-689). Counter: drop d=2 claim; state "bar degree filtration starts at 2."
- **FM114**: "Platonic" ambiguous (Plato vs Platonic-solid/ADE via McKay). No ADE content in frontier_modular_holography_platonic.tex. Counter: rename "canonical" or "completed."
- **FM115**: Operadic Koszul-dual flip misnamed Feigin-Frenkel. genus_expansions.tex:3154, standalone five_theorems p.945 cite "FF involution k → -k - 2h^v" — genuine FF duality (k+h^v)(k'+h^v)r = 1 is NONLINEAR. Counter: rename to "operadic Koszul-dual scalar flip"; distinguish from W-algebra FF self-duality.
- **FM116**: "(2-d)-shifted" vs −(3g−3)-shifted symplectic. Thm C standalone reads PTVV-for-CY_d; chapter uses Verdier-on-M̄_g. Different structures. Counter: state −(3g−3) explicitly; drop PTVV-for-CY_d framing from Vol I.
- **FM117**: cor:string-amplitude-genus0 is Conditional mis-tagged as Corollary (free_fields.tex:4845-4880). Pairing-compatibility hypothesis is independent analytic input, not a derivation. Counter: re-environment as Conditional Proposition.
- **FM118**: "Analytic HS-sewing proved at all genera" (N5_mc5_sewing.tex, analytic_sewing.tex:1772-1793) is amplitude BOUND, not modular-invariant sewing package. Counter: "HS bound on |Z_g|; modular well-definedness + full Huang sewing separate."

### Meta-pattern: metadata drift

Three files advertise theorem status (CLAUDE.md, AGENTS.md, ROADMAP_85_TO_100.md); .tex ground truth diverges from each. Enforcement: before claiming any status in prose, grep the .tex for (a) \ClaimStatus tag, (b) \begin{theorem}/proposition/lemma environment, (c) actual \begin{proof} body or ProvedElsewhere citation. Treat metadata as STALE until verified against .tex.

### Waves 5-6 supplement (FM119-FM129, 2026-04-16 adversarial campaign continued)

**Lattice / Monster / moonshine:**
- **FM119**: κ(K3) subscripting. symmetric_orbifolds.tex:113,411 gives κ(K3)=2; bv_brst.tex:2767 gives κ(K3)=24. Both are correct with different subscripts (κ_ch=2, κ_fiber=24) but the bare κ usage violates AP113. Counter: subscript every κ; add a mandatory "κ_WHICH" convention block.
- **FM120**: Monster V^♮ = V_Leech^+ "inherits E_3-topological by finite-group invariants." Z/2 Leech involution is BULK GAUGING (orbifold), not trivial-action fixed-point; "finite-group invariants preserve E_n" applies to the latter, not the former. Counter: downgrade FM66 to "requires (i) explicit abelian-CS level-matrix selecting V_Leech as boundary, (ii) Dijkgraaf-Witten H³(BZ/2,U(1)) anomaly vanishing; modular invariance of partition function is NOT equivalent to DW anomaly vanishing."
- **FM121**: prop:symn-twist-vanishing q⁰ mechanism. symmetric_orbifolds.tex:146-171 justifies obs_1 vanishing via q⁰ torus amplitude; actual mechanism is weight-1 current / stress-tensor counting. Right conclusion, wrong proof — would break at other c. Counter: use generator-count additivity.
- **FM122**: Moonshine G→M class transition collapsed. moonshine.tex:288-317 treats V_Λ → V^♮ as single step; class-change happens at V_Λ^+ (already class M by lone-Virasoro lane). Counter: two-step decomposition; "only instance in standard landscape" needs enumeration or deletion.
- **FM123**: Sym^N K3 κ = c/3 treated as law. symmetric_orbifolds.tex:459-470 attaches "anomaly ratio ϱ=1/3" non-standard terminology; c/κ=3 at c=6 is a coincidence of the Virasoro subalgebra, not an additive law. Affine+Virasoro direct sum gives κ=4 not 2. Counter: drop the "ϱ=c/3" rule.
- **FM124**: Moonshine Koszul dual. moonshine.tex:225-243 frames "partner Vir_2" as Koszul dual of V^♮; actually Koszul dual of the Vir_{24} subalgebra, not of V^♮. Counter: relabel "Koszul dual of Vir subalgebra"; (V^♮)^! is separate and undefined.

**3D gravity climax:**
- **FM125**: thm:gravity-koszul-triangle projection vs equivalence. 3d_gravity.tex:2103-2118 declares Bulk = Z^der(Vir_c) ≃ HH^0 ⊕ HH^2[-2] ≃ C[[c]] ("pure 3d gravity has one parameter"). Right: HH^0 = HH^2 = C for Gel'fand-Fuchs. Wrong: the declared framework is ChirHoch C^•_ch; projection onto two sectors is not the full derived chiral centre (AP-CY64 three-way). Counter: state as PROJECTION onto saddle-point reading; "bulk ≃ C[[c]]" is not a derived equivalence.
- **FM126**: Stale bridge label + LG/chiral conflation. Vol II CLAUDE.md bridge "Global triangle: PROVED for G/L/C (thm:global-triangle-boundary-linear)" — cited label does not exist. Actual theorem thm:boundary-linear-bulk-boundary (ht_bulk_boundary_line_core.tex:1234) proves bulk = dCrit for commutative Landau-Ginzburg superpotentials, NOT for chiral algebras G/L/C. Counter: fix stale label; clarify bridge row scope (LG cotangent identification ≠ chiral global triangle); the chiral G/L/C triangle rests on separate HH computations.
- **FM127**: "Perturbative finiteness" — algebraic not physical. thqg_perturbative_finiteness.tex:788-798 claims no UV renormalization at any genus. Right: the bar-complex MC generating function on the scalar lane converges. Wrong: this is algebraic/combinatorial finiteness, not QFT UV finiteness (the latter requires chain-level E_3, open for class M). Counter: split algebraic finiteness (Proved) vs physical UV finiteness (subject to class-M chain-level E_3 gap). **Forward reference (2026-04-17 Wave-2):** class-M chain-level is now CLOSED on the pro-ambient / J-adic / filtered-completed ambients of the raw bar complex via Vol I `thm:mc5-class-m-chain-level-pro-ambient` (`chapters/theory/mc5_class_m_chain_level_platonic.tex:229-437`); direct-sum `Ch(Vect)` remains genuinely false (S_4(Vir_c) ≠ 0) but is the WRONG AMBIENT for the raw bar complex. The physical UV-finiteness gap tracked here is therefore resolved on the correct ambient; the remaining open direction is physical-UV interpretation, not chain-level E_3.
- **FM128 [CLOSED 2026-04-17]**: "Bounded technical construction" as research expectation → SUPERSEDED by `thm:monster-chain-level-e3-top` explicit α=0 computation (Kapustin-Saulina formula + Conway Λ^σ=0 + FLM twisted Jacobi + Dong-Mason uniqueness). V^♮ chain-level E_3-topological is PROVED unconditional; no longer a research expectation. See `chapters/connections/monster_chain_level_e3_top_platonic.tex`, commit 549f881.

**Celestial / arithmetic:**
- **FM129**: "Ramanujan bound via shadow tower" arithmetic_shadows.tex:132-140 claims to bypass Weil. Chain goes through converse theorem + Langlands functoriality, which uses Deligne-type inputs — NOT independent of Weil. Counter: rephrase as "structural refinement of Deligne's bound via shadow stratification; dependency on Langlands inputs acknowledged."

### Wave 7 supplement (FM130-FM142, W-algebras + Yangians + YM/anomaly/log bridges)

**W-algebras:** (W_N kappa probe DEFUSED — Vol I has the general formula c*ρ(g) = c*Σ 1/(m_i+1) at `w_algebras.tex:2307`, B_2=3/4 verified at line 2327.)

- **FM130**: thm:wn-obstruction Step 2 cross-term vanishing (w_algebras.tex:2214-2231) proved for N=2,3 by direct computation; computationally verified N≤6 (Creutzig-Linshaw); N≥7 CONJECTURAL without cross-channel curvature hypothesis. "Orthogonality + associativity" gives invariant-form orthogonality, which is weaker than curvature-channel vanishing. Counter: mark "proved N=2,3; computationally verified N≤6; conjectural N≥7."
- **FM131**: BP self-dual proof (bershadsky_polyakov.tex:194-223) chains hook-transport + FF involution without citing de Boer-Tjin 1993 free strong generation (required hypothesis of CLNS24 hook transport). Counter: add one proof line citing de Boer-Tjin + note PBW collapse at E_2.
- **FM132**: "Inherits Koszulness" phrasing. logarithmic_w_algebras.tex:311-314 asks whether W(2)=SF^{Z_2} inherits Koszulness. Z_2 invariants generically BREAK free strong generation (K[x,y]^{Z_2} has 3 gens + 1 rel). Risk of AP-CY54 averaging/inheritance conflation. Counter: "orbifold kernels generically break free strong generation; whether Adamovic-Milas generators satisfy PBW universality is OPEN."
- **FM133**: N=2 SCA "verified computationally through weight 6" (n2_superconformal.tex:287-312) — no `@independent_verification` decorator; AP-CY49 tautological test risk (engine may self-verify). Counter: install decorator pointing to N=2 SCA compute module with disjoint derived_from / verified_against.
- **FM134**: Y-algebra triality invariance of shadow class (y_algebras.tex:88-145,289,714-800) asserted as foundational without proof. Gaiotto-Rapcak S_3 triality is real; preservation of PBW collapse page / shadow depth under triality is NOT proven. Counter: "CONJECTURAL: triality preserves shadow class; verified for small L,M,N."
- **FM135**: W_3 holographic datum standalone (w3_holographic_datum.tex:54-100) claims "83 tests / 3 independent paths" without Vol II independent-verification decorator structure (disjoint derived_from/verified_against). "First rank-2 holographic modular Koszul datum controls every 3d HT QFT" is unqualified existential. Counter: install decorators per Vol II protocol; downgrade "controls every" to "conjecturally controls; verified for standard landscape."

**YM / anomaly / log-monodromy / critical string:** (FM56 CLEAN across 7 chapters; AP40 447-environment spot-check CLEAN.)

- **FM136**: Open_B = B^ch(A_B) ≃ C^{∞/2+•}(A_B) "for Koszul-admissible A_B" (ym_boundary_theory.tex:186, ym_synthesis_core.tex:53) tagged ProvedHere. "Koszul-admissible" broader than the actual proof scope (affine + principal W only). Counter: "(for A_B in the affine + principal-W lineage)"; downgrade to ProvedElsewhere for broader classes.
- **FM137**: Mass-gap theorem vacuous-hypothesis framing (ym_instanton_screening.tex:695). Hypothesis "algebraic screening domination with α·μ² > ε" effectively contains the conclusion; min-max gives gap trivially. Theorem framed as mass-gap breakthrough; actually an algebraic reduction principle. Counter: retitle "Algebraic mass-gap reduction principle"; preserve ProvedHere on the min-max corollary; acknowledge the bridge construction is the remaining work.
- **FM138**: "Yang-Mills" unmodified across four YM chapters invites Clay-problem reading. Actual scope: HT-twisted 4d N=2 YM (Costello-Gwilliam / Paquette-Williams). Counter: global rename "HT-twisted N=2 YM boundary"; keep unmodified "Yang-Mills" only when discussing the Clay problem explicitly.
- **FM139**: "Central screening sequence" (ym_instanton_screening.tex:184, 593) borrows VOA screening terminology without content. VOA screenings = residues of weight-1 primaries (Felder, Fuchs); none present here. Counter: rename "central q-adic annihilator sequence"; add remark on conjectural Felder/Wakimoto connection.
- **FM140**: "Logarithmic HT monodromy" chapter title (log_ht_monodromy_core.tex:1-48) means log-FM compactification, NOT logarithmic VOA. Reader-misdirection risk. Counter: prepend Scope Remark distinguishing log-FM from logarithmic-VOA.
- **FM141**: "Critical string dichotomy" at c=26 (thqg_critical_string_dichotomy.tex:904, 1068, 1224). Theorem actually proves Clifford-degeneration dichotomy u=0 vs u≠0 at c=0/c=26 (Koszul pair); rem:g9-no-ghost:1134 honestly disclaims deriving the no-ghost theorem. Subsection titles hype. Counter: retitle to emphasize Clifford-degeneration content.
- **FM142**: "Anomaly-completed Yangian completion theorem" (anomaly_completed_core.tex:1426) floats between universal-algebra and physical-identification levels. No specific chiral algebra A with genus anomaly Θ_g identified as input. Counter: add Interpretation remark noting applicability to any specific physical Y+Θ pair is CONJECTURAL.

### Wave 8 partial supplement (FM143-FM147, FM compactification + Kontsevich)

- **FM143**: Re/Im swap in prop:propagator-restriction (kontsevich_integral.tex:186-213). Proposition writes Re(η_{ij})|_{S^1} = d arg + exact; proof correctly derives η = d log|z| + i d arg (so d arg is IMAGINARY). ProvedHere tag conceals notation collision. Counter: write Im (or "real 1-form coefficients on S^1"); add glossary.
- **FM144**: Arnold cancellation proof (fm-proofs.tex:413-434) produces 2∫γ_{ST} then hand-waves via ∂²=0. Sign tracking gives Res_T·Res_S = -Res_S·Res_T (Step 2), then Step 3 orientation swap adds a SECOND (-1), giving +1·+1 = 2. Author double-counted — outward-normal convention on nested faces introduces ONE (-1), not two. Counter: redo sign bookkeeping OR cite Getzler-Jones and drop explicit calc.
- **FM145**: prop:general-orient-sign (orientations.tex:371-416) tagged ProvedHere with uniform formula ε_{D_S} = (-1)^σ(S); Corollary 3 lines later: "requires more care; general formula depends on specific coordinate change." Proof checked only n=3,4. Counter: scope-restrict to fixed coordinate ordering OR downgrade Corollary to Remark; general n OPEN.
- **FM146**: Kontsevich formality "exactly this statement" (kontsevich_integral.tex:540-594) overclaims. Kontsevich formality is L_∞ quasi-iso over Q; chain-level to rational E_3 collapse (AP-CY33). Construction environment is correct; prose overreaches. Counter: excise "exactly"; keep `construction` env; identification as theorem is conjectural.
- **FM147**: "4T = Arnold" (kontsevich_integral.tex:130-164, thm:bar-weight-systems). 4T on chord diagrams involves 4 endpoints on circle; Arnold = quadratic relation among 3 propagators. 4T descends from Arnold + STU + graded commutativity, NOT Arnold alone. Counter: cite Bar-Natan 1995 §3; spell out STU.

### Wave 8 partial supplement ctd. (FM148-FM154, raviolo + PVA descent)

- **FM148**: thm:PVA-descent-roadmap (raviolo.tex:579) uses universal "for any logarithmic SC^{ch,top}-algebra". Def:log-SC-algebra (L363-374) requires ω_k^hol ∈ Ω^•_log (d log only), excluding class M (quartic poles). Counter: restrict to "classes G, L, C"; class M gives P_∞-chiral not PVA (V2-AP21/22).
- **FM149**: D6 transverse closedness hidden (prop:m3_vanish:1032-1040). "Product decomposition ensures topological contraction does not disturb the holomorphic kernel" conceals requirement that ω_k^hol is d-closed in transverse direction — true for Arnold-OS log kernels, false for quartic. Counter: add explicit hypothesis; state class M outside scope.
- **FM150**: raviolo R-matrix twist absent. def:raviolo-restriction (raviolo.tex:31-43) and prop:SC-raviolo Step 2 write A_ch(D×I)/~ identifying "from above/below via E_1-coherence" without specifying Mon(R) isotopy. For E_1 (Yangian) seeds, R(z) is independent external data; as written, the construction yields untwisted V⊗V. Counter: Mon(R) must appear in the equivalence relation; E_1 seeds supply it externally.
- **FM151**: Internal tension prop:chain-D-vs-S1 (raviolo-restriction.tex:50-123). (iii) "ρ is qiso to Z(A) on both sides" while (iv) source E_2, target only E_1 (AP-CY62/64/65). Counter: "qiso of underlying chain complexes; both compute HH^ch_• as graded vector spaces; E_2 + spectral R(z) survive only on punctured-disk side."
- **FM152**: Y(a,z) reconstructed only at leading order (prop:raviolo-VA Step 2, raviolo.tex:84-105). "Y reconstructed from regular part μ(a,b) = m_2^reg|_{λ=0}" — setting λ=0 kills all ∂^k data; only a_{(-1)}b recovered, not the full Σ_{n<0} a_{(n)}b z^{-n-1}. Counter: full reconstruction requires d_B + translation T, not μ|_0.
- **FM153**: Raviolo coinvariants via Lie-algebra framing. def:coinvariants (raviolo-restriction.tex:28-34) uses Γ(X, V_rav)_G^h where G is a Lie algebra. Native operation in BD pseudo-tensor is CHIRAL coinvariants; Lie-algebra version requires Sugawara/Zhu mode bridge. Counter: name Sugawara/Zhu bridge or define chiral coinvariants directly.
- **FM154**: D2-D6 README shorthand "proved" compresses log-SC scope + worked-example-vs-universal. README: "PVA descent D2-D6 proved" — actually proved for logarithmic SC-algebras with sl_2 as demonstration. AP28 partial tautology (PVA λ-bracket defined from OPE via Borel). Counter: "D2-D6 proved for logarithmic SC-algebras (classes G, L, C); sl_2 worked; class M descent is P_∞-chiral, separate theorem."

### Wave 8 partial supplement ctd. (FM155-FM160, SC^{ch,top} pentagon of equivalences)

- **FM155**: Phantom label `prop:sc-koszul-dual-three-sectors` (spectral-braiding-core.tex:3730, bv_brst.tex:2059). TWO \ref citations, ZERO \label definitions across chapters/. Load-bearing for thm:dual-sc-algebra. Counter: either write the proposition with real operadic computation, or downgrade thm:dual-sc-algebra to Conjectured. (Phantom-label pattern repeat of FM87.)
- **FM156**: Koszul dual closed sector Com^! = Lie conflates E_2 with Com. thm:dual-sc-algebra declares closed sector of (SC^{ch,top})^! is Com^!=Lie; but closed color of SC^{ch,top} is C_*(FM_k(C)) = E_2, whose homology is Gerstenhaber (self-dual up to shift, Getzler-Jones), NOT Com. Com→Lie holds only on gr w.r.t. Poisson filtration. Counter: "on gr SC^{ch,top}, Koszul dual is (Lie·Com, Ass, trivial-mixed); on SC^{ch,top} itself, closed-sector dual is chiral Gerstenhaber dual (E_2{1})."
- **FM157**: Liv06 citation mis-binding across 7+ files. main.tex:1627 binds Liv06 = Livernet, "A rigidity theorem for pre-Lie algebras" JPAA 207 (2006) — about pre-Lie rigidity, NOT Swiss-cheese. Yet cited for SC Koszulity at line-operators.tex:88,205; modular_swiss_cheese_operad.tex:1501; bar-cobar-review.tex:1726; introduction.tex:1468; preface.tex:801; concordance.tex:100. Correct attribution: Hoefel arXiv:0809.4623 or Hoefel-Livernet arXiv:1207.2307. Counter: global rebind; add Hoefel09 and HL12 to bibliography.
- **FM158**: thm:homotopy-Koszul Step 2 overstates Kontsevich formality as strict dg-operad map (line-operators.tex:121-122). "Since φ is an operad map, φ_{k+l-1} ∘ ∘_i^{FM} = ∘_i^{E_2} ∘ (φ_k ⊗ φ_l)" — Kontsevich/Tamarkin formality is ∞-morphism, associator-dependent. Counter: "Fix a Drinfeld associator Φ"; reword as zigzag of ∞-operads; cite Fresse/Vallette for Koszulity transfer.
- **FM159**: SC^{ch,top} ≠ sub-operad of Voronov's SC. rmk:hKoszul-evidence transfers Koszulity from classical SC; Voronov's FM_{k,m}(H, ∂H) is NOT a product, while SC^{ch,top}'s FM_k(C) × E_1(m) IS (rem:product-forced-by-locality). Koszulity transfer through the product collapse needs explicit Künneth + homotopy-operad argument. Counter: add lemma "product-collapse qiso SC^{ch,top} → SC_Vor is map of homotopy operads"; or restate as zigzag.
- **FM160**: Edge (3↔4) chain-level overclaim. bv-construction.tex:4 "QME becomes the open/closed MC equation." Two MC elements (S_eff vs α_T ∈ g^SC_T) agree at quasi-iso level via homotopy transfer (Step 4), NOT at chain level on a canonical model. FM67 pattern repeat. Counter: "QME ↔ MC at level of quasi-iso classes; chain-level equality after fixed gauge/semifree model."

### Wave 7 supplement ctd. (FM161-FM170, Yangians cluster)

- **FM161**: Y(g) Koszulness via PP05 nonhomogeneous duality (yangians_foundations.tex:623-635) — PP05 Ch. 4 requires connected grading A_0 = k. Yangian level grading has PRO-FINITE A_0; "passing to augmentation ideal" (L552) does not produce PP05-compatible grading. Counter: "filtered-CDG-Koszul deformation of U(g[t])"; use Positselski nonhomogeneous properly; restrict to classical types.
- **FM162**: Exceptional-type PBW uncited. yangians_foundations.tex:310,344,623 cites Molev §2.5 as giving PBW "for all classical types"; prop:yangian-koszul extends to "any simple g." Molev 2007 covers A,B,C,D only; E_6-E_8, F_4, G_2 need Guay-Regelskis-Wendlandt 2018 (arXiv:1706.05176), uncited. Counter: add GRW18 citation or restrict prop:yangian-koszul to classical types.
- **FM163**: Y(g)^! = Y(g)^{hbar→-hbar} handwave. yangians_foundations.tex:557-558 "higher-order terms in R^{-1} are automatic consequences of YBE." R^{-1}(u) on symmetric/antisymmetric subspaces equals u/(u∓hbar), NOT 1 + hbar P/u at higher orders. Matching algebras requires all orders. The Chevalley-involution T → T^{-1T} with hbar → -hbar is a SEPARATE automorphism, not quadratic Koszul duality. Counter: verify R^perp under trace pairing to all orders; state isomorphism independently.
- **FM164**: Bar-cobar Yangian completion elision. yangians_foundations.tex:677-701 "counit is quasi-iso for augmented pro-nilpotent E_1-chiral algebras." Pro-nilpotence of A (∩ I^n = 0) does NOT imply conilpotence of B(A); gives conilpotence only on COMPLETED \hat{B}(A). Counter: "\hat{Ω}^ch \hat{B}^ch(A) → \hat{A} is qiso in pro-nilpotent completion category; raw bar-cobar fails for Yangian." Wave 6 A6 repeat with specific location.
- **FM165**: Gaudin from MC "projection" handwave. gaudin_from_collision.tex:210-266 "[H_i^{GZ}, H_j^{GZ}] = 0 follows from MC equation." MC projects to CYBE; FFR 1994 proof uses CYBE + explicit r-matrix computation on eval-module tensors (Sugawara + Bethe steps). At k = -h^v FF center gives commutants, not zero — but proof excludes critical level without addressing mechanism. Counter: replace "MC projection" with "CYBE + r-matrix computation on eval tensors (FFR)."
- **FM166**: Jones polynomial from ordered-E_1 bar monodromy. ordered_associative_chiral_kd.tex:5810-5871: "J_K(q) = tr_q(ρ_n^{HT}(β))." Bar monodromy = KZ monodromy = DK = U_q braid rep is proved at GENERIC q. Jones is RT at INTEGER level, requiring Rep_q(sl_2) at q = e^{πi/(k+2)} modulo NEGLIGIBLE MODULES (MTC quotient). Level truncation + negligible-quotient step elided — this is E_∞ factorisation homology (CFG), NOT E_1-ordered-bar (FM55 repeat). Counter: split into (i) bar monodromy = braid rep (proved); (ii) Jones = RT functor on MTC quotient (separate; cite Reshetikhin-Turaev).
- **FM167**: Y(g)^! = Y(g^v) non-simply-laced scope overreach. yangians_foundations.tex:569-588 rem:yangian-langlands "conjecturally Y(g^v) for non-simply-laced." Simply-laced case reduces to hbar-sign-flip automorphism (FM163). Non-simply-laced is QUANTUM GEOMETRIC LANGLANDS at Yangian level — a deeper conjecture. Counter: tag simply-laced (proved via automorphism) vs non-simply-laced (Langlands conjecture) separately.
- **FM168**: Gravitational Yangian CYBE = formal-series identity only. thqg_gravitational_yangian.tex:1751-1870 Virasoro r^{grav}(z) = Σ_m Ω_m/z^{m+1} with CYBE "via Arnold + IBR." [Ω_0, Ω_0] = [Σ L_{-n} ⊗ L_n, ...] is regularised infinite sum on infinite-dim algebra; CYBE is FORMAL-SERIES identity in z_{ij}, NOT algebraic identity in a genuine algebra. Vir^! = Vir_{26-c} is c↔26-c Koszul involution at operator level, not r-matrix Koszul dual. Counter: "CYBE as formal-series identity in pro-completion; genuine algebraic interpretation requires specifying Vir-module category."
- **FM169**: "Gravitational Yangian" as Hopf algebra. dg-shifted Yangian = ordered E_1 face of universal twisting — is bialgebra, NO antipode (Layer B/C of rem:yangian-triage). Vol II prose uses it as Hopf for graviton S-matrix. Counter: rename "Gravitational dg Lie bialgebra"; genus-0 S-matrix uses classical r-matrix only (no antipode needed); Hopf promotion open.
- **FM170**: k_max = 2 landscape exclusion missing super-qualifier. gaudin_from_collision.tex:334-343 correct for bosonic self-OPEs; FAILS for fermionic weight-3/2 (NS, super-Vir, N=2 SCA odd generators, AP107). Counter: add "bosonic" qualifier to rem:k2-absent; note superconformal exception.

### Wave 9 supplement (FM171-FM181, foundations + RTT/Baxter/coideals)

**Foundations / axioms / recognition:**
- **FM171**: (H1)-(H2)=(a)-(c) misidentification. CLAUDE.md reads "(H1)-(H2) are conditions of physics bridge theorem"; pva-preview.tex:18 still has `\begin{assumption}[Analytic hypotheses (H1)-(H4)]`. thm:physics-bridge (raviolo.tex:407) hypotheses are (a) BV data, (b) one-loop finiteness [GRW21], (c) polynomial interactions — NOT the (H1)-(H4) list. Counter: bridge hypotheses (a)-(c) IMPLY (H1)-(H4) as derived log-SC properties; do not equate the two lists.
- **FM172**: Zombie pva-descent.tex. Lines 186, 668, 818 still carry `Assume (H1)-(H4)` in theorem statements while pva-descent-repaired.tex exists as the unconditional version. Counter: delete pva-descent.tex entirely or rewrite to cite log-SC hypothesis.
- **FM173**: Double-labeled recognition theorem. foundations.tex:1462-1464 has both `\label{thm:recognition-foundations}` and `\label{thm:recognition}`; locality.tex:364 has `\label{thm:recognition-SC}`. Two ProvedHere theorems with overlapping content. Counter: single canonical label + cross-references; delete duplicate content.
- **FM174**: Zombie foundations drafts. foundations_overclaims_resolved.tex (305L) + foundations_recast_draft.tex (749L) coexist with foundations.tex (2631L); KK-transfer duplicated at foundations.tex:2585 + foundations_overclaims_resolved.tex:263. V2-AP27 (duplicated .tex forbidden). Counter: merge canonical content; delete drafts.
- **FM175**: gr-splitting "second proof" not independent. line-operators.tex:214-220 rmk:hKoszul-evidence (iii) claims gr SC^{ch,top} ≅ P_ch ∐ E_1 gives SECOND proof. Identifying gr(C_*(FM)) with P_ch silently invokes Kontsevich formality (same input as first proof) + Poisson/Gerstenhaber split; two "independent" proofs share the same input. Counter: demote to Remark ("alternative perspective"); explicitly name the Gerstenhaber→Poisson collapse.

**Part II RTT / Baxter / coideals:**
- **FM176**: Type-A scope drifts gl_N vs sl_N (typeA_baxter_rees_theta.tex:12 title, 203 lemma `gl_N`, 393 `Y^{RTT}_{≤M}(sl_N)`). Counter: fix uniform notation Y_ℏ(sl_N) with explicit R-matrix naming; scope is legitimately type-A-only.
- **FM177**: "Baxter-Rees family" has no Baxter operator. typeA_baxter_rees_theta.tex:12,820,827,847,922,981,1030 name the family "Baxter-Rees" but construct no Q-operator and verify no TQ = T_+Q + T_-Q relation. "Baxter" is decorative. Counter: rename "weight-Rees spectral-telescope family" OR construct Q + verify TQ.
- **FM178**: thm:pairwise-to-all-point-reconstruction hides slot-commutativity hypothesis (typeA:338-374). "Commutators between disjoint pairs vanish because they act on disjoint tensor factors" (L352) — requires cross-slot Lie-bracket commutativity, stronger than m_k=0 for k≥3. Counter: add slot-commutativity as explicit hypothesis.
- **FM179**: thm:quotient-coideal-descent proves sub-dg-module, claims subcoalgebra (shifted_rtt_duality_orthogonal_coideals.tex:731-755). "Image of dg algebra map is stable under dual differential" — differential stability ≠ coproduct stability (coideal property Δ(C) ⊂ C⊗ambient + ambient⊗C not verified). Counter: weaken to sub-dg-module OR add coideal verification.
- **FM180**: thm:pbw-recurrence tagged ProvedHere but imports Riordan GF externally (casimir_divisor_core_transport.tex:744,784-864). Riordan algebraic equation x(1+x)P² − (1+x)P + 1 = 0 (L820) asserted without derivation. Counter: ProvedElsewhere-layered with Vol I input; "Assuming bar GF = Riordan, ..." status annotation.
- **FM181**: "Orthogonal coideal" terminology collides with Letzter-Kolb (shifted_rtt_duality_orthogonal_coideals.tex title). Def 709, 830: orthogonal = bar-pairing-annihilator. "Orthogonal" suggests B-type / symmetric-pair ι-quantum-groups (Letzter); neither present here. Counter: scope remark disambiguating; alternative name "pairing-annihilator coideal."

### Wave 9-10 supplement (FM182-FM196, Hochschild/brace/holographic + Vol II standalones)

**Hochschild cluster:**
- **FM182**: hochschild.tex:575 unqualified "HH^0" violates AP-CY64 three-Hochschild. "The center Z(A_∂) corresponds to HH^0(A_∂,A_∂)" — which HH^0? ChirHoch vs HH*_mode vs H*_GF. Counter: named sub-lemma "ChirHoch^0_{δ_Q-only}(A_∂) = Z(A_∂)"; drop bare "HH^0".
- **FM183**: Missing named bridge between algebraic (hochschild.tex:98, End^ch_A formal-Laurent) and geometric (hochschild.tex:619, FM_k(C)×Conf_m(R)) chiral-Hoch models. Downstream ProvedHere theorems (bulk_hochschild, bulk-CHC, MC-deformations) switch without a named qi theorem. AP-CY62 repeat. Counter: introduce `thm:chiral-hochschild-models-equivalent` for logarithmic SC^{ch,top}.
- **FM184**: brace.tex:9-11 "terminal local chiral open/closed pair" overclaims. Chiral Deligne-Tamarkin makes Z^{der}_{ch} initial-bulk at E_2-COHOMOLOGY after associator fix; "terminal" asserts chain-level universal property (the open chiral-Deligne-at-chain-level gap). Counter: "universal-at-cohomology after fixing a Drinfeld associator."
- **FM185**: thqg_holographic_reconstruction.tex:1805-1867 ProvedHere across G/L/C/M with "asymptotic convergence for M (rate ≈0.231)." Conflates SHADOW-MC reconstruction (proved all classes as formal series) with BULK = derived centre at chain level (CLAUDE.md: "Global triangle PROVED G/L/C; OPEN class M"). Counter: split into thm:shadow-reconstruction (all classes, formal) and thm:holographic-reconstruction (G/L/C Proved; M Conditional on DS-Hochschild gap).
- **FM186**: thqg_symplectic_polarization.tex:1107-1117 rem:thqg-III-conditionality silently upgrades Conditional to ProvedHere for class M by asserting (H1)(H2) hold for entire landscape via Vol I `prop:standard-examples-modular-koszul`. Verdier nondegeneracy for class M at g≥2 rides on same DS-Hochschild gap. Counter: restrict landscape remark to G/L/C at g≥2.
- **FM187**: hochschild.tex:410-412 Kel06+BZFN10 cited to give Z_der(C_∂) → C^•_ch(A_∂,A_∂). Kel06 gives CLASSICAL HH of End(b); chirality upgrade (AP-CY67 spectral provenance) elided. Counter: two-step derivation — Kel06 gives HH^•(A_∂) classical; then chirality via local-global FM identification.
- **FM188**: hochschild.tex:516-548 triple conflation. HH^•(A_∂) ≃ O(T^*[-1]L_b) ≃ O(M_vac)|_{L_b} as consequence of thm:CDG_compatibility(iii). (i) "HH^•" unqualified (AP-CY64); (ii) CDG(iii) is only PVA morphism, not HKR; (iii) chain vs cohomology unstated. Counter: cohomological proposition after global-triangle datum; chain-level → Conjectured for class M.
- **FM189**: brace.tex:96-103 brace identities cite Stokes on FM + Arnold without associator disclosure. rem:brace-strict-coordinates honestly concedes brace is "convenient strict presentation" but downstream ProvedHere uses strict braces as canonical. Counter: promote remark to numbered Convention; cite at every strict-brace appeal. (FM158 repeat for braces.)

**Vol II standalones (bar_chain_models, preface_full_survey, stokes_gap_kzb_regularity, class_m_global_triangle, etc.):**
- **FM190**: bar_chain:300,182-186 conflates geometric vs algebraic chiral Hochschild (AP-CY64 repeat); invokes classical Deligne (for E_2 topological Hochschild) for chiral E_2. Counter: state ChirHoch model explicitly; chiral Deligne at chain level is CONJECTURAL.
- **FM191**: bar_chain:350,368-378 thm:topologise tagged ProvedHere for KM, but surrounding prose scope-creeps to "all W via DS" and "all freely-generated PVAs" — both CONJECTURAL per Vol II CLAUDE.md AP153/FM81/FM82. Counter: keep theorem scope to KM non-critical; use remark for conjectural extensions.
- **FM192**: stokes_gap_kzb_regularity:57-60,199-200 target "all genera" KZB Stokes reduction hides a SECOND conjecture: R(z)-twisted clutching and curved-Dunn H² (FM58/FM67). Counter: state both conjectures explicitly; downgrade "reduces to" to "conditional on two open problems."
- **FM193**: class_m_global_triangle:108-119,158-163 "weight-by-weight HPL gives total-complex qi" — FM65/AP157 pattern. Weight-level rationality ≠ total convergence + collapse. Convergence argument absent. Counter: state level-level vs level-sum convergence gap explicitly.
- **FM194**: bar_chain:675,720-722,764 Schiffmann-Vasserot coproduct is RECONSTRUCTED (matched to the SV theorem as consistency check) but framed as "produced" by the framework. AP155 overclaiming. Counter: "reproduces the SV coproduct as consistency check" — the framework does not independently construct it.
- **FM195**: bar_chain:198,730 cite [Theorem A]{Vol I} as authority for bar-cobar; actual Vol I Theorem A is the ordered bar coassociative coalgebra statement (per Wave 1, now known to have FORM-A/FORM-B split via FM69). Wrong-theorem citation (AP5 cross-volume violation). Also label thm:bv-bar-coderived cited without verification the label exists. Counter: cite correct Vol I theorem; grep-verify all cross-volume labels.
- **FM196**: bar_chain:155-168 β_{M,N}(z) = R(z)·σ conflates spectral parameter with E_2 categorical braiding (FM54/AP-CY25 repeat). Counter: spectral R(z) is a family over z; categorical braiding is a single nat. transformation; identification requires additional theorem, not definition.

(Bonus: README of Vol II lists "ordered_associative_chiral_kd" as a standalone but file is NOT present on disk — metadata drift. Counter: remove from README status table OR produce the file.)

### Wave 11 supplement (FM197-FM206, Vol I N-paper series)

- **FM197**: N1 (vii) "factorization homology concentrated in degree 0 for all g" listed "unconditional"; actually uniform-weight g=0 only. g≥2 has curvature obstruction d²=κ·ω_g (AP32/FM67). Counter: tag (vii)/(viii) "uniform-weight g=0 unconditional; g≥2 scalar-lane only."
- **FM198**: N1 "twelve equivalences" / "ten unconditional" overclaim. Core 5 + 5 conditional + 2 conjectural after AP32 scope. (FM83 pattern: same as Koszulness "fourteen equivalent" standalone.) Counter: honest count "core-5 + 5 conditional + 2 conjectural."
- **FM199**: N2 MC3 All Types — proves evaluation-generated core only (AP47). Non-path sectors for E_8 open per Wave 3 strictification (FM93). Abstract should say "for the eval-generated core of DK_g." Counter: retitle "thick generation on eval-generated core of DK_g."
- **FM200**: N3 "dg Lie on pseudo-tensor codomain" — g^{E_1} := ∏ Hom(M_Ass(g,n), End_A(n)) claimed dg Lie from ribbon Feynman transform. Chiral algebras form pseudo-tensor (FM56), not symmetric monoidal; Hom^{cyc} is not obviously dg Lie without proving convolution closure. GetzlerKapranov98 proves COMMUTATIVE Feynman transform, not ribbon. Counter: restrict to scalar lane / genus 0 tree level; or prove ribbon convolution closes.
- **FM201**: N3 "five theorems A-D,H lift to ordered" — only Theorem D explicitly computed. AP150 confabulation-risk. Counter: prove each lift individually or downgrade to "Theorem D lifts; B, C, H conjectural."
- **FM202**: N4 V_k(g) "strong completion tower" axiom (4) requires mu_0 ∈ F^2; double-pole J^a J^b OPE central term is scalar central cocycle NOT in F^2. Axiom (4) fails literally unless curved A_∞ with mu_0 = κ_dp absorbed. Counter: rename "curved strong completion tower"; state mu_0 = κ_dp as curvature datum.
- **FM203**: N4 W_{N+1} → W_N projection "forgets generator of weight N+1 ... strict morphism" without OPE-closure verification. Counter: either prove OPE of weight-≤N generators closes without weight-(N+1), or replace "strict" with "up to homotopy."
- **FM204**: N4 Rem 7.4 "Twenty-one standing conjectures resolved" — no catalogue. AP155 grandstanding. Counter: produce explicit list or delete the claim.
- **FM205**: N5 Vir OPE-growth bound |C| ≤ K(n+1)^2 uses N=2; cubic central term c·m^3/12 in [L_m, L_n] suggests N=3 is required for safety. Counter: use N=3 polynomial bound.
- **FM206**: N6 "Class M consists of intrinsically non-formal algebras" — AP14 conflation. "Non-formal" ambiguous between SC-formality (all families Koszul; only class G SC-formal) and L_∞-formality on g^{mod,(0)} (the genus-0 convolution dg-Lie). Counter: write "L_∞ non-formal on g^{mod,(0)}"; shadow coefficients S_4=10/(c(5c+22)) uncited (AP28/AP43) — add independent verification or ProvedElsewhere[Lorgat26I].

### Wave 10 supplement (FM207-FM213, DNP + rosetta + half-space BV)

- **FM207**: rosetta_stone.tex:2039-2041 misattributes Vol II label `thm:Koszul_dual_Yangian` (actual location: spectral-braiding-core.tex:1827) as Vol I. One of Wave 1 memory's "3 fabricated cross-volume citations"; persisting despite prior correction pass. Counter: delete "Volume~I," prefix; leave `\ref*{thm:Koszul_dual_Yangian}` Vol II-local.
- **FM208**: dnp_identification_master.tex:247 thm:vol2-seven-faces-master tagged ProvedHere but F3 (g=0 only), F4 (W_N conjectural), F5/F7 (non-critical only) — 4+ conditional clauses. AP40 violation: outer env tag dominates citation indexing. Counter: replace with `\ClaimStatusProvedHereConditional` OR split into proved/conjectural theorems.
- **FM209**: affine_half_space_bv.tex:1548-1564 prop:affine-is-log-SC claims "BV-BRST complex of affine PV sigma model IS a logarithmic SC^{ch,top}-algebra." Vol II pitfall AP165/FM40 enforced: SC^{ch,top} lives on the PAIR (Z^{der}_{ch}(A), A), NOT on A itself. Counter: rephrase as "the pair (Z^{der}_{ch}(V^{Keff}), V^{Keff}) is a log SC^{ch,top}-datum via Thm H."
- **FM210**: dnp_identification_master.tex:11-21 opener claims "seven equivalent realizations" uniformly while master theorem per-face qualifiers differ. Construction/narration: unqualified opener promotes conjunction of qualified claims to unqualified coincidence. Counter: "on the common locus (g=0, non-critical, classical simple g)".
- **FM211**: dnp_identification_master.tex:94-97 "Non-renormalization = Koszulness ... IS the E_2-collapse of the bar spectral sequence." DNP Thm 4.1 proves one-loop exactness; programme proves E_2-collapse. "IS" identifies two propositions without a comparison theorem. Counter: "conjecturally corresponds to"; tag as Conjectured until bridge lemma is written.
- **FM212**: ht_physical_origins.tex:444-456 thm:cl-n4-chirality ProvedElsewhere[CL16] claims KM chirality from N=4 SYM. CL16 builds HT twist + factorization algebra; D-module descent to Ran(X) needs CDG20/Zeng23, not CL16 alone. Counter: add `\cite{CDG20,Zeng23}` alongside `\cite{CL16}` or narrow scope.
- **FM213**: Missing file chapters/connections/thqg_open_closed_realization.tex (phantom). ht_physical_origins.tex:379 points to it; no chapter of that name exists. AP38 phantom-label retirement pattern. Counter: create stub or reroute pointers across preface/concordance.

### Wave 10 supplement ctd. (FM214-FM223, Vol II preface + introduction)

- **FM214**: Universal IS-claim without scope. preface.tex:26-39,1606,1765,1811 + intro.tex:24-28 repeatedly write "derived chiral centre of a boundary algebra IS the bulk algebra of a 3d HT gauge theory" — omits boundary-linear-only qualifier (class G/L/C proved; class M OPEN per FM126). Counter: lead every IS-claim with "On the boundary-linear exact sector (classes G/L/C), Z^der_ch(B_∂) ≃ A_bulk; class M conjectural."
- **FM215**: Internal contradiction with own FM82. preface.tex:187-210,1820,2348 Stage 9 declared "proved for affine, DS/W, and freely-generated-PVA lanes" (including Vir, W_N = class M), citing rem:E3-top-free-PVA-scope. FM82 (this file) explicitly: class M quartic poles incompatible with KZ polynomial λ-brackets. Counter: verify Vir `gr_Li` is KZ-admissible in an independent lemma; otherwise scope Stage 9 to G/L/C.
- **FM216**: Chriss-Ginzburg "precise parallel" (preface.tex:622-650) — 7-row table, zero rows carry equivalence theorems. Springer↔Lagrangian, KL-basis↔α_T, KL polynomials↔shadow tower are metaphors. AP155. Counter: retitle "Structural analogy"; per-row metaphor-vs-theorem footnote.
- **FM217**: intro.tex:1473-1525 list-before-prove (AP109). ~1500-char paragraph chains complementarity + algebraicity + formality identification + shadow depth + discriminant, each with distinct Vol I hypotheses. Connective "also", "becomes", "explains" hides scope conditions. Counter: split into 4 paragraphs; state scope per piece.
- **FM218**: "Only" universal quantifiers (preface.tex:64 "only language"; preface.tex:1561 "only with all five assembled does gravitational theory become computable"). Part VI's genus-0 gravity uses a subset. Counter: drop "only"/"only language."
- **FM219**: Preface inherits FM158 strictness overclaim (preface.tex:801-803). Kontsevich formality φ: C_*(FM_•(C)) → E_2 implicitly strict; actually ∞-quasi-iso with Drinfeld associator. Counter: fix upstream (line-operators.tex Step 2).
- **FM220**: Internal contradiction on modular-operad status WITHIN preface. preface.tex:1597 (early ladder) "full modular extension to genus ≥ 1 remains open"; preface.tex:1976-1980 (Frontier v) correctly "composition proved integral, Stokes gap only generic non-integral" (FM68). Same document, two different statuses. Counter: align early ladder to Frontier formulation.
- **FM221**: Spectral-vs-categorical conflation in preface (preface.tex:881-882 "two parallel lines interact through the bulk, producing the meromorphic braiding"). thm:affine-monodromy-identification is on EVALUATION-MODULE CORE only (AP47). FM54 repeat. Counter: "restrict to evaluation-module core; cite thm:affine-monodromy explicitly."
- **FM222**: Preface's declarative conjecture. preface.tex:1849-1852 "derived centre of line category recovers bulk" stated as declarative; conjectural tag appears 3 sentences later. AP40 violation. Counter: "is conjectured to recover (conj:...)".
- **FM223**: Triple repetition of "complete" strictification (preface.tex:408, 1263, 1479). Theorem real but "complete every simple Lie type" without qualifier — Wave 3 found E_8 non-path sectors OPEN (FM93). AP155 + AP109. Counter: keep one statement; replace others with "rank-1 rigidity-based path-sector strictification."

### Preface positive findings (no FM needed)

- FM56 clean in preface (no "symmetric monoidal category of chiral algebras").
- AP29 em-dashes clean (zero "Moreover/Notably/Crucially/Remarkably/We now" hits).
- AP151 hbar usage consistent.
- AP126 r vs k=0 treated correctly, including Sugawara-shift explanation for κ(g_k) at k=0 (preface:1269-1272).
- AP136 κ(W_N)=c(H_N-1) verified at N=2 → c/2.

### Wave 11 supplement ctd. (FM224-FM229, compute library decorator audit)

**Critical coverage stat: 0 / 1134 Vol II ProvedHere claims have `@independent_verification` decorators installed. `make verify-independence` returns PASS (no tautologies, no orphans) but 100% coverage gap. Infrastructure green; campaign not started.**

- **FM224**: Decorator campaign at 0%. `make verify-independence` reports "coverage gap: 1134 claims without independent verification." Running commentary in CLAUDE.md has said Vol II snapshot was 0 / 1134 at installation; no change since. Counter: install decorators for the top 5 climax theorems first (see list in Independent Verification Protocol section); gate any new ProvedHere by decorator presence.
- **FM225**: Pre-existing V2-AP28 tautology live in test suite. `compute/tests/test_adversarial_verification.py:712-719` hardcodes `expected = [Rational(1,24), Rational(7,5760), Rational(31,967680)]` compared DIRECTLY against `modular_completion_koszul('abelian_cs', ...)`. Direct FRAME_SHAPE_DATA analogue from Vol III. V2-AP28 already showed engine+test moved together when λ_3 was corrected 1/82944 → 31/967680 — the bug THIS protocol was designed to prevent is still live. Counter: recompute expected F_g values from Arakelov heat-kernel / zeta-regularised determinant inside the test; do not use engine-output-style hardcoding.
- **FM226**: Dictionary self-consistency test masquerading as theorem. `compute/tests/test_exceptional_affine_bar.py:446-451` `test_generator_weights_from_exponents` reads `_EXCEPTIONAL_E_DATA[name]['exponents']` (same dict engine reads) and computes expected as `[e+1 for e in data['exponents']]`. Tests dict self-consistency, NOT the Feigin-Frenkel W-algebra weight theorem. Bourbaki citation in docstring is aspirational (AP-CY24 docstring confabulation). Counter: derive expected weights from Kac's classification independently; or use engine output from a different code path.
- **FM227**: Eight engines without tests — `ainfty`, `arnold`, `convention_check`, `fm_boundary`, `genus2_ordered_bar`, `laplace_bridge`, `spectral`, `symbolic_stasheff`. Highest-stakes: `genus2_ordered_bar` (underpins curved-Dunn claims at g=2) and `spectral` (spectral parameter handling for R(z)). Counter: prioritize these for test scaffolding; install decorators tied to independent external anchors.
- **FM228**: Archival tests as AP28 danger zone. Tests with no engine counterpart (21 total): `cross_engine_consistency`, `infrastructure`, `signs`, `conventions` are legitimate integration tests; but `session_results`, `adversarial_verification` are result-archival tests with hardcoded numerical values. Class (ii) pattern where hardcoded values become decorated tautologies if auto-applied. Counter: audit archival tests line-by-line; each hardcoded value needs `# VERIFIED` comment citing independent source (AP10/AP128 protocol) or must be removed.
- **FM229**: `convention_check` engine itself lacks a test. Meta-irony: the module that enforces convention consistency has no convention check applied to it. Counter: write a test of the test harness itself (self-verification).

### Top 5 decorator-install priorities (for coverage campaign)

1. `thm:E3-topological-km` — CFG arXiv:2602.12412 (BV-quantised Chern-Simons trace).
2. `thm:E3-topological-DS-general` — Costello-Gaiotto holomorphic CS with DS boundary (also: FM81 scope restriction).
3. `thm:E3-topological-free-PVA` — Khan-Zeng 3d Poisson sigma model (also: FM82 scope restriction to G/L/C only).
4. `thm:global-triangle-boundary-linear` — Lurie HA 5.3.1.30 (BZFN) (also: FM126 stale label).
5. `thm:modular-bar` D²=0 — Getzler-Kapranov modular operad axioms (FM61/FM68/FM92 scoping).

### Wave 11 supplement ctd. (FM230-FM239, Vol I survey papers)

- **FM230**: Heisenberg labeled "pole-free commutative" (survey_track_b_compressed.tex:179-183 Tier (a)). Own body L221: "α(z)α(w) ~ k/(z-w)^2" — DOUBLE pole. V2-AP7: Heisenberg R-matrix = exp(k·ℏ/z), NOT trivial. Self-contradicting classification label. Counter: rename tier (a) "scalar-R abelian"; drop "pole-free" across survey and Track B.
- **FM231**: CY-A_3 abstract/body self-contradiction. programme_summary.tex:98 abstract: "single open conjecture is CY-A at d=3"; :2599 body: `\begin{theorem}[CY-A at d=3]`. Vol III AP-CY11/AP-CY14: PROVED inf-cat (2026-04). Counter: unify abstract and body — "CY-A_3 proved inf-cat; CY-C open"; strike "single open conjecture" phrasing.
- **FM232**: Vol II/III climax content attributed to Vol I survey. survey_modular_koszul_duality_v2.tex:203-216 advertises "3d quantum gravity climax ... Calabi-Yau quantum groups ... CoHA ... 6d holomorphic Chern-Simons" as Vol I content; actually Vol II Part VI (3d gravity, FM126) and Vol III (CY QG). Counter: strike or tag "previewed; proved in Vol II/III" in survey v2 abstract.
- **FM233**: Pole-free label self-contradiction in Track B (survey_track_b_compressed.tex tier (a)). Classifies Heisenberg + lattice VOAs as "pole-free" yet Track A pole-absorption (survey_v2:381) shows OPE double pole → r(z) simple pole. Not pole-free at either level. Counter: rename "abelian-R scalar" tier.
- **FM234**: "Interpolate" across E_∞/E_1 gap (introduction_full_survey.tex:142). "KM, Virasoro, W, lattice interpolates between Heisenberg and Yangian." V2-AP1 / locality hierarchy: Heisenberg, KM, Virasoro, W, lattice are ALL E_∞; Yangian is E_1. Not a continuum. Counter: "span pole-structure gradation within E_∞; Yangian sits outside as E_1."
- **FM235**: AP152 ordering conflation (introduction_full_survey.tex:141). "Simple poles give collisions a canonical ordering." FM50: E_1 ordering is OPERADIC (operations depend on sequence), not geometric from pole structure. Counter: "simple poles yield Lie bracket; E_1 operadic ordering is independent datum."
- **FM236**: "Unconditional for every family" without AP32 scope tags (survey_v2:646, 920, 1084, 1434, 1805 etc.). AP32 requires every obs_g/F_g/λ_g to carry (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Counter: tag every occurrence.
- **FM237**: "120K+ tests" vs 2 independently-decorated claims. programme_summary.tex:101: "120K+ tests; 4,542 pages." Actual: ~3900 test modules across 3 volumes; 2 independently-decorated claims total (Vol III snapshot 2/283 at installation; Vol II 0/1134 per FM224; Vol I 0/2275). Counter: "~3900 test modules comprising ~120K assertions; 2 decorated claims under Independent Verification Protocol (baseline)."
- **FM238**: Bare κ in programme_summary:1931 "κ(A_C) = χ^CY(C)." AP113 bans bare κ. For CY_d with d=2, h^{1,0}=0: κ_ch = χ(O_X) (AP-CY34); at odd d or h^{1,0}>0 this fails (FM127-like but Vol III). Counter: κ_cat or κ_ch with explicit d, h^{1,0} hypothesis.
- **FM239**: §14 dropped by both compressed tracks. Full programme_summary v1 has §1-14; Track A covers §1-6 + §9; Track B covers §7, §8, §10-13. §14 "Overview of the frontier" absent from both. Counter: add footnote in each track: "§14 frontier overview lives in programme_summary.tex."

### Wave 12 supplement (FM240-FM247, spectral-braiding-core deep dive)

(File located at chapters/connections/spectral-braiding-core.tex, 4950 lines — not in theory/ as Wave 12 launch assumed. FM155/FM156 confirmed present at L3730 with specific line anchors.)

- **FM240**: Half-braiding narration without construction. spectral-braiding-core.tex:444-446 + thm:braided-category Part A (L280-284) narrate AP-CY25 corrected ontology ("R(z) acts as a braiding") without CONSTRUCTING σ_L(z) explicitly. Downstream thm:braided-category assumes β_z "as a natural isomorphism arising from exchange of insertion points." Counter: insert explicit half-braiding σ_A(z)(a⊗n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)} before thm:braided-category.
- **FM241**: thm:Koszul_dual_Yangian Step 6 (L1883-1888) "This is a rewriting of YBE obtained by substituting R(z) = exp(r(z)) and expanding" — FALSE. Classical co-YBE is an INDEPENDENT axiom: requires YBE + intertwiner Δ^op = R·Δ·R^{-1} + coassociativity. Three ingredients collapsed into "rewriting" downgrades ProvedHere. (Good news: all three ingredients ARE present in the chapter — YBE Thm 3, intertwining Step 3, coassoc Step 3.) Counter: rename Step 6 "Co-YBE compatibility"; cite three ingredients separately.
- **FM242**: Step 7 L1892 pole universalisation. "associated graded ... r(z) ~ r_0/z (simple pole)" stated universally. Class M (Virasoro) has quartic OPE pole. Yangian signature = simple pole r-matrix (Drinfeld); class M inherits higher poles. Counter: scope "for the affine lineage"; flag pole-order dichotomy.
- **FM243**: def:E2-chiral-algebra L469-472 "E_2 structure arises from Deligne conjecture applied to chiral Hochschild cochains" — no chiral-vs-topological qualifier. AP-CY62/63. Counter: specify "chiral Deligne (Francis 2012 / Costello-Gwilliam Vol 2)."
- **FM244**: thm:genus-tower-asymmetry (ii) L3815-3828 "Open color is flat at ALL genera" conflates (a) operad-flatness (E_1 has contractible parameter spaces, true) with (b) bar-flatness (every SC^{ch,top}-module bar). "No open-to-closed" protects the operad, not every module structure. AP150 multi-step. Counter: separate operad flatness from bar flatness.
- **FM245**: def:E2-chiral-algebra L473-478 "E_2 ≃ E_1^{hol} ⊗ E_1^{top}" stated as unqualified global Dunn decomposition. Dunn requires a polarisation; global on arbitrary X requires factorisation gluing. Counter: insert "locally on formal disks."
- **FM246**: thm:Koszul_dual_Yangian L1833-1835 cites DNP25 Thm 5.5 as "established independently, self-contained proof below"; self-contained proof then mixes classical Drinfeld Yangian (DNP25 covers) with A_∞-shifted enhancement (arities ≥ 4 hand-waved via "W(SC^{ch,top})-module structure"). Counter: split into (a) classical = DNP25 ProvedElsewhere, (b) A_∞-shifted refinement ProvedHere with explicit arity-4+ coherences.
- **FM247**: spectral-braiding-core confirms FM155 + FM156 with sharper anchors. Phantom `prop:sc-koszul-dual-three-sectors` cited at L3730 (two \ref sites: here + bv_brst.tex:2059, zero \label across chapters/). "Com^!=Lie" category error at L3730 — closed colour of SC^{ch,top} is E_2 (FM_k(C)), not Com; E_2^! ≃ E_2^{shifted} (self-dual up to shift, Gerstenhaber linearisation). Counter: already in FM155/FM156 repairs.

### HEAL-MODE DIRECTIVE (2026-04-16, from author)

**Every FM counter must target the STRONGEST honest form, not a downgrade. If the strongest claim is TRUE (the "ghost theorem" of the first-principles triple), the repair is to PROVE it — supply the missing construction, cite the correct reference, write the missing lemma. "Downgrade to Conjectured" is only the repair when no proof path exists. Technical malpractice (wrong citation, missing lemma, ambient mis-specification) is not grounds for weakening the claim — it is grounds for FIXING the proof.**

Reread existing FMs through this lens:
- FM69 (Thm A ambient): FORM-A (symmetric) goes through LV12; FORM-B (ordered E_1) is the stronger claim and needs its own proof via factorization algebras on Ran(X) (Francis-Gaitsgory 2012). Prove FORM-B, do not split-and-downgrade.
- FM87 (phantom genus1-twisted-tensor-product): write the proposition with Gauss-Manin uncurving explicit. Strongest form survives.
- FM155/FM247 (phantom sc-koszul-dual-three-sectors): supply Vallette coloured Koszul duality computation. Strongest form survives.
- FM157 (Liv06 mis-binding): cite Hoefel + Hoefel-Livernet correctly. Strongest claim (homotopy-Koszulity of SC^{ch,top}) survives.
- FM81 (thm:E3-topological-DS-general non-principal): supply ghost-bilinear bulk-antighost lift example-by-example for BP, min sl_4; strongest form of "all W via DS" may survive.
- FM82 (class M free-PVA): verify Vir `gr_Li` is KZ-admissible; if it is, FM215 contradiction resolves AND Stage 9 stands for class M.
- FM214 (universal IS-claim): prove bulk=derived center at chain level for class M via the DS-Hochschild compatibility bridge; strongest "Z^der_ch(A) = bulk" survives unconditionally.
- FM224 (0/1134 decorators): install; strongest verification posture is achievable.

### Wave 12 supplement ctd. (FM248-FM257, derived Langlands + spectral sequences + existence criteria) — HEAL-FRAMED

- **FM248**: spectral_sequences.tex:411 prop:central-charge-d1(i) uses κ(Vir_c)=c/2 to force κ=0 from c=0; other families (Heisenberg κ=k at c=1; triangle algebras c=0, κ≠0) have κ ≠ c/2 (AP39). Ghost theorem: for algebras with κ(A)=0, d_1=0 and s.s. degenerates at E_1 — this holds universally. Heal: replace "c=0" with "κ(A)=0" hypothesis. Strongest universal form survives.
- **FM249**: prop:degen-koszul (spectral_sequences.tex:328-352) E_2 collapse needs bar degree = internal weight bigrading; curved Koszul at non-critical level fails. Ghost: Koszul + weight-graded ⇒ E_2 collapse. Heal: state weight-graded hypothesis explicitly; claim survives for all standard-landscape algebras (Heis, KM, Vir, W_N, lattice — all weight-graded).
- **FM250**: thm:oper-bar-dl (derived_langlands.tex:594-703) claimed "all n ≥ 0"; FT06 publishes n ≤ 2; n=3 closed via independent d_4 transgression argument; n ≥ 4 open (FT06 Conjecture 1.5). Heal: prove n=3 independently (chapter has the transgression argument, just needs un-circularising); invite the FT06 n ≥ 4 upgrade. Strongest n=3 form survives; n ≥ 4 is the genuine research frontier.
- **FM251**: thm:kl-bar-cobar-adjunction (derived_langlands.tex:1121-1221) Step 4 uses Koszul purity at admissible level — exactly what conj:periodic-cdg asserts is OPEN. Two independent repair paths: (i) prove conj:periodic-cdg (this would close semisimplified KL globally — major result); (ii) state adjunction at generic k, with admissible level conditional on periodic-cdg. Strongest form: close conj:periodic-cdg.
- **FM252**: existence_criteria.tex framework is QUADRATIC/BD-pseudo-tensor; Yangian ROW mis-frames E_1-chiral as "filtered". Yangian escapes the ambient operadic category (V2-AP1, V2-AP6). Heal: extend existence-criteria to cover E_1-chiral Koszul duality on equal footing; the two-column (E_∞ BD + E_1 ordered) existence criterion is a stronger theorem than either alone.
- **FM253**: existence_criteria.tex:470, 338-358 "Vir_{26-c} same-family shadow" uses 26 (matter-ghost convention); Koszul shadow is 13-c (AP8 explicit). Heal: use both conventions with clear labels — 13-c is the Koszul-dual operadic involution; 26-c is the matter-ghost critical central charge. Both are REAL and DIFFERENT; stating both sharpens the theorem.
- **FM254**: derived_langlands.tex:58-60 "unique homological framework." Multiple d²=0 frameworks reach the same oper package (FF Sugawara, Arakawa W-BRST, chiral Hochschild via BD pseudo-tensor). Heal: replace "unique" with "canonical" or "maximally economical"; this is a stronger positioning than "unique" because it can be proved (the alternatives factor through the programme's framework).
- **FM255**: spectral_sequences.tex:319 "FM_2(A^1) ≅ A^2" ambiguous between algebraic blow-up (itself) and real FM / Deligne-Mumford FM. Heal: specify the real FM model; the log-de-Rham computation works for the real model. Strongest form survives with explicit model.
- **FM256**: spectral_sequences.tex:584-589 Adams s.s. analogy without ClaimStatus tag, Steenrod↔chiral-endomorphism functor, or primary-op↔d_1 construction. Heal: CONSTRUCT the Steenrod-analog functor on chiral endomorphism operad. If it exists (and it should for admissible level KM), this would be a major independent result — the analogy becomes a theorem.
- **FM257**: existence_criteria.tex:208-213 Cofree(sV*) conilpotency check is circular (construction produces T^c, conilpotency automatic). Heal: rename T^c; replace conilpotency with finite cogeneration in each weight. The existence criterion remains true; the check is made non-circular and hence VERIFIES the strongest form.

### Campaign summary (post-pivot)

The adversarial sweep surfaced 181 distinct mistakes, most of which are TECHNICAL MALPRACTICE (mis-citations, phantom labels, absent lemmas, scope-inflation prose, circular proofs) rather than mathematical overclaiming. The STRONGEST HONEST FORM of the Vol I + Vol II programme survives most of them once the technical work is done: supply missing constructions, cite correct references, derive explicit bridges, install decorators. Genuine frontiers remaining after heal: (i) curved-Dunn H²=0 at g≥2 bridging modular-bootstrap H²=0 (FM67); (ii) class M chain-level E_3 + DS-Hochschild compatibility (FM126); (iii) FT06 H^n at n≥4 for opers; (iv) conj:periodic-cdg for KL at admissible level; (v) chain-level chiral Deligne-Tamarkin for SC^{ch,top} pentagon edge (2↔3). These are research-level opens, not malpractice.

## HEAL-SWEEP (2026-04-16, supersedes all prior downgrade counters)

**Directive (author 2026-04-16):** "NOT interested in tolerating downgrades of scope or gravity or impact of claims simply due to technical malpractice. If it is possible to prove the strongest result, we will realize that."

The registry's "Counter" fields were written in attack-mode (what to weaken). This section inverts the ~30 most impactful downgrades into STRENGTHENING paths — the construction, lemma, or citation that realizes the strongest form instead of weakening the claim. For each original FM, the prior "Counter" is now SUPERSEDED unless a genuine impossibility is stated.

### Backbone theorems (A, B, C, D, H, E_3-topologization)

- **FM69 → HEAL**: Theorem A at full strength. Prove FORM-B (ordered E_1 bar) via Francis-Gaitsgory factorization algebras on Ran(X) under ⋆-tensor (GR17 IV.5) PLUS R-twisted Σ_n-descent preserves weak equivalences. Both forms proven; "E_1 primacy" headline stands unconditionally. Do NOT split-and-downgrade.
- **FM75 → HEAL**: "generic c/k" euphemism. Prove bar-cobar inversion at minimal-model and admissible loci directly — Arakawa's C_2-cofiniteness gives simple-quotient semisimplicity; Adamović's admissible-level framework gives conilpotent completion. Inversion holds everywhere without exception.
- **FM76 → HEAL**: Vir_{c_{p,q}} simple quotient classification. Shadow tower on simple quotient is computed as universal tower MODULO null-vector ideal; null vectors contribute EXTRA bar differential terms, do not kill shadow class. Class M stands for Ising and all minimal models (Saveliev-Arakawa gives explicit null-vector-corrected S_r).
- **FM80 → HEAL**: Theorem H at critical level. State Thm H in two flavours: (a) concentration in {0,1,2} at non-critical; (b) Feigin-Frenkel regime at k=-h^v where ChirHoch^0 = Feigin-Frenkel center (infinite-dim polynomial algebra on opers), higher ChirHoch^n controlled explicitly. NOT an exclusion — a companion theorem.
- **FM81 → HEAL**: thm:E3-topological-DS-general at non-principal nilpotents. Construct ghost-bilinear bulk-antighost lift case-by-case for BP, minimal sl_4, subregular — chapter already has the Kazhdan-grading framework; extend via Jacobson-Morozov triples' half-integer weights absorbed into fractional ghost CDG. Theorem stands for ALL good-graded nilpotents, not just principal.
- **FM82 → HEAL**: thm:E3-topological-free-PVA for class M. Verify Vir gr_Li PVA is KZ-admissible — class M's quartic OPE poles descend to gr-PVA with polynomial λ-brackets (Li-filtration separates pole order from PVA λ-degree). Khan-Zeng applies to Vir; Stage 9 stands for class M.
- **FM108 → HEAL**: DS L→M for all simple g. Principal-DS proof extends to non-principal via the Frenkel-Kac-Wakimoto principle (kappa formula is level-shift invariant under DS reduction regardless of Kazhdan grading). Type-A low-rank computation is evidence of a general theorem waiting to be written.
- **FM126 / FM185 / FM186 / FM214 → HEAL (unified bridge)**: close the DS-Hochschild compatibility bridge. For class M, the bulk = derived center at chain level follows from (a) Costello-Gaiotto holomorphic CS with DS boundary (already FM57), (b) explicit HKR-type identification HH^*(A_DS) ≃ O(derived M_vac), (c) DS-bar intertwining (Vol I thm:ds-koszul-intertwine, Bridges table). Once the bridge is written, the global triangle + symplectic polarization + holographic reconstruction + universal IS-claim become unconditional at class M. SINGLE PROOF closes FM126, FM185, FM186, FM214.

### Modular operad + curved Dunn + higher genus

- **FM67 / FM88 → HEAL**: curved-Dunn H²=0 at g≥2 bridging modular-bootstrap H²=0. Construct the bridge chain map explicitly: modular-bootstrap complex's vanishing passes to curved-Dunn complex via the gauge-fixed convolution model. Cross-genus MC equation stands unconditional. This is the single frontier with highest-impact heal.
- **FM84 / FM86 → HEAL**: W_3 g=2 formula (c+204)/(16c) + multi-weight (obs_g)²=0. Supply cross-channel δF_g^cross vanishing via graph-sum contraction on the multi-weight lattice; obs_g nilpotence is ALL-WEIGHT, not just UNIFORM.
- **FM87 → HEAL**: phantom label prop:genus1-twisted-tensor-product. Write the proposition with explicit Gauss-Manin uncurving — the genus-1 twisted Künneth follows from Λ²H^1 ⊗ curvature + Arakelov pairing. Proved statement, not phantom.
- **FM91 / FM92 → HEAL**: concrete operadic composition at all genera. Apply curved-Dunn bridge (FM67 heal) + KZB-regularized Stokes regularity at M̄_{g,n} boundary divisors via the Jimbo-Miwa irregular-singular framework. Modular operad composition PROVED at generic non-integral level.

### Operadic + SC^{ch,top} pentagon

- **FM155 / FM156 / FM247 → HEAL**: phantom sc-koszul-dual-three-sectors + Com^!=Lie category error. Write the proposition with Vallette coloured Koszul duality computation; closed sector is E_2^! ≃ E_2^{shifted} (Tamarkin self-duality), NOT Com^!=Lie. Three-sector structure (E_2 closed, E_1 open, trivial mixed) is proved via Ginzburg-Kapranov + Künneth for colored operads with empty cross-arrows.
- **FM157 → HEAL**: Liv06 → Hoefel/Hoefel-Livernet rebinding is pure citation fix; homotopy-Koszulity of SC^{ch,top} stands. Already heal-oriented.
- **FM158 / FM219 → HEAL**: Kontsevich formality as ∞-quasi-iso with Drinfeld associator. Name the associator; Tamarkin zigzag transfers homotopy-Koszulity rigorously. Strict presentation is achievable via Fresse-Vallette operadic model structure + fixed associator.
- **FM159 → HEAL**: SC^{ch,top} ⊂ Voronov's SC via product-collapse. Prove the product-collapse qiso SC^{ch,top} → SC_Vor is a map of homotopy operads explicitly (Künneth for homotopy operads). Koszulity transfer is then rigorous.
- **FM160 → HEAL**: QME ↔ MC at chain level. Fix gauge (semifree model) + apply homotopy transfer; chain-level identity is obtained, not just quasi-iso class.

### Yangians + spectral braiding

- **FM161 → HEAL**: Y(g) Koszulness in Positselski nonhomogeneous framework. Replace PP05 connected-grading with filtered-CDG-Koszul framework properly. Strongest form: filtered Koszul deformation of U(g[t]) for ALL simple g (classical + exceptional).
- **FM162 → HEAL**: Exceptional-type PBW. Cite Guay-Regelskis-Wendlandt 2018 (arXiv:1706.05176) for E_6-E_8, F_4, G_2. "Any simple g" claim stands.
- **FM163 → HEAL**: Y(g)^! = Y(g)^{ℏ→-ℏ}. Supply all-order R^{-1} comparison via trace pairing; Chevalley-involution + ℏ-flip combine as an explicit dg-bialgebra automorphism.
- **FM167 → HEAL**: Y(g)^! = Y(g^v) non-simply-laced. Prove via Finkelberg-Tsymbaliuk's quantum geometric Langlands at Yangian level (the framework is set up for non-simply-laced; the theorem is the natural extension).
- **FM166 → HEAL**: Jones from ordered-E_1 bar. Show that the RT functor on MTC quotient at roots of unity factors through the ordered E_1 bar complex via negligible-ideal kernel = bar-computable quotient. Jones comes from ordered E_1 bar after level specialization + MTC quotient — BOTH operations factor through the bar.
- **FM168 / FM169 → HEAL**: Gravitational Yangian Hopf structure. Construct the antipode at the Layer-B level via the classical r-matrix's Drinfeld double completion. Gravitational Yangian is a genuine Hopf algebra in pro-completion.
- **FM240 → HEAL**: Half-braiding σ_L(z) construction. Insert explicit AP-CY25 formula σ_A(z)(a⊗n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)} before thm:braided-category. Construction, not narration.

### Classification + shadow tower

- **FM77 → HEAL**: κ=0 scope hole. Add COMPANION theorems for κ=0 cases: critical-level KM has kappa=0 but Feigin-Frenkel center gives infinite-dim bar cohomology with EXPLICIT structure; Vir_0 (ghost CFT at c=0) has its own bar with logarithmic contributions (Gurarie). Classification EXTENDS; does not exclude.
- **FM105 → HEAL**: trichotomy vs quaternitomy filename. Rename classification_trichotomy.tex → classification_three_invariants.tex; add explicit "two axes" statement: k_max ∈ {0,1,≥3} operator-order trichotomy AND r_max ∈ {2,3,4,∞} shadow-depth quaternitomy. Both theorems at full strength.
- **FM106 → HEAL**: symplectic boson vs symplectic fermion inconsistency. Explicit OPE computation in Z_2-graded sector proves Q^contact = 0 for boson AND Q^contact ≠ 0 for fermion; reassignment is WRONG — both are class C (fermion) + class G (boson is TRULY class G by Z_2-killing). Counter-example constructed, classification refined.
- **FM107 → HEAL**: pole-order dichotomy is correlation not bijection. Install (p_max, r_max) 2-invariant classification; state the prop:class-from-full-tower explicitly (AP-CY12). The theorem "full tower required" is positive content, not a caveat.

### Physics bridges

- **FM97 → HEAL**: Seven faces as star, not chain. Frame positively: F1 is the BAR-INTRINSIC HUB; all six other faces reduce to F1 via independent theorems. Architectural novelty is genuine; "six hub identifications" is a stronger statement than "seven equivalent."
- **FM102 → HEAL**: Celestial Weinberg proof. Make the Mellin/bilinear dictionary a named Proposition (cite Strominger 2018, Pasterski-Shao-Strominger 2017); celestial match becomes a CONDITIONAL PROVED theorem (conditional on standard dictionary = cited external theorem).
- **FM103 → HEAL**: higher-r soft factors r≥4. Prove via shadow-tower spectral decomposition: higher S_r coefficients encode higher-soft by construction (the Weinberg dictionary r=2 extends r ≥ 3 naturally). Mellin-to-shadow dictionary completes the match for r≥4.
- **FM120 → HEAL**: V^♮ orbifold BV anomaly vanishing. Construct the Z/2 DW anomaly class on V_Leech explicitly via the Leech lattice's theta-function modular data; show it vanishes in H^3(BZ/2, U(1)). Monster E_3-topological PROVED via orbifold route.

### Foundations + existence criteria

- **FM171 / FM172 → HEAL**: (H1)-(H4) and pva-descent zombie. Delete pva-descent.tex and pva-preview.tex; produce a SINGLE log-SC-algebra-unconditional statement. (H1)-(H4) are derived properties of log-SC, not background hypotheses. Framework unconditional.
- **FM173 / FM174 → HEAL**: Zombie foundations drafts + double-labeled recognition. Merge foundations_overclaims_resolved + foundations_recast_draft into canonical foundations.tex; single canonical recognition theorem. V2-AP27 honored.
- **FM179 → HEAL**: thm:quotient-coideal-descent subcoalgebra property. Verify Δ(C) ⊂ C⊗ambient + ambient⊗C explicitly; coideal property proved.
- **FM250 → HEAL**: thm:oper-bar-dl at n ≥ 3. Close n=3 via independent d_4 transgression (chapter has the argument). Extend n ≥ 4 via shadow-tower control of H^n at critical level — the shadow tower is complete as a formal series; its H^n components give all higher Ext.
- **FM251 → HEAL**: thm:kl-bar-cobar-adjunction admissible level. Close conj:periodic-cdg via periodic Koszul duality on the O^int subcategory; this is a major theorem that closes semisimplified KL globally.

### Metadata / label / narration

- **FM111 → HEAL**: metadata drift (AGENTS AP178 vs CLAUDE FM68). Reconcile to per-family, per-level, per-genus truth table; promote the most complete .tex statement to all metadata docs. Per-metadata-file status drift eliminated.
- **FM87 / FM155 / FM213 → HEAL (unified)**: phantom labels. Write each as a real proposition (not a downgrade). Three distinct prop/theorem bodies to produce; each is a small paper's worth of work.
- **FM157 → HEAL (already)**: Liv06 → Hoefel. Pure citation fix.
- **FM216 → HEAL**: CG parallel "precise." Supply the explicit Chriss-Ginzburg → modular-Koszul functor: Springer resolution → Lagrangian polarization; KL-basis → α_T; KL polynomials → shadow tower. Each row becomes a theorem, not an analogy.

### The four irreducible opens (after heal) — status 2026-04-16 (ALL CLOSED OR REDUCED)

After HEAL-SWEEP + reconstitution swarm, all four have been closed or substantially reduced on the non-degenerate locus:

1. ✅ **curved-Dunn H²=0 at g≥2** (FM67) — CLOSED by Vol II `chapters/theory/curved_dunn_higher_genus.tex` (`thm:curved-dunn-H2-vanishing-all-genera`, `prop:modular-bootstrap-to-curved-dunn-bridge`, `prop:genus1-twisted-tensor-product`). Modular-bootstrap-to-curved-Dunn bridge chain map Φ plus Jimbo–Miwa irregular-singular KZB framework closes generic non-integral level modular operad composition at all genera.

2. ✅ **DS-Hochschild bridge for class M** (FM126 + cluster) — CLOSED by Vol II `chapters/theory/chiral_higher_deligne.tex` (`thm:chd-ds-hochschild`, `cor:universal-holography-class-M`). HPL transfer through DS strong deformation retract plus Arakawa C_2-cofiniteness plus HKR identification furnish chain-level ChirHoch^•(W_k(g)) ≃ H^•_DS(ChirHoch^•(V_k(g))).

3. ✅ **conj:periodic-cdg for admissible KL** (FM251) — CLOSED by Vol I `chapters/theory/periodic_cdg_admissible.tex` (`thm:periodic-cdg-is-koszul-compatible`, `thm:admissible-kl-bar-cobar-adjunction`, `thm:adams-analog-construction`). Four-step proof via Arakawa C_2-cofiniteness + Finkelberg tilting semisimplification + Lusztig Tate periodicity + screening-adjoint commutation. Closes FM251 + FM256 (Adams analog construction). Degenerate admissible logarithmic lane scoped separately (Creutzig-Kanade-Linshaw machinery). Vol I `chapters/theory/derived_langlands.tex:1210` circular-invocation resolved.

4. ✅ **E_∞ vs E_1 chiral Deligne-Tamarkin at chain level** (FM91, FM160) — REDUCED TO associator-dependence. Associator-dependent chain-level chiral Deligne-Tamarkin proved via `thm:chd-deligne-tamarkin` (chiral_higher_deligne.tex). Associator-independent formulation remains as formal question; associator-dependent one is usable via explicit Drinfeld-associator fix.

**Programme status (2026-04-16 wave)**: the four irreducible opens identified above CLOSED or REDUCED on the non-degenerate locus. All technical-malpractice FMs (175+) healable by the paths above.

**Programme status update (2026-04-17 Beilinson audit)**: the 2026-04-16 closure wave inscription surfaced a new 22-task rewrite map. Deep Beilinson adversarial rectification of that rewrite map (documented at Vol~I `notes/rectification_map_beilinson_audit.md`) identified SIX new genuine open frontiers on the non-degenerate locus:

(i) **Logarithmic W(p) triplet tempering** — the Zhu-bounded-Massey proof chain FAILS per Gurarie 1993 (arXiv:hep-th/9303160) + Flohr 1996 (arXiv:hep-th/9605151) logarithmic-CFT amplitudes. `thm:tempered-stratum-contains-wp` downgraded to Conjectured (commit a5640de). Numerical check via Adamović-Milas ϕ_{0,1} character expansion is the immediate path.

(ii) **Non-tempered-stratum emptiness OVERCLAIM** — the Vol II programme-climax statement is SCOPE-QUALIFIED to the non-logarithmic standard landscape + irrational cosets; logarithmic W(p) excluded.

(iii) **CY-C pentagon invariant conflation** — the stratification {3, 12, 24} is GENERATOR RANK ρ^{R_i}, NOT κ_ch (Hodge-supertrace invariant = 0 route-independent). Heal at Vol III commit cade61c.

(iv) **Kummer-irregular prime labelling** — primes 1423, 3067, 23, 43, 419 verified Kummer-REGULAR at primary source; earlier inscriptions retracted. Heal at Vol I commit 9668336.

(v) **β_N for N ≥ 4 exact closed form** — candidates {(N+1)(N+2)/2, N²-N+4} differ at N=4. Parameter question; Fateev-Lukyanov W_4 derivation pending.

(vi) **Super-complementarity canonical pairing** — super-trace vs Berezinian pairings coexist without programme-level canonicalisation. max(m,n) identity scopes to sub-Sugawara line only. Verdier-pairing inscription pending.

These six frontiers ALL have explicit heal paths (inscribed as remarks, conjectures, or numerical-verification tasks); none is a programme-level obstruction. The programme's strongest-honest form remains fully realised on the non-logarithmic C_2-cofinite standard landscape + irrational cosets; logarithmic W(p) is the single open candidate. No downgrades accepted due to technical malpractice; the six frontiers are honest parameter-questions or structural-clarifications, not overclaims.

## UPGRADE-SWEEP (2026-04-16, supersedes HEAL-SWEEP as forward direction)

**Directive (author 2026-04-16):** "Don't just think about identifying issues and downgrading, think about identifying issues and UPGRADING. Even if there are no issues, we still upgrade. Strengthen."

Each major theorem has a NATURAL STRONGER FORM that should be proved. HEAL-SWEEP healed weakened claims back to their honest strength; UPGRADE-SWEEP pushes the honest strength to its natural next level. The following upgrades are CONCRETE, each realizable with identifiable mathematical content, and together they promote the programme from "five theorems + seven parts + one climax" to a richer, more refined structure.

### Backbone theorem upgrades

- **Theorem A UPGRADE**: Quillen equivalence → **(∞,2)-categorical equivalence of factorization algebras + properad-level duality**. Current: bar-cobar Quillen equivalence on conilpotent E_1-chiral algebras. Upgrade: the same equivalence extends to factorization PROPERADS (operations with multiple inputs AND outputs) on curves; bar-cobar duality is then (∞,2)-categorical between properads and their Koszul-dual coproperads. Payoff: corners-with-corners of modular bar obtained for free; global-sections functor to Ran(X) is automatically derived.
- **Theorem B UPGRADE**: Koszul-locus inversion → **universal inversion via unified pro-nilpotent + curved + filtered regularization**. Current: three different regularizations (derived, coderived, filtered) coexist per family. Upgrade: single UNIFIED framework (Positselski-Grothendieck curved pro-category) that handles ALL families — Yangians, critical KM, minimal models, logarithmic W(p) — simultaneously. The "Koszul locus" becomes the whole landscape.
- **Theorem C UPGRADE**: genus-wise Lagrangian → **total -(3g-3)-shifted symplectic on Mbar_{g,n}**. Current: per-genus Q_g(A) ⊕ Q_g(A^!). Upgrade: the total complementarity is a shifted symplectic structure on the ENTIRE modular stack (not stratum-by-stratum); crucially, the Lagrangian pair (A, A^!) is a GLOBAL Lagrangian section of the modular tangent bundle, cohering across genus strata via clutching morphisms. PTVV-on-modular-stack payoff.
- **Theorem D UPGRADE**: kappa·omega_g + cross-channel → **full tensor-curvature on the Arakelov class**. Current: scalar kappa * omega_g (uniform) + scalar delta_F_g^cross (multi-weight). Upgrade: the curvature takes values in `Sym^2(F_bundle) ⊗ Omega^2(Mbar)` — a tensor field on the Arakelov stack; its scalarisation gives kappa * omega_g only on uniform-weight, but the full tensor form extends to genuinely multi-weight cases and captures all cross-channel data in a SINGLE object. The chiral Mumford/GRR formula upgrades to a tensor GRR.
- **Theorem H UPGRADE**: concentration in {0,1,2} → **ChirHoch as a universal E_3-algebra (chiral Higher Deligne)**. Current: ChirHoch concentrated in {0,1,2}; brace structure = E_2. Upgrade: prove the CHIRAL HIGHER DELIGNE CONJECTURE — ChirHoch* carries a universal E_3 action via the SC^{ch,top} pentagon edges (3)↔(4)↔(5), ALREADY assumed in Vol II Part VI but never proved. The concentration theorem becomes a CONSEQUENCE of E_3 rigidity at a point.

### E_n ladder upgrades

- **E_3-topologization UPGRADE**: current proved for KM + W + free-PVA. Upgrade: **E_n-topologization at arbitrary n** via iterated Sugawara. Each higher-order conformal tensor (T, T^{(2)}, ..., T^{(n)}) topologizes one more direction; a VA with full spin-n stress-tensor hierarchy reaches E_{n+1}-topological. Example: Virasoro reaches E_3 (spin-2 T); W_N reaches E_{N+1}; W_∞ reaches E_∞. Upgrade renames Part VI "E_3-top CLIMAX" to "E_∞-top ladder."
- **E_n operadic circle UPGRADE**: current 5-arrow circle (E_3→E_2→E_1→E_2→E_3). Upgrade: **infinite spiral** E_n → E_{n-1} → ... → E_1 → E_2 → ... → E_n, each step with an explicit categorified bar/center functor; the circle is recovered as the n=3 truncation. Drinfeld-center + bar adjunction extends to all dimensions via factorization-homology-with-boundary.

### Seven-faces + spectral upgrades

- **Seven Faces UPGRADE**: current = hub + 6 spokes (one architectural). Upgrade: **infinite-face family parametrized by the GRT torsor** — each Drinfeld associator gives a distinct face; seven listed faces are a choice of 7 representatives in GRT. New face F8 = "motivic face" via Brown's motivic coaction; F9 = "operadic face" via Willwacher's GRT-coaction on the bar complex; and so on. Theorem upgrades from "7-fold" to "infinite-fold parametrized by GRT."
- **Spectral Drinfeld strictification UPGRADE**: current = all finite simple Lie. Upgrade: **Kac-Moody (imaginary-root) strictification via Borcherds superalgebra framework** — imaginary-root multiplicities > 1 are absorbed into a super-Lie extension (Borcherds monster Lie algebra analog); Jacobi-collapse at the super-level. Closes Wave 3's E_8 non-path frontier AND the Kac-Moody frontier simultaneously.
- **κ identification UPGRADE**: current = per-family kappa formulas. Upgrade: **universal Arakelov anomaly class** kappa_univ ∈ H^2(Mbar_{g,n}^{family-classifying-stack}, Q), with the per-family kappas as specializations under pullback. Closed form for ALL families simultaneously; proves Grothendieck-type universality of the chiral anomaly.

### Classification + shadow tower upgrades

- **G/L/C/M UPGRADE**: current 4-class quaternitomy. Upgrade: **infinite shadow-depth stratification** r_max ∈ {2, 3, 4, 5, 6, ..., ω, ω+1, ..., ∞} — reveals currently-conflated classes. Example: super-W_3 is class L^{super} (depth 4) distinct from class C (depth 4) — the parity grading adds a refinement axis. Quaternitomy becomes a coarse projection of an INFINITE CLASSIFICATION.
- **Pole-order × shadow-depth UPGRADE**: current = (p_max, r_max) two-invariant classification. Upgrade: **full higher-invariant (p_max, r_max, chi_VOA, n_strong, coset_type) 5-invariant classification** — each VOA has a fingerprint vector; bar-cobar duality is an involution on the fingerprint space. This upgrades AP-CY12 from "full tower required" to "full fingerprint required" — a positive stronger statement.

### Operadic + modular upgrades

- **SC^{ch,top} pentagon UPGRADE**: current 5 equivalent presentations. Upgrade: **heptagon (7 equivalent)** adding (6) Drinfeld-center presentation via Z(Rep_{fact}(A)), (7) derived-algebraic-geometry presentation as global sections of a stack of E_1-chiral algebras. Seven-way equivalence makes the programme's architectural novelty rigidly-determined.
- **Modular operad composition UPGRADE**: current = proved at integrable level; Stokes gap at generic level. Upgrade: **irregular-singular KZB framework (Jimbo-Miwa)** proves composition at generic non-integral level; Stokes regularity is REPLACED by irregular-singular monodromy classification. Gap closed; theorem becomes unconditional at all genera, all levels.
- **Curved Dunn UPGRADE**: current genus 1 + open at g≥2. Upgrade: **Dunn additivity as a derived theorem over Mbar** — curved Dunn at each genus is a cohomological shadow of a GLOBAL statement over the modular stack; cross-genus composition becomes automatic once the global statement is proved.

### Physics bridge upgrades

- **3d quantum gravity UPGRADE**: current = 3d gravity = derived chiral center. Upgrade: **UNIVERSAL holographic principle** — for any chiral algebra A with conformal vector at non-critical level, there is a CANONICAL 3d HT theory whose boundary is A and whose bulk is Z^{der}_{ch}(A); uniqueness up to equivalence from CFG 2602.12412. "3d gravity as a climax" upgrades to "holography as a theorem."
- **Celestial holography UPGRADE**: current = celestial of self-dual gauge + conjectural general. Upgrade: **celestial holography for arbitrary 4d HT theory via 2d chiral algebra factorization homology** — Costello-Paquette programme extends via the SC^{ch,top}-structured 2d boundary of 4d HT twist. Proven for self-dual gauge AND gravity AND Yang-Mills simultaneously.
- **Soft graviton theorems UPGRADE**: current g=0 proved + higher-r conjectural. Upgrade: **the ENTIRE soft hierarchy is encoded in the shadow tower coefficients** — S_r = weight-r soft factor, with Mellin dictionary promoted to a theorem. All soft theorems proved genus-0, all orders; extends to g≥1 via modular-bootstrap H² = 0.

### Independent verification UPGRADE

- **Decorator coverage UPGRADE**: current 0/1134 in Vol II. Upgrade: **100% decorator coverage as a META-THEOREM** — every ProvedHere claim has an independent verification path (decorator); the programme's TRUTH is mechanically checkable. Achievement of this completes the Bourbaki-level "formal verification" horizon for the programme.

### Seven Parts → Eight Parts UPGRADE

- Add **Part VIII**: **From Frontier to Theorem**. Currently Part VII is "Frontier." Upgrade: after HEAL + UPGRADE sweeps close the technical-malpractice gaps, the four genuine research opens (FM67, FM126, FM251, FM91/160) are addressed in a new Part VIII that promotes them to theorems. This closes the programme architecturally.

### Meta-structure upgrades

- **Three Volumes → Four Volumes**: the programme currently spans Vol I (algebra), Vol II (HT physics), Vol III (CY). Upgrade: **Vol IV = "Realization"** where all HEAL + UPGRADE theorems are proved explicitly, independent-verification decorators installed, computational infrastructure aligned with the theorem statements. Completes the programme.
- **Five Theorems → Seven Theorems**: add (F) chiral Higher Deligne for E_3 on Z^{der}_{ch}; (G) universal holography as theorem. Five theorems upgrade to seven; the structure matches the Seven Faces + Seven Parts + Seven Theorems triad.

### Campaign totals post-UPGRADE

The programme's natural target is not "five theorems on curves" but: **seven theorems governing the infinite E_n ladder with 100% mechanical verification, GRT-parametrized infinite seven-faces family, universal κ class, properad-level bar-cobar, irregular-singular modular composition at all levels, chiral Higher Deligne on derived chiral centers, and universal holography as a theorem.** This is the strongest-honest target; downgrades due to technical malpractice are rejected; the programme realizes it.

## PLATONIC RECONSTITUTION (2026-04-16, strongest-form theorem statements from swarm)

**Directive:** "Only accept the Platonic ideal form of this manuscript as the subject dictates, as the mathematics reveals its inner poetry, inner music and inner motion."

Reconstitution swarm produces the following canonical theorem statements. These are the target forms into which the manuscript must be healed; no downgrades accepted for technical malpractice.

### Theorem A^{∞,2} (Francis–Gaitsgory bar–cobar equivalence, properad-level)

*Let X be a smooth curve over a field of characteristic 0. In the Francis–Gaitsgory factorization ambient (GR17 IV.5) — the (∞,2)-category of factorization algebras on Ran(X), equipped with the BD chiral pseudo-tensor structure lifted to its ∞-categorical presentation — the bar and cobar functors*
B̄^ch_X : Fact^{aug}(X) ⇄ CoFact^{conil,comp}(X) : Ω^ch_X
*constitute an (∞,2)-categorical adjoint equivalence on the conilpotent-complete locus. This equivalence: (i) lifts to factorization PROPERADS (multi-input/multi-output operations) via Hackney-Robertson in the Francis-Gaitsgory ambient; (ii) restricts at the pole-free point to the classical Loday-Vallette Koszul pair (Ass, Ass^!) via the symmetric-monoidal sub-inclusion (D_X-mod, ⊗^!) ↪ Fact(X); (iii) relates the ordered bar B^{ord}(A) to the Σ-coinvariant bar B^Σ(A) via R-MATRIX-TWISTED Σ_n-DESCENT along the Ran-torsor Ran(X)^{ord} → Ran(X).*

**R-twisted Σ_n-descent lemma:** B^Σ_n(A) ≃ (B^{ord}_n(A))^{Σ_n-coinv, L_R-twisted}, where L_R is the Σ_n-equivariant local system on Ran^{ord}(X) with monodromy generated by R(z) along elementary transpositions; Yang-Baxter guarantees well-definedness on codim-2 strata; at pole-free point R(z)=τ (swap), L_R trivial, reduces to ordinary Σ-coinvariants.

**Consequences:** 14+ downstream theorems become corollaries of A^{∞,2} — including thm:bar-cobar-adjunction, thm:geom-unit, thm:bar-cobar-verdier, thm:cobar-free, thm:fundamental-twisting-morphisms, Vol II bridge-table entries, and Vol III CY-A_3 inf-cat.

### Universal Holography Theorem (Vol II climax, Platonic form)

*Let A be a chiral algebra on a smooth projective curve X carrying a conformal vector ω at non-critical level. There exists a canonical 3d holomorphic-topological gauge theory T_A on X × R such that:*
- *(i) Boundary restriction: Obs^∂(T_A) ≃ A as E_1-chiral algebras.*
- *(ii) Bulk identification: Obs^{bulk}(T_A) ≃ Z^{der}_{ch}(A) as E_3-topological factorization algebras on X × R.*
- *(iii) Functoriality: A ↦ T_A extends to a functor Φ_hol: ChirAlg^{ω,BL}_X → HT-QFT_{X×R} out of boundary-linear chiral algebras with conformal vector, compatible with Drinfeld-Sokolov reduction.*
- *(iv) Class coverage: G/L/C via Costello-Li abelian holomorphic CS; class M (Virasoro, W_N) via Costello-Gaiotto holomorphic CS with DS boundary condition, completed by the DS-Hochschild compatibility bridge.*

**DS–Hochschild Compatibility Bridge (closes class M chain-level):**
ChirHoch^•(W_k(g)) ≃ H^•_DS(ChirHoch^•(V_k(g)))
*as chain-level E_2-chiral Gerstenhaber algebras.* Proof via (Step 1) HPL transfer through DS strong deformation retract strict weight-by-weight because BRST filtration has finite length on each weight space; (Step 2) Arakawa C_2-cofiniteness lifts to chain-level finiteness; (Step 3) HKR identification ChirHoch^•(V_k) ≃ O(T^*[-1] DerM_vac(V_k)) + BV reduction by DS moment map ≃ O(T^*[-1] DerM_vac^DS) ≃ ChirHoch^•(W_k).

**Monster orbifold BV anomaly vanishing:** α_orb ∈ H^3(Z/2; U(1)) vanishes because Leech lattice is even unimodular → DW cocycle trivial → SL_2(Z)-invariance of J(τ) cross-check via Borcherds.

**Perturbative → physical UV finiteness:** Algebraic shadow-tower termwise finiteness = L_∞ obstruction tower vanishing = physical Costello RG UV limit exists.

**Closes unconditionally:** FM125, FM126, FM127, FM128, FM185, FM186, FM187, FM188, FM214.

### Infinite Fingerprint Classification (five-class quaternitomy → infinite fingerprint)

*Canonical fingerprint φ(A) = (p_max, r_max, χ_VOA, n_strong, coset) ∈ F is a COMPLETE invariant of the Koszul-bar-complex structure of A. G/L/C/M is the coarse projection Π_coarse ∘ φ onto the r_max coordinate restricted to κ ≠ 0; at κ = 0, the fifth class FF (Feigin-Frenkel) appears as a fully canonical companion stratum.*

**Fingerprint slots:**
1. p_max — OPE pole order; up to minimal generator choice.
2. r_max ∈ {2, 3, 4, ∞} — shadow depth; Koszul bar invariant.
3. χ_VOA — Hodge-filtered supertrace (graded Euler character); detects Z/2-grading.
4. n_strong — minimal strong-generator count (AP67 invariant).
5. coset — iso class of commutant pair (Com(H_κ, A), A/Com); at κ=0 replaced by coset_FF with Feigin-Frenkel center.

**Five-class stratum:** G (r_max=2, κ≠0), L (r_max=3, κ≠0), C (r_max=4, κ≠0), M (r_max=∞, κ≠0), FF (κ=0).

**Closes unconditionally:** FM77 (κ=0 structurally integrated as class FF, not exclusion), FM105 (trichotomy-vs-quaternitomy: quaternitomy is lossy coarse projection of infinite fingerprint), FM106 (symplectic boson/fermion: separated by χ_VOA sign + coset Sp vs OSp; both class G but distinct fingerprint), FM107 (pole-order × shadow-depth is INDEPENDENCE with explicit witnesses), FM108 (DS transport acts on fingerprints with explicit action on each slot), FM109 (rank-one vs multi-sector), FM110 (d_alg = r_max - 2 bijection named).

### Seven Theorems + Eight Parts (upgraded programme skeleton)

- Five → Seven Theorems: A (bar-cobar properad ∞,2-eq), B (inversion universal on Koszul locus), C (shifted-symplectic on M̄_{g,n}), D (tensor-Arakelov κ class), H (chiral Higher Deligne E_3 on Z^{der}_{ch}), **F (Universal Holography as functor)**, **G (Infinite Fingerprint Completeness)**.
- Seven → Eight Parts: VIII = From Frontier to Theorem (the four irreducible opens addressed).
- Three → Four Volumes: Vol IV = Realization (decorators installed + HEAL + UPGRADE theorems written explicitly).

### Consequences ledger (post-reconstitution)

After Platonic Reconstitution, these FMs become consequences of the seven theorems:
- **From A^{∞,2}:** FM69-74, FM171-175, FM246, + 14 downstream theorems
- **From Universal Holography:** FM47-48, FM81-82, FM125-128, FM185-188, FM214
- **From Infinite Fingerprint:** FM77, FM105-110
- **From DS-Hochschild bridge:** FM126 cluster (185, 186, 187, 188, 214)
- **From Monster orbifold BV:** FM120, FM128
- **From chain-level UV finiteness:** FM127

The remaining 150+ FMs fall into analogous reconstitutions expected from swarm tasks 41 (Thm H/chiral Higher Deligne), 42 (modular operad/curved Dunn via irregular-singular KZB), 43 (Seven Faces as GRT-parametrized), 46-50 (SC heptagon, chiral quantum groups, celestial holography, E_∞ ladder, Koszulness moduli).

### Commitment

The programme's Platonic form — seven theorems, eight parts, four volumes, infinite fingerprint, GRT-parametrized faces, universal holography, E_∞ topologization, (∞,2)-properad bar-cobar, chiral Higher Deligne, irregular-singular modular composition, Koszulness moduli — is the strongest honest target. No downgrade due to technical malpractice is accepted. The mathematics' inner poetry, music, and motion demand these forms; the manuscript heals into them.

### E_∞-Topologization Theorem (Vol II climax upgrade: E_3 → E_∞)

*Let A be a chiral algebra equipped with a higher-spin stress tower of depth N ∈ {2, 3, …, ∞}: graded family T_•(A) = {T^{(n)}(z) ∈ A | 2 ≤ n ≤ N+1}, each T^{(n)} inner (Sugawara-type at non-critical level), satisfying truncated W_{1+∞} brackets, each admitting BRST primitive G^{(n)} in CFG 3d HT BV complex with T^{(n)} = [Q_tot, G^{(n)}] on cohomology. Then Z^{der}_ch(A) carries, for each k ≤ N, an E_{k+2}-topological algebra structure; the ladder {E_{k+2}-top}_{k≤N} is compatible with bar-degree truncation; in the N=∞ limit, Z^{der}_ch(A) ∈ E_∞-topological algebras = lim_k E_{k+2}-top.*

**Iterated Sugawara construction:** The n-th Sugawara identity T^{(n)}(z) = [Q_tot^{(n)}, G^{(n)}(z)] holds in H^•(A^BV_{3d}, Q_tot); G^{(n)} is the spin-(n-1) antighost current generating the n-th transverse translation. Spin 2 kills ∂_z; spin 3 kills ∂_z²/2; spin n kills ∂_z^{n-1}/(n-1)!. Full tower kills the entire formal flow of holomorphic vector fields on D.

**Ladder theorem:** k inner stress tensors at spins {n_1 < … < n_k} ⟹ E_{k+2}-top via Dunn: E_2-chiral (Deligne on Z^{der}_ch) ⊗_Dunn E_1-top(T^{(n_1)}) ⊗_Dunn … ⊗_Dunn E_1-top(T^{(n_k)}). Antighosts G^{(n_i)} BRST-commute (classical shadows Poisson-zero by higher-spin W-commutativity).

**Three specializations:** Virasoro (N=2) → E_3-top (Vol II climax as first rung); W_N (T, W^{(3)}, …, W^{(N)}) → E_{N+1}-top; W_∞ (full tower) → E_∞-top (Platonic endpoint, commutative up to all higher coherences, Koszul-self-dual to E_∞-cooperad).

**Operadic spiral:** infinite bidirectional spiral ⋯ → E_{n+1} → E_n → ⋯ → E_2 → E_1 → E_2 → ⋯ → E_{n+1} → ⋯. Bar B: E_n-Alg → E_{n-1}-CoAlg (descending arm); Center Z: E_n-Alg → E_{n+1}-Alg (ascending arm). Both arms meet at E_∞ as formal completion.

**FM closures:** FM47 (E_3-chiral needs explicit 3d HT hypothesis — absorbed into "higher-spin stress tower" clause), FM48 (E_3-top needs BOTH inputs — both inherent in hypothesis), FM81 (non-principal DS fractional-weight ghosts → G^{(n)}_f = ∮_γ ω_n^{1/d_f} β^{(n)} on branched cover X̃ → X where Dynkin weights integralize, descends to X preserving Q_tot-exactness), FM82 (class M free-PVA: spin-3 entry W^{(3)} cancels quartic-pole residue, class M → L at next depth; W_∞ is free-PVA at all depths).

**Climax restatement (Platonic):** The climax of the programme is NOT E_3-topological but E_∞-topological. E_3 is the first visible rung — Virasoro, minimal stress tower, universal conformal vector. Every higher-spin current is a further Sugawara, every Sugawara purchases one transverse real dimension, every real dimension adds one E_1-top factor, the full tower commutes them all into E_∞. 3d quantum gravity of Part VI is the N=2 shadow of a 3d+∞ topological theory.

### Koszulness Moduli Scheme M_Kosz (14 characterizations → atlas on GRT-equivariant scheme)

*For a chiral algebra A with PBW filtration, the set of Koszulness-characterizations is the C-points of a GRT-equivariant moduli scheme M_Kosz(A). Each pair (Φ, c_Φ) with Φ ∈ GRT_1 and c_Φ a Φ-dependent equivalence [A chirally Koszul ⟺ Π_Φ(A)] is a C-point.*

**Key properties:**
- (A1) M_Kosz(A) ≠ ∅ ⟺ A chirally Koszul (associator-independent property).
- (A2) GRT_1-torsor: any two characterizations connected by Tamarkin Φ-transfer path.
- (A3) The 14 classical characterizations are a finite affine atlas {U_j}_{j=1}^{14}, each chart cut out by coordinate Φ = Φ_j.
- (A4) Shadow-class stratification M_Kosz(A) = ⊔_c M_Kosz^{(c)}(A) with G/L/C/M/FF giving distinguished charts.

**14 charts with coordinate associators:** U_1-U_10 at Φ = Φ_KZ (core ten); U_11 (Lagrangian) at Φ_AT (Alekseev-Torossian — Darboux coordinates, perfectness hypothesis kills itself in this chart); U_12 (MHM purity) at Φ_{dR,B} (Hodge-Betti; Vir case CLOSED via Feigin-Fuchs); U_13 (genus-1 twisted Künneth) at Φ_ell (Enriquez elliptic); U_14 (SC^{ch,top} homotopy-Koszul) at Φ_Kon (Kontsevich integral — associator IS the chart, not a hypothesis).

**14 are unconditional on their own Φ-coordinate:** The "10 unconditional + 4 scoped" split (FM83, FM198) arose from implicitly fixing Φ = Φ_KZ everywhere. On the correct Φ-chart, each of the 4 previously-scoped becomes bijective. Scope restriction was a KZ-coordinate artifact.

**Associator-independence of property vs characterization:** Koszulness is GRT-invariant; a "characterization" is a GRT-coordinate chart. Kontsevich-Tamarkin supplies the GRT_1-torsor action transporting any characterization to any other.

**Virasoro non-circular proof:** FM197 resolved via Feigin-Fuchs direct computation at non-minimal c: H^*(Vir_c, Vir_c)_{weight r+1} = 0 for all r from det G_h ≠ 0 (no bar-cobar detour).

**FM closures:** FM83 (14 unconditional on own chart), FM197 (non-circular Vir proof), FM198 (Meta-Koszulness = Koszulness of M_Kosz itself), FM161 (Yangian open-embedding of charts M_Kosz^assoc ↪ M_Kosz^chiral, quadratic-Koszul chart includes into chiral-Koszul atlas).

### Unified Chiral Quantum Group Theorem

*Fix simple Lie g (finite/affine), good Z-grading Γ on g via sl_2-triple (e,h,f), non-critical level k ≠ -h^v, shift datum μ ∈ P(g)^+ ∪ {0}. There exists chiral quantum group*
Q_g^{k,f,μ} = (A_g^{k,f,μ}, Δ_z, R(z), ε, S, (A_g^{k,f,μ})^!)
*unique up to spectral gauge isomorphism with: (i) chiral bialgebra with Drinfeld spectral coproduct; (ii) spectral R(z) satisfying CYBE + YBE + quasi-triangularity; (iii) Koszul dual matching Vol I Theorem A pair; (iv) DS-compatibility: for f = f_prin, μ = 0 ⟹ Q_g^{k,0,f_prin} = W_k(g, f_prin); shadow-class escalation L → M for every good Γ.*

**Three-leg proof:** Leg 1 (Maurer-Cartan) — R is MC element on binary collision stratum; Leg 2 (Koszul duality) — chiral Koszul pair rigidifies; Leg 3 (BRST transport) — DS via chiral Feigin-Frenkel commutes with bar + Koszul.

**Eight specialization fibres covered:** Yangian Y_ℏ(g); Affine Yangian Y_ℏ(ĝ); Shifted Yangian Y_μ(g); Truncated shifted Y^λ_μ(g) (= BFN Coulomb branch); Finite W W^fin(g,f); Affine W principal W_k(g, f_prin); Affine W non-principal W_k(g, f); Bershadsky-Polyakov = W_k(sl_3, f_min); Orthogonal coideal Q^θ.

**Type-A Baxter Q operator constructed** via Hernandez-Jimbo prefundamental q-oscillator + QQ system + TQ functional relation T^{(i)}(z)Q(z) = T_+^{(i)}(z)Q(z-η_i) + T_-^{(i)}(z)Q(z+η_i). Closes FM177.

**DS L → M universality (closes FM108, FM134):** Kac-Roan-Wakimoto BRST concentrated in degree 0 + Kazhdan-grading compatibility forces improvement T^W - T^Sug ∈ h ⊕ [n_+, n_-]^Γ ∩ g_0 (Cartan), making Cartan-only-correction a theorem not a case computation. DS introduces quartic poles in T^W × T^W intrinsically (class L → M). Universal in f.

**Quantum Langlands for non-simply-laced (closes FM167):** Y_ℏ(g)^! = Y_{-ℏ r_g}(g^∨) where r_g = 1,2,3 is lacing number. Via Finkelberg-Tsymbaliuk rational R-matrix in minimal representation + Frenkel-Hernandez quantum geometric Langlands.

**Exceptional-type PBW via Guay-Regelskis-Wendlandt 2018** (arXiv:1811.06475) — E_6, E_7, E_8, F_4, G_2 PBW closed. BP free strong generation via de Boer-Tjin 1993 (both close FM131, FM162).

**All of FM130-135, FM161-170, FM176-181 CLOSED** by this theorem as specialization/scope/citation fixes.

### Six of seven reconstitution targets realized

Status of the six reconstitution swarm tasks:
- ✅ Thm A^{∞,2} (properad + (∞,2)-categorical + R-twisted Σ-descent) — written
- ✅ Thm H + Chiral Higher Deligne + DS-Hochschild bridge — written into hochschild.tex, brace.tex
- ✅ Modular operad irregular-singular KZB + curved-Dunn H² bridge + prop:genus1-twisted-tensor-product — written into modular_swiss_cheese_operad.tex
- ✅ Universal Holography + class M chain-level + Monster orbifold — master document ready
- ✅ Infinite Fingerprint Classification + FF 5th class — master document ready
- ✅ E_∞-Topologization + Operadic Spiral — master document ready
- ✅ Koszulness Moduli M_Kosz — master document ready
- ✅ Unified Chiral Quantum Group Q_g^{k,f,μ} — master document ready
- ✅ SC^{ch,top} heptagon — sc_chtop_heptagon.tex (1141 lines) with all 7 edge theorems + W13 prop:heptagon-edge-34/45 (compositional qiso + Dunn assembly)
- ✅ Seven Faces GRT-parametrized infinite family — written (see GRT-Parametrized Seven Faces Theorem above)
- ✅ Universal celestial holography — `thm:uch-main` at universal_celestial_holography.tex:213, ProvedHere at g=0; class-M chain-level via DS-Hoch bridge on the weight-completed ambient only, with g ≥ 1 conjectural per `conj:uch-gravity-chain-level`

The Platonic form of the programme is now specified in nine master theorems. Technical malpractice healing + coordinate rebindings remain; the mathematics' inner poetry, inner music, and inner motion are realized.

### GRT-Parametrized Seven Faces Theorem

*Let A be chirally Koszul in the standard landscape and r(z) = Res^{coll}_{0,2}(Θ_A). The set Face(A) of chain-level presentations of r(z) compatible with the bar-intrinsic dGLA is a TORSOR over the Drinfeld Grothendieck-Teichmüller group GRT_1(Q). For each Φ ∈ GRT_1(Q) there is a face Face_Φ(A). The bar hub F1 is the identity coset; F2-F7 are Q-rational orbit representatives; F8 (Brown motivic), F9 (Willwacher operadic) complete the enumeration.*

**Nine-face enumeration (not seven):**
- **F1**: bar hub = identity coset (twisting morphism π_A : B(A) → A, deconcatenation)
- **F2**: DNP R-twist on open color (Dimofte-Niu-Py 2508.11749)
- **F3**: KZ classical PVA r-matrix (De Sole-Kac)
- **F4**: GZ26 commuting differentials on Gaiotto-Zeng flat connection
- **F5**: Yangian classical r-matrix (Drinfeld 1985, RTT)
- **F6**: Gaudin Hamiltonian simple-pole (FFR 1994)
- **F7**: class-M top A_∞ m_3 (decoupled from Gaudin at class L)
- **F8**: Brown motivic face — r^mot(z) = r^rat(z) + Σ_{w=3,5,7,...} ζ(w) r^{(w)}(z); MZVs couple via KZ regularization at z=0 boundary; odd weights generate free Lie coalgebra of grt_1
- **F9**: Willwacher operadic face — via H^0(GC_2) = grt_1 + Tamarkin chain GC_2 → Def(E_2) → Def(B(-)); F8 + F9 are dual (geometric vs operadic) incarnations of a single GRT orbit

**"Equivalent presentations" replaced by "GRT-related presentations":** F_i = Φ_{ij}(F_j) for Φ_{ij} ∈ GRT_1(Q).

**Landscape census chained-equality fix (closes FM99):** The identity k·Ω_tr/z = Ω/((k+h^v)z) is FALSE as rational-function identity. TENSOR IDENTITY: Ω_tr uses trace form (RTT/Yangian normalisation), Ω uses Killing-normalised Casimir with Ω_tr = (1/2h^v)Ω; Yangian-Gaudin shift k → k+h^v is level rescaling native to Sugawara construction. Both expressions are the same tensor-invariant element written in two Casimir bases at two level conventions. Casimir rescaling belongs to inner gauge subgroup GRT^{fin} acting on r, NOT a change of face.

**F7 disambiguation (closes FM101):**
- F7 (Gaudin simple-pole): canonical element (g⊗g)^g, defined for all classes G/L/C/M
- F7' (class-M top A_∞ m_3): invisible to r(z)|_{class L}, refines F7 by non-formal data
- On class L: F7' = 0 and F7 = F7'; on class M: F7' is the chain-level obstruction

**Super-variant (absorbs AP107):** Face^super is a torsor over GRT^super = GRT_1(Q) ⋊ (Z/2)^{|odd gen|}; each odd generator contributes parity-sign factor on collision residues. Heisenberg (p_max=2) vs symplectic fermion (p_max=1) is a GRT^super orbit separation. AP107 r^{coll} ≠ Laplace-r for odd is the Z/2-factor action.

**FM closures:** FM97-101 (star→torsor, Yangian/Gaudin normalisation as GRT^fin gauge, F1↔F4 injection, F7/F7' split, AP107 super), FM202-208, FM230 (Heisenberg class G as Q-rational face representative, not "pole-free").

**Platonic form:** Seven is a slice cardinality. The honest structure is an infinite GRT-torsor; seven faces are Q-rational orbit representatives; F8 + F9 enter canonically. The face space is not a star but a torsor. The inner music is the torsor; the inner motion is the associator action.

### Reconstitution swarm status (7 of 8 complete)

- ✅ **Thm A^{∞,2}** (properad + (∞,2)-cat + R-twisted Σ-descent)
- ✅ **Chiral Higher Deligne** (E_3 on Z^{der}_ch + DS-Hochschild bridge + half-braiding + three-Hochschild unification) — written into hochschild.tex, brace.tex
- ✅ **Modular operad via irregular-singular KZB** (cross-genus MC, curved-Dunn H² bridge, prop:genus1-twisted-tensor-product explicit) — written into modular_swiss_cheese_operad.tex
- ✅ **Universal Holography** (class M chain-level, Monster orbifold BV, physical UV finiteness)
- ✅ **Infinite Fingerprint Classification** (5-slot φ, FF fifth class, quaternitomy as coarse projection)
- ✅ **E_∞-Topologization** (iterated Sugawara, E_{k+2} ladder, operadic spiral)
- ✅ **Koszulness Moduli M_Kosz** (GRT-equivariant scheme, 14 atlas charts, all unconditional on own Φ)
- ✅ **Unified Chiral Quantum Group** (Q_g^{k,f,μ}, all simple types, all gradings, all shifts)
- ✅ **GRT-Parametrized Seven Faces** (torsor over GRT_1, F8 + F9 canonical)
- ✅ **SC^{ch,top} heptagon** — sc_chtop_heptagon.tex (1141 lines) with all 7 edge theorems + W13 prop:heptagon-edge-34/45 (compositional qiso + Dunn assembly)
- ✅ **Universal Celestial Holography** — `thm:uch-main` at universal_celestial_holography.tex:213, ProvedHere at g=0; class-M chain-level via DS-Hoch bridge on the weight-completed ambient only, with g ≥ 1 conjectural per `conj:uch-gravity-chain-level`

### Platonic theorem upgrades inscribed (2026-04-17 session)

Individual theorem-level UPGRADE-SWEEP inscriptions now anchored in `.tex`:

- ✅ **Theorem A^{∞,2}** R-twisted $\Sigma_n$-descent — `prop:R-twisted-sigma-n-descent` at `chapters/theory/factorization_swiss_cheese.tex` (end of properad section); four-step proof (local system, YBE braid coherence, involutivity, descent via GR17 IV.5.4) plus `rem:ordered-symmetric-bar-primacy` closing FM69 critique.
- ✅ **Theorem C total shifted-symplectic** — `thm:theoremC-total-shifted-symplectic` at `working_notes.tex:~19475` (session-synthesis `subsec:theoremC-total-shifted-symplectic`); three-part statement (PTVV $-(3g{-}3{+}n)$-shifted symplectic on characteristic bundle, Lagrangian section via genus-wise complementarity, clutching compatibility across boundary strata); Heisenberg example; FM-attack heal noting the correct target is $\cQ(\cA) \oplus \cQ(\cA^!)$, not $\overline{\mathcal{M}}_{g,n}$ itself.
- ✅ **Theorem D tensor-Arakelov** — `thm:theoremD-tensor-arakelov` at `working_notes.tex:~19633` (session-synthesis `subsec:theoremD-tensor-arakelov`); tensor-valued $K \in \operatorname{Sym}^2(\cF^\vee) \otimes \Omega^2(\overline{\mathcal{M}}_{g,n})$; diagonal (UNIFORM-WEIGHT) = weight-$w$ Arakelov scalar, off-diagonal = cross-channel $\delta F_g^{\mathrm{cross}}$; tensor chiral Mumford formula; Virasoro example recovering scalar Theorem~D.
- ✅ **Theorem H chiral Higher Deligne** — `thm:theoremH-chiral-higher-deligne` at `working_notes.tex:~19800` (session-synthesis `subsec:theoremH-chiral-higher-deligne`); four-part statement (degree-$\le 2$ = classical chiral Deligne $E_2$ brace, degree-$\ge 3$ via heptagon edges 3$\leftrightarrow$4, concentration as $E_3$-rigidity consequence, $E_3$-topological via iterated Sugawara); class M chain-level via DS-Hoch bridge remark.
- ✅ **Part VIII shell** — `\part{From Frontier to Theorem}` at `main.tex:~1609` with intro referencing the four closed frontiers and inputting `chapters/theory/koszulness_moduli_M_kosz.tex` + `chapters/theory/infinite_fingerprint_classification.tex` (both newly created; not previously inputted into the main architecture).
- ✅ **Preface architectural upgrades** — six surgical edits at `chapters/frame/preface.tex`: seven parts $\to$ eight parts (Section~XI), $E_\infty$-topological ladder remark (Section~XI$''$), nine-face GRT$_1(\Q)$-torsor (Part~III description), G/L/C/M/FF five-class quaternitomy (Leap~2), two-theorems-native-to-Vol~II paragraph (Section~II). Pentagon$\to$heptagon was already in place at line~238.

## Cross-Volume Bridges

| Bridge | Vol II claim | Vol I anchor | Status |
|--------|-------------|--------------|--------|
| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved |
| DS-bar | Bar-cobar commutes with DS | ds-koszul-intertwine | Proved |
| Hochschild | BV-BRST origin of Thm H | Theorem H | Proved |
| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
| PVA-Coisson | PVA descent recovers Coisson | Deformation theory | Proved |
| W-algebras | Feynman-diag m_k matches bar diff | MC5 | (1) HS-sewing all genera; (2) genus-0 algebraic BRST/bar; (3) D^co-level BV=bar for ALL shadow classes incl. class M; (4) genuswise chain-level BV/BRST/bar PROVED in weight-completed category for all four classes (prop:bv-bar-class-m-weight-completed, 2026-04-16); direct-sum chain-level class M genuinely false on raw direct sum (AP203-healed); (5) tree-level amplitude pairing cond. on cor:string-amplitude-genus0; (6) **[2026-04-17 TEMPERED EXTENSION]** genuswise chain-level BV/BRST/bar extends to ORIGINAL COMPLEX unconditional on the NON-LOGARITHMIC C_2-cofinite standard landscape via the Banach completion B_ρ(A) at ρ < |c|/β_A (Virasoro β=6, W_N β=(N+1)(N+2)/2, Schellekens 71 via α=0, Monster V^♮, irrational cosets via VSKR+BGG), per thm:programme-climax (commit d1a4e7c) + tempered-stratum heal (commit a4277d7). Logarithmic W(p) triplet EXCLUDED at current scope: Zhu-bounded-Massey proof chain FAILS per Gurarie 1993 + Flohr 1996 unbounded Massey constructions; W(p) tempering OPEN pending direct Adamović-Milas character-amplitude bound (thm:tempered-stratum-contains-wp downgraded to Conjectured, commit a5640de). |
| Affine monodromy | C_line^red = Rep_q(g) on eval modules | Thm A + DK | Proved |
| Soft theorems | Shadow tower controls soft graviton hierarchy | Thm H | Proved g=0 |
| Two-colour | ordered → A^!_line, symmetric → A^!_ch | two-color-master | Proved |
| W_N Koszul | alpha_N generalizes c→26-c to all W-algebras | Koszul pairs | Proved |
| Wick anomaly | Genus tower measures Wick rotation breaking | Thm D | Proved genus tower |
| Annular bar-HH | B^ann computes HH^ch | Thm H | Proved |
| FG-shadow-strat | Commutator filtration spectral sequence | Shadow tower | Proved |
| Gauge-gravity | m_k=0 (gauge) vs m_k≠0 (gravity) dichotomy | G/L/C/M | Proved |
| 3D gravity | Part VI: 3d QG = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | E_3-top PROVED for KM (thm:E3-topological-km), ALL W-algebras (thm:E3-topological-DS-general), ALL freely-generated PVAs (thm:E3-topological-free-PVA). Global triangle: PROVED G/L/C (thm:global-triangle-boundary-linear); CLASS M CLOSED chain-level via DS-Hochschild compatibility bridge (thm:chd-ds-hochschild + cor:universal-holography-class-M, 2026-04-16 reconstitution). E_∞-topological ladder (Virasoro rung 1, W_N rung N-1, W_∞ rung ∞) stated as climax extension, Platonic form; chain-level rungs k≥3 conditional on higher-spin antighost construction. |

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make    # Vol II
cd ~/chiral-bar-cobar && make fast                           # Vol I
cd ~/chiral-bar-cobar && make test                           # Tests
```

## File Map

**Theory** (chapters/theory/): foundations, locality, axioms, equivalence, bv-construction, raviolo, raviolo-restriction, fm-calculus, orientations, fm-proofs, pva-descent-repaired, pva-expanded-repaired, factorization_swiss_cheese, modular_swiss_cheese_operad, introduction.

**Examples** (chapters/examples/): rosetta_stone, examples-computing, examples-worked, examples-complete-proved, examples-complete-conditional, w-algebras-virasoro, w-algebras-w3.

**Core Parts II-VI**: bar-cobar-review, line-operators, ordered_associative_chiral_kd_core, dg_shifted_factorization_bridge, thqg_gravitational_yangian, typeA_baxter_rees_theta, shifted_rtt_duality_orthogonal_coideals, casimir_divisor_core_transport (II); dnp_identification_master, spectral-braiding-core, ht_bulk_boundary_line_core, celestial_boundary_transfer_core, affine_half_space_bv, fm3_planted_forest_synthesis, kontsevich_integral (III); hochschild, brace, relative_feynman_transform, modular_pva_quantization_core, ht_physical_origins (IV); ym_synthesis_core, ym_boundary_theory, ym_higher_body_couplings, ym_instanton_screening, celestial_holography_core, log_ht_monodromy_core, anomaly_completed_core, holomorphic_topological, thqg_holographic_reconstruction, thqg_modular_bootstrap (V); thqg_gravitational_complexity, 3d_gravity, thqg_3d_gravity_movements_vi_x, thqg_critical_string_dichotomy, thqg_perturbative_finiteness, thqg_soft_graviton_theorems, thqg_symplectic_polarization (VI).

**Frontier** (chapters/connections/*_frontier): spectral-braiding, ht_bulk_boundary_line, celestial_boundary_transfer, w-algebras, modular_pva_quantization, ordered_associative_chiral_kd, ym_synthesis, celestial_holography, log_ht_monodromy, anomaly_completed.

**Frame + Appendices**: chapters/frame/preface, chapters/connections/conclusion, appendices/brace-signs.

## Vol III 6d hCS Session Cross-Awareness (2026-04-12/13)

**Anti-patterns applicable to Vol II (digest; full versions in Vol III CLAUDE.md)**:
- AP-CY23: E_1-chiral bialgebra uses Vol II's SC^{ch,top}. Δ_z lives on OPEN (E_1/topological) colour. CLOSED (E_2/chiral) colour carries no Hopf data — recovered via Drinfeld center.
- AP-CY25: R=(id⊗S)∘Δ(1) WRONG (→1⊗1 by counit). Use half-braiding σ_A(z)(a⊗n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)}.
- AP-CY26: σ_2 is EVEN under h_i→-h_i. k^!=-k from Shapovalov (Verdier transposes inner product), not σ_2 negation.
- AP-CY24: Docstring ground-truth confabulation — verify EVERY numerical value against function output.
- AP-CY27-33 (digest): agent sandbox non-persistence; pole-unsafe test points; wrong-repo writes; factored≠solved (ZTE); spectral z≠worldsheet z; reorganisation≠bypass; chain-level≠rational (E_3 is genuine at chain level but collapses to E_2 under Kontsevich formality).
- AP-CY34: Cyclic invariance ≠ bar-level compatibility. Individual {b_k, B^{(2)}}≠0 for non-formal. ONLY total {b,B^{(2)}}=0 via Costello TCFT. Cross-arity Stasheff cancellation. Obs_Ainf=0 universally in ∞-cat.

**Key results affecting Vol II (129-agent session, April 2026):**
- E_1-chiral bialgebra axioms (H1)-(H5) formalized in Vol III e1_chiral_algebras.tex §7. ALL spins verified. Coassociativity trivial via Miura multiplicativity.
- Universal coproduct Δ_z(e_s) = Σ (-1)^k C(N_R-b,k) z^k e_a^L·e_b^R for ALL spins — extends Vol II's spin-2 Drinfeld. z-degree at spin s = exactly s.
- ZTE failure proves E_3 genuinely nontrivial beyond E_2. ZTE deformation cohomology: S^{corr} EXISTS (rank 35/36 in extended complex).
- E_2→E_3: derived center HH*(B,B), NOT iterated Z(Z(C)).
- Shadow tower = A_∞ coproduct corrections: S_k = δ^{(k)} PROVED. Shadow-Feynman: L-loop = S_{L+1}.
- CY-A_3 PROVED in ∞-cat. [m_3,B^{(2)}]≠0 at chain level NOT an obstruction (HH^{-2}_{E_1}=0, Goodwillie vanishing, contractible space of liftings).
- Swiss-cheese SC^{ch,top} now has derived ∞-cat formulation via Vol III's thm:derived-framing-obstruction.
- Chiral CE complex: B(U^ch(L)) = CE_*(L) PROVED.
- **Class M E_3 bar: dim = 6^g (closed form via Kunneth). NOT infinite at cohomology. Chain: P(q)^{6g}.**
- **kappa_BKM = c_N(0)/2** is the ONLY correct universal formula (Borcherds weight theorem).

See ~/calabi-yau-quantum-groups/FRONTIER.md F13-F37 and CLAUDE.md. Vol III: ~693pp, ~34,000 tests, ~460 engines, 10 publication-standard proofs, clean build. CY-A_3 PROVED (∞-cat). K3 abelian Yangian PROVED. ZTE T matrix COMPUTED (exact rational, 35 tests). kappa_BKM = c_N(0)/2 universal. Class M E_3 bar = 6^g. Shadow tower through m_8 (160 tests, S_8=4144720/19683). m_5 independently verified (G_5^{conn}=775/5184). Chiral volume conjecture FORMULATED. Mock modular K3: THEOREM at d=2. CY-D dim-stratified: kappa_ch ≠ chi(O_X) at odd d. CY-C abelian: C(g,q) = D(Y^+(g_{K3})). BKM Serre P_2=0. E_8×E_8 structure function (24,24), c=24. N=2 root-of-unity: 324 modules, S-matrix degenerate. Mathieu: frame shape = twined bar Euler (all 25 M_24 classes). Incompatibility: μ_3≠0 forces μ_2=0 on aug.

## Cross-Volume Failure Modes (2026-04-14)

FM42 (Vol I): Bulk substring replace corrupts compound words (singularity→singuldegree). FM43: Φ outputs E_1 at d≥3, not E_2. FM44: >10 concurrent agents → rate limiting. FM45: Subagents lack full skill programme. FM46: Stale line counts in preface. See Vol I CLAUDE.md for full descriptions.

## Geometric vs Algebraic Model Conflations (AP-CY62-AP-CY67, Vol III 2026-04-16 swarm)

Relevant to Vol II (SC^{ch,top} uses derived center; D*/S^1 comparison; Drinfeld center vs derived center). Each AP has first-principles fact (inline) + trigger → counter.

**AP-CY62. Geometric vs algebraic chiral Hochschild model.** (a) C^*_{ch,geom}(A): sections over FM_{n+1}(X) with log forms, differential d_int + d_fact + d_config. (b) C^*_{ch,alg}(A): Prod_{n≥0} End^ch_A(n+1)[-n] with δf=[m,f]. Quasi-iso for logarithmic chiral algebras; genus ≥ 1 geometric model carries curve-dependent data algebraic lacks. The chiral Hoch comparison is a REMARK (rem:comparison-geometric-hoch), not named theorem. The bar comparison IS named (thm:geometric-equals-operadic-bar).

| Trigger | Counter |
|---------|---------|
| "C^*_ch(A,A)" without model qualifier | specify "geometric (FM)" or "algebraic (bar/operadic)" |
| "derived center Z^der_ch" without model when E_n claimed | same |
| Mixing FM integration with formal-variable language same paragraph | FIRE |

**AP-CY63. BD chiral operad vs algebraic End^ch.** BD: End^ch_M(n) = Hom_{D(X^n)}(j_*j^*M^{boxtimes n}, Δ_*M). Algebraic: End^ch_A(n) = Hom(A^{⊗n}, A((λ_1))...((λ_{n-1}))). Iso after formal-disk restriction + coordinate choice (4 steps: choose point, choose coord, trivialise D-mod, identify spectral vars with relative positions). Standalone Bridge Prop currently absent.

| Trigger | Counter |
|---------|---------|
| "the chiral endomorphism operad on FM_k(C)" | End^ch is algebraic, not on FM |
| "OPE data from configuration spaces" | correct geometric, wrong algebraic |
| "End^ch_A" mixing D-module with formal Laurent series | FIRE |

**AP-CY64. Three-way Hochschild confusion (ChirHoch/HH*/H*_GF).** (i) ChirHoch*(A): concentrated in {0,1,2} (Thm H). (ii) HH*(A_mode): concentrated in {0} for simple algebras (Weyl: dim=1). (iii) H*_GF(Lie(A)): Gel'fand-Fuchs continuous, unbounded polynomial. "Theorem H has no THH analogue" is FALSE in general (HH*(Weyl)=1-dim MORE concentrated); genuine "fails to concentrate" object is GF. At k=-h^v, ChirHoch* becomes infinite-dim (FF center); HH*(A_mode) stays finite — ONLY regime of genuine difference.

| Trigger | Counter |
|---------|---------|
| "ChirHoch finite while THH infinite" | FIRE — HH*(Weyl)=1-dim |
| "Theorem H has no classical analogue" | FIRE — HH* of Weyl MORE concentrated |
| "concentration fails for THH" | FIRE — confuses GF with THH |
| "GF agrees with ChirHoch" | FIRE — only at critical level |

**AP-CY65. Spectral parameter provenance.** Three-part origin: (a) Algebraic: A must have translation automorphism τ_z (creating eval modules V_u); (b) Geometric: in HT setup, τ_z = holomorphic translation on curve C (closed colour of SC^{ch,top}); (c) Rep-theoretic: R(z) depends on z=u-v. "Topological Drinfeld center has no spectral params" is FALSE — Yangian Y(g) as purely associative has eval modules V_u and spectral R(z=u-v) in Drinfeld center. Correct claim: chiral bar DIFFERENTIAL z-dependent (OPE residues); topological bar COPRODUCT z-independent (deconcat).

| Trigger | Counter |
|---------|---------|
| "spectral parameters from the chiral structure" | FIRE — from evaluation modules |
| "topological center has no spectral parameters" | FIRE — Yangian counterexample |
| "R-matrix R(z) comes from derived center" | FIRE — from evaluation modules |
| "E_2 braiding carries spectral parameters" | FIRE — braiding is single iso; z via representations |

**AP-CY66. BZFN ambient category not tunable.** Lurie HA 5.3.1.30: Z(LMod_A(S)) = LMod_{HH*(A,A)}(S); both sides use SAME S. Two derived centers arise from two DIFFERENT ALGEBRAS: A (chiral in IndCoh(Ran(X))) → C^*_ch(A,A); A_mode (mode alg in Vect) → HH*(A_mode,A_mode).

| Trigger | Counter |
|---------|---------|
| "applying BZFN in two different ambient categories" | FIRE |
| "same algebra viewed in D-modules vs Vect" | FIRE — DIFFERENT algebras |
| "varying S in BZFN" | FIRE — S not free parameter |

**AP-CY67. "Spectral parameters from FM_k(C)" is narration.** Spectral parameters in End^ch_A are FORMAL algebraic variables. Relationship to FM is mediated by local-global identification theorem (comparison, not definition). Three layers: (i) global geometric on FM_{n+1}(X); (ii) formal-disk restriction → relative positions λ_i; (iii) algebraic End^ch_A with formal vars.

| Trigger | Counter |
|---------|---------|
| "spectral parameters from FM_k(C)" | FIRE |
| "chiral endomorphism operad on FM_k(C)" | FIRE |

### Higher-order ramification guards (AP-CY62-AP-CY67)
Wrong reasoning chains using these as premises:
- "Because ChirHoch is finite-dim, Drinfeld center is finite" — WRONG (Drinfeld center is a CATEGORY, not a finite-dim object).
- "Spectral parameter distinguishes chiral from topological" — WRONG (Yangian Drinfeld center has spectral params despite being "topological").
- "Curve geometry is what makes QGs possible" — PARTIALLY RIGHT (curve creates τ_z → eval modules; but spectral params persist once Yangian is constructed, regardless of curve).

## Cross-Volume AP Index (curated subset; canonical = linked volume)

**Vol I APs full set: see ~/chiral-bar-cobar/CLAUDE.md.** Most-relevant-to-Vol-II subset inline below.

| AP# | One-line essence | Vol canonical |
|-----|------------------|---------------|
| AP2 | Read actual .tex proof, not CLAUDE.md description (descriptions ≠ ground truth) | Vol I |
| AP4 | ClaimStatusProvedHere: verify proof proves stated claim | Vol I |
| AP40 | Env matches tag: Conjectured→conjecture; ProvedElsewhere→theorem+Remark attribution | Vol I |
| AP5 | Grep ALL THREE volumes for variants after EVERY correction | Vol I |
| AP6 | Specify genus, degree, level (conv vs ambient) for D²=0, kappa, Theta_A | Vol I |
| AP7 | Before writing universal quantifier, verify no implicit type/genus/level restriction | Vol I |
| AP8 | NEVER "self-dual" unqualified. Virasoro self-dual at c=13 | Vol I |
| AP12 | When proving a claim, search entire manuscript for variants; update all same commit | Vol I |
| AP14 | **Koszulness ≠ SC formality.** Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k≥3. All standard families Koszul; only class G SC-formal | Vol I |
| AP17 | After any new theorem, IMMEDIATELY audit before next result | Vol I |
| AP18 | "Entire standard landscape" → list every family, check each against hypotheses | Vol I |
| AP30 | CohFT flat identity requires vacuum in V; always list conditional axioms at cross-ref | Vol I |
| AP32 | Genus-1 ≠ all-genera. obs_1=kappa·λ_1 unconditional. Multi-weight g≥2 scalar formula FAILS. Every obs_g/F_g/λ_g MUST carry tag (UNIFORM-WEIGHT) or (ALL-WEIGHT, w/ cross-channel correction) | Vol I |
| AP36 | "implies" proved, "iff" claimed → write "implies" until converse has independent proof | Vol I |
| AP39 | **kappa ≠ S_2 for non-Virasoro.** Heis_k: kappa=k (NOT k/2). Vir_c: kappa=c/2 (ONLY family w/ kappa=S_2/2). KM: kappa=dim(g)(k+h^v)/(2h^v) | Vol I |
| AP47 | Evaluation-generated core ≠ full category. MC3 proved on eval core; DK-4/5 downstream | Vol I |
| AP60 | Tag only genuinely new content ProvedHere; classical parts ProvedElsewhere + attribution | Vol I |
| AP67 | Strong gen ≠ FREE strong gen. W(p) has 4 strong gens but FREE strong gen OPEN | Vol I |
| AP105 | Heisenberg = abelian KM at level k = abelian CS boundary. Same OPE J(z)J(w)~k/(z-w)². Simple-pole needs ODD generator (symplectic fermion) | Vol I |
| AP106 | NEVER "This chapter constructs..." Open with PROBLEM. CG opening | Vol I |
| AP107 | r^coll(z) differs from Laplace-transform r(z) for odd generators | Vol I |
| AP108 | Heisenberg = CG opening, NOT atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA) | Vol I |
| AP109/111 | Never list results before proving. No "What this chapter proves" blocks | Vol I |
| AP113 | kappa without subscripts FORBIDDEN in Vol III. Always kappa_ch, kappa_BKM, kappa_cat, kappa_fiber | Vol III/I |
| AP114 | Stub chapters (<50 lines, no theorems) → develop or comment out | Vol I |
| AP126/AP141 | **Level-stripped r-matrix.** Affine KM at level k: r(z) = k·Omega/z, NOT Omega/z. 42+ instances across 3 volumes. THE MOST VIOLATED AP. After any r-matrix: verify k=0 → r=0; grep bare Omega/z | Vol I |
| AP136 | **Harmonic number notation trap.** H_{N-1} ≠ H_N - 1. H_{N-1} = Σ_{j=1}^{N-1} 1/j. H_N-1 = Σ_{j=2}^{N} 1/j. At N=2: H_1=1 but H_2-1=1/2. kappa(W_N) = c·(H_N - 1), NOT c·H_{N-1} | Vol I |
| AP138 | Degenerate graded Jacobi. ||m||=0: [[m,m],f]=0 tautological. [m,[m,f]]=½[[m,m],f] requires ||m|| ODD | Vol I |
| AP139 | Unbound variable in theorem — every variable in displayed equation MUST be quantified | Vol I |
| AP234 | Two-Koszul-conductors-same-letter. κ(A)+κ(A^!) (scalar complementarity) distinct from Trinity K(A)=c+c^!=-c_ghost(BRST). κ+κ^!=ϱ_A·K with family-dependent ϱ_A | Vol I |
| AP235 | quaternitomy/quadrichotomy drift. "quadrichotomy" canonical; grep "quaternitomy" after every G/L/C/M write | Vol I |
| AP236 | Blacklist-slug leakage (`/B\d+`) into typeset parentheticals via agent edits. Grep `\\textup\{\(\}\s*\/B\d+` before any .tex commit | Vol I |
| AP237 | Splitting-principle degree accounting. $\prod_i (\alpha x_i) = \alpha^g \prod x_i$ is a monomial in $\alpha$; no linear-in-$\alpha$ projection exists. Use $\alpha\cdot\lambda_{-1}(\mathbb{E})$ K-theoretic class instead | Vol I |
| AP238 | Statement/proof internal contradiction. Same object assigned different values within a single proposition-proof pair (AP10 variant, single-environment scope) | Vol I |
| AP239 | Naming-after-physical-source without geometric content. K3-X, Y(gl(4|20)), Monster-Y depend only on rank+signature; rename or annotate the redundancy | Vol I |
| AP240 | Closure-by-repackaging. "N gaps CLOSED" where the closure relocates the gap into cited remarks rather than independently resolving | Vol I |
| AP241 | Advertised-but-not-inscribed characterization. Preface/FRONTIER.md advertises equivalence clauses absent from the `.tex` theorem | Vol I |
| AP242 | Forward-reference lemma labelled as inscribed. `\ref{lem:foo}` with no matching `\label` across three volumes, or with a forward-reference body | Vol I |
| AP243 | HZ-IV decorator non-disjoint dependency. V1/V2/V3 paths share a hidden lemma/input. Cross-check literature citations per path | Vol I |
| AP244 | Overcounted foundational terms. N named notions where N-k are distinct on the working locus. 5 E_1-chiral notions → 2 (HEALED 2026-04-17 via Vol I `thm:e1-chiral-notions-collapse`: (A)/(B)/(C)/(E) mutually Quillen-equivalent on Koszul locus; only (D) remains open via `conj:double-ainfty-notion-D-relation`). G/L/C/M is a 2×2 Boolean grid (still pending) | Vol I |
| AP245 | Statement-proof-engine numerical agreement. Evaluate every numerical value at a common test point across statement / proof / engine before inscription; any mismatch = retraction (prospective guard for AP238) | Vol I |
| AP246 | Lattice signature $(p,q)$ → Lie-algebra type. Symmetric indefinite → $SO(p,q)$ or $OSP(p|q)$ via reflection equations, NOT $\mathfrak{gl}(p\|q)$ | Vol I |
| AP247 | Functor requires single target. $d$-indexed family with $d$-dependent target is a CORRESPONDENCE PROGRAMME, not a functor. CY-to-chiral $\{\Phi_d\}$ | Vol I |
| AP248 | Coloured dioperads vs operads. $\Sigma_n$-equivariance broken between colours → dioperad (Gan 2003) or wheeled properad (Merkulov-Vallette 2009), not operad. $SC^{ch,top}$ is a dioperad | Vol I |
| AP249 | Base-change / extension theorems require inscription, not citation. Promoting "fixed curve X" to "$\overline{\mathcal{M}}_{g,n}$" needs inscribed modular-family theorem | Vol I |
| AP250 | Algorithm uniformity requires per-type verification. FM q-characters, Nakajima quiver, Lusztig canonical: $G_2$, $F_4$ often fail uniformity | Vol I |
| AP251 | Attribution density floor. `ProvedHere` with zero classical citations = novelty-inflation suspect; either attribute or mark "not previously in the literature" | Vol I |
| AP252 | Chern / Taylor expansion degree direction. $\prod(1-e^{x_i})$ starts at degree $2g$, corrections go UP. "Lower-degree" is wrong (healed 2026-04-17) | Vol I |
| AP253 | Inter-volume dependency graph for "one programme". $<30$ cross-volume theorem citations = loosely coupled trilogy, not unified theory | Vol I |
| AP254 | Closure-date commit-floor. "N-agent wave on DATE" needs commit density $\geq N/10$ on DATE; otherwise retroactive-compression | Vol I |

### AP237-AP244 + HZ-11 Full Inscription (2026-04-17 Beilinson-audit wave)

(Registered in Vol II CLAUDE.md for complete local access; source of truth remains `/Users/raeez/chiral-bar-cobar/CLAUDE.md`. The compact one-line table above summarises; the bodies below are VERBATIM from the canonical Vol I entry and must stay synchronised across all three volumes.)

**AP237 (Splitting-principle degree accounting).** Product $\prod_{i=1}^g (\alpha \cdot x_i) = \alpha^g \prod x_i$ is a SINGLE MONOMIAL in $\alpha$, NOT a candidate for "scalar-channel linear-in-$\alpha$ extraction". When applying the splitting principle to extract a scalar-channel coefficient, verify the coefficient depends linearly in the scalar parameter. The correct route is a $K$-theoretic class $\alpha \cdot \lambda_{-1}(\mathbb{E})$ linear in $\alpha$ by construction, NOT a product-formula manipulation. Found at Vol I `higher_genus_foundations.tex:5742-5786` in `prop:scalar-obstruction-hodge-euler` Step 3d — Theorem D's "all-genera CLOSED" chain relies on this step. Counter: if you write $\alpha^g \prod x_i$ and claim "linear-in-$\alpha$ projection gives $\alpha \cdot c_g(\mathbb{E})$", STOP — that projection does not exist. Return to $K$-theoretic class Step 1c.

**AP238 (Statement/proof internal contradiction).** Same mathematical object assigned different numerical values within a single proposition-proof pair. Example: Vol III `cy_d_kappa_stratification.tex:1143` proposition STATEMENT writes $\kappa_{BKM}(\Phi_1) = 0 + 0 = 0$ (N=1 coincidence); proof at :1170-1171 writes $\kappa_{BKM}(\Phi_1) = 10$ (Φ_10 weight 10). Counter: before inscribing a proposition, numerically evaluate every symbol in statement AND proof at a common test point; discrepancy = retraction required.

**AP239 (Naming-after-physical-source without geometric content).** Programme systematically names objects after physical sources (K3, Y(gl(4|20)), Kummer) without verifying the geometric input is actually used beyond lattice rank/signature. Examples: (i) Y(gl(4|20)) is Mukai signature (4,20) symmetric indefinite → OSP(4|20) candidate, NOT gl(4|20) super-Yangian (Wave-2 F19); (ii) K3 abelian Yangian `thm:k3-abelian-yangian-presentation` depends only on rank-24 signature-(4,20) even unimodular lattice + CY_2 constraint — no K3-specific geometry enters beyond Mukai pairing. Counter: for every named object (K3-X, Monster-Y, CY-Z), list what geometric input beyond rank+signature is USED in the theorem; if none, rename to "rank-N sig-(p,q) X" with a remark noting physical source inspiration.

**AP240 (Closure-by-repackaging).** Claimed "N prior gaps CLOSED (date)" where inscribed closure repackages the gap into cited remarks rather than independently resolving. Example: Vol I Theorem D claim "All 3 prior gaps CLOSED (2026-04-16)" per CLAUDE.md Theorem Status — source-level inspection at `higher_genus_foundations.tex:6172-6229` shows the proof chain (a)-(d) exhibits fiberwise curvature = κ·ω_g^Ar, but step (b) "no higher Hodge bundle enters scalar channel" is ASSERTED via `rem:propagator-weight-universality`, not derived. AGENTS.md:566 SELF-DECLARES the gap. Counter: "N gaps CLOSED" requires INDEPENDENT resolution, not relocation into cited remarks. Audit each claimed closure: does the proof use any load-bearing `\ref{}` that itself asserts rather than derives?

**AP241 (Advertised-but-not-inscribed characterization).** Preface/FRONTIER.md/CLAUDE.md advertises a theorem component that is absent from the inscribed theorem. Example: "Tropical Koszulness" listed in CLAUDE.md Koszul 10+1+1 meta-theorem breakdown (Vol I `chapters/theory/chiral_koszul_pairs.tex` advertised equivalence); ZERO matches for "tropical" in the source file. Only appears in `preface_sections5_9_draft.tex:943` prose. Counter: every time CLAUDE.md lists an equivalence (i)-(xii), grep the target theorem's .tex home for the equivalence keyword; absence = the advertisement is heuristic not theorem.

**AP242 (Forward-reference lemma labelled as inscribed).** Load-bearing lemma cited in a proof as `\ref{lem:foo}` where either (a) the label `\label{lem:foo}` exists nowhere, or (b) the lemma body at the label is itself a forward-reference. Example: Vol I `thm:hochschild-concentration-E1` proof cites `lem:chiral-quadratic-koszul` as the chiral transport of Shelton-Yuzvinsky contracting homotopy — this lemma is load-bearing for Theorem H but the inscription is a forward reference, not proven at callsite. Counter: before inscribing a theorem, verify every `\ref{lem:...}` in the proof resolves to a `\label{lem:...}` with a proven body.

**AP243 (HZ-IV decorator non-disjoint dependency).** "Three disjoint independent-verification paths" claim where V1/V2/V3 share hidden lemma dependency. Example: `thm:bfn-phi-ade-identification` HZ-IV decorators cite V1 Kronheimer ALE + V2 BFN 2016 + V3 BKR01 derived McKay — but V1 Kronheimer is INPUT to V3 BKR01 (Kronheimer-Nakajima hyperkähler input to McKay correspondence theorem). Counter: for every HZ-IV block, list literature citations per path; cross-check that path-A citations do not appear as lemmas in path-B or path-C; shared papers = non-disjoint.

**AP244 (Overcounted foundational terms).** Programme has N+k named "distinct" foundational notions where only N are mathematically distinct. Example: 5 E_1-chiral notions (A strict ChirAss / B A_∞ in End^ch / C EK quantum VA / D A_∞ in E_1-chiral / E factorization on Ran^ord) — on the Koszul locus where the programme's theorems apply, (A)=(B)|_{strict}, (E)=(B) D-module-theoretic, (C)↔(B) via Drinfeld associator; only (B) and (D) are genuinely different, and (D) is labelled "open problem." 5 names → 2 objects. Also: 4 classes G/L/C/M are post hoc labels on a 2×2 Boolean grid ($C = 0$ vs $\neq 0$) × ($Q = 0$ vs $\neq 0$). Counter: for every "N foundational notions" claim, construct a concrete example (e.g., V_k(sl_2) at generic k) where ALL N notions yield distinct objects; if any two coincide on the programme's working locus, declare terminological collapse. HEALED 2026-04-17 (E_1-chiral instance) — Vol I `thm:e1-chiral-notions-collapse` in `chapters/theory/algebraic_foundations.tex` proves (A)/(B)/(C)/(E) mutually Quillen-equivalent on Koszul locus via Stasheff truncation + Etingof-Kazhdan + Beilinson-Drinfeld D-module realization; (D) remains open (`conj:double-ainfty-notion-D-relation`). Operational registry: two notions. The G/L/C/M 2×2 Boolean grid instance remains pending.

### 2026-04-17 Preventative Anti-Patterns (AP245-AP254) — Full cross-inscription

(Source of truth: `/Users/raeez/chiral-bar-cobar/CLAUDE.md` §AP245-AP254. Bodies VERBATIM; must stay synchronised across all three volumes per the 2026-04-17 directive.)

**AP245 (Statement-proof-engine numerical agreement).** Every proposition carrying a numerical value must be evaluated at a common test point across (a) statement body, (b) proof body, (c) compute engine; any mismatch forces retraction before inscription. Canonical violation: $\kappa_{BKM}(\Phi_1)$ at Vol III `cy_d_kappa_stratification.tex:1143/1170-1171` — statement gave 0, proof gave 10, engine `compute/lib/kappa_bkm_universal.py:396-401` gave 5; correct value is 5 via Gritsenko 1999 $\Delta_5$ (weight-5 paramodular form of level 1). Counter: before inscribing a proposition with a numerical value, grep for the proposition's claim across statement / proof / engine and reject on any inconsistency. Relation to AP238: AP238 is the retrospective diagnostic; AP245 is the prospective guard.

**AP246 (Signature type-assignment discipline).** A lattice signature $(p, q)$ determines the Lie-algebra type of any Yangian attached to it. Mukai signature $(4, 20)$ is symmetric INDEFINITE (orthogonal form), giving the orthogonal series $O(p, q)$ or the orthosymplectic super series $OSP(p|q)$ (Arnaudon-Crampé-Doikou-Frappat-Ragoucy 2003, arXiv:math/0304188), NOT the general linear GL(p|q) or super-linear $\mathfrak{gl}(m|n)$. Counter: before naming a Yangian from a lattice signature, verify (i) symmetric indefinite → $SO(p,q)$ Yangian or $OSP(p|q)$ super-Yangian via reflection equations; (ii) symplectic → C-type Yangian; (iii) Z/2-supergraded with parity swap → $GL(m|n)$ super-Yangian. $Y(\mathfrak{gl}(4|20))$ was a naming artifact (AP239); correct candidate is $Y_{osp}(4|20)$.

**AP247 (Functor terminology requires single target).** A functor $\Phi: \mathcal{C} \to \mathcal{D}$ requires a SINGLE target category $\mathcal{D}$. A $d$-indexed family $\{\Phi_d\}$ with $d$-dependent target $\mathcal{D}_d$ is a CORRESPONDENCE PROGRAMME, not a functor. Counter: before using "functor" terminology, verify (a) single unified target category; (b) morphism action defined; (c) composition verified on a concrete morphism pair (e.g., Mukai transform K3 → K3 for d=2). CY-to-chiral $\Phi$ failed all three; correct terminology is "CY-to-chiral correspondence programme $\{\Phi_d\}_{d \geq 1}$". Relation to AP244: this is the terminological-inflation diagnostic specialised to functor claims.

**AP248 (Coloured dioperads vs operads).** When $\Sigma_n$-equivariance fails between colours (e.g., closed-to-open but not open-to-closed), the correct term is DIOPERAD (Gan 2003, arXiv:math/0210098) or WHEELED PROPERAD (Merkulov-Vallette 2009, arXiv:0907.2895), NOT operad. Dunn additivity does not apply to coloured structures with directional restriction. $SC^{ch,top}$ was mislabeled as an operad; it is a two-coloured dioperad with directional colour-restriction. Counter: before writing "P is an operad" for any coloured structure, verify all $\Sigma_n$-equivariances; colour-restricted equivariance = dioperad.

**AP249 (Base-change / extension theorems require inscription, not citation).** CLAUDE.md theorem-status labels cannot promote a theorem from "on fixed curve X" to "over $\overline{\mathcal{M}}_{g,n}$ including boundary" without an inscribed modular-family theorem. Base-change via six-functor formalism (Francis-Gaitsgory GR17 Vol II) must be INSCRIBED or marked `\ClaimStatusProvedElsewhere` with explicit attribution, not silently cited. Theorem A was advertised "modular-family PROVED 2026-04-16", but the inscribed `thm:A-infinity-2` is on fixed curve only; the modular-family extension was cited but not inscribed. Now healed to "PROVED unconditional on fixed smooth curve X; modular-family extension CONDITIONAL on GR17". Counter: for every claim "theorem extends from $X$ to $\overline{\mathcal{M}}_{g,n}$", locate either a local inscription or an explicit `\ClaimStatusProvedElsewhere` attribution; absence = the extension is rhetorical.

**AP250 (Algorithm uniformity requires per-type verification).** When citing an algorithm (Frenkel-Mukhin q-characters, Nakajima quiver variety, Kashiwara crystal basis, Lusztig canonical basis) as uniform across type classification (A/B/C/D/exceptional), verify per-type validity. Non-simply-laced exceptionals ($G_2$, $F_4$) often fail uniformity per Hernandez 2006 (arXiv:math/0606381) + Nakajima 2001+. The claim "FM algorithm gives true q-character for all simple types" is FALSE for $G_2$, $F_4$; per-case verification required. Counter: before writing "uniformly in type", list the types and cite the per-type reference; absence = the uniformity is aspirational.

**AP251 (Attribution density floor).** A theorem marked `\ClaimStatusProvedHere` without $\geq 1$ load-bearing citation to a classical source is suspect of novelty-inflation. Programme-wide novelty audit (2026-04-17) found 37% classical recast without explicit attribution (Drinfeld 1985, Frenkel-Jing 1988, Kac-Peterson 1984, Gritsenko-Nikulin 1995, Borcherds 1998, DMVV 1997, Gannon 2016 absent from Vol III K3 Yangian theorem bodies). Counter: every `ProvedHere` theorem's proof must cite $\geq 1$ classical input; zero citations = either mark as "to the best of our knowledge, not previously in the literature" or inscribe the missing attribution (AP251 violation).

**AP252 (Chern character / Taylor expansion degree direction).** $\prod_{i=1}^g (1 - e^{x_i}) = \prod_{i=1}^g (-x_i + O(x_i^2))$ begins at degree $2g$ (top-degree monomial $(-1)^g \prod x_i$); higher-order corrections from $O(x_i^2)$ terms live in degree strictly GREATER than $2g$. "Lower degree" is wrong. Similarly $(1-t)^{-1} = \sum_n t^n$ expands UPWARD. Counter: before writing "lower-degree corrections" or "higher-degree corrections" in a Chern character / Taylor / splitting-principle expansion, substitute $x_i = 0.01$ numerically and verify the expansion direction. Vol I `higher_genus_foundations.tex:5505` had "lower degree" where "higher degree" was meant (healed 2026-04-17).

**AP253 (Inter-volume dependency graph for "one programme" claim).** Before claiming "one programme" across multiple volumes, verify cross-volume load-bearing citation count. Sparse dependency graph ($< 30$ cross-volume theorem citations) = loosely coupled trilogy, not unified theory. Counter: grep each volume for `\ref{V[0-9]-thm:}` or `\ref{V[0-9]-prop:}`; if Vol I contains zero references to Vol II or Vol III theorems, information flow is strictly forward and the "one programme" framing is rhetorical. Downgrade to "three-volume series" until the dependency count crosses threshold.

**AP254 (Closure-date commit-floor).** Any "closure wave" or "N-agent session" claim attributing theorem closures to a specific date must have commit density $\geq N/10$ on that date (conservative batching factor). "Wave 14 closure 2026-04-16" produced 3 commits programme-wide — implying retroactive-compression. Counter: narrative wave labels are project-management shorthand, not synchronized mathematical events; status-table "PROVED (date)" entries should reference the inscription-commit date of the theorem body, not the rhetorical wave label. Audit: `git log --since=DATE --until=DATE+1day --oneline | wc -l` must match claimed agent count / 10.

**Cache entry references (Vol I `notes/first_principles_cache_comprehensive.md`, Patterns 226-229, task-directive "#222-#225"):** Pattern 226 Mukai signature → orthogonal/orthosymplectic series (AP246 companion); Pattern 227 Taylor / Chern-character expansion degree direction (AP252 companion); Pattern 228 Venue inflation at ~2× realistic (AP251 companion); Pattern 229 Physical-source name vs used geometric content (AP239/AP246 companion). Local numbering 226-229 (not 222-225) avoids collision with pre-existing Patterns 222-225 in the cache; the four new entries are authored 2026-04-17.

**HZ-11 (Cross-volume ProvedHere discipline).** Vol N `\ClaimStatusProvedHere` theorem whose proof invokes `\ref{prop:...}` or `\ref{lem:...}` must pass atomic check: grep all three volumes for the `\label{}`; if label lives outside Vol N, either (a) inscribe locally, or (b) downgrade to `\ClaimStatusConditional` with explicit `ProvedElsewhere` attribution remark. Example: Vol I `thm:lagrangian-complementarity-global-upgrade` clause (iv) cites `prop:modular-bootstrap-to-curved-dunn-bridge` — ZERO `\label` hits in Vol I; lives only in Vol II `curved_dunn_higher_genus.tex:138`. Constitutional AP4/AP60 violation. Recommend `make verify-crossvolume-provedhere` commit-gate.

**Vol I HOT ZONE addition (compact pointer):** HZ-11 (Cross-volume ProvedHere discipline, 2026-04-17). Any Vol II `\ClaimStatusProvedHere` theorem whose proof cites a `\ref{prop:...}` or `\ref{lem:...}` whose `\label` lives in Vol I or Vol III must either (a) inscribe the prop/lemma locally in Vol II, or (b) downgrade to `\ClaimStatusProvedElsewhere` with explicit Remark[Attribution]. Grep gate before committing a ProvedHere theorem: for each `\ref{prop:X}`/`\ref{lem:X}` in the proof body, verify `\label{prop:X}`/`\label{lem:X}` hits are present in `/Users/raeez/chiral-bar-cobar-vol2/chapters/`, `standalone/`, `appendices/`. Zero local hits with nonzero cross-volume hits = HZ-11 violation; downgrade or inscribe. Canonical specification in `/Users/raeez/chiral-bar-cobar/CLAUDE.md` §HZ-11.

**Vol I FMs digest (relevant to Vol II):**
- **FM24**: B-cycle i² error (see Unified Error Catalogue above).
- **FM42**: Bulk substring replacement corruption. `replace_all` "arity"→"degree" corrupts singularity→singuldegree, complementarity→complementdegree, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity, popularity, circularity, hilarity. 45 corruptions fixed in Vol III campaign. Counter: NEVER bulk-replace short strings inside common words; after any bulk replace, grep `ldegree|ndegree|rdegree|pdegree|tdegree`.
- **FM43**: Φ outputs E_1 at d≥3, not E_2. Always write `E_n-ChirAlg` with scope (n=2 for d≤2; n=1 for d≥3).
- **FM44**: >10 concurrent agents → rate limiting (31 launched, 27 rate-limited). Launch in batches of ≤3.
- **FM45**: Subagents receive ~200-word brief, not full 15,000-word skill. For full rectification, invoke skill directly.
- **FM46**: Stale preface/intro line counts. After large campaigns, update with `wc -l`.

**Vol III APs full set: see ~/calabi-yau-quantum-groups/CLAUDE.md.** Most-relevant-to-Vol-II subset inline below.

| AP# | One-line essence | Vol canonical |
|-----|------------------|---------------|
| AP-CY1 | CY dimension d ≠ complex dim n. Fuk(X)/D^b(Coh(X)) is CY_n (not 2n) | Vol III |
| AP-CY2 | CY trace in HC^-_d(C), NOT just HH_d→k. Negative cyclic for S^d-framing | Vol III |
| AP-CY3 | E_2 ≠ commutative. E_2 braiding NOT symmetric. E_2→E_∞ loses QG | Vol III |
| AP-CY4 | Drinfeld center Z(C) (monoidal cat) ≠ derived center Z^der_ch(A) (chiral). State which | Vol III |
| AP-CY5 | Kazhdan-Lusztig requires root of unity. Generic q: Rep_q(g) semisimple | Vol III |
| AP-CY6 | A_X for CY3 EXISTS in ∞-cat (thm:derived-framing-obstruction, Apr 2026). Chain-level open for non-formal. Results using ∞-cat: theorem OK; chain-level required: conjecture | Vol III |
| AP-CY7 | CoHA ≠ E_1-chiral algebra (CoHA is associative) | Vol III |
| AP-CY8 | Borcherds denominator ≠ bar Euler product. Identification needs CY-to-chiral functor | Vol III |
| AP-CY10 | Flop ≠ Koszul dual. Flop preserves kappa; Koszul: kappa(A)+kappa(A^!)=rho_K. kappa(A_X)=kappa(A_{X+}) for flop | Vol III |
| AP-CY11 | CY-A_3 PROVED now. Results through CY-A_3 no longer conditional. Through CY-C or chain-level A_X: still conjecture | Vol III |
| AP-CY12 | Shadow class from FULL computation, not generator count. Non-formality m_3≠0 does NOT determine depth. local P^2 is class M | Vol III |
| AP-CY13 | Part number staleness. grep 3 volumes after any restructuring. 7+ stale refs survived one restructuring | Vol III |
| AP-CY14 | Post CY-A_3 proof: A_X(d=3) EXISTS ∞-cat; G(X), C(g,q) UNCONSTRUCTED. Through G(X)/C(g,q) → conjecture | Vol III |
| AP-CY16 | Matrix size conflation. Sp_4 quot by ±I_4 (4×4); O(Λ^{3,2}) quot by ±I_5 (5×5) | Vol III |
| AP-CY17 | MF(W) CY dim = n-2 NOT n-1 (Dyckerhoff). ADE in 2 vars: CY_0. Need 4 vars for CY_2 | Vol III |
| AP-CY21/AP-CY38 | **E_3 bar dims RESOLVED.** Tricomplex P(q)^{3g} chain-level. Cohomology by class: G: P(q)^{3g}; L: (1+t)^{3g}=2^{3g}; C: 2^{3g} (charge conservation kills d_4); **Class M: 6^g** (Kunneth; d_4 survives → 6=2·3 per handle; g=1 gives [0,3,3,0]). NEVER (1+t)^{3g} for class M | Vol III |
| AP-CY22 | Miki automorphism algebra-specific, not operadic. S_3 perm of (q_1,q_2,q_3) from CY torus Weyl. k[x]/(x²) is E_3 but no Miki | Vol III |
| AP-CY30 | **Factored ≠ solved** (ZTE). S_{ijk}=R_{ij}R_{ik}R_{jk} from YBE-satisfying R does NOT satisfy tetrahedron (thm:zte-failure, O(κ²) obstruction). K-V theorem requires E_∞; Ω-deformation breaks it | Vol III |
| AP-CY31 | Spectral z ≠ worldsheet z. Δ_z (Yangian spectral) vs OPE T(z)T(w)~c/2·(z-w)^{-4} (worldsheet). DIFFERENT objects | Vol III |
| AP-CY33 | Chain-level ≠ rational. E_3 genuine chain-level; collapses to E_2 under Kontsevich formality (rational). Physics lives chain-level | Vol III |
| AP-CY34/AP-CY44 | **kappa_ch ≠ chi(O_X) at odd d.** Any compact CY_d odd: chi(O_X)=0 (Serre). kappa_ch = chi(O_X) PROVED ONLY for CY_2 with h^{1,0}=0. At d=3: dimension-stratified (conj:cy-kappa-identification). 76 tests in cy_d_kappa_d3.py | Vol III |
| AP-CY35 | B^{(j)} hierarchy. B^{(0)}=Connes B (mixed complex). B^{(j≥1)}=Connes hierarchy (S^d-framing). Mixed-complex [b,B^{(0)}]=0 does NOT extend to j≥1. Three "proofs" wrong from this | Vol III |
| AP-CY36 | kappa_ch formula: Σ(-1)^i dim HH_i = chi_top (24 for K3), NOT kappa_ch (=2). Correct: Hodge-filtered supertrace Σ(-1)^q h^{0,q}. Serre kills non-F^0 | Vol III |
| AP-CY37 | **kappa_BKM = c_N(0)/2 is universal** (Borcherds weight theorem). kappa_BKM = kappa_ch + kappa_cat is coincidence for N=1. Fails 7/8 diagonal Siegel orbifolds | Vol III |
| AP-CY39 | **Incompatibility Theorem.** Single-object cyclic A_∞ CY_3: μ_3≠0 forces μ_2=0 on aug ideal. Cross-arity cancellation IMPOSSIBLE at naive level. TCFT B^{(2)} differs from naive pairwise contraction | Vol III |
| AP-CY40 | ProvedHere MUST have \begin{proof} block within 50 lines | Vol III |
| AP-CY42 | phi_{0,1} normalization. c(-1)=1 (Gritsenko-Nikulin std) vs c(-1)=2 (K3 elliptic genus = 2·phi_{0,1}). Factor = kappa_ch(K3) | Vol III |
| AP-CY43 | Shadow-Feynman tautology at L≥4. Feynman engine calls shadow recursion. For L≥4, independent path (e.g. k-pt conformal blocks) | Vol III |
| AP-CY45 | N=2 root-of-unity gives TRIVIAL double braiding. q²=1 at N=2. Non-abelian MTC needs N≥3 where q²≠1 | Vol III |
| AP-CY46 | PROVED NEGATIVE: no native CY_4 Yangian (π_4(BU)=Z Pontryagin BLOCK-obstruction to E_4). CONSTRUCTED: p_1-twisted double current algebra as chain-level P^1-family model (Vol III `constr:phi-4-p1-family`). CONJECTURED: associator coherence verified at sextic order only (`conj:cy4-p1-family-associator-sextic`). Cascade max = E_3 at d=4 via this construction; "ALL d≥3" unqualified claim is SCOPE-RESTRICTED to d=4 constructed case + cases where analogous p_1-twist is verified. d≥5 open | Vol III |
| AP-CY47 | Structure function degree from Mukai rank, NOT Lie dim. E_8×E_8: (24,24) from 24 Mukai directions, NOT (500,500) | Vol III |
| AP-CY48 | 3d→6d lift rate 24%. Algebraic lifts 100%, topological 0%. 6d NOT a dim upgrade of 3d | Vol III |
| AP-CY53 | π_1(Conf_2) ordered vs unordered. π_1(Conf_2(R^d))=0 for d≥3 (ORDERED); π_1(UConf_2(R^d))=Z/2 (UNORDERED) | Vol III |
| AP-CY54 | "Categorified averaging" for Drinfeld center WRONG. Z = right adjoint to forgetful BrMon→Mon (categorified commutant). Averaging E_1→E_∞ DESTROYS QG data; center E_1→E_2 CONSTRUCTS braiding via half-braidings | Vol III |
| AP-CY55 | kappa_cat=chi(O_X), kappa_fiber=rank(Λ) are TOPOLOGICAL manifold invariants, NOT properties of algebraization. Only kappa_ch, kappa_BKM depend on algebraization. Never assert "algebraizations share kappa_cat" as meaningful | Vol III |
| AP-CY56 | E_n level conflation across CY dim. At d=3, A=Φ_3(C) is E_1 (NATIVE). E_2 lives on Z(Rep^{E_1}(A)) NOT on A. GB degree = 1-d: d=1→E_∞, d=2→E_2, d≥3→E_1 | Vol III |
| AP-CY57 | Narration instead of construction. R-matrix IS universal half-braiding σ_M(N):M⊗N→N⊗M in Z(Rep^{E_1}(A)). Constructed from center, not "given by" | Vol III |
| AP-CY58 | CY-B E_n scope d-DEPENDENT: E_2-Koszul at d=2; E_1-Koszul at d=3 (inducing E_2 on center via Verdier) | Vol III |
| AP-CY59 | Multiple algebraizations from SINGLE functor. Φ(D^b(Coh(K3)))=H_{Muk} PERIOD. BKM g_{Δ_5} from Borcherds lift (DIFFERENT). Conway from Leech lattice VOA (DIFFERENT) | Vol III |
| AP-CY60 | Six routes to G(K3×E) = six DIFFERENT constructions (Φ, Borcherds lift, lattice VOA, Kummer, sigma model, BLLPR). Convergence is CONTENT of CY-C (conjectural) | Vol III |
| AP-CY61 | Shallow correction without first-principles [= AP158 above — one canonical statement] | Vol III |

**Vol III workflow APs (mostly process, digest only):** AP-CY15 README scope inflation; AP-CY18 lattice theta series direct computation; AP-CY19 Â-hat /2 in argument (radius 2π); AP-CY20 normal bundle vs spectral params via Ω-background; AP-CY23/25/26 bialgebra/R-matrix/σ_2 (see Cross-Awareness section); AP-CY27-33 workflow hazards (see Cross-Awareness digest); AP-CY41 internal contradictions from partial upgrades; AP-CY49 tautological tests; AP-CY50 duplicate agent launches; AP-CY51 rate-limited engines on disk; AP-CY52 mega-file anti-pattern (>3000 lines split).

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
