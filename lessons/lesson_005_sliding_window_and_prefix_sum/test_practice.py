import unittest

from lessons.lesson_005_sliding_window_and_prefix_sum.practice import (
    max_sum_fixed_window,
    min_subarray_len,
    range_sum_queries,
)


class MaxSumFixedWindowTests(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(max_sum_fixed_window([2, 1, 5, 1, 3, 2], 3), 9)

    def test_all_negative(self):
        self.assertEqual(max_sum_fixed_window([-4, -2, -7], 2), -6)

    def test_single_and_whole_list_window(self):
        self.assertEqual(max_sum_fixed_window([5], 1), 5)
        self.assertEqual(max_sum_fixed_window([1, 2, 3, 4], 4), 10)


class RangeSumQueriesTests(unittest.TestCase):
    def test_multiple_ranges(self):
        self.assertEqual(
            range_sum_queries([2, 4, 1, 3], [(0, 2), (1, 3), (2, 2)]),
            [7, 8, 1],
        )

    def test_negative_values(self):
        self.assertEqual(
            range_sum_queries([-2, 5, -1, 4], [(0, 3), (1, 2)]),
            [6, 4],
        )

    def test_no_queries(self):
        self.assertEqual(range_sum_queries([1, 2, 3], []), [])


class MinSubarrayLenTests(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(min_subarray_len(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_entire_list_and_single_element(self):
        self.assertEqual(min_subarray_len(4, [1, 1, 1, 1]), 4)
        self.assertEqual(min_subarray_len(5, [1, 5, 10]), 1)

    def test_no_valid_window_and_empty(self):
        self.assertEqual(min_subarray_len(100, [1, 2, 3]), 0)
        self.assertEqual(min_subarray_len(1, []), 0)


if __name__ == "__main__":
    unittest.main()

