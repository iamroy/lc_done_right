# Leet Code 66 def plus_one(nums)
# Leet Code 498 def findDiagonalOrder(mat)
# Leet Code 54 def spiralOrder(matrix)
# Leet Code 118 def generate_pascals_triangle(num_rows)
# Leet Code 1465 Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

import math

def dominantIndex(nums):
    max_val = max(nums)
    norm_nums = [number / max_val for number in nums]
    count = len([i for i in norm_nums if i<=0.5])

    if count == len(nums)-1:
        return norm_nums.index(1)

    return -1

## Leet Code 66
def plus_one(nums):

    i = len(nums)-1
    carry_over  = 1

    while i>=0:
        new_sum = nums[i]+carry_over
        print(new_sum)
        if new_sum>=10:
            nums[i] = new_sum-10
            carry_over = 1
        else:
            nums[i] = new_sum
            carry_over = 0
        i-=1

    if carry_over:
        nums.insert(0, carry_over)

    return nums

# Leet Code 498
def findDiagonalOrder(mat):
    out_list, temp_list = [], []
    n_row, n_col = len(mat), len(mat[0])

    for i in range(n_col + n_row - 1):
        temp_list.clear()
        col_id = i
        row_id = 0

        if i >= n_col:
            col_id = n_col - 1
            row_id = i - n_col + 1

        while col_id >= 0 and row_id < n_row:
            temp_list.append(mat[row_id][col_id])
            row_id += 1
            col_id -= 1

        if i == 0 or i % 2 == 0:
            out_list += temp_list[::-1]
        else:
            out_list += temp_list

    return out_list

# Leet Code 54
def spiralOrder(mat):
    seen = []
    out_list = []
    n_row, n_col = len(mat), len(mat[0])

    row_id, col_id = 0, 0
    turn = 0

    while len(seen) < n_row * n_col:

        out_list.append(mat[row_id][col_id])
        seen.append(row_id * n_col + col_id)

        if len(seen) == n_row * n_col:
            return out_list

        last_row_id, last_col_id = row_id, col_id

        valid_box_found = 0

        while not valid_box_found:

            rem = turn % 4
            row_id, col_id = last_row_id, last_col_id

            if rem == 0:
                if col_id + 1 < n_col:
                    col_id += 1
                else:
                    turn += 1
                    continue
            elif rem == 1:
                if row_id + 1 < n_row:
                    row_id += 1
                else:
                    turn += 1
                    continue
            elif rem == 2:
                if col_id - 1 >= 0:
                    col_id -= 1
                else:
                    turn += 1
                    continue
            else:
                if row_id - 1 >= 0:
                    row_id -= 1
                else:
                    turn += 1
                    continue

            if row_id * n_col + col_id in seen:
                turn += 1
            else:
                valid_box_found = 1

    return out_list

# Leet Code 118
def generate_pascals_triangle(num_rows):

    out_list = []
    if not num_rows:
        return out_list

    out_list = [[1]]

    for i in range(1, num_rows):
        new_row = [1]
        previous_row = out_list[i - 1]
        for j in range(1,i):
            new_row.append(previous_row[j-1]+previous_row[j])

        new_row.append(1)
        out_list.append(new_row)

    return out_list


def maxArea(h, w, horizontalCuts, verticalCuts):
    MOD = 10**9+7
    horizontalCuts = sorted(horizontalCuts)
    verticalCuts = sorted(verticalCuts)
    horizontalCuts.append(h)
    verticalCuts.append(w)

    maxH = horizontalCuts[0]
    maxW = verticalCuts[0]

    prev = horizontalCuts[0]

    for i in range(1, len(horizontalCuts)):
        h = horizontalCuts[i]-prev
        if h>maxH:
            maxH = h
        prev = horizontalCuts[i]

    prev = verticalCuts[0]
    for i in range(1, len(verticalCuts)):
        w = verticalCuts[i] - prev
        if w > maxW:
            maxW = w
        prev = verticalCuts[i]

    return maxH*maxW%MOD



if __name__ == '__main__':
    nums = [9]
    #print(dominantIndex(nums))
    #print(plus_one(nums))
    #mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    #print(findDiagonalOrder(mat))
    #print(spiralOrder(mat))
    #print(generate_pascals_triangle(5))

    #h = 5
    #w= 4
    #horizontalCuts = [1, 2, 4]
    #verticalCuts = [1, 3]
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    print(maxArea(h, w, horizontalCuts, verticalCuts))

