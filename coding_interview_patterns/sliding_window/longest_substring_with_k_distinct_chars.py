# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Input: String = "araaci", K = 2
# Output: 4
#
#
# Input: String="araaci", K=1
# Output: 2
#
# Input: String="cbbebi", K=3
# Output: 5


def longest_substring_with_k_distinct(str, k):
    ans = []  # keep track of length
    # use set() to check for distinct characters
    # pick max() from ans list

    startIdx = 0
    while startIdx < len(str):
        for endIdx in range(len(str)):
            curr_str = str[startIdx: endIdx + 1]
            curr_set = set(curr_str)
            if len(curr_set) <= k:
                ans.append(len(curr_str))
        startIdx += 1

    return max(ans)


def longest_substring_with_k_distinct(s, k):
    d = {}
    low, ret = 0, 0
    for i, c in enumerate(s):
        d[c] = i
        if len(d) > k:
            low = min(d.values())
            del d[s[low]]
            low += 1
        ret = max(i - low + 1, ret)
    return ret





str = "araaci"
k = 2
print(longest_substring_with_k_distinct(str, k) == 4)

str = "araaci"
k = 1
print(longest_substring_with_k_distinct(str, k) == 2)

str = "cbbebi"
k = 3
print(longest_substring_with_k_distinct(str, k) == 5)

