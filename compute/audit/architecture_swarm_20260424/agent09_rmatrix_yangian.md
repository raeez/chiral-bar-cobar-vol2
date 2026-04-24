# Agent 09 report: r(z), Yangian, RTT, seven/nine faces

Date: 2026-04-24.

Scope owned: `compute/audit/architecture_swarm_20260424/agent09_rmatrix_yangian.md`.
No shared TeX was edited.

## Source surface read

- Vol II doctrine: `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`.
- Live Vol II anchors: `main.tex`; `chapters/theory/grt_parametrized_seven_faces.tex`; `chapters/theory/unified_chiral_quantum_group.tex`; `chapters/theory/super_chiral_yangian.tex`; `chapters/connections/spectral-braiding-core.tex`; `chapters/connections/spectral-braiding.tex`; `chapters/connections/typeA_baxter_rees_theta.tex`; `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex`; `chapters/connections/casimir_divisor_core_transport.tex`.
- Vol I anchors: `~/chiral-bar-cobar/chapters/examples/landscape_census.tex`; `yangians_foundations.tex`; `yangians_drinfeld_kohno.tex`.
- Compute anchors: Vol II `collision_residue_rmatrix.py`, `non_simply_laced_rmatrix.py`, `test_super_chiral_yangian.py`; Vol I Yangian RTT/residue/bar tests.

## Verification commands

- `~/chiral-bar-cobar/compute/.venv/bin/python -m pytest compute/tests/test_yangian_rtt_all_types.py compute/tests/test_yangian_residue.py compute/tests/test_yangian_bar.py -q -ra`
  - Result: `224 passed in 5.97s`.
- `compute/.venv/bin/python -m pytest compute/tests/test_super_chiral_yangian.py -q -ra`
  - Result: `9 passed in 0.02s`.
- `compute/.venv/bin/python -m pytest compute/tests/test_collision_residue_rmatrix.py -q -ra`
  - Result: `48 passed in 24.25s`.
- Attempted combined Vol II batch `test_collision_residue_rmatrix.py test_non_simply_laced_rmatrix.py test_super_chiral_yangian.py`; stopped after several minutes at partial progress to avoid leaving a long-running process. No conclusion drawn from that interrupted batch.
- Ambient shell note: bare `python` is absent; system `python3` lacks `pytest`; repo virtualenvs were used.

## ATTACK -> HEAL cycles

### 1. Casimir/level bridge: chained equality is still used as a proof input

ATTACK. The Vol II GRT chapter correctly says the chained equality is not a rational-function identity, but then keeps treating the bridge as a finite gauge equivalence:

- `chapters/theory/grt_parametrized_seven_faces.tex:480-524`: compares
  `r^tr(z)=k Omega_tr/z` with `r^KZ(z)=Omega/((k+h^\vee)z)`.
- `chapters/theory/unified_chiral_quantum_group.tex:785-820`: proves the MC statement using the bridge identity
  `k Omega_tr = Omega/(k+h^\vee)`.
- Vol I still has the stale form at `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:381-388` and table text at `:685`.

Failure mode. Algebraically, after `Omega_tr = Omega/(2h^\vee)`, the trace-form expression is
`k Omega/(2h^\vee z)`. It is not equal to `Omega/((k+h^\vee)z)` under the additive level shift `k -> k+h^\vee`; equality would impose `k(k+h^\vee)=2h^\vee`, not a convention. The k=0 check exposes the mismatch: trace-form collision residue gives zero, KZ normalization gives nonzero `Omega/(h^\vee z)`.

HEAL. Split three objects:

- OPE collision residue: `r_OPE(z)=k Omega_tr/z`.
- KZ/conformal-block connection coefficient: `r_KZ(z)=Omega_Kill/((k+h^\vee)z)`.
- Scalar obstruction characteristic: `kappa(V_k(g))=dim(g)(k+h^\vee)/(2h^\vee)`.

