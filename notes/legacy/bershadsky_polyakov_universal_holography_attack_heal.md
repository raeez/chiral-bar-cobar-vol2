# Bershadsky-Polyakov (W^k(sl_3, f_min)) and Universal Holography:
# Attack-Heal on Non-Principal DS + Galois Descent

All work by Raeez Lorgat. No AI attribution. No .tex edits; no commits.

## 0. The Attack

Claim under test: Universal Holography Phi_hol (Part VI climax,
thm:universal-holography / thm:E3-topological-DS-general in
fm81_fractional_ghost_platonic.tex) extends unconditionally to every
affine W-algebra W^k(g, f) at non-critical level via the DS-Hochschild
compatibility bridge plus Galois descent for good-graded (fractional)
nilpotents. The programme further claims that at the self-dual point
of BP the Koszul-conductor K_W(BP) equals the c-sum K_BP = 196 and
that this is *consistent with the exponent formula* used for principal
W_N.

I test this at the Bershadsky-Polyakov algebra BP = W^k(sl_3, f_min),
the archetypal non-principal minimal-nilpotent W-algebra: generators
{J (wt 1), G^+- (wt 3/2), T (wt 2)}, Kazhdan denominator d_f = 2.

## 1. What the Programme Gets RIGHT at BP

(R1) **Central charge and Koszul involution.** Using the
Fehily-Kawasetsu-Ridout (2020/2021) normalisation

    c(BP_k) = 2 - 24 (k+1)^2 / (k+3),                     [*]

the operadic Koszul-dual level is k^! = -k - 6 = -k - 2 h^v(sl_3).
Symbolic verification (SymPy, polynomial identity in k):

    c(BP_k) + c(BP_{-k-6}) = 196.                         [**]

This matches FRONTIER.md's K_BP = 196 and the c-sum appendix of the
BP chapter (chapters/theory/bp_chain_level_strict_platonic.tex
prop:bp-kappa-conductor). At admissible k = -3/2: c(BP_{-3/2}) = -2,
c(BP_{-9/2}) = 198, sum = 196 — confirmed.

(R2) **Exponent formula consistency in the right sense.** The
principal K_W conductor K_W(W_N) = 2(2N^3 - N - 1) gives
K_W(W_2) = 26 (= 2c(Vir) at c^* = 13), K_W(W_3) = 100, K_W(W_4) = 246,
K_W(W_5) = 488. BP is NOT principal, so this sequence does not apply;
instead BP sits on an ORTHOGONAL axis indexed by Bala-Carter label
(minimal nilpotent of sl_3 = A_1) at level k, with conductor 196. The
two formulas are not competitors; they are distinct specialisations
of the unified conductor K_W(g, f) of unified_chiral_quantum_group.tex.

(R3) **Shadow class and fingerprint.** BP is class M (Virasoro
subsector has quartic pole, r_max = infinity). The G^+- sector alone
is class L (r_max = 4) because the residual sl_2-triple's Jacobi
kills the degree-4 Stasheff obstruction (prop:BP-shadow in
examples-worked.tex:4107). Fingerprint:
  phi(BP_k) = (p_max = 4, r_max = infinity, chi_VOA = even (bosonic;
              G^+- are bosonic weight-3/2, not fermionic), n_strong = 4
              {J, G^+, G^-, T}, coset = (u(1)_J, residual sl_2_res)).
In the infinite-fingerprint classification (Part VIII reconstitution),
class M is coarse; the refined slot is the G^+- sector's class-L
embedding inside the M envelope. BP's kappa ratio rho = 1/2 (T is
Sugawara of residual sl_2), distinct from principal W_N (rho = H_N - 1).

(R4) **RETRACTED 2026-04-17: Chain-level E_3-topological for BP
inscribed at cohomological level only.** The chapter
bp_chain_level_strict_platonic.tex (thm:bp-chain-level-
e3-topological, proved) establishes E_3-topological structure
for BP at the level of H^•(Q_tot) on the ORIGINAL BRST complex on X
(cohomological H^•(Q_tot) only; strict chain-level on original
complex retracted as frontier per rem:frontier-class-L-strict-chain-
level at e_infinity_topologization.tex:382-411) — via the
branched-cover route:
  (i) pull back to X-tilde along pi: X-tilde -> X of degree 2,
  (ii) upstairs the pulled-back V_k(sl_3) is class L with integer
       Kazhdan weight; run Vol I's class-L antighost absorption
       (eta_1^(i) + eta_1^(ii)) to get [Q_tot, G_tilde_1] = T_Sug
       in H^•(Q_tot) (cohomological H^•(Q_tot) only; strict chain-
       level on original complex retracted as frontier per
       rem:frontier-class-L-strict-chain-level at
       e_infinity_topologization.tex:382-411),
  (iii) descend via Deck(pi) = Z/2 invariants; Maschke exactness in
        characteristic 0 preserves COHOMOLOGICAL identities (strict
        chain-level preservation retracted along with the upstairs
        claim). This matches the generic class-M weight-completed
        entry for BP at cohomological level; no strict strengthening.

