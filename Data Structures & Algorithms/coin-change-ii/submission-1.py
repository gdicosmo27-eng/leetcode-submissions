class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        N = len(coins)
        dp = [[0 for i in range(amount + 1)] for i in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(N - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]

