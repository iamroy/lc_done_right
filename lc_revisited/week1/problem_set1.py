
#209: Minimum Size Subarray Sum
#424
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