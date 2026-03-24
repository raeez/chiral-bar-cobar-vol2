# Common Mathematical Errors Agents Make

**Repository**: Vol II — A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT
**Derived from**: Deep audit of 200+ commits, 6 adversarial audit sessions, plus full analysis of the uncommitted dirty working state (~38 files of in-flight corrections). Cross-referenced with Vol I error catalogue. **85+ distinct error instances** catalogued (2026-03-16 through 2026-03-24).
**Purpose**: Mandatory pre-flight checklist for any agent session touching this codebase.

---

## Error Class 1: FORMULA ERRORS (13+ instances)

### 1A. Kappa formula confusion — THE #1 RECURRING ERROR (cross-volume)

**What happens**: The modular characteristic kappa is confused with the Sugawara central charge c. One wrong formula propagates across volumes.

**Vol II-specific instances**:
- kappa = k*dim(g)/(2(k+h^v)) used in 12 THQG files instead of the correct kappa = dim(g)*(k+h^v)/(2h^v). Commits: `32dc1e5`, `8df1fcf`, `f79627b`. Blast radius: **19+ files**.
- kappa for sl_2 written as 3k/(k+2) (which is c, the central charge). **Correct**: 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2h^v). Propagated to 7 files.

**Diagnostic**: The wrong affine kappa diverges at k = -h^v; the correct formula vanishes there.

**Prevention rules**:
1. Before writing ANY kappa formula, check Vol I's `landscape_census.tex`.
2. NEVER copy from Vol I without verifying the formula is correct in Vol I first.
3. Use family-qualified notation: kappa^{KM}, kappa^{Vir}, kappa^{W_N}.
4. kappa != c/2 for the affine family (it IS c/2 for Virasoro, which causes the confusion).

### 1B. Virasoro A-infinity operations — completely wrong derivation

**What happened**: The Virasoro associator A_3 and m_3 had wrong coefficients throughout:
- dT coefficient: `2(l-mu)` instead of correct `-(2l+3mu)`
- T coefficient: `4*l*mu` instead of correct `-2mu(2l+mu)`
- Scalar: `(c/6)(l^2*mu+l*mu^2)` instead of correct `-(c/12)*mu^3*(2l+mu)`
- The d^2T term was missing entirely

Commit: `13bf16d`. **Wrong simultaneously in .tex AND .py code.**

**Root cause**: Wrong derivation route (Stasheff equation integration instead of direct m_3 = -A_3 from Borcherds identity). When the formula is wrong in the derivation, the code, and the test all at once, there is no safety net.

**Prevention rule**: For A-infinity operations, always verify by the Borcherds identity route (direct) AND by checking the A-infinity relations (e.g., m_1 m_3 + m_2(m_2 x 1) + m_2(1 x m_2) + m_3 m_1 = 0 at arity 3).

### 1C. Heisenberg r-matrix pole order

**What happened**: Written as k/z (simple pole) instead of k/z^2 (double pole). The Laplace transform maps lambda^n to n!/z^{n+1}, so lambda^1 in {J_lambda J} = k*lambda maps to k/z^2.

Commits: `645af75`, `635fcd6`. Files: preface.tex, introduction.tex.

**Prevention rule**: When converting between lambda-bracket and OPE/rational function, always track the Laplace transform carefully. Lambda^0 -> 1/z, lambda^1 -> 1/z^2, lambda^n -> n!/z^{n+1}.

### 1D. W_3 self-bracket coefficient

32/(5c) instead of 32/(5c+22). The h^v correction (22 = 2*h^v for sl_3) was dropped. Commit: `645af75`.

### 1E. QME factor 1/2

`{S,S}_BV + hbar*Delta*S = 0` missing the 1/2. **Correct**: `(1/2){S,S}_BV + hbar*Delta*S = 0`. Commit: `67bcd3b`. Files: axioms.tex, w-algebras.tex.

### 1E'. betagamma central charge and kappa sign (NEW from dirty state)

**Dirty working state**: c(betagamma) = -2 corrected to c = +2; kappa = -1 corrected to kappa = +1; kappa! = +1 corrected to kappa! = -1. Also c(bc) = -26 corrected to c(bc) = -2.

Files: `hochschild_bulk_bridge.py`, `modular_pva_quantization.py`, `test_modular_pva_quantization.py`.

**Root cause**: Sign error cascaded: wrong c sign -> wrong kappa sign -> wrong dual kappa sign. All three simultaneously wrong, so tests passed.

### 1E''. F_2 genus-2 free energy (NEW from dirty state)

**Dirty working state** in `thqg_perturbative_finiteness.tex`: Old text had TWO contradictory computations of F_2 in a single sentence (3/4 and 7/8). Corrected to single clean computation: (2^3-1)/2^3 = 7/8, giving F_2 = 7*kappa/5760.

### 1E'''. W_3 quartic contact coefficient (NEW from dirty state)

**Dirty working state** in `preface.tex`: 16/(22+5c) corrected to 32/(22+5c) in 3 preface passages. Same error as in Vol I — the WW->Lambda channel is off by factor 2.

### 1E''''. kappa vs kappa_eff labeling (NEW from dirty state)

**Dirty working state** in `main.tex`: `kappa = (6k-26)/2` corrected to `kappa_eff = (6k-26)/2`. The bare kappa for Virasoro is c/2 = 3k. The expression (6k-26)/2 is the effective kappa accounting for the complementary central charge shift.

