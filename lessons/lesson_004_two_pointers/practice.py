"""Lesson 004 exercises: two-pointer patterns."""


def is_palindrome(text):
    """Return whether text reads the same from left to right and right to left."""
    # Examples: "level" -> True; "hello" -> False
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def two_sum_sorted(numbers, target):
    """Return indices of the unique pair summing to target in a sorted list.

    The input is sorted in non-decreasing order and exactly one pair exists.
    Return the earlier index first.
    """
    # Example: two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum > target:
            right -= 1
        elif current_sum == target:
            return [left, right]
        else:
            left += 1


def remove_duplicates_sorted(numbers):
    """Remove duplicates in place from a sorted list and return its new length.

    After returning k, only numbers[:k] is considered part of the result.
    """
    # Example: [1, 1, 2, 2, 3] -> k == 3 and numbers[:k] == [1, 2, 3]
    if len(numbers) == 0:
        return 0
    write = 1
    for read in range(1, len(numbers)):
        if numbers[read] == numbers[write - 1]:
            pass
        else:
            numbers[write] = numbers[read]
            write += 1
    return write
