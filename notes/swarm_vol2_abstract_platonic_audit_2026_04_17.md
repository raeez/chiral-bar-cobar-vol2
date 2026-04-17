# Vol II Abstract/Preface — Platonic-Ideal Audit (adversarial agent #5 of 5)

2026-04-17. Scope: the claimed identity of Vol II as expressed in `README.md`, `chapters/frame/preface.tex` (2274 lines), `chapters/theory/introduction.tex` (2714 lines), and the CLAUDE.md "Identity" block. Read-only audit; no commits.

---

## Section 1. Claimed identity (≤200-word extract)

Vol II claims to be *the physical volume* of the trilogy: Vol I constructs E_n-chiral algebras as algebraic-geometric objects on curves (ordered bar, derived chiral centre, SC^{ch,top} pair); Vol II *discovers that these constructions ARE physics*. The derived chiral centre Z^{der}_{ch}(A) is the bulk of a 3d HT gauge theory; the SC^{ch,top} pair is a boundary-bulk system; the E_3-topological algebra IS a TQFT. The paradigm case is 3d gravity (Brown-Henneaux: Vir_c = boundary of SL(2,R)×SL(2,R) Chern-Simons). The volume climbs an E_n ladder (stages 0-9) ending at E_3-topological (Stage 9) with a conditional E_∞-topological upgrade (iterated Sugawara). Seven (→ eight) parts; five (→ seven) theorems: A-D+H inherited from Vol I plus native Theorem F (Universal Holography functor Φ_hol) and Theorem G (Infinite Fingerprint Classification). The README compresses all of this into "A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT"; the preface opens with "From algebraic geometry to physics" and closes with "holomorphic chiral factorisation (co)homology via bar/cobar at various geometric locations." Approximately 1,949 pages; 3,200+ tagged claims; 3,703 collected tests.

---

## Section 2. Claim vs content delta (word-for-word mismatches)

### 2a. "Two theorems native to this volume" — fragile status

Preface Section II (`preface.tex:456-478`): "this volume proves two additional theorems... *Theorem F (Universal Holography)* — every boundary-linear chiral algebra A with conformal vector at non-critical level is the boundary of a canonical 3d HT gauge theory T_A... *Theorem G (Infinite Fingerprint Classification)* — ... is a complete invariant."

Adversarial finding: Theorem F's scope statement in the preface is broader than the body. The programme-climax theorem in `chapters/theory/wn_tempered_closure_platonic.tex` etc. is SCOPE-QUALIFIED to the non-logarithmic C_2-cofinite standard landscape + irrational cosets; W(p) triplet was downgraded to Conjectured (Vol II commit `a5640de`, per Vol I CLAUDE.md "Beilinson-rectified open frontiers"). The preface opens the theorem with "every boundary-linear chiral algebra A with conformal vector at non-critical level" — no scope qualifier on W(p). FM214 in Vol II CLAUDE.md flagged this exact "universal IS-claim without scope" pattern at preface:26-39,1606,1765,1811 ≥ 5 times; the heal directive ("lead every IS-claim with 'On the boundary-linear exact sector...'") is not honored in the preface abstract.

### 2b. "On the original complex, at the level of chain maps"

