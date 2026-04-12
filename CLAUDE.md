# CLAUDE.md -- Volume II: A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol II-specific material.**

## Identity

The bar complex B(A) is an E_1-chiral coassociative coalgebra over (ChirAss)^!. The SC^{ch,top} structure emerges on the derived chiral center Z^{der}_{ch}(A) = C^bullet_{ch}(A,A): the pair (C^bullet_{ch}(A,A), A) is the SC datum where bulk acts on boundary. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. Physics IS the homotopy type.

~1,500pp, this repo. Seven parts: I(The Open Primitive) II(The E_1 Core) III(Seven Faces of r(z)) IV(Characteristic Datum and Modularity) V(Standard HT Landscape) VI(Three-Dimensional Quantum Gravity = CLIMAX) VII(Frontier).

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

The modular extension: the A_inf structure becomes curved at genus >= 1. The curvature kappa * omega_g is the obstruction to flatness. Curved Dunn additivity (conjectural) would extend E_2 = E_1 x E_1 to the curved setting.

### Rung 4: E_3 — Holomorphic-topological (1 cpx + 1 real = 3 real) [Parts V-VI = CLIMAX]
- **X x R** (slab, holomorphic on X, topological on R): E_3 = E_2 x E_1 by Dunn. The E_2 is the holomorphic/braided structure on X (Rung 2). The new E_1 is the topological direction R (transverse).
- **X x [0,1]** (slab with two boundaries): Bar complex of the bulk in the transverse direction. The interval model in the E_1 transverse factor.
- **X x S^1** (torus bundle): Hochschild of the bulk in the transverse direction. Modular invariance of the 3d theory.

The E_2-to-E_3 step: the A_inf-chiral algebra structure. An A_inf-algebra in E_1-chiral algebras is the 3d HT bulk factorisation algebra. Z(A) with E_2 gives the bulk observables; the transverse E_1 gives the topological direction; together E_3. This is the CLIMAX: 3d quantum gravity = E_3-chiral algebra = derived center of boundary with transverse E_1 extension.

For E_3: CFG (arXiv:2602.12412) construct a filtered E_3-algebra from BV quantisation of Chern-Simons. Their factorisation homology trace = RT link invariant. This is the perturbative E_3 at genus 0.

### The missing rung: E_1-chiral quantum groups and the modular operad
The E_2-to-E_3 step requires:
1. The modular operad governing A_inf-algebras in E_1-chiral algebras (not yet constructed).
2. The chiral coproduct Delta: A -> A otimes A on the E_1-chiral algebra (not visible in the shadow tower; sources: Gaiotto-Rapcak-Zhou arXiv:2309.16929, Jindal-Kaubrys-Latyntsev arXiv:2603.21707).
3. Curved Dunn additivity at genus >= 1 (conjectural).

An E_1-chiral quantum group is: E_1-chiral algebra A + chiral coproduct Delta + R-matrix R(z) + quasi-triangularity + antipode, such that Mod_A is braided monoidal (E_2 in Cat). This provides the data for the E_2-to-E_3 step.

The volume goes: E_1 (Parts I-II) -> E_2 (Parts III-IV) -> E_3 (Parts V-VI). Part VII is the frontier beyond E_3.

### The E_N definition ladder: CHIRAL vs TOPOLOGICAL (MUST BE IN THE MANUSCRIPT)

CRITICAL DISTINCTION: E_N-CHIRAL != E_N-TOPOLOGICAL. Chiral depends on complex structure. Topological does not. The conformal vector T(z) (Sugawara) is what enables TOPOLOGIZATION: chiral -> topological. Without conformal vector: stuck at chiral. With conformal vector at non-critical level: can topologize.

The volume must define E_N at BOTH chiral and topological levels for N=1,2,3.

