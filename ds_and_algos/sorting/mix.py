def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def binary_search(arr, target):
    midpoint = len(arr) // 2
    left = arr[0:midpoint]
    right = arr[midpoint:]
    if target == arr[midpoint]:
        print("FOUND!", arr[midpoint])
        return target
    elif len(left) == 0:
        print("NOT FOUND!")
        return -1
    elif len(right) == 0:
        print("NOT FOUND!")
        return -1

    if target > arr[midpoint]:
        binary_search(right, target)
    else:
        binary_search(left, target)


def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2  # Finding the mid of the array
        left = unsorted_array[:mid]  # Dividing the array elements
        right = unsorted_array[mid:]  # into 2 halves

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1


arr = [9, 7, 4, 3, 2, 10, 25, 60, 0]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
b = binary_search(arr, 4)
arr1 = [9, 7, 4, 3, 2, 10, 25, 60, 0, 55, 5, 1]
c = merge_sort(arr1)
print(arr1)