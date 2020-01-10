
def bin_search(arr, target):
  left = 0
  right = len(arr)-1
  while left < right:
    midpoint = (left + right) // 2

    if arr[midpoint] == target:
      return True
    if target > arr[midpoint]:
      left = midpoint+1
    elif target < arr[midpoint]:
      right = midpoint-1

  return False


arr = [0,1,2,3,4,5,6,7,8,9,10,11,12]
target = 7
print("Binary Search: ")
print(bin_search(arr, target))