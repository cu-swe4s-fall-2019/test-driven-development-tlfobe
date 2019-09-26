import unittest
import math_lib


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