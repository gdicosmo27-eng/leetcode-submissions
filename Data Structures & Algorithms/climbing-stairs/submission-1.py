class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        numWays = 0
        
        def memo(n, cache):
            if n == 0:
                return 1
            if n == 1:
                return memo(n - 1, cache)
            if n in cache:
                return cache[n]

            cache[n] = memo(n - 1, cache) + memo(n - 2, cache)
            return cache[n]

        numWays += memo(n, cache)

        return numWays