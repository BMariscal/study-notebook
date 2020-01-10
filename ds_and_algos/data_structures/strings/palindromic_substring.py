
def palindromic_substring(s):
    res = len(s)
    d = {}

    for i ,e in enumerate(s):
        if e not in d:
            d[e] = i
        else:
            previous_idx = d[e]
            current_idx = i
            current_chunk = s[previous_idx: current_idx +1]
            if current_chunk[::-1] == current_chunk: res+=1
                d[e] = i

    return res

print(


"Palindromic Substring: ")
s = "asasd"
print(palindromic_substring(s) == 7)

s = "abcbaba"
print(palindromic_substring(s) == 11)