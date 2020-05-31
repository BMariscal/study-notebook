TABLE = {
    "0": [""],
    "1": [""],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def r(nums, res):
    if not nums:
        fin.append(res)
        return

    for key in TABLE[nums[0]]:
        r(nums[1:], res + key)


fin = []
res = ""
nums = list("23")
r(nums, res)
print(fin)