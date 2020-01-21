# NOT stable
# O(n log n) in the best case, O(n log n) in the average case, and O(n^2) in the worst case

"""
The quick sort is in place as it doesn't require any additional storage.
 Efficiency : Merge sort is more efficient and works faster than quick sort
 in case of larger array size or datasets. Quick sort is more efficient and
  works faster than merge sort in case of smaller array size or datasets.

"""


def quickSort(arr, low, high):
  if low < high:
    p = partition(arr, low, high)
    quickSort(arr, low, p - 1)
    quickSort(arr, p + 1, high)


def partition(arr, low, high):
  i = low - 1
  pivot = arr[high]

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


# sorted in place
arr = [2, 9, 7, 4, 6]
quickSort(arr, 0, len(arr) - 1)
print(arr)

