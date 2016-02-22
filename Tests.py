# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 08:21:38 2016

@author: vp
"""

import unittest as ut
from Asset import *

#####################################################################################
# Asset tests
#####################################################################################
class AssetTests(ut.TestCase):
    """Test Asset module"""
    
    def test_ccy_construction_notavailable(self):
        self.assertRaises(ValueError, Ccy, "usd")
    
    def test_ccy_equality(self):
        self.assertEqual(Ccy("USD"), Ccy("USD"))
        
class PairTests(ut.TestCase):
    """Test Asset module"""
    def test_pair_construction_inconsistent_inputs(self):
        self.assertRaises(TypeError, Pair, Ccy("JPY"), "USD")

    def test_pair_construction_lhs_equals_rhs(self):
        self.assertRaises(ValueError, Pair, "USD", "USD")
        
    def test_pair_equality(self):
        self.assertEqual(Pair("AUD","JPY"), Pair("AUD","JPY"))
        
#####################################################################################
# Market tests
#####################################################################################

#####################################################################################
# Fix tests
#####################################################################################

if __name__ == '__main__':
    ut.main()
