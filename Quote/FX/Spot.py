"""
Quote base class implementations (see pyStrat.Quote.Quote.py
"""

import Quandl

import Asset
import Market
import Source
import Quote.Utils
import Quote.FX.Utils as FxUtils
from Quote.Quote import QuoteInterface, Ticker


class FXSpotQuandl(QuoteInterface):
    def __init__(self, asset, market, source):
        # cache asset, market, source
        self.asset, self.market, self.source = asset, market, source
        # Type checks
        Quote.Utils.check_quote_types(self, Asset.Pair, Market.Spot,
                                      Source.Quandl)

    def tickers(self):
        pairs = FxUtils.split_to_usd_crosses(self.asset)
        return [
            Ticker(Source.quandl_code(p), FxUtils.is_inverted(p))
            for p in pairs
        ]

    def series(self, start, end, fix, bid_ask):
        # FIXME : works for market convention USD crosses for now
        tckr, = self.tickers()
        return Quandl.get(tckr.name, start_date=start, end_date=end)

        # return Quandl.get(self.ticker(), start_date=start, end_date=end)


"""
List of registered classes
"""
QuoteInterface.register(FXSpotQuandl)
