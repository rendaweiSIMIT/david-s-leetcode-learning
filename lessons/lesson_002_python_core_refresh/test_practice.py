import unittest

from lessons.lesson_002_python_core_refresh.practice import (
    count_greater_than,
    unique_in_order,
    word_frequencies,
)


class CountGreaterThanTests(unittest.TestCase):
    def test_typical_and_strict_boundary(self):
        self.assertEqual(count_greater_than([1, 5, 5, 8], 5), 1)

    def test_empty(self):
        self.assertEqual(count_greater_than([], 10), 0)


class WordFrequenciesTests(unittest.TestCase):
    def test_repeated_words(self):
        self.assertEqual(
            word_frequencies(["ai", "ml", "ai"]),
            {"ai": 2, "ml": 1},
        )

    def test_empty(self):
        self.assertEqual(word_frequencies([]), {})


class UniqueInOrderTests(unittest.TestCase):
    def test_duplicates_preserve_first_seen_order(self):
        self.assertEqual(unique_in_order([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_empty(self):
        self.assertEqual(unique_in_order([]), [])


if __name__ == "__main__":
    unittest.main()

