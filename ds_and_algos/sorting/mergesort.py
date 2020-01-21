
# n*log(n) and stable

def mergeSort(arr):
  lstlen = len(arr)
  if lstlen == 0 or lstlen == 1:
    return arr[:lstlen]

  midpoint = lstlen // 2
  arr1 = arr[0:midpoint]
  arr2 = arr[midpoint:lstlen]
  newarr1 = mergeSort(arr1)
  newarr2 = mergeSort(arr2)
  newarr = sort(newarr1, newarr2)
  return newarr


def sort(arr1, arr2):
  newlst = []
  idxarr1 = 0
  idxarr2 = 0

  while idxarr1 < len(arr1) and idxarr2 < len(arr2):
    if arr1[idxarr1] <= arr2[idxarr2]:
      newlst.append(arr1[idxarr1])
      idxarr1 += 1
    else:
      newlst.append(arr2[idxarr2])
      idxarr2 += 1
  newlst.extend(arr1[idxarr1:])
  newlst.extend(arr2[idxarr2:])
  return newlst


# Not sorted in place
arr = [2, 9, 7, 4, 6, 1]
newarr = mergeSort(arr)
print(newarr)



