# Given an infinite supply of ‘n’ coin denominations and a total money amount,
# we are asked to find the minimum number of coins needed to make up that amount.
def coinChange(coins, amount):
    if not amount: return 0
    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0

    for c in coins:  # 2
        for i in range(c, amount + 1):  # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
            min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

    return min_coins[-1] if min_coins[-1] != (amount + 1) else -1