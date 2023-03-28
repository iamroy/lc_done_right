#3: Longest Substring Without Repeating Characters
#76
#487: Max Consecutive Ones II
#567
#1423: Maximum Points You Can Obtain from Cards
#1695: Maximum Erasure Value
#2207

#3: Longest Substring Without Repeating Characters
# O(n) time complexity, single traversal
# O(m) space complexity, where m is number of unique characters
def lengthOfLongestSubstring2(s) -> int:
    start = 0
    max_len = 0
    seen_dict = dict()
    for end in range(len(s)):

        seen_dict[s[end]] = seen_dict.get(s[end], 0) + 1

        if max(seen_dict.values()) == 1:
            max_len = max(max_len, len(seen_dict.keys()))
        else:
            seen_dict[s[start]] -= 1
            if seen_dict[s[start]] == 0:
                seen_dict.pop(s[start])
            start += 1

    return max_len


#487: Max Consecutive Ones II
# O(n) time complexity, single traversal
# O(1) space complexity
def findMaxConsecutiveOnes(data) -> int:
    zero_id  = -1
    max_len = 0
    start = 0

    for end in range(len(data)):
        if data[end] == 0:

            if zero_id != -1:
                start = zero_id + 1
            zero_id = end

        max_len = max(max_len, end-start+1)

    if zero_id == -1:
        max_len = len(data)

    return max_len

#1423: Maximum Points You Can Obtain from Cards
# O(n) time complexity, single traversal
# O(1) space complexity
def maxScore(cardPoints, k) -> int:

    rem_arr_len = len(cardPoints)-k
    start = 0
    end = start+rem_arr_len-1
    sub_arr_sum = sum(cardPoints[:end+1])
    min_sum = sub_arr_sum
    end += 1

    while end>=start and end < len(cardPoints):
        sub_arr_sum = sub_arr_sum + cardPoints[end] - cardPoints[start]
        min_sum = min(min_sum, sub_arr_sum)
        end += 1
        start += 1

    max_sum = sum(cardPoints)-min_sum

    return max_sum


#1695: Maximum Erasure Value
# O(n) time complexity, single traversal
# O(m) space complexity, where m is number of unique characters
def maximumUniqueSubarray(nums) -> int:
    seen = []
    max_sum = 0
    subarr_sum = 0

    for end in range(len(nums)):

        if nums[end] in seen:
            while True:
                popped_element = seen.pop(0)
                subarr_sum -= popped_element
                if popped_element == nums[end]:
                    break

        seen.append(nums[end])
        subarr_sum += nums[end]

        max_sum = max(max_sum, subarr_sum)

    return max_sum