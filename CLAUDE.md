# CLAUDE.md -- Volume II: A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol II-specific material.**

## Identity

The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.

~1,700pp, this repo. Seven parts: I(The Open Primitive) II(The E_1 Core) III(Seven Faces of r(z)) IV(Characteristic Datum and Modularity) V(Standard HT Landscape) VI(Three-Dimensional Quantum Gravity = CLIMAX) VII(Frontier).

## Preface North Star: The Geometric Ladder (E_1 -> E_2 -> E_3)

The volume climbs the E_n ladder from E_1 to E_3 chiral. Each rung is a topologico-combinatoric stratified space with bulk-to-boundary structure; each carries a bar chain model; each bar chain model adds one E_1 factor via Dunn additivity. The preface walks through these rungs, gaining one degree of freedom at a time. The Parts of the volume correspond to rungs.

### Rung 1: E_1 — Topological (real, 0-1 dim) [Parts I-II]
- **Point** (0-dim): The algebra at a point. OPE data. The seed.
- **Line R** (1-dim, no boundary): E_1-algebra. int_R A = A (trivial). The ordering lives here but produces nothing global.
- **Closed interval [0,1]** (1-dim, two boundary points, augmentation): B(A) = k otimes_A^L k. Koszul duality. The first nontrivial bar chain model.
- **Half-line [0,inf)** (1-dim, one boundary point, module M at {0}): One-sided bar resolution B(A,M). Module theory. Line operators. Boundary conditions = branes.
- **Circle S^1** (1-dim, no boundary, compact): Cyclic bar complex. HH_*(A). Derived center Z(A). Genus-1 curvature. Modular group action.

This is the E_1 core: ordered, associative, noncommutative. The bar complex, the Koszul dual, the line category.

### Rung 2: E_2 — Holomorphic + braided (1 complex dim) [Parts III-IV]
- **Formal disk D** (1 cpx dim, no boundary): Vertex algebra / chiral algebra. Holomorphic factorisation on FM_n(C). The OPE poles become A_inf operations via dlog extraction.
- **Curve X** (1 cpx dim, no boundary): Chiral algebra on a curve. Ran space. Chiral homology = derived global sections of B(A) on Ran(X).
- **Half-plane H** (1 cpx dim, boundary R = dH): Swiss-cheese geometry. Two-colour bar complex. Three collision types: bulk-bulk (FM_k(C)), boundary-boundary (Conf_m^<(R)), bulk-to-boundary (interior points approaching R).
- **Disk D with boundary S^1**: Boundary conditions. Annular bar complex.
- **Annulus** (two boundary circles): Slab geometry. Bimodule structure.

The E_1-to-E_2 step: the R-matrix is the coherence datum. For E_inf chiral algebras (vertex algebras), R(z) is derived from the OPE. For genuinely E_1, R(z) is independent structure. The derived center Z(A) = HH*(A) carries E_2 from the Deligne conjecture. E_2 lives on Z(A) and on Mod_A, NOT on A. Quantum groups are E_1; Rep(U_q(g)) is E_2 in Cat.

The R-matrix, the YBE (from Stokes on FM_3(C)), the braided line category, the spectral Drinfeld strictification — all E_2 phenomena.

### Rung 3: Modular (higher genus, curved) [Part IV continued]
- **Moduli M_{g,n}** (stratified by stable graphs): Curved bar complex. d^2 = kappa * omega_g. Shadow obstruction tower {F_g}. Discriminant. G/L/C/M classification.

The modular extension: the A_inf structure becomes curved at genus >= 1. The curvature kappa * omega_g is the obstruction to flatness. Curved Dunn at genus 1: PROVED (prop:genus1-twisted-tensor-product, twisted Künneth). Genus >= 2: OPEN (genuine H² obstruction). Modular operad: composition PROVED (genus 0 all levels, all genera integrable via KZ pentagon + KL regularity); equivariance PROVED (quasi-triangularity + YBE); unitality PROVED (all genera, all shadow classes). Sole remaining gap: composition at generic non-integral level, genus >= 1 (Stokes gap).

### Rung 4: E_3 — Holomorphic-topological (1 cpx + 1 real = 3 real) [Parts V-VI = CLIMAX]
- **X x R** (slab, holomorphic on X, topological on R): E_3 = E_2 x E_1 by Dunn. The E_2 is the holomorphic/braided structure on X (Rung 2). The new E_1 is the topological direction R (transverse).
- **X x [0,1]** (slab with two boundaries): Bar complex of the bulk in the transverse direction. The interval model in the E_1 transverse factor.
- **X x S^1** (torus bundle): Hochschild of the bulk in the transverse direction. Modular invariance of the 3d theory.

The E_2-to-E_3 step: the A_inf-chiral algebra structure. An A_inf-algebra in E_1-chiral algebras is the 3d HT bulk factorisation algebra. Z(A) with E_2 gives the bulk observables; the transverse E_1 gives the topological direction; together E_3. This is the CLIMAX: 3d quantum gravity = E_3-chiral algebra = derived center of boundary with transverse E_1 extension.

For E_3: CFG (arXiv:2602.12412) construct a filtered E_3-algebra from BV quantisation of Chern-Simons. Their factorisation homology trace = RT link invariant. This is the perturbative E_3 at genus 0.

