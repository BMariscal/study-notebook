def n_queens(n):
    res = []
    path = []
    index = 0
    nums = [-1] * n

    def backtracking(nums, index, path):
        if index == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            nums[index] = i
            if is_valid(nums, index):
                temp = "." * len(nums)
                backtracking(nums, index + 1, path + [temp[:i] + "Q" + temp[i + 1:]])

    def is_valid(nums, index):
        for i in range(index):
            if abs(nums[i] - nums[index]) == index - i or nums[i] == nums[index]:
                return False

        return True

    backtracking(nums, index, path)
    return res


n = 8
print(n_queens(n))