#496. Next Greater Element I

def find_next_greater_element(nums):
    n = len(nums)
    largest_number = 0
    arr_index = [0]*n
    out = {}
    for index in range(n-1, -1, -1):
        current_index = index
        current_value = nums[current_index]

        if current_value>largest_number:
            largest_number = current_value
            continue

        jump_index = 1
        while not current_value<nums[jump_index+index]:
            jump_index += arr_index[jump_index+index]

        arr_index[index] = jump_index
        #print(nums[index], nums[index+arr_index[index]])
        out[nums[index]] = nums[index+arr_index[index]]

    return out

#496. Next Greater Element I
def next_greater_element_1(nums1, nums2):
    arr = find_next_greater_element(nums2)
    out_arr = [-1] * len(nums1)

    for i, num in enumerate(nums1):
        if num in arr.keys():
            out_arr[i] = arr[num]
    return out_arr


if __name__ == '__main__':
    #nums1 = [4, 1, 2]
    #nums2 = [1,3,4,2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    #nums2 = [8, 9, 6, 7, 5, 4, 3, 10, 1]
    print(find_next_greater_element(nums2))
    print(next_greater_element_1(nums1, nums2))