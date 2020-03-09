

from collections import Counter
def permutations(string):
  c = Counter(string)
  idx = 0
  res = []
  stack = [0] * len(string)
  def parse(c, res, idx, stack):
    if idx == len(stack):
      res.append("".join(stack[::]))
      return
    for key in c:
      if c[key] > 0:
        stack[idx] = key
        c[key]-=1
        parse(c, res, idx+1, stack)
        c[key]+=1

  parse(c, res, idx, stack)
  return res


string = "aaabc"
print(permutations(string))