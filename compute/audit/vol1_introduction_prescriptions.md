# Vol I `introduction.tex` prescriptions

## 1. Summary header

- Lines read:
  `introduction.tex` `1-1240`, `1328-1362`, `1426-1445`, `1548-1605`, `1688-1735`, `1798-1918`, `2336-2348`, `2466-2484`, `2658-2696`, `2794-2850` (`1649` lines);
  `main.tex` `724-954` (`231` lines);
  `preface.tex` `1-420`, `1778-1806` (`449` lines);
  `landscape_census.tex` `120-230`, `470-540`, `930-980`, `1740-1860` (`354` lines).
  Total inspected: `2683` lines.
- Findings count: `13` material findings.
- AP293-positive deliverable statement:
  replace the current theorem-and-bridge surface by one introduction-level ordered-bar read-back in which A/B/C/D/H/F/G are all stated at their strongest honest form, with the ordered bar primitive, family-dependent complementarity constants explicit, and Vol II/III bridges scoped to the verified Koszul/boundary-obstruction locus.

## 2. Opening-paragraph audit

Current opening (`introduction.tex:19-25`):

> Classical Koszul duality terminates over a point: a quadratic algebra~$A$ has a Koszul dual coalgebra~$A^{!}$, the bar construction $B(A)$ mediates between them, and the inversion $\Omega(B(A))\xrightarrow{\sim}A$ closes the theory. Over a smooth algebraic curve~$X$ it does not terminate. Generators become sections of a $\mathcal{D}_X$-module; relations become operator product expansions; the bar differential becomes an integral transform with logarithmic kernel $\eta=d\log(z_1-z_2)$ on Fulton--MacPherson configuration spaces; the topology of higher-genus curves forces Hodge-curvature obstructions that have no classical counterpart.
>
> This monograph studies one phenomenon: the chiral Koszul reflection $K\colon\mathrm{Kosz}(X)\to\mathrm{Kosz}(X)^{\mathrm{op}}$ on chirally Koszul algebras over~$X$. The atomic object is the ordered bar coalgebra
> \[
> \barB^{\mathrm{ord}}_X(\cA)\;=\;T^{c}\bigl(s^{-1}\bar\cA\bigr),
> \]
> a cofree $\Eone$-coalgebra with deconcatenation coproduct, R-matrix carrier, and Yangian source. Its degree-$2$ component is the classical $r$-matrix $r_\cA(z)$. Its symmetric coinvariant $\barB^{\Sigma}_X(\cA)=\Sym^{c}(s^{-1}\bar\cA)$ is the modular shadow; the lossy projection that discards the $R$-matrix and retains only the scalar modular characteristic extracted from $\mathrm{av}(r_\cA(z))$. For non-abelian affine Kac--Moody the precise degree-$2$ formula is $\kappa(\cA)=\mathrm{av}(r_\cA(z))+\dim(\fg)/2$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it through two equations and seven theorems.

Verdict: `fails target 1`.

- It does not begin atom-first. The point-case recap occupies the first sentence and first paragraph (`introduction.tex:19-20`), whereas the platonic ideal starts immediately with the phenomenon and the ordered bar (`main.tex:728-752`, `preface.tex:42-60`).
- The first sentence is also AP25-incorrect: it calls `$A^{!}$` a coalgebra (`introduction.tex:19`), but the same file later distinguishes the dual coalgebra `$A^{\scriptstyle \text{\normalfont !\textasciigrave}}$` from the dual algebra `$A^!$` (`introduction.tex:61-65`).
- The opener then swings straight into a theorem dump (`introduction.tex:27-38`) before the explicit construction sequence is on the page, so even the atomic second paragraph is immediately buried under abstract-style summary.

Prescription:

- Move the ordered bar and chiral Koszul reflection to sentence one.
- Push the point-case comparison behind the primitive object.
- Repair the three-object discipline at the first mention: `B(A)`, `\Omega(B(A))`, Verdier/Koszul dual, and derived centre must not be conflated.

## 3. Derivation-sequence audit

| Step | Status | Evidence | Audit |
| --- | --- | --- | --- |
| 1. Smooth algebraic curve `X` as input geometry | `present` | `introduction.tex:67-75`, `303-325` | The curve and chiral bracket are explicitly introduced. |
| 2. `X` determines the factorisation operad/cooperad | `garbled` | `introduction.tex:40-43` | This appears only as narration. No explicit operadic construction is inserted before the bar object is used. |
| 3. Ordered bar complex `\barB_X^{\mathrm{ord}}(\cA)` | `present` | `introduction.tex:21-25`, `366-375`, `1346-1353` | The ordered bar is explicitly written as `T^c(s^{-1}\bar\cA)`. |
| 4. Differential `D` from the logarithmic kernel plus Arnold relation | `present` | `introduction.tex:257-279`, `382-408` | `d_{\barB}=d_{\mathrm{int}}+d_{\mathrm{res}}+d_{\mathrm{dR}}` and the role of `\eta_{ij}=d\log(z_i-z_j)` are explicit. |
| 5. Nilpotence `D^2=0` | `present` | `introduction.tex:211-253`, `598-601` | The selection principle gives the nilpotence criterion and the Heisenberg example exhibits the Arnold cancellation. |
| 6. Two coproducts: deconcatenation and shuffle | `garbled` | deconcatenation: `introduction.tex:25`, `1353-1355`; symmetric shadow without shuffle construction: `introduction.tex:25`, `1338-1359` | The ordered coproduct is explicit, but the symmetric/shuffle coproduct is never explicitly constructed. |
| 7. Log / exp / dual trifecta | `garbled` | `introduction.tex:2470-2473`, `2800-2801`, `2827-2831`, `2868` | `categorical logarithm` is only roadmap language; the logarithm/exponential/dual triad is never assembled as one construction sequence. |