### 1E'''''. Koszul sign variable (NEW from dirty state)

**Dirty working state** in `fm3_planted_forest_synthesis.tex`: `(-1)^{|x||x'|}` corrected to `(-1)^{|alpha||alpha'|}` in the l_2 bracket. Variables |x| and |x'| were undefined; the correct arguments are alpha, alpha'.

### 1F. sl_2 Sugawara central charge

`c = 6k` stated for sl_2. **Correct**: `c = 3k/(k+2)` (dim=3, h^v=2). Commit: `645af75`.

### 1G. Tree Euler formula for ghost counting

`E = V+k-1` used (incorrect for trivalent trees). **Correct**: `E = (3V-k)/2` from half-edge counting. Commit: `645af75`.

### 1H. Sign errors (3 instances in single audit)

- Spurious (-1)^|a| in raviolo state-field creation property
- Missing (-1)^|a| in arity-2 A-infinity identity
- Wrong sign in BV construction at arity 2

All in commit `645af75`. BV/Koszul sign conventions are the hardest to get right.

**Prevention rule**: For any formula involving signs, expand the simplest nontrivial example and verify term-by-term.

### 1I. Missing lambda in Heisenberg relation

`{J_lambda J} - k` written instead of `{J_lambda J} - k*lambda`. Commit: `645af75`.

### 1J. q=1 at critical level k=-2

"At k=-2: q=1, the quantum group degenerates." But q = e^{i*pi/(k+2)} is **undefined** (division by zero) at k=-2. Commit: `645af75`.

---

## Error Class 2: THE KOSZUL/NON-KOSZUL FALSE DICHOTOMY — #1 by file count

**What happened**: Virasoro and W_N were repeatedly described as "non-Koszul" or "not chirally Koszul" throughout Vol II. This is **wrong**. They ARE chirally Koszul (PBW spectral sequence concentrates). What they have is non-formal Swiss-cheese structure (m_k^SC != 0 for k >= 3).

**Blast radius**: **20+ files** — easily the most pervasive single error in Vol II. Required systematic manuscript-wide rewrite in commits `e704063` + `8df1fcf`.

**Files affected**: preface, introduction, foundations, bar-cobar-review, spectral-braiding (core + frontier), examples-complete, examples-worked, w-algebras-stable, rosetta_stone, ht_physical_origins, ht_bulk_boundary_line_frontier, celestial_holography_frontier, conclusion, log_ht_monodromy (core + frontier), modular_pva_quantization_frontier, pva-descent-repaired, and more.

**Root cause**: Conflating Swiss-cheese formality (m_k = 0 on cohomology) with chiral Koszulness (PBW concentration). The Virasoro has non-formal Swiss-cheese structure but IS chirally Koszul. The false narrative grew across multiple additions, appearing in 4+ new remarks that all propagated the same error.

**Prevention rules**:
1. Shadow depth classifies COMPLEXITY of Koszul algebras, not Koszulness itself.
2. Both finite (Heis@2, aff@3, betagamma@4) and infinite (Vir@infinity) shadow depth algebras are Koszul.
3. Never write "non-Koszul" for the Virasoro or any W-algebra. The correct statement is "non-formal Swiss-cheese structure" or "infinite shadow depth."
4. Before claiming non-Koszulness, check Vol I's prop:pbw-universality: freely strongly generated vertex algebras ARE chirally Koszul.

---

## Error Class 3: STATUS INFLATION (4+ instances)

### 3A. ProvedHere on conditional results

- Virasoro m_7 truncation tagged ProvedHere but depends on analytic hypotheses (H1)-(H4). Commit: `208ffe3`.
- Steinberg convolution tagged ProvedHere but awaits categorical CG projectors. Downgraded to Conditional. Commit: `3d342dc`.
- Gap-Steinberg geometric translation tagged ProvedHere but is suggestive, not formal. Downgraded to Heuristic. Commit: `5b20f9a`.

### 3B. "Proof" instead of "Evidence"

Steinberg modular sewing at genus > 0 presented with `\begin{proof}` but the fiber product construction is not fully rigorous. Changed to `\begin{proof}[Evidence]`. Commit: `5b20f9a`.

**Additional instances from dirty working state**:
- `3d_gravity.tex`: Two results (prop:gravity-koszul-dual, prop:gravity-ybe) changed ProvedHere -> ProvedElsewhere. These are Vol I results; Vol II was claiming credit.
- `spectral-braiding.tex`: "Theorem" -> "Conjecture" for bar-Kontsevich identification (contingent on MC3 extension beyond type A).
- MC3 in `thqg_gravitational_yangian.tex`: K_0-level proved for all types conflated with categorical lift (only proved for type A). B_n folding explicitly marked Conjectured. New conj:mc3-type-B2 added as test case.
- `preface.tex`: YM boundary theory and anomaly-completed KD: Theorem references changed to Section references with "conditional" qualifier.

**Prevention rules**:
1. If a result depends on standing analytic hypotheses, tag it Conditional, not ProvedHere.
2. If the argument is suggestive but not rigorous, use `\begin{proof}[Evidence]` or tag Heuristic.
3. Distinguish "modulo standing hypotheses" from "unconditionally proved."
4. Vol II must not tag ProvedHere for results proved in Vol I. Use ProvedElsewhere.
5. K_0-level character identities != categorical lift. Specify which.

---

## Error Class 4: OBJECT CONFLATION (5+ instances)

### 4A. A^! = Omega(B(A)) — WRONG

