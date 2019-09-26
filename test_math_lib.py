import unittest
import math_lib
import numpy as np


class TestMathLib(unittest.TestCase):
    def test_list_mean_null(self):
        self.assertRaises(TypeError,
                          math_lib.list_mean,
                          None,
                          )

    def test_list_mean_empty_list(self):
        self.assertRaises(IndexError,
                          math_lib.list_mean,
                          [],
                          )

    def test_list_mean_wrong_type(self):
        self.assertRaises(TypeError, math_lib.list_mean, 'string')
        self.assertRaises(TypeError, math_lib.list_mean, dict())
        self.assertRaises(TypeError, math_lib.list_mean, True)

    def test_list_mean_list_wrong_type(self):
        self.assertRaises(TypeError, math_lib.list_mean,
                          ['string', 1, 2, ['List!']]
                          )

    def test_list_mean_const(self):
        self.assertEquals(math_lib.list_mean([1,2,3,4,5]), 3)

        
