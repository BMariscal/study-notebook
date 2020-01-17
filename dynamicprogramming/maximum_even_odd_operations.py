"""
Even-Off Operations

Given an array of non-negative integers, perform a series of operations until the array becomes empty.
Each of the operations gives a score, and the goal is to maximize the overall score, the sum of the scores from all operations. Determine the maximum possible score after performing the operations on the array.

All operations are 1-indexed and are defined as below:

1. For every odd-indexed operation, the score is incremented by the sum of all integers present in the array.

2. For every even-indexed operation, the score is decremented by the sum of all integers present in the array.

3. After every operation (odd or even), a choice to remove either the leftmost or the rightmost integer is made, in order to achieve the maximum possible score.



For example:

n = 6

integerArray = [1, 2, 3, 4, 2, 6]

Initial score = 0



The optimal operations are as follows:

1. Operation 1 is odd, so add the sum of the array to the score: score += 18 = 18, remove the 6 and integerArray = [1, 2, 3, 4, 2], sum = 12.

2. Operation 2 is even, so subtract the sum of the array: score -12 = 6. Remove the 2 and integerArray = [1, 2, 3, 4], sum = 10.

3. Operation 3 is odd, score += 10 = 16, remove the 4, integerArray = (1,2, 3), sum = 6.

4. Operation 4 is even, score -= 6 = 10, remove the 1, integerArray = [2, 3], sum = 5.

5. Operation 5 is odd, score += 5 = 15, remove the 3, integerArray = [2] sum = 2.

6. Operation 6 is even, score -= 2 = 13, Remove the 2. integerArray = []

The final answer is 13.


"""


def getMaximumScore(nums):

    preSum = [0] * (len(nums) + 1)

    for i in range(1,len(nums)+1):
        preSum[i] = preSum[i - 1] + nums[i - 1]

    isOdd = len(nums) % 2 == 1

    dp = [[0 for x in range(len(nums)+1)] for i in range(len(nums)+1)]

    for l in range(0, len(nums)+1):
        for i in range(0, len(nums)+1):
          if i + l < (len(nums)):
            if l == 0:
                if isOdd:
                    dp[i][i] = nums[i]
                else:
                    dp[i][i] = -nums[i]
                continue
            else:
                if isOdd:
                    dp[i][i + l] = max(dp[i + 1][i + l], dp[i][i + l - 1]) + preSum[i + l + 1] - preSum[i]
                else:
                    dp[i][i + l] = max(dp[i + 1][i + l], dp[i][i + l - 1]) - preSum[i + l + 1] + preSum[i]


        isOdd = not isOdd
    return dp[0][len(nums) - 1]

print("**Even odd operations: ")
nums = [1, 2, 3, 4, 2, 6]
print(getMaximumScore(nums) == 13)