import unittest
from problem_set2 import *

class TestLeetCodeFunctions(unittest.TestCase):

    def test_length_of_longest_substring2_success(self):

        s = "abcabcbb"
        expected = 3
        actual = lengthOfLongestSubstring2(s)
        self.assertEqual(actual, expected)
        s = "bbbbb"
        expected = 1
        actual = lengthOfLongestSubstring2(s)
        self.assertEqual(actual, expected)
        s = "pwwkew"
        expected = 3
        actual = lengthOfLongestSubstring2(s)
        self.assertEqual(actual, expected)


    def test_find_max_consecutive_ones_success(self):

        nums = [1,0,1,1,0]
        expected = 4
        actual = findMaxConsecutiveOnes(nums)
        self.assertEqual(actual, expected)
        nums = [1,0,1,1,0,1]
        expected = 4
        actual = findMaxConsecutiveOnes(nums)
        self.assertEqual(actual, expected)


    def test_max_score_success(self):

        cardPoints = [1,2,3,4,5,6,1]
        k = 3
        expected = 12
        actual = maxScore(cardPoints, k)
        self.assertEqual(actual, expected)
        cardPoints = [2,2,2]
        k = 2
        expected = 4
        actual = maxScore(cardPoints, k)
        self.assertEqual(actual, expected)
        cardPoints = [9,7,7,9,7,7,9]
        k = 7
        expected = 55
        actual = maxScore(cardPoints, k)
        self.assertEqual(actual, expected)


    def test_maximum_unique_subarray_success(self):

        nums = [4,2,4,5,6]
        expected = 17
        actual = maximumUniqueSubarray(nums)
        self.assertEqual(actual, expected)
        nums = [5,2,1,2,5,2,1,2,5]
        expected = 8
        actual = maximumUniqueSubarray(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    obj = TestLeetCodeFunctions()
    obj.test_length_of_longest_substring2_success()
    obj.test_find_max_consecutive_ones_success()
    obj.test_max_score_success()
    obj.test_maximum_unique_subarray_success()