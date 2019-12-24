# Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way
#  that will maximize the profit. We are also given the price of every piece of length
#  ‘i’ where ‘1 <= i <= n’.
#
# Example:
#
# Lengths: [1, 2, 3, 4, 5]
# Prices: [2, 6, 7, 10, 13]
# Rod Length: 5
#
# Let’s try different combinations of cutting the rod:
#
# Five pieces of length 1 => 10 price
# Two pieces of length 2 and one piece of length 1 => 14 price
# One piece of length 3 and two pieces of length 1 => 11 price
# One piece of length 3 and one piece of length 2 => 13 price
# One piece of length 4 and one piece of length 1 => 12 price
# One piece of length 5 => 13 price
#
# This shows that we get the maximum price (14) by cutting the rod
#  into two pieces of length ‘2’ and one piece of length ‘1’.

def rod_cutting(lengths, prices, rod_length):
    dp = [0] * (rod_length + 1)
    dp[0] = 1

    for length in range(rod_length + 1):
        if lengths[0] <= length:
            dp[length] = prices[0]

    for i in range(1, len(lengths)):
        for length in range(rod_length, -1, -1):
            prices1, prices2 = 0, 0
            if lengths[i] <= length:
                prices1 = prices[i] + dp[length - lengths[i]]

            prices2 = dp[length]
            dp[length] = max(prices2, prices1)

    return dp[rod_length]


lengths = [1, 2, 3, 4, 5]
prices = [2, 6, 7, 10, 13]
rod_length = 5
print(rod_cutting(lengths, prices, rod_length) == 14)