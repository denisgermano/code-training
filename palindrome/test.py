
from unittest import TestCase, main

from solution1 import can_do_palindrome, is_palindrome


class PalindromeTestCase(TestCase):
    def setUp(self):
        self.palindrome_words = ["Civic", "Kayak", "Level", "Mom", "Noon"]
        self.non_palindrome_words = ["Hello", "World", "Not", "Palindrome", "Words"]

    def test_is_palindrome(self):
        for word in self.palindrome_words:
            self.assertTrue(is_palindrome(word))

    def test_not_is_palindrome(self):
        for word in self.non_palindrome_words:
            self.assertFalse(is_palindrome(word))

    def test_can_do_palindrome(self):
        for word in self.palindrome_words:
            self.assertTrue(can_do_palindrome(word))

    def test_cannot_do_palindrome(self):
        for word in self.non_palindrome_words:
            self.assertFalse(can_do_palindrome(word))

    def test_can_do_palindrome_with_non_palindrome_words(self):
        words = ["a", "aa", "aaa", "aaabb", "aaaab"]
        some_possible_palindrome = ["a", "aa", "aaa", "baaab", "aabaa"]
        for word, expected in zip(self.palindrome_words, some_possible_palindrome):
            self.assertTrue(can_do_palindrome(word))
            self.assertTrue(is_palindrome(expected))


if __name__ == "__main__":
    main()