A^! is the Koszul dual: A^! = H*(B(A))^v (Verdier dual of bar cohomology).
Omega(B(A)) is bar-cobar inversion: it recovers A itself (Theorem B).
These are DIFFERENT operations with DIFFERENT outputs.

Commit: `1d8a5f5` (line-operators.tex).

### 4B. Tor conflation

Tor^A(k,k) (bar cohomology) confused with Tor^{O(M)}(O(L),O(L)) (derived self-intersection). Commit: `786505a`.

### 4C. Steinberg fiber product

FM_k(C) x Conf_k(R) (bare product) confused with L x_M^h L (derived Lagrangian self-intersection). Commit: `d7665ab`.

### 4D. HH_ch(A!) vs HH(A!)

A^! is an E_1-algebra, so its Hochschild cohomology is ordinary HH^*(A!), NOT the chiral variant HH_ch^*(A!). Commit: `645af75`.

### 4E. Swiss-cheese directionality

Bulk restricts to boundary (correct), NOT boundary restricts to bulk. Commit: `645af75`.

### 4F. MC target algebra

alpha_T lives in g^{SC}_T (two-coloured Swiss-cheese convolution algebra), NOT in Hom(B^ch(A), End_A). Commits: `573b417`, `a3c3ec9`.

### 4G. Bar complex is COALGEBRA, not algebra (NEW from dirty state)

**Dirty working state** in `preface.tex`: "The bar complex (B^ch(A), D_A, Delta) is an **algebra** over SC^{ch,top}" corrected to "**coalgebra** over SC^{ch,top}." The algebra structure lives on the Koszul dual A^!, not on B(A). Same correction in the fourteen theorems list: "(A') Swiss-cheese identification" changed from "SC-algebra" to "SC-coalgebra."

**Root cause**: Fundamental category error — bar produces coalgebras, Koszul dual A^! gets the algebra structure via operadic self-duality.

### 4H. Yangian two-layer structure denied (NEW from dirty state)

**Dirty working state** in `introduction.tex`: Old text claimed the Koszul dual enrichment "is not a second layer of structure." **Corrected**: A^! carries TWO layers — the SC-algebra structure from operadic self-duality (algebra half) AND the bialgebra structure from line-operator monoidal structure (coalgebra half). Together they make A^! a dg-shifted Yangian.

### 4I. (H1)-(H4) hypothesis framework retired (NEW from dirty state)

**Dirty working state**: 8+ instances across 3 files (affine_half_space_bv, hochschild, ht_bulk_boundary_line_frontier) replace old "(H1)-(H4)" references with the formal Definition~\ref{def:log-SC-algebra} and Theorem~\ref{thm:physics-bridge}.

**Root cause**: The hypothesis numbering from an earlier draft was never systematically replaced when the formal definition was introduced.

**Prevention rules**:
1. The four fundamental objects (B, Omega B, D_Ran B, A^!) are distinct. Always name which one.
2. When a Koszul dual A^! appears, it lives in a different categorical context (often E_1) than A (chiral). Qualifier prefixes change accordingly.
3. Always specify the full convolution algebra target, not a projection.
4. Bar is a coalgebra functor. The algebra structure on A^! comes from Koszul duality, not from bar.
5. When a definition replaces a hypothesis list, update ALL references to the old hypotheses.

---

## Error Class 5: SCOPE INFLATION (4+ instances)

### 5A. W_3 truncation overclaim

W_3 A-infinity structure claimed to truncate at m_10. **Actually infinite depth** by the wheel diagram argument. Commit: `645af75`, corrected in `37eec11`.

### 5B. One-loop exactness overclaim

"Reduced central charges are one-loop exact" — the LEVEL K_eff is one-loop exact; the central charge c(K_eff), being rational, acquires higher hbar powers. Commit: `645af75`.

### 5C. Shifted Lagrangian vs Lagrangian in shifted stack

"L is (-2)-shifted Lagrangian in M" — the Lagrangian condition is standard; the ambient STACK is shifted. Commit: `5b20f9a`.

### 5D. One-directional implication as equivalence

Koszulness (ii) => (iii) presented as (ii) iff (iii). Commit: `8df1fcf`.

### 5E. Virasoro shadow recursion exact -> approximation (NEW from dirty state)

**Dirty working state** in `thqg_holographic_reconstruction.tex`: The ENTIRE recursion S_{r+1} = -6r/(c(r+1)) S_r requalified as "cubic-source approximation." All S_r for r >= 6 relabeled S_r^{cub} with daggers. This is because the full recursion involves {Sh_j, Sh_k} brackets with j,k >= 4 starting at arity 6.

This is the single most mathematically significant correction in the dirty state — an entire proposition, corollary, and computation were presenting a truncated recursion as exact.

### 5F. Koszul dodecahedron missing qualifiers (NEW from dirty state)

**Dirty working state** in `bar-cobar-review.tex`: K11 (Lagrangian criterion) qualified as "conditional on perfectness and nondegeneracy hypotheses." K12 (Hodge purity) qualified as "forward direction proved; converse open."

**Prevention rules**:
1. Before claiming truncation/termination, check for infinite-depth arguments (wheel diagrams, recursive structures).
2. "X is one-loop exact" — specify which quantity (level, central charge, partition function).
3. Mark the direction of every implication.
4. When a recursion is truncated, call it an "approximation."
5. When restating a meta-theorem from Vol I, check the exact status of each item.

---

## Error Class 6: SELF-DUALITY AMBIGUITY

