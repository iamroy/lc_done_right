
def two_sum(numbers, target):
    i, j = 0, len(numbers)-1

    while i<j:
        sum_val = numbers[i]+numbers[j]
        if sum_val == target:
            return [i+1, j+1]
        elif sum_val > target:
            j -= 1
        else:
            i += 1


if __name__ == '__main__':
    #numbers = [2, 7, 11, 15]
    #numbers = [2, 3, 4]
    numbers = [-1, 0]
    target = -1

    print(two_sum(numbers, target))