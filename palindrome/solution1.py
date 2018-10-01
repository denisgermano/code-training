from collections import Counter


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def can_do_palindrome(word):
    word = word.lower()
    counter = Counter(word)
    odd_characters = sum([1 for value in counter.values() if value % 2 == 1])
    return odd_characters <= 1
