import unittest
from unittest.mock import patch, MagicMock

import numpy as np

import tsneplot


class TSNEPlotTests(unittest.TestCase):
    @patch('tsneplot._train_tsne')
    @patch('tsneplot.plot')
    def test_display_all(self, plot_mock, tsne_mock):
        model = MagicMock()
        model.vocab = {'chicken': 1, 'beef': 1}
        model.vectors = np.array([(1., 2., 3.), (4., 5., 6.)])
        tsne_mock.return_value = np.array([(1, 2), (3, 4)])

        tsneplot.display_all(model)

        words, x_coords, y_coords = plot_mock.scatterplot.call_args[0]
        self.assertEqual(words, ['chicken', 'beef'])
        np.testing.assert_array_equal(x_coords, np.array([1, 3]))
        np.testing.assert_array_equal(y_coords, np.array([2, 4]))

        tsne_mock.assert_called_once_with(model.vectors)

    @patch('tsneplot._train_tsne')
    @patch('tsneplot.plot')
    def test_display_words(self, plot_mock, tsne_mock):
        model = MagicMock()
        tsne_mock.return_value = np.array([(1, 2), (3, 4)])

        tsneplot.display_words(model, ['chicken', 'beef'])

        words, x_coords, y_coords = plot_mock.scatterplot.call_args[0]
        self.assertEqual(words, ['chicken', 'beef'])
        np.testing.assert_array_equal(x_coords, np.array([1, 3]))
        np.testing.assert_array_equal(y_coords, np.array([2, 4]))

        model.similar_by_word.assert_any_call('chicken')
        model.similar_by_word.assert_any_call('beef')
        self.assertEqual(model.similar_by_word.call_count, 2)

    @patch('gensim.models.KeyedVectors')
    def test_load_model(self, gensim_mock):
        tsneplot.load_model('my path')
        gensim_mock.load_word2vec_format.assert_called_once_with('my path')