The bridge is a comparison of normalized connection conventions after Sugawara/KZ transport, not a tensor identity in one level coordinate. Downgrade any proof using `k Omega_tr = Omega/(k+h^\vee)` as an equality. Recommended status: `prop:grtfin-casimir` may remain proved only for the Casimir tensor rescaling `Omega_tr = Omega/(2h^\vee)`; the level comparison should be `ClaimStatusProvedElsewhere` or `ClaimStatusConditional` with explicit KZ-connection scope. `thm:r-matrix-from-MC` must not use the chained equality in its proof.

### 2. GRT(Q)-torsor and motivic face: coefficient field is wrong

ATTACK. The GRT chapter asserts a free transitive `GRT(Q)` action on the full face space and lists F8/F9 as Q-rational orbit representatives:

- `grt_parametrized_seven_faces.tex:160-184`, `:271-289`.
- F8 proof: `:640-656`, especially the passage from motivic MZVs to `GRT(Q)`.
- F9 proof: `:675-704`.
- Main overview: `main.tex:1887-1902`.

Failure mode. Brown's motivic associator lives over motivic periods/MZVs, not canonically in `GRT(Q)`. The real period realization lands over a period field (or `R`), not `Q`; choosing an MZV basis does not turn the associator into a rational point. Conversely, Willwacher gives `H^0(GC_2)=grt_1` over `Q` at the Lie-algebra level. These are compatible only after naming the scalar extension. The present text conflates:

- rational associator torsor;
- motivic-period associator torsor;
- cohomological binary residue, where associator data may disappear.

HEAL. State the theorem over a coefficient field `K`:

`Face_K(A)` is a torsor under `GRT_1(K)` after fixing a formality base point and a chain model.

Then specialize:

- historical F1-F7: rational/finite-gauge representatives where actually verified;
- F8: motivic-period face in `Face_{Z^mot}` or after realization in `Face_R`;
- F9: graph-complex/operadic face over `Q`;
- F8/F9 comparison: same orbit only after scalar extension to a common coefficient field.

Recommended status: master torsor theorem should be split. The abstract Tamarkin-Willwacher torsor is `ClaimStatusProvedElsewhere`; the concrete "all nine Q-rational representatives" statement should be downgraded.

### 3. MZV invisibility contradicts the advertised motivic r(z)

ATTACK. The chapter proves that the MZV tail is invisible to the binary residue:

- `grt_parametrized_seven_faces.tex:361-404`.
- Standing qualifier: `:839-869`.

But the same surface advertises motivic corrections inside `r(z)`:

- `main.tex:1900-1902`: `r^mot = r^rat + sum zeta(w) r^(w)`.
- `grt_parametrized_seven_faces.tex:640-656`: nontriviality of F8 lies in bar-degree `>=3`.
- `grt_parametrized_seven_faces.tex:332-337`: F7 on class M acquires MZV corrections at weight `>=3`, while `:283-288` says F1-F7 are finite-gauge.

Failure mode. The binary collision residue cannot both kill all weight `>=3` associator data and carry an MZV expansion in the same object `r(z)`. The correct split is already latent in the qualifier: cohomological binary `r(z)` is associator-independent; cochain-level higher operations depend on associator.

HEAL. Reserve `r(z)` for the binary degree-2 collision residue. Move motivic/graph corrections to `Theta_A^{>=3}`, `m_3`, or a named cochain-level lift `r(z)|^Phi` only when the degree is explicit. Amend the face theorem:

- F1-F6 and F7 on the Gaudin/simple-pole locus can be finite-gauge.
- F7 prime on class M is a higher `A_infty` operation and not a finite-gauge binary face.
- F8/F9 are higher-degree cochain faces, not new binary residues.

Recommended status: keep MZV invisibility as proved for cohomological binary `r(z)`; downgrade any statement putting MZVs in binary `r(z)`.

### 4. R(z)=exp(r(z)) and RTT sign conventions are inconsistent

ATTACK. The spectral-braiding chapter defines `r(z)` as a degree-1 "Spectral R-Matrix" and identifies `R(z)=exp(r(z))`:

- `spectral-braiding-core.tex:534-560`.

But the same chapter later distinguishes OPE-derived and independent quantum `R`-matrix provenance:

- `spectral-braiding-core.tex:567-582`.

The Yangian sign convention also changes across files:

