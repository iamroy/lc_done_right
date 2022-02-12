
def three_sum(nums):
    nums = sorted(nums)

    out = []
    if len(nums)<3:
        return out

    zero_index = -1
    seen = {}

    for i, num in enumerate(nums):

        if num not in seen:
            seen[num] = i

        if num<=0:
            zero_index = i

    counter = 0
    for num in nums:
        if num == 0:
            counter += 1
            if counter == 3:
                out = [[0, 0, 0]]

    if zero_index == -1:
        return out


    for i in range(zero_index):
        for j in range(i+1, zero_index+1):
            sum_val = nums[i] + nums[j]

            if -sum_val in seen:
                if seen[-sum_val]>zero_index:
                    if [nums[i], nums[j], -sum_val] not in out:
                        out.append([nums[i], nums[j], -sum_val])

    for i in range(zero_index+1, len(nums)-1):
        for j in range(i+1, len(nums)):
            sum_val = nums[i] + nums[j]
            if -sum_val in seen:
                if seen[-sum_val]<=zero_index:
                    if [-sum_val, nums[i], nums[j]] not in out:
                        out.append([-sum_val, nums[i], nums[j]])

    return out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #nums = [-1, 0, 1, 2, -1, -4]
    nums = [-1, -2, 0, 0, 0]
    #nums = [1,1,-2]
    #nums = []
    #nums = [0]
    nums = [-1,0,1,0]
    print(three_sum(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
