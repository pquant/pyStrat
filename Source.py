import os
import Asset
import Quote.FX.Utils as FxUtils


class CSV:
    def __init__(self, repo):
        if not os.path.isdir(repo):
            ValueError("Input directory {} is invalid".format(repo))
        self.repo = repo
        self.fileName = None


class Quandl:
    def __init__(self, authtoken):
        self.authtoken = authtoken


###################################################################################
# Quandl Utils
###################################################################################
def quandl_db(asset) -> str:
    """
    Name of the Quandl db associated with asset.
    See the 'Quandl Code' section of https://www.quandl.com/blog/getting-started-with-the-quandl-api
    :param asset: An asset object with type defined in Asset.py
    :return: The name of the associated db, as a str
    """
    if isinstance(asset, Asset.Pair):
        return 'CUR'


def quandl_code(asset) -> str:

    if isinstance(asset, Asset.Pair):
        if not FxUtils.is_usd_cross(asset):
            raise ValueError(
                'Use of Quandl source for ccy pairs requires USD crosses only, got {}'
                .format(asset))
        # Since this a USD cross, only expect 1 ccy when unpacking
        non_usd_ccy, = FxUtils.non_usd_currencies(asset)
        return quandl_db(asset) + '/' + non_usd_ccy.__str__()
