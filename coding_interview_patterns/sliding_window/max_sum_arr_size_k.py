# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
#  Output: [2.2, 2.8, 2.4, 3.6, 2.8]


def max_sum_arr_size_k(arr, k):
    ans = []
    windowStart, windowSum = 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            ans.append(windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1

    return max(ans)


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(max_sum_arr_size_k(arr, k))

