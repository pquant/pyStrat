

ccy_list = ["USD",  "AUD", "JPY", "EUR", "GBP"]
######################################################################
## FX types
######################################################################

class Ccy():
    """ A type for individual currencies"""

    def __init__(self,ccy_str):
        if ccy_str in ccy_list:
            self.ccy = ccy_str
        else:
            raise ValueError(ccy_str + " is not in the list of currently accepted currencies:" + ccy_list.__str__())

    #Special methods
    def __str__(self):
        return self.ccy
        
    def __eq__(self, other):
        return self.ccy == other.ccy

class Pair():
    """ A type for currency pairs. Internally Pair stores 2 Ccy's (i.e. 2 objects of type Ccy)"""

    def __init__(self, lhs, rhs):
        if isinstance(lhs,Ccy) and isinstance(rhs,Ccy):
            self.lhs = lhs
            self.rhs = rhs
        elif isinstance(lhs,str) and isinstance(rhs,str):
            self.lhs = Ccy(lhs)
            self.rhs = Ccy(rhs)
        else:
            raise TypeError("Expected input lhs/rhs to be of type str or Ccy. Got type(lhs)={0:}, and type(rhs)={1:}".format(type(lhs), type(rhs)))
        if lhs == rhs:
                raise ValueError("Input and lhs and rhs must be different. Got lhs==rhs==" + lhs.__str__())
        

    #Special methods
    def __str__(self):
        return self.lhs.__str__() + self.rhs.__str__()

    def __eq__(self, other):
        return (self.lhs == other.lhs) and (self.rhs == other.rhs)
            

if __name__ == '__main__':
#def main():
    lhs, rhs = "AUD","JPY"
    ccy1, ccy2 = map(Ccy, [lhs, rhs])
    pair0 = Pair(lhs, rhs)
    pair1 = Pair(ccy1, ccy2)
