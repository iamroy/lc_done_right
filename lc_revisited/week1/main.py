import unittest
from problem_set1 import *

class TestLeetCodeFunctions(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        expected = 2
        actual = minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)
        target = 4
        nums = [1, 4, 4]
        expected = 1
        actual = minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        expected = 0
        actual = minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    obj = TestLeetCodeFunctions()
    obj.test_add_fish_to_aquarium_success()
