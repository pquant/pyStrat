# -*- coding: utf-8 -*-

"""
Definition of various market types
"""

################################################################################
# A Spot Market
# TODO : Should we call that Cash?
################################################################################
class Spot:
    pass

################################################################################
# A Futures Market
################################################################################
class Futures:
    def __init__(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("A Futures Market object is constructed with a contract of type Contract. Got "
                            + contract.__repr__() + " of type " + type(contract).__name__)
        self.contract = contract

    #Special methods
    def __repr__(self):
        return self.contract

    def __eq__(self, other):
        return self.contract == other.contract


class Contract:
    """ 
    Futures contract type
    Traditional Contract() instantiation forbidden. Alternative constructors are Contract.active() and Contract.month('someMonth') instead
    TODO: Define a separate type for Months? Z15 might feel universal because everyone uses Bloomberg, but some other source might have it 
    represented in a different way, say 'Dec2015'
    """
    def __init__(self,*args):
        raise SyntaxError("A Contract cannot be instantiated with the traditional Contract(...) function." 
                        + "Please use tailor-made instantiations instead - "
                        + "for active contracts (Contract.active()) and contracts of a certain month (e.g. Contract.month('Z1'))")

    @classmethod
    def active(cls):
        c = cls.__new__(cls)
        c.contractTy = "Active"
        c.month = None
        return c
    
    @classmethod
    def month(cls, month):
        if not isinstance(month, str):
            TypeError("A Contract month should be a string. Got " + month.__str__() + " of type" + type(month).__name__)
        c = cls.__new__(cls)
        c.contractTy = "Month"
        c.month = month
        return c
        
    #Special methods
    def __repr__(self):
        return self.contractTy if self.month is None else self.contractTy + "(" + self.month + ")"

    def __eq__(self, other):
        return self.contractTy == other.contractTy and self.month == other.month
