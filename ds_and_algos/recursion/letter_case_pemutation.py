def r(input, res, i):
    if i == len(input):
        b = "".join(res)
        arr.append(b)
        return

    if not input[i].isalpha():
        res.append(input[i])
        r(input, res, i + 1)
        res.pop()

    else:
        input[i] = input[i].upper()
        res.append(input[i])
        r(input, res, i + 1)
        res.pop()

        input[i] = input[i].lower()
        res.append(input[i])
        r(input, res, i + 1)
        res.pop()

# Time: O(2^N)
# Space: O(N)
input = "a1b1"
arr = []
res = []
a = r(list(input), res, i=0)
print(arr)
