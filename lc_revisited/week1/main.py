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

    def test_total_fruit_success(self):
        fruits = [1,2,1]
        actual = totalFruit(fruits)
        expected = 3
        self.assertEqual(actual, expected)
        fruits = [0,1,2,2]
        actual = totalFruit(fruits)
        expected = 3
        self.assertEqual(actual, expected)
        fruits = [1,2,3,2,2]
        actual = totalFruit(fruits)
        expected = 4
        self.assertEqual(actual, expected)
        fruits = [3,3,3,1,2,1,1,2,3,3,4]
        actual = totalFruit(fruits)
        expected = 5
        self.assertEqual(actual, expected)


    def test_longest_subarray_success(self):
        nums = [1,1,0,1]
        actual = longestSubarray(nums)
        expected = 3
        self.assertEqual(actual, expected)
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        actual = longestSubarray(nums)
        expected = 5
        self.assertEqual(actual, expected)
        nums = [1,1,1]
        actual = longestSubarray(nums)
        expected = 2
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    obj = TestLeetCodeFunctions()
    obj.test_min_sub_array_len_success()
    obj.test_character_replacement_success()
    obj.test_total_fruit_success()
    obj.test_longest_subarray_success()
