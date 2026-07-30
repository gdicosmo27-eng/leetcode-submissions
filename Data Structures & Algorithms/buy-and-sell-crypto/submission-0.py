class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        low_idx, high_idx = 0, 0
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[high_idx]:
                high_idx = r
            if prices[r] < prices[low_idx]:
                low_idx = r
                high_idx = low_idx
            
            max_profit = max(max_profit, prices[high_idx] - prices[low_idx])

            r += 1

        return max_profit
            