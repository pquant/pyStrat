from dataclasses import dataclass
from enum import Enum


class Ccy(Enum):
    USD = 0
    EUR = 1
    GBP = 2
    CHF = 3


@dataclass(frozen=True)
class CcyPair:
    lhs: Ccy
    rhs: Ccy

    def __post_init__(self):
        assert self.lhs != self.rhs

    def __iter__(self):
        yield [self.lhs, self.rhs]

    def __repr__(self):
        return 'f{self.lhs}{self.rhs}'

    def is_USD_cross(self):
        return self.lhs is Ccy.USD or self.rhs is Ccy.USD
