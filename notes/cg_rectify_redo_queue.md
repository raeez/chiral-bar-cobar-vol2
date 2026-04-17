# Chriss-Ginzburg rectification queue — Volume II

One entry per `\input{}`'d chapter in `main.tex`, excluding abstract / preface / introduction.
Mark `[x]` when a chapter completes all five phases; `[~]` if partial with a `RESUME-FROM` cursor.
Order follows `main.tex` linear traversal (Part I $\to$ Part VIII $\to$ Conclusion).

## Part I — The Open Primitive

- [ ] `chapters/theory/foundations.tex`
- [x] `chapters/theory/locality.tex` — 2026-04-17: Gate-2 forward-ref qualifier on $\cP^{\mathrm{ch}}$ + orphan-notation cleanup (opener); Gate-3 forcing-sentence paragraphs before each of §1.1.1/1.1.2/1.1.3 cold subsubsection openers. No formula/scope/status changes. V2-AP40 pre-clean. Balance 34=34. Audit converged.
- [x] `chapters/theory/axioms.tex` — 2026-04-17: Gate-3 forcing paragraphs before cold openers of §1.1 (underlying data), §1.6 (product+bracket), §1.10 (sesqui proof), §1.13 (compat PVA). Gate-1 structural: restored missing `\end{construction}` for `const:coend-formula-mk` (pre-existing 74=73 imbalance → 74=74). No formulas/scope/status touched. κ values verified (Heis k, KM dim(g)(k+h^v)/(2h^v), Vir c/2, W_N c(H_N-1), W_2 boundary=c/2). Audit converged. AP43 hook false positive on pre-existing line.
- [x] `chapters/theory/equivalence.tex` — 2026-04-17: CONVERGED on first look, zero edits. Bridge chapter linking operad ↔ axioms. V2-AP40 clean; balance 2=2; all four subsections have forcing sentences; Gate-4 scope on E_3-algebraic vs E_3-topological correctly qualified (affine KM non-critical proved, general conjectural, class M weight-completed). Reconstituted state already at Chriss-Ginzburg standard.
- [x] `chapters/theory/bv-construction.tex` — 2026-04-17: Gate-3 forcing sentences for §1.4 (higher operations via FM/E_1 integrals) and §1.5 (framing the 4-subsection PVA-verification unit: well-definedness, sesqui, comm/assoc, skewsym/Jacobi, Leibniz). No formulas/scope/status touched. V2-AP40 pre-clean. Balance 27=27. All A_∞-at-n=2 signs, sesqui on cohomology, skewsym, Jacobi, Leibniz (divided-power convention) verified.
- [~] `chapters/theory/factorization_swiss_cheese.tex` — 2026-04-17 partial: Gate-1 typo fix (`\end{remark>` → `\end{remark}` at line 2595, restoring remark env balance); V2-AP40d environment-title leak cleaned (`[Ordered vs symmetric bar primacy; resolution of FM69]` → `[Ordered vs symmetric bar primacy]`; in-prose "FM69 critique" → "the objection"). Spot-audited κ formulas in §1-3 (Heisenberg/KM/Virasoro subsections 258-720): κ(Ĥ_k)=k, κ(ĝ_k)=(k+h^∨)·d/(2h^∨), κ(Vir_c)=c/2, all correct per AP39/AP105/AP1. Heisenberg OPE `1/(z-w)` is BD/D-module convention for log-1-form chiral product, not physicist's `k/(z-w)^2` — self-consistent throughout chapter, not a bug. **RESUME-FROM: full Phase-3 linear sweep of §4-§14 (lines ~738-4129) deferred to next cron tick**. Non-commented balance is correct (199=198 includes a commented-out `\begin{theorem}[Pentagon]` at line 1886, harmless).
- [x] `chapters/theory/sc_chtop_heptagon.tex` — 2026-04-17: V2-AP40 sweep (6 leaks healed into declarative mathematics). (1) `(MP1/FM41)` × 2 restated as "categorical-level distinction" prose (A is E_1; braided structure on Mod_A one level up). (2) `FM160` × 2 restated as "chain-level BV/convolution identification". (3) `(Vol.~I, AP47)` restated as "evaluation-generated core where affine monodromy identification holds unconditionally". (4) `(FM158 heal)` restated as "Kontsevich-Tamarkin formality treated as ∞-quasi-isomorphism with associator data, not strict dg-operad map". Balance 75=75; all leaks 0. No formula/scope/status changes.
- [ ] `chapters/theory/raviolo.tex`
- [ ] `chapters/theory/raviolo-restriction.tex`
- [ ] `chapters/theory/fm-calculus.tex`
- [ ] `chapters/theory/orientations.tex`
- [ ] `chapters/theory/fm-proofs.tex`
- [ ] `chapters/theory/pva-descent-repaired.tex`
- [ ] `chapters/theory/pva-expanded-repaired.tex`

## Part II — The $E_1$ Core

- [ ] `chapters/connections/bar-cobar-review.tex`
- [ ] `chapters/connections/line-operators.tex`
- [ ] `chapters/connections/ordered_associative_chiral_kd_core.tex`
- [ ] `chapters/connections/dg_shifted_factorization_bridge.tex`
- [ ] `chapters/connections/thqg_gravitational_yangian.tex`
- [ ] `chapters/connections/typeA_baxter_rees_theta.tex`
- [ ] `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex`
- [ ] `chapters/connections/casimir_divisor_core_transport.tex`
- [ ] `chapters/theory/unified_chiral_quantum_group.tex`
- [ ] `chapters/theory/super_chiral_yangian.tex`

## Part III — The Faces of $r(z)$ ($\mathrm{GRT}_1(\Q)$-torsor)

