class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = {}

        def dfs(i, j):
            if i >= M:
                return N - j
            if j >= N:
                return M - i
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] =  min(1 + dfs(i + 1, j),1 + dfs(i, j + 1), 1+ dfs(i + 1, j + 1))
            return dp[(i, j)]

        return dfs(0, 0)



            