Section XI''' (preface:1997-1999) promotes programme-climax to "as E_3-topological factorisation algebras, *on the original complex, at the level of chain maps*." But CLAUDE.md (Vol II) "Bridges" row at (5) reads: "genuswise chain-level BV/BRST/bar PROVED in weight-completed category for all four classes (prop:bv-bar-class-m-weight-completed, 2026-04-16); direct-sum chain-level class M genuinely false on raw direct sum (AP203-healed)." The preface's "original complex, at the level of chain maps" conflates weight-completed Banach B_ρ(A) with raw direct-sum original complex. This is the exact AP203 pattern. CLAUDE.md's tempered-extension row qualifies the original-complex claim to "the NON-LOGARITHMIC C_2-cofinite standard landscape"; preface does not.

### 2c. "Heptagon" in preface vs "pentagon of equivalences" in some chapters

Preface:243-252 advertises "seven mutually redundant presentations forming a *heptagon of equivalences*" (five classical + Drinfeld-centre + derived-AG). But Vol II CLAUDE.md §"SC^{ch,top} as first-class object" still lists five presentations (operadic, Koszul dual, factorisation, BV/BRST, convolution) as a *pentagon*. The `sc_chtop_heptagon.tex` file exists but the preface's heptagon narration is ahead of most chapter rhetoric — classic metadata/ground-truth drift (FM111 pattern).

### 2d. README lists standalone that does not exist

README line 75: "Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd)". FM196's parenthetical: "bonus: README of Vol II lists 'ordered_associative_chiral_kd' as a standalone but file is NOT present on disk." Still live.

### 2e. Chriss-Ginzburg "precise parallel" (preface:681-707)

Section IV: "The parallel with the Chriss-Ginzburg theory is precise: Springer resolution ↔ Lagrangian embedding; Steinberg variety ↔ bar complex; convolution ⇒ Hecke algebra ↔ convolution ⇒ SC^{ch,top}-algebra; Springer correspondence ↔ bulk-boundary-line triangle; KL basis ↔ MC element α_T; H_W at q=1 ⇒ C[W] ↔ classical limit ⇒ PVA; KL polynomials ↔ shadow obstruction tower; Hecke eigenvalues ↔ spectral R-matrix." FM216 flags this entire table: "CG 'precise parallel' — 7-row table, zero rows carry equivalence theorems. Springer↔Lagrangian, KL-basis↔α_T, KL polynomials↔shadow tower are metaphors." Preface still calls it "precise."

### 2f. "Only with all five assembled" / "only language"

Preface:1645 "Only with all five assembled does the gravitational theory become computable"; preface:64 "factorization is the only language." FM218 flagged these universal quantifiers; not removed.

### 2g. "Seven Faces" numbering drift

Part III described as "seven faces" in the README seven-parts table (README:35); in the preface body (XI, preface:1575-1591) it expanded to "nine representatives" F1–F9 parametrising a GRT_1(Q)-torsor. The README table and preface Section III headline both still use "Seven Faces" as section name. Reader gets "seven" → then nine → then seven-parts → then eight-parts, with cardinality drift within one document.

### 2h. Heisenberg reached E_3 / Stage 9 scope

Preface:240-242: "Examples stuck at SC^{ch,top}: critical-level Kac–Moody V_{-h^∨}(g) where Sugawara degenerates; genuinely E_1-chiral algebras (Yangians) where no conformal vector is available; and Calabi–Yau functor outputs lacking conformal vectors." Yet elsewhere (preface:193-227) Stage 9 is proved for affine KM, W-algebras, ALL freely-generated PVAs, 71 Schellekens, Monster, irrational cosets. FM62 (Vol II) explicitly: "Heisenberg and lattice VOAs reach E_3-topological" — the "stuck" list is narrower than the preface paragraph acknowledges.

### 2i. "Five named open problems" (Section XII) vs "four closed frontiers" (Section XI)

Section XI (preface:1508-1516): Part VIII promotes "four closed frontiers" (curved-Dunn H², DS–Hochschild, periodic-CDG, chain-level chiral Deligne–Tamarkin) to theorems. Section XII (preface:2210-2252) THEN lists "five named open problems": chain-level topologisation, general topologisation, MC5 chain-level class M, global triangle, Stokes regularity gap. Overlap with Part VIII is unacknowledged: Item (iii) "MC5 chain-level class M" IS the DS–Hochschild-bridge closure; Item (v) "Stokes regularity gap" IS the curved-Dunn H²=0-at-g≥2 closure. Preface advertises both "closed" and "open" for the same content within 700 lines.

### 2j. "R-matrix data destroyed by averaging" → stated as abstract motivation, but the body's ordered/symmetric story is more nuanced

Preface:588-597 asserts "The Σ_n-coinvariant projection destroys the R-matrix data." But per Thm A^{∞,2} R-twisted Σ_n-descent in `factorization_swiss_cheese.tex` (CLAUDE.md Vol II §"Theorem A at full strength"), B^Σ(A) ≃ (B^{ord}(A))^{Σ_n-coinv, L_R-twisted} with monodromy generated by R(z); the R-matrix is NOT destroyed — it becomes the twist. Preface's motivational claim contradicts the volume's own upgrade.

---

## Section 3. Proposed Platonic-ideal abstract (250-400 words, LOSSLESS)

**Volume II — A-infinity Chiral Algebras and 3d Holomorphic-Topological QFT.**

Volume I constructs the algebraic engine: the ordered bar complex B^{ord}(A) = T^c(s^{-1}\bar A) of a chiral algebra A on a curve, an E_1 coassociative coalgebra whose differential comes from OPE residues on FM_k(C) and whose coproduct is deconcatenation along Conf_k^<(R). This volume asks one question: **when A carries a conformal vector at non-critical level, is the derived chiral centre Z^{der}_{ch}(A) the algebra of bulk observables of a canonical 3d holomorphic-topological gauge theory whose boundary algebra is A?** The answer is the **Universal Holography theorem** (Theorem F, this volume, native): on the non-logarithmic C_2-cofinite standard landscape and on irrational cosets, there exists a canonical 3d HT theory T_A with Obs^∂(T_A) ≃ A and Obs^{bulk}(T_A) ≃ Z^{der}_{ch}(A) as E_3-topological factorization algebras, on the original complex at the level of chain maps after weight-completion B_ρ(A) at ρ<|c|/β_A. The classification that indexes this correspondence is the **Infinite Fingerprint theorem** (Theorem G, native): the six-slot φ'(A) = (p_max, r_max, χ_VOA, n_strong, coset, κ_ch) is a complete invariant of the Koszul-bar-complex structure; the G/L/C/M/FF quaternitomy — a fifth Feigin-Frenkel class at κ=0 — is its coarse projection. The volume executes this correspondence along a nine-stage geometric ladder from point to formal disk to complex plane to half-plane to modular surface to derived centre to topologization, and through a nine-face GRT_1(Q)-torsor presentation of the collision residue r(z). The five Vol I theorems (A bar-cobar, B inversion, C complementarity, D modular characteristic, H Hochschild concentration) control each stage; Theorem F and Theorem G close the 3d-HT story in the original chain-level complex on the tempered locus and in weight-completion elsewhere. The logarithmic W(p) triplet is the sole standard-landscape family for which chain-level E_3-topologization remains conjectural. Critical-level Kac-Moody, genuinely E_1-chiral Yangians, and CY functor outputs without conformal vector remain stuck at SC^{ch,top} (Stage 8). Part VIII promotes four frontiers to theorems (curved-Dunn H²=0 at g≥2, DS–Hochschild bridge, admissible-level periodic-CDG, associator-fixed chain-level chiral Deligne–Tamarkin). The climax (Part VI, 3d quantum gravity via Vir_c) is the N=2 shadow of an iterated-Sugawara E_∞-topological endpoint at W_∞[λ].

---

## Section 4. Preface structural critique (section-by-section)

**Section 0 "From algebraic geometry to physics"** — Correct thesis statement. Strong opener. Identifies Vol II as the physical-realization volume. The nine-stage stage table is a genuine Platonic structure.

**Section I "The open/closed primitive"** — Starts with the Heisenberg worked example. The CG-standard "deficiency opening" move. Good. Heisenberg four-step verification works as the motivic atom.

**Section II "What this volume proves"** — Introduces Theorem F (Universal Holography) and Theorem G (Infinite Fingerprint). PROBLEM: Theorem F is advertised without scope; the body qualifies it to non-logarithmic C_2-cofinite + irrational cosets. This is the load-bearing abstract claim of the volume and needs FM214 heal treatment.

**Section III "Three conceptual leaps"** — Commutative-to-E_1, Genus-0-to-modular, Local-to-nonlocal. Clean tripartite arc. This section is architecturally sound. The "fourth leap" rider ("derived centres produce physics") is well-motivated — but it's a meta-leap about the volume itself, not the subject; better subsumed in Section 0.

**Section IV "The Steinberg principle"** — CG metaphor table. FM216 flagged "precise parallel" overreach. The Steinberg principle IS a genuine organizational tool (one coalgebra, three functors: cobar, Verdier, Hochschild), but the 7-row CG table should be titled "Structural analogy" with per-row theorem/metaphor footnotes.

**Section V "The Swiss-cheese operad SC^{ch,top}"** — Says SC sits between E_1-chiral and E_3-topological in the E_n hierarchy; correct position. The heptagon extension (two new faces: Drinfeld-centre, derived-AG) appears here and reappears at Section XI with different rhetoric. One canonical statement, not two.

**Section VI "The slab, the Drinfeld double, and the BBL triangle"** — Introduces the Drinfeld double programme as the "deepest open programme." This IS the climax question (conj:v1-drinfeld-center-equals-bulk). Clean.

**Section VII "The 3d Maurer–Cartan element"** — Six-face decomposition table of α_T. Architecturally sound: closed/mixed/open MC hierarchy. The Heisenberg / Kac-Moody / Virasoro cascade through classes G/L/M mirrors the CG unique-survivor sequencing.

**Section VIII "PVA descent"** — Good content, but: FM148 flagged "thm:PVA-descent-roadmap universal quantification leaks to class M"; preface's PVA-descent narration treats "every standard family" without restating the log-SC-algebra scope.

**Section IX "Three computations"** — Heisenberg, Kac-Moody, W_3. The paradigmatic cascade. Sound.

**Section X "Curved genus expansion"** — Introduces δF_g^cross cross-channel correction. AP32 (UNIFORM-WEIGHT tag) is properly applied in most formula blocks here.

**Section XI "The eight parts"** — Part-by-part architectural map. Introduces Part VIII "From Frontier to Theorem" which is genuinely new. HOWEVER: this section and Section XII both list the same four items with different status. Section XI says they are theorems in Part VIII; Section XII Item (iii) and Item (v) still list them as "open problems." The reader cannot tell which is true.

**Section XI' "The holographic programme"** — Reprises abelian CS, non-abelian CS, 3d gravity through the H(T) datum. Redundant with Section IX; could be compressed. Symphonic-structure repetition (Gelfand move) is intentional but here it competes with Section XI''' "The programme climax."

