import unittest
from problem_set1 import *

class TestLeetCodeFunctions(unittest.TestCase):
    def test_min_sub_array_len_success(self):
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


    def test_character_replacement_success(self):
        s = "ABAB"
        k = 2
        actual = characterReplacement(s, k)
        expected = 4
        self.assertEqual(actual, expected)
        s = "AABABBA"
        k = 1
        actual = characterReplacement(s, k)
        expected = 4
        self.assertEqual(actual, expected)
        s = "ABBB"
        k = 1
        actual = characterReplacement(s, k)
        expected = 4
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    obj = TestLeetCodeFunctions()
    obj.test_min_sub_array_len_success()
    obj.test_character_replacement_success()
