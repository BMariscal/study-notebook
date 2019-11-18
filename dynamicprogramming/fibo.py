# recursive
def fib(n):
 if n <= 1:
     return n
 else:
     return fib(n-1) + fib(n-2)

# dp
def fibdp(n):
    if (n == 0): return 0
    # Initialize cache
    cache = [0 for i in range(n + 1)]
    cache[1] = 1

    # Fill cache iteratively
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    print(cache)
    return cache[n]


ans = fib(10)
print(ans)