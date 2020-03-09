def power_set(nums):
    res = []
    index = len(nums) - 1
    parse(nums, res, index)
    return res


import copy

def parse(nums, res, index):
    if index == -1:
        res.append([])
        return

    parse(nums, res, index - 1)
    subarr = copy.deepcopy(res)
    for i in subarr:
        i.append(nums[index])

    res.extend(subarr)
    return res


print(power_set([1, 3, 7]))