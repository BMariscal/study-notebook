# Given an array of positive numbers, find the maximum sum of a subsequence with
#  the constraint that no 2 numbers in the sequence should be adjacent in the array.
#  So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).
# Answer the question in most efficient way.
#
# Examples :
#
# Input : arr[] = {5, 5, 10, 100, 10, 5}
# Output : 110
#
# Input : arr[] = {1, 2, 3}
# Output : 4
#
# Input : arr[] = {1, 20, 3}
# Output : 20


"""
Example:

  arr[] = {5,  5, 10, 40, 50, 35}

  incl = 5
  excl = 0

  For i = 1 (current element is 5)
  incl =  (excl + arr[i])  = 5
  excl =  max(5, 0) = 5

  For i = 2 (current element is 10)
  incl =  (excl + arr[i]) = 15
  excl =  max(5, 5) = 5

  For i = 3 (current element is 40)
  incl = (excl + arr[i]) = 45
  excl = max(5, 15) = 15

  For i = 4 (current element is 50)
  incl = (excl + arr[i]) = 65
  excl =  max(45, 15) = 45

  For i = 5 (current element is 35)
  incl =  (excl + arr[i]) = 80
  excl =  max(65, 45) = 65

And 35 is the last element. So, answer is max(incl, excl) =  80
"""


# Function to return max sum such that
# no two elements are adjacent
def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

        # return max of incl and excl
    return (excl if excl > incl else incl)


# Driver program to test above function
arr = [5, 5, 10, 100, 10, 5]
print(find_max_sum(arr))