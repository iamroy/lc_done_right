#283. Move Zeroes
def move_zeroes(nums):

    if len(nums) <= 1:
        return nums

    i,j = -1,0

    while j < len(nums):
        if nums[j] == 0 and i < 0:
            i = j
        if nums[j] != 0 and i >= 0:

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(move_zeroes(nums))