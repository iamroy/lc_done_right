

def coin_change(coins, amount):

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_bfs(coins, amount):
    if not amount:
        return 0

    level = 0
    queue = {amount}

    coins = sorted(coins)

    while queue:
        level += 1
        next_queue = set()
        for remainder in queue:
            if remainder in coins:
                return level
            for coin in coins:
                if remainder < coin:
                    break
                else:
                    if (remainder - coin) not in queue:
                        next_queue.add(remainder - coin)

        queue = next_queue

    return -1

if __name__ == '__main__':
    #coins = [2,5]
    #amount = 3
    #coins = [1, 2147483647]
    #amount = 2
    coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

    amount = 9999
    print(coin_change(coins, amount))
    print(coin_change_bfs(coins, amount))
