#136. Single Number
#155. Min Stack
#70. Climbing Stairs


#136. Single Number
def single_number(nums):
    return sum(set(nums)) - (sum(nums) - sum(set(nums)))

#155. Min Stack
#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return

        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][1]


#70. Climbing Stairs
def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    i = 3
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    return dp[n]


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(single_number(nums))
    obj = MinStack()
    obj.push(2)
    #obj.push(3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(climb_stairs(45))