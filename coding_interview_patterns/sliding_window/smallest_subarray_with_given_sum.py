# Given an array of positive numbers and a positive number ‘S’,
# find the length of the smallest contiguous subarray whose sum
# is greater than or equal to ‘S’. Return 0, if no such subarray exists.


# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2


def smallest_subarray_with_given_sum(s, arr):
    if s in arr:
        return 1

    if len(arr) <= 2 and sum(arr) < s:
        return 0

    length_of_subarr = 1
    max_num_idx = 0
    max_num = 0

    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_num_idx = i

    if max_num >= s:
        return 1

    midpoint = max_num_idx
    left = midpoint - 1
    right = midpoint + 1

    if midpoint == 0:
        left = None

    if midpoint == len(arr) - 1:
        right = None

    while left > 0 or right < len(arr):
        if left == None:
            l_most = 0
        else:
            l_most = arr[left]

        if right == None:
            r_most = 0
        else:
            r_most = arr[right]

        if left != None and arr[midpoint] + arr[left] > arr[midpoint] + r_most:
            length_of_subarr += 1
            if sum(arr[left: midpoint + 1]) >= s:
                return length_of_subarr
            left -= 1
        elif right != None and arr[midpoint] + arr[right] > arr[midpoint] + l_most:
            length_of_subarr += 1
            if sum(arr[midpoint: right + 1]) >= s:
                return length_of_subarr
            right += 1

    return length_of_subarr


arr = [2, 1, 5, 2, 3, 2]
s = 7
smallest_subarray_with_given_sum(s, arr)






def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  min_length = float('inf')
  window_start = 0

  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  if min_length == float('inf'):
    return 0
  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [5,3, 1])))


main()