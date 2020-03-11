def regularExpressionMatching(s, p):
    if not p:
        return not s

    first_match = s and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return bool((regularExpressionMatching(s, p[2:]) or
                     first_match and regularExpressionMatching(s[1:], p)))
    else:
        return bool(first_match and regularExpressionMatching(s[1:], p[1:]))

