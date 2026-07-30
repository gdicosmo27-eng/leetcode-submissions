class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # num_coins x amount
        ROWS, COLS = len(coins), amount + 1
        dp = [float('inf') for i in range(COLS)]
        dp[0] = 0

        for i in range(ROWS):
            cur_row = [float('inf') for i in range(COLS)]
            cur_row[0] = 0
            for c in range(1, COLS):
                skip = dp[c]
                include = float('inf')
                if c >= coins[i]:
                    include = 1 + cur_row[c - coins[i]]
                cur_row[c] = min(skip, include)
            dp = cur_row
        
        return -1 if dp[COLS - 1] == float('inf') else dp[COLS - 1]
