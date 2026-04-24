"""Finite pole-envelope model for logarithmic triplet regular shadows.

This module does not compute the actual W(p) triplet shadow tower.  It
encodes the first finite regular-sector shadow model forced by the
guarded OPE pole constants:

    TT transition weight: 6.
    TW transition weight: 3(2p - 1).
    WW transition weight: 9(4p - 3).

The missing mathematical input is the factorisation of the real regular
TW/WW shadow sector through such a finite residue-state model.  Once
that hypothesis is supplied, the combinatorics below gives the required
exponential-polynomial bound and rejects factorial growth.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, lgamma, log

from compute.lib.logarithmic_wp_triplet_constants import (
    triplet_central_charge,
    tt_transition_weight,
    tw_transition_weight,
    ww_bar_pole_order,
    ww_transition_weight,
    zhu_dimension,
)


def catalan_number(n: int) -> int:
    """Return the nth Catalan number."""
    if n < 0:
        raise ValueError(f"Catalan index must be non-negative, got {n}")
    return comb(2 * n, n) // (n + 1)


@dataclass(frozen=True)
class ChannelWeights:
    """Local transition weights in the finite pole-envelope model."""

    p: int
    tt: int
    tw: int
    ww: int

    @property
    def no_ww(self) -> int:
        """Return the total transition weight with no WW collision."""
        return self.tt + self.tw

    @property
    def ambient(self) -> int:
        """Return the total transition weight allowing TT, TW, and WW."""
        return self.tt + self.tw + self.ww


def channel_weights(p: int) -> ChannelWeights:
    """Return the W(p) pole-envelope channel weights."""
    return ChannelWeights(
        p=p,
        tt=tt_transition_weight(),
        tw=tw_transition_weight(p),
        ww=ww_transition_weight(p),
    )


@dataclass(frozen=True)
class ExponentialPolynomialBound:
    """A bound C r^N R^r for a shadow sequence."""

    C: int
    N: int
    R: int

    def upper(self, r: int) -> int:
        """Return C r^N R^r exactly."""
        if r < 0:
            raise ValueError(f"arity must be non-negative, got {r}")
        return self.C * (r ** self.N) * (self.R ** r)

    def log_tempered_rate(self, r: int) -> float:
        """Return log((C r^N R^r / r!)^(1/r))."""
        if r < 2:
            raise ValueError(f"tempered rate requires r >= 2, got {r}")
        return (
            log(self.C)
            + self.N * log(r)
            + r * log(self.R)
            - lgamma(r + 1)
        ) / r

    def factorial_probe_violates(self, r: int, base: int = 1) -> bool:
        """Return True when base^r r! exceeds this bound at arity r."""
        if r < 2:
            raise ValueError(f"factorial probe requires r >= 2, got {r}")
        if base < 1:
            raise ValueError(f"factorial probe base must be positive, got {base}")
        probe_log = r * log(base) + lgamma(r + 1)
        bound_log = log(self.C) + self.N * log(r) + r * log(self.R)
        return probe_log > bound_log

    def first_factorial_violation(self, r_max: int, base: int = 1) -> int | None:
        """Return the first r <= r_max where base^r r! exceeds the bound."""
        for r in range(2, r_max + 1):
            if self.factorial_probe_violates(r, base=base):
                return r
        return None


@dataclass(frozen=True)
class FiniteRegularShadowModel:
    """Finite residue-state pole-envelope model for W(p).

    `residue_state_bound` is a hypothesis of the model, not a theorem
    about the actual triplet shadow sector.
    """

    p: int
    residue_state_bound: int
    polynomial_degree: int = 3

    def __post_init__(self) -> None:
        if self.p < 2:
            raise ValueError(f"triplet parameter p must be >= 2, got {self.p}")
        if self.residue_state_bound < 1:
            raise ValueError("residue_state_bound must be positive")
        if self.polynomial_degree < 0:
            raise ValueError("polynomial_degree must be non-negative")

    @property
    def central_charge(self):
        """Return c(p) for the model parameter."""
        return triplet_central_charge(self.p)

    @property
    def ww_bar_pole_order(self) -> int:
        """Return the guarded WW bar pole order 4p - 3."""
        return ww_bar_pole_order(self.p)

    @property
    def weights(self) -> ChannelWeights:
        """Return local channel weights."""
        return channel_weights(self.p)

    @classmethod
    def wp2_zhu_sized_pole_envelope(cls) -> "FiniteRegularShadowModel":
        """Return the W(2) pole-envelope model with four finite states."""
        return cls(p=2, residue_state_bound=zhu_dimension(2), polynomial_degree=3)


def finite_regular_shadow_bound(
    model: FiniteRegularShadowModel,
) -> ExponentialPolynomialBound:
    """Return C r^N R^r for the finite regular-sector model."""
    return ExponentialPolynomialBound(
        C=model.residue_state_bound,
        N=model.polynomial_degree,
        R=4 * model.weights.ambient,
    )


def regular_channel_envelopes(
    model: FiniteRegularShadowModel,
    r: int,
) -> dict[str, int]:
    """Return TW, WW, and non-Virasoro envelope values at arity r.

    The model uses the disjoint priority split:
      TW = at least one TW collision and no WW collision;
      WW = at least one WW collision.
    Their sum is the non-Virasoro regular envelope.
    """
    if r < 2:
        raise ValueError(f"shadow arity must be >= 2, got {r}")
    steps = r - 1
    weights = model.weights
    scale = (
        model.residue_state_bound
        * (r ** model.polynomial_degree)
        * catalan_number(steps)
    )
    tw = scale * ((weights.no_ww ** steps) - (weights.tt ** steps))
    ww = scale * ((weights.ambient ** steps) - (weights.no_ww ** steps))
    return {
        "TW": tw,
        "WW": ww,
        "nonvir": tw + ww,
    }


def finite_model_certificate(
    model: FiniteRegularShadowModel,
    r_values: range,
) -> dict[int, bool]:
    """Check the exponential-polynomial certificate on finite arities."""
    bound = finite_regular_shadow_bound(model)
    return {
        r: regular_channel_envelopes(model, r)["nonvir"] <= bound.upper(r)
        for r in r_values
    }
