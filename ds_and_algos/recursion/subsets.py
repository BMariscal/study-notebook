import copy


def subsets(nums, i, ans):
    if i == len(nums):
        ans.append([])
        return

    subsets(nums, i + 1, ans)
    subset = copy.deepcopy(ans)
    for item in subset:
        item.append(nums[i])

    ans.extend(subset)
    return ans


a = subsets([1, 2, 3], 0, [])
print(a)