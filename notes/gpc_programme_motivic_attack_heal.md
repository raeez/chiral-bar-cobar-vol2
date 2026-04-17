# Grothendieck Period Conjecture vs Kontsevich--Zagier: What Does the
# Programme Actually Close?

*Style register: Grothendieck 1966 / Deligne 1989 / Beilinson / Brown / Ayoub
/ Deligne--Goncharov 2005. Russian-school terseness. Attack-then-heal.*

---

## 0. Short form of the attack

The prior F8-motivic-face agent (see
`notes/kontsevich_zagier_period_f8_motivic_platonic.md`) claimed:

> "The programme CLOSES Kontsevich--Zagier for motivic periods."

I do NOT dispute that claim at face value: the three factorisation
operations (Ran additivity, Aut(O) change-of-variables, bar Stokes) do
generate the Q-linear relations on the MOTIVIC MZV ring
Z_•^{mot} via Furusho's pentagon closure, and F8's identification
Z_•^{Φ_KZ} = Z_•^{mot} is real.

But the KZ conjecture has two halves, and the agent implicitly
smuggled the stronger half. The DECISIVE question is whether the
programme says anything about the **Grothendieck Period Conjecture
(GPC)** -- namely, whether the period realisation map

Per : Z_•^{mot} ⟶ C

is injective. GPC implies KZ for motivic periods trivially (Per
injective ⇒ motivic relations = numerical relations), but GPC is
STRICTLY stronger: it says Q-linear relations among the ABSTRACT
numerical periods ζ(n_1, ..., n_k) ∈ R are ALL captured by motivic
relations. GPC is wide open (Deligne 1989 `Catégories tannakiennes`;
Ayoub 2014 `Motifs et anneaux dérivés`; Brown 2012 Annals §8).

---

## 1. Step (a) -- what the F8 agent gets RIGHT (ghost of the true theorem)

The F8 face supplies, as an invariant of the chiral-algebra r-matrix
moduli, a faithful embedding

(F8) Z_•^{mot} ↪ Face(A)_{bar-degree ≥ 3}.

Three consequences are genuinely true at the motivic level:

(i) Every Q-linear relation among the motivic ζ^{mot}(w_1,...,w_r)
 that holds in Z_•^{mot} holds in the ℏ^w component of Φ_KZ acting on
 F1. (Brown 2012 Thm 1.1 + Furusho 2011 pentagon closure.)

(ii) The three KZ operations (additivity, change-of-variables, Stokes)
 ARE the three colours of the bar complex.

(iii) The weight-6 Q-line Q·ζ^{mot}(3)² is recovered from the
 ℏ^6 term of Φ_KZ via the symmetric square σ_3 ⊙ σ_3 in U(grt_1);
 grt_1 itself has dim 0 at weight 6 (antisymmetry of [σ_3,σ_3]),
 but U(grt_1) has dim 1, and that is where the r-matrix r^mot lives.

All three are correct at the motivic level. Agent claim (ii) on KZ
operations is a genuine **reduction**, not a mere reformulation.

---

## 2. Step (b) -- what the agent gets WRONG (precise overreach)

The agent's verdict "KZ for motivic periods = CLOSED by the programme"
is correct. The agent's HIDDEN slip is that ALL the work happens on
the motivic side -- inside Z_•^{mot} as a Q-linear abstract ring with
its motivic Galois action. Per : Z_•^{mot} → C never appears.

**The GPC question** -- is Per injective? -- requires information the
programme categorically cannot supply:

• GPC is a TRANSCENDENCE claim about numerical values of periods in
 C. It says: for every Q-linear relation Σ_I c_I ζ(I) = 0 among
 numerical MZVs, there is a MOTIVIC lift Σ_I c_I ζ^{mot}(I) = 0 in
 Z_•^{mot}.

• The programme lives entirely over Q (chiral algebras, bar complex,
 factorisation homology, GRT_1(Q)-torsor, motivic MZV ring
 Z_•^{mot} as a graded Q-Hopf algebra). Nothing in the programme
 performs numerical evaluation ζ^{mot}(w) ↦ ζ(w) ∈ R.

• The period map Per is an input to the programme from outside:
 Brown 2012 chooses a specific realisation functor ω_B (Betti
 realisation) and defines Per as ω_B applied to the motivic lift.
 Chiral algebras do not select ω_B; they live in motivic de Rham
 cohomology (the abstract Tannakian ring), and the choice of Betti
 comparison is exogenous.

• Concretely: GPC says that if c_1 ζ(3)² + c_2 ζ(6) = 0 holds
 NUMERICALLY, then c_1 ζ^{mot}(3)² + c_2 ζ^{mot}(6) = 0 holds
 MOTIVICALLY. The programme predicts the RHS independently (via F8
 at weight 6), but cannot bridge RHS ↔ LHS without Per.

