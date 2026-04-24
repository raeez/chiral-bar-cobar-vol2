"""Independent checks for the Khan--Zeng BV core and SDR recursion."""

from __future__ import annotations

from compute.lib.independent_verification import independent_verification


def _sl2_structure_constants():
    """Structure constants for [h,e]=2e, [h,f]=-2f, [e,f]=h."""
    basis = {"h": 0, "e": 1, "f": 2}
    f = {}

    def set_bracket(a, b, terms):
        ia, ib = basis[a], basis[b]
        for c, coeff in terms.items():
            f[(ia, ib, basis[c])] = coeff
            f[(ib, ia, basis[c])] = -coeff

    set_bracket("h", "e", {"e": 2})
    set_bracket("h", "f", {"f": -2})
    set_bracket("e", "f", {"h": 1})
    return f, range(3)


def _c(f, a, b, c):
    return f.get((a, b, c), 0)


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
    f, indices = _sl2_structure_constants()
    for a in indices:
        for b in indices:
            for c in indices:
                for d in indices:
                    jac = sum(
                        _c(f, a, b, e) * _c(f, e, c, d)
                        + _c(f, b, c, e) * _c(f, e, a, d)
                        + _c(f, c, a, e) * _c(f, e, b, d)
                        for e in indices
                    )
                    assert jac == 0


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
    claim="prop:kz-all-loop-counterterm-recursion",
    derived_from=[
        "Vol II recursion I_l=-h Ob_l in a finite jet-weight quotient",
    ],
    verified_against=[
        "Elementary SDR identity id-H=d h+h d on a two-term acyclic complex",
    ],
    disjoint_rationale=(
        "The manuscript proof assumes a finite-quotient analytic SDR package. "
        "This test checks only the algebraic heart of the conditional "
        "recursion in an independent finite-dimensional SDR."
    ),
)
def test_counterterm_recursion_solves_finite_qme_obstruction():
    # Basis e0, e1 with d(e0)=e1 and h(e1)=e0.
    d = [[0, 0], [1, 0]]
    h = [[0, 1], [0, 0]]
    H = [[0, 0], [0, 0]]
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
        [identity[i][j] - H[i][j] for j in range(2)]
        for i in range(2)
    ]

    obstruction = [0, 1]
    assert _mat_vec(d, obstruction) == [0, 0]
    assert _mat_vec(H, obstruction) == [0, 0]

    counterterm = _scale(-1, _mat_vec(h, obstruction))
    assert _add(_mat_vec(d, counterterm), obstruction) == [0, 0]
