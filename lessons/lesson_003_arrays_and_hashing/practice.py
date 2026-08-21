"""Lesson 003 exercises: array traversal and hash-based lookup."""


def index_of_first(numbers, target):
    """Return the first index whose value equals target, or -1 if absent."""
    a = -1
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return a

def contains_duplicate(items):
    """Return whether any value appears at least twice."""
    # Examples: [1, 2, 1] -> True; [1, 2, 3] -> False
    seen = set()
    for number in items:
        if number not in seen:
            seen.add(number)
        else:
            return True
    return False

def two_sum_indices(numbers, target):
    """Return indices of two different values whose sum equals target.

    Exactly one valid pair exists. Return the earlier index first.
    """
    # Example: two_sum_indices([2, 7, 11, 15], 9) == [0, 1]
    seen = {}
    for i, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], i]
        seen[number] = i
