
def change(amount, coins):

    if amount == 0:
        return 1

    if coins == []:
        return 0

    curr = [0 for i in range(amount + 1)]
    curr[0] = 1

    for coin in coins:
        for amt in range(1, amount + 1):
            if amt >= coin:
                curr[amt] += curr[amt - coin]

    return curr[-1]

