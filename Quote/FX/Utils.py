from Asset import Ccy, Pair
import copy

# cross_ccy_pairs = [ ('EUR','GBP'),
#                     ('EUR','JPY'),
#                     ('AUD','NZD'),
#                     (),
#                     (),
#                     ()]



def is_usd_cross(pair: Pair) -> bool:
    """
    Checks if input pair is a USD cross
    :param pair: input pair of type Asset.Pair (not type-checked)
    :return: True if any of lhs/rhs is USD
    """
    usd = Ccy('USD')
    return pair.lhs == usd or pair.rhs == usd


def is_inverted(pair: Pair) -> bool:
    pair_conv = quote_convention(pair)
    return pair != pair_conv

"""
List of currencies XXX whose USD-cross is quoted XXXUSD (as the vast majority of USD crosses will be quoted USDXXX)
"""
usd_crosses_exceptions = ['AUD', 'EUR', 'GBP', 'NZD']


def quote_convention(pair) -> Pair:
    """
    Provides market quote convention for input ccy pair (not type-checked, and returns a new Pair object)
    :param pair: of type Asset.Pair
    :return: an Asset.Pair, as per market convention
    """
    usd = Ccy('USD')
    lhs = pair.lhs
    rhs = pair.rhs
    if is_usd_cross(pair):
        if lhs == usd:
            if rhs in map(Ccy, usd_crosses_exceptions):
                return Pair(rhs, lhs)
            else:
                return copy.deepcopy(pair)  # meh...might as well write Pair(pair.lhs, pair.rhs)
        elif rhs == usd:
            if lhs in map(Ccy, usd_crosses_exceptions):
                return copy.deepcopy(pair)
            else:
                return Pair(rhs, lhs)
    else:
        raise ValueError('Not dealing with cross ccy pairs for now')


def convert_to_quote_convention(pair: Pair) -> Pair:
    """
    Provides market quote convention for input ccy pair (not type-checked, but potentially swaps lhs/rhs of input Pair)
    :param pair: of type Asset.Pair
    :return: the input Pair
    """
    usd = Ccy('USD')
    lhs = pair.lhs
    if is_usd_cross(pair):
        if not (lhs == usd or lhs in map(Ccy, usd_crosses_exceptions())):
            pair.lhs, pair.rhs = pair.rhs, pair.lhs
    else:
        raise ValueError('Not dealing with cross ccy pairs for now')

    return pair


def split_to_usd_crosses(pair: Pair) -> [Pair]:
    """
    Splits a potentially cross ccy pair into usd crosses, without applying quote conventions for usd crosses.
    Example: EURGBP will return [EURUSD, USDGBP] NOT [EURUSD, GBPUSD]
    Example : JPYUSD will return [JPYUSD]
    :param pair: of type Asset.Pair
    :return: a 1- or 2- element list of Asset.Pairs
    """
    if is_usd_cross(pair):
        return [pair]     # returning input object here
    else:
        usd = Ccy('USD')
        return [Pair(pair.lhs, usd), Pair(usd, pair.rhs)]


def non_usd_currencies(pair: Pair) -> [Ccy]:
    """
    Extracts non-USD currencies from input Pair
    :param pair: of type Asset.Pair
    :return:
    """
    return [c for c in [pair.lhs, pair.rhs] if c.__str__() != 'USD']