**Verdict on (b).** The agent claim "closes KZ for motivic subring" is
true; the tacit upgrade to "closes GPC for motivic subring" would be
FALSE if it were made. GPC = injectivity of Per is not closed, not
reduced, not even approached by the programme's architecture.

---

## 3. Step (c) -- precise correct relationship

Let me distinguish three distinct closures:

**(C-motivic)** KZ relations on Z_•^{mot}: every Q-linear motivic
relation follows from KZ operations (a)+(b)+(c). CLOSED by the
programme via F8 + Furusho pentagon.

**(C-period)** KZ relations on numerical periods: every numerical
 Q-linear relation Σ c_I ζ(I) = 0 in R follows from KZ operations.
 This requires Per injective, = GPC. NOT CLOSED. The programme has
 nothing to offer.

**(C-rank)** Explicit rank of the F8 period matrix at weight ≤ W:
 compute dim_Q image(Per|_{Z_≤W^{mot}}) and compare to dim_Q
 Z_≤W^{mot} = Zagier's Padovan-sequence prediction
 (1, 0, 1, 1, 1, 2, 2, 3, 4, 5, ...). If Per is injective at weight
 ≤ W, the two match. PARTIAL INFORMATION -- computable at specific
 weights, but the injectivity is hypothesis not theorem.

---

## 4. Explicit Φ_KZ rank readout at weight ≤ 10

Zagier's conjectural dimension sequence for Z_•^{mot} (Brown 2012 Thm
1.3, unconditional for the motivic ring):

| w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|----|
| dim Z_w^{mot} | 1 | 0 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 7 |

