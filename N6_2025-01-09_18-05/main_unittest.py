import unittest

from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(1501)

    def test_char(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrome(self):
        self.assertEqual(reverse('palilap'), 'palilap')

    def test_string(self):
        self.assertEqual(reverse('string'), 'gnirts')

    def test_not_iter(self):
        with self.assertRaises(TypeError):
            reverse(int())

    def test_iter(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 1])


if __name__ == '__main__':
    unittest.main()
