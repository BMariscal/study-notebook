def kpalindrome(s, k):
    def func_dp(str1, str2, m, n):

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                # If first string is empty,
                # the only option is to remove
                # all characters of second string
                if not i:
                    dp[i][j] = j
                    # If second string is empty,
                # the only option is to remove
                # all characters of first string
                elif not j:
                    dp[i][j] = i
                    # If last characters are same,
                    # ignore last char
                elif (str1[i - 1] == str2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    # If last character are different,
                    # remove it and find minimum
                    dp[i][j] = 1 + min(dp[i - 1][j], (dp[i][j - 1]))

        return dp[m][n]

    l = len(s)
    # string, reversed string, m, n
    # O(mxn)
    return (func_dp(s, s[::-1], l, l) <= k * 2)