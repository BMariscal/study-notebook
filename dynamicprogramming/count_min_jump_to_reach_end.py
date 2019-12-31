# Given an array of positive numbers, where each element
# represents the max number of jumps that can be made forward
# from that element, write a program to find the minimum number
# of jumps needed to reach the end of the array (starting from the
#     first element). If an element is 0, then we cannot move through that element.


def count_min_jumps(jumps):
  n = len(jumps)
  # initialize with infinity, except the first index which should be zero as we
  # start from there
  dp = [float('inf') for _ in range(n)]
  dp[0] = 0

  for start in range(n - 1):
    end = start + 1
    while end <= start + jumps[start] and end < n:
      dp[end] = min(dp[end], dp[start] + 1)
      end += 1

  return dp[n - 1]




print(count_min_jumps([2, 1, 1, 1, 4]))
print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))