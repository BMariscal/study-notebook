from sorting import mergesort
from sorting import quicksort
from sorting import binaryinsertionsort
from sorting import timsort
from sorting import heapsort
from sorting import selectionsort
from sorting import radixsort
from sorting import shellsort
from sorting import insertionsort


unsortedList = [0,4,2,9,10,-20,30,1,5]
msort = mergesort.merge(unsortedList)
print("merge sort")
print(msort)

l = len(unsortedList)
qsort = quicksort.quickSort(unsortedList, 0, l-1)
print("quick sort")
print(unsortedList)


unsortedList = [0,4,2,9,10,-20,30,1,5]
binsertsort = binaryinsertionsort.insertion_sort(unsortedList)

print("binary insertion sort")
print(binsertsort)

timsort = timsort.timsort(unsortedList)
print("timsort")
print(timsort)

unsortedList = [0,4,2,9,10,-20,30,1,5]
heapsort = heapsort.heap_sort(unsortedList)
print("heapsort")
print(unsortedList)

unsortedList = [0,4,2,9,10,-20,30,1,5]
selectionsort = selectionsort.selection_sort(unsortedList)
print("selection sort")
print(unsortedList)


unsortedList = [0,4,2,9,10,20,30,1,5]
radixSort = radixsort.radixSort(unsortedList)
print("radix sort")
print(unsortedList)

unsortedList = [0,4,2,9,10,20,30,1,5]
shellsort = shellsort.shellSort(unsortedList)
print("shellsort")
print(unsortedList)

unsortedList = [0,4,2,9,10,20,30,1,5]
insertionsort = insertionsort.insertionSort(unsortedList)
print("insertion sort")
print(unsortedList)