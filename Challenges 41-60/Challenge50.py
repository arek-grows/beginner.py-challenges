import unittest
from typing import List


def circular_shift(lst1: List[int], lst2: List[int],  n: int) -> bool:
    lst2_l = len(lst2)
    new_lst = [0] * lst2_l
    for x, nr in enumerate(lst2):
        # lst_2 item's index added to the shift (n) and then modular'd by the length of lst_2 produces unshifted index
        new_lst[(x + n) % lst2_l] = nr
    return lst1 == new_lst  # Put your code here!!!


class TestCircularShift(unittest.TestCase):
    def test_1(self):
        self.assertTrue(
            circular_shift(
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                2
            )
        )

    def test_2(self):
        self.assertTrue(
            circular_shift(
                [1, 1],
                [1, 1],
                6
            )
        )

    def test_3(self):
        self.assertFalse(
            circular_shift(
                [0, 1, 2, 3, 4, 5],
                [3, 4, 5, 2, 1, 0],
                3
            )
        )

    def test_4(self):
        self.assertFalse(
            circular_shift(
                [0, 1, 2, 3],
                [1, 2, 3, 1],
                1
            )
        )

    def test_5(self):
        self.assertTrue(
            circular_shift(
                list(range(32)),
                list(range(32)),
                0
            )
        )

    def test_6(self):
        self.assertTrue(
            circular_shift(
                [1, 2, 1],
                [1, 2, 1],
                3
            )
        )

    def test_7(self):
        self.assertTrue(
            circular_shift(
                [5, 7, 2, 3],
                [2, 3, 5, 7],
                -2
            )
        )

    def test_8(self):
        self.assertFalse(
            circular_shift(
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                1
            )
        )


if __name__ == "__main__":
    unittest.main()