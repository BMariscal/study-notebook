from collections import Counter


def permuations(c, res, word):
    if len(res) == len(word):
        st = "".join(res)
        ans.append(st)
        return

    for key in c:
        if c[key] > 0:
            res.append(key)
            c[key] -= 1
            permuations(c, res, word)
            res.pop()
            c[key] += 1


# T: O(n^n)
# S: O(n!)

ans = []
word = "aabc"
c = Counter(word)
res = []
permuations(c, res, word)
print(ans)