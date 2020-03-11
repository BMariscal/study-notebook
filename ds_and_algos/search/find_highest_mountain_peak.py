
# O(Logn)
# A binary search based function
# that returns index of a peak element
def find_peak(arr, low, high, n):
    # Find index of middle element
    # (low + high)/2
    mid = low + (high - low) // 2

    # Compare middle element with its
    # neighbors (if they exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid


    # If middle element is not peak and
    # its left neighbor is greater
    # than itself, then left half must
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peak(arr, low, (mid - 1), n)

    # If middle element is not peak and
    # its right neighbor is greater
    # than itself, then right half must
    # have a peak element
    else:
        return find_peak(arr, (mid + 1), high, n)


arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
find_peak(arr, 0, n - 1, n)

