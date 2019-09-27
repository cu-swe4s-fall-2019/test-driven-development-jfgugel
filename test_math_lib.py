import sys
import math_lib
import unittest
import random

class TestMathLib(unittest.TestCase)

    def mean_None_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)
        
    def stdev_None_list(self):
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)
        
    def mean_empty_list(self):
        r = math_lib.list_stdev([])
        self.assertEqual(r, None)
    

if __name__ == '__main__'
    unittest.main()
    
