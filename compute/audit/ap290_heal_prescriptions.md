# AP290 heal prescriptions

Status: direct writes to the Vol I targets were blocked in this session.

Checked with:

```bash
test -w /Users/raeez/chiral-bar-cobar/chapters/theory/infinite_fingerprint_classification.tex
test -w /Users/raeez/chiral-bar-cobar/notes/first_principles_cache_comprehensive.md
```

Both returned `not_writable`.

## Converged findings

1. The AP290 theorem in Vol I is no longer a bare counting slogan. It now names the Niemeier rows, isolates the `V_1=0` row, and states a separate `w_* = 2` proposition. That part survives attack.
2. The remaining high-severity defect is ambient scope: the theorem still reads like a theorem about `71` proven isomorphism classes of holomorphic VOAs. The cited literature only licenses a theorem about Schellekens rows / weight-one Lie algebra types, with the `V_1=0` row represented by `V^\natural`.
3. The row-0 proof sentence still collapses representation into uniqueness.
4. The compute-surface sentence is false as written: no AP290 tests live in `compute/tests/test_infinite_fingerprint.py`.
5. The AP290 cache entry is directionally right but stale on writability, live Vol II drift count, and current Vol III anchors.

## Independent-path count after hostile reread

- `71 = 24 + 1 + 46`: `3` surviving paths.
  1. Explicit partition of Schellekens rows.
  2. Niemeier `24` + FLM moonshine representative + complement subtraction.
  3. van Ekeren--Lam--M\"oller--Shimakura / M\"oller--Scheithauer orbit-orbifold realization of the nonzero rows plus the distinguished `V_1=0` branch.
- `24 = \operatorname{rank}(N) = #\{\text{Niemeier rows}\}`: `3` surviving paths.
  1. Niemeier class-number theorem in rank `24`.
  2. In-place ADE/common-Coxeter enumeration plus Leech.
  3. Explicit intersection with the Schellekens row set.
- `w_* = 2`: `3` verified lanes, with `2` structurally distinct chain complexes.
  1. Schellekens row classification plus the `V_1=0` exception forces weight `2` as the first uniform threshold.
  2. Ordered bar differential on weight-one residues reconstructs `V_1`.
  3. Hochschild / derived-center lane reads the same threshold on the common cochain complex, with derived-center retaining the extra `E_2` structure.

## Exact edit prescriptions

### 1. Vol I theorem file

File: `/Users/raeez/chiral-bar-cobar/chapters/theory/infinite_fingerprint_classification.tex`

#### Edit 1A. Repair the theorem ambient from `71` VOAs to `71` Schellekens rows

old_string:

```tex
Let $\mathfrak{S}_{24}^{\mathrm{hol}}$ be the closed ambient of the
$71$ strongly rational holomorphic VOAs of central charge~$24$ on
Schellekens's list, viewed as chiral algebras~$A$ with fingerprint
$\varphi(A)$. Then:
```

new_string:

```tex
Let $\mathfrak{S}_{24}^{\mathrm{hol}}$ be the closed ambient of the
$71$ Schellekens rows at central charge~$24$: the $70$ nonzero
weight-one Lie algebra types of Schellekens's Table~2 together with the
distinguished $V_1=0$ row, written $\rho_0$. When a concrete
representative is needed, we take the corresponding Niemeier lattice
VOA on the lattice rows and
$V^\natural$ as a distinguished representative of the $V_1=0$ row.
Then:
```

#### Edit 1B. Stop identifying the middle summand with moonshine uniqueness

old_string:

```tex
 \mathfrak{S}_{24}^{\mathrm{Niem}}
 \;\sqcup\;
 \{V^\natural\}
 \;\sqcup\;
 \mathfrak{S}_{24}^{\mathrm{nonlat}},
```

new_string:

```tex
 \mathfrak{S}_{24}^{\mathrm{Niem}}
 \;\sqcup\;
 \{\rho_0\}
 \;\sqcup\;
 \mathfrak{S}_{24}^{\mathrm{nonlat}},
```

old_string:

```tex
 row~$0$ is the Monster slot $V_1=0$, and the non-lattice summand is
 the explicit complement
```

new_string:

```tex
 row~$0$ is the distinguished row $\rho_0$ with $V_1=0$, represented by
 $V^\natural$ when a concrete model is needed, and the non-lattice
 summand is the explicit complement
```

#### Edit 1C. Rewrite Step 3 as a representative statement, not a uniqueness claim

old_string:

```tex
\emph{Step~3: isolate the Monster singleton.}
Schellekens isolates the unique row with~$V_1=0$; FLM identify that row
with the Moonshine module~$V^\natural$
\textup{(}FLM88, Chapters~8--11; compare also M\"oller--Scheithauer
2023, Theorem~6.9, pp.~40--41\textup{)}. This gives the singleton
summand~$\{V^\natural\}$.
```

new_string:

```tex
\emph{Step~3: isolate the distinguished $V_1=0$ row.}
Schellekens isolates the unique row with~$V_1=0$. FLM construct the
Moonshine module~$V^\natural$ in that row
\textup{(}FLM88, Chapters~8--11; compare also M\"oller--Scheithauer
2023, Theorem~6.9, pp.~40--41\textup{)}. The AP290 theorem is therefore
a theorem about Schellekens rows: the middle summand is the distinguished
row~$\rho_0$, with $V^\natural$ fixed only as a representative when a
concrete model is needed. No general uniqueness statement at~$V_1=0$ is
used here.
```

#### Edit 1D. Correct the compute-harness sentence

old_string:

```tex
Compute-side harness at
\texttt{compute/tests/test\_infinite\_fingerprint.py}.
```

new_string:

