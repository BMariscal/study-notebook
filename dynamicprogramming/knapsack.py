#python3



def knapsack_dp(profits, weights, capacity):
    n = len(profits)

    if n != len(weights) or capacity <= 0:
        return 0

    dp = [0 for i in range(capacity + 1)]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]

    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]

            profit2 = dp[c]

            dp[c] = max(profit1, profit2)

    return dp[capacity]


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7

knapsack_dp(profits, weights, capacity)

profits = [1, 22, 10, 5]
weights = [2,4,5,10]
capacity = 7

knapsack_dp(profits, weights, capacity)

#
# Items:
#  profits | weights | capacity
#     1          2        0-7
#     22         4        0-7
#    10          5        0-7
#     5          10       0-7
#