(modulo ζ^{mot}(2) -- which is kept here since we are comparing to
 R-periods not Brown's ζ(2)-quotient).

F8 rank prediction = dim U(FreeLie(σ_3, σ_5, σ_7, ...))^{(w)} ⊕
(π^2·lower-weight contributions). In Brown's Q-linear motivic algebra
this matches the table above (Brown 2012 Cor 1.2).

**Numerical rank.** The actual rank of the Φ_KZ period matrix under
Per at weight ≤ 10 -- i.e. the rank of the matrix

M_{Per,≤10} := [Per(b_i)]_{b_i ∈ basis Z_{≤10}^{mot}}

considered as a real matrix -- is UNKNOWN unconditionally. Deligne--
Goncharov 2005 prove this rank matches the upper bound for MIXED TATE
MOTIVES (i.e. the motivic rank is sharp over Q(ζ_N) after Galois), but
the numerical rank match rests on Per being injective.

**Partial numerical information the programme DOES supply**: at level
k=1 affine KM (lattice VOA), the Φ_KZ associator reduces to the
rational associator Φ_1 (= identity at weight ≥ 3). Hence the F8
face collapses to F1 at k=1, and the weight-≥3 MZV coefficients
vanish. This is a TRUE statement of the programme but it is trivial
(rational associator has no MZV content).

At generic level (e.g. k ∉ Q), the full Z_•^{mot} embeds in F8, and
the rank at weight ≤ 10 is predicted to be 1+0+1+1+1+2+2+3+4+5+7 =
27, matching Zagier's count. Per injective would confirm this
numerically. **Programme does not supply numerical confirmation.**

---

## 5. Can the programme provide arithmetic obstruction information?

The attack's item (3) asks: can the programme give ARITHMETIC
information about Q-linear independence of ζ(n_1, ..., n_k)?

**Answer: partial, and only at the level of motivic Galois.**

Three separations:

(α) The motivic Galois action 𝒢^mot ↷ Z_•^{mot} distinguishes motivic
 classes. The programme internalises this as GRT_1(Q)-action on
 Face(A) via F8. This IS information: the programme predicts the
 motivic rank = Zagier's prediction, all weights.

(β) The numerical rank (after Per) requires at minimum one
 algebraically-independent numerical input -- e.g. that ζ(3) is
 irrational (Apéry 1978) or ζ(3), π^2 are Q-linearly independent
 (known). The programme does not supply any such input.

(γ) Conjectural Q-independence of {ζ(3), ζ(5), ζ(7), ...} is strictly
 stronger than any theorem: Ball--Rivoal 2001 gives infinitely many
 odd ζ-values are irrational but their Q-linear relations are
 unconstrained. The programme's odd-weight generator structure
 (σ_{2k+1} in grt_1) is MOTIVIC evidence for Q-independence, but
 cannot promote motivic to numerical independence without GPC.

**Verdict on arithmetic obstruction.** The programme CAN say: "if
k numerical periods ζ(I_1), ..., ζ(I_k) have a Q-linear relation,
then either (GPC holds and there is a motivic lift), OR (GPC fails
and the programme says nothing)". This is a conditional arithmetic
statement, parameterised by GPC as an independent hypothesis. It is
NOT a new arithmetic obstruction.

---

## 6. Verdict (≤200 words; the short answer the attack asked for)

**Does the programme close the Grothendieck Period Conjecture for the
motivic subring?**

**No.** The closure is strictly weaker: KZ-for-motivic-periods
(closure of Q-linear relations on Z_•^{mot} under the three
factorisation operations), NOT GPC (injectivity of the period map
Per : Z_•^{mot} → C).

GPC is a transcendence statement about numerical values of motivic
periods in R; the programme lives over Q and lacks the Betti
realisation data needed for Per. The F8 motivic face provides a
faithful embedding Z_•^{mot} ↪ Face(A), which is motivic-rank
information; numerical rank requires the independent hypothesis of
Per injective.

The prior agent's claim "closes KZ for the motivic subring" is
correct as stated. The GPC upgrade is an overreach. Concretely: F8
predicts motivic rank 27 at weight ≤ 10 (Zagier sequence sum); this
matches the numerical rank IFF GPC holds at weight ≤ 10, which is
not a programme theorem.

The programme is a closure for motivic relations, a reformulation for
numerical ones. Genuine partial progress, not a GPC solution.

---

## 7. Heal-direction (follow the HEAL-MODE directive)

Per the HEAL-MODE clause in CLAUDE.md, this is the STRONGEST HONEST
FORM the programme can offer at the GPC interface:

**Theorem (programme F8 contribution to periods -- strongest honest
form).** *Let A be a chirally Koszul chiral algebra with conformal
vector at non-critical level. The F8 motivic face of Face(A) is
canonically isomorphic as a graded Q-Hopf algebra to Z_•^{mot}
(Brown). The three factorisation operations (Ran additivity,
Aut(O)-equivariance, bar Stokes) realise Furusho's pentagon + Ihara--
Kaneko derivation relations, and hence generate all motivic-Galois
Q-linear relations on F8. Consequently: the Kontsevich--Zagier
conjecture for motivic periods (not numerical periods) reduces to
programme-native factorisation axioms. The injectivity of the period
map Per : Z_•^{mot} → C (Grothendieck Period Conjecture) remains an
independent transcendence statement outside the programme's
architectural scope.*

This is the maximally honest statement. It does NOT downgrade the F8
achievement; it locates GPC precisely outside the programme's reach,
where it genuinely is.

---

## 8. What would CLOSE GPC inside the programme?

For completeness (= frontier speculation):

GPC injectivity for Z_•^{mot} requires a chain-level realisation
functor ω_B : motivic de Rham → Betti that the programme could define
NATIVELY from bar-cobar data. This would require:

(i) A Betti analogue of F1 (the identity face) -- a chain-level
 realisation of the rational associator as a numerical integration
 functor. The programme's E_3-topological factorisation homology,
 evaluated on concrete manifolds (S^1 × R, T^2, Σ_g), gives
 numerical output in C. If these numerical outputs were
 shown to match Per on the F8 image, a partial GPC would follow.

(ii) This is close to Costello--Gaiotto's partition-function
 computations for BV-quantised 3d HT theories: the partition
 function on T^3 for E_3-topological A should numerically
 evaluate F8 at the associator image. CLAUDE.md's FM128 (V^♮
 orbifold BV anomaly vanishing) suggests this is computable for
 specific A.

(iii) A rigorous such chain would upgrade F8 from a Q-motivic face
 to a Q-motivic-plus-Betti face, and matching motivic vs numerical
 rank at each weight would constitute an explicit verification of
 GPC at that weight. NOT a proof, but accumulated numerical
 evidence of a new programme-native kind.

This is the only honest path. The programme does not currently supply
ω_B; building it is a frontier task (adjacent to Vol III's Mock
modular K3 periods and arithmetic_shadows.tex bounds).

---

## 9. Inner music

The F8 face tells us Z_•^{mot} is an intrinsic invariant of chiral
algebra structure. The Grothendieck Period Conjecture tells us
Z_•^{mot} faithfully detects the numerical periods. These are two
separate hypotheses; the programme makes the first into a theorem
(via bar-cobar + Brown + Furusho) and leaves the second untouched.

The inner music: GPC is the bridge from abstract motivic Galois to
numerical transcendence. The programme builds the motivic-Galois
side from chiral algebra data; the numerical side is external. The
honest statement is that the programme CONSTRUCTS Z_•^{mot}
intrinsically, from pure factorisation-algebra operations on a chiral
algebra, but it does not EVALUATE Z_•^{mot} in R. Evaluation is the
transcendence problem, and transcendence is not a programme
operation.

The chiral bar complex hears the motivic Galois group; it does not
hear the real line.
