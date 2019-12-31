# Given a stair with ‘n’ steps, implement a method to count
#  how many possible ways are there to reach the top of the
#  staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.


def count_ways(n):
  if n < 2:
    return 1
  if n == 2:
    return 2
  n1, n2, n3 = 1, 1, 2
  for i in range(3, n+1):
    n1, n2, n3 = n2, n3, n1+n2+n3
  return n3




print(count_ways(3))
print(count_ways(4))
print(count_ways(5))