Internal contradiction firing AP97/AP104:

- `introduction.tex:366-375` explicitly defines the ordered bar with no `\Sigma_n`-quotient.
- `introduction.tex:1338-1344` later claims that `\S\ref{sec:volume-one-route}` had presented the symmetric bar and only now reaches the ordered primitive.
- These two surfaces cannot both be true. The introduction currently states both the correct E1-primacy story and its negation.

Prescription:

- Replace the organising-principle paragraph by an explicit seven-step construction.
- Repair the later E1-primacy paragraph so it says the earlier section already built the ordered bar and only the theorem read-back had passed to its symmetric `\operatorname{av}`-image.

## 4. Per-family example spacing audit

Overall cadence verdict: `uneven`.

- `G/L` receive early worked surfaces (`introduction.tex:257-280`, `578-670`).
- `C/M` are mostly taxonomic labels until much later (`introduction.tex:119-121`, `2209`, `2406-2407`).
- Against the target cadence, the introduction does not balance Heisenberg/Kac--Moody with comparably explicit `\beta\gamma` and Virasoro read-backs.

| Family | Introduction cadence lines | Canonical landscape datum | Correctness check | Spacing verdict |
| --- | --- | --- | --- | --- |
| `G` Heisenberg | `77-85`, `117-118`, `257-263`, `578-670`, table row `2342` | `\kappa(\mathcal{H}_\kappa)=\kappa` (`landscape_census.tex:138-140`); `r_{\max}=2`, no higher shadow (`landscape_census.tex:478-479`) | `r_{\max}=2` is correct at `117-118`; the theorem subsection is consistent at `630-657`. But the later summary table gives `K=2` at `2342`, contradicting canonical `K=0` (`landscape_census.tex:1747-1749`). | Over-represented and later numerically inconsistent in the summary table. |
| `L` affine Kac--Moody | `25`, `118-119`, `264-280`, `429-431`, `1432-1440`, table row `2344` | `\kappa(\widehat{\fg}_k)=td/(2h^\vee)` (`landscape_census.tex:145-148`); `r_{\max}=3`, first higher shadow `C` (`landscape_census.tex:488-490`) | `\kappa` formula is correct at `25` and `1432-1440`; `r_{\max}=3` is correct at `118-119`. The first higher shadow is not named where the class is first introduced. | Early and mathematically sound, but the class-`L` witness is under-described relative to the canonical `C`-shadow wording. |
| `C` `\beta\gamma` | `119-120`, `483`, `727`, `954`, `2209`, roadmap `2406-2407`, `2583-2586`, table row `2345` | `\kappa(\beta\gamma_\lambda)=6\lambda^2-6\lambda+1` (`landscape_census.tex:1821-1829`); `r_{\max}=4`, quartic contact shadow (`landscape_census.tex:494-498`, `955-960`) | `r_{\max}=4` is correct at `119-120`; `\mu_{\beta\gamma}=0` and degree-`4` termination are correctly recalled at `2406-2407`. But no `\kappa` formula is ever stated in the introduction, and the table row `2345` silently specializes to `\lambda=1` without saying so. | Too late and too compressed; the `C` family never gets a peer-level worked introduction surface. |
| `M` Virasoro / finite-type `\mathcal{W}` | `84`, `120-121`, `431`, `456-459`, `504-505`, `1809`, table row `2346` | `\kappa(\mathrm{Vir}_c)=c/2` (`landscape_census.tex:195-197`, `1832-1838`); `r_{\max}=\infty`, first higher shadows `C+Q` (`landscape_census.tex:504-508`, `936-943`) | `\kappa=c/2` is correct at `431`; `r_{\max}=\infty` is correct at `120-121`; the Virasoro `T`-line constant `C_\cA=6` at `456-459` matches the canonical class-`M` read-back. But the introduction never gives a balanced worked Virasoro example at the same cadence as Heisenberg/KM. | Formulaically correct, but the `M` lane is introduced as taxonomy and slogan rather than explicit construction. |

Net formula check against `landscape_census.tex`:

- `Heisenberg`: one concrete discrepancy at `introduction.tex:2342` versus `landscape_census.tex:1747-1749`.
- `Affine Kac--Moody`: no discrepancy found.
- `\beta\gamma`: no wrong formula written, but the family `\kappa` formula is missing and the unlabelled `\lambda=1` specialization at `2345` is scope drift.
- `Virasoro`: no discrepancy found.

## 5. Seven-theorems audit (A/B/C/D/H/F/G)

Platonic comparator:

- abstract: `main.tex:775-837`
- preface dual-lane read-back: `preface.tex:130-191`

