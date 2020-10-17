_ccy_list = ['USD', 'AUD', 'JPY', 'EUR', 'GBP', 'NZD']
_agro_list = ['Coffee', 'Cocoa']
_eq_idx_list = ['FTSE100', 'S&P']

supported_list = {'ccy': _ccy_list, 'agro': _agro_list, 'eq_idx': _eq_idx_list}
######################################################################
# FX asset-class types
######################################################################


class Ccy():
    """
    A type for individual currencies
    """
    def __init__(self, ccy):
        if ccy in _ccy_list:
            self.ccy = ccy
        else:
            raise ValueError(_unsupportedItem_error(ccy, _ccy_list))

    #Special methods
    def __repr__(self):
        return self.ccy

    def __eq__(self, other):
        return self.ccy == other.ccy


class Pair():
    """
    A type for currency pairs. Internally Pair stores 2 Ccy's (i.e. 2 objects of type Ccy)
    """
    def __init__(self, lhs, rhs):
        if isinstance(lhs, Ccy) and isinstance(rhs, Ccy):
            self.lhs = lhs
            self.rhs = rhs
        elif isinstance(lhs, str) and isinstance(rhs, str):
            self.lhs = Ccy(lhs)
            self.rhs = Ccy(rhs)
        else:
            raise TypeError(
                "Expected input lhs/rhs to be of type str or Ccy. Got type(lhs)={0:}, and type(rhs)={1:}"
                .format(type(lhs), type(rhs)))
        if lhs == rhs:
            raise ValueError(
                "Input and lhs and rhs must be different. Got lhs==rhs==" +
                lhs.__str__())

    #Special methods
    def __repr__(self):
        return self.lhs.__str__() + self.rhs.__str__()

    def __eq__(self, other):
        return (self.lhs == other.lhs) and (self.rhs == other.rhs)


######################################################################
## CM asset-class types
######################################################################
class Agro():
    """
    A type for the agriculturals
    """
    def __init__(self, agro):
        if agro in _agro_list:
            self.agro = agro
        else:
            raise ValueError(_unsupportedItem_error(agro, _agro_list))

    #Special methods
    def __repr__(self):
        return self.agro

    def __eq__(self, other):
        return (self.agro == other.agro)


######################################################################
## EQ asset-class types
######################################################################
class EQ_Idx():
    """
    A type for the Equity Indices
    """
    def __init__(self, eq_idx):
        if eq_idx in _eq_idx_list:
            self.eq_idx = eq_idx
        else:
            raise ValueError(_unsupportedItem_error(eq_idx, _eq_idx_list))

    #Special methods
    def __repr__(self):
        return self.eq_idx

    def __eq__(self, other):
        return (self.eq_idx == other.eq_idx)


######################################################################
## Utils
######################################################################
def _unsupportedItem_error(x, supported_list):
    return x + " is not currently supported. The supported list is :" + supported_list.__str__(
    )
