class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, cur_sum):
            if cur_sum == amount:
                return 1
            if i >= len(coins) or cur_sum > amount:
                return 0
            
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            dp[(i, cur_sum)] = dfs(i, cur_sum + coins[i]) + dfs(i + 1, cur_sum)

            return dp[(i, cur_sum)]
        
        return dfs(0, 0)