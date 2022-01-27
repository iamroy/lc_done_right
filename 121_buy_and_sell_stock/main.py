import sys

def max_profit_brute_force(prices):
    max_profit = 0

    for i, val in enumerate(prices):
        for j in range(i+1, len(prices)):
            if (prices[j]-val)>max_profit:
                max_profit = prices[j]-val

    return max_profit


def max_profit(prices):
    max_profit = 0
    min_price = sys.maxsize

    for val in prices:
        if val < min_price:
            min_price = val
        elif val - min_price > max_profit:
            max_profit = val - min_price

    return max_profit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
