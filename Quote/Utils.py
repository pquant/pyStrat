"""
Various utility functions
"""


def check_quote_types(obj, *target_tys):
    """
    Used to raise TypeErrors when instantiating QuoteInterface from Quote.py
    :param obj: object to type-check
    :param tys: target types for asset, market, source (expected in that order)
    :return: None if object's asset/market/source are consistent with target types - otherwise TypeError raised
    """
    targ_asset_ty, targ_market_ty, targ_source_ty = target_tys
    obj_asset, obj_market, obj_source = obj.asset, obj.market, obj.source

    if not isinstance(obj.asset, targ_asset_ty):
        raise TypeError(
            'Expected asset of type {0}, got object {1} of type {2}'.format(
                targ_asset_ty, obj_asset, type(obj_asset)))
    if not isinstance(obj.market, targ_market_ty):
        raise TypeError(
            'Expected market of type {0}, got object {1} of type {2}'.format(
                targ_market_ty, obj_market, type(obj_market)))
    if not isinstance(obj.source, targ_source_ty):
        raise TypeError(
            'Expected source of type {0}, got object {1} of type {2}'.format(
                targ_source_ty, obj_source, type(obj_source)))
    return None
