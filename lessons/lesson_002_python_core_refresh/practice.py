"""Lesson 002 exercises: functions and core Python containers."""


def count_greater_than(numbers, threshold):
    """Return how many values in numbers are strictly greater than threshold."""
    count = 0
    for number in numbers:
        if number > threshold:
            count = count + 1
    return count # Example: count_greater_than([1, 5, 5, 8], 5) == 1



def word_frequencies(words):
    """Return a dictionary mapping each word to its occurrence count."""
    # Example: word_frequencies(["ai", "ml", "ai"]) == {"ai": 2, "ml": 1}
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def unique_in_order(items):
    """Return the first occurrence of each value while preserving input order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
