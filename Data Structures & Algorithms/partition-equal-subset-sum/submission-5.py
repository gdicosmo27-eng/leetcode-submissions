class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        # Init DP array
        N, M = total // 2, len(nums)
        dp = [[False] * (N + 1) for i in range(M)]

        # Fill in 
        for r in range(M):
            dp[r][0] = True
        dp[0][nums[0]] = True

        for c in range(1, N + 1):
            for r in range(1, M):
                if dp[r - 1][c] or (c >= nums[r] and dp[r - 1][c - nums[r]]):
                    dp[r][c] = True
                
        return dp[M - 1][N]
                    
