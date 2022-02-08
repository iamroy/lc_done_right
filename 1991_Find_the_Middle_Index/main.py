def findMiddleIndex(nums):
    arr_sum = sum(nums)
    left_sum = 0

    for i, x in enumerate(nums):
        if left_sum == arr_sum - x - left_sum:
            return i

        left_sum += x

    return -1

if __name__ == '__main__':
    #nums = [2, 3, -1, 8, 4]
    nums = [2, 5]
    print(findMiddleIndex(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
