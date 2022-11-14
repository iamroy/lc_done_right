
#209: Minimum Size Subarray Sum
#424: Longest Repeating Character Replacement
#904
#1493
#2213
import sys

# O(n) time complexity, single traversal
# O(1) space complexity
def minSubArrayLen(target, nums):
    min_len = sys.maxsize
    l, r = 0, 0
    sub_arr_sum = 0
    while r < len(nums):
        sub_arr_sum += nums[r]

        while sub_arr_sum >= target:
            min_len = min(min_len, r - l + 1)
            sub_arr_sum -= nums[l]
            l += 1
        r += 1

    if min_len == sys.maxsize:
        min_len = 0

    return min_len


# O(n) time complexity, single traversal
# O(m) space complexity, where m is number of unique characters
def characterReplacement(s, k):
    max_len = 0
    chars_dict = dict()
    l, r = 0, 0
    max_freq = 0

    while r < len(s):
        chars_dict[s[r]] = chars_dict.get(s[r], 0) + 1
        max_freq = max(max_freq, chars_dict[s[r]])
        if not max_freq + k >= r - l + 1:
            chars_dict[s[l]] -= 1
            l += 1
        max_len = r - l + 1

        r += 1

    return max_len