- Vol I RTT: `~/chiral-bar-cobar/.../yangians_foundations.tex:337-345` uses `R=1-hbar P/u+...`.
- Vol I benchmark: `yangians_drinfeld_kohno.tex:6885-6892` uses `R=1-hbar P/u` but says `r=hbar P/z`.
- Vol II type-A: `typeA_baxter_rees_theta.tex:400-404` uses `1-hbar P/z`; `:1540-1552` uses `1+hbar P/u` and then declares classical `r=-P/u`.
- Vol II shifted RTT: `shifted_rtt_duality_orthogonal_coideals.tex:451-453` uses `1-hbar P/u`, while `:1129-1133` uses `1+hbar P/(u-v)`.
- Vol II spectral core: `spectral-braiding-core.tex:2086-2100` uses `1+hbar P/u`.

Failure mode. For nonabelian Yangian-type quantization, `R` is not canonically `exp(r)`; the quantization data and associator matter. `log R` can be chosen in an hbar-adic/pronilpotent setting, but it is not the same as the classical `r` without higher corrections. The sign of the classical `r` is also not globally fixed.

HEAL. Lock one convention at the architecture level. Either:

- `R(u)=1-hbar P/u+O(hbar^2)`, hence `r(u)=-P/u`; or
- `R(u)=1+hbar P/u+O(hbar^2)`, hence `r(u)=+P/u`.

Then propagate the sign through Vol II and compare to Vol I before editing. Replace global `R=exp(r)` by:

`R(z;hbar)=1+hbar r(z)+O(hbar^2)`.

Permit `R=exp(hbar r)` only in scalar/pronilpotent examples after saying a logarithm has been chosen. Separate algebraic degree from bar-desuspended degree: standard classical `r` is degree 0 as an algebra tensor; its bar representative may be degree 1 after desuspension.

Recommended status: sign-convention remarks are `ClaimStatusProvedElsewhere`; any theorem depending on the current mixed sign should be held conditional until the convention lock is propagated.

### 5. Shifted RTT "orthogonal coideal" theorem proves only differential stability

ATTACK. The shifted RTT chapter proves:

- `shifted_rtt_duality_orthogonal_coideals.tex:731-740`: `C_{-\mu,\lambda}^{(N)}` is a dg subcoalgebra/coideal.
- Proof at `:743-755` uses only image stability under a dual differential.

But the same chapter later admits the distinction:

- `shifted_rtt_duality_orthogonal_coideals.tex:1088-1101`: image of a dg algebra map gives differential stability, not the coideal condition; higher rank needs case-by-case Delta-stability.

Failure mode. Differential stability is not coproduct/coideal stability. The theorem overclaims exactly what the convention warning later repairs.

HEAL. Split the theorem:

- Proved generally: pairing-annihilator sub-dg-module / differential-stable annihilator, weightwise dual to the quotient bar.
- Proved in rank one: explicit curved coideal/cobar model, anchored at `:848-863`.
- Conditional in higher rank: coideal after explicit Delta-stability verification.

Recommended status: `thm:quotient-coideal-descent` should be downgraded to `ClaimStatusConditional` for the coideal/subcoalgebra wording outside the rank-one verified case. Rename "orthogonal coideal" to "pairing-annihilator coideal" where Letzter-Kolb confusion is possible.

### 6. Unified chiral quantum group theorem exceeds its own caveat and Vol I Yangian scope

ATTACK. The main theorem asserts one object with all nine fibers, all-order YBE, Koszul dual, DS compatibility:

- `unified_chiral_quantum_group.tex:724-773`.
- Fiber claims at `:907-955`, `:969-1018`.
- Main overview asserts strictification vanishes for every simple Lie algebra: `main.tex:1848-1855`.

But the same chapter restricts concrete construction:

- `unified_chiral_quantum_group.tex:546-583`: explicit six-piece construction is verified only for the `sl_2` Yangian and affine KM; elliptic is partial; toroidal is absent.

Vol I also refuses the stronger Yangian completion:

- `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:1055-1066`: category-O/KL completion and RTT-complete H-level comparison are not claimed.
- `:1087-1089`: central charge/kappa are not defined for Yangians in the VOA sense.

