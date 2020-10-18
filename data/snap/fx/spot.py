from datetime import date, datetime
from typing import Dict
import Quandl
from pandas import Series

from data.fx.ccy import *
from data.QuoteSpecs import Metric
from Source import Source
import Source


def get_fx_spot_series(
        ccy_pair: CcyPair,
        start: date,
        end: date,
        #tz: str,
        metrics: [Metric],
        src: Source) -> Dict[Metric, Series]:

    if type(src) == Source.Quandl:

        metric, *rest = metrics

        if rest or metric != Metric.Close:
            raise ValueError(
                f'can only handle {Metric.Close} for Quandl. Got: {metrics}')

        return Quandl.get(Source.Quandl.quandl_code(ccy_pair),
                          start_date=start.strftime('%Y-%m-%d'),
                          end_date=end.strftime('%Y-%m-%d'))
