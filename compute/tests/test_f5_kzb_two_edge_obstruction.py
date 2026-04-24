"""Exact witnesses for the KZB two-edge corner obstruction."""

from __future__ import annotations

from fractions import Fraction

from compute.lib.independent_verification import independent_verification


Matrix = list[list[Fraction]]
Vector = list[Fraction]


def _zero(n: int, m: int) -> Matrix:
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def _eye(n: int) -> Matrix:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def _add(a: Matrix, b: Matrix, scale: Fraction = Fraction(1)) -> Matrix:
    return [
        [a[i][j] + scale * b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def _mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def _commutator(a: Matrix, b: Matrix) -> Matrix:
    return _add(_mul(a, b), _mul(b, a), Fraction(-1))


def _kron(a: Matrix, b: Matrix) -> Matrix:
    return [
        [a[i][j] * b[k][ell] for j in range(len(a[0])) for ell in range(len(b[0]))]
        for i in range(len(a))
        for k in range(len(b))
    ]


def _mat_vec(a: Matrix, v: Vector) -> Vector:
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def _operator_on_positions(first: Matrix, i: int, second: Matrix, j: int) -> Matrix:
    factors = []
    for pos in range(3):
        if pos == i:
            factors.append(first)
        elif pos == j:
            factors.append(second)
        else:
            factors.append(_eye(2))

    out = factors[0]
    for factor in factors[1:]:
        out = _kron(out, factor)
    return out


def _sl2_casimir() -> Matrix:
    e = [[Fraction(0), Fraction(1)], [Fraction(0), Fraction(0)]]
    f = [[Fraction(0), Fraction(0)], [Fraction(1), Fraction(0)]]
    h = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]

    omega = _zero(4, 4)
    omega = _add(omega, _kron(e, f), Fraction(1, 2))
    omega = _add(omega, _kron(f, e), Fraction(1, 2))
    omega = _add(omega, _kron(h, h), Fraction(1, 4))
    return omega


def _sl2_casimir_13() -> Matrix:
    e = [[Fraction(0), Fraction(1)], [Fraction(0), Fraction(0)]]
    f = [[Fraction(0), Fraction(0)], [Fraction(1), Fraction(0)]]
    h = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]

    omega_13 = _zero(8, 8)
    omega_13 = _add(omega_13, _operator_on_positions(e, 0, f, 2), Fraction(1, 2))
    omega_13 = _add(omega_13, _operator_on_positions(f, 0, e, 2), Fraction(1, 2))
    omega_13 = _add(omega_13, _operator_on_positions(h, 0, h, 2), Fraction(1, 4))
    return omega_13


def _is_zero(a: Matrix) -> bool:
    return all(entry == 0 for row in a for entry in row)


@independent_verification(
    claim="prop:kzb-two-edge-corner-defect-nonzero",
    derived_from=[
        "Boundary KZB formal-type edge/corner reduction in curved_dunn_higher_genus.tex",
        "Getzler-Kapranov clutching obstruction formula",
    ],
    verified_against=[
        "Exact standard sl2 representation matrices",
        "Infinitesimal braid relation for the invariant Casimir",
    ],
    disjoint_rationale=(
        "The manuscript reduction supplies the obstruction shape. The test "
        "uses only the standard two-dimensional sl2 matrices and exact "
        "matrix multiplication to decide whether the adjacent-edge "
        "commutator vanishes."
    ),
)
def test_adjacent_two_edge_defect_nonzero_and_mixed_channel_cancels():
    omega = _sl2_casimir()
    omega_12 = _kron(omega, _eye(2))
    omega_23 = _kron(_eye(2), omega)
    omega_13 = _sl2_casimir_13()

    raw_defect = _commutator(omega_12, omega_23)
    assert not _is_zero(raw_defect)

    # Basis order is +++, ++-, +-+, +--, -++, -+-, --+, ---.
    vector_plus_minus_plus = [Fraction(0)] * 8
    vector_plus_minus_plus[2] = Fraction(1)
    expected = [Fraction(0)] * 8
    expected[1] = Fraction(1, 4)
    expected[4] = Fraction(-1, 4)
    assert _mat_vec(raw_defect, vector_plus_minus_plus) == expected

    mixed_channel_cancellation = _commutator(omega_12, _add(omega_13, omega_23))
    assert _is_zero(mixed_channel_cancellation)
    assert raw_defect == _add(_zero(8, 8), _commutator(omega_12, omega_13), Fraction(-1))

