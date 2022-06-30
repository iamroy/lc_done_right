
#3. Longest Substring Without Repeating Characters
#215. Kth Largest Element in an Array
#1642. Furthest Building You Can Reach
#844. Backspace String Compare
#581. Shortest Unsorted Continuous Subarray
#1209. Remove All Adjacent Duplicates in String II
#456. 132 Pattern
#1658. Minimum Operations to Reduce X to Zero
#209. Minimum Size Subarray Sum
#525. Contiguous Array
#325. Maximum Size Subarray Sum Equals k

import heapq
import sys

#3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):

    char_dict = {}
    counter = 0
    max_len = 0
    max_previous_loc = 0

    for i, c in enumerate(s):
        if c in char_dict.keys():

            max_len = max(counter,max_len)

            if char_dict[c]>max_previous_loc:
                max_previous_loc = char_dict[c]

            counter = i-max_previous_loc
            char_dict[c] = i
        else:
            counter += 1
            char_dict[c] = i

    max_len = max(counter,max_len)

    return max_len


#215. Kth Largest Element in an Array
def findKthLargest(nums, k):

    # return sorted(nums)[-k]
    return heapq.nlargest(k, nums)[-1]


#1642. Furthest Building You Can Reach
def furthestBuilding(heights, bricks, ladders):
    ladder_allocations = []  # We'll use heapq to treat this as a min-heap.
    for i in range(len(heights) - 1):
        climb = heights[i + 1] - heights[i]
        # If this is actually a "jump down", skip it.
        if climb <= 0:
            continue
        # Otherwise, allocate a ladder for this climb.
        heapq.heappush(ladder_allocations, climb)
        # If we haven't gone over the number of ladders, nothing else to do.
        if len(ladder_allocations) <= ladders:
            continue
        # Otherwise, we will need to take a climb out of ladder_allocations
        bricks -= heapq.heappop(ladder_allocations)
        # If this caused bricks to go negative, we can't get to i + 1
        if bricks < 0:
            return i
    # If we got to here, this means we had enough to cover every climb.
    return len(heights) - 1


def furthestBuilding2(heights, bricks, ladders):

    # Helper function to check whether or not the specified building is reachable
    # from the first building with the bricks and ladders we have.
    def is_reachable(building_index):
        # Make a sorted list of all the climbs needed to get to the given building.
        climbs = []
        for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
            if h2 - h1 > 0:
                climbs.append(h2 - h1)
        climbs.sort()
        # Check whether or not we have enough bricks and ladders to cover all
        # of these climbs. Bricks will be used before ladders.
        bricks_remaining = bricks
        ladders_remaining = ladders
        for climb in climbs:
            # If there are enough bricks left, use those.
            if climb <= bricks_remaining:
                bricks_remaining -= climb
            # Otherwise, you'll have to use a ladder.
            elif ladders_remaining >= 1:
                ladders_remaining -= 1
            # And if there are no ladders either, we can't reach buildingIndex.
            else:
                return False
        return True

    # Do the binary search to find the final reachable building.
    lo = 0
    hi = len(heights) - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if is_reachable(mid):
            lo = mid
        else:
            hi = mid - 1
    return hi  # Note that return lo would be equivalent.


#844. Backspace String Compare
def backspaceCompare(s, t):
    arr_s = []
    for c in s:
        if c == '#':
            if arr_s:
                arr_s.pop()
        else:
            arr_s.append(c)

    arr_t = []
    for c in t:
        if c == '#':
            if arr_t:
                arr_t.pop()
        else:
            arr_t.append(c)

    return arr_s == arr_t


#581. Shortest Unsorted Continuous Subarray
def findUnsortedSubarray(nums):
    stack = []
    left_id = len(nums) - 1
    right_id = 0

    for i, val in enumerate(nums):
        if (not stack or stack[-1][1] <= val):
            stack.append((i, val))
        elif stack and stack[-1][1] > val:
            pop_val = stack.pop()
            left_id = min(left_id, pop_val[0])
            while stack:
                if stack[-1][1] <= val:
                    break
                else:
                    pop_val = stack.pop()
                    left_id = min(left_id, pop_val[0])

    stack = []

    for i, val in reversed(list(enumerate(nums))):

        if (not stack or stack[-1][1] >= val):
            stack.append((i, val))
        elif stack and stack[-1][1] < val:
            pop_val = stack.pop()
            right_id = max(right_id, pop_val[0])
            while stack:
                if stack[-1][1] >= val:
                    break
                else:
                    pop_val = stack.pop()
                    right_id = max(right_id, pop_val[0])

    if right_id - left_id > 0:
        return right_id - left_id + 1
    else:
        return 0


#1209. Remove All Adjacent Duplicates in String II
def removeDuplicates(s, k):

    stack = []
    for c in s:
        if not stack:
            stack.append((1, c))
        elif stack[-1][1] == c:
            if stack[-1][0] == k-1:
                j = k-1
                while j>0:

                    stack.pop()
                    j -= 1
            else:
                stack.append((stack[-1][0]+1, c))
        else:
            stack.append((1, c))

    out_arr = ''
    for c in stack:
        out_arr += c[1]
    return out_arr


#456. 132 Pattern
def find132pattern(nums):

    exclude_start = []
    for i in range(len(nums)-1):

        if i in exclude_start:
            continue

        stack = []
        for j in range(i+1, len(nums)):
            if not stack:
                if nums[j]>nums[i]:
                    stack.append(nums[j])
            elif stack[-1]>nums[j] and nums[j]>nums[i]:
                    return True
            elif stack[-1]<nums[j]:
                stack.append(nums[j])

        exclude_start = exclude_start+stack

    return False