**Section XI'' "The E_n hierarchy as physical realisation"** — Another E_n circle exposition. Third or fourth restatement of the same circle. This is where the section count (XI, XI', XI'', XI''') signals authorial uncertainty about the climax structure.

**Section XI''' "The programme climax"** — THIS is the true abstract of the volume. The "three pillars + intersection" architecture (Convergence via Stirling, Rigidity via bounded Zhu + VSKR+BGG refinement, Gauge-theoretic via CG + DW vanishing, Intersection) is the architectural payload. The climax-as-shadow remark (Part VI is the N=2 shadow of W_∞[λ]) is genuinely Platonic. **This section should be Section 0.**

**Section XII "The completeness question and the frontier"** — Overlaps with Section XI and XI'''. Item (iii) and Item (v) are already closed per Section XI. Section XII reads as stale draft.

### Structural verdict

The preface has FOUR climax sections (XI, XI', XI'', XI''') plus a completeness-question postlude (XII). This is the authorial signature of an unresolved Platonic convergence: the volume has a climax, but the climax is *still being found*. The Platonic preface would collapse these four into ONE canonical climax section ("The programme climax via three pillars"), place it immediately after the stage table (Section 0 + stage table + climax = three-move opening), and let Section XII's "five open problems" be downgraded/promoted in line with Section XI's Part VIII claims.

