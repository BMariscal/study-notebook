# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
# Write a function to calculate the count of the minimum number of deletion and insertion operations.



def find_MDI(s1, s2):
  c1 = find_LCS_length(s1, s2)
  print("Minimum deletions needed: " + str(len(s1) - c1))
  print("Minimum insertions needed: " + str(len(s2) - c1))


def find_LCS_length(s1,  s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

      maxLength = max(maxLength, dp[i][j])

  return maxLength


find_MDI("abc", "fbc") # 1 deletion, 1 insertion
find_MDI("abdca", "cbda")# 2 deletions, 1 insertion
find_MDI("passport", "ppsspt")# 3 deletions, 1 insertion


