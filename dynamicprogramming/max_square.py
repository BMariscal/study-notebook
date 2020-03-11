def maximalSquare(matrix):
    if not matrix:
        return 0
    height = len(matrix)
    width = len(matrix[0])
    dp = [[int(j) for j in row] for row in matrix]
    print(dp)

    for x in range(1, height):
        for y in range(1, width):
            if matrix[x][y] == '1':
                dp[x][y] = 1 + min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1])

    total = [max(row) for row in dp]

    return max(total) ** 2