| Thm | Introduction statement range | AP289 strongest-honest-form verdict | AP113/AP270/AP275 scope verdict | Prescription |
| --- | --- | --- | --- | --- |
| `A` | `introduction.tex:698-714`; weaker summaries at `477-483`, `534-535` | `fails` | `fails` | Replace the theorem surface with the preface two-lane statement (`preface.tex:132-138`): factorization-`∞` and chain-level lanes both load-bearing; remove the drift to a bare `(\infty,2)` slogan. |
| `B` | `introduction.tex:716-729`; overcompressed summary at `480-483` | `mixed` | `mixed` | Keep the ambient-qualified surface, but name the strict Koszul-locus statement and the weight-completed/coderived Positselski continuation exactly as in `preface.tex:139-145`; do not let earlier slogans overstate all-genera strict inversion. |
| `C` | `introduction.tex:732-754`; scalar shadows only later at `969-971` | `fails` | `partial pass` | Keep the proved Verdier/Lagrangian core and the perfectness boundary, but add the family-dependent scalar sums `0,13,250/3,98/3` at theorem level as in `main.tex:789-801` and `preface.tex:152-153`. |
| `D` | `introduction.tex:756-812`; weaker slogans at `139-142`, `488-494`, `896-902` | `mixed` | `mixed` | Canonicalize the later strong form everywhere: all-weight `F_g=\kappa(\cA)\lambda_g^{\mathrm{FP}}+\delta F_g^{\mathrm{cross}}(\cA)` with uniform-weight specialization `\mathrm{obs}_g=\kappa(\cA)\lambda_g`; remove bare `\mathrm{obs}_g=\kappa\lambda_g` slogans outside their lane. |
| `H` | `introduction.tex:814-836`; three-Hochschild warning at `839-859` | `mostly passes` | `mostly passes` | Keep this as the canonical theorem surface; demote the compressed line-`38`/line-`817` slogans to references back to this scoped statement. |
| `F` | only slogan-level at `introduction.tex:548-550` and `38` | `fails` | `fails` | Promote the preface theorem statement (`preface.tex:174-181`) into the introduction: source, target, image, and boundary-Lagrangian scope must be on the page. |
| `G` | only slogan-level at `introduction.tex:551-553` and `38` | `fails` | `fails` | Promote the preface theorem statement (`preface.tex:182-190`) into the introduction: the `iff` classification clause and its `\kch\ne 0`/`FF` scope must be explicit. |

Theorem-specific notes:

- `A`: the target lane label in the prompt is `(∞,1) native, chain-level via Pattern 269)`. The current introduction never states that pair. Its best theorem bullet is still the one-lane quadratic surface at `698-714`.
- `B`: the introduction's best local formulation is already close to the desired honest form, but it is undercut by earlier globalized summaries.
- `C`: the theorem surface is missing the exact family-dependent complementarity constants even though the abstract already carries them (`main.tex:798-801`).
- `D`: the file contains both the strong theorem and a weaker older slogan. Those two surfaces must be unified.
- `H`: this is the cleanest theorem surface in the introduction because the warning block (`839-859`) enforces AP25.
- `F/G`: on the introduction surface these are still architecture slogans, not theorem statements.

## 6. Cross-volume-bridge audit

Platonic comparator:

- abstract: `main.tex:921-949`
- preface: `preface.tex:1778-1798`, `197-218`

| Bridge | Introduction lines | AP275 verdict | Audit | Prescription |
| --- | --- | --- | --- | --- |
| Vol II dimensional-reduction bridge | `introduction.tex:1701-1705` | `fails` | `SC`/derived-centre language is presented as a global dimensional layer with no Koszul-locus or boundary-obstruction qualifier. | Scope to the chirally Koszul boundary-Lagrangian locus and name the obstruction boundary explicitly. |
| Vol II topologization bridge | `introduction.tex:1878-1903` | `partial pass` | This is the one bridge passage already naming a proved surface (affine KM, non-critical) and a conditional surface (general Vir/W). | Keep this as the model, but fold its non-critical/BRST boundary into the final bridge paragraph. |
| Final Vol II outlook bridge | `introduction.tex:2672-2687` | `fails` | `\SCchtop`, homotopy-Koszulity, bulk/boundary/line triangle, and `3d quantum gravity` are all advertised as programme-global. | Replace by a scoped bridge paragraph: proved affine/Sugawara lane, conditional general conformal-vector lane, frontier `\cW_\infty` endpoint. |
| Vol III dimensional-reduction bridge | `introduction.tex:1706-1715` | `fails` | The `\Phi_{\mathrm{CY}}` source is described too globally; the verified `d=2` slice and the scoped `d\ge 3` frontier are not turned into the governing qualifier. | Rewrite to foreground the verified `d\le 2` surface and the scope-dependent `d\ge 3` frontier. |
| Final Vol III outlook bridge | `introduction.tex:2688-2689` | `fails` | `Volume~III constructs the Calabi--Yau-to-chiral functor` is presented as an achieved global bridge, not a scoped source/comparison surface. | Replace with the abstract/preface scope language: source supplied on the verified surface, programme-level comparison conjectural beyond it. |

High-risk global sentence:

- `introduction.tex:1862-1864` claims that for every standard vertex algebra the boundary OPE determines the entire bulk.
- This overstates the bridge: it suppresses the boundary-Lagrangian/Koszul hypothesis and the obstruction surfaces named elsewhere in the programme.

## 7. Verbatim Edit prescriptions

### Prescription 1: opener

