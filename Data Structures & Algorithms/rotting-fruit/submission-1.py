from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        minutes = 0
        fresh_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0: return 0
        while queue:
            if fresh_count == 0: break
            minutes += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[1, 0], [-1, 0], [0, -1], [0, 1]]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
                    visited.add((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes