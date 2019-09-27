import sys
import math_lib
import unittest
import random
import statistics

class TestMathLib(unittest.TestCase)

    def mean_None_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)
        
    def stdev_None_list(self):
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)
        
    def mean_empty_list(self):
        r = math_lib.list_mean([])
        self.assertEqual(r, None)
        
    def stdev_empty_list(self):
        r = math_lib.list_stdev([])
        self.assertEqual(r, None)
        
    def mean_test_easy_calc(self):
        r = math_lib.list_mean([5, 5, 5, 5, 5])
        self.assertEqual(r, 5)
        
    def stdev_test_easy_calc(self):
        r = math_lib.list_mean([5, 5, 5, 5])
        self.assertEqual(r, 0)
    
    def mean_test_random_calc(self)
        L = []
        
        for i in range(10):
            L.append(random.randint(0, 100))
        
        r = math_lib.list_mean(L)
        self.assertEqual(r, statistics.mean(L))

        
    
if __name__ == '__main__'
    unittest.main()
    
