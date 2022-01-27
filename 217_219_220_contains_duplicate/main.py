from collections import OrderedDict


def contains_duplicate_extra_space(nums):
    seen = {}

    for i, val in enumerate(nums):
        if val in seen:
            return True
        else:
            seen[val] = i

    return False

def contains_duplicate_2(nums, k):

    seen = dict()

    for i, val in enumerate(nums):

        if str(val) in seen.keys() and abs(seen[str(val)]-i)<=k:
            return True
        else:
            seen[str(val)] = i
            if len(seen.keys())>k:
                del seen[str(nums[i-k])]

    return False


def contains_duplicate_3_brute_force(nums, k, t):

    for i, val in enumerate(nums):
        for j in range(i+1, min(len(nums), i+k+1)):
            print(i,j,abs(val-nums[j]))
            if abs(val-nums[j])<=t:
                return True

    return False

# Code Pending
def contains_duplicate_3_optimized(nums, k, t):
    return False

def contains_duplicate(nums):
    if len(nums)<2:
        return False

    nums = sorted(nums)

    i, j = 0,1

    while j<len(nums):
        if nums[i] == nums[j]:
            return True

        i += 1
        j += 1

    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    print(contains_duplicate_3_brute_force(nums, k, t))
    #print(contains_duplicate_extra_space(nums))
    #print(contains_duplicate(nums))
    #print(contains_duplicate_2(nums, k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
