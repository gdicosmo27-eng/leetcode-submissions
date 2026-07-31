class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def dfs(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if text1[i1] == text2[i2]:
                return 1 + dfs(i1 + 1, i2 + 1)
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            dp[(i1, i2)] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            return dp[i1, i2]

        return dfs(0, 0)

            
