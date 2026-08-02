class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp, minc = 0, float('inf')
        
        for i in range(len(prices)):
            maxp = max(prices[i] - minc, maxp)

            if prices[i] < minc:
                minc = prices[i]
        
        return maxp