
def maximalSquare(matrix):
    """
    [["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]

    """

    if not matrix or not matrix[0]:
        return 0
    height = len(matrix)  # matrix height or number of rows
    width = len(matrix[0])  # matrix width or number of columns
    dp = [[1 if item == '1' else 0 for item in row] for row in matrix]
    """
    dp == matrix, where '0' are 0 and '1' are 1:
    [[1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]]

    """
    for y in range(1, height):
        for x in range(1, width):
            if matrix[y][x] == '1':
                dp[y][x] = 1 + min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][
                    x - 1])  # check cell above current, cell to left of current, cell up and left of current

    total = [max(row) for row in dp]

    """
    dp:
    [[1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 2, 2],
    [1, 0, 0, 1, 0]]

    total:
    [1, 1, 2, 1]

    """
    return max(total) ** 2