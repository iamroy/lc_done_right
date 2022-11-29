#75: Sort Colors
#80: Remove Duplicates from Sorted Array II
#81: Search in Rotated Sorted Array II

#75: Sort Colors
def sortColors(nums) -> None:
    i, j = 0, 0
    k = len(nums)-1
    while j <= k:
        if nums[j] < 1:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j]>1:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        else:
            j += 1

    return nums


#80: Remove Duplicates from Sorted Array II
def removeDuplicates(nums) -> int:
    k = 1
    start = 0

    for end in range(1, len(nums)):
        if nums[start] != nums[end]:
            k = 1
            start += 1
            nums[start] = nums[end]
        else:
            if k>0:
                start += 1
                nums[start] = nums[end]
                k -= 1

    return start+1, nums


#81: Search in Rotated Sorted Array II
def search(nums, target) -> bool:
    pass


if __name__ == '__main__':
    #nums = [1, 1, 1, 2, 2, 3]
    #nums = [0,0,0,0,1]
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums))
    #print(removeDuplicates(nums))
