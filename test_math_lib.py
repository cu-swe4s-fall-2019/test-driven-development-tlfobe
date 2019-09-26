import unittest
import math_lib


class TestMathLib(unittest.TestCase):
    def test_list_mean_empty_list(self):
        self.assertRaises(TypeError,
                          math_lib.list_mean,
                          None
                          )
