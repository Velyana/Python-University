import unittest

import hom2


class TestFiveFunctions(unittest.TestCase):

    def test_is_pangram(self):
        self.assertFalse(
            hom2.is_pangram('Малката пухкава панда яде бамбук.'))

        self.assertTrue(
            hom2.is_pangram(
                'Ах, чудна българска земьо, полюшвай цъфтящи жита!'))

    def test_is_pangram_uppercase_1(self):
        self.assertTrue(
            hom2.is_pangram('АБВ ГДЕЖЗ ЯЮъьЩшчц ийКлМН опрстуфьдх'))

    def test_char_histogram(self):
        self.assertEqual(
            {' ': 3, 'i': 2, 'a': 2, 'e': 2, 's': 2, 'h': 1, 'l': 1, 'm': 1,
             'n': 1, 'x': 1, '!': 1, 'p': 1, 'T': 1},
            hom2.char_histogram('This is an example!'))

    def test_char_histogram_10a_3b(self):
        self.assertEqual(hom2.char_histogram('aaaabbaaaabaa'), {'a': 10, 'b': 3})

    def test_sort_by(self):
        self.assertEqual(
            ['a', 'ab', 'abc'],
            hom2.sort_by(lambda x, y: len(x) - len(y), ['abc', 'a', 'ab']))

    def test_group_by_type(self):
        self.assertEqual(
            {str: {'b': 1, 'a': 12}, int: {1: 'foo'}},
            hom2.group_by_type({'a': 12, 'b': 1, 1: 'foo'}))

        self.assertEqual(
            {str: {'c': 15}, int: {1: 'b'},
             tuple: {(1, 2): 12, ('a', 1): 1}},
            hom2.group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b', 'c': 15}))

    def test_group_by_type_2(self):
        self.assertEqual(hom2.group_by_type({int: 2, str: 'a', (1,): [1, 2], 'a': (1, 'v')}),
            {type: {str: 'a', int: 2}, tuple: {(1,): [1, 2]}, str: {'a': (1, 'v')}})

    def test_anagrams(self):
        words = ['army', 'mary', 'ramy', 'astronomer', 'moonstarer',
                 'debit card', 'bad credit', 'bau']
        anagrams = [['army', 'mary', 'ramy'],
                    ['bad credit', 'debit card'],
                    ['astronomer', 'moonstarer'], ['bau']]
        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, hom2.anagrams(words))))

    def test_anagrams_2(self):
        words = ['listen', 'are', 'pets', 'inlets', 'ear', 'enlist',
                'step', 'pest', 'silent', 'tinsel', 'era']
        anagrams = [['listen', 'inlets', 'enlist', 'silent', 'tinsel'],
                    ['are', 'ear', 'era'],
                    ['pets', 'step', 'pest']]
        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, hom2.anagrams(words))))




if __name__ == '__main__':
    unittest.main()