import unittest


def factorial(number: int) -> int:
    total = 1
    for n in range(number, 0, -1):
        total *= n
    return total  # Put your code here!!!


class TestFactorial(unittest.TestCase):
    def test_1(self):
        self.assertEqual(24, factorial(4))

    def test_2(self):
        self.assertEqual(1, factorial(0))

    def test_3(self):
        self.assertEqual(362880, factorial(9))

    def test_4(self):
        self.assertEqual(1, factorial(1))

    def test_5(self):
        self.assertEqual(2, factorial(2))

    def test_6(self):
        self.assertEqual(
            93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000,
            factorial(100)
        )

    def test_bonus(self):
        try:
            factorial(1000)
        except RecursionError:
            passed = False
        else:
            passed = True
        self.assertTrue(passed, "Too much recursion")


if __name__ == "__main__":
    unittest.main()