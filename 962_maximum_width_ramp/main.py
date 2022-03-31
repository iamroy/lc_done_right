#962. Maximum Width Ramp
#Input: nums = [6,0,8,2,1,5]
#Output: 4
#Input: nums = [9,8,1,0,1,9,4,0,4,1]
#Output: 7
import bisect

# O(Nlog(N))
def max_width_ramp(A):
    stack = []
    res = 0
    for i in range(len(A))[::-1]:
        #print(stack)
        if not stack or A[i] > stack[-1][0]:
            stack.append([A[i], i])
        else:
            j = stack[bisect.bisect(stack, [A[i], i])][1]
            res = max(res, j - i)
    return res

# O(N)
def max_width_ramp2(A):
    s = []
    res = 0
    for i, a in enumerate(A):
        if not s or A[s[-1]] > a:
            s.append(i)
    for j in range(len(A))[::-1]:
        while s and A[s[-1]] <= A[j]:
            res = max(res, j - s.pop())
    return res

# O(Nlog(N))
def max_width_ramp3(A):
    table = [(a, i) for i, a in enumerate(A)]
    table = sorted(table)
    i_min = float('Inf')
    res = 0
    for a, i in table:
        res = max(res, i - i_min)
        i_min = min(i_min, i)

    return res

# O(Nlog(N))
def max_width_ramp4(A):
    ans = 0
    stack = []
    for i in range(len(A)):
        if not stack or A[stack[-1]] > A[i]:
            stack.append(i)
        else:
            lo, hi = 0, len(stack)
            while lo < hi:
                mid = (lo + hi)//2
                #mid = lo + hi >> 1
                if A[stack[mid]] <= A[i]:
                    hi = mid
                else:
                    lo = mid + 1
            ans = max(ans, i - stack[lo])
    return ans

if __name__ == '__main__':
    #nums = [6, 8, 2, 9, 1, 6]
    nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    print(max_width_ramp(nums))
    print(max_width_ramp2(nums))
    print(max_width_ramp3(nums))
    print(max_width_ramp4(nums))
