
from functools import lru_cache
def robotingrid(grid):
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def parse(m, n):
        if m == 0 and n == 0:
            return 1 - grid[0][0]

        if m < 0 or n < 0 or grid[m][n] == 1:
            return 0

        # up, left
        return parse(m - 1, n) + parse(m, n - 1)

    return parse(m - 1, n - 1)

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

robotingrid(grid)