# Given a string, find the total number of palindromic substrings in it.
# Please note we need to find the total number of substrings and not subsequences.



def count_PS(st):
  n = len(st)
  # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
  dp = [[False for _ in range(n)] for _ in range(n)]
  count = 0

  # every string with one character is a palindrome
  for i in range(n):
    dp[i][i] = True
    count += 1

  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      if st[startIndex] == st[endIndex]:
        # if it's a two character string or if the remaining string is a palindrome too
        if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
          dp[startIndex][endIndex] = True
          count += 1

  return count


print(count_PS("abdbca"))
print(count_PS("cddpd"))
print(count_PS("pqr"))
print(count_PS("qqq"))
