# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
# without changing the order of the remaining elements.


def find_LCS_length(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(2)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i - 1] == s2[j - 1]:
        dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
      else:
        dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

      maxLength = max(maxLength, dp[i % 2][j])

  return maxLength


print(find_LCS_length("abdca", "cbda") == 3)
print(find_LCS_length("passport", "ppsspt") == 5)
