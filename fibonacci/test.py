
from unittest import TestCase, main
from solution1 import fibonacci
from solution2 import fibonacci as fibonacci_recursive
from solution3 import fibonacci as fibonacci_generator


class FibonacciTestCase(TestCase):
    def setUp(self):
        self.firsts = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

    def test_fibonacci(self):
        for position, expected in enumerate(self.firsts):
            self.assertEqual(fibonacci(position), expected)

    def test_fibonacci_recursive(self):
        for position, expected in enumerate(self.firsts):
            self.assertEqual(fibonacci_recursive(position), expected)

    def test_fibonacci_generator(self):
        generator = fibonacci_generator()
        for expected in self.firsts:
            self.assertEqual(next(generator), expected)


if __name__ == "__main__":
    main()