### The missing rung: E_1-chiral quantum groups and the modular operad
The E_2-to-E_3 step requires:
1. The modular operad governing A_inf-algebras in E_1-chiral algebras (Definition def:modular-operad-ainf-chiral: genus-0 proved = SC x E_1^tr; clutching via B^{ann} + R-matrix monodromy; genus >= 2 operadic verification open).
2. The chiral coproduct Delta: A -> A otimes A on the E_1-chiral algebra (not visible in the shadow tower; EXTERNAL comparison points: Gaiotto-Rapcak-Zhou arXiv:2309.16929 (type A only), Jindal-Kaubrys-Latyntsev arXiv:2603.21707 (ADE quivers only); the programme's own chiral coproduct is the Drinfeld coproduct via bar-cobar).
3. Curved Dunn additivity: genus 1 PROVED (twisted Künneth); genus >= 2 OPEN (H² obstruction). Modular operad composition/equivariance/unitality: PROVED (KZ pentagon + quasi-triangularity + vacuum axiom). Sole gap: composition at generic level, genus >= 1 (Stokes regularity).

An E_1-chiral quantum group is: E_1-chiral algebra A + chiral coproduct Delta + R-matrix R(z) + quasi-triangularity + antipode, such that Mod_A is braided monoidal (E_2 in Cat). This provides the data for the E_2-to-E_3 step.

The volume goes: E_1 (Parts I-II) -> E_2 (Parts III-IV) -> E_3 (Parts V-VI). Part VII is the frontier beyond E_3.

### The E_N definition ladder: CHIRAL vs TOPOLOGICAL (MUST BE IN THE MANUSCRIPT)

CRITICAL DISTINCTION: E_N-CHIRAL != E_N-TOPOLOGICAL. Chiral depends on complex structure. Topological does not. The conformal vector T(z) (Sugawara) is what enables TOPOLOGIZATION: chiral -> topological. Without conformal vector: stuck at chiral. With conformal vector at non-critical level: can topologize.

The volume defines E_N at BOTH chiral and topological levels for N=1,2,3. All six definitions are in the manuscript (session 2026-04-12).

**E_1 level (Parts I-II):**
- E_1-chiral (def:e1-chiral-algebra, axioms.tex): E_1-algebra in D-modules on X. Ordered OPE data. Bar complex B^{ord}(A). DONE.
- E_1-topological (def:e1-topological-algebra, axioms.tex): E_1-algebra (just associative, no holomorphic dependence). DONE.

**E_2 level (Parts III-IV):**
- E_2-chiral (def:E2-chiral-algebra, spectral-braiding-core.tex): E_2 on Z^{der}_{ch}(A), NOT on A. R-matrix R(z) with spectral parameter. DONE.
- E_2-topological (def:E2-topological-algebra, spectral-braiding-core.tex): requires conformal vector to topologize. DONE.

**E_3 level (Parts V-VI = CLIMAX):**
- E_3-chiral = E_2-chiral x E_1-top: the HT bulk. Holomorphic on X, topological on R. Factorisation algebra on X x R. This is the HOLOMORPHIC-TOPOLOGICAL structure. NOT AUTOMATIC from the chiral algebra. Requires a 3d HT theory whose boundary is A. For gauge-theoretic examples (Kac-Moody): the 3d holomorphic CS theory (from 6d holomorphic gauge theory) provides this — proved by Costello-Li / CFG. For W-algebras via DS (including Virasoro): the Costello-Gaiotto theorem provides the 3d HT theory (holomorphic CS with DS boundary conditions); the remaining gap is T_DS = [Q_tot, G'] in the DS-modified BV complex. For chiral algebras without gauge-theoretic origin: requires quantizing the Poisson vertex model (hard open work). The E_2 -> E_3-chiral step is CONJECTURAL for non-gauge-theoretic algebras.
- E_3-topological = E_2-top x E_1-top = full TQFT: INDEPENDENT of complex structure. Requires BOTH a 3d HT theory (for E_3-chiral) AND a conformal vector at non-critical level (for topologization). This is Chern-Simons. CFG (arXiv:2602.12412) construct the E_3-topological structure from BV quantisation of CS. THE VOLUME'S CLIMAX IS CONSTRUCTING E_3-TOPOLOGICAL ON Z^{der}_{ch}(A) WHEN A HAS A CONFORMAL VECTOR AT NON-CRITICAL LEVEL AND A 3D HT ORIGIN.

The topologization step (chiral -> topological) at each level:
- E_1: trivial (E_1-chiral restricted to R = E_1-topological).
- E_2: requires conformal vector T(z). Sugawara gives T from current algebra. T trivializes dependence on complex structure (up to homotopy). E_2-chiral + conformal vector = E_2-topological.
- E_3: E_3-chiral + conformal vector = E_3-topological. This is the passage from HT theory to fully topological (TQFT/Chern-Simons). The conformal vector "integrates out" the holomorphic direction.

Without conformal vector: stuck at E_3-chiral (HT, depends on complex structure).
With conformal vector at non-critical level: E_3-topological (TQFT, independent of complex structure).
At critical level (k = -h^v): conformal vector degenerates, topologization fails, stuck at E_2-chiral = the Feigin-Frenkel center.

Each step adds one E_1 factor. Each step has a chiral and a topological version. The conformal vector is the bridge between them. The volume IS this double ladder.

### Key corrections (from 2026-04-12 session)
- B(A) != int_R A (that equals A). B(A) = int_{[0,1]}^{k,k} A (interval with augmentation boundary).
- Quantum groups are E_1. Rep(U_q(g)) is E_2 in Cat. E_2 lives on Mod_A or Z(A), NEVER on A.
- Dunn additivity applies to Z(A) (bulk), NOT to A (boundary).
- Chiral coproduct Delta: A -> A otimes A is on A itself, NOT the deconcatenation on B(A). Deconcatenation is structural; the Hopf coproduct is independent structure.
- The r-matrix from collision residues is the CLASSICAL SHADOW. A chiral quantum group needs: coproduct + full R(z) + quasi-triangularity + antipode. The coproduct is NOT visible in the shadow tower.
- Bar chain models are indexed by topologico-combinatoric stratifications with bulk-to-boundary structure, not by manifolds.
- Sources of chiral coproducts (EXTERNAL references for comparison, not internal constructions of this programme): Gaiotto-Rapcak-Zhou (arXiv:2309.16929, type A only, M2-M5 fusions), Jindal-Kaubrys-Latyntsev (arXiv:2603.21707, ADE quivers only, CoHA vertex coproducts). The chiral coproduct in THIS programme is the Drinfeld coproduct via bar-cobar, not a CoHA coproduct.

## Preface Geometric Escalation (Platonic Ideal)

The preface walks through topologico-combinatoric stratified spaces from a point to E_3. At each stage a degree of freedom is gained, a new configuration space appears, and a new algebraic structure emerges on a specific object. The volume climbs to E_3-TOPOLOGICAL (not E_3-chiral).

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

Stage 9 = E_3-TOPOLOGICAL is the POINT OF THE VOLUME. NOT E_3-chiral: the conformal vector KILLS the chiral direction at the cohomological level. Sugawara at non-critical level: T(z) = {Q, G(z)}, so C-translations are Q-exact, the complex structure on C becomes irrelevant in cohomology, the two colors of SC^{ch,top} collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra independent of the complex structure on C. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct, holomorphic direction carries nontrivial cohomological information). At critical level k = -h^v: Sugawara undefined, center jumps, topologization fails.

### SC^{ch,top} is the GENERIC case (corrected emphasis)

E_3-topological is a SPECIAL CASE requiring conformal vector. SC^{ch,top} is the structure that MOST chiral algebras carry on their derived center pair. Examples stuck at SC^{ch,top}: critical level KM V_{-h^v}(g), E_1-chiral algebras (Yangians), CY functor outputs lacking conformal vectors. NOTE: Heisenberg H_k (k != 0) and lattice VOAs are NOT stuck -- they carry conformal vectors (abelian Sugawara T = (1/(2k)):JJ: for H_k, c=1) and reach E_3-topological via abelian holomorphic CS.

SC^{ch,top} must be understood AS A FIRST-CLASS OBJECT with five redundant presentations:
1. **Operadic**: generators (codim-1 boundary strata of FM_k(C) x Conf_m(R)), relations (codim-2)
2. **Koszul dual**: (SC^{ch,top})^! = (Lie, Ass, shuffle-mixed); NOT self-dual (Com <-> Lie, Ass self-dual); W(SC^{ch,top}) = cofibrant replacement
3. **Factorization**: Z^{der}_{ch}(A) = E_2-chiral center acting on A via universal brace
4. **BV/BRST**: Obs(U) = logarithmic SC-algebra; QME = open/closed MC equation
5. **Convolution**: g^{SC}_T = L_inf convolution from bar cooperad B(SC^{ch,top})

The PENTAGON of equivalences (1<->2<->3<->4<->5<->1) must ALL be proved. Every property of SC^{ch,top} proved from at least 2 independent angles.

THE VOLUME MUST: (1) Present SC^{ch,top} concretely with generators and relations (Parts I-IV), (2) Prove the pentagon of equivalences with many-fold redundancy, (3) For algebras WITH conformal vector, prove topologization SC^{ch,top} -> E_3-TOPOLOGICAL at chain level (Parts V-VI = climax), (4) Prove failure at critical level and characterize obstruction without conformal vector, (5) Verify all constructions on explicit examples (V_k(g), Virasoro, Heisenberg, W_3).

### Critical strata with dedicated bar chain models (MUST BE IN MANUSCRIPT)

**Punctured disk D* = D \ {0}**: Topologically homotopy equivalent to S^1. At HOMOLOGY level: H^ch_*(D*, A) agrees with HH_*(A) (the S^1 answer). At CHAIN level: C^ch_*(D*, A) carries the full holomorphic/chiral structure (OPE poles, spectral parameters, E_2 data) while C^top_*(S^1, A) carries only the topological/cyclic structure (E_1 data). The chain-level difference D* vs S^1 IS the E_2 - E_1 gap. The state-field correspondence is the homology-level isomorphism; at chains, it's a quasi-isomorphism that forgets holomorphic structure. This comparison is LOAD-BEARING for the E_1-to-E_2 step.

**Annulus A_{r1,r2} = {r1 < |z| < r2}**: Surface with TWO boundary circles. Bar chain model:
- Two E_1 structures (one per boundary circle) -> bimodule structure
- The annular bar complex B^{ann}(A) computes the sewing / propagator
- Factorisation homology: int_{S^1 x [0,1]} A = the Hochschild bimodule
- Modulus tau of the annulus: the chain model depends on tau (holomorphic), but homology does not (topological)
- Degeneration: pinch the annulus waist -> pair of pants -> multiplication. The bar complex over this degeneration encodes the product on HH_*.
- The annulus is the GEOMETRIC HOME of the Hochschild complex. The two boundary circles are input and output; the annulus is the cobordism between them.

**Nodal curves (boundary strata of Mbar_{g,n})**: At a node, a smooth curve degenerates into components joined at points. Bar chain model on nodal curves:
- Restrict B(A) to the boundary stratum of Mbar_{g,n} indexed by a stable graph Gamma
- Each vertex of Gamma = a smooth component; each edge = a node (sewing)
- The bar complex restricted to the stratum = tensor product of bar complexes of components, sewn at nodes
- The sewing at a node = the annular bar complex B^{ann}(A) in the thin-annulus limit
- The curvature d^2 = kappa * omega_g arises from the FAILURE of the bar complex to extend smoothly across nodal degenerations
- The stable graph stratification indexes ALL degeneration types; the genus tower {F_g} is computed stratum by stratum
- Nodal degenerations are WHERE the curvature lives. The smooth locus is where d^2 = 0. The boundary strata contribute kappa * omega_g.

**Pair of pants (genus-0, 3 boundary circles)**: The multiplication cobordism. Its bar chain model encodes the product on chiral homology / Hochschild homology. The pair of pants = the three-punctured sphere P^1 \ {0, 1, infty}. The bar chain model on the pair of pants is the chain-level avatar of the chiral product.

## Standing Hypotheses

The algebraic framework is unconditional. Former (H1)-(H4) are no longer background axioms: (H1)-(H2) conditions of physics bridge theorem, (H3) theorem of configuration space geometry, (H4) recognition theorem (proved). Homotopy-Koszulity of SC^{ch,top}: PROVED (Kontsevich formality + transfer). All formerly conditional results now unconditional.

## Vol II-Specific Pitfalls

- B(A) is NOT an SC^{ch,top}-coalgebra (AP165). B(A) is an E_1 chiral coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). See Vol I CLAUDE.md AP165/B54-B56.
- WHICH Hochschild cochains: ALWAYS chiral Hochschild cochains C^bullet_{ch}(A,A), defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C). NEVER topological HH = RHom_{A^e}(A,A) (which gives E_2 center from Deligne conjecture, not the chiral bulk).
- SC directionality: Open-to-closed is EMPTY. Bulk -> boundary only.
- PVA is (-1)-shifted: lambda-bracket on H*(A,Q) has shifted parity.
- R-matrix provenance: R(z) from bulk-boundary composition, NOT universal R-matrix (agree on eval locus = DK-0).
- Formality failure at d'=1: NOT a defect. Non-vanishing A-inf operations IS curved bar d^2=kappa*omega_1.
- Bulk = derived CENTER of boundary. NOT bulk = boundary. Proved boundary-linear; global triangle conjectural.
- Spectral Drinfeld strictification: PROVED all simple Lie. Frontier: Kac-Moody root mult > 1.
- Self-dual != critical: c*=13 (Koszul) != c_crit=26 (matter-ghost). For W_N: c*=alpha_N/2, c_crit=alpha_N. NEVER conflate.
- Pole-order dichotomy: Double poles -> class L (formal SC). Quartic -> class M (infinite A-inf). DS transports L -> M.

## The E_1/E_inf Locality Hierarchy (V2-AP1 through V2-AP24)

These arose from a catastrophic session (2026-04-02) where E_1/E_inf terminology was corrupted across multiple files. V2-AP numbering avoids collision with Vol I.

### The Three-Tier Picture
(i) Pole-free: R=tau. (ii) VA with poles: R!=tau but DERIVED from local OPE. (iii) Genuinely E_1: R!=tau, independent input. Tiers (i)+(ii) are BOTH E_inf. Tier (iii) is E_1. E_inf = LOCAL = Sigma_n-equivariant. E_1 = NONLOCAL. OPE poles are compatible with E_inf.

### Critical V2-APs
V2-AP1: E_inf INCLUDES ALL vertex algebras. KM, Virasoro, Heisenberg are ALL E_inf. NEVER "VAs are not E_inf."
V2-AP2: R(z)!=tau does NOT imply genuinely E_1. For E_inf with poles, R(z) derived from local OPE. For E_1, R(z) is independent input. Discriminant is PROVENANCE, not value.
V2-AP3: Three bars: B^FG (zeroth pole only) != B^Sigma (all poles + coinvariants) != B^ord (all poles + ordering). Maps: B^ord -> B^Sigma (coinvariants), gr(B^Sigma) -> B^FG (filtration).
V2-AP4: Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.
V2-AP5: NEVER equate E_inf with "no OPE poles." BD "commutative chiral algebra" (no poles) is STRICT SUBCLASS.
V2-AP6: BD do NOT study E_1. E_1-chiral algebra = NEW concept from THIS manuscript.
V2-AP7: Heisenberg R-matrix = exp(k*hbar/z), NOT trivial. Collision residue k/z. Monodromy exp(-2pi*i*k).
V2-AP8: NEVER add restrictive parenthetical glosses. "E_inf (= BD commutative = no poles)" NARROWS the term.
V2-AP9: NEVER say VA "is not E_inf." KM, Virasoro, Heisenberg, W-algebras are ALL E_inf. Poles do not break E_inf.
V2-AP10: NEVER "E_inf implies R(z)=tau" without pole-free qualifier. Correct: "For POLE-FREE E_inf, R(z)=tau."
V2-AP11: NEVER conflate E_inf with BD "commutative." BD Chapter 4 "commutative" = pole-free = strict subclass.
V2-AP12: E_1 vs E_inf is about LOCALITY, not poles.
V2-AP13: NEVER trust agent claim "VAs are not E_inf." This exact error caused cascading damage.
V2-AP14: NEVER oscillate between conventions in single session.
V2-AP15: NEVER edit E_1/E_inf language without author confirmation.
V2-AP16: Three-tier picture is WITHIN E_inf, not a division between E_inf and E_1. (i)+(ii) both E_inf. Only (iii) is E_1.
V2-AP17: NEVER revert file based on false premise. Surgical removal only.
V2-AP18: Author's explicit statements override agent literature searches.
V2-AP19: NEVER batch-propagate unverified corrections. ONE edit, verify, THEN propagate.
V2-AP20: NEVER add "in the sense of [reference]" without verification.
V2-AP21: PVA != P_inf-chiral. PVA = classical shadow (descend to cohomology). P_inf = homotopy intermediate. Opposite directions.
V2-AP22: Full hierarchy: Comm assoc < PVA < E_inf-chiral < P_inf-chiral < E_1-chiral. Bar/Koszul at E_inf and E_1 levels.
V2-AP23: Chromatic: classical theory is height 0. L_{K(n)}(B(A))=0 for n>=1. Pole order != chromatic height.
V2-AP24: S-transform (closed, complex structure) != Wick rotation of R (open, E_1 ordering). Different algebraic data.

