import unittest
from typing import List


def count_overlapping(intervals: List[List[int]], point: int) -> int:
    total = 0
    for interval in intervals:
        if interval[0] <= point <= interval[1]:
            total += 1
    return total  # Put your code here!!


class TestOverlappingIntervals(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_overlapping([[1, 2], [2, 3], [3, 4]], 5), 0)

    def test_2(self):
        self.assertEqual(count_overlapping([[1, 2], [5, 6], [5, 7]], 5), 2)

    def test_3(self):
        self.assertEqual(count_overlapping([[1, 2], [5, 8], [6, 9]], 7), 2)

    def test_4(self):
        self.assertEqual(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 5), 5)

    def test_5(self):
        self.assertEqual(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 6), 2)

    def test_6(self):
        self.assertEqual(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 2), 2)

    def test_7(self):
        self.assertEqual(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 1), 1)


if __name__ == "__main__":
    unittest.main()