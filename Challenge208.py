# Challenge 208 - Add the Values of the Symbols in a Matrix
#
# Write a function that takes a list of lists and returns the value of all the symbols in it, where each symbol adds or takes something from the total score. Symbol values:
#
# # = 5
# O = 3
# X = 1
# ! = -1
# !! = -3
# !!! = -5
#
# A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
#
# If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
# Examples
#
# check_score([
#   ["#", "!"],
#   ["!!", "X"]
# ]) ➞ 2
#
# check_score([
#   ["!!!", "O", "!"],
#   ["X", "#", "!!!"],
#   ["!!", "X", "O"]
# ]) ➞ 0
#
# check_score([
#   ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
#   ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
#   ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
#   ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
#   ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
#   ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
#   ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
#   ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
#   ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
#   ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
#   ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
#   ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
#   ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
#   ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
# ]) ➞ 12
#
# Notes
#
#     Strings in the lists will only be #, O, X, !, !! and !!!.


from __future__ import annotations
import unittest


def check_score(matrixes: list[list[str]]) -> int:
    total_score = 0
    for matrix in matrixes:
        for n in matrix:
            if n == '#':
                total_score += 5
            elif n == 'O':
                total_score += 3
            elif n == 'X':
                total_score += 1
            elif n == '!':
                total_score += -1
            elif n == '!!':
                total_score += -3
            elif n == '!!!':
                total_score += -5
    if total_score < 0:
        total_score = 0
    return total_score  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            check_score(
                [
                    ['#', '!', 'O', '!!', '#', '!!', '!!', 'X', '!', 'X', '!!!', '!!!', 'X', '#'],
                    ['!', '#', '!!', '!!!', 'X', 'X', '#', '!!', 'O', '!!!', '!', '!!!', '#', 'O'],
                    ['O', 'X', '!!!', '#', '!!!', '!', '!', '!', '#', '!!', '!!!', 'X', '!', 'X'],
                    ['#', '!!', '!!', '#', 'O', '!', 'X', 'X', '!!!', '#', '#', '!!!', '#', '!'],
                    ['#', 'O', 'X', 'X', '!!', '#', 'O', 'X', '#', '!', '!', '!', 'O', '#'],
                    ['X', '!', 'X', 'O', '!', '!', '!!', '!!', '!!', '!!', '!!!', '!!!', '!', 'X'],
                    ['!!!', '!', '!!', 'O', '!!!', 'X', '#', '#', 'X', 'X', '!', '!', 'X', '!'],
                    ['!!!', 'O', '!!!', '!!!', 'O', '#', '!!', '!!!', '!', '!!!', 'O', 'O', 'X', '!!!'],
                    ['!!', 'X', 'O', '!!!', '!!', 'O', '#', 'X', 'O', 'X', '!!', 'X', '#', '!'],
                    ['X', '#', '!!!', '!!!', '!!', '#', '!', '!!', 'O', '!', 'O', '#', '!!!', '#'],
                    ['!', '#', '!', '!!!', '!!!', 'X', '!', 'X', '#', '!!', '!', '!!', 'X', '!!!'],
                    ['!!!', '#', '#', '!!', 'O', '!!', '#', '!!!', '#', '#', '!!', '#', '!', 'O'],
                    ['!!!', 'X', 'O', '!!', 'X', '!', 'O', 'X', 'O', '!!!', '#', '#', '#', '#'],
                    ['X', 'X', '!!!', '!!', 'O', '#', 'O', '#', 'X', 'X', 'X', '!!!', '!', '!!!']
                ]
            ), 32)

    def test_2(self):
        self.assertEqual(
            check_score(
                [
                    ['!', '#', '#', 'O', '#', '!', 'X', '!!', '!!!', '!!', 'O', '!!', '!!!', '!', '!'],
                    ['#', 'O', '!!', '!!', 'X', 'X', '!!!', '!', '!!!', 'X', '!!!', '!!!', '#', '#', '!!!'],
                    ['X', '!!!', '!!!', 'O', '!!!', '!!', '!', '#', 'O', '!', '!!', '!!', '!', 'O', '!'],
                    ['#', '!!', 'O', '#', '!', 'X', 'X', 'X', 'X', 'X', 'O', 'O', '!!', '!!', 'X'],
                    ['O', 'O', '!', '!', '!!', '!!!', 'O', 'O', '!', 'O', '!!', '!!', '!!', '!!', '!!!'],
                    ['!!!', 'O', 'O', '!!!', '!', 'X', '!!', '#', '!!', '!!!', 'X', '!!', '!!!', 'X', '!'],
                    ['!!!', '!!', '!', '#', '#', '!!', '!', 'X', 'O', '!!', 'X', '!!', '!!', '#', '!!'],
                    ['X', '!!!', '!!', 'O', '!!!', 'O', '!', '!!', 'X', '#', '!', '!!!', '!!', 'O', '#'],
                    ['O', 'O', '!', 'X', 'O', '!', 'O', 'X', '#', '!!!', '#', '!!', '!', 'O', 'O'],
                    ['#', '!!', 'O', '!!', '!', '#', '!', 'O', '!!', 'X', 'O', '!!!', '!!', '!', '!!!'],
                    ['!!', '!!!', 'O', '!!', 'O', '!', '!!', '!', '!!', '!!!', 'X', '!!', 'O', '!!!', '!!'],
                    ['!!!', '#', '!!', '#', '!!', '!!!', '#', 'X', '#', 'X', 'X', '!!', '!', '!!!', 'X'],
                    ['!', 'X', 'X', '!', '!!!', '!', '!', 'O', '!', 'X', '!!', '!!!', '!!!', '!', '!!'],
                    ['!!!', '!', '!', '!', '!', '!', '!!', 'X', '!!!', 'O', '!!!', '!!!', '!', '!!!', '#'],
                    ['!!!', '#', '!', 'O', '!', '!!', '!', '!', '!!!', '!!!', 'O', '!!!', '!', '!!', '!']
                ]
            ), 0)

    def test_3(self):
        self.assertEqual(
            check_score(
                [
                    ['!', '!!!', '!', '!', '!!!', '!', 'X', '!!!', '!!!', 'X', '!!', 'X', 'O', '!!!', '!!!', '!', '#'],
                    ['!!', 'X', '!!!', 'X', 'X', 'O', '!!!', '!!!', 'X', '!!', '!!', '!', 'X', '!!', '!!', 'X', '!!!'],
                    ['!!', '#', '#', '!', 'X', 'X', 'X', '#', '!!', '#', 'X', '!!', '!!!', '!', 'X', '!!!', 'X'],
                    ['!!!', '!!', 'O', '#', 'O', '!', '!!!', '!!', 'X', '#', 'X', '!!!', '!!!', 'X', '#', 'X', 'O'],
                    ['X', 'O', '!', '!!', '#', '!', 'X', '#', '!!!', '!!!', 'O', '!', 'X', '!', '!', '!!', '#'],
                    ['#', '!', '!!', '!!!', '!!!', '!!!', 'O', '!!', '!', '!', '!!', '!', '!!!', '#', 'O', '!!!', 'O'],
                    ['!', '!', '!!', 'X', 'O', '!', '!!', '!!!', '!!', '!!!', '!!!', '!', 'X', 'X', '!!!', '!', 'O'],
                    ['#', 'X', '!!!', '!!', '!', '!!', '!!!', 'X', 'O', '#', '!!!', 'O', 'X', 'X', '!!!', 'O', '!!'],
                    ['!', '!!', '!!!', '!!!', '!', '!!!', '!', '!!!', 'X', '!!!', 'O', '#', '#', '!', 'O', 'O', 'X'],
                    ['O', 'X', '!', 'O', 'X', '!', 'O', '!', '!!!', '#', '#', '!!', '#', '#', 'X', 'X', '#'],
                    ['#', '#', 'X', '#', '!!!', '!!', '!!!', '!!', 'X', 'O', 'O', '!', '!!!', 'O', '!!', '!!', 'O'],
                    ['#', 'O', 'O', 'O', '#', '!', '!', 'O', '!!!', '!!!', '!!', '!!', 'O', '!!!', '!!!', 'X', 'O'],
                    ['O', 'X', '!!', 'O', '!!', '!', '!!!', 'X', '#', '!!', '!!!', 'O', '#', '!', '!!', '#', 'O'],
                    ['!', '!', 'X', '!!!', 'O', '#', '#', 'X', 'X', '!!', '!', '!!', '!', '!!', '!!!', '!', '!!'],
                    ['!!!', '!', 'X', '!', 'O', '!!!', 'O', '!!', 'O', '#', 'X', '!!', 'O', '!', 'X', 'O', 'O'],
                    ['#', 'X', '!', 'O', '!!!', '!!', '!', 'X', '!', 'X', '!!!', '!', 'X', '!', '!', 'X', 'X'],
                    ['!', 'O', 'X', '#', '#', '#', 'X', '!!!', '!', '!!', '!!!', 'O', '#', '!', '!!!', '!!!', 'X']
                ]
            ), 0)

    def test_4(self):
        self.assertEqual(
            check_score(
                [
                    ['X', '!!!', '#', '#', '!', '#', '!'],
                    ['!', '!', 'X', 'X', '#', 'O', '!!!'],
                    ['#', '!', '!!!', 'X', 'O', '!!!', '#'],
                    ['!!!', 'O', '#', 'O', '#', 'O', '!!!'],
                    ['!!!', '!!', '!', 'X', '#', '!!!', '!!!'],
                    ['O', '!!', '!!!', '!!!', 'X', '#', 'X'],
                    ['O', 'X', '!', '!!!', '!!!', '#', 'X']
                ]
            ), 7)

    def test_5(self):
        self.assertEqual(
            check_score(
                [
                    ['X', '!!!', 'O', '!!!', 'O', '!', '!!!', '!!', 'X', 'O', '!!', '#', '!!', '!!!', '!!', '#', '#',
                     '#', 'X', 'O'],
                    ['X', '!', '!!!', '!!!', '#', '#', '#', 'X', 'O', 'X', 'X', '!!', '!', 'X', 'X', '!!!', '!!', '!!!',
                     'X', '#'],
                    ['!!!', 'X', 'O', '!!', '!!!', '!!!', '!', '!!!', 'O', '!!!', '#', '!', '!', '!!!', '!!', '!!',
                     '!!', '!', 'O', '!'],
                    ['!!', 'X', 'X', '!!', 'X', '!!', '!!!', '!!', 'O', '#', '!!!', '!!!', '!!', '#', 'O', 'X', '!!',
                     '!', '!', '#'],
                    ['X', '!', '#', '!', 'O', '!!', 'X', 'O', '!', '#', '!!!', '!!', '!', '#', 'X', '!!', '!!!', '!',
                     'O', 'O'],
                    ['O', '!!!', 'O', 'X', '#', 'O', '#', '!!', '!!!', '!!', 'X', '!!!', 'X', 'X', '!!!', '!!!', '!',
                     'X', 'O', '!!!'],
                    ['X', '!!!', '!!', 'O', '#', 'O', '!!', 'X', '!!', '!!', '!!!', 'O', '!', '#', '!!!', '!!!', '#',
                     'X', '!', '!!!'],
                    ['!!!', '!!!', 'O', '#', '!!', '!', '#', 'O', 'X', '#', 'X', '!', '!!!', 'O', '!!!', '!!', '!',
                     '!!', 'O', '!'],
                    ['!', 'O', 'O', 'O', '!', 'O', '!!', '!', '!!', '!', '#', '!', '!!', 'X', '!', '#', 'X', '!!!', '#',
                     '!!'],
                    ['!!!', '!!', '#', 'O', '!!', 'X', '#', '!!!', 'X', 'O', '!!!', 'X', '!!', 'X', 'X', '#', '!!!',
                     '!!', '!', '#'],
                    ['O', '!!', 'X', '!!', 'X', '#', 'O', '#', '!', '!', '!!!', 'O', 'O', '!!!', '!!!', '#', '!!', '!!',
                     '!!', 'O'],
                    ['O', '#', '!!!', '#', 'X', '!', '!!', '!!', '!!!', 'X', '!', '#', '#', 'O', 'X', '#', 'O', '!',
                     '!!', 'X'],
                    ['O', '!!', '!!!', '!', '!', '#', '!!', '!!!', 'X', '!!', '#', 'O', '!!!', '!!!', '#', '#', 'O',
                     '#', 'O', 'O'],
                    ['!', '#', 'X', '!', '!!!', '!!', '!!', '#', '!', '#', 'O', '!!', '!!!', '!!!', '!!!', '!', '!',
                     '!', '!!!', '!'],
                    ['#', '!', 'O', 'X', '!!!', 'X', 'O', '!!!', '!!!', '!!', 'X', '!!', '!!', '!', '!!!', 'X', '!!!',
                     '!', '!!', 'X'],
                    ['!', '!!!', 'X', '!', '!!!', '!!!', '!!', '!!!', '#', 'X', '!!!', '!!', '#', 'X', '!!', 'O', 'O',
                     '#', '#', '#'],
                    ['!!!', 'X', '!', '!', 'O', '!!', 'O', 'X', 'O', 'O', '!', 'X', '#', '!', '!', 'O', '!!!', '#', '!',
                     '!'],
                    ['O', '#', '!!', 'X', '!!', '!', 'O', '!', '!!!', '!', 'O', 'O', 'O', '#', '!', 'O', '!!!', 'X',
                     '!!!', 'X'],
                    ['O', '!', '!!!', '!!', '!!', '#', '!!!', '!', '#', '!!', 'O', 'O', 'O', 'X', 'O', 'O', '!!!', 'X',
                     '#', '!!'],
                    ['!', 'O', '!', '!', '#', '!', 'O', 'O', 'X', 'O', '!!', '!', '!!!', '!!!', '#', '!!!', '!!', '!',
                     '!', '!!']
                ]
            ), 0)

    def test_6(self):
        self.assertEqual(
            check_score(
                [
                    ['O', '!!!', '!', '!', '!!!', '!', '#', '!!'],
                    ['!!', '#', 'O', '!!', 'X', '#', '!!!', '!!'],
                    ['!!!', '#', '!!!', '!!!', '!!!', '!!!', '!!!', '!!'],
                    ['!', '!!', 'X', 'O', '!', 'O', '#', '#'],
                    ['#', '!!!', '#', 'O', 'X', '!!', 'X', '#'],
                    ['!!!', '!!', '#', 'O', '!!!', 'X', '!!', '!'],
                    ['#', '!!!', 'O', 'X', '#', '#', '!!!', '!!!'],
                    ['!!', '#', '!!!', '!', 'X', '!!!', '!', 'O']
                ]
            ), 0)


if __name__ == "__main__":
    unittest.main()