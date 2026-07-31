class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(t), len(s)
        dp = [1] * (M + 1)

        for i in range(N):
            cur_row = [0] * (M + 1)
            for j in range(M):
                if s[j] == t[i]:
                    cur_row[j + 1] = cur_row[j] + dp[j]
                else:
                    cur_row[j + 1] = cur_row[j]
            dp = cur_row
        
        return dp[M]