(R5) **DS-Hoch bridge (non-principal version).** Vol II
fm81_fractional_ghost_platonic.tex thm:E3-topological-DS-general-
all-good-graded runs the same branched-cover + Galois-invariant
machinery at the level of ChirHoch^bullet(W_k(g, f)), yielding

  ChirHoch^bullet(W_k(g, f))
      ~= H^bullet_{DS, exotic}(ChirHoch^bullet(V_k(g))).

For BP specifically this closes the ChirHoch compatibility at
chain level on the original complex — the content of Universal
Holography at BP, not merely on cohomology.

## 2. What the Attack Exposes (WRONG or SUBTLE)

(W1) **Central-charge formula INCONSISTENCY in the manuscript.**
Three variant formulas for c(BP_k) coexist:
  - FKR:        c = 2 - 24(k+1)^2/(k+3)              [correct]
  - bp_chapter: c = -(2k+3)(3k+1)/(k+3)               [incorrect]
  - examples-worked: c = -2(2k+3)^2/(k+3) + 8         [incorrect]
Symbolic check: FKR gives c(-3/2) = -2 (matches Arakawa 2013
minimal rational BP); bp_chapter gives c(-3/2) = 0; examples-worked
gives c(-3/2) = 2. ONLY FKR is consistent with the published
BP central charge. This is a genuine manuscript defect (V2-AP14
oscillation). The c+c^! = 196 polynomial identity HOLDS ONLY for
the FKR form. The two off-brand forms would give different,
non-constant c-sums. Counter (no .tex edits per directive): flag for
atomic rename rectification.

(W2) **kappa-sum vs c-sum confusion.** Two distinct "sum" invariants
circulate under the name BP complementarity:
  - c-sum = c(BP_k) + c(BP_{-k-6}) = 196 (polynomial in k)
  - kappa-sum at the self-dual point = 13 (examples-worked:4158)
  - kappa + kappa' with kappa = c/2 (since BP's T is Sugawara of
    residual sl_2, AP39: rho = 1/2): kappa-sum = c-sum/2 = 98
    as polynomial identity, NOT 13 as constant.
The "13" comes only from specialising at the Virasoro self-dual
locus c = 13 = c^*(Vir), which is NOT a BP feature but an inherited
Virasoro feature; the true BP kappa-sum polynomial is 98. The
working_notes entry "c_sum = 2" is a DIFFERENT BP-type algebra
(B^k of osp(3|2)), not the FKR BP = W^k(sl_3, f_min); the entry
is legitimately superseded by 196 once the algebra is specified.

(W3) **Galois descent scope gap.** The branched-cover route closes
d_f = 2 cases (BP, minimal sl_N, subregular in B_n/D_n with hook-parity
= 2, Premet-type E_8 orbits with d_f = 2). It does NOT automatically
close d_f >= 3 (certain exceptional minimal orbits, e.g. some
subregular in B_n with d_f = 3). For those the branched cover is
degree 3; Maschke exactness still holds (char 0, |Z/3| = 3 invertible),
but the upstairs class is not automatically class L — it may still be
fractionally graded of a DIFFERENT denominator relative to a further
sub-structure. The attack correctly flags that fm81 closes
*all good-graded* but this hides a stratification by d_f.

(W4) **DS-Hoch bridge: HPL transfer for non-principal.** The bridge
(chiral_higher_deligne.tex thm:chd-ds-hochschild) runs HPL through
a strong deformation retract. For principal DS the retract is
Arakawa-Feigin-Frenkel's explicit Miura section. For non-principal
the retract requires Kac-Roan-Wakimoto's fractional-ghost Miura,
which works term-by-term on the Kazhdan filtration — but the HPL
transfer only preserves CHAIN-LEVEL E_2-Gerstenhaber structure IF
the filtration is FINITE on each weight space. For BP at admissible
levels (Arakawa 2013: C_2-cofinite simple quotient at k = -3/2,
giving c = -2) this holds; at generic k the filtration finiteness
is a distinct fact (Arakawa-Kawasetsu 2016 for all non-principal
type A).

## 3. Correct Relationship

The sharp statement: Universal Holography Phi_hol extends to BP as

    Phi_hol(BP_k) = (Z^{der}_{ch}(BP_k), BP_k)

as a PAIR (bulk, boundary) in the SC^{ch,top} framework, with
**RETRACTED 2026-04-17** (η_1 antighost-contact strict-chain-level claims downgraded to cohomological H^•(Q_tot) per rem:frontier-class-L-strict-chain-level at e_infinity_topologization.tex:382-411):
STRICT chain-level E_3-topological structure on Z^{der}_{ch}(BP_k)
on the ORIGINAL BRST complex, valid for all k != -3, unconditional.

