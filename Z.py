from data.fx.ccy import *
import Market
import Source
from Fix import Fix
from Quote.FX.Spot import FXSpotQuandl

import matplotlib.pyplot as pyplot

if __name__ == '__main__':

    ccy_pair = CcyPair(Ccy.EUR, Ccy.USD)
    mkt = Market.Spot()
    src = Source.Quandl('e9JqdpNvY711i8FKYywP')

    pair_spot_quandl = FXSpotQuandl(asset, mkt, src)
    ticker = pair_spot_quandl.tickers()
    print('Spot Quandl ticker: {}'.format(tickers))

    series_df = pair_spot_quandl.series(start='1970-01-01',
                                        end='1970-01-10',
                                        fix=Fix.close(),
                                        bid_ask='MID')

    pyplot.plot(series_df)  # type: ignore
    pyplot.show()  # type: ignore