### 6A. c=26 called "self-dual datum"

c=13 is the self-dual point (Vir_c^! = Vir_{26-c}, so 26-c=c gives c=13). c=26 is the critical string dimension. Commit: `645af75`.

**Prevention rule**: NEVER write "self-dual" for Virasoro unqualified. Always specify: uncurved (c=0), FF-involution (c=13), or complementarity sum (c=26).

---

## Error Class 7: CIRCULAR REASONING / PROOF GAPS (3+ instances)

### 7A. LG Q^2=0 incomplete computation

Q^2(phi) claimed to vanish "by direct computation" but Q^2(phi) = 2*lambda_3*phi*(psi + lambda_3*phi^2) is NOT zero on the nose. Correct argument: Q = {S,-}_BV and Q^2 = {{S,S}/2,-} = 0 by Jacobi. Commit: `1d8a5f5`.

### 7B. [d_BRST, d_bar] = 0 wrong proof

"Because the BRST differential is an inner derivation" — valid for derivations on associative algebras, NOT for coderivations on coalgebras. Commit: `8df1fcf`.

### 7C. (k+h^v) normalization underived

Division by (k+h^v) asserted without derivation in KZ identification proof. Commit: `c00d660`.

**Prevention rules**:
1. "Direct computation" proofs must be carried to completion — not stopped at "the remaining terms cancel."
2. Arguments valid for algebras don't automatically transfer to coalgebras. Check the categorical context.
3. Every division must be justified: what is the origin of the normalization factor?

---

## Error Class 8: STRUCTURAL/LABEL ERRORS (6+ instances)

### 8A. Cross-volume references (55 dangling)

~55 plain `\ref{}` used for Vol I labels, creating "??" in compilation. Commit: `0b659c9`. 18 files affected.

### 8B. Duplicate labels

sec:Ainfty-to-PVA defined in two files. Commit: `645af75`.

### 8C. Stale cross-references

Remark cited `\ref{ex:LG-Ainfty}` which no longer existed. Commit: `30cede3`.

### 8D. Undefined macros / wrong load order

\RHom undefined in preface (loaded before the file that defines it). Double superscript errors. Undefined \cB_\partial. Missing bibliography entries. Commit: `53cb0d6`.

### 8E. Undefined shorthand macros

\bZ used but undefined; should be \mathbb{Z}. Commit: `f79627b`.

### 8F. Typos in definition names

"Instaton" instead of "Instanton" in 3 occurrences. Commit: `645af75`.

### 8G. Systematic \ref* cross-volume breakage — 20+ instances (NEW from dirty state)

**Dirty working state**: The single largest category of changes by instance count. `\ref*{label}` references to Vol I labels throughout 15+ files replaced with descriptive prose. Examples:
- `3d_gravity.tex`: `Theorem~\ref*{thm:virasoro-koszul-dual-early}` -> "the Virasoro Koszul-duality theorem of Volume~I"
- `hochschild.tex`: `Computation~\ref*{comp:kz-from-graph-sum}` -> "the KZ graph-sum computation of Volume~I"
- `foundations.tex`: `Chapter~\ref*{ch:en-koszul-duality}` -> "the E_n-Koszul duality chapter"
- Similar in: anomaly_completed_core, line-operators, ht_bulk_boundary_line_frontier, examples-worked, rosetta_stone, w-algebras-stable, axioms, fm-calculus, raviolo, pva-descent-repaired, preface

**Root cause**: `\ref*` to Vol I labels produce "??" in compilation because Vol II doesn't have access to Vol I's .aux file.

### 8H. Specific broken label names — 8+ instances (NEW from dirty state)

