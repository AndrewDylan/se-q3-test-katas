import unittest
import katas
from random import randint

__author__ = "Andrew Canter"


class TestKatas(unittest.TestCase):
    def test_add(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        self.assertEqual(katas.add(x, y), x+y)
        self.assertEqual(katas.add(-10, 11), 1)

    def test_multiply(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        self.assertEqual(katas.multiply(x, y), x*y)
        self.assertEqual(katas.multiply(-10, 11), -110)

    def test_power(self):
        x = randint(-100, 100)
        n = randint(0, 10)

        self.assertEqual(katas.power(x, n), x**n)
        self.assertEqual(katas.power(-10, 2), 100)
        with self.assertRaises(ValueError):
            katas.power(10, -2)
        with self.assertRaises(ValueError):
            katas.power(10, .5)

    def test_factorial(self):
        answers = []
        for i in range(15):
            if i == 0:
                answers.append(1)
                continue
            cur = 1
            for x in range(1, i+1):
                cur = cur * x
            answers.append(cur)

        for i in range(15):
            self.assertEqual(katas.factorial(i), answers[i])

        with self.assertRaises(ValueError):
            katas.factorial(-3)

    def test_fibonacci(self):
        answers = [0, 1]

        for i in range(2, 30):
            answers.append(answers[i-1]+answers[i-2])

        for i in range(30):
            self.assertEqual(katas.fibonacci(i), answers[i])

        with self.assertRaises(ValueError):
            katas.fibonacci(-3)


if __name__ == '__main__':
    unittest.main()
