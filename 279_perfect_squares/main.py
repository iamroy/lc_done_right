import math

# dynamic programming where we are storing values in the dp array
def num_squares(n):
    squares = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
    dp = [float('inf') for i in range(n+1)]

    dp[0] = 0

    i = 1
    while i<n+1:
        for square in squares:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)

        i += 1

    return dp[-1]

# greedy enumeration approach
def num_squares_greedy_recursion(n):

    squares = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

    def is_divided_by(k, count):
        if count == 1:
            return k in squares

        for square in squares:
            if is_divided_by(k-square, count-1):
                return True

        return False

    for count in range(1, n+1):
        if is_divided_by(n, count):
            return count

# greedy bfs based approach
def num_squares_greedy_dfs(n):
    squares = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
    level = 0
    queue = {n}

    while queue:
        level += 1
        next_queue = set()
        for remainder in queue:
            for square in squares:
                if remainder == square:
                    return level
                elif remainder<square:
                    break
                else:
                    next_queue.add(remainder-square)
        queue = next_queue

    return level

if __name__ == '__main__':
    n = 12
    print(num_squares(n))
    print(num_squares_greedy_recursion(n))
    print(num_squares_greedy_dfs(n))