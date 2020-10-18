from dataclasses import dataclass
import os
from pathlib import Path

from data.ccy import CcyPair
import Quote.FX.Utils as FxUtils


class Source:
    pass


@dataclass(frozen=True)
class CSV(Source):
    filepath: Path

    def __post_init(self):
        if not self.filepath.exists():
            ValueError("Input directory {} is invalid".format(repo))


@dataclass(frozen=True)
class Quandl(Source):
    authtoken: str

    @staticmethod
    def quandl_db(cls: type) -> str:
        # Name of the Quandl db associated with asset.
        # See 'Quandl Code' section of https://www.quandl.com/blog/getting-started-with-the-quandl-api
        if cls == CcyPair: return 'CUR'
        else:
            raise ValueError(f'no known Quandl DB for: {cls}')

    @staticmethod
    def quandl_code(obj: Any) -> str:

        if type(obj) == CcyPair:

            lhs, rhs = obj

            if not obj.is_USD_cross():
                raise ValueError(
                    f'Quandl only accepts USD crosses, got {lhs}/{rhs}')

            non_USD_ccy = rhs if lhs is Ccy.USD else lhs
            return f'{quandl_db(CcyPair)}/{non_usd_ccy}'
