class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set()

        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return cost
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc))
        



