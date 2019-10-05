# pylint: skip-file
"""
Checks the first lab. Part about the creation of the frequencies dictionary
"""

import unittest

import main


STOP_WORDS = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
              'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be',
              'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself',
              'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
              'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
              'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
              'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
              'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
              'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
              'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',
              'it', 'how', 'further', 'was', 'here', 'than')


class FilterStopWordsTest(unittest.TestCase):
    """
    Tests dictionary filtering
    """

    def test_filter_words_ideal(self):
        """
        Filter stop words ideal case - good dict, good stop words
    	"""

        freq_dict = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        expected_result = {
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.filter_stop_words(freq_dict, STOP_WORDS)
        self.assertEqual(expected_result, res)

    def test_filter_words_stop_dublicate(self):
        """
        Stop words with duplicates
    	"""

        freq_dict = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        expected_result = {
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.filter_stop_words(freq_dict, ('the', 'the', 'over'))
        self.assertEqual(expected_result, res)

    def test_filter_words_stop_numbers(self):
        """
        Stop words with numbers
    	"""

        freq_dict = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        expected_result = {
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.filter_stop_words(freq_dict, ('the', 1, 'over', 4))
        self.assertEqual(expected_result, res)

    def test_filter_words_empty(self):
        """
        Filter stop words when stop words tuple is empty
    	"""
        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.filter_stop_words(expected_result, ())
        self.assertEqual(expected_result, res)

    def test_filter_words_dict_empty(self):
        """
        Filter stop words when stop words tuple is empty
    	"""
        expected_result = {}
        res = main.filter_stop_words({}, STOP_WORDS)
        self.assertEqual(expected_result, res)

    def test_filter_words__dict_no_str(self):
        """
        Filter stop words when dict has keys - not strs
    	"""
        expected_result = {'fox': 2}
        res = main.filter_stop_words({1: 1, 'fox': 2}, STOP_WORDS)
        self.assertEqual(expected_result, res)

    def test_filter_words_copy(self):
        """
        Check that frequencies dict is immutable
    	"""
        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }

        freq_dict = expected_result
        main.filter_stop_words(freq_dict, STOP_WORDS)
        self.assertEqual(expected_result, freq_dict)

    def test_filter_words_stop_none(self):
        """
        Stop words is none
    	"""
        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }

        freq_dict = expected_result
        main.filter_stop_words(freq_dict, None)
        self.assertEqual(expected_result, freq_dict)

    def test_filter_words_dict_none(self):
        """
        Frequencies dict is none
    	"""
        expected_result = {}

        freq_dict = expected_result
        main.filter_stop_words(None, STOP_WORDS)
        self.assertEqual(expected_result, freq_dict)

    def test_filter_words_both_none(self):
        """
        Frequencies dict is none
    	"""
        expected_result = {}

        freq_dict = expected_result
        main.filter_stop_words(None, None)
        self.assertEqual(expected_result, freq_dict)