def generateParenthesis(n):
    left = n
    right = n
    string = ""
    res = []
    return dfs(left, right, string, res)


def dfs(left, right, string, res):
    if left:
        dfs(left - 1, right, string + "(", res)
    if right and left < right:
        dfs(left, right - 1, string + ")", res)
    if not right:
        res.append(string)
    return res


a = generateParenthesis(3)
print(a)