#560. Subarray Sum Equals K - dynamic programming
def subarray_sum_1(nums, target):
    counter = 0
    prev_list = []
    for i in range(len(nums)):
        element_count = len(prev_list)
        tmp_list = []
        for j in range(element_count):
            tmp_list.append(prev_list[j] + nums[i])
            if (prev_list[j] + nums[i]) == target:
                counter += 1
        tmp_list.append(nums[i])
        if nums[i] == target:
            counter += 1
        prev_list = tmp_list
    return counter

#560. Subarray Sum Equals K - iterative
def subarray_sum_2(nums, target):
    counter = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if (sum == k):
                counter += 1
    return counter

#560. Subarray Sum Equals K - hash map
def subarray_sum_3(nums, target):
    element_sum, counter = 0, 0
    hash_map = {}
    hash_map[0] = 1

    for i in range(len(nums)):
        element_sum += nums[i]

        if (element_sum - target) in hash_map:
            counter += hash_map[element_sum - target]
        if element_sum in hash_map:
            hash_map[element_sum] += 1
        else:
            hash_map[element_sum] = 1

    return counter

if __name__ == '__main__':
    #nums = [1, 1, 1]
    #k = 2
    nums = [1, 2, 3]
    k = 3
    print(subarray_sum_1(nums, k))
    print(subarray_sum_2(nums, k))
    print(subarray_sum_3(nums, k))