import math

def max_sub_array_brute_force(nums):
    max_sum = -math.inf
    for i in range(len(nums)):
        current_subarray = 0
        for j in range(i, len(nums)):
            current_subarray += nums[j]
            max_sum = max(max_sum, current_subarray)

    return max_sum

def max_sub_array(nums):
    current_subarray = max_sum = nums[0]
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        max_sum = max(max_sum, current_subarray)

    return max_sum


if __name__ == '__main__':
    #nums = [5,4,-1,7,8]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #nums = [-2,-1]
    print(max_sub_array_brute_force(nums))
    print(max_sub_array(nums))