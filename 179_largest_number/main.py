#179. Largest Number
# We are using a custom comparison function for sorting
import functools

def custom_compare(n1, n2):
    #print("comparing ", n1, " and ", n2)
    if n1+n2>n2+n1:
        return -1
    else:
        return 1

def largest_number(nums):

    for i, num in enumerate(nums):
        nums[i] = str(num)
    print(nums)

    nums = sorted(nums, key=functools.cmp_to_key(custom_compare))
    largest_num = "".join(nums)
    return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    #nums = [10, 2]

    nums = [3, 30, 34, 5, 9, 91]
    print(largest_number(nums))