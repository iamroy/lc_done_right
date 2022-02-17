#238. Product of Array Except Self
#You must write an algorithm that runs in O(n) time and without using the division operation.
def productExceptSelf(nums):

    left_arr = [1]
    for i in range(0, len(nums)-1):
        left_arr.append(left_arr[i]*nums[i])
    right_arr = [1]
    j = 1
    for i in range(len(nums)-1, 0, -1):
        right_arr.append(right_arr[j-1]*nums[i])
        j += 1
    return [a*b for a,b in zip(left_arr,reversed(right_arr))]

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))