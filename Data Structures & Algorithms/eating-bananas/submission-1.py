from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            k = left + (right - left) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / k)
            
            if totalTime > h: 
                left = k + 1
            else:
                right = k - 1
                res = k
        return res
