def removeDuplicates(nums):
    i,j =0,1
    curr_val = nums[0]

    while j<len(nums):
        if nums[j] != curr_val:
            i+=1
            nums[i] = nums[j]
            curr_val = nums[j]
        j += 1
    return i+1