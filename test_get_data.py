import unittest
import get_data

class TestGetData(unittest.TestCase):
    def test_read_stdin_null(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, None)
        