- [ ] `chapters/connections/dnp_identification_master.tex`
- [ ] `chapters/theory/grt_parametrized_seven_faces.tex`
- [ ] `chapters/connections/spectral-braiding-core.tex`
- [ ] `chapters/connections/ht_bulk_boundary_line_core.tex`
- [ ] `chapters/connections/celestial_boundary_transfer_core.tex`
- [ ] `chapters/connections/affine_half_space_bv.tex`
- [ ] `chapters/connections/fm3_planted_forest_synthesis.tex`
- [ ] `chapters/connections/kontsevich_integral.tex`

## Part IV — The Characteristic Datum and Modularity

- [ ] `chapters/examples/rosetta_stone.tex`
- [ ] `chapters/examples/examples-computing.tex`
- [ ] `chapters/examples/examples-complete-proved.tex`
- [ ] `chapters/examples/examples-worked.tex`
- [ ] `chapters/examples/w-algebras-virasoro.tex`
- [ ] `chapters/examples/w-algebras-w3.tex`
- [ ] `chapters/connections/hochschild.tex`
- [ ] `chapters/connections/brace.tex`
- [ ] `chapters/theory/modular_swiss_cheese_operad.tex`
- [ ] `chapters/theory/curved_dunn_higher_genus.tex`
- [ ] `chapters/theory/class_m_direct_sum_obstruction_platonic.tex`
- [ ] `chapters/theory/topologization_class_m_original_complex_platonic.tex`
- [ ] `chapters/theory/tempered_stratum_characterization_platonic.tex`
- [ ] `chapters/theory/wn_tempered_closure_platonic.tex`
- [ ] `chapters/theory/beta_N_closed_form_all_platonic.tex`
- [ ] `chapters/theory/logarithmic_wp_tempered_analysis_platonic.tex`
- [ ] `chapters/theory/irrational_cosets_tempered_platonic.tex`
- [ ] `chapters/theory/bp_chain_level_strict_platonic.tex`
- [ ] `chapters/connections/fm81_fractional_ghost_platonic.tex`
- [ ] `chapters/connections/relative_feynman_transform.tex`
- [ ] `chapters/connections/modular_pva_quantization_core.tex`

## Part V — The Standard HT Landscape

- [ ] `chapters/connections/ht_physical_origins.tex`
- [ ] `chapters/connections/ym_boundary_theory.tex`
- [ ] `chapters/connections/ym_higher_body_couplings.tex`
- [ ] `chapters/connections/ym_instanton_screening.tex`
- [ ] `chapters/connections/celestial_holography_core.tex`
- [ ] `chapters/connections/log_ht_monodromy_core.tex`
- [ ] `chapters/connections/anomaly_completed_core.tex`
- [ ] `chapters/connections/thqg_holographic_reconstruction.tex`
- [ ] `chapters/connections/thqg_modular_bootstrap.tex`
- [ ] `chapters/connections/holomorphic_topological.tex`
- [ ] `chapters/connections/feynman_diagrams.tex`
- [ ] `chapters/connections/feynman_connection.tex`
- [ ] `chapters/connections/bv_brst.tex`

## Part VI — Three-Dimensional Quantum Gravity

- [ ] `chapters/connections/part_vi_platonic_introduction.tex`
- [ ] `chapters/connections/thqg_gravitational_complexity.tex`
- [ ] `chapters/connections/3d_gravity.tex`
- [ ] `chapters/connections/e_infinity_topologization.tex`
- [ ] `chapters/connections/w_infty_e_infty_endpoint_platonic.tex`
- [ ] `chapters/connections/programme_climax_platonic.tex`
- [ ] `chapters/connections/thqg_3d_gravity_movements_vi_x.tex`
- [ ] `chapters/connections/thqg_critical_string_dichotomy.tex`
- [ ] `chapters/connections/thqg_perturbative_finiteness.tex`
- [ ] `chapters/connections/thqg_soft_graviton_theorems.tex`
- [ ] `chapters/connections/thqg_symplectic_polarization.tex`
- [ ] `chapters/theory/chiral_higher_deligne.tex`
- [ ] `chapters/connections/universal_holography_functor.tex`
- [ ] `chapters/connections/universal_celestial_holography.tex`
- [ ] `chapters/connections/celestial_moonshine_bridge.tex`
- [ ] `chapters/connections/soft_graviton_mellin_shadow_bridge_platonic.tex`
- [ ] `chapters/connections/monster_chain_level_e3_top_platonic.tex`
- [ ] `chapters/connections/schellekens_71_alpha_classification_platonic.tex`

## Part VII — The Frontier

- [ ] `chapters/connections/spectral-braiding-frontier.tex`
- [ ] `chapters/connections/ht_bulk_boundary_line_frontier.tex`
- [ ] `chapters/connections/celestial_boundary_transfer_frontier.tex`
- [ ] `chapters/examples/examples-complete-conditional.tex`
- [ ] `chapters/examples/w-algebras-frontier.tex`
- [ ] `chapters/connections/modular_pva_quantization_frontier.tex`
- [ ] `chapters/connections/ordered_associative_chiral_kd_frontier.tex`
- [ ] `chapters/connections/celestial_holography_frontier.tex`
- [ ] `chapters/connections/log_ht_monodromy_frontier.tex`
- [ ] `chapters/connections/anomaly_completed_frontier.tex`

## Part VIII — From Frontier to Theorem

- [ ] `chapters/frame/part_viii_synthesis.tex`
- [ ] `chapters/theory/koszulness_moduli_M_kosz.tex`
- [ ] `chapters/theory/infinite_fingerprint_classification.tex`

## Conclusion

- [ ] `chapters/connections/conclusion.tex`

## Completion log

(Append one line per completed chapter, with date, file, one-sentence summary of fixes, and final line count.)
