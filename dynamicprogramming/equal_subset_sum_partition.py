#python3

# Given a set of positive numbers, find if we can partition it into two subsets such that the
# sum of elements in both the subsets is equal.


## button-up
def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with same total
  if s % 2 != 0:
    return False

  # we are trying to find a subset of given numbers that has a total sum of 's//2'.
  s = s // 2

  n = len(num)
  dp = [[False for x in range(s+1)] for y in range(n)]

  # populate the s=0 columns, as we can always for '0' sum with an empty set
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, s+1):
    dp[0][j] = num[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, s+1):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]

print(can_partition([1, 2, 3, 4]) == True)
print(can_partition([1, 1, 3, 4, 7]) == True)
print(can_partition([2, 3, 4, 6]) == False)

# top-down
def can_partition(nums):
  if sum(nums) % 2 != 0:
    return False

  target = sum(nums) / 2
  return can_partition_helper(nums, target, 0, {})


def can_partition_helper(nums, target_sum, idx, cache):
  if (idx, target_sum) in cache:
    return cache[(idx, target_sum)]

  if target_sum == 0:
    return True

  if target_sum < 0 or idx >= len(nums) or len(nums) == 0:
    return False

  result = can_partition_helper(nums, target_sum - nums[idx], idx + 1, cache) or can_partition_helper(nums, target_sum,
                                                                                                      idx + 1, cache)
  cache[(idx, target_sum)] = result
  return result


a = can_partition([1, 5, 11, 5])
b = can_partition([1, 2, 3, 5])

print(a, b)