"""Tests for P3 PVA-quantum HT theory: conditional all-loop quantum lift.

Verifies the hypothesis-tracking discipline for Construction Problem 3
(unified PVA-quantum HT theory with classical lambda-Jacobi limit and
E_3-lift on Q_{tot}-cohomology, conditional on hypKZSDR + hypStokes +
hypReflWts + hypTLift; CLAUDE.md sec.9; FRONTIER.md row P3;
programme_climax_platonic.tex thm:construction-problem-stage-stratification).

Three independent route signatures (Khan-Zeng SDR + Stokes; Lurie HA ch.5 +
reflected weights; iterated Sugawara T-lift) must:
  (1) cover all four hypotheses (no hypothesis is orphaned);
  (2) recover the classical lambda-Jacobi PVA at hbar -> 0;
  (3) agree on non-critical-level availability (k + h^v != 0 for affine KM);
  (4) agree on the critical-level failure mechanism.

The conditional theorem 'classical PVA + 4 hyp => quantum E_3-lift' is
well-formed iff the structural invariants hold.

References:
  Vol II chapters/theory/pva-descent.tex
  Vol II chapters/connections/e_infinity_topologization.tex
  Vol II chapters/connections/modular_pva_quantization_core.tex
  Vol II chapters/connections/programme_climax_platonic.tex
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.p3_pva_quantum_lift import (
    HYPOTHESIS_PACKAGE,
    ROUTES,
    hypKZSDR, hypStokes, hypReflWts, hypTLift,
    route_A_khan_zeng, route_B_lurie_reflected, route_C_iterated_sugawara,
    P3_CLAUSE_LEDGER,
    FRAGILITY_REPORT,
    hypothesis_coverage,
    routes_all_classical_limit_lambda_jacobi,
    routes_agree_non_critical_availability,
    routes_agree_critical_level_failure,
    claim_status_summary,
    conditional_theorem_well_formed,
    most_fragile_hypothesis,
    CROSS_VOLUME_ANCHORS,
)


# ===================================================================
# 1. HYPOTHESIS PACKAGE INVARIANTS
# ===================================================================

class TestHypothesisPackage:
    def test_exactly_four_hypotheses(self):
        """The CP3 endpoint hypothesis package has exactly four elements."""
        assert len(HYPOTHESIS_PACKAGE) == 4

    def test_all_hypotheses_delta_type(self):
        """All four hypotheses are licensing-type delta (endpoint / convergence)
        per CLAUDE.md sec.5."""
        for h in HYPOTHESIS_PACKAGE:
            assert h.licensing_type == 'delta', (
                f"{h.tag} must be delta-type endpoint hypothesis"
            )

    def test_hypothesis_tags_canonical(self):
        """Canonical tags must match CLAUDE.md sec.5 + main.tex preamble."""
        tags = {h.tag for h in HYPOTHESIS_PACKAGE}
        assert tags == {'hypKZSDR', 'hypStokes', 'hypReflWts', 'hypTLift'}

    def test_hypothesis_primary_sources_present(self):
        """Every hypothesis carries a primary-source attribution."""
        for h in HYPOTHESIS_PACKAGE:
            assert h.primary_source, f"{h.tag} missing primary source"
            assert len(h.primary_source) > 20, (
                f"{h.tag} primary source too short to be meaningful"
            )


# ===================================================================
# 2. ROUTE COVERAGE (no hypothesis is orphaned)
# ===================================================================

class TestRouteCoverage:
    def test_three_routes(self):
        """Exactly three independent derivation routes."""
        assert len(ROUTES) == 3

    def test_route_names_canonical(self):
        names = {r.name for r in ROUTES}
        expected = {
            'Khan-Zeng SDR + Stokes',
            'Lurie HA ch.5 + reflected weights',
            'Iterated Sugawara T-lift',
        }
        assert names == expected

    def test_route_A_consumes_kz_and_stokes(self):
        consumed = set(route_A_khan_zeng.hypotheses_consumed)
        assert hypKZSDR in consumed
        assert hypStokes in consumed

    def test_route_B_consumes_reflected_weights(self):
        consumed = set(route_B_lurie_reflected.hypotheses_consumed)
        assert hypReflWts in consumed

    def test_route_C_consumes_t_lift(self):
        consumed = set(route_C_iterated_sugawara.hypotheses_consumed)
        assert hypTLift in consumed

    def test_every_hypothesis_consumed_by_some_route(self):
        """No orphan hypothesis: every hyp in the package is consumed."""
        coverage = hypothesis_coverage()
        for tag, routes in coverage.items():
            assert routes, f"hypothesis {tag} is orphaned (no route consumes it)"

    def test_hypothesis_coverage_partition(self):
        """Each hypothesis is consumed by at least one route; in this
        arrangement, exactly one route per hypothesis (modulo route A
        consuming both hypKZSDR and hypStokes)."""
        coverage = hypothesis_coverage()
        assert coverage['hypKZSDR'] == ['Khan-Zeng SDR + Stokes']
        assert coverage['hypStokes'] == ['Khan-Zeng SDR + Stokes']
        assert coverage['hypReflWts'] == ['Lurie HA ch.5 + reflected weights']
        assert coverage['hypTLift'] == ['Iterated Sugawara T-lift']


# ===================================================================
# 3. ROUTE AGREEMENT INVARIANTS
# ===================================================================

class TestRouteAgreement:
    def test_classical_limit_is_lambda_jacobi(self):
        """All three routes recover the classical lambda-Jacobi PVA at
        hbar -> 0. This is the unconditional clauses (i)-(ii) of
        pva-descent.tex thm:cohomology-PVA-main; any conditional lift
        must collapse to it."""
        assert routes_all_classical_limit_lambda_jacobi()

    def test_non_critical_level_agreement(self):
        """At non-critical level k + h^v != 0, all three routes produce
        the E_3-lift on Q_{tot}-cohomology for affine V_k(g).

        Route A: Khan-Zeng SDR regular at non-critical level.
        Route B: Reflected weights well-defined off resonance loci.
        Route C: Sugawara primitive G^{(n)} exists iff (k + h^v) invertible.
        """
        assert routes_agree_non_critical_availability()

    def test_critical_level_failure_agreement(self):
        """At critical level k + h^v = 0, all three routes fail via
        independent mechanisms (SDR divergence; resonance wall;
        Sugawara denominator). The cross-diagnoses are the
        non-tautological cross-check."""
        assert routes_agree_critical_level_failure()


# ===================================================================
# 4. CLAIM-STATUS LEDGER
# ===================================================================

class TestClaimStatus:
    def test_classical_pva_proved_unconditionally(self):
        """The classical lambda-Jacobi PVA descent is ProvedHere with no
        hypothesis. This is pva-descent.tex clauses (i)-(ii)."""
        classical = [cs for cs in P3_CLAUSE_LEDGER
                     if 'Classical lambda-Jacobi' in cs.clause]
        assert len(classical) == 1
        assert classical[0].status == 'ProvedHere'
        assert classical[0].hypotheses_required == ()

    def test_all_loop_quantum_lift_conditional(self):
        """The all-loop quantum lift clause is ConditionalProved on
        all four hypotheses."""
        quantum = [cs for cs in P3_CLAUSE_LEDGER
                   if 'All-loop quantum lift' in cs.clause]
        assert len(quantum) == 1
        assert quantum[0].status == 'ConditionalProved'
        assert set(quantum[0].hypotheses_required) == set(HYPOTHESIS_PACKAGE)

    def test_iterated_sugawara_proved_core(self):
        """T^{(n)} = [Q_{tot}, G^{(n)}] on cohomology is ProvedHere
        (Vol II thm:iterated-sugawara-construction)."""
        sug = [cs for cs in P3_CLAUSE_LEDGER
               if 'Iterated Sugawara' in cs.clause]
        assert len(sug) == 1
        assert sug[0].status == 'ProvedHere'
        assert sug[0].hypotheses_required == ()

    def test_e3_lift_non_critical_proved(self):
        """E_3-lift on Q_{tot}-cohomology for affine KM at non-critical
        level is ProvedHere (Vol II thm:E3-topological-km)."""
        e3 = [cs for cs in P3_CLAUSE_LEDGER
              if 'E_3-lift' in cs.clause and 'non-critical' in cs.clause]
        assert len(e3) == 1
        assert e3[0].status == 'ProvedHere'

    def test_chain_level_t_lift_conditional(self):
        """The chain-level T-lift to the all-loop quantum object is
        ConditionalProved on hypTLift only (the cohomological identity
        is the proved core)."""
        t_lift = [cs for cs in P3_CLAUSE_LEDGER
                  if 'Chain-level T-lift' in cs.clause]
        assert len(t_lift) == 1
        assert t_lift[0].status == 'ConditionalProved'
        assert hypTLift in t_lift[0].hypotheses_required

    def test_status_summary_partition(self):
        """Every clause is exactly one of ProvedHere / ConditionalProved /
        Conjectured. No clause is unclassified."""
        buckets = claim_status_summary()
        all_clauses = sum(len(v) for v in buckets.values())
        assert all_clauses == len(P3_CLAUSE_LEDGER)


# ===================================================================
# 5. CONDITIONAL THEOREM WELL-FORMEDNESS
# ===================================================================

class TestConditionalTheoremWellFormed:
    def test_conditional_theorem_is_well_formed(self):
        """The CP3 conditional theorem
        'classical PVA + 4 hypotheses => quantum E_3-lift'
        passes all four structural checks:
          (a) classical lambda-Jacobi clause is ProvedHere unconditional;
          (b) every conditional clause names at least one hypothesis;
          (c) every hypothesis is consumed by some route;
          (d) the proved core (Sugawara T-identity, E_3-lift at non-critical
              level) is independent of the four hypotheses.
        """
        assert conditional_theorem_well_formed()

    def test_forbidden_slogan_16_resolved(self):
        """CLAUDE.md sec.8 forbidden slogan #16: 'PVA => quantum theory'
        is replaced by 'classical only; quantum conditional on hypKZSDR,
        hypStokes, hypReflWts, hypTLift'. This is enforced by the
        clause ledger: the classical lambda-Jacobi clause is unconditional,
        the all-loop quantum lift clause is ConditionalProved on the
        four hypotheses."""
        # Slogan #16 is structurally enforced: no clause is labeled
        # 'PVA => quantum theory' as ProvedHere without hyp tags.
        for cs in P3_CLAUSE_LEDGER:
            if 'quantum' in cs.clause.lower() and 'lift' in cs.clause.lower():
                if cs.status == 'ProvedHere':
                    assert cs.hypotheses_required == (), (
                        f"clause '{cs.clause}' is ProvedHere; cannot demand hyp"
                    )
                else:
                    assert cs.hypotheses_required, (
                        f"clause '{cs.clause}' is conditional on quantum lift but "
                        f"names no hypothesis. Slogan #16 (PVA => quantum) "
                        f"would re-emerge."
                    )


# ===================================================================
# 6. FRAGILITY / ATTACK-HEAL
# ===================================================================

class TestFragility:
    def test_t_lift_is_most_fragile(self):
        """The chain-level T-lift (hypTLift) is the most fragile of the
        four hypotheses: it is the only one demanding chain-level (not
        cohomological) data, and depends on Mittag-Leffler antighost-
        commutativity at all weight windows simultaneously."""
        assert most_fragile_hypothesis().tag == 'hypTLift'

    def test_fragility_report_covers_all_hypotheses(self):
        """Every hypothesis has a fragility-attack-heal entry."""
        covered = {r.hypothesis.tag for r in FRAGILITY_REPORT}
        package_tags = {h.tag for h in HYPOTHESIS_PACKAGE}
        assert covered == package_tags

    def test_fragility_ranks_total_order(self):
        """The four fragility ranks are 1, 2, 3, 4 (a total order)."""
        ranks = sorted(r.fragility_rank for r in FRAGILITY_REPORT)
        assert ranks == [1, 2, 3, 4]

    def test_every_attack_has_a_heal_path(self):
        """Every attack pairs with a heal path: no fragile hypothesis is
        left without a route to repair / restrict / declare ambient."""
        for r in FRAGILITY_REPORT:
            assert r.attack, f"{r.hypothesis.tag} missing attack"
            assert r.heal_path, f"{r.hypothesis.tag} missing heal path"
            assert len(r.heal_path) > 30, (
                f"{r.hypothesis.tag} heal path too short to be substantive"
            )


# ===================================================================
# 7. CROSS-VOLUME PROPAGATION
# ===================================================================

class TestCrossVolumeAnchors:
    def test_all_four_volumes_anchored(self):
        """The cross-volume propagation manifest covers all four volumes
        of the CLAUDE.md sec.12 cross-volume coherence statement."""
        expected = {'Vol I', 'Vol II', 'Vol III', 'Vol IV'}
        assert set(CROSS_VOLUME_ANCHORS.keys()) == expected

    def test_vol_ii_anchor_lists_proved_core(self):
        """Vol II anchor names the four load-bearing files: pva-descent,
        e_infinity_topologization, modular_pva_quantization_core,
        programme_climax_platonic."""
        anchor = CROSS_VOLUME_ANCHORS['Vol II']
        for needle in [
            'pva-descent.tex',
            'e_infinity_topologization.tex',
            'modular_pva_quantization_core.tex',
            'programme_climax_platonic.tex',
        ]:
            assert needle in anchor, f"Vol II anchor missing {needle}"

    def test_vol_iii_anchor_names_two_stage_functor(self):
        """Vol III anchor names the two-stage CY-chiral functor
        Phi_d = Sp_Ch o PhiFA_d (CLAUDE.md sec.7)."""
        anchor = CROSS_VOLUME_ANCHORS['Vol III']
        assert 'Phi_d' in anchor or 'two-stage' in anchor.lower()