```tex
Compute-side harness for the pre-existing chapter theorems is at
\texttt{compute/tests/test\_infinite\_fingerprint.py}. The AP290
structured-subset / weight-two-threshold surface still requires a
dedicated harness for the explicit Schellekens row partition, the
Niemeier-row count, and the uniform threshold~$w_\ast=2$.
```

### 2. Vol I AP290 cache entry

File: `/Users/raeez/chiral-bar-cobar/notes/first_principles_cache_comprehensive.md`

#### Edit 2A. Add the row-vs-VOA scope note that remains open after the first heal

Insert immediately after the `**Verification ledger required by AP290**:` bullet list:

new_string:

```md
**Scope note after hostile reread**:
- The repaired theorem should be stated on the `71` Schellekens rows / weight-one Lie algebra slots, not as an unconditional theorem about `71` proven isomorphism classes of holomorphic VOAs. The modern literature gives uniqueness for the `70` nonzero `V_1` rows and supplies `V^\natural` as the distinguished representative of the `V_1=0` row; the AP290 heal should not silently upgrade that to a closed moonshine-uniqueness theorem.
```

#### Edit 2B. Replace the stale cross-family block

old_string:

```md
**Cross-family verification state**:
- Vol I: `chapters/examples/landscape_census.tex` is synchronized to the structured-subset theorem; the master-table surface now names the `24+1+46` decomposition as a theorematic corollary rather than a frontier slogan.
- Vol II: `/Users/raeez/chiral-bar-cobar-vol2/main.tex:1149-1152` and `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex:450-457` still advertise `71 = 24 + 1 + 46` as a bare three-stratum classification formula. The drift is identified but not healable in this session because those files lie outside the writable root.
- Vol III BKM: `/Users/raeez/calabi-yau-quantum-groups/main.tex:561-564` and `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:1617-1619` were checked against AP290. The honest transport is `24 =` Leech/Niemeier rank datum, not full holomorphic-`c=24` family count.
- Vol III CY$_3$ DT: `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1541-1550` was checked against AP290. The portable statement is the low-degree / weight-two threshold, not a new integer-decomposition theorem. This drift is likewise blocked from in-place repair by the current sandbox.
```

new_string:

```md
**Cross-family verification state (re-attacked)**:
- Vol I: `chapters/examples/landscape_census.tex:327-340` has the counting-vs-classification heal, but its ambient sentence should still be sharpened from "`71` holomorphic VOAs" to the `71` Schellekens rows / weight-one types, with `V^\natural` only as a representative of the `V_1=0` row.
- Vol II: live drift remains at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:1149-1152`, `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex:450-457`, `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1778-1786`, and `/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1807-1812`; each still advertises `71 = 24 + 1 + 46` as a classification theorem rather than as the counting corollary of a structured-subset derivation. These files are in the current writable root, so the old "outside the writable root" note is stale.
- Vol III BKM: `/Users/raeez/calabi-yau-quantum-groups/main.tex:561-564` is honest if read as the transport of the common rank datum `24`, not as a new holomorphic-`c=24` classification theorem. No live `71 = 24 + 1 + 46` advertisement was found on the checked BKM surfaces.
- Vol III CY$_3$ DT: the checked live theorem surface `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1541-1550` now carries only a test-count sentence, not an AP290 integer-decomposition slogan. The portable statement remains the low-degree / weight-two threshold, not a new `71` theorem.
```

#### Edit 2C. Record the missing compute coverage

Insert after the cross-family block:

new_string:

```md
**Compute-surface state**:
- `compute/tests/test_infinite_fingerprint.py` currently does not cover `thm:schellekens-structured-subset` or `prop:schellekens-weight-two-threshold`.
- The only live Schellekens tests found in this session are counting-level checks in `compute/tests/test_exceptional_shadow_engine.py:471-497` (`71`, `24`, and a few class labels). AP290 still needs a dedicated structured-subset / threshold harness.
```

### 3. Vol I landscape census follow-up

File: `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex`

#### Edit 3A. Keep the heal but repair the ambient scope

old_string:

```tex
\noindent The Schellekens $71$~holomorphic VOAs at $c = 24$ are no
longer a frontier gap on the classification surface:
Theorem~\ref{thm:schellekens-structured-subset} identifies the
structured decomposition
\[
71 = 24_{\mathrm{Niemeier}} + 1_{\mathrm{Monster}} + 46_{\mathrm{nonlat}}
\]
as a corollary of an explicit partition of Schellekens's numbered list.
```

new_string:

```tex
\noindent The Schellekens $71$ rows at $c = 24$ are no
longer a frontier gap on the classification surface:
Theorem~\ref{thm:schellekens-structured-subset} identifies the
structured decomposition
\[
71 = 24_{\mathrm{Niemeier}} + 1_{V_1=0} + 46_{\mathrm{nonlat}}
\]
as a counting corollary of an explicit partition of Schellekens's
numbered list. When a concrete representative of the $V_1=0$ row is
needed we use $V^\natural$, but the row statement itself does not assume
moonshine uniqueness.
```

## Additional live drift surfaces

These were checked during the AP290 pass and still need propagation once the Vol I theorem wording is repaired:

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/schellekens_71_alpha_classification_platonic.tex:130-154`
- `/Users/raeez/chiral-bar-cobar-vol2/main.tex:1149-1152`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex:450-457`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1778-1786`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:1807-1812`

## Sources checked

- Schellekens, *Meromorphic `c=24` conformal field theories* (CERN record / DOI surface).
- van Ekeren--Lam--M\"oller--Shimakura, *Schellekens' list and the very strange formula* (row scope and nonzero `V_1` theorem).
- M\"oller--Scheithauer, deep-hole / generalized-orbifold realization surfaces for the nonzero rows and the distinguished `V_1=0` branch.
- FLM, Chapters 8--11, for the Moonshine representative.
