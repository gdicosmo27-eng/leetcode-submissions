class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[0] * 2 for i in range(len(strs))]
        dp = {}

        for i, string in enumerate(strs):
            for c in string:
                if c == "0":
                    arr[i][0] += 1
                else:
                    arr[i][1] += 1

        def dfs(i, m_remain, n_remain):
            if i >= len(strs):
                return 0
            if m_remain == 0 and n_remain == 0:
                return 0
            if (i, m_remain, n_remain) in dp:
                return dp[(i, m_remain, n_remain)]
            
            res = dfs(i + 1, m_remain, n_remain)
            
            if m_remain >= arr[i][0] and n_remain >= arr[i][1]:
                res = max(res, 1 + dfs(i + 1, m_remain - arr[i][0], n_remain - arr[i][1]))
            dp[(i, m_remain, n_remain)] = res
            return res

        return dfs(0, m, n)

            
            


        