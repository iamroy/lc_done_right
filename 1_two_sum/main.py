def two_sum_brute_force(nums, target):
    ind1 = []
    ind2 = []

    for i in range(0, len(nums)-1):
        rem = target-nums[i]
        for j in range(i+1, len(nums)):
            if rem == nums[j]:
                return i, j

    return ind1,ind2


def two_sum_optimized(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        other = target - num

        if other in seen:
            return [seen[other], index]
        else:
            seen[num] = index

    return []


if __name__ == '__main__':
    nums = [3,1,2,7,3]
    target = 6
    print(two_sum_brute_force(nums, target))
    print(two_sum_optimized(nums, target))