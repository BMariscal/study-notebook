"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 9.

[output] integer

The largest integer of length n.


"""

def largestNumber(n):
    return (10**n)-1


"""
Input: n: 2
Expected Output: 99


Input: n: 1
Expected Output: 9


Input:n: 7
Expected Output: 9999999


Input:n: 4
Expected Output: 9999


Input: n: 3
Expected Output: 999

"""