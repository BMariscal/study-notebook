# Given a number ‘n’, implement a method to count how
# many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.


def count_ways(n):
  dp = [0 for x in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  dp[2] = 1
  dp[3] = 2

  for i in range(4, n+1):
    dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

  return dp[n]


print(count_ways(5))


