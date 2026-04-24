"""F6 scalar projection versus multichannel socle lift."""

from __future__ import annotations

from fractions import Fraction

from compute.lib.independent_verification import independent_verification


LAMBDA_3_FP = Fraction(31, 967680)


def _scalar_projection(vector: tuple[Fraction, ...]) -> Fraction:
    return sum(vector, Fraction(0))


@independent_verification(
    claim="prop:f6-scalar-projection-no-multichannel-lift",
    derived_from=[
        "F6 scalar residue proposition in programme_climax_platonic.tex",
        "Uniform-weight planted-forest scalar projection",
    ],
    verified_against=[
        "Kernel computation for the projection Q^2 -> Q",
        "Exact two-channel rational linear algebra",
    ],
    disjoint_rationale=(
        "The scalar residue fixes the value after projection. The test "
        "checks the independent linear-algebra question of whether that "
        "projected value determines a vector in a two-channel socle."
    ),
)
def test_f6_scalar_projection_does_not_determine_two_channel_socle_lift():
    first_channel = (LAMBDA_3_FP, Fraction(0))
    second_channel = (Fraction(0), LAMBDA_3_FP)

    assert _scalar_projection(first_channel) == LAMBDA_3_FP
    assert _scalar_projection(second_channel) == LAMBDA_3_FP
    assert first_channel != second_channel

    kernel_difference = (
        first_channel[0] - second_channel[0],
        first_channel[1] - second_channel[1],
    )
    assert kernel_difference != (Fraction(0), Fraction(0))
    assert _scalar_projection(kernel_difference) == 0

