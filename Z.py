from data.ccy import *
import Source
from data.snap.fx.spot import get_fx_spot_series

import matplotlib.pyplot as pyplot
from datetime import date

if __name__ == '__main__':

    ccy_pair = CcyPair(Ccy.EUR, Ccy.USD)
    src = Source.Quandl('e9JqdpNvY711i8FKYywP')

    series_df = get_fx_spot_series(
        ccy_pair,
        start=date(1970, 1, 1),
        end=date(1970, 1, 10),
    )

    pyplot.plot(series_df)  # type: ignore
    pyplot.show()  # type: ignore