**E_1 level (Parts I-II):**
- E_1-chiral: E_1-algebra in chiral algebras on X. Ordered OPE data. Bar complex B^{ord}(A). MANUSCRIPT HAS THIS.
- E_1-topological: E_1-algebra (just associative, no holomorphic dependence). Deconcatenation coproduct on Conf^<(R). MANUSCRIPT HAS THIS (it's the topological factor of SC^{ch,top}).

**E_2 level (Parts III-IV):**
- E_2-chiral: chiral algebra with braiding from the OPE. The derived center Z^{der}_{ch}(A) carries this via chiral Hochschild. Depends on complex structure of X. The R-matrix R(z) has spectral parameter from the holomorphic direction. LIVES ON Z(A), NOT on A.
- E_2-topological: braided algebra independent of complex structure. Would require topologizing the chiral E_2 via conformal vector. At this level: the Drinfeld center of the E_1-topological algebra.

**E_3 level (Parts V-VI = CLIMAX):**
- E_3-chiral = E_2-chiral x E_1-top: the HT bulk. Holomorphic on X, topological on R. Factorisation algebra on X x R. This is the HOLOMORPHIC-TOPOLOGICAL structure. NOT AUTOMATIC from the chiral algebra. Requires a 3d HT theory whose boundary is A. For gauge-theoretic examples (Kac-Moody): the 3d holomorphic CS theory (from 6d holomorphic gauge theory) provides this — proved by Costello-Li / CFG. For GENERAL vertex algebras: requires quantizing the Poisson vertex model, which is HARD OPEN WORK, not automatic. The E_2 -> E_3-chiral step is CONJECTURAL in general.
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
- Sources of chiral coproducts: Gaiotto-Rapcak-Zhou (arXiv:2309.16929, type A, M2-M5 fusions), Jindal-Kaubrys-Latyntsev (arXiv:2603.21707, ADE quivers, CoHA vertex coproducts).

## Preface Geometric Escalation (Platonic Ideal)

The preface walks through topologico-combinatoric stratified spaces from a point to E_3. At each stage a degree of freedom is gained, a new configuration space appears, and a new algebraic structure emerges on a specific object. The volume climbs to E_3-TOPOLOGICAL (not E_3-chiral).

| Stage | Space | Structure gained | Lives on |
|-------|-------|-----------------|----------|
| 0 | Point | Classical Koszul duality | A |
| 1 | R | E_1 coalgebra (deconcatenation) | B(A) |
| 2 | [0,1], R_≥0 | A_inf, modules, line operators | B(A), C(I) |
| 3 | C | Chiral product (bar differential) | B(A) |
| 4 | C x R | E_1 dg coalgebra (both structures) | B(A) |
| 5 | H (half-plane, dH=R) | SC^{ch,top} (bulk -> boundary) | PAIR (Z^{der}_{ch}, A) |
| 6 | D (formal disk) | Vertex algebras, End^{ch}_A | Local model |
| 7 | Annulus, Sigma_g | Modular tower, curvature kappa*omega_g | Theta_A |
| 8 | Drinfeld center | E_2 (chiral Deligne) | Z^{der}_{ch}(A) |
| 9 | Topologization | E_3-TOPOLOGICAL (Sugawara + conformal vector) | Z^{der}_{ch}(A) |

Stage 9 = E_3-TOPOLOGICAL is the POINT OF THE VOLUME. NOT E_3-chiral: the conformal vector KILLS the chiral direction at the cohomological level. Sugawara at non-critical level: T(z) = {Q, G(z)}, so C-translations are Q-exact, the complex structure on C becomes irrelevant in cohomology, the two colors of SC^{ch,top} collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra independent of the complex structure on C. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct, holomorphic direction carries nontrivial cohomological information). At critical level k = -h^v: Sugawara undefined, center jumps, topologization fails.

### SC^{ch,top} is the GENERIC case (corrected emphasis)

E_3-topological is a SPECIAL CASE requiring conformal vector. SC^{ch,top} is the structure that MOST chiral algebras carry on their derived center pair. Examples stuck at SC^{ch,top}: Heisenberg, lattice VOAs, critical level, E_1-chiral algebras (Yangians), free fields without Sugawara, CY functor outputs.

SC^{ch,top} must be understood AS A FIRST-CLASS OBJECT with five redundant presentations:
1. **Operadic**: generators (codim-1 boundary strata of FM_k(C) x Conf_m(R)), relations (codim-2)
2. **Koszul dual**: SC^{ch,top} is Koszul self-dual; W(SC^{ch,top}) = cofibrant replacement
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

## Opus 4.6 Failure Modes (Vol II-Specific)

FM24: B-cycle i^2 error. q = e^{2*pi*i*pi*i/(k+2)} is real, not root of unity. Counter: verify |q|=1.

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
| 3D gravity | Part VI: 3d quantum gravity = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | Boundary-linear bulk = Hochschild proved; full global triangle (boundary -> bulk -> boundary) conjectural beyond the Koszul locus |

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

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
