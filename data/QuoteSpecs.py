from enum import Enum


class Side(Enum):
    Bid = 0
    Ask = 1
    Mid = 2


class Metric(Enum):
    Open = 0
    Close = 1
    Low = 2
    High = 3
