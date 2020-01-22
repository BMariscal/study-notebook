def count_islands(grid):
    height = len(grid)
    width = len(grid[0])
    num_of_islands = 0

    for row in range(height):
        for column in range(width):
            if grid[row][column] == '1':
                num_of_islands += 1
                dfs(grid, row, column)
    return num_of_islands


def dfs(grid, row, column):
    max_row = len(grid[0]) - 1
    max_column = len(grid) - 1

    # ROW IS LESS THAN LEN OF COLUMN
    # COLUMN IS LESS THAN LEN OF ROW
    if (row > max_column) or (column > max_row):
        return
    elif grid[row][column] == '0':
        return
    else:
        grid[row][column] = '0'
        dfs(grid, row - 1, column) # UP
        dfs(grid, row + 1, column) # DOWN
        dfs(grid, row, column - 1) # LEFT
        dfs(grid, row, column + 1) # RIGHT


grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
count = count_islands(grid)
print("++++DFS connected components++++")
print(count)