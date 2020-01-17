# Find nth root a number without using a standard library function


# input:  x = 7, n = 3 (find 3rd root of 7)
# output: 1.913
#
# input:  x = 9, n = 2
# output: 3


"""
The function takes a nonnegative number x and a positive integer n,
 and returns the positive n’th root of x within an error of 0.001
 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).


"""


def root(x, n):
    if (x == 0):
        return 0

    lowerBound = 0
    upperBound = x
    approxRoot = float((upperBound + lowerBound) / 2)

    while (approxRoot - lowerBound >= 0.001):
        if (pow(approxRoot, n) > x):
            upperBound = approxRoot
        elif (pow(approxRoot, n) < x):
            lowerBound = approxRoot
        else:
            break

        approxRoot = float((upperBound + lowerBound) / 2)

    return approxRoot