import unittest

from lessons.lesson_003_arrays_and_hashing.practice import (
    contains_duplicate,
    index_of_first,
    two_sum_indices,
)


class IndexOfFirstTests(unittest.TestCase):
    def test_returns_first_matching_index(self):
        self.assertEqual(index_of_first([4, 7, 7, 9], 7), 1)

    def test_absent_and_empty(self):
        self.assertEqual(index_of_first([4, 7], 8), -1)
        self.assertEqual(index_of_first([], 8), -1)


class ContainsDuplicateTests(unittest.TestCase):
    def test_duplicate(self):
        self.assertTrue(contains_duplicate([1, 2, 1]))

    def test_all_distinct_and_empty(self):
        self.assertFalse(contains_duplicate([1, 2, 3]))
        self.assertFalse(contains_duplicate([]))


class TwoSumIndicesTests(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(two_sum_indices([2, 7, 11, 15], 9), [0, 1])

    def test_duplicate_values_use_different_indices(self):
        self.assertEqual(two_sum_indices([3, 3], 6), [0, 1])

    def test_negative_values(self):
        self.assertEqual(two_sum_indices([-3, 4, 3, 90], 0), [0, 2])

    def test_pair_is_not_adjacent(self):
        self.assertEqual(two_sum_indices([5, 1, 8, 2], 7), [0, 3])


if __name__ == "__main__":
    unittest.main()

