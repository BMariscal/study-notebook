def steps(n):
    if n == 0:
        return 1
    if n < 3:
        return n

    n1, n2, n3 = 1, 1, 2
    for i in range(3, n + 1):
        n1, n2, n3 = n2, n3, n1 + n2 + n3

    return n3


print(steps(3))
print(steps(4))

# Visualization: https://media.geeksforgeeks.org/wp-content/uploads/2-3.jpg