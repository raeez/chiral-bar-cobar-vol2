"""Independent checks for the Khan--Zeng BV core and conditional recursion."""

from __future__ import annotations

from fractions import Fraction

from compute.lib.independent_verification import independent_verification


def _sl2_structure_constants():
    """Structure constants for [h,e]=2e, [h,f]=-2f, [e,f]=h."""
    basis = {"h": 0, "e": 1, "f": 2}
    constants = {}

    def set_bracket(a, b, terms):
        ia, ib = basis[a], basis[b]
        for c, coeff in terms.items():
            constants[(ia, ib, basis[c])] = coeff
            constants[(ib, ia, basis[c])] = -coeff

    set_bracket("h", "e", {"e": 2})
    set_bracket("h", "f", {"f": -2})
    set_bracket("e", "f", {"h": 1})
    return constants, range(3)


def _c(constants, a, b, c):
    return constants.get((a, b, c), 0)


@independent_verification(
    claim="lem:kz-cme-pva-jacobi",
    derived_from=[
        "Vol II KZ shifted-cotangent BV action: CME is variational Schouten square",
    ],
    verified_against=[
        "Finite-dimensional Lie-Poisson affine PVA: Schouten square reduces to ordinary Lie algebra Jacobi",
    ],
    disjoint_rationale=(
        "The manuscript proof uses the De Sole--Kac Hamiltonian-operator "
        "dictionary. This test checks the affine Lie-Poisson specialization "
        "directly from structure constants, without using the variational "
        "PVA formalism."
    ),
)
def test_affine_lie_pva_cme_reduces_to_jacobi():
    constants, indices = _sl2_structure_constants()
    for a in indices:
        for b in indices:
            for c in indices:
                for d in indices:
                    jacobiator = sum(
                        _c(constants, a, b, e) * _c(constants, e, c, d)
                        + _c(constants, b, c, e) * _c(constants, e, a, d)
                        + _c(constants, c, a, e) * _c(constants, e, b, d)
                        for e in indices
                    )
                    assert jacobiator == 0


def _mat_vec(matrix, vector):
    return [
        sum(matrix[row][col] * vector[col] for col in range(len(vector)))
        for row in range(len(matrix))
    ]


def _add(u, v):
    return [a + b for a, b in zip(u, v)]


def _scale(s, v):
    return [s * x for x in v]


@independent_verification(
    claim="thm:doubling-rwi",
    derived_from=[
        "Vol II image-choice reflected propagator formula with field-parity signs",
    ],
    verified_against=[
        "Elementary expansion of a product of ordinary-plus-image edge kernels",
    ],
    disjoint_rationale=(
        "The manuscript proof uses logarithmic FM/raviolo Stokes. This "
        "test checks the separate combinatorial convention: every edge "
        "contributes an ordinary term plus an image term, with odd or "
        "Dirichlet parity represented by the coefficient -1 rather than by "
        "removing the image summand."
    ),
)
def test_reflected_kernel_keeps_signed_image_summand():
    # Each edge contributes K^- + epsilon K^+.  The image branch exists
    # even when epsilon=-1; the sign is the coefficient.
    epsilons = [1, -1, 1]
    terms = [((), 1)]
    for edge_index, epsilon in enumerate(epsilons):
        expanded = []
        for choices, coeff in terms:
            expanded.append((choices + (("ordinary", edge_index),), coeff))
            expanded.append((choices + (("image", edge_index),), coeff * epsilon))
        terms = expanded

    assert len(terms) == 2 ** len(epsilons)
    odd_image_terms = [
        coeff
        for choices, coeff in terms
        if ("image", 1) in choices
        and all(
            choice[0] == "ordinary"
            for choice in choices
            if choice[1] != 1
        )
    ]
    assert odd_image_terms == [-1]


