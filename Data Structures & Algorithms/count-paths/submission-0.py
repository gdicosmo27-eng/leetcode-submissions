class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for i in range(m)]

        def memo(r, c, m, n, cache):
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n - 1:
                return 1
            
            cache[r][c] = (memo(r + 1, c, m, n, cache) + memo(r, c + 1, m, n, cache))
            return cache[r][c]
        
        return memo(0, 0, m, n, cache)