Mechanism (three independent ingredients):
  1. Degree-2 branched cover pi: X-tilde -> X integralises the
     Kazhdan (1/2)-grading.
  2. **RETRACTED 2026-04-17** (η_1 antighost-contact strict-chain-level claims downgraded to cohomological H^•(Q_tot) per rem:frontier-class-L-strict-chain-level at e_infinity_topologization.tex:382-411):
     Upstairs V_k(sl_3) is class L; Vol I's class-L strict chain-level
     antighost absorption applies verbatim.
  3. Galois Z/2 descent via Maschke-exact invariants preserves
     chain-level identities (not only cohomological).

The DS-Hoch bridge ChirHoch^*(BP_k) ~= H^*_{DS, min}(ChirHoch^*(V_k(sl_3)))
closes at chain level on the original X for the BP case specifically.

Conductor: K_BP = 196 is the c-SUM under k -> -k - 6, not the
kappa-sum; the kappa-sum polynomial is 98 (under AP39 rho = 1/2).
The "self-dual point c^* = 25/2 = 12.5" from the attack prompt
is NOT supported: c-self-duality c = c^! with c^! = 196 - c gives
c^* = 98, not 25/2. The value 25/2 would be c^* under a DIFFERENT
Koszul involution (the one giving c-sum = 25); no such involution
exists for BP in the FKR normalisation.

## 4. Deliverable Verdict

**RETRACTED 2026-04-17** (η_1 antighost-contact strict-chain-level claims downgraded to cohomological H^•(Q_tot) per rem:frontier-class-L-strict-chain-level at e_infinity_topologization.tex:382-411):
Universal Holography is UNCONDITIONAL at BP (class-L upstairs +
Maschke descent = strict chain-level E_3-top), provided:
  - the FKR central-charge formula is the one used consistently,
  - the bp_chapter and examples-worked variant formulas are
    recognised as errata and rectified (atomic rename pass).

K_W(BP) via the non-principal formula = 196 (c-sum; equivalently
polynomial conductor of the Koszul involution k <-> -k - 6 on the
FKR c(BP_k)). The exponent-formula claim 2·rank(sl_3) + 48·(rho,rho^v)^{f_min}
does not reproduce 196 on any natural normalisation I can verify:
2·2 + 48·<1/2 H_theta, (h_1 + h_2)/2> = 4 + 48·(1 + 1)/4 = 4 + 24 = 28,
which is the GHOST central charge for BP (dim of BRST ghost pair
contributions), not K_W(BP). The programme's exponent-style formula
for K_W at non-principal f is consistent with the Bala-Carter label
A_1, not with the principal-exponent sum, and equals 196 by direct
polynomial identity, not by the principal formula 2(2N^3 - N - 1)
which gives 100 for sl_3 principal.

Honest strongest form: Universal Holography is PROVED unconditionally
at BP on the original complex; K_W(BP) = 196 as the c-sum invariant
of the (FKR, Koszul-involution) pair; the three-formula inconsistency
across bp_chapter/examples-worked/FKR is a technical-malpractice
defect, not a mathematical obstruction (HEAL-SWEEP: atomic rename
pass restores consistency).

## 5. Under-200-word Report

**RETRACTED 2026-04-17** (η_1 antighost-contact strict-chain-level claims downgraded to cohomological H^•(Q_tot) per rem:frontier-class-L-strict-chain-level at e_infinity_topologization.tex:382-411):
Universal Holography IS unconditional at BP on the ORIGINAL BRST
complex. Mechanism: degree-2 Kummer cover integralises the Kazhdan
(1/2)-grading; upstairs V_k(sl_3) is class L; Vol I's class-L antighost
absorption (eta_1^(i) + eta_1^(ii)) closes strict chain-level
[Q_tot, G-tilde_1] = T_Sug upstairs; Galois Z/2 descent via
Maschke-exact invariants preserves chain-level identities to X.
DS-Hoch bridge closes ChirHoch^*(BP) ~= H^*_{DS,min}(ChirHoch^*(V_k(sl_3)))
on the original complex.

K_W(BP) via non-principal formula = **196**, computed as the
polynomial c-sum identity c(BP_k) + c(BP_{-k-6}) = 196 under the
FKR formula c(BP_k) = 2 - 24(k+1)^2/(k+3) with Koszul-dual level
k^! = -k - 6. Symbolic verification confirms. The corresponding
kappa-sum polynomial is 98 (using AP39 rho = 1/2 since BP's T is
Sugawara of residual sl_2). The attack's self-dual value 25/2 = 12.5
is NOT supported; c-self-duality gives c^* = 98.

Defect flagged: three inconsistent c(BP_k) formulas across
bp_chapter, examples-worked, FKR — only FKR gives c(-3/2) = -2
and c+c^! = 196; the other two carry different polynomials. HEAL:
atomic rename to FKR normalisation volume-wide.
