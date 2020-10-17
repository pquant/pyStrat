from dataclasses import dataclass
from enum import Enum


class Ccy(Enum):
    USD = 0
    EUR=1
    GBP=2
    CHF=3


@dataclass(frozen=True)
class CcyPair:
    lhs: Ccy
    rhs: Ccy

