
# There are ‘n’ houses built in a line. A thief wants to steal maximum
# possible money from these houses. The only restriction the thief has is that
# he can’t steal from two consecutive houses, as that would alert the security system.
# How should the thief maximize his stealing?

def find_max_steal(wealth):
  n = len(wealth)
  if n == 0:
    return 0

  n1, n2 = 0, wealth[0]
  for i in range(1, n):
    n1, n2 = n2, max(n1 + wealth[i], n2)

  return n2



print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal([2, 10, 14, 8, 1]))
