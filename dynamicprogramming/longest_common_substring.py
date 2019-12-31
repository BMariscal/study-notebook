def find_LCS_length(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(2)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      dp[i % 2][j] = 0
      if s1[i - 1] == s2[j - 1]:
        dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
        maxLength = max(maxLength, dp[i % 2][j])

  return maxLength



print(find_LCS_length("abdca", "cbda"))
print(find_LCS_length("passport", "ppsspt"))
