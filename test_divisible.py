# create a TestCase using the unittest framework and use asserts 
# to verify that the divisible_by()function returns the correct result. 
# Don’t forget to import your divisible_by() function.

import unittest
from divisible import divisible_by_other

class TestDivisible(unittest.TestCase):
    
    def test_divisible_by_other(self):
        self.assertTrue(divisible_by_other(10,2))
        self.assertFalse(divisible_by_other(10,3))
