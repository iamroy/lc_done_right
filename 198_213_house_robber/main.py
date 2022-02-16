#198. House Robber
#213. House Robber II


#198. House Robber
def house_robber(nums):

    dp = [nums[0]]*len(nums)
    if len(nums) <= 1:
        return nums[0]

    for i in range(1, len(nums)):
        if i == 1:
            dp[i] = max(dp[0], nums[i])
        else:
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    #print(dp)
    return max(dp)

#198. House Robber recursive
def robFrom(index, newList, dataTable):

    if index >= len(newList):
        return 0

    if index in dataTable:
        return dataTable[index]

    dataTable[index] = max(robFrom(index + 1, newList, dataTable),
                           robFrom(index + 2, newList, dataTable) + newList[index])
    return dataTable[index]


def house_robber_recursive(nums):

    dataTable = {}

    return robFrom(0, nums, dataTable)

#213. House Robber II
#For a values [1,2,3,4], you run the linear array twice
# [1,2,3] and [2,3,4]
def house_robber2(nums):

    if len(nums) <= 2:
        return max(nums)

    dp1 = house_robber(nums[:-1])
    dp2 = house_robber(nums[1:])

    return max(dp1, dp2)

if __name__ == '__main__':
    #nums = [1, 2, 3, 2]
    #nums = [2, 7, 9, 3, 1]
    #nums = [1,2,3]
    nums = [1,2,1,1]
    #print(nums[-1])
    #print(nums[1:-1])
    #print(house_robber(nums))
    #print(house_robber_recursive(nums))
    #print(house_robber2(nums))
    print(house_robber2(nums))