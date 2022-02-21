import collections
#974. Subarray Sums Divisible by K

def subarrays_div_by_k_brute_force(nums, k):
    counter = 0
    prev_arr = []
    for i in nums:
        tmp_arr = [i]
        for j in prev_arr:
            tmp_arr.append(i + j)
            if not (i + j)%k:
                counter += 1
        if not i%k:
            counter += 1
        prev_arr = tmp_arr

    return counter

# prefix sum O(N)
def subarrays_div_by_k(nums, k):
    count = collections.defaultdict(int)
    count[0] = 1
    sum_num = 0
    counter = 0
    for num in nums:
        sum_num += num
        if (sum_num % k) in count:
            counter += count[sum_num % k]
        count[sum_num % k] += 1

    return counter

if __name__ == '__main__':
    nums = [4]
    k = 5
    #nums = [5]
    #k = 9
    print(subarrays_div_by_k_brute_force(nums, k))
    print(subarrays_div_by_k(nums, k))