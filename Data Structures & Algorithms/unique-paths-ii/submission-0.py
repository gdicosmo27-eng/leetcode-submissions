class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * COLS for i in range(ROWS)]

        def memo(r, c, cache):
            if r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 1:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            cache[r][c] = (memo(r + 1, c, cache) + memo(r, c + 1, cache))
            return cache[r][c]

        return memo(0, 0, cache)
        