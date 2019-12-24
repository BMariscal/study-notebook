
# We are given a ribbon of length ‘n’ and a set of possible ribbon lengths.
# Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths.
# Write a method that will return the count of pieces.

def count_ribbon_pieces(ribbonLengths, total):
    n = len(ribbonLengths)
    dp = [[float('-inf') for _ in range(total + 1)] for _ in range(n)]

    # populate the total=0 columns, as we don't need any ribbon to make zero total
    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for t in range(1, total + 1):
            if i > 0:  # exclude the ribbon
                dp[i][t] = dp[i - 1][t]
            # include the ribbon and check if the remaining length can be cut into available lengths
            if t >= ribbonLengths[i] and dp[i][t - ribbonLengths[i]] != float('-inf'):
                dp[i][t] = max(dp[i][t], dp[i][t - ribbonLengths[i]] + 1)

    # total combinations will be at the bottom-right corner, return '-1' if cutting is not possible
    return -1 if dp[n - 1][total] == float('-inf') else dp[n - 1][total]


ribbon_lengths = [2, 3, 5]
total = 5
print(count_ribbon_pieces(ribbon_lengths, total) == 2)

ribbon_lengths = [2, 3]
total = 7
print(count_ribbon_pieces(ribbon_lengths, total) == 3)

ribbon_lengths = [3, 5, 7]
total = 13
print(count_ribbon_pieces(ribbon_lengths, total) == 3)