```text
old_string:
Classical Koszul duality terminates over a point: a quadratic algebra~$A$ has a Koszul dual coalgebra~$A^{!}$, the bar construction $B(A)$ mediates between them, and the inversion $\Omega(B(A))\xrightarrow{\sim}A$ closes the theory. Over a smooth algebraic curve~$X$ it does not terminate. Generators become sections of a $\mathcal{D}_X$-module; relations become operator product expansions; the bar differential becomes an integral transform with logarithmic kernel $\eta=d\log(z_1-z_2)$ on Fulton--MacPherson configuration spaces; the topology of higher-genus curves forces Hodge-curvature obstructions that have no classical counterpart.

This monograph studies one phenomenon: the chiral Koszul reflection $K\colon\mathrm{Kosz}(X)\to\mathrm{Kosz}(X)^{\mathrm{op}}$ on chirally Koszul algebras over~$X$. The atomic object is the ordered bar coalgebra
\[
\barB^{\mathrm{ord}}_X(\cA)\;=\;T^{c}\bigl(s^{-1}\bar\cA\bigr),
\]
a cofree $\Eone$-coalgebra with deconcatenation coproduct, R-matrix carrier, and Yangian source. Its degree-$2$ component is the classical $r$-matrix $r_\cA(z)$. Its symmetric coinvariant $\barB^{\Sigma}_X(\cA)=\Sym^{c}(s^{-1}\bar\cA)$ is the modular shadow; the lossy projection that discards the $R$-matrix and retains only the scalar modular characteristic extracted from $\mathrm{av}(r_\cA(z))$. For non-abelian affine Kac--Moody the precise degree-$2$ formula is $\kappa(\cA)=\mathrm{av}(r_\cA(z))+\dim(\fg)/2$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it through two equations and seven theorems.

new_string:
This monograph studies one phenomenon: the chiral Koszul reflection $K\colon\mathrm{Kosz}(X)\to\mathrm{Kosz}(X)^{\mathrm{op}}$ on chirally Koszul algebras over a smooth algebraic curve~$X$. The primitive object is the ordered bar coalgebra
\[
\barB^{\mathrm{ord}}_X(\cA)\;=\;T^{c}\bigl(s^{-1}\bar\cA\bigr),
\]
a cofree $\Eone$-coalgebra with deconcatenation coproduct whose logarithmic kernel $\eta=d\log(z_1-z_2)$ records the full OPE data of~$\cA$ on Fulton--MacPherson configuration spaces. Its degree-$2$ component is the classical $r$-matrix $r_\cA(z)$, and its symmetric coinvariant $\barB^{\Sigma}_X(\cA)=\Sym^{c}(s^{-1}\bar\cA)$ is the lossy modular shadow obtained by averaging ordered data. For non-abelian affine Kac--Moody the degree-$2$ scalar extracted from the ordered bar is
\[
\kappa\bigl(V_k(\fg)\bigr)\;=\;\operatorname{av}\bigl(r_k(z)\bigr)+\tfrac{1}{2}\dim\fg.
\]
Classical Koszul duality over a point reappears only as the degenerate shadow in which one forgets the curve, the ordering, and the higher-genus Hodge curvature: $\Omega(B(A))\simeq A$ is inversion, $\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the Verdier/Koszul-dual lane, and $R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$ is the derived-centre lane.

rationale:
Move the atom to sentence one, remove the point-first abstract dump, and repair the AP25 conflation of inversion / Verdier / derived-centre outputs.

AP anchor:
AP25, AP97, AP104, AP289
```

### Prescription 2: derivation spine

```text
old_string:
The organising principle is as follows. The geometry of the
curve~$X$ determines an operad (the Fulton--MacPherson
compactifications $\FM_n(X)$ with their boundary strata); the
operad determines a bar complex (the cofree coalgebra
$T^c(s^{-1}\bar\cA)$ with its residue-extraction differential);
the bar complex computes the invariants (the modular
characteristic~$\kappa$, the shadow obstruction tower, the
chiral Hochschild cohomology $\ChirHoch^*$). At each step the
passage is forced: one form ($\eta = d\log(z_1 - z_2)$), one
relation (Arnold), one object ($\Theta_\cA$), one equation
($D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$). The
two-equation climax \textup{(G1)+(G2)} is the deepest
inevitability: the bar differential is not primitive, but the
chiral instantiation of Arnold's universal connection through
the Knizhnik--Zamolodchikov functor; and the universal
conductor is not a scalar invariant, but the functorial
ordered-to-symmetric averaging map attached to every ordered
bar package.

new_string:
The organising principle is a sequence of explicit constructions. Start with a smooth algebraic curve~$X$ and the Fulton--MacPherson compactifications $\FM_n(X)$ of ordered configuration spaces, whose boundary strata encode factorisation of collisions. From this geometry one obtains the ordered factorisation/cooperadic input for a chiral algebra~$\cA$ and hence the ordered bar coalgebra
\[
\barB^{\mathrm{ord}}_X(\cA)\;=\;T^c(s^{-1}\bar\cA)
\]
with deconcatenation coproduct. Its differential is
\[
D=d_{\mathrm{int}}+d_{\mathrm{res}}+d_{\mathrm{dR}},
\]
where $d_{\mathrm{res}}$ is built from the logarithmic propagator $\eta_{ij}=d\log(z_i-z_j)$. On triple collisions the Arnold relation is exactly the identity needed for $D^2=0$. Applying $\Sigma_n$-coinvariants then produces the symmetric shadow
\[
\barB^{\Sigma}_X(\cA)\;=\;\Sym^c(s^{-1}\bar\cA),
\]
whose commutative shuffle coproduct is the averaged image of deconcatenation. In this order the theory reads correctly: logarithm first (the ordered bar), exponential/shadow second (the symmetric factorisation package), and duality third (Verdier on the bar package, bar--cobar inversion on the Koszul locus, derived centre via Hochschild). The two-equation climax \textup{(G1)+(G2)} is the universal summary of this construction, not a substitute for it.

rationale:
Make the seven-step construction explicit, insert the missing second coproduct, and turn the current narration into a genuine derivation sequence.

AP anchor:
AP97, AP104, AP25, AP289
```

### Prescription 3: E1 primacy contradiction

