#55. Jump Game

# recursive
def can_jump_from(start_index, nums):

    if start_index >= len(nums)-1:
        return True

    max_jump = min(start_index + nums[start_index], len(nums) - 1)
    for j in range(start_index+1, max_jump+1):
        if can_jump_from(j, nums):
            return True

    return False

def can_jump_recursive(nums):
    return can_jump_from(0, nums)

# top-down dynamic programming O(N^2)
def can_jump_2(nums):

    dp = [-1 for _ in range(len(nums))]
    dp[0] = 0

    for i in range(len(nums)):
        if dp[i] != 0:
            continue
        num = nums[i]
        if num>0:
            for j in range(1, min(len(nums)-i, num+1)):
                if dp[i+j] != 0:
                    dp[i+j] = 0

    return not dp[-1]

# O(N)
def can_jump(nums):
    last_pos = len(nums)-1

    for i in range(len(nums)-1, -1, -1):
        if i+nums[i]>=last_pos:
            last_pos = i
    return last_pos == 0

if __name__ == '__main__':
    #nums = [2, 3, 1, 1, 4]
    #nums = [3, 2, 1, 0, 4]
    #nums = [177,176,175,174,173,172,171,170,169,168,167,166,165,164,163,162,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135,134,133,132,131,130,129,128,127,126,125,124,123,122,121,120,119,118,117,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,0]
    nums = [1,2]
    #print(can_jump(nums))
    print(can_jump_recursive(nums))