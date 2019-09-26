import unittest
import get_data

class TestGetData(unittest.TestCase):
    def test_read_stdin_null(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, None)

    def test_read_stdin_incorrect_types(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, [1,2,3])
        self.assertRaises(TypeError, get_data.read_stdin_col, "string")
        self.assertRaises(TypeError, get_data.read_stdin_col, {1:2, 2:3})
        self.assertRaises(TypeError, get_data.read_stdin_col, 10.32)
        self.assertRaises(TypeError, get_data.read_stdin_col, 1+1j)
