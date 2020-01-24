# Uses python3
def calc_fib(n):
    dp = [-1] * (n+1)
    return fib(n, dp)

def fib(n, dp):
    if (n <= 1):
        return n

    if dp[n] >= 0:
        return dp[n]

    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]

n = int(input())
print(calc_fib(n))
