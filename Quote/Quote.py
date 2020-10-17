"""
Interface for retrieving market quotess
"""

from abc import ABCMeta, abstractmethod
from collections import namedtuple
from Fix import Fix
from pandas import DataFrame
"""
A Ticker named tuple to store label to query source. Also contains a Bool to be used in case resulting data needs to be
inverted - e.g. JPYUSD instead of USDJPY. Most of the time though, it won't be necessary, so defaults to None
"""
Ticker = namedtuple('Ticker', 'name inverted')


class QuoteInterface(metaclass=ABCMeta):
    """
    Defines methods that need to be implemented for a chosen combination of (asset, market, source)
    """
    @abstractmethod
    def __init__(self, asset, market, source):
        """
        Constructor for any class implementing QuoteInterface.
        Expects an asset type (see Asset.py), a market type (see Market.py), and a source type (see Source.py)

        :param asset: e.g. :class:`pyStrat.Asset.Pair`
        :param market: e.g. :class:`pyStrat.Market.Spot`
        :param source: e.g. :class:`pyStrat.Source.Quandl`
        :return: An instance of the class that implements the QuoteInterface
        """
        pass

    @abstractmethod
    def tickers(self) -> [Ticker]:
        """
        Returns the list of tickers (because we might need more than 1) required to query source.
        Example: EURJPY should break down into EURUSD and USDJPY rather than fetch data from a source for EURJPY.
        There are two reason for that : the source might not have it, while it's much more likely to have the USD crosses, and above
        all, it might not be consistent with EURUSD and USDJPY.

        :return: [Ticker]
        """
        pass

    @abstractmethod
    # def series(self, start, end, bid_ask='MID', fix=Fix.close()):
    def series(self,
               start: str,
               end: str,
               fix: Fix = Fix.close(),
               bid_ask: str = 'MID') -> DataFrame:
        """
        TODO : doc and annotations

        :param start:
        :param end:
        :param fix:
        :param bid_ask:
        :return:
        """
        pass
