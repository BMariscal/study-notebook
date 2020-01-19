
# In computer science, counting sort is an algorithm for sorting a collection of objects
# according to keys that are small integers; that is, it is an integer sorting algorithm.
# It operates by counting the number of objects that have each distinct key value, and using
# arithmetic on those counts to determine the positions of each key value in the output sequence.
# Its running time is linear in the number of items and the difference between the maximum and minimum key values,
# so it is only suitable for direct use in situations where the variation in keys is not significantly greater
# than the number of items. However, it is often used as a subroutine in another sorting algorithm, radix sort,
# that can handle larger keys more efficiently
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php


#  O(n+k) and stable
def counting_sort(self, unsorted):
    final_arr = [0] * len(unsorted)
    low = min(unsorted)
    high = max(unsorted)
    count_array = [0 for i in range(low, high + 1)]
    for i in unsorted:
        count_array[i - low] += 1
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j - 1]
    for k in reversed(unsorted):
        final_arr[count_array[k - low] - 1] = k
        count_array[k - low] -= 1
    return final_arr