Failure mode. The theorem statement and main overview promote an abstract Koszul-locus architecture into concrete all-fiber, all-order, all-simple-type construction. The proof of the theorem relies on generic quantization references and the faulty Casimir bridge from cycle 1.

HEAL. Recast:

- The abstract `Q_g^{k,f,mu}` is a conditional/structural package on the chirally Koszul locus.
- Concrete generator-and-relation identification is proved only for the listed anchors.
- The remaining fibers are specialization programs with per-fiber status tags.
- Replace "strictification vanishes for every simple Lie algebra" by "vanishes on the evaluation-generated simple-type core currently verified; completion remains a DK-4/DK-5 obligation."

Recommended status: keep anchor propositions proved; downgrade the universal theorem to `ClaimStatusConditional` or split into an abstract theorem plus concrete verified corollaries.

### 7. Super-GRT parity action has the wrong sign mechanism

ATTACK. The GRT chapter defines a super extension:

- `grt_parametrized_seven_faces.tex:553-587`.

The super-Yangian chapter repeats it:

- `super_chiral_yangian.tex:284-310`: odd-odd residue/Laplace sign.
- `super_chiral_yangian.tex:1104-1125`: semidirect factor acts by `X -> -X` and "flips the sign of the X tensor X entry".

Failure mode. The automorphism `X -> -X` sends `X tensor X` to `(+1) X tensor X`; it does not flip the odd-odd tensor entry. The sign in Lemma `lem:ap107-sign` is a Koszul/orientation comparison between collision residue and Laplace transform, not a faithful `(Z/2)^{|odd|}` generator-sign action on `X tensor X`. Also the odd-odd tensor has even total parity, so calling the symplectic-fermion residue "valued in the odd sector" is imprecise.

HEAL. Define the super factor as a parity-coordinate convention acting on ordered half-edges/orientation of the residue-to-Laplace comparison, not as the algebra automorphism `X -> -X` on both tensor legs. If an actual automorphism is wanted, act on one marked leg or on the orientation line; then the sign is explicit. Replace "odd sector" by "odd-odd OPE channel, even total tensor parity." Downgrade the super-GRT torsor claims until this action is defined functorially.

### 8. Casimir divisor transport: Hom=gcd is correct, universal factorization is underspecified

ATTACK. The divisor-core chapter states:

- `casimir_divisor_core_transport.tex:1062-1078`: canonical exact sequences through the gcd core.
- `:1086-1104`: any `k[t]`-linear map factors uniquely through the maximal common core.

Failure mode. The algebraic identity `Hom_{k[t]}(k[t]/p_A,k[t]/p_B) ~= k[t]/gcd(p_A,p_B)` is correct. The stronger factorization through a named quotient/inclusion is not canonical unless the maps are specified, usually quotient to `k[t]/g` and injection by multiplication with `p_B/g` (or the dual convention). Without those maps, "factors uniquely through the maximal common core" is stronger than the Hom calculation.

HEAL. State the precise Hom theorem first. Then define the quotient/inclusion maps explicitly before claiming factorization. In examples such as `sl_3/W_3` (`:1174-1239`), keep the calculation but mark the input discriminants as assumed predictions unless independently computed.

Recommended status: algebraic `Hom=gcd` remains proved; universal transport language should be tightened to "after choosing the standard quotient/inclusion determined by the divisibility data."

## Architecture-level recommendations

1. Install one global rational RTT convention: sign of `R(u)`, extracted classical `r(u)`, and whether hbar is included in `r` or only in `R`.
2. Split every `r(z)` into one of three lanes: OPE collision residue, KZ/connection coefficient, or quantum `R` tangent. Do not identify them by a chained equality.
3. Split GRT claims by coefficient field: rational, motivic-period, real/complex, and cohomological binary residue.
4. Preserve the line "cohomological binary r is associator-independent"; move all MZV content to higher cochain operations.
5. Treat shifted RTT boundary quotient/coideal claims as conditional outside rank one until Delta-stability is explicitly verified.
6. Align the unified chiral quantum group theorem with its own concrete-scope caveat and with Vol I's DK-core restriction.

## Files changed

- `compute/audit/architecture_swarm_20260424/agent09_rmatrix_yangian.md` only.
