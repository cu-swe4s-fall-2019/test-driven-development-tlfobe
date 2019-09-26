import unittest
import math_lib
import numpy as np


class TestMathLib(unittest.TestCase):
    # list_mean Tests
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
        self.assertEqual(math_lib.list_mean([1, 2, 3, 4, 5]), 3)

    def test_list_mean_random(self):
        exp_mean = np.random.uniform(0, 100)
        dist = np.random.normal(loc=exp_mean, scale=1, size=10000).tolist()
        self.assertAlmostEqual(math_lib.list_mean(dist), exp_mean, places=1)

    def test_list_mean_random_numpy(self):
        exp_mean = np.random.uniform(0, 100)
        dist = np.random.normal(loc=exp_mean, scale=1, size=10000)
        self.assertAlmostEqual(math_lib.list_mean(dist), exp_mean, places=1)

    def test_list_mean_complex(self):
        self.assertEqual(math_lib.list_mean([1-3j, 2-2j, 3-1j]), 2-2j)

    # list_stdev test
    def test_list_stdev_null(self):
        self.assertRaises(TypeError,
                          math_lib.list_stdev,
                          None,
                          )

    def test_list_stdev_empty_list(self):
        self.assertRaises(IndexError,
                          math_lib.list_stdev,
                          [],
                          )

    def test_list_stdev_wrong_type(self):
        self.assertRaises(TypeError, math_lib.list_stdev, 'string')
        self.assertRaises(TypeError, math_lib.list_stdev, dict())
        self.assertRaises(TypeError, math_lib.list_stdev, True)

    def test_list_stdev_list_wrong_type(self):
        self.assertRaises(TypeError, math_lib.list_stdev,
                          ['string', 1, 2, ['List!']]
                          )

    def test_list_stdev_const(self):
        self.assertEqual(math_lib.list_stdev([1, 1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(math_lib.list_stdev([1, 2]), 0.5)

    def test_list_stdev_random(self):
        exp_std = np.random.uniform(0, 100)
        dist = np.random.normal(loc=0, scale=exp_std, size=100000).tolist()
        self.assertAlmostEqual(math_lib.list_stdev(dist), exp_std, places=0)

    def test_list_stdev_random_numpy(self):
        exp_std = np.random.uniform(0, 100)
        dist = np.random.normal(loc=0, scale=exp_std, size=100000)
        self.assertAlmostEqual(math_lib.list_stdev(dist), exp_std, places=0)
