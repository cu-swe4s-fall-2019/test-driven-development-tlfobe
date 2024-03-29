import unittest
import os
import data_viz
import stat


class TestBoxPlot(unittest.TestCase):
    def test_boxplot_null(self):
        self.assertRaises(TypeError,
                          data_viz.boxplot,
                          None,
                          )

    def test_boxplot_empty_list(self):
        self.assertRaises(IndexError,
                          data_viz.boxplot,
                          [],
                          )

    def test_boxplot_wrong_type(self):
        self.assertRaises(TypeError, data_viz.boxplot, 'string', 'file.png')
        self.assertRaises(TypeError, data_viz.boxplot, dict(), 'file.png')
        self.assertRaises(TypeError, data_viz.boxplot, True, 'file.png')

    def test_boxplot_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.boxplot,
                          ['string', 1, 2, ['List!'], ],
                          )

    def test_boxplot_filename_str(self):
        self.assertRaises(TypeError, data_viz.boxplot,
                          [1, 2, 3, 4, 5, 6, 7],
                          1,
                          )

    def test_boxplot_write_to_file(self):
        data_viz.boxplot([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], 'newfile.png')
        self.assertTrue(os.path.exists("newfile.png"))
        os.remove("newfile.png")

    def test_boxplot_permission(self):
        with open("read_only.png", "w") as f:
            f.write("Hello, World!")
        os.chmod("read_only.png", stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        self.assertRaises(PermissionError, data_viz.boxplot, [
                          1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "read_only.png")
        os.remove("read_only.png")

    def test_boxplot_wrong_file(self):
        self.assertRaises(ValueError, data_viz.boxplot,
                          [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "read_only.txt")


class TestHistogram(unittest.TestCase):
    def test_histogram_null(self):
        self.assertRaises(TypeError,
                          data_viz.histogram,
                          None,
                          )

    def test_histogram_empty_list(self):
        self.assertRaises(IndexError,
                          data_viz.histogram,
                          [],
                          )

    def test_histogram_wrong_type(self):
        self.assertRaises(TypeError, data_viz.histogram, 'string', 'file.png')
        self.assertRaises(TypeError, data_viz.histogram, dict(), 'file.png')
        self.assertRaises(TypeError, data_viz.histogram, True, 'file.png')

    def test_histogram_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.histogram,
                          ['string', 1, 2, ['List!'], ],
                          )

    def test_histogram_filename_str(self):
        self.assertRaises(TypeError, data_viz.histogram,
                          [1, 2, 3, 4, 5, 6, 7],
                          1,
                          )

    def test_histogram_write_to_file(self):
        data_viz.histogram([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], 'newfile.png')
        self.assertTrue(os.path.exists("newfile.png"))
        os.remove("newfile.png")

    def test_histogram_permission(self):
        with open("read_only.png", "w") as f:
            f.write("Hello, World!")
        os.chmod("read_only.png", stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        self.assertRaises(PermissionError, data_viz.histogram, [
                          1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "read_only.png")
        os.remove("read_only.png")

    def test_histogram_wrong_file(self):
        self.assertRaises(ValueError, data_viz.histogram,
                          [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "read_only.txt")


class TestCombo(unittest.TestCase):
    def test_combo_null(self):
        self.assertRaises(TypeError,
                          data_viz.combo,
                          None,
                          )

    def test_combo_empty_list(self):
        self.assertRaises(IndexError,
                          data_viz.combo,
                          [],
                          )

    def test_combo_wrong_type(self):
        self.assertRaises(TypeError, data_viz.combo, 'string', 'file.png')
        self.assertRaises(TypeError, data_viz.combo, dict(), 'file.png')
        self.assertRaises(TypeError, data_viz.combo, True, 'file.png')

    def test_combo_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.combo,
                          ['string', 1, 2, ['List!'], ],
                          )

    def test_combo_filename_str(self):
        self.assertRaises(TypeError, data_viz.combo,
                          [1, 2, 3, 4, 5, 6, 7],
                          1,
                          )

    def test_combo_write_to_file(self):
        data_viz.combo([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], 'newfile.png')
        self.assertTrue(os.path.exists("newfile.png"))
        os.remove("newfile.png")

    def test_combo_permission(self):
        with open("read_only.png", "w") as f:
            f.write("Hello, World!")
        os.chmod("read_only.png", stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        self.assertRaises(PermissionError, data_viz.combo,
                          [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "read_only.png")
        os.remove("read_only.png")

    def test_combo_wrong_file(self):
        self.assertRaises(ValueError, data_viz.combo,
                          [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "read_only.txt")
