# Uses python3
import sys

def get_change(m):
    coins = [1,3,4]
    dp = [float('inf')] * (m+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, m+1):
            dp[i] = min(dp[i], dp[i-coin]+ 1)

    return dp[m]




if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
