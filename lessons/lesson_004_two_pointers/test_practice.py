import unittest

from lessons.lesson_004_two_pointers.practice import (
    is_palindrome,
    remove_duplicates_sorted,
    two_sum_sorted,
)


class IsPalindromeTests(unittest.TestCase):
    def test_odd_and_even_length_palindromes(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("abba"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_and_single_character(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("x"))


class TwoSumSortedTests(unittest.TestCase):
    def test_pair_at_ends(self):
        self.assertEqual(two_sum_sorted([1, 2, 4, 8, 13], 14), [0, 4])

    def test_pair_in_middle(self):
        self.assertEqual(two_sum_sorted([1, 3, 4, 6, 8], 10), [2, 3])

    def test_duplicate_values(self):
        self.assertEqual(two_sum_sorted([1, 3, 3, 7], 6), [1, 2])

    def test_negative_values(self):
        self.assertEqual(two_sum_sorted([-5, -2, 1, 4, 9], 2), [1, 3])


class RemoveDuplicatesSortedTests(unittest.TestCase):
    def assert_compacted(self, numbers, expected):
        k = remove_duplicates_sorted(numbers)
        self.assertEqual(k, len(expected))
        self.assertEqual(numbers[:k], expected)

    def test_typical(self):
        self.assert_compacted([1, 1, 2, 2, 3], [1, 2, 3])

    def test_all_duplicates(self):
        self.assert_compacted([5, 5, 5], [5])

    def test_already_unique(self):
        self.assert_compacted([1, 2, 3], [1, 2, 3])

    def test_empty(self):
        self.assert_compacted([], [])


if __name__ == "__main__":
    unittest.main()
