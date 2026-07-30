class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * COLS for i in range(ROWS)]
        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                for j in range(i, COLS):
                    dp[0][j] = 0
                break
        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                for j in range(i, ROWS):
                    dp[j][0] = 0
                break
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[ROWS - 1][COLS - 1]

        
            