---

## Section 5. Identity tensions (specific passages)

**T1. "This volume discovers these are physics" vs. "seven theorems + eight parts + infinite fingerprint + W_∞ endpoint" (programme synthesis).**
Preface:35-40 frames Vol II as *discovery of physical content* of Vol I's algebraic machinery. Preface:1984-2068 frames it as *programme climax* with three pillars unconditional on the tempered stratum. These are TWO identities: (a) physical interpretation volume (applications of Vol I), (b) programme-synthesis volume (own climax, own theorems F, G, own open problems promoted to Part VIII theorems). A volume can be both, but the abstract must pick ONE lead.

**T2. "A-infinity Chiral Algebras" (title) vs. "3D HT QFT" (title).**
Title binds two nouns. The preface treats "A_infinity chiral algebras" as Vol I content (Stasheff hierarchy from FM_k(C)), and "3D HT QFT" as Vol II content (Costello-Li holomorphic Chern-Simons, Costello-Gaiotto DS). The title suggests equal weight; the preface gives 80% weight to the QFT side. Tension unresolved.

**T3. "Climbs the E_n ladder" vs. "stays at SC^{ch,top} most of the time."**
Preface:62-66 says Virasoro "reached via Sugawara T=[Q,G] at non-critical level" is "the first rung" of E_∞-topological. Preface:230-242 says "SC^{ch,top} is the generic case; E_3-topological is a special case." These two framings are incompatible: either the programme climbs to E_3 (and beyond) as its target, or it organizes the GENERIC SC^{ch,top} case as first-class. The current text does both.

