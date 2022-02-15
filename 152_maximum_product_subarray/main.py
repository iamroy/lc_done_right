def maximum_product_subarray(nums):
    max_product = nums[0]
    min_product = nums[0]
    max_val     = nums[0]
    dp          = [nums[0]]*len(nums)

    if len(nums) >1:
        i = 1
        while i < len(nums):
            tmp_max_product = max(nums[i], max_product*nums[i], min_product*nums[i])
            tmp_min_product = min(nums[i], max_product*nums[i], min_product*nums[i])

            max_val = max(max_val, tmp_max_product)
            dp[i]   = max_val
            max_product     = tmp_max_product
            min_product     = tmp_min_product
            i += 1
    print(dp)
    return max_val


if __name__ == '__main__':
    #nums = [2, 3, 0, -2, 4, -2]
    #nums = [-4, 2, -2]
    nums = [-3,-1,-1]
    #nums = [-2, 2, -2, 2, -2, 2, -2]
    print(maximum_product_subarray(nums))