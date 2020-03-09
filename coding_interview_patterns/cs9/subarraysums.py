def subarray_sum(nums):
    #  O(n) time and uses only O(1) space.
    result = 0
    for i in range(len(nums)):
        result += nums[i] * (i + 1) * (len(nums) - i)

    return result


nums = [1, 3, 7]
p = subarray_sum(nums)
print(p)