**T4. "Algebra" vs. "Physics" level of rigour.**
Preface:25-40 says algebraic-geometric constructions ARE physics. Preface:1689-1691 "the derived chiral centre of a boundary algebra IS the bulk algebra of a 3d HT gauge theory." These IS-claims require categorical qualifiers: the derived centre is ALGEBRAICALLY EQUIVALENT to Obs^{bulk}(T_A) under specific hypotheses (boundary-linear, non-critical, C_2-cofinite, non-logarithmic). The preface's declarative "IS" repeats AP-CY54 / FM214 pattern: structural conjecture promoted to IS-claim.

**T5. "Programme" identity creep.**
Preface:2127-2142 "The three descriptions agree; they are the same object read from three pillars." This is three-volume synthesis rhetoric. Vol II's job is not to close the three-volume synthesis; that's Vol IV ("Realization") per README. The preface's closing paragraph reverts to Vol II as the middle/physical volume — but Section XI''' already announced the three-volume junction. Tension: the climax section wants three-volume reach; the closing paragraph has two-volume scope.

**T6. "E_∞-topological" climax (XI'') vs. "E_3-topological" climax (XI').**
Preface:1957-1981 says "the climax of the programme is *not* E_3^{top} but E_∞^{top}." Preface:1913 says "E_3 is the target of the volume." Three paragraphs apart, incompatible identification of the climax.

**T7. "Two theorems native" (F, G) vs. "One universal holography" (programme-climax).**
README line 29 and preface:456-478 name TWO native theorems (F, G). Section XI''' (the actual climax) names ONE theorem (programme-climax, Theorem~\ref{thm:programme-climax}) that bundles Universal Holography + Infinite Fingerprint + tempered-stratum convergence. The native count is 2 or 1 depending on which section is read.

---

## Section 6. One-sentence Platonic identity

**Proposed (lossless against current content):**

> "Vol II is the physical realization of Vol I's algebraic engine: the derived chiral centre of a C_2-cofinite non-logarithmic boundary chiral algebra IS, chain-level on weight-completed Banach B_ρ(A), the bulk factorization algebra of a canonical 3d holomorphic-topological gauge theory, with the SC^{ch,top} heptagon, the GRT_1(Q)-faces of r(z), the nine-stage E_n ladder, and the G/L/C/M/FF fingerprint classification as its organizational structure."

**Compare to Vol I's identity (established):** "Vol I is the algebraic engine: bar-cobar for chiral algebras on curves, with the ordered bar B^{ord}(A) as primitive, R-matrix-twisted Σ_n-descent to the symmetric bar, and the five theorems A–D+H as invariants of the coinvariant projection."

**The Vol II identity "lands cleanly" if and only if the abstract:**
1. Opens with the question (when does boundary determine bulk as a 3d HT theory?);
2. Gives the answer (Universal Holography + Infinite Fingerprint on the tempered locus);
3. Names the scope qualifier up front (non-logarithmic C_2-cofinite standard landscape + irrational cosets; logarithmic W(p) conjectural; critical-level KM / Yangian / CY-without-conformal stuck at SC^{ch,top});
4. Positions the climax (Part VI, 3d quantum gravity) as the paradigm instance, not the content;
5. Acknowledges the four Part VIII theorems as programme-closure, not frontier.

The current preface does all five pieces — but across four climax sections (XI, XI', XI'', XI''') rather than in one. The reader has to synthesize. The Platonic preface WOULD synthesize.

---

## Verdict

Vol II is substantively at its Platonic ideal in CONTENT (the executed mathematics: Universal Holography is stated and proved, Infinite Fingerprint is stated and proved, Part VIII theorems are inscribed, the nine-face GRT torsor is in place, the E_∞-topological ladder is constructed). It is NOT at Platonic ideal in PRESENTATION: the preface has four climaxes, the section count signals convergence-in-progress, universal IS-claims leak through despite FM214 heal directives, the README advertises a missing standalone, the climax theorem's scope qualifier is only partially propagated, and the Chriss-Ginzburg table still calls itself "precise" after FM216 flagged it as metaphor.

The gap between content-Platonic and presentation-Platonic is ~2-3 redrafts of sections XI/XI'/XI''/XI''' into a single unified climax, plus a scope-qualifier sweep on the abstract-level "IS" claims in Sections 0 and II. The mathematics is ready; the framing is one convergent-loop short.