@independent_verification(
    claim="prop:kz-all-loop-counterterm-recursion",
    derived_from=[
        "Vol II recursion I_l=-h Ob_l in a finite jet-weight quotient",
    ],
    verified_against=[
        "Elementary SDR identity id-H=d h+h d on a two-term acyclic complex",
    ],
    disjoint_rationale=(
        "The manuscript proof constructs the finite-quotient recursion in "
        "the half-space BV algebra under the KZ analytic SDR package. This "
        "test checks the algebraic heart of the conditional recursion in an "
        "independent finite-dimensional SDR."
    ),
)
def test_counterterm_recursion_solves_finite_qme_obstruction():
    d = [[0, 0], [1, 0]]
    h = [[0, 1], [0, 0]]
    harmonic = [[0, 0], [0, 0]]
    identity = [[1, 0], [0, 1]]

    dh_plus_hd = [
        [
            sum(d[i][k] * h[k][j] for k in range(2))
            + sum(h[i][k] * d[k][j] for k in range(2))
            for j in range(2)
        ]
        for i in range(2)
    ]
    assert dh_plus_hd == [
        [identity[i][j] - harmonic[i][j] for j in range(2)]
        for i in range(2)
    ]

    obstruction = [0, 1]
    assert _mat_vec(d, obstruction) == [0, 0]
    assert _mat_vec(harmonic, obstruction) == [0, 0]

    counterterm = _scale(-1, _mat_vec(h, obstruction))
    assert _add(_mat_vec(d, counterterm), obstruction) == [0, 0]


@independent_verification(
    claim="assum:kz-analytic-sdr-package",
    derived_from=[
        "Vol II KZ analytic SDR package with side conditions",
    ],
    verified_against=[
        "A three-dimensional special deformation retract with one harmonic class and one acyclic pair",
    ],
    disjoint_rationale=(
        "The manuscript isolates the analytic SDR package as a named "
        "hypothesis for the nonlinear finite-jet PVA lane. This test checks "
        "the algebraic side conditions and the requirement that the "
        "obstruction lie in the zero-harmonic sector."
    ),
)
def test_sdr_package_side_conditions_with_harmonic_projection():
    # Basis h0, e0, e1 with d(e0)=e1, H projects to h0, h(e1)=e0.
    d = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
    h = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
    harmonic = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def matmul(a, b):
        size = len(a)
        return [
            [
                sum(a[i][k] * b[k][j] for k in range(size))
                for j in range(size)
            ]
            for i in range(size)
        ]

    dh_plus_hd = [
        [
            sum(d[i][k] * h[k][j] for k in range(3))
            + sum(h[i][k] * d[k][j] for k in range(3))
            for j in range(3)
        ]
        for i in range(3)
    ]
    assert dh_plus_hd == [
        [identity[i][j] - harmonic[i][j] for j in range(3)]
        for i in range(3)
    ]
    assert matmul(h, harmonic) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert matmul(harmonic, h) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert matmul(h, h) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    obstruction = [0, 0, 1]
    assert _mat_vec(d, obstruction) == [0, 0, 0]
    assert _mat_vec(harmonic, obstruction) == [0, 0, 0]


@independent_verification(
    claim="thm:general-half-space-bv",
    derived_from=[
        "Vol II reflected half-space propagator and doubling theorem",
        "Vol II all-loop counterterm recursion in finite jet-weight quotients",
        "Khan-Zeng Poisson-vertex sigma-model input for finite-type PVAs",
    ],
    verified_against=[
        "Equivariant formality principle: restrict the doubled whole-space "
        "complex to the sigma-invariant sector by the averaging projector",
    ],
    disjoint_rationale=(
        "The conditional theorem uses reflected logarithmic weights plus "
        "the finite-quotient QME recursion. This test checks the independent "
        "homological algebra behind the doubling comparison: the averaging "
        "projector onto sigma-invariants is idempotent and commutes with a "
        "sigma-equivariant BV differential, so the half-space complex is a "
        "subcomplex of the doubled whole-space complex before graph weights "
        "are inserted."
    ),
)
def test_doubling_projector_is_a_chain_projection():
    """A sigma-equivariant doubled BV complex restricts to invariants."""
    # Two original/image field pairs. Sigma swaps the two halves.
    sigma = [
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
    ]
    identity = [
        [Fraction(int(i == j)) for j in range(4)]
        for i in range(4)
    ]
    projector = [
        [(identity[i][j] + sigma[i][j]) / 2 for j in range(4)]
        for i in range(4)
    ]
    # A sigma-equivariant differential: two identical acyclic two-term
    # complexes on original and image fields.
    d = [
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
    ]

    def matmul(a, b):
        return [
            [
                sum(a[i][k] * b[k][j] for k in range(4))
                for j in range(4)
            ]
            for i in range(4)
        ]

    assert matmul(projector, projector) == projector
    assert matmul(projector, d) == matmul(d, projector)