def find132pattern2(nums):

    min_arr = []
    min_arr.append(nums[0])
    for i in range(1, len(nums)):
        min_arr.append(min(min_arr[i-1], nums[i]))

    print(min_arr)
    stack = []
    for i in range(len(nums)-1, -1, -1):
        if not stack or stack[-1]>nums[i]:
            stack.append(nums[i])
        elif stack[-1]<nums[i]:
            print(stack)
            while stack and stack[-1]<nums[i]:
                if min_arr[i]>=stack[-1]:
                    stack.pop()
                elif min_arr[i]<stack[-1]:
                    return True
            stack.append(nums[i])

    return False

#1658. Minimum Operations to Reduce X to Zero
## direct sum
def minOperations(nums, x):

    min_len = sys.maxsize
    n = len(nums)
    l = 0
    current = sum(nums)

    for r in range(n):
        current -= nums[r]
        while current<x and l<=r:
            current += nums[l]
            l += 1
        if current == x:
            min_len = min(min_len, l+n-r-1)

    return min_len if min_len != sys.maxsize else  -1

## indirect sum
def minOperations2(nums, x):

    n = len(nums)
    subarray_sum = sum(nums)-x
    max_len = -sys.maxsize
    l = 0
    current = 0

    for r in range(n):
        current += nums[r]
        while current>subarray_sum and l<=r:
            current -= nums[l]
            l += 1
        if current == subarray_sum:
            max_len = max(max_len, r-l+1)

    return n-max_len if max_len != -sys.maxsize else  -1

#209. Minimum Size Subarray Sum
def minSubArrayLen(target, nums):

    min_len = sys.maxsize
    left = 0
    tmp_sum = 0

    for i in range(len(nums)):
        tmp_sum += nums[i]
        while tmp_sum>=target:
            min_len = min(min_len, i+1-left)
            tmp_sum -= nums[left]
            left += 1

    if sum(nums)<target:
        return 0
    else:
        return min_len


#525. Contiguous Array
def findMaxLength(nums):

    hash_map = {0 : -1}
    max_len = 0
    counter = 0

    for i, val in enumerate(nums):
        if val == 0:
            counter -= 1
        else:
            counter += 1

        if counter not in hash_map.keys():
            hash_map[counter] = i
        else:
            max_len = max(max_len, i-hash_map[counter])

    return max_len


#325. Maximum Size Subarray Sum Equals k
def maxSubArrayLen(nums, k):
    max_len = 0
    current = 0
    n = len(nums)
    sum_dict = {}

    for l in range(n):
        current += nums[l]

        if current not in sum_dict.keys():
            sum_dict[current] = l

        if current == k:
            max_len = max(max_len, l + 1)

        if current - k in sum_dict.keys():
            max_len = max(max_len, l - sum_dict[current - k])

    return max_len




if __name__ == '__main__':
    s = "dvdf"
    #s = "abcabcbb"
    #s = "bbbb"
    #s = "pwwkew"
    #s = " "
    #s = "abba"
    #print(lengthOfLongestSubstring(s))
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    #nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    #k = 4
    #print(findKthLargest(nums, k))
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19, 16, 124, 41, 11, 22, 11, 12, 13, 14]
    bricks = 10
    ladders = 2

    #heights = [14, 3, 19, 3, 30]
    #bricks = 17
    #ladders = 0
    #print(heights[:])
    #heights = [4, 2, 7, 6, 9, 14, 12]
    #bricks = 5
    #ladders = 1
    #heights = [7,5,13]
    #bricks = 0
    #ladders = 0
    #print(furthestBuilding2(heights, bricks, ladders))
    s = "ab#c"
    t = "ad#c"
    s = "ab##"
    t = "c#d#"
    s = "a#c"
    t = "b"
    #print(backspaceCompare(s, t))
    nums = [2,6,4,8,10,9,15]
    #nums = [1,2,3,4]
    #print(findUnsortedSubarray(nums))
    #s = "abcd"
    #k = 2
    #s = "deeedbbcccbdaa"
    #k = 3
    #s = "pbbcggttciiippooaais"
    #k = 2
    #print(removeDuplicates(s, k))
    #nums = [1, 2, 3, 4]
    #nums = [3, 1, 4, 2]
    #nums = [-1, 3, 2, 0]
    #nums = [3, 5, 0, 3, 4, 2]
    #nums = [1,-4,2,-1,3,-3,-4,0,-3,-1]
    #nums = [-2,1,1,-2,1,1]
    #nums = [2,4,3,1]
    #print(find132pattern2(nums))
    #nums = [1, 1, 4, 2, 3]
    #x = 5
    #nums = [5, 6, 7, 8, 9]
    #x = 4
    #nums = [3, 2, 20, 1, 1, 3]
    #x = 10
    #nums = [1, 1]
    #x = 3
    #print(minOperations(nums, x))
    #print(minOperations2(nums, x))
    #nums = [2,3,1,2,4,3]
    #target = 7
    #nums = [1,4,4]
    #target = 4
    #nums = [1,1,1,1,1,1,1,1]
    #target = 11
    #print(minSubArrayLen(target, nums))
    #nums = [0,0,1,0,0,0,1,1]
    #print(findMaxLength(nums))
    nums = [1, -1, 5, -2, 3]
    k = 3
    #nums = [-2, -1, 2, 1]
    #k = 1
    print(maxSubArrayLen(nums, k))