def lengthOfLIS(nums):
    if len(nums) < 1:
        return len(nums)

    dp = [1] * (len(nums))

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)
