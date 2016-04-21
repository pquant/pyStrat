"""
Interface for retrieving market quotess
"""

from abc import ABCMeta, abstractmethod
from collections import namedtuple
from Fix import Fix

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
        Constructor for any class implementing QuoteInterface. Expects an asset type, a market type, and a source type
        :param asset: e.g. Asset.Pair
        :param market: e.g. Market.Spot
        :param source: e.g. Source.YahooFinance
        :return: An instance of the class that implements the QuoteInterface
        """
        pass

    @abstractmethod
    def tickers(self) -> [Ticker]:
        """
        Tickers with an 's' because we might need more than 1.
        Example: EURJPY should break down into EURUSD and USDJPY rather than fetch data from a source for EURJPY.
        2 reason for that : the source might not have it, while it's much more likely to have the USD crosses, and above
        all, it might not be consistent with EURUSD and USDJPY.
        :return: a list of Tickers
        """
        pass

    @abstractmethod
    # def series(self, start, end, bid_ask='MID', fix=Fix.close()):
    def series(self, start, end, fix=Fix.close(), bid_ask='MID'):
        """
        TODO : doc and annotations
        :param start:
        :param end:
        :param fix:
        :param bid_ask:
        :return:
        """
        pass