```text
old_string:
The bar complex $\barB(\cA)$ presented in \S\ref{sec:volume-one-route}
is the symmetric (commutative) bar: it lives on
$(s^{-1}\bar\cA)^{\otimes n}_{\Sigma_n}$ and forgets the order in
which collisions occur. This presentation is convenient for
formulating the five main theorems and connecting to the modular
operad on~$\overline{\cM}_{g,n}$, but it is not the natural
primitive of the theory. The natural primitive is the
\emph{ordered} bar
\begin{equation}\label{eq:intro-bar-ord}
\barB^{\mathrm{ord}}(\cA)
\;=\;
T^c(s^{-1}\bar\cA)
\;=\;
\bigoplus_{n \ge 0}\,(s^{-1}\bar\cA)^{\otimes n}
\end{equation}
with deconcatenation coproduct, which by Stasheff's theorem
\textup{\cite{Sta63}} is the universal cofree conilpotent
coalgebra on~$s^{-1}\bar\cA$. Every $A_\infty$-chiral algebra
admits a canonical ordered bar; the symmetric bar arises only
after applying $\Sigma_n$-coinvariants externally on each tensor
factor. The unsymmetrized object retains strictly more
information (\S\ref{subsec:e1-as-primitive}).

new_string:
The bar complex constructed in \S\ref{sec:volume-one-route} is already the ordered bar. What the earlier theorem summaries extract from it is the symmetric modular shadow obtained only after applying $\Sigma_n$-coinvariants. Concretely,
\begin{equation}\label{eq:intro-bar-ord}
\barB^{\mathrm{ord}}(\cA)
\;=\;
T^c(s^{-1}\bar\cA)
\;=\;
\bigoplus_{n \ge 0}\,(s^{-1}\bar\cA)^{\otimes n}
\end{equation}
with deconcatenation coproduct, and
\[
\barB^{\Sigma}(\cA)\;=\;\operatorname{av}\bigl(\barB^{\mathrm{ord}}(\cA)\bigr)
\;=\;
\Sym^c(s^{-1}\bar\cA)
\]
is its symmetric coinvariant shadow. Stasheff's theorem
\textup{\cite{Sta63}} identifies $T^c$ as the universal cofree conilpotent
coalgebra on~$s^{-1}\bar\cA$, so the ordered object is primitive and the symmetric object is derived. Every $A_\infty$-chiral algebra admits the ordered bar first; the modular theorems A/B/C/D/H are read after averaging, not before.

rationale:
Resolve the direct contradiction between `introduction.tex:366-375` and `1338-1359` and restore the one-way ordered-to-symmetric information flow.

AP anchor:
AP97, AP104
```

### Prescription 4: family cadence block

```text
old_string:
The tower classifies chiral algebras into four shadow-depth classes
on the non-critical locus, with a fifth companion stratum at the
critical level completing the classification.
The Heisenberg has $r_{\max} = 2$ (formal,
$\Delta = 0$, class~$G$); affine Kac--Moody algebras at non-critical
level have $r_{\max} = 3$ (class~$L$); the $\beta\gamma$ system has
$r_{\max} = 4$ with nilpotent $R$-matrix (class~$C$); Virasoro and
$\mathcal{W}$-algebras have $r_{\max} = \infty$ (class~$M$); at the
critical level $k=-h^\vee$ the Sugawara construction is undefined,
Theorem~H fails, and the Feigin--Frenkel centre
$\operatorname{Fun}(\operatorname{Op}_{{}^L\fg})$ makes
$\ChirHoch^\bullet$ unbounded (Feigin--Frenkel stratum~$FF$). The

new_string:
The tower classifies the standard landscape into four shadow-depth classes
on the non-critical locus, with a fifth companion stratum at the
critical level completing the classification.
The cadence is family-by-family.
Heisenberg lies in class~$G$: $\kappa(\cH_k)=k$, $r_{\max}=2$, and no higher shadow survives.
Affine Kac--Moody lies in class~$L$: $\kappa(V_k(\fg))=\dim(\fg)(k+h^\vee)/(2h^\vee)$, $r_{\max}=3$, and the first higher shadow is the cubic Lie-bracket class.
The $\beta\gamma$ system lies in class~$C$: $\kappa(\beta\gamma_\lambda)=6\lambda^2-6\lambda+1$, $r_{\max}=4$, and the quartic contact shadow is the first genuinely new witness.
Virasoro and the finite-type $\mathcal{W}$-algebras lie in class~$M$: $\kappa(\mathrm{Vir}_c)=c/2$, $r_{\max}=\infty$, and the cubic/quartic shadows do not terminate.
At the
critical level $k=-h^\vee$ the Sugawara construction is undefined,
Theorem~H fails, and the Feigin--Frenkel centre
$\operatorname{Fun}(\operatorname{Op}_{{}^L\fg})$ makes
$\ChirHoch^\bullet$ unbounded (Feigin--Frenkel stratum~$FF$). The

rationale:
Restore the requested G/L/C/M cadence and make each family carry both its canonical `\kappa` datum and its shadow-depth witness.

AP anchor:
AP113, AP289
```

### Prescription 5: seven-theorem block

