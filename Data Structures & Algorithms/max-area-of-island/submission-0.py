class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        max_area = 0

        def dfs(r, c):
            if (r, c) in seen:
                seen.add((r,c))
                return 0
            
            seen.add((r,c))
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0 
            if grid[r][c] == 1:
                return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c)
                if area > max_area:
                    max_area = area
        return max_area

