#136. Single Number


#136. Single Number
def single_number(nums):
    return sum(set(nums)) - (sum(nums) - sum(set(nums)))


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(single_number(nums))