```text
old_string:
\medskip\noindent\textbf{From climax to seven theorems.}
The seven theorems are corollaries of (G1)+(G2)+Quadrichotomy and the
Maurer--Cartan element $\Theta_\cA$ they generate. They are:

\medskip\noindent\textbf{The forced chain A $\Rightarrow$ B $\Rightarrow$ C $\Rightarrow$ D $\Rightarrow$ H.}
Without Theorem~A, the dual object is only a formal symbol: there is
no theorem identifying
$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ with a chiral algebra.
Without Theorem~B, the bar construction can lose the boundary algebra.
Without Theorem~C, higher-genus deformation theory has no canonical
polarization. Without Theorem~D, the genus tower has no distinguished
scalar shadow. Without Theorem~H, the bulk coefficient ring is
uncontrolled. The unique survivor of all five failures is the
genus-completed bar differential, first in the ordered $E_1$ theory and
then in its $\Sigma_n$-coinvariant shadow.

Theorem~A identifies the homotopy Koszul dual on the quadratic Koszul
lane: for a chiral Koszul pair, the unit and counit are
quasi-isomorphisms and Verdier duality exchanges the two members of the
pair. Theorem~B shows that the bar-cobar transform is faithful on the
Koszul locus: genus~$0$ is unconditional, while the genus-$g \ge 1$
inversion is proved on the modular pre-Koszul lane and is unconditional
on the standard CFT-type landscape except integer-spin $\beta\gamma$.
Once both sides are present, Theorem~C forces the Verdier decomposition
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$ of the ambient complex;
the Lagrangian splitting is proved, while the ambient
shifted-symplectic upgrade remains conditional on perfectness and
nondegeneracy. Tracing the same object yields Theorem~D: on the
uniform-weight modular Koszul lane,
$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ \textup{(UNIFORM-WEIGHT)} at all genera and the free
energies are the $\hat A$-series; at genus~$1$ this scalar statement is
\textup{(unconditional at $g=1$)} for every family, while at genus $g \ge 2$ multi-weight
algebras acquire the explicit cross-channel term
$\delta F_g^{\mathrm{cross}}$. Theorem~H identifies the coefficient
ring of the same universal class: on the Koszul locus,
$\ChirHoch^n(\cA) = 0$ for $n \notin \{0,1,2\}$ and
\[
P_\cA(t)
=
\dim Z(\cA)
+ \dim \ChirHoch^1(\cA)\, t
+ \dim Z(\cA^!)\, t^2.
\]
For Heisenberg this gives $P(t) = 1+t+t^2$; for generic Virasoro and
principal $\mathcal{W}$-algebras it gives $P(t) = 1+t^2$; for generic
affine Kac--Moody one has
$\ChirHoch^1(V_k(\mathfrak g)) \cong \mathfrak g$, so the coefficient
ring is still polynomial but need not be four-dimensional.

\medskip\noindent
All five theorems are $\Sigma_n$-coinvariant projections of a single
$E_1$ object.
The ordered bar differential $D_\cA^{\Eone}$ on
$\barB^{\mathrm{ord}}(\cA)$ defines
$\Theta_\cA^{\Eone} := D_\cA^{\Eone} - d_\cA^{(0)}
\in \MC({\gAmod}^{\Eone})$
(Theorem~\ref{thm:e1-mc-element}); since
$(D_\cA^{\Eone})^2 = 0$, the MC equation
$d\Theta_\cA^{\Eone} + \tfrac{1}{2}[\Theta_\cA^{\Eone}, \Theta_\cA^{\Eone}] = 0$
is automatic. Averaging into~$\gAmod$ produces the modular
Maurer--Cartan element $\Theta_\cA$ of
Theorem~\ref{thm:mc2-bar-intrinsic}. The binary ordered projection of
$\Theta_\cA^{\Eone}$ is the collision residue $r_\cA(z)$, and
$\operatorname{av}(r_\cA(z)) = \kappa_{\mathrm{dp}}(\cA)$, the
double-pole component of the modular characteristic; for non-abelian
affine Kac--Moody the full modular characteristic carries an
additive $\dim(\fg)/2$ from the Sugawara shift (simple-pole
self-contraction through the adjoint Casimir), giving
$\kappa(\cA) = \operatorname{av}(r_\cA(z)) + \dim(\fg)/2$, whereas
for abelian and scalar families
$\kappa(\cA) = \operatorname{av}(r_\cA(z))$ without shift. The seven
theorems characterise seven structural properties of this
projection.
\emph{Existence}: Theorem~A identifies the duality arena at
$(\infty,2)$-properad level.
\emph{Faithfulness}: Theorem~B reconstructs~$\cA$ from its bar data
on the Koszul lane at all genera via Positselski's periodic CDG
filtration.
\emph{Decomposition}: Theorem~C polarizes the genus-$g$ ambient
complex as a $-(3g{-}3)$-shifted symplectic pair with Lagrangian
section.
\emph{Leading coefficient}: Theorem~D extracts the scalar shadow
$\kappa(\cA)$ and closes the all-genera UNIFORM-WEIGHT universality
via Graber--Vakil.
\emph{Coefficient ring}: Theorem~H identifies the polynomial
coefficient ring over which~$\Theta_\cA$ varies, with universal
$\Ethree$-algebra structure.
\emph{Holography}: Theorem~F lifts the bar-cobar pair
$(\cA,\cA^{!}_\infty)$ to the bulk-boundary pair of a 3d
holomorphic-topological QFT via the functor~$\Phihol$.
\emph{Classification}: Theorem~G establishes that the five-slot
fingerprint $\phi(\cA)$ is a complete invariant on the standard
landscape, with critical stratum $FF$ completing the classification.

new_string:
\medskip\noindent\textbf{From climax to seven theorems.}
Seven theorems extract the structural content of the ordered bar.

\medskip\noindent
Theorem~A is load-bearing in two lanes: the chain-level bar-cobar
adjunction with universal twisting morphism and Verdier-intertwined
counit witness, and the factorization-$\infty$ adjunction on
$\operatorname{Ran}(X)$ with $R$-twisted $\Sigma_n$-descent. The
fixed-curve readout of these two lanes is proved; the separate
relative-boundary modular-family extension remains a downstream scope
surface rather than part of the Climax readout.

Theorem~B proves bar-cobar inversion in ambient-qualified form:
$\Omega_X(\barB_X(\cA))\xrightarrow{\sim}\cA$ on the Koszul locus, and off
that strict lane the explicit weight-completed chiral
CDG-coalgebra $\widehat{\barB}^{\mathrm{ch}}(\cA)$ carries the
coderived Positselski equivalence. In class~$M$ the raw direct-sum bar
complex fails on the nose, so the restored statement there is
pro-object / $J$-adic / filtered weight-completed, not raw direct sum.

Theorem~C decomposes the derived chiral centre
$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)
= R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
into complementary halves controlled by~$\cA$ and~$\cA^!$; this
proved C0/C1 core is distinct from the shifted-symplectic C2 upgrade,
which stays conditional off the verified Heisenberg and affine
perfectness surface. On the enumerated families the scalar Verdier
sums are exactly $0$, $13$, $250/3$, and $98/3$.

Theorem~D identifies the universal genus-$1$ scalar shadow for every
family and the all-weight genus tower
$F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}
+\delta F_g^{\mathrm{cross}}(\cA)$
\textup{(ALL-WEIGHT $+\delta F_g^{\mathrm{cross}}$)}; on the
uniform-weight lane the correction vanishes and one recovers
$\mathrm{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g$ with
$\lambda_g=c_g(\mathbb{E})$. The clutching/socle route is now
separated cleanly: it supplies a proof route for the scalar lane and
leaves only Conjecture~\ref{conj:F6-lambda-g-clutching-uniqueness} as
the residual lift problem at $g\ge3$, not as a hypothesis of
Theorem~D.

Theorem~H proves that the \emph{chiral} Hochschild complex, distinct
from topological and categorical Hochschild theories, is concentrated
in degrees $\{0,1,2\}$ on the Koszul/generic proved surface with a
family-dependent Hilbert polynomial of degree at most~$2$; at critical
affine level $k=-h^\vee$ and at non-generic class~$M$ parameters the
theorem does not apply. The Swiss-cheese structure lives on the pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)$; the bar coalgebra itself
remains an $E_1$-coalgebra.

Theorem~F defines the universal holography functor on the chirally
Koszul boundary-Lagrangian locus
$\Phihol\colon\ChirAlg^{\omega,\mathrm{BL}}_X
\longrightarrow\HTQFT_{X\times\bR}$,
$\cA\mapsto
(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)\rightsquigarrow(\cA,\cA^{!}_\infty))$,
sending the bar-cobar pair of a conilpotent boundary-Lagrangian chiral
algebra to the bulk-boundary pair of the reconstructed
holomorphic-topological QFT; the Drinfeld double is its image.

Theorem~G establishes the completeness of the five-slot fingerprint
$\phi(\cA) = (p_{\max},\,r_{\max},\,\chi_{\mathrm{VOA}},\,
n_{\mathrm{strong}},\,\mathrm{coset})$ on the standard landscape:
$\phi(\cA_1)=\phi(\cA_2)$ if and only if
$\barB^{\mathrm{ch}}(\cA_1)\cong\barB^{\mathrm{ch}}(\cA_2)$ as
$\mathrm{Ass}^{\mathrm{ch}}$-coalgebras and
$\cA_1^{!}\cong\cA_2^{!}$; the quadrichotomy $G/L/C/M$ is the coarse
projection on the locus $\kch\ne 0$, with the critical-level
companion stratum $FF$ completing the classification on the full
standard landscape.

All seven theorems are read from the same primitive object.
The ordered bar differential $D_\cA^{\Eone}$ on
$\barB^{\mathrm{ord}}(\cA)$ defines the ordered Maurer--Cartan element
$\Theta_\cA^{\Eone}$, and averaging into~$\gAmod$ produces the modular
Maurer--Cartan element $\Theta_\cA$. The binary ordered projection is
the collision residue $r_\cA(z)$; its averaged image is the degree-$2$
shadow, with the affine Sugawara shift added only on the non-abelian
Kac--Moody lane. Theorems~A/B/C/D/H/F/G are therefore not seven
independent slogans but seven readouts of one ordered bar package.

rationale:
Promote A/B/C/D/H/F/G to the strongest honest introduction-level form, recover the two-lane theorem A surface, insert the family-dependent theorem C constants, preserve the all-weight/uniform-weight theorem D split, and stop treating F/G as mere architectural slogans.

AP anchor:
Pattern 269, AP270, AP275, AP289
```

