import unittest
import data_viz

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
        self.assertRaises(TypeError, data_viz.boxplot, 'string','file.png')
        self.assertRaises(TypeError, data_viz.boxplot, dict(),'file.png')
        self.assertRaises(TypeError, data_viz.boxplot, True,'file.png')

    def test_boxplot_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.boxplot,
                          ['string', 1, 2, ['List!'],],
                           )

    def test_boxplot_filename_str(self):
        self.assertRaises(TypeError, data_viz.boxplot,
                          [1, 2, 3, 4, 5, 6, 7],
                          1,
                          )

    