- `ht_physical_origins.tex`: `ch:foundations` -> `sec:foundations`
- `log_ht_monodromy_frontier.tex`: `chap:spectral-braiding-core` -> `sec:spectral_braiding`
- `log_ht_monodromy_frontier.tex`: `conv:five-levels-log-ht` -> prose (label doesn't exist)
- `spectral-braiding-core.tex`: `subsec:YBE-proof` -> `subsec:YBE`; `subsec:line-ops-spectral` -> `subsec:line-ops`
- `modular_pva_quantization_frontier.tex`: hyphens vs underscores in 2 labels
- `pva-descent-repaired.tex`: `prop:commutativity` -> `prop:product-commutative`
- `hochschild.tex`: `thm:complementarity-triangle` -> prose (label changed)

### 8I. Undefined macros — 4 instances (NEW from dirty state)

- `\DS` -> `\mathrm{DS}` (7 occurrences in affine_half_space_bv.tex)
- `\bA` -> `\mathbb{A}` (5 occurrences in ordered_associative_chiral_kd_frontier.tex)
- `\GL_N` / `\SL_N` -> `\mathrm{GL}_N` / `\mathrm{SL}_N` (8 occurrences in modular_pva_quantization_core.tex)
- `\FT` -> `\mathrm{FT}` (1 occurrence in modular_pva_quantization_core.tex)

**Root cause**: Macros defined in Vol I preamble but not Vol II, or never defined at all.

**Prevention rules**:
1. Vol II references to Vol I must use descriptive prose, not \ref* to Vol I labels.
2. After any rename: grep for ALL old labels across both volumes.
3. New macros go in the preamble in load-order-safe position.
4. Never use a macro without verifying it is defined in the local preamble.
5. Use hyphens consistently or underscores consistently in label names — don't mix.

---

## Error Class 9: LEVEL/GENUS CONFUSION

### 9A. D^2=0 scope unspecified

D^2=0 stated without specifying convolution vs ambient level. Commit: `208ffe3`.

### 9B. Chain-level vs cohomological axioms

Sesquilinearity at the chain level (def:sesquilinearity) is distinct from the PVA definition on cohomology (def:PVA). Citing the wrong one creates proof gaps. Commit: `00a2159`.

**Prevention rule**: ALWAYS specify: chain-level or cohomological? Convolution or ambient? Genus 0 or higher?

---

## Vol II-Specific Patterns (beyond shared Vol I patterns)

1. **The Koszul/non-Koszul conflation is Vol II's worst error by file count.** Vol I has the kappa formula disaster (47 files); Vol II has the non-Koszul narrative (20+ files). Both are copy-paste propagation of a conceptual error.

2. **Sign errors cluster in the BV/Swiss-cheese chapters.** Three sign errors found in a single audit commit (645af75). BV sign conventions are the hardest to get right.

3. **The Virasoro m_3 was wrong in tex + code + test simultaneously.** When the error is in the derivation, there is no automated safety net. Independent cross-checks (e.g., A-infinity relations) are essential.

4. **Vol II imports Vol I errors.** The kappa formula, the Verdier/cobar conflation, and the self-duality ambiguity all originated in Vol I and were imported. Vol II agents must verify formulas against Vol I's corrected source, not against Vol II's historical text.

5. **"Evidence" vs "Proof"** is a Vol II-specific concern because Vol II has more physics-facing content where rigorous proofs are sometimes replaced by physics arguments. Use `\begin{proof}[Evidence]` for suggestive arguments.

---

## Error Class 10: CATEGORICAL CONFLATION — OPERATIONS vs CO-OPERATIONS (2026-03-23/24 thread)

This error class captures the deepest conceptual errors from a sustained multi-session adversarial audit of the dg-shifted Yangian identification.

### 10A. "SC^{ch,top}-algebra = dg-shifted Yangian" — THE FALSE RECOGNITION THEOREM

**What happened**: A "Recognition Theorem" was written claiming that an SC^{ch,top}-algebra concentrated on a single object IS a dg-shifted Yangian, and conversely. This was propagated through 20+ files across the manuscript.

**Why it's wrong**: An operad gives OPERATIONS (maps Y^⊗k → Y). A Yangian requires CO-OPERATIONS (coproduct Δ: Y → Y⊗Y) and a UNIVERSAL ELEMENT (R-matrix r(z) ∈ Y⊗̂Y). These are categorically different objects. No operad algebra axiom system produces co-operations. Out of the four pieces of Yangian structure (τ, r, Δ, ε), only the translation τ comes directly from the SC^{ch,top}-algebra axioms.

**The correct decomposition**:
- **Algebra half** (from SC^{ch,top} self-duality): product, λ-bracket, translation, compatibility. These are operations on A^!.
- **Bialgebra half** (from line-operator module tensor product): coproduct Δ_z, counit ε, R-matrix r(z). These come from the monoidal structure on C_line ≃ A^!-mod.
- **Yangian axioms** = compatibility of these two halves, controlled by the MC equation.

**Root cause**: Failure to check each direction of a claimed equivalence. The forward direction (SC-algebra → coproduct) fails immediately: an operad gives operations, not co-operations. This should have been caught in 30 seconds by asking "can I get Δ: Y → Y⊗Y from the operad?" The answer is no — operads have operations with one output.

**Prevention rules**:
1. When claiming "X = Y," check BOTH directions: can every piece of Y-data be obtained from X-data? Can every piece of X-data be obtained from Y-data? If the answer is "no" for even one piece, the equivalence is false.
2. **Operads give operations (many inputs, one output). Co-operations (one input, many outputs) require additional structure.** Never claim an operad-algebra structure determines a bialgebra structure.
3. **An element r ∈ Y⊗Y is NOT the same as a bilinear map Y⊗Y → Y.** The arity-2 closed-color operation gives a map; converting it to an element requires a pairing (Casimir construction), which is additional data.

**Blast radius**: 20+ files. This was the largest single conceptual error in this thread.

### 10B. "Coproduct is dual of shuffle product" — FALSE ALGEBRAIC CLAIM

**What happened**: After dismissing the false Recognition Theorem, a "decomposition" was proposed attributing the Yangian coproduct to the dual of the shuffle product on the cofree coalgebra T^c(V).

**Why it's wrong**: Direct computation in the Heisenberg case shows the shuffle-dual coproduct has binomial coefficients (n choose p), while the Yangian coproduct (T-matrix presentation, Δ(T(u)) = T(u) ⊗ T(u)) has all coefficients equal to 1. The two disagree at degree 2.

**Root cause**: Failure to compute a SINGLE EXAMPLE before making a general claim. The Heisenberg case is 5 lines of computation and immediately falsifies the claim.

**Prevention rule**: **Before asserting any algebraic identity, verify it in the simplest nontrivial example.** For Yangian claims, compute in the Heisenberg/abelian case first.

### 10C. "R-matrix is Casimir of Koszul pair" — IMPRECISE TO THE POINT OF BEING FALSE

**What happened**: The R-matrix r(z) ∈ A^! ⊗̂ A^! was attributed to "the Casimir element of the Koszul pair (A, A^!)."

**Why it's wrong**: The arity-2 closed-color structure map gives μ_2: C_*(FM_2(ℂ)) ⊗ (A^!)^⊗2 → A^!. This is a bilinear MAP (operation). The R-matrix r(z) is an ELEMENT of A^! ⊗̂ A^!. Converting a map to an element requires choosing a basis and pairing, which is the Casimir construction. But the Casimir formula written in the manuscript (r(z) = Σ_i ⟨e_i, μ_2([FM_2]; -, -)⟩ ⊗ e^i) was garbled: it pairs μ_2 against a dual basis in a way that doesn't type-check.

**What the R-matrix actually is**: The braiding of the monoidal category C_line (Definition spectral-braiding), computed by configuration integrals over FM_2(ℂ) × E_1(2). It's a module-theoretic datum, not an operadic one.

**Prevention rule**: When describing a mathematical object, state its TYPE (element, map, functor) and verify it matches the formula. An element of Y⊗Y is not a map Y⊗Y → Y.

### 10D. Bar-cobar inversion ≠ Koszul involution — PROOF ERROR

**What happened**: The duality involution theorem ((A^!)^! ≃ A) was "proved" by citing bar-cobar inversion (Ω(B(X)) ≃ X). The proof said: "the bar-cobar composite applied to A^! yields an SC-algebra quasi-isomorphic to the SC-algebra that produced A^!, namely A."

**Why it's wrong**: Bar-cobar inversion gives Ω(B(A^!)) ≃ A^! (recovering A^! from its own bar), NOT ≃ A. The claim (A^!)^! ≃ A is the KOSZUL INVOLUTION, which is a different theorem requiring A^! to ALSO be chirally Koszul.

**The distinction**:
- Bar-cobar inversion: Ω(B(X)) ≃ X for any X (homotopy-Koszul operads). Recovers X from its own bar.
- Koszul involution: (X^!)^! ≃ X for Koszul X. Requires X^! to also be Koszul. Different theorem (LV 7.4.5 vs LV 10.1.13).

**Root cause**: Two different theorems with similar statements were conflated. The proofs of both involve bar-cobar adjunctions, making the conflation easy to miss.

**Prevention rule**: **When citing a theorem, verify the STATEMENT matches your use case, not just the topic area.** Bar-cobar inversion and the Koszul involution both involve bar-cobar adjunctions but have different inputs and outputs.

### 10E. Wrong citation — Livernet (2006) on pre-Lie algebras

**What happened**: The Koszul self-duality of the Swiss-cheese operad was cited as "Livernet (2006), Proposition 5.4." This paper is "A rigidity theorem for pre-Lie algebras" — it's about pre-Lie algebras, not Swiss-cheese.

**Root cause**: The citation was plausible (Livernet has worked on Koszul duality for colored operads) but never verified against the actual paper.

**Correct references**: Loday-Vallette (2012), Chapter 8 (distributive law Koszulity); Vallette (2007), §4.2 (colored operads); the self-duality follows from: E_2 self-dual (GK94), Ass self-dual (GK94), distributive law preserved under Koszul duality (LV12 Ch.8).

**Prevention rule**: **When citing a specific proposition number, verify it exists in the cited paper.** A citation that "sounds right" is not a citation that IS right.

### 10F. "Tannaka reconstruction" — OVERBLOWN TERMINOLOGY

**What happened**: The coproduct on A^! was attributed to "Tannaka reconstruction applied to C_line ≃ A^!-mod."

**Why it's misleading**: Tannaka reconstruction in the technical sense requires a fiber functor and produces a Hopf algebra from a rigid abelian monoidal category. The actual content is elementary: if A^! acts on the tensor product V_L1 ⊗ V_L2 of two modules (via the OPE at separation z), this action determines a coproduct Δ_z on A^!. This is the definition of a bialgebra, not Tannaka reconstruction.

**Prevention rule**: **Use the simplest correct description.** If the content is "giving a bialgebra structure is equivalent to giving a monoidal structure on the module category compatible with the forgetful functor," say that — don't invoke Tannaka.

### 10G. "For any SC^{ch,top}-algebra" — FALSE GENERALITY

**What happened**: The self-duality theorem's "In particular" clause said: "for any SC^{ch,top}-algebra A, the linear dual A^! := Hom(B^{SC}(A), k) is again an SC^{ch,top}-algebra."

**Why it's wrong**: The full linear dual of an infinite-dimensional bar complex is pathological. The Koszul dual A^! = H•(B(A))^∨ is well-behaved only when B(A) has concentrated cohomology (= Koszulness). Without the Koszulness hypothesis, A^! is either infinite-dimensional in each degree or poorly behaved.

**Prevention rule**: **When dualizing, always check finiteness.** The dual of an infinite-dimensional object requires care. State the hypotheses under which the dual is well-behaved.

## Error Class 11: FAILURE TO PROPAGATE CORRECTIONS (systemic)

### 11A. Corrected theorem, uncorrected references — THE CONTRADICTION FACTORY

**What happened**: The core theorems were corrected (SC-algebra ≠ Yangian, coproduct from module tensor product, etc.) but dozens of REMARKS, EXAMPLES, CONNECTING PASSAGES, SUBSUBSECTION TITLES, and the PREFACE still used the old language. This created internal contradictions within the manuscript.

**Specific instances found**:
- Subsubsection title still said "Recognition: the Yangian axioms as operadic identities" while the theorem inside correctly distinguished algebra and bialgebra halves.
- Introduction said "the Yangian axioms ARE the operadic identities, decomposed by color" while the theorem said the coproduct comes from the module category.
- Line-operators remark said "the Yangian axioms are consequences of the same operadic structure, not additional input" while the theorem said the coproduct IS additional (module-theoretic) input.
- Factorization bridge opening said "axioms are the SC-operadic identities" and "a dg-shifted Yangian (i.e. an SC-algebra)" — equating them.
- Bar-cobar-review said "by operadic self-duality...A^! is a dg-shifted Yangian" without mentioning the bialgebra half.
- Main.tex abstract said "the Yang-Baxter equation — the operadic identity at FM_3 × E_1(3)" — the YBE involves the coproduct, which is not operadic.

**Root cause**: Corrections were made to the THEOREM but not propagated to every passage that REFERENCES the theorem. The blast radius of a conceptual correction in a 759-page monograph is enormous.

**Prevention rules**:
1. After correcting ANY theorem, grep the ENTIRE manuscript for every reference to that theorem's label AND every passage that describes the theorem's content in prose.
2. Also grep for the OLD language that was corrected — it will appear in passages that don't reference the theorem label but describe the same content.
3. Titles, subsubsection headers, and opening paragraphs are especially dangerous — they're written early and rarely updated.
4. The abstract is the last thing to update and the first thing a reader sees. Always update the abstract LAST after all corrections are propagated.

### 11B. Bulk replacement without proof verification

**What happened**: "Assume (H1)-(H4)" was replaced with "Let A be a logarithmic SC^{ch,top}-algebra" across ~30 files via bulk replacement, without verifying that each individual PROOF still works with the new hypothesis.

**Risk**: Some proofs may use specific properties of (H1)-(H4) (e.g., "the propagator has a simple pole") that don't follow directly from the logarithmic SC-algebra definition. The theorem STATEMENTS are correct, but some PROOFS may have gaps.

**Prevention rule**: After a bulk hypothesis replacement, read the PROOF of each affected theorem (not just the statement) and verify each step works with the new hypothesis. Flag any step that uses a specific property not obviously implied by the new hypothesis.

## Statistical Summary

| Error Class | Committed | Dirty State | Key Blast Radius |
|---|---|---|---|
| Formula errors (kappa, signs, m_3) | 13 | 6+ new | 19 files (kappa) |
| Koszul/non-Koszul false dichotomy | 1 systemic | — | 20+ files |
| W_3 coefficient (16->32) | — | 3 instances | 1 file (preface) |
| betagamma c/kappa sign | — | 3 files | code + tests |
| Status inflation/downgrades | 4 | 6+ new | 8+ files |
| Object conflation | 6 | 3 new (bar coalg, Yangian, H1-H4) | 10+ files |
| Scope inflation | 4 | 2 new (recursion, dodecahedron) | 5+ files |
| Cross-volume \ref* breakage | — | 20+ instances | 15 files |
| Broken label names | — | 8+ instances | 8 files |
| Undefined macros | — | 4 macros | 4 files |
| Self-duality ambiguity | 1 | — | 1 file |
| Circular reasoning / gaps | 3 | — | 3 files |
| Structural/label errors (committed) | 6 | — | 25+ files |
| Level/genus confusion | 2 | — | 3 files |
| Categorical conflation (ops vs co-ops) | — | 7 new | 20+ files |
| Failure to propagate corrections | — | 2 systemic | 10+ files |
| **TOTAL** | **40+** | **60+** | **~48 dirty files** |

**Combined total**: 100+ distinct error instances catalogued across committed history and dirty working state.

---

## The Golden Rules (cross-volume, distilled from 215+ errors across both volumes)

1. **Never copy a formula between families without recomputing from first principles.** (AP1 — kappa disaster in both volumes)
2. **After every correction, grep both volumes for all variant forms.** (AP5 — every correction propagates)
3. **ProvedHere is a LaTeX macro, not a proof.** Verify the proof text. (AP4 — 8+ downgrades in dirty state)
4. **Specify the level**: convolution vs ambient, genus-0 vs genus-1, strict vs homotopy, chain vs cohomological. (AP6)
5. **Cross-family consistency checks are the real tests**, not hardcoded expected values. (AP10)
6. **The four fundamental objects (B, Omega B, D_Ran B, A^!) are distinct.** Name which one. (16+ files in Vol I)
7. **Bar is a coalgebra functor.** The bar complex is a coalgebra, not an algebra. A^! gets the algebra structure. (dirty state preface fix)
8. **A truncated recursion is an approximation, not a formula.** State which terms are included. (shadow recursion)
9. **A physics analogy is not a theorem.** Label it accordingly.
10. **Universal claims need universal proofs.** If proved in type A, say "type A." (AP7 — MC3, orbit duality)
11. **kappa + kappa' = 0 is NOT universal.** It is family-dependent. (25+ instances in Vol I dirty state)
12. **Shadow depth != Koszulness.** Never call Virasoro or W-algebras "non-Koszul." (20+ files in Vol II)
13. **Vol II imports Vol I errors.** Verify formulas against Vol I's corrected source, not Vol II's historical text.
14. **Sign conventions in BV/Swiss-cheese require term-by-term verification** on the simplest nontrivial example.
15. **Vol II must not use \ref* to Vol I labels.** Use descriptive prose references instead. (20+ dirty instances)
16. **Vol II must not tag ProvedHere for Vol I results.** Use ProvedElsewhere.
17. **After any rename, grep everything.** The blast radius is always larger than you think. (8+ broken labels in dirty state)
18. **Your correction might also be wrong.** Mark uncertain corrections with RECTIFICATION-FLAG.

---

## Vol II-Specific Error Patterns from 2026-03-24 Comprehensive Audit

### NEW: betagamma/bc sign confusion (4 tex + 2 compute files in Vol II)

**Files fixed in Vol II**:
- `thqg_symplectic_polarization.tex:1853` — kappa(bg)=-1 → parametric formula
- `thqg_gravitational_complexity.tex:870` — kappa(bg)=-1 → kappa=0 on weight-changing line
- `line-operators.tex:927,930` — kappa(bg)=-2 → +1
- `thqg_holographic_reconstruction.tex:1857` — spurious /2 in kappa formula
- `compute/lib/hochschild_bulk_bridge.py` — c=-2,kappa=-1 → c=+2,kappa=+1
- `compute/lib/modular_pva_quantization.py` — same

### NEW: Virasoro kappa(Vir_13)=0 errors (4 files in Vol II)

**Files fixed**:
- `thqg_anomaly_extensions.tex:957,984,1209` — kappa(Vir_26)=0 and kappa(Vir_13)=0 (should be 13 and 13/2)
- `anomaly_completed_topological_holography.tex:2259` — kappa(Vir_13)=0
- `twisted_holography_quantum_gravity.tex:993,2022` — kappa(Vir_13)=0
- `thqg_spectral_braiding_extensions.tex:1240` — kappa+kappa'=0 (should be 13)

**Note**: The CORRECT values exist in Vol II at `anomaly_completed_frontier.tex:493-500` and `3d_gravity.tex:188-191`. The error propagated from a Vol I source file into these Vol II THQG chapters.

### NEW: Koszulness conditionality dropped in Vol II bar-cobar-review

The "Koszul dodecahedron" (bar-cobar-review.tex:774-855) stated all 12 conditions as unconditionally equivalent. Fixed: added conditionality note after items (xi) Lagrangian and (xii) Hodge purity.

### NEW: κ(Vir_c)=c (missing /2) in thqg_bv_ht_extensions.tex:1390

A single factor-of-2 error. kappa(Vir_c) = c/2, not c.

### NEW: κ_eff missing subscript in Vol II abstract (main.tex:502)

κ = (6k-26)/2 is the effective kappa after ghost subtraction, not the intrinsic kappa. Added subscript.

### Vol II Prevention Addendum

19. **betagamma has positive c at standard weights.** c(bg,lambda=1)=+2. If you see c(bg)=-2, you have bc.
20. **kappa(Vir_13) = 13/2, NOT 0.** Self-duality does NOT imply vanishing curvature for W-algebras.
21. **F_1(Vir) = c/48, NOT c/24.** The physical anomaly c/24 and the shadow F_1 = kappa/24 = c/48 differ.
22. **kappa and kappa_eff differ by the ghost contribution.** Always specify which one.
23. **Operads give operations (many→one). Co-operations (one→many) are NOT operadic.** Never claim an operad-algebra structure determines a bialgebra. The coproduct on A^! comes from the module tensor product, not from the SC-algebra.
24. **An element of Y⊗Y is NOT a bilinear map Y⊗Y → Y.** Before attributing an element to an operation, check the types match.
25. **Bar-cobar inversion (Ω(B(X))≃X) ≠ Koszul involution ((X^!)^!≃X).** The first recovers X from its own bar. The second requires X^! to also be Koszul. Different theorems.
26. **Before asserting any algebraic identity, verify it in the simplest nontrivial example.** For Yangian claims, compute in the Heisenberg case first.
27. **When citing a proposition number, verify it exists in the cited paper.** A plausible citation is not a correct citation.
28. **After correcting a theorem, grep the ENTIRE manuscript for the OLD language.** Titles, subheaders, opening paragraphs, and the abstract are the most dangerous — written early, rarely updated, first thing readers see.
29. **When claiming X = Y, check both directions separately.** Can every piece of Y-data be obtained from X? Can every piece of X-data be obtained from Y? If "no" for even one piece, the equivalence is false.
30. **When dualizing, always check finiteness.** The dual of an infinite-dimensional object requires Koszulness or other concentration hypotheses.

---

## Deep Beilinson Audit (2026-03-24): New Patterns

7 agents, ~53K lines, 51 files. 20+ fixes. Critical findings:

31. **Virasoro IS chirally Koszul.** Shadow depth ∞ = non-formal ≠ non-Koszul. Fixed in rosetta_stone.tex (×2) and examples-worked.tex (×1).
32. **κ(Vir_26) = 13, NOT 0.** The effective κ_eff = 0, but intrinsic κ = c/2 = 13. Fixed in 4 files.
33. **WW Lambda OPE coefficient is 32/(22+5c).** The ∂Lambda coefficient is 16/(22+5c). Never confuse them. Fixed in 8 Vol II locations.
34. **Cross-volume claims drift.** Verify every Vol II restatement against actual Vol I source. Found 8 cross-volume discrepancies.
35. **Superseded files cause 1018 duplicate labels.** Stripped labels from 42 superseded files. Always verify a file is actively \input'd before editing.
36. **F₁(Vir) = c/48, not c/24.** F₁ = κ/24 and κ(Vir) = c/2, so F₁ = c/48. Fixed in Vol II thqg_spectral_braiding_extensions.tex.

**Total Vol II instances this session**: 20+ fixes applied. Structural crisis (1018 duplicate labels) fully resolved.
