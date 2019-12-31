# Given a string, find the length of its Longest Palindromic Substring (LPS).
# In a palindromic string, elements read the same backward and forward.


def find_LPS_length(st):
  n = len(st)
  # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
  dp = [[False for _ in range(n)] for _ in range(n)]

  # every string with one character is a palindrome
  for i in range(n):
    dp[i][i] = True

  maxLength = 1
  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      if st[startIndex] == st[endIndex]:
        # if it's a two character string or if the remaining string is a palindrome too
        if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
          dp[startIndex][endIndex] = True
          maxLength = max(maxLength, endIndex - startIndex + 1)

  return maxLength



print(find_LPS_length("abdbca"))
print(find_LPS_length("cddpd"))
print(find_LPS_length("pqr"))
