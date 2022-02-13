from collections import Counter
def top_k_frequent(nums, k):
    out = []
    frequency_dict = {}

    num_frequency = Counter(nums)
    
    for key_val in num_frequency.keys():
        frequency = num_frequency[key_val]
        if frequency not in frequency_dict:
            frequency_dict[frequency] = [key_val]
        else:
            tmp_list = frequency_dict[frequency]
            tmp_list.append(key_val)
            frequency_dict[frequency] = tmp_list

    if k > 0:
        count = 0
        sorted_frequency = sorted(frequency_dict.keys(), reverse=True)

        for values in sorted_frequency:

            count += len(frequency_dict[values])
            if count <= k:
                out += frequency_dict[values]

    return out
    # return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    #nums = [4, 1, 1, 1, 2, 2, 3]
    #k = 2
    nums = [1]
    k = 1
    print(top_k_frequent(nums, k))