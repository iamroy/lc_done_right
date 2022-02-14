#496. Next Greater Element I
#503. Next Greater Element II

def find_next_greater_element_stack(nums):
    out_arr = [0] * len(nums)
    stack = []
    out = {}

    for day, temp in enumerate(nums):
        while stack and nums[stack[-1]] < temp:
            out_arr[stack[-1]] = day - stack[-1]
            out[stack[-1]] = temp
            stack.pop()

        stack.append(day)
    return out

def find_next_greater_element(nums):

    n = len(nums)
    largest_number = 0
    arr_index = [-1]*n
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

    return arr_index

#496. Next Greater Element I
def next_greater_element_1(nums1, nums2):
    arr = find_next_greater_element(nums2)
    out_arr = [-1] * len(nums1)

    for i, num in enumerate(nums1):
        if num in arr.keys():
            out_arr[i] = arr[num]
    return out_arr

#503. Next Greater Element II
def next_greater_element_2(nums):
    original_arr_length = len(nums)
    nums += nums[:-1]
    out_map = find_next_greater_element_stack(nums)
    out_arr = [-1]*len(nums)

    for i in range(original_arr_length):
        if i in out_map.keys():
            out_arr[i] = out_map[i]

    return out_arr[:original_arr_length]


if __name__ == '__main__':
    #nums1 = [4, 1, 2]
    #nums2 = [1,3,4,2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4, 2, 3, 1, 5]
    #nums2 = [8, 9, 6, 7, 5, 4, 3, 10, 1]
    #nums = [1, 2, 3, 4, 3]
    nums = [1, 2, 1]
    #print(find_next_greater_element(nums2))
    #print(find_next_greater_element_stack(nums))
    #print(next_greater_element_1(nums1, nums2))
    print(next_greater_element_2(nums))