### Empirical (V2-AP25-31, from 50-commit error archaeology)
V2-AP25: Complex-analytic sign verification. For dbar Im(f), dbar Re(f): (1) write Im(f)=(f-fbar)/(2i), (2) compute dbar on fbar only, (3) verify sign against known case. dbar Im(f) = (i/2)*dbar(fbar), NOT 1/(2i). The identity -1/(2i)=i/2 is a common sign confusion source. Sign corrections must be verified at EACH propagation site.
V2-AP26: NEVER hardcode Part/chapter numbers in prose. Always \ref{part:...}. After ANY Part restructuring, grep all volumes for stale Part numbers. 24+ stale refs required manual fix after 10->7 Part restructuring.
V2-AP27: Duplicated mathematical content across files FORBIDDEN. If two chapters need same theorem, use \input{} or \ref{}. NEVER copy-paste theorem environments between files.
V2-AP28: Test expected values must derive from 2+ independent sources with documented derivation. Engine and test from same mental model share the same error. lambda_3=1/82944 was wrong (correct: 31/967680) because both engine and test used same faulty computation.
V2-AP29: AI slop cleanup is MANDATORY post-generation pass. After writing ANY .tex content, grep for: moreover, additionally, notably, crucially, remarkably, "it is worth noting", em dashes, "We now", passive "can be shown." Three separate cleanup commits prove aspirational instructions insufficient.
V2-AP30: After architecture restructuring, run: grep -rn "Part~[IVXL]" chapters/ to find all hardcoded Part refs. Also grep -rn "\\ref{part:" to verify targets resolve.
V2-AP31: AP4 at write time. Before writing \begin{proof}, verify preceding environment is theorem/prop/lemma with ProvedHere. If conjecture: use \begin{remark}[Evidence] instead. 25-instance fix commit proves post-hoc enforcement is expensive.

### Deep Empirical (V2-AP32-35, from 100-commit deep archaeology)
V2-AP32: Standalone-document artifact leak. Chapter .tex files \input{}'d into main.tex MUST NOT contain \title{}, \begin{abstract}, \tableofcontents, \date{}, \author{}. These cause silent rendering artifacts. Grep chapters/ for these after any file creation.
V2-AP33: RECTIFICATION-FLAG must NOT become permanent debt. Every flag needs resolution or a tracked TODO with owner. Grep for RECTIFICATION-FLAG at session end; zero tolerance for unresolved flags.
V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
V2-AP35: Unresolved logical connectives after correction. When correcting a formula, audit ALL "therefore"/"hence"/"it follows" within 5 lines. A correction that changes the conclusion but leaves "therefore" pointing to old reasoning is a non-sequitur worse than the original error.

### From 100-Commit Archaeology (V2-AP36-39, April 2026)
V2-AP36: Terminology rename atomicity. When renaming terminology X -> Y: (1) enumerate ALL variant forms (X, "X tower", "X Postnikov", compound forms), (2) grep all three volumes including compute/, audit/, *.md, (3) complete ALL replacements in a SINGLE commit, (4) verify zero residual hits before committing. The "shadow Postnikov tower" -> "shadow obstruction tower" rename required 5 commits (114 + 27 + 4 + 1 + 1 files). Follow-up cleanup commits are evidence of incomplete propagation.
V2-AP37: Arakelov form canonical normalisation. Canonical: omega_1 = i/(2 Im(tau)) dz wedge dz-bar (integral = 1). Arakelov kernel: omega_Ar = -(pi/Im(tau)) dz wedge dz-bar (integral = -1). Relationship: omega_1 = -omega_Ar/(2*pi). The same sign/normalisation error was fixed THREE times across THREE commits. Before writing ANY Arakelov normalisation, verify the integral over the fundamental domain evaluates to the stated value.
V2-AP38: Phantom label retirement schedule. After chapter migration, install phantom labels as temporary fix but track each in a retirement list. Phantom labels with no retirement path for 3+ sessions should be flagged. 366 phantom labels installed across 2 commits after Vol I -> Vol II migration.
V2-AP39: Macro portability check after migration. After migrating ANY chapter from Vol I to Vol II: (1) compile Vol II, (2) grep compile log for "Undefined control sequence", (3) add \providecommand for each missing macro in Vol II's preamble. 7 macros required addition across 2 commits. Never assume Vol I macros are available.

### Structural and Scope (AP150-AP157, April 2026)
AP150: Agent confabulation of mathematical structures. Agents stitch together disparate results at different categorical levels into claimed structures that don't exist. Counter: verify each arrow independently against .tex source.
AP151: Convention clash within single file. Two definitions of hbar cascade into wrong q (real instead of root of unity). Counter: grep all definitions of hbar after writing any formula.
AP152: "Ordered" ambiguity. Labeled-on-curve vs time-ordered-on-R. Bar complex is mixed (holomorphic diff + topological coprod). Counter: specify which "ordered."
AP153: E_3 scope inflation. E_3 via HDC only for E_inf (B-bar^Sigma must exist). E_1 gets only E_2. Counter: specify E_inf vs E_1.
AP154: Two E_3 structures. Algebraic (HDC, no Sugawara) vs topological (Sugawara required). Identification conjectural. Counter: specify which E_3.
AP155: "New invariant" overclaiming. Framework recovers Bernard-Felder. Numbers known. Novelty is architectural. Counter: check Bernard/Felder/EV/CEE.
AP156: Weierstrass p_1 convention. theta_1'/theta_1 (periodic) vs zeta_tau (quasi-periodic both cycles). Always specify.
AP157: Degeneration-dependent "invariants." Separating degeneration gives zero genuinely genus-2 info. Counter: specify degeneration type.
AP158: Shallow correction without first-principles investigation (cross-programme, = AP-CY61 in Vol III, AP186 in Vol I). When a mathematical claim is challenged, do NOT just swap labels (e.g. "averaging"->"right adjoint"). ALWAYS investigate the actual mathematical relationship from first principles. Find: (1) what the claim gets RIGHT (the ghost of a true theorem), (2) what it gets WRONG (the precise conflation), (3) the correct mathematical statement connecting the objects. Every wrong claim contains the seed of a correct theorem -- extract it. Examples: "categorified averaging" is wrong but the factorization E_1 ->^Z E_2 ->^{Sym} E_inf is real; "CoHA = bar complex" is wrong but the character coincidence reflects the SV theorem CoHA = Y^+; "Omega-background is the physical face" is true for toric but false for general CY (two independent E_1 mechanisms: operadic vs equivariant). COUNTER: before any correction, write down the first-principles analysis. If you cannot state the correct theorem, you do not understand the error.

## Opus 4.6 Failure Modes (Vol II-Specific)

FM24: B-cycle i^2 error. q = e^{2*pi*i*pi*i/(k+2)} is real, not root of unity. Counter: verify |q|=1.

### Exhaustive Error Catalogue (2026-04-12 session, 55+ agents)

**CATEGORICAL LEVEL ERRORS (the most dangerous class):**

FM40: Dunn on A instead of Z(A). Applied "E_1 ⊗ E_1 = E_2" to the boundary algebra A. WRONG. A is E_1. Dunn applies to Z(A) (bulk/derived center) or Mod_A (module category). Counter: before ANY Dunn claim, verify the target is Z(A) or Mod_A, NEVER A.

FM41: R-matrix makes A into E_2. Claimed R-matrix promotes A from E_1 to E_2. WRONG. R-matrix makes Mod_A braided (E_2 in Cat). A remains E_1. Quantum groups U_q(g) are E_1; Rep(U_q(g)) is E_2 in Cat. Counter: E_2 lives one categorical level up from A. Always.