### Prescription 6: bridge paragraph

```text
old_string:
\item \emph{Outlook and Volume~II bridge}.
 $\Eone$-chiral bar on $\FM_k(\C) \times \operatorname{Conf}_k(\R)$;
 $\SCchtop$ on the derived center pair; curved at
 $g \geq 1$; homotopy-Koszulity of
 $\mathrm{SC}^{\mathrm{ch,top}}$; the bulk/boundary/line triangle
 that propagates $\Theta_\cA$ to Volume~II and Volume~III.
\end{enumerate}

Thirty-two chapters, one protagonist. The seven theorems
A/B/C/D/H/F/G and the five depth classes $G/L/C/M/FF$ mark its
landmarks, together with the bell theorem on the non-degenerate
locus $\{\kch\ne 0, \text{non-critical level}, \text{Koszul locus}\}$;
the remainder test, project, and extend the protagonist. Volume~I
(this volume) constructs the ordered bar and proves the seven
theorems; Volume~II lifts to the holomorphic-topological Swiss-cheese
operad $\SCchtop$ and to 3d quantum gravity at the $\cW_\infty$
level; Volume~III constructs the Calabi--Yau-to-chiral functor
$\Phicy$; Volume~IV inscribes the HEAL and UPGRADE theorems with
complete independent-verification coverage across the four volumes.

new_string:
\item \emph{Outlook and Volume~II bridge}.
 Volume~II adds the open/closed holomorphic-topological lift of the ordered bar through
 $\SCchtop$ on the chirally Koszul boundary-Lagrangian locus:
 the pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)$ carries the
 Swiss-cheese structure, and after the named boundary obstruction
 vanishes the topologized bulk reaches the $E_3^{\mathrm{top}}$ lane.
 The affine non-critical Sugawara case is proved; the general
 Virasoro/$\cW$ lift and the $\cW_\infty$ quantum-gravity endpoint remain
 scope-qualified rather than global.
\end{enumerate}

Thirty-two chapters, one protagonist. The seven theorems
A/B/C/D/H/F/G and the five depth classes $G/L/C/M/FF$ mark its
landmarks, together with the bell theorem on the non-degenerate
locus $\{\kch\ne 0, \text{non-critical level}, \text{Koszul locus}\}$;
the remainder test, project, and extend the protagonist. Volume~I
(this volume) constructs the ordered bar and proves the seven
theorems; Volume~II supplies the open/closed holomorphic-topological
lift through $\SCchtop$ only on the named Koszul and
boundary-obstruction surfaces; Volume~III supplies the
Calabi--Yau-to-chiral functor $\Phicy$ on its verified $d\le 2$
surface and its scoped $d\ge 3$ frontier, not as a global comparison
theorem; Volume~IV inscribes the HEAL and UPGRADE theorems with
complete independent-verification coverage across the four volumes.

rationale:
The current bridge prose advertises Vol II and Vol III as global closures. The abstract and preface both require scoped bridges tied to the Koszul locus and named boundary obstructions.

AP anchor:
AP275, AP270, AP289
```

