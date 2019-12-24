# Given an infinite supply of ‘n’ coin denominations and a total money amount,
# we are asked to find the total number of distinct ways to make up that amount.
def count_change(amount, coins):

    if amount == 0:
        return 1

    if coins == []:
        return 0

    curr = [0 for i in range(amount + 1)]
    curr[0] = 1

    for coin in coins:
        for amt in range(coin, amount + 1):
            curr[amt] += curr[amt - coin]

    return curr[-1]

print(count_change(5, [1, 2, 3]) == 5)