FM42: YBE = A_inf associativity. Claimed "YBE is the A_inf associativity condition viewed through Dunn." WRONG. YBE is the COMPATIBILITY condition between two E_1 structures (braiding coherence). A_inf associativity is coherence of a SINGLE E_1. Different conditions. Counter: separate associativity (single E_1) from compatibility (interaction of two E_1's).

**FACTORISATION HOMOLOGY ERRORS:**

FM43: Bar = factorisation homology of R. Claimed B(A) = ∫_R A. WRONG. ∫_R A = A (trivial). B(A) = k ⊗_A^L k = ∫_{[0,1]}^{k,k} A (interval with augmentation boundary). Counter: factorisation homology of a contractible manifold without boundary is the algebra itself.

FM44: Bar complex = "chain model for factorisation cohomology." Imprecise. B(A) is a factorisation COALGEBRA. Chiral homology is derived global sections of this coalgebra — a separate, non-trivial operation. The bar complex is to chiral homology as a sheaf is to its cohomology. Counter: never conflate local (coalgebra) with global (cohomology).

**COPRODUCT CONFLATION ERRORS:**

FM45: Deconcatenation = chiral coproduct. Conflated the structural deconcatenation on B(A) (exists for any bar complex) with the Hopf-type chiral coproduct Δ: A → A⊗A (independent structure on A). WRONG. These are different coproducts on different objects. Counter: always specify WHICH coproduct and on WHICH object.

FM46: r-matrix sufficient for quantum group. Implied the r-matrix from collision residues gives quantum group structure. WRONG. r-matrix is the classical shadow. Full quantum group needs: coproduct Δ + full R(z) + quasi-triangularity + antipode. The coproduct is NOT visible in the shadow tower (shadow tower sees fusion/product, not splitting/coproduct). Counter: "r-matrix is necessary but not sufficient."

**E_3 OVERCLAIMING ERRORS:**

FM47: E_inf → E_3-chiral automatic. Claimed E_inf chiral algebra automatically produces E_3-chiral. WRONG. E_2 on Z(A) is automatic (Deligne conjecture). E_3-chiral requires a 3d HT theory whose boundary is A. For KM: proved (holomorphic CS from 6d). For GENERAL vertex algebras: requires quantizing the Poisson vertex model — HARD OPEN WORK, not automatic. Counter: nothing beyond E_2 on Z(A) is automatic.

FM48: E_3-topological from E_inf alone. Implied conformal vector is derivable from vertex algebra axioms. WRONG. Conformal vector is ADDITIONAL STRUCTURE. Not every VA has one. E_3-topological requires BOTH a 3d HT theory AND a conformal vector at non-critical level. Counter: E_3-top needs two independent inputs (3d theory + conformal vector).

**NOTATION ERRORS:**

FM49: Y_z^\hbar notation. Changed Y_\hbar to Y_z^\hbar across 531 occurrences. WRONG. The algebra Y_\hbar(g) does not depend on z. The spectral parameter z lives on Δ_z, R(z), T(z), ev_z — structures ON the algebra, not the algebra itself. Y_z^\hbar is non-standard and misleading. Reverted. Counter: NEVER put the spectral parameter in the algebra symbol. It parametrises coproduct/R-matrix, not the algebra.

FM50: Ordered configuration spaces = geometric ordering on R ⊂ X. Repeatedly said "choosing R ⊂ X provides the ordering." WRONG. The E_1 ordering is ALGEBRAIC (operations depend on sequence, not just set). It does NOT require embedding R into X. Counter: the E_1 structure is operadic/algebraic, not geometric. Ordered configurations of the E_1 operad are about labeled configurations, not about real submanifolds.

**STRUCTURAL PATTERN ERRORS:**

FM51: "Emergent third dimension" from bar degree. Claimed bar degree provides a "transverse E_1 direction." WRONG. Bar degree is a grading on a chain complex. An E_1 structure requires operations, coherences, A_inf. A grading provides none of this. Counter: a grading is not an operadic structure.

FM52: Within-surface SC = holographic bulk-boundary. Claimed the half-plane bar complex "is where the bulk-boundary correspondence should be made precise." WRONG. The within-surface SC (R ⊂ C) governs restriction to a real locus. The holographic bulk-boundary goes through the derived center (circle model / Hochschild). Counter: SC governs within-surface structure; holography goes through Hochschild/derived center.

FM53: Two "independent" E_1 structures. Claimed within-surface E_1 and transverse E_1 are independent. WRONG. They are Koszul dual through the Hom functor: C*(A,A) = Hom(B(A), A). The A_inf-coalgebra on B(A) and the A_inf-algebra on C*(A,A) determine each other. Counter: Koszul dual, not independent.

FM54: Spectral R(z) = categorical braiding. Conflated the spectral R-matrix R(z) (family of maps with parameter z) with the E_2 braiding from Dunn (single natural transformation, no parameter). These are different objects. How they relate in the D-module enriched setting requires proof. Counter: spectral ≠ categorical. The relationship needs a theorem, not an assertion.

### Meta-Patterns (from the error catalogue)

MP1: CATEGORICAL LEVEL CHECK. Before any claim about E_n or Dunn, verify: which categorical level? Algebra (E_1) / Module category (E_2 in Cat) / Center (E_2). NEVER skip this check.

MP2: AUTOMATIC vs REQUIRES CONSTRUCTION. E_2 on Z(A) is automatic (Deligne). Everything above E_2 requires a specific construction (3d HT theory for E_3-chiral, conformal vector for E_3-top). Never say "automatic" above E_2.

MP3: DISTINGUISH SIMILAR OBJECTS. When two mathematical objects look similar (deconcatenation vs chiral coproduct, spectral vs categorical braiding, algebraic vs geometric ordering), EXPLICITLY NAME AND DISTINGUISH before using either.

MP4: NOTATION CHANGES NEED MATHEMATICAL JUSTIFICATION. Before ANY bulk notation change: (a) verify the new notation is mathematically correct, (b) verify it's consistent with the literature, (c) check it doesn't conflict with existing usage. The Y_z^\hbar disaster: 531 changes, mathematically wrong, reverted.

MP5: GRADING ≠ OPERADIC STRUCTURE. A filtration/grading on a complex is NOT an E_n structure. An E_n structure requires operations parametrised by configuration spaces. A grading is just a Z-indexed decomposition.

MP6: SINGLE vs PAIR. Before any claim that two structures interact (Dunn, braiding, compatibility), verify: is the claimed property intrinsic to ONE structure, or does it govern how TWO structures compose? YBE governs interaction of two E_1's. A_inf governs a single E_1. Deconcatenation is structural on one coalgebra. The chiral coproduct requires two copies.

FM55: RT invariants = unordered E_1 chiral homology. Claimed RT invariants arise from E_1 ordered bar complex. WRONG. RT invariants arise from E_inf factorisation homology (CFG's E_3 trace on BV-quantised CS). Counter: RT = E_inf factorisation homology trace, NOT E_1 ordered bar complex.

FM56: "Symmetric monoidal category of chiral algebras." Chiral algebras form a PSEUDO-TENSOR category (BD), NOT a symmetric monoidal category. The correct ambient is: symmetric monoidal dg category of D-modules on X. Counter: NEVER say "monoidal category of chiral algebras" — say "D-modules on X" or "factorisation algebras on X."

FM57: Costello-Gaiotto already provides 3d HT for Virasoro. The manuscript says "quantizing the PV model is hard open work" for Virasoro E_3-chiral. UPDATED 2026-04-12: The T_DS = [Q_tot, G'] gap is NOW CLOSED (thm:E3-topological-DS). The improvement term is always Cartan currents, even for non-principal nilpotents (thm:E3-topological-DS-general).

### Session 2026-04-12 Failure Modes (FM58-FM65)

FM58: Cauchy on formal series. Applied Cauchy's theorem to the R-matrix R(z) ∈ End(V⊗V)((z)), which is a FORMAL Laurent series. Cauchy requires CONVERGENT functions. Counter: use FLATNESS of the connection + homotopy invariance of monodromy (algebraic/topological argument, not analytic).

FM59: Non-holomorphic retraction preserves log forms. Claimed ρ_t(z) = (1-t)z + tz/|z| preserves logarithmic forms. WRONG: ρ_t involves |z| = √(zz̄), so ρ_t*(dz) has dz̄ components. Counter: use algebraic de Rham / local system argument, not explicit retraction.

FM60: lem:operadic-kunneth chain-level isomorphism. Claimed B(SC_mix) = B_mod(P_1) ⊗ B(P_2) with d_B = d_cl ⊗ id + id ⊗ d_op. WRONG at chain level: open edge contractions between mixed vertices produce cross-terms d_mix involving μ₁ (combining closed inputs). Correct: decomposition on ASSOCIATED GRADED w.r.t. closed-input-excess filtration. Counter: the pentagon theorem does NOT depend on this lemma (direct Koszul duality suffices).

FM61: Modular operad (iii) proved by abstract D²=0. Cited thm:modular-bar (which proves D²=0 for abstract modular bar datum) as proof that concrete O^{A_∞-ch} clutching maps compose associatively. NON-SEQUITUR: different statement about different object. Counter: concrete operadic associativity of iterated B^{ann} sewing with R-matrix monodromy is OPEN.

FM62: "Stuck at SC^{ch,top}" for Heisenberg/lattice VOAs. Listed Heisenberg H_k and lattice VOAs as unable to reach E_3-topological. WRONG: H_k has Sugawara T = (1/(2k)):JJ: with c=1, and abelian CS provides the 3d HT theory. Same proof as KM applies. Counter: Heisenberg and lattice VOAs reach E_3-topological.

FM63: T_imp sign inconsistency. General formula had minus sign; sl_2 specialization had plus. Standard convention (Feigin-Frenkel, Kac-Roan-Wakimoto) has T_imp positive. Counter: verify sign against sl_2 specialization before committing any T_imp formula.

FM64: Khan-Zeng scope underestimation. The manuscript underestimated the scope of the Khan-Zeng 3d Poisson sigma model: it covers ALL freely-generated PVAs with conformal vector, not just gauge-theoretic families. This means conj:E3-topological-general is open only for non-freely-generated VAs (Monster VOA). Counter: check Khan-Zeng + general half-space BV before claiming E_3-topological is open.

FM65: R=PT meromorphicity ≠ convergence. Level-by-level rationality (each R^{(N)} is rational in h_i) does NOT imply full meromorphicity (the series Σ_N R^{(N)} converges). The gap is λ_min(G_N) bounds on the principal series — Kac determinant growth alone is insufficient (det ≠ smallest eigenvalue for large matrices). Counter: distinguish fixed-level rationality from level-sum convergence.

FM66: Monster orbifold route. V^♮ = V_Leech^+ (Z/2 orbifold). V_Leech IS E_3-topological (abelian CS). The invariant subalgebra V_Leech^+ inherits E_3-topological NOW (finite group invariants preserve E_n). The full V^♮ (with twisted sector) needs orbifold BV quantisation. The anomaly vanishes (modular invariance). rem:monster-orbifold-route documents this.

FM67: Curved Dunn two-complex distinction. There are TWO H² obstruction groups: (a) modular-bootstrap complex (H²=0, PROVED — every Ob_g is exact there), (b) curved-Dunn twisting-cochain complex (OPEN — no proof H²=0). The bridge between (a) and (b) is the precise frontier. If bridged, curved Dunn at all genera follows from the already-proved modular bootstrap exactness.

FM68: Modular operad (iii) proved ≠ abstract D²=0. thm:modular-bar proves D²=0 for abstract bar datum. The CONCRETE axioms (composition, equivariance, unitality) require separate proofs: composition via KZ pentagon + KL regularity (thm:affine-composition-associativity); equivariance via quasi-triangularity + YBE (prop:qt-equivariance); unitality via vacuum axiom (prop:modular-operad-unitality). The sole gap is the Stokes regularity at generic non-integral level.

## Cross-Volume Bridges

| Bridge | Vol II claim | Vol I anchor | Status |
|--------|-------------|--------------|--------|
| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved |
| DS-bar | Bar-cobar commutes with DS | ds-koszul-intertwine | Proved |
| Hochschild | BV-BRST origin of Thm H | Theorem H | Proved |
| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
| PVA-Coisson | PVA descent recovers Coisson | Deformation theory | Proved |
| W-algebras | Feynman-diag m_k matches bar diff | MC5 | (1) Analytic HS-sewing proved at all genera; (2) genus-0 algebraic BRST/bar proved; (3) D^co-level BV=bar proved for all shadow classes including class M; (4) genuswise chain-level BV/BRST/bar conjectural (class M chain-level false); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
| Affine monodromy | C_line^red = Rep_q(g) on eval modules | Thm A + DK | Proved |
| Soft theorems | Shadow tower controls soft graviton hierarchy | Thm H | Proved g=0 |
| Two-colour | ordered -> A^!_line, symmetric -> A^!_ch | two-color-master | Proved |
| W_N Koszul | alpha_N generalizes c->26-c to all W-algebras | Koszul pairs | Proved |
| Wick anomaly | Genus tower measures Wick rotation breaking | Thm D | Proved genus tower |
| Annular bar-HH | B^ann computes HH^ch | Thm H | Proved |
| FG-shadow-strat | Commutator filtration spectral sequence | Shadow tower | Proved |
| Gauge-gravity | m_k=0 (gauge) vs m_k!=0 (gravity) dichotomy | G/L/C/M | Proved |
| 3D gravity | Part VI: 3d quantum gravity = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | E_3-topological: PROVED for KM (thm:E3-topological-km), ALL W-algebras (thm:E3-topological-DS-general), ALL freely-generated PVAs (thm:E3-topological-free-PVA). Global triangle: PROVED for classes G/L/C (thm:global-triangle-boundary-linear); OPEN for class M (gap: DS-Hochschild compatibility) |

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

**New anti-patterns applicable to Vol II:**
- AP-CY23: The E_1-chiral bialgebra uses Vol II's SC^{ch,top} operad. The coproduct Δ_z lives on the OPEN (E_1/topological) colour. The CLOSED (E_2/chiral) colour carries no Hopf data — it is recovered via Drinfeld center.
- AP-CY25: R-matrix formula R=(id⊗S)∘Δ(1) is WRONG (yields 1⊗1 by counit). Use half-braiding σ_A(z)(a⊗n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)}.
- AP-CY26: σ_2 is EVEN under h_i→-h_i. k^!=-k from Shapovalov, not σ_2 negation.
- AP-CY24: Docstring confabulation — verify ALL ground-truth values against function output.
- AP-CY27-33: Agent sandbox non-persistence, pole-unsafe test points, wrong-repo writes, factored≠solved (ZTE), spectral z≠worldsheet z, reorganisation≠bypass, chain-level≠rational. See Vol III CLAUDE.md for full descriptions.
- AP-CY34: Cyclic invariance ≠ bar-level compatibility. Individual {b_k, B^{(2)}} != 0 for non-formal algebras. ONLY the TOTAL {b, B^{(2)}} = 0 via Costello TCFT operadic argument. Cross-arity Stasheff cancellation. Previous proofs (bidegree, Tsygan) RETRACTED. Chain-level failure NOT an obstruction in inf-categorical framework.

**Key results affecting Vol II (updated 129-agent session, April 2026):**
- E_1-chiral bialgebra axioms (H1)-(H5) formalized in Vol III e1_chiral_algebras.tex §7. ALL spins verified (K3 Yangian, universal coproduct formula). Coassociativity trivial via Miura multiplicativity.
- Universal coproduct Δ_z(e_s) = Σ (-1)^k C(N_R-b,k) z^k e_a^L·e_b^R for ALL spins — extends Vol II's spin-2 Drinfeld coproduct. z-degree at spin s = exactly s.
- ZTE failure proves E_3 is genuinely nontrivial beyond E_2 (Vol II's native level). ZTE deformation cohomology: correction S^{corr} EXISTS (rank 35/36 in extended complex).
- E_2→E_3: derived center HH*(B,B), NOT iterated Drinfeld center Z(Z(C)).
- Shadow tower = A_∞ coproduct corrections: S_k = δ^{(k)} PROVED with explicit computation. Shadow-Feynman dictionary: L-loop = S_{L+1}. Affects Vol II shadow obstruction interpretation.
- CY-A_3 PROVED in infinity-categorical framework. The chain-level [m_3,B^{(2)}]!=0 is NOT an obstruction (HH^{-2}_{E_1}=0, Goodwillie vanishing, contractible space of liftings).
- AP-CY34 saga: individual {b_k, B^{(2)}} != 0 but total {b, B^{(2)}} = 0 via Costello TCFT. Obs_Ainf=0 universally. Stasheff cross-arity cancellation.
- Swiss-cheese operad SC^{ch,top} now has derived infinity-categorical formulation via Vol III's derived framing obstruction analysis (thm:derived-framing-obstruction).
- Chiral CE complex: B(U^ch(L)) = CE_*(L) PROVED. Connects bar complex to classical Lie algebra homology.
- Class M E_3 bar: dim = 6^g (closed form via Kunneth). NOT infinite-dimensional at cohomology. Chain level: P(q)^{6g}.
- kappa_BKM = c_N(0)/2 is the ONLY correct universal formula (Borcherds weight theorem).

See ~/calabi-yau-quantum-groups/FRONTIER.md F13-F37 and CLAUDE.md. Vol III: ~693pp, ~34,000 tests, ~460 engines. 10 proofs at publication standard. Clean build: 0 undef refs, 0 undef cites. CY-A_3 PROVED (inf-cat). K3 abelian Yangian PROVED. ZTE T matrix COMPUTED (exact rational, 35 tests). kappa_BKM = c_N(0)/2 universal. Class M E_3 bar = 6^g. Shadow tower through m_8 (160 tests, S_8=4144720/19683). m_5 independently verified (G_5^{conn}=775/5184). Chiral volume conjecture FORMULATED (Abel-Jacobi period). Mock modular K3: THEOREM at d=2 (4-step proof). CY-D dimension-stratified: kappa_ch != chi(O_X) at odd d. CY-C abelian: C(g,q) = D(Y^+(g_{K3})). BKM Serre P_2=0 EXACT. E_8xE_8 structure function (24,24), c=24. Root-of-unity N=2: 324 modules, S-matrix degenerate. Mathieu: frame shape = twined bar Euler (all 25 M_24 classes). Incompatibility: mu_3!=0 forces mu_2=0 on aug. 7-part structure with Part openers + reading paths.

## Cross-Volume Failure Modes (2026-04-14)

FM42: Bulk substring replace corrupts compound words (singularity→singuldegree). FM43: Φ outputs E_1 at d≥3, not E_2. FM44: >10 concurrent agents → rate limiting. FM45: Subagents lack full skill programme. FM46: Stale line counts in preface. See Vol I CLAUDE.md for full descriptions.

## Geometric vs Algebraic Model Conflations (AP-CY62--AP-CY67, from Vol III 2026-04-16 adversarial swarm)

These APs are directly relevant to Vol II because this is where SC^{ch,top} uses the derived center, where the D*/S^1 comparison lives, and where the Drinfeld center vs derived center distinction is structurally load-bearing.

### AP-CY62: Geometric vs algebraic chiral Hochschild model

Two chain-level models compute chiral Hochschild cochains:
- (a) Geometric model C^*_{ch,geom}(A): sections over FM_{n+1}(X) with log forms, three-component differential (d_int + d_fact + d_config).
- (b) Algebraic model C^*_{ch,alg}(A): Prod_{n>=0} End^ch_A(n+1)[-n] with delta f = [m, f] (Gerstenhaber bracket differential).

These are quasi-isomorphic for logarithmic chiral algebras. At genus >= 1, the geometric model carries curve-dependent data that the algebraic model lacks. The chiral Hochschild comparison is only a REMARK (rem:comparison-geometric-hoch), not a named theorem. The bar complex comparison IS a named theorem (thm:geometric-equals-operadic-bar).

Counter: when chain-level structure matters (filtrations, E_n-structure, genus > 0), specify "geometric (FM)" or "algebraic (bar/operadic)."

**Surface-form triggers:**
- "C^*_ch(A,A)" without model qualifier -> FIRE
- "the derived center Z^der_ch" without specifying which model -> FIRE when E_n structure claimed
- Mixing FM integration language with formal-variable language in same paragraph -> FIRE

### AP-CY63: BD chiral operad vs algebraic End^ch

Beilinson-Drinfeld define chiral operations via D-module maps: End^ch_M(n) = Hom_{D(X^n)}(j_* j^* M^{boxtimes n}, Delta_* M). The algebraic chiral endomorphism operad has End^ch_A(n) = Hom(A^{tensor n}, A((lambda_1))...((lambda_{n-1}))) (formal Laurent series). These are isomorphic after formal-disk restriction and coordinate choice (four-step chain: choose point, choose coordinate, trivialise D-module, identify spectral variables with relative positions).

Counter: never write "the chiral endomorphism operad" without specifying BD (D-module, coordinate-free) or algebraic (formal Laurent series, coordinate-dependent). The bridge is an isomorphism of non-Sigma operads, valid after local coordinate trivialisation. A standalone Bridge Proposition assembling the four steps is currently absent from the manuscript.

**Surface-form triggers:**
- "the chiral endomorphism operad on FM_k(C)" -> FIRE (End^ch is algebraic, not on FM)
- "OPE data from configuration spaces" -> CHECK (correct at geometric level, wrong at algebraic level)
- "End^ch_A" mixing D-module language with formal Laurent series -> FIRE

### AP-CY64: Three-way Hochschild confusion (ChirHoch/HH*/H*_GF)

Three invariants share the name "Hochschild" or "derived centre":
- (i) ChirHoch*(A): chiral Hochschild cochains. Concentrated in {0,1,2} (Theorem H).
- (ii) HH*(A_mode): classical Hochschild cochains of the mode algebra. Concentrated in {0} for simple algebras (Weyl algebra: dim = 1).
- (iii) H*_GF(Lie(A)): Gel'fand-Fuchs continuous Lie cohomology. Unbounded polynomial ring.

The claim "Theorem H has no THH analogue" is FALSE in general: HH* of the Weyl algebra is ALSO concentrated. The genuine "fails to concentrate" object is (iii) Gel'fand-Fuchs, which is neither ChirHoch nor THH. At critical level k = -h^v, ChirHoch* becomes infinite-dimensional (Feigin-Frenkel centre); HH*(A_mode) remains finite. This is the ONLY regime where the two genuinely differ in dimension.

**Surface-form triggers:**
- "ChirHoch is finite while THH is infinite" -> FIRE (wrong: HH*(Weyl) = 1-dim)
- "Theorem H has no classical analogue" -> FIRE (HH* of Weyl is MORE concentrated)
- "concentration fails for topological Hochschild" -> FIRE (confuses GF with THH)
- "the Gel'fand-Fuchs cohomology agrees with ChirHoch" -> FIRE (only at critical level)

### AP-CY65: Spectral parameter provenance

The spectral parameter z in R(z) has a three-part origin:
- (a) Algebraic: the algebra A must have a translation automorphism tau_z (creating evaluation modules V_u).
- (b) Geometric: in the HT setup, tau_z is holomorphic translation on the curve C (the closed colour of SC^{ch,top}).
- (c) Representation-theoretic: R(z) depends on z = u - v (evaluation parameter difference).

The claim "topological Drinfeld centre has no spectral parameters" is FALSE: the Yangian Y(g), as a purely associative algebra, has evaluation modules V_u and spectral R(z=u-v) in its Drinfeld centre. The correct claim is about the bar complex: the chiral bar DIFFERENTIAL is z-dependent (OPE residues); the topological bar COPRODUCT is z-independent (deconcatenation).

**Surface-form triggers:**
- "spectral parameters from the chiral structure" -> FIRE (from evaluation modules)
- "topological center has no spectral parameters" -> FIRE (Yangian counterexample)
- "the R-matrix R(z) comes from the derived center" -> FIRE (comes from evaluation modules)
- "the E_2 braiding carries spectral parameters" -> FIRE (braiding is a single isomorphism; z enters via representations)

### AP-CY66: BZFN ambient category is NOT tunable

The BZFN theorem (Lurie HA 5.3.1.30) states: for an E_1-algebra A in a symmetric monoidal stable inf-category S, Z(LMod_A(S)) = LMod_{HH*(A,A)}(S). Both sides use the SAME S.

The two derived centres arise from two DIFFERENT ALGEBRAS:
- A (chiral algebra in IndCoh(Ran(X))) -> C^*_ch(A,A);
- A_mode (mode algebra in Vect) -> HH*(A_mode, A_mode).

Counter: NEVER say "applying BZFN in two different ambient categories to the same algebra." Say: "two different algebras (A in D-modules, A_mode in Vect), each with its own BZFN equivalence."

**Surface-form triggers:**
- "applying BZFN in two different ambient categories" -> FIRE
- "the same algebra viewed in D-modules vs Vect" -> FIRE (they are DIFFERENT algebras)
- "varying S in the BZFN theorem" -> FIRE (S is not a free parameter)

### AP-CY67: "Spectral parameters from FM_k(C)" is narration

The spectral parameters in End^ch_A are formal algebraic variables. Their relationship to FM configuration spaces is mediated by the local-global identification theorem (a comparison, not a definition). Three layers: (i) global geometric model on FM_{n+1}(X), (ii) formal-disk restriction gives relative positions lambda_i, (iii) algebraic model End^ch_A with formal variables.

**Surface-form triggers:**
- "spectral parameters from FM_k(C)" -> FIRE
- "the chiral endomorphism operad on FM_k(C)" -> FIRE (End^ch is algebraic, not on FM)

### Higher-order ramification guards (AP-CY62--AP-CY67)

WRONG REASONING chains that use these conflations as premises:
- "Because ChirHoch is finite-dimensional, the Drinfeld center is finite" -> WRONG (Drinfeld center is a CATEGORY not a finite-dimensional object)
- "The spectral parameter distinguishes chiral from topological" -> WRONG (Yangian's Drinfeld center has spectral parameters despite being "topological")
- "The curve geometry is what makes quantum groups possible" -> PARTIALLY RIGHT (the curve creates tau_z enabling evaluation modules; but once the Yangian is constructed, spectral parameters persist regardless of curve geometry)

## Cross-Volume Anti-Patterns (Vol I + Vol III, injected for self-contained agent awareness)

### Vol I Anti-Patterns (from ~/chiral-bar-cobar/CLAUDE.md)

AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.
AP4: ClaimStatusProvedHere = verify proof proves stated claim. Status tag != ground truth.
AP40: Environment MUST match tag. Conjectured -> \begin{conjecture}. ProvedElsewhere -> theorem + Remark attribution.
AP5: Grep ALL THREE volumes for variant forms: ~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2, ~/calabi-yau-quantum-groups. After EVERY correction.
AP6: Specify genus, degree, level (convolution vs ambient) for D^2=0, kappa, Theta_A.
AP7: Before writing universal quantifier, verify proof has no implicit type/genus/level restriction.
AP8: NEVER "self-dual" unqualified. Specify which duality, which c. Virasoro self-dual at c=13.
AP12: When proving a claim, search entire manuscript for variants. Update all instances same commit.
AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
AP17: After writing ANY new theorem, IMMEDIATELY audit before building next result.
AP18: "Entire standard landscape" -> list every family, check each against hypotheses.
AP30: CohFT flat identity requires vacuum in V. ALWAYS list conditional axioms at cross-reference.
AP32: Genus-1 != all-genera. obs_1=kappa*lambda_1 unconditional. Multi-weight g>=2: scalar formula FAILS. **Every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation.**
AP36: "implies" proved, "iff" claimed -> write "implies" until converse has independent proof. **Before writing "iff" or biconditional arrow, STOP: is the converse proved in the same theorem? If not, write "implies."**
AP39: kappa != S_2 for non-Virasoro. Coincide only rank-1. Lookup: Heis_k: kappa=k (NOT k/2). Vir_c: kappa=c/2 (ONLY family where kappa=S_2/2). KM: kappa=dim(g)(k+h^v)/(2h^v).
AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.
AP60: Tag only genuinely new content ProvedHere. Classical parts ProvedElsewhere with attribution.
AP67: Strong gen != FREE strong gen. W(p) has 4 strong generators but FREE strong gen OPEN.
AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w) ~ k/(z-w)^2. Simple-pole requires ODD generator (symplectic fermion).
AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
AP108: Heisenberg = CG opening, NOT the atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
AP111: No "What this chapter proves" blocks. Restructure instead.
AP113: kappa without subscripts FORBIDDEN in Vol III. Always kappa_ch, kappa_BKM, kappa_cat, kappa_fiber.
AP114: Stub chapters (<50 lines, no theorems) create false coverage -> develop or comment out.
AP126: Level-stripped r-matrix. Classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. The level k survives d-log absorption. Verify: at k=0 the r-matrix MUST vanish. 42+ instances found across all three volumes (12 in first commit, 30 more in full-volume CG sweep). THE MOST VIOLATED AP in the manuscript. After writing ANY r-matrix, verify k=0 -> r=0.
AP136: Harmonic number notation trap. H_{N-1} != H_N - 1. H_{N-1} = sum_{j=1}^{N-1} 1/j. H_N - 1 = (sum_{j=1}^{N} 1/j) - 1 = sum_{j=2}^{N} 1/j. At N=2: H_1=1 but H_2-1=1/2. CLAUDE.md itself had this error (kappa(W_N)=c*H_{N-1} instead of c*(H_N-1)). When a formula involves harmonic numbers with shifted arguments, ALWAYS evaluate at the smallest N to distinguish.
AP138: Degenerate graded Jacobi. At even suspended degree ||m||=0, [[m,m],f]=0 is TAUTOLOGICAL. The identity [m,[m,f]]=½[[m,m],f] requires ||m|| ODD. Check parity before using Jacobi to relate ad_m^2 to [[m,m],-].
AP139: Unbound variable in theorem. If LHS depends on {g} but RHS on {g,n}, the variable n is FREE. Every variable in a displayed equation within a theorem MUST be quantified. Found in Thm C^{E1}.
AP141: AP126 is systemic. The original AP126 noted "12 instances across 5 files." This rectification session found 30 MORE instances across all three volumes. The error survives because Omega/z and kOmega/z look similar and both give valid-looking formulas. ENFORCEMENT: after writing ANY r-matrix formula, (a) check that k=0 gives r=0, (b) grep the manuscript for bare Omega/z without level prefix.
AP150: Agent confabulation of mathematical structures. Agents can stitch together disparate results from different categorical levels into claimed structures (e.g., an "E_n operadic circle" E_3->E_2->E_1->E_2->E_3) that do not exist in any manuscript. COUNTER: every claimed multi-step structure must be verified arrow-by-arrow against actual .tex source. Each arrow must have an independent theorem reference. If ANY arrow is conjectural, the structure is conjectural.
AP151: Convention clash within a single file. Two different definitions of the same symbol hbar (e.g., 1/(k+2) in one section vs pi*i/(k+2) in another) produce cascade errors in downstream formulas. The B-cycle monodromy q = e^{2*pi*i*hbar} becomes real instead of a root of unity when hbar has an extra factor of pi*i. COUNTER: after writing ANY formula involving hbar, grep the file for all other definitions of hbar and verify consistency.
AP152: "Ordered" ambiguity (labeled vs time-ordered). "Ordered configurations" on a curve means LABELED (non-coinvariant), not totally ordered (the curve has no natural total order). The total ordering lives in the topological direction R. The bar complex B^{ord}(A) is a MIXED object: holomorphic differential (from OPE on C) + topological coproduct (from deconcatenation along R). COUNTER: always specify whether "ordered" means "labeled on C" or "time-ordered on R."
AP153: E_3 scope inflation. The E_3 structure on the derived chiral center Z^{der}_{ch}(A) via the Higher Deligne Conjecture requires B-bar^Sigma(A) to exist as an E_2-coalgebra. For E_inf-chiral algebras (all standard VAs), B-bar^Sigma exists and E_3 follows. For genuinely E_1-chiral algebras (Yangians), B-bar^Sigma does NOT exist (the D-module doesn't descend to X^{(n)}), and the ordered bar gives only E_2 via classical Deligne. COUNTER: every E_3 claim must specify: is the input E_inf or E_1? If E_1, the passage to E_3 requires the Drinfeld center (conjectural).
AP154: Two distinct E_3 structures. (a) Algebraic E_3: from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3: from Sugawara topologisation, requires conformal vector at non-critical level. These are NOT the same; their identification as families over hbar*H^3(g)[[hbar]] is CONJECTURAL (conj:e3-identification). Topological E_3 (b): PROVED for affine KM at non-critical level (thm:topologization); CONJECTURAL for general chiral algebras with conformal vector (conj:topologization-general in Vol I, conj:E3-topological-climax in Vol II). Proof is cohomological; for class M, chain-level E_3 may fail. COUNTER: always specify which E_3 and whether the claim requires Sugawara.
AP155: "New invariant" overclaiming. The ordered chiral homology framework recovers known invariants (KZB from Bernard 1988, elliptic R-matrix from Felder 1994, Verlinde from BD) from a unified bar-complex construction. The novelty is ARCHITECTURAL (a new framework), not COMPUTATIONAL (new numbers). Claiming "genuinely new E_1 invariants" when the numbers are known under other names is misleading. COUNTER: for any claimed "new invariant," check Bernard/Felder/Etingof-Varchenko/Calaque-Enriquez-Etingof.
AP156: Quasi-periodicity convention for wp_1. Two different functions both called wp_1: (a) theta_1'(z|tau)/theta_1(z|tau) -- periodic under z->z+1, quasi-periodic under z->z+tau with increment -2*pi*i. (b) Weierstrass zeta_tau(z) = (a) + 2*eta_1*z -- quasi-periodic under BOTH z->z+1 (increment 2*eta_1) and z->z+tau. These produce DIFFERENT monodromy formulas. COUNTER: always specify which function and verify the quasi-periodicity at the point of use.
AP157: Degeneration-dependent "invariants." A formula computed from a specific degeneration (separating vs non-separating) of a higher-genus curve is NOT an invariant of the curve unless degeneration-independence is proved. The separating degeneration of a genus-2 curve contains ZERO genuinely genus-2 information (everything is determined by genus-0 S-matrix + genus-1 R-matrix eigenvalues). The non-separating channel carries genuinely new data. COUNTER: always specify the degeneration type and state whether independence is proved or assumed.

#### Vol I Failure Modes

**FM24. B-cycle monodromy i^2 error.** When hbar contains a factor of pi*i (from a non-standard convention), the formula q = e^{2*pi*i*hbar} gives q = e^{2*pi*i*pi*i/(k+2)} = e^{-2*pi^2/(k+2)}, which is a REAL number less than 1, not a root of unity. The i^2 = -1 turns an imaginary exponential into a real exponential. This error propagates silently because q still "looks like" a parameter. Counter: after defining q = e^{2*pi*i*hbar}, substitute a specific integer k and verify q is on the unit circle (|q| = 1).
**FM42. Bulk substring replacement corruption (CRITICAL).** Using replace_all for "arity" → "degree" corrupts every English word containing "arity" as a substring: singularity→singuldegree, complementarity→complementdegree, unitarity→unitdegree, regularity→reguldegree, modularity→moduldegree, parity→pdegree, familiarity→familidegree, similarity→simildegree, polarity→poldegree, disparity→dispdegree, linearity→linedegree. These corruptions pass LaTeX compilation silently and are invisible to grep for the target word. 45 corruptions were introduced and fixed in the Vol III campaign. COUNTER: (1) NEVER use bulk substring replace for short strings that appear inside common words. Fix individual instances or use word-boundary patterns. (2) After ANY bulk replace, immediately grep for `ldegree|ndegree|rdegree|pdegree|tdegree` and all known compound forms. (3) Maintain the checklist: words containing "arity" as substring = {singularity, complementarity, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity, popularity, circularity, hilarity}.
**FM43. E_n output scope of CY-to-chiral functor (Vol III).** The functor Φ outputs E_2-chiral at d ≤ 2 and E_1-chiral at d ≥ 3. Writing `Φ: CY_d-Cat → E_2-ChirAlg` without d-qualification is WRONG for d ≥ 3. Found in 5 files across Vol III (preface, cyclic_ainf, cy_categories, main.tex, working_notes). COUNTER: always write `E_n-ChirAlg` with explicit scope `(n = 2 for d ≤ 2; n = 1 for d ≥ 3)`.
**FM44. Agent rate limiting from parallel launch.** Launching >10 agents simultaneously causes mass rate limiting (31 launched, 27 rate-limited, only 4 completed). Even 4 concurrent agents can hit limits. COUNTER: launch agents in batches of 3, not 30+. Expect ~5-13 minutes per agent on 1000-3000 line files.
**FM45. Agent skill fidelity gap.** Subagents receive a compressed ~200-word brief, not the full /chriss-ginzburg-rectify 15,000-word programme. The agents DO apply anti-patterns and fix violations, but they lack the full 5-gate framework, the 15-peak standard, and the connective tissue requirements. COUNTER: for full skill-level rectification, invoke the skill directly in the main conversation for each file. Agents are useful for bulk violation scanning, not for deep reconstitution.
**FM46. Stale preface/introduction line counts (AP112 variant).** Chapter assessment sections in the preface and introduction list line counts that become stale as chapters grow. Found 8 counts off by up to 3x in the Vol III preface. COUNTER: after any large content campaign, update line counts in preface/introduction assessment sections. Automate with `wc -l` comparison.

### Vol III CY-Specific Anti-Patterns (from ~/calabi-yau-quantum-groups/CLAUDE.md)

AP-CY1: CY dimension d != complex dimension n. Fuk(X) is CY_n, D^b(Coh(X)) is CY_n. Not real dim 2n.
AP-CY2: CY trace is in HC^-_d(C), NOT just HH_d -> k. Negative cyclic refinement essential for S^d-framing.
AP-CY3: E_2 != commutative. E_2 braiding is NOT symmetric. E_2 -> E_inf loses quantum group structure.
AP-CY4: Drinfeld center Z(C) (monoidal category) != derived center Z^der_ch(A) (chiral). State which.
AP-CY5: Kazhdan-Lusztig requires root of unity. Generic q: Rep_q(g) semisimple.
AP-CY6: A_X for CY3 EXISTS in the inf-categorical framework (thm:derived-framing-obstruction, April 2026). Chain-level explicit construction remains open for non-formal algebras. Results using inf-cat existence: \begin{theorem} OK. Results requiring chain-level explicit A_X: \begin{conjecture}. **Previous version** (pre-April 2026): "A_X does NOT exist" -- this is SUPERSEDED by the inf-cat proof.
AP-CY7: CoHA != E_1-chiral algebra. CoHA is associative. "E_1-sector of G(X)" assumes G(X) exists (AP43).
AP-CY8: Borcherds denominator != bar Euler product. Identification requires CY-to-chiral functor. For K3 x E: observation, not theorem.
AP-CY9: Jacobi form discriminant constraint. For phi_{k,m} of index m, only discriminants D with D=0 or D=3 mod 4 (m=1) can appear. NEVER fill coefficient table with sequential D-values. Verify discriminant constraint. c(-1)=2 for phi_{0,1} in EZ convention, NOT 1.
AP-CY10: Flop != Koszul dual. Birational flop X->X^+ is derived equivalence PRESERVING kappa. Koszul dual A^! has kappa(A)+kappa(A^!)=rho_K. Flop exchanges chambers; Koszul exchanges algebra/coalgebra. kappa(A_X)=kappa(A_{X+}) for flop, NOT kappa(A_X)+kappa(A_{X+})=0.
AP-CY11: Conditional d=3 transitivity. **Updated**: CY-A_3 is now PROVED (inf-cat). Results chaining through CY-A_3 are no longer conditional. However, results depending on CY-C (quantum group realization) or chain-level explicit A_X remain conditional. DEFAULT for CY-C-dependent results: \begin{conjecture}.
AP-CY12: Shadow class from full computation. G/L/C/M must be determined by computing full shadow tower, NOT by counting generators. Non-formality (m_3!=0) does NOT by itself determine shadow depth. local P^2 is class M (infinite depth), not class L.
AP-CY13: Cross-volume Part number staleness. After ANY Part restructuring in ANY volume, grep ALL THREE volumes for stale Part references. Part numbers are the most fragile cross-reference. Use \ref{part:...} exclusively, never hardcode. **Strengthened**: run grep -rn 'Part~[IVXL]' chapters/ notes/ and verify EVERY match. 7+ stale refs survived a single restructuring.
AP-CY14: **Updated post CY-A_3 proof.** A_X at d=3 now EXISTS (inf-cat). G(X) and C(g,q) remain unconstructed. Any statement whose proof chain passes through G(X) or C(g,q) MUST use \begin{conjecture}. Statements using only CY-A (any d) may use \begin{theorem}. The LLM pattern-matches on logical structure ("if X then Y") without checking whether X exists. 11+ instances fixed across 4 commits.
AP-CY15: README scope inflation beyond .tex ground truth. README must not claim "verified" or "proved" for structural analogies or pattern matches. The README accumulates stronger claims than the .tex supports because the LLM optimizes for impressiveness. After README edits, verify every "proved"/"verified" against corresponding \ClaimStatus tag.
AP-CY16: Matrix size conflation in group quotients. Sp_4 quotient by +/-I_4 (4x4), NOT +/-I_5. O(Lambda^{3,2}) quotient by +/-I_5 (5x5). When two groups of different rank appear in the same formula, the LLM harmonizes subscripts to whichever appears more frequently.
AP-CY17: MF(W) CY dimension is n-2, NOT n-1. For W: A^n -> A^1, MF(W) is CY_{n-2} (Dyckerhoff). ADE in 2 variables: CY_0 (semisimple). Need 4 variables for CY_2. The n-1 vs n-2 error changes which families are CY_2.
AP-CY18: Lattice theta series comparison. Verify q-power divergence by DIRECT COMPUTATION. Leech theta: minimum norm^2=4, first correction at q^2 not q^1. The match with 1/eta^24 extends through q^1. Never conflate j(tau) coefficients with V_Lambda character coefficients.
AP-CY19: A-hat genus argument halving. A-hat(x) = (x/2)/sinh(x/2). Convergence radius = 2*pi (first pole of sin(x/2) at x=2*pi). NEVER drop the /2 in the argument, which gives spurious radius pi. Appeared in 3+ independent computations.
AP-CY20: Normal bundle vs spectral parameters. The Z x Z grading from the normal bundle N_{C/Y} of a curve C in a CY threefold Y connects to the quantum toroidal parameters (q,t) through the Omega-background, NOT through the bundle grading directly. The intermediary mechanism (equivariant localization on the Omega-background, Nekrasov partition function, refinement) must be stated explicitly. NEVER write "N_{C/Y} grading = (q,t) parameters" as a direct identification. Counter: before any claim relating normal bundle gradings to quantum group parameters, name the intermediary mechanism and cite the equivariant/Omega-background passage.
AP-CY21: E_3 bar dimensions RESOLVED. The tricomplex model P(q)^{3g} gives CHAIN-level dimensions for all classes. COHOMOLOGY by shadow class: class G: P(q)^{3g} (formal, infinite). Class L: (1+t)^{3g} = 2^{3g}. Class C: (1+t)^{3g} = 2^{3g} (charge conservation kills d_4). **Class M: 6^g** (PROVED, closed form via Kunneth; d_4 survives giving 6=2*3 per handle). NEVER claim (1+t)^{3g} for class M. Counter: state the shadow class before claiming E_3 bar cohomology.
AP-CY22: Miki automorphism is algebra-specific, NOT operadic. The S_3 permutation of (q_1,q_2,q_3) comes from the Weyl group of the CY torus, not from the E_3 operad in general. Counterexample: k[x]/(x^2) is E_3 but has no Miki. Counter: never derive Miki from the E_3 operad alone; always state it requires the specific algebra U_{q,t}(gl_hat_hat_1).
AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
AP-CY24: Docstring ground-truth confabulation. Agents produce correct CODE but fabricate "ground truth" values in docstrings. The function computes correctly; the docstring claims wrong values for n ≥ 4. Counter: verify EVERY numerical value in docstrings against the actual function output. Especially dangerous for OEIS sequences.
AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
AP-CY26: Verdier duality parameter inversion does NOT invert σ_2. For the Heisenberg, k^! = -k comes from Shapovalov form transposition (Verdier duality transposes the inner product), NOT from σ_2(-h_i) = -σ_2 (FALSE: σ_2 is degree-2 homogeneous, hence EVEN under h_i → -h_i). Counter: derive k^! from Shapovalov/Verdier, not from σ_2 inversion.
AP-CY27: Agent sandbox non-persistence. Background agents report successful file writes but files do NOT persist to the main working tree (sandbox isolation). ALWAYS verify file existence with `ls` after agent completion. Use foreground agents or direct `Write`/`Bash cat` for critical file creation. Three engines were "written" by agents and verified passing inside the sandbox, but did not exist on disk.
AP-CY28: Pole-unsafe test points. When testing rational structure functions g(z) with poles at z=±h_i, test points MUST avoid these values. For h=(1,-2,1): poles at z=±1,±2. The default test point z=2 with h₁=2 gives φ(2)=0, hence g₀₁(2)=1/0. Counter: choose test points far from all ±h_i, e.g., use h=(37,41,-78) for large-parameter safety.
AP-CY29: Wrong-repo file writes. Agents sometimes write files to the WRONG volume's directory. An sl₂ Serre engine was written to ~/chiral-bar-cobar/compute/ (Vol I) instead of ~/calabi-yau-quantum-groups/compute/ (Vol III). Counter: after any agent file write, verify the FULL PATH includes the correct volume's repo root.
AP-CY30: Factored ≠ solved for higher coherence. The 3-particle S-operator S_{ijk}=R_{ij}R_{ik}R_{jk} constructed from a YBE-satisfying R-matrix does NOT automatically satisfy the Zamolodchikov tetrahedron equation (proved: thm:zte-failure, O(κ²) obstruction). NEVER assume pairwise consistency implies higher-order consistency. The Kapranov-Voevodsky theorem requires E_∞ (fully symmetric), which the Omega-deformation breaks.
AP-CY31: Spectral z ≠ worldsheet z. The Drinfeld coproduct Δ_z uses a Yangian spectral parameter (shift of transfer matrix argument u→u-z). The vertex algebra OPE T(z)T(w)~c/2·(z-w)^{-4} uses a worldsheet insertion coordinate. These are DIFFERENT mathematical objects. Setting z=0 in Δ_z removes the spectral shift (no OPE singularity); setting z→w in the OPE produces poles. Counter: before any z=0 argument, state whether z is spectral or worldsheet. Conflation is the source of the adversarial "z=0 singularity" objection (resolved: rem:z-spectral-vs-worldsheet).
AP-CY32: Reorganisation ≠ bypass. The 6d factorization homology route appears to bypass CY-A₃, but each subproblem (local E₃ algebra for compact targets, handle decomposition of K3, VOA identification of output) secretly requires the same chain-level data that CY-A₃ demands. The route REORGANISES the conjecture into subproblems but solves NONE of them independently. Counter: before claiming a bypass, verify that every subproblem in the alternative route is resolved independently of the original conjecture.
AP-CY33: Chain-level ≠ rational. E₃ structure is genuine at the CHAIN level but collapses to E₂ under Kontsevich formality (rational coefficients). The physical content (Miki automorphism, factorization homology, tetrahedron corrections) lives at the chain level. Formality destroys it. Counter: always state whether a claim about E_n structure is at the chain level or the rational/formal level. Claims about "E₃ being trivial" that invoke formality are true RATIONALLY but miss the chain-level content that the physics requires.
AP-CY34: kappa_ch != chi(O_X) at odd d. For ANY compact CY_d with d odd, chi(O_X) = 0 by Serre duality (h^{0,q}=h^{0,d-q} and pairwise cancellation). Therefore kappa_ch = chi(O_X) is FALSE whenever kappa_ch != 0. Known falsifications: E (d=1, kappa=1), abelian surface (d=2, kappa=2, h^{1,0}=2), K3xE (d=3, kappa=3). The formula kappa_ch = chi(O_X) is PROVED ONLY for CY_2 with h^{1,0}=0 (K3, etc.) where HH_{-1}=0 and the Serre argument kills the quantum correction. For d>=3: HH_{-1} = h^{2,0}+h^{1,1}+h^{0,2} is ALWAYS nonzero (h^{1,1}>=1 for projective), so the Serre argument NEVER applies. The correct CY-D uses the categorical chi^CY, distinct from chi(O_X). Counter: NEVER write kappa_ch = chi(O_X) outside the scope d=2, h^{1,0}=0. At d=3: use the dimension-stratified formula (conj:cy-kappa-identification). 76 tests in cy_d_kappa_d3.py.
AP-CY35: B^{(j)} hierarchy confusion. B^{(0)} = Connes B (mixed complex). B^{(j>=1)} = Connes HIERARCHY (S^d-framing). The mixed complex axiom [b, B^{(0)}]=0 does NOT extend to [b, B^{(j)}]=0. Three "proofs" were wrong because of this confusion. Counter: always specify which B^{(j)} and never assume the mixed complex identity for j>=1.
AP-CY36: kappa_ch formula gives wrong value. The formula Sigma(-1)^i dim HH_i gives chi_top (=24 for K3), NOT kappa_ch (=2). The correct formula is the Hodge-filtered supertrace Sigma(-1)^q h^{0,q}. The Serre duality kills non-F^0 contributions. Counter: never compute kappa_ch as alternating sum of HH_i dimensions. Use str_{F^0}(q^{L_0}).
AP-CY37: kappa_BKM = kappa_ch + kappa_cat is a COINCIDENCE for N=1. The correct universal formula is kappa_BKM = c_N(0)/2 (Borcherds weight theorem). Fails for 7/8 diagonal Siegel orbifolds. Counter: use c_N(0)/2, never the naive decomposition.
AP-CY38: Class M E_3 bar != infinite. It's 6^g (proved via Kunneth). The d_4 kills Lambda^0 and Lambda^3, leaving [0,3,3,0] at g=1. Counter: state "6^g (closed form via Kunneth)" for class M, not "infinite."
AP-CY39: Incompatibility Theorem. For single-object cyclic A_inf CY_3: mu_3!=0 forces mu_2=0 on augmentation ideal. Cross-arity cancellation is IMPOSSIBLE at the naive level. The TCFT B^{(2)} differs from naive pairwise contraction. Counter: never assume mu_2 and mu_3 can coexist on the same graded piece at the chain level.
AP-CY40: ProvedHere with no proof block. A theorem carrying \ClaimStatusProvedHere MUST have a \begin{proof} block. The adversarial agent found thm:cy-to-chiral-d3 had ProvedHere but no proof. Counter: grep for ProvedHere and verify a \begin{proof} block follows within 50 lines.
AP-CY41: Internal contradictions from partial updates. When upgrading a conjecture to theorem, ALL instances must be updated. The session found ~30 locations still saying "open" after CY-A_3 was proved. Counter: after any status change, grep all three volumes for the old status string and update every match.
AP-CY42: phi_{0,1} normalization. c(-1)=1 (standard Gritsenko-Nikulin) vs c(-1)=2 (K3 elliptic genus = 2*phi_{0,1}). The factor of 2 is kappa_ch(K3). Propagated silently across 3 engines. Counter: state which normalization convention is in force and verify against the K3 elliptic genus.
AP-CY43: Shadow-Feynman tautology at L>=4. The Feynman engine calls the shadow recursion, making the match tautological. Independent verification requires computing m_k directly (e.g., from k-point conformal blocks). Counter: for L>=4, verify via an independent computation path, not through the shadow recursion.
AP-CY44: CY-D false at odd d. kappa_ch != chi(O_X) when d is odd, because Serre duality forces chi(O_X)=0 for all odd-dimensional CY, while kappa_ch can be nonzero. Root cause: additivity vs multiplicativity. Counter: NEVER write kappa_ch = chi(O_X) outside the scope d=2, h^{1,0}=0. Use the dimension-stratified formula.
AP-CY45: N=2 root-of-unity gives TRIVIAL double braiding. q^2=1 at N=2. Non-abelian MTC requires N>=3 where q^2!=1. Counter: verify q^2 != 1 before claiming modular (non-symmetric) structure.
AP-CY46: No native CY_4 Yangian. pi_4(BU)=Z obstructs E_4. The correct structure is a p_1-twisted double current algebra. The cascade max is E_3 for ALL d>=3. Counter: never write "E_4 Yangian" or "CY_4 Yangian." Use "p_1-twisted double current algebra."
AP-CY47: Structure function degree from Mukai rank, NOT Lie algebra dimension. For E_8 x E_8: degree (24,24) from 24 Mukai directions, NOT (500,500) from dim(e_8)*2. Counter: verify structure function degree against Mukai lattice rank.
AP-CY48: 3d->6d lift rate is only 24%. Algebraic structures lift 100%, topological 0%. 6d is NOT a dimensional upgrade of 3d. Counter: state the lift rate and specify which structures lift and which do not.
AP-CY49: Agent tautological tests. 10% of agent-produced tests are tautological (testing hardcoded values against themselves). Must verify via independent computation paths. Counter: every test must have at least two independent verification sources (AP10 protocol).
AP-CY50: Duplicate agent launches. When relaunching failed agents, check the agent registry to avoid running the same task twice. Duplicate launches waste compute and create merge conflicts. Counter: check the agent registry before any relaunch. Use unique task IDs.
AP-CY51: Rate-limited agents write engines+tests but not manuscript. When an agent is rate-limited, check disk for persisted files before relaunching from scratch. Counter: check disk for persisted files before relaunching. Resume from persisted state.
AP-CY52: Mega-file anti-pattern. Files >3000 lines should be split. toroidal_elliptic.tex was 7190 lines; k3_times_e.tex was 5986 lines. Both needed splitting. Counter: when a .tex file exceeds 3000 lines, split it by section. Target 1000-2000 lines per file.
AP-CY53: π₁(Conf₂) ordered vs unordered confusion. π₁(Conf₂(R^d)) = 0 for d≥3 (ORDERED, S^{d-1} simply connected). π₁(UConf₂(R^d)) = Z/2 (UNORDERED). NEVER confuse ordered and unordered configuration spaces. Counter: always specify ordered/unordered.
AP-CY54: "Categorified averaging" for Drinfeld center. The Drinfeld center is the RIGHT ADJOINT to the forgetful functor BrMon→Mon (categorified COMMUTANT z(A)={a:ab=ba}), NOT a categorified averaging map. The averaging map E₁→E_∞ DESTROYS quantum group data. The center E₁→E₂ CONSTRUCTS braiding via half-braidings. Counter: write "categorified center" or "right adjoint to forgetful", never "categorified averaging".
AP-CY55: kappa_cat = chi(O_X) and kappa_fiber = rank(Lambda) are TOPOLOGICAL invariants of the MANIFOLD, NOT properties of the algebraization. Saying "algebraizations share kappa_cat" is VACUOUS. Only kappa_ch and kappa_BKM depend on the algebraization. Counter: every kappa-spectrum table or discussion MUST distinguish manifold invariants (kappa_cat, kappa_fiber) from algebraization invariants (kappa_ch, kappa_BKM). NEVER present all four as the same type. NEVER assert that kappa_cat "agrees" between algebraizations as if this were meaningful.
AP-CY56: E_n level conflation across CY dimensions. At d=3, A = Φ₃(C) is E₁ (NATIVE). E₂ lives on Z(Rep^{E₁}(A)), NOT on A. NEVER say "E₂-chiral algebra" at d=3 when referring to A itself. The E_n level of A is determined by the Gerstenhaber bracket degree (1-d): d=1→E_∞, d=2→E₂, d≥3→E₁. Counter: always state which object carries the E_n structure (A vs Rep(A) vs Z(Rep(A))).
AP-CY57: Narration instead of construction (Chriss-Ginzburg violation). Saying "the E₂ structure gives the R-matrix" without constructing the half-braiding mechanism. The R-matrix IS the universal half-braiding σ_M(N): M⊗N→N⊗M in Z(Rep^{E₁}(A)). It is CONSTRUCTED from the center, not "given by" or "recovered via" it. Counter: every claim "X gives Y" must be backed by an explicit construction.
AP-CY58: CY-B E_n scope uniformity. CY-B is d-DEPENDENT: E₂-Koszul at d=2 (A is natively E₂), E₁-Koszul at d=3 (A is E₁, inducing E₂ on center via Verdier spectral functor). NEVER say "E₂-chiral Koszul duality" uniformly across all d. Counter: always state the d-dependent E_n level.
AP-CY59: Multiple algebraizations from single functor. Φ(D^b(Coh(K3))) = H_{Muk}. PERIOD. ONE output. The BKM algebra g_{Δ₅} comes from the Borcherds lift (DIFFERENT construction). The Conway module comes from the Leech lattice VOA (DIFFERENT construction). Saying "Φ distinguishes three algebras" is NONSENSE — Φ gives one. Counter: for each algebra, state which CONSTRUCTION produces it. Different κ values come from different constructions, not different applications of Φ.
AP-CY60: Six routes ≠ six applications of Φ. The six routes to G(K3×E) are six DIFFERENT mathematical constructions (Φ, Borcherds lift, lattice VOA, Kummer, sigma model, BLLPR). NOT six applications of the same functor. Their convergence is the CONTENT of CY-C (conjectural), not a consequence of functoriality. Counter: for each route, name the construction and state what it produces independently.
AP-CY61: Shallow correction without first-principles investigation. When a mathematical claim is challenged, do NOT just swap labels (e.g. "averaging"->"right adjoint"). ALWAYS investigate the actual mathematical relationship from first principles. Find: (1) what the claim gets RIGHT (the ghost of a true theorem), (2) what it gets WRONG (the precise conflation), (3) the correct mathematical statement connecting the objects. Every wrong claim contains the seed of a correct theorem -- extract it. Examples: "categorified averaging" is wrong but the factorization E_1 ->^Z E_2 ->^{Sym} E_inf is real; "CoHA = bar complex" is wrong but the character coincidence reflects the Schiffmann-Vasserot theorem CoHA = Y^+; "SN bracket vanishes" is false for non-toric but reveals two independent E_1 mechanisms (operadic vs equivariant). Counter: before any correction, write down the first-principles analysis. If you cannot state the correct theorem, you do not understand the error.


## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