### Prescription 7: family-summary table correction

```text
old_string:
\textbf{Family} & $c$ & $\kappa$ & $K$ & $\Delta$ & \textbf{Archetype} \\ \hline
Heisenberg $\mathcal{H}_k$ & $1$ & $k$ & $2$ & $0$ & Gaussian, $@2$ \\[2pt]
Free fermion $\mathcal{F}$ & $\frac{1}{2}$ & $\frac{1}{4}$ & $0$ & $0$ & Gaussian, $@2$ \\[2pt]
$\widehat{\mathfrak{sl}}_2$ at level $k$ & $\frac{3k}{k+2}$ & $\frac{3(k+2)}{4}$ & $6$ & $(1-3x)(1+x)$ & Lie/tree, $@3$ \\[2pt]
$\beta\gamma$ & $2$ & $1$ & $0$ & $(1-3x)(1+x)$ & contact, $@4$ \\[2pt]
Virasoro $c$ & $c$ & $\frac{c}{2}$ & $26$ & $(1-3x)(1+x)$ & mixed, $\infty$ \\[2pt]

new_string:
\textbf{Family} & $c$ & $\kappa$ & $K$ & $\Delta$ & \textbf{Archetype} \\ \hline
Heisenberg $\mathcal{H}_k$ & $1$ & $k$ & $0$ & $0$ & Gaussian, $@2$ \\[2pt]
Free fermion $\mathcal{F}$ & $\frac{1}{2}$ & $\frac{1}{4}$ & $0$ & $0$ & Gaussian, $@2$ \\[2pt]
$\widehat{\mathfrak{sl}}_2$ at level $k$ & $\frac{3k}{k+2}$ & $\frac{3(k+2)}{4}$ & $6$ & $(1-3x)(1+x)$ & Lie/tree, $@3$ \\[2pt]
$\beta\gamma_{\lambda=1}$ & $2$ & $1$ & $0$ & $(1-3x)(1+x)$ & contact, $@4$ \\[2pt]
Virasoro $c$ & $c$ & $\frac{c}{2}$ & $26$ & $(1-3x)(1+x)$ & mixed, $\infty$ \\[2pt]

rationale:
`K=2` for Heisenberg contradicts the canonical complementarity table (`landscape_census.tex:1747-1749`), and the unlabelled `\beta\gamma` row silently specializes to `\lambda=1`.

AP anchor:
AP113, AP289
```

## 8. AP293-positive deliverable

Concrete mathematical upgrade enabled by these prescriptions:

- the introduction can become an honest theorem-level read-back of the ordered bar package itself, rather than a mix of theorem slogans and architectural advertising. Concretely, after the repairs the reader will already know at introduction level that the ordered bar is primitive, the symmetric bar is its `\Sigma_n`-coinvariant shadow, theorem C carries the exact family-dependent complementarity constants `0,13,250/3,98/3`, theorem D splits into all-weight plus uniform-weight lanes, and the Vol II/III bridge is only asserted on the verified Koszul/boundary-obstruction surface.

This is AP293-positive because it is a mathematical strengthening of the introduction's load-bearing theorem surface, not a bookkeeping rewording.

## 9. Convergence (a)-(g) per AP306

- `(a)` materially stronger than baseline: `yes` for the audit deliverable. The file isolates exact replacement surfaces and identifies one concrete numerical mismatch (`Heisenberg K=2` at `introduction.tex:2342`) and one explicit missing family formula (`\kappa(\beta\gamma_\lambda)` absent).
- `(b)` no unresolved obstruction in the stated scope: `no`. The opening, derivation spine, theorem block, E1-primacy paragraph, family cadence, and Vol II/III bridges all still require manuscript repair.
- `(c)` hostile-reviewer robust under re-attack: `not yet`. The audit is evidence-complete, but the manuscript surface has not been healed and re-attacked.
- `(d)` every numerical claim verified by `>=3` independent paths: `no` at the introduction surface. This pass cross-checked against the canonical landscape tables and internal theorem surfaces, but the introduction itself still omits or miscites family data.
- `(e)` every scope qualifier paired with boundary-obstruction content: `no`. This is the main failure on Theorems A/F/G and on the Vol II/III bridge paragraphs.
- `(f)` strongest honest form, never downgraded: `no`. The introduction still carries weaker older slogans beside stronger later theorem surfaces, and F/G remain below theorem level.
- `(g)` AP293-negative satisfied: `yes` for the audit artifact. The report contains a falsifying witness (`introduction.tex:2342` versus `landscape_census.tex:1747-1749`), a structural contradiction witness (`introduction.tex:366-375` versus `1338-1359`), and exact replacement blocks that sharpen the theorem surface.

Convergence verdict: `not converged`. The next honest state is: apply the prescriptions in Vol I, then run a hostile re-attack focused on the repaired theorem block and the final bridge paragraph.
