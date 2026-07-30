import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        available = [(capital[i], profits[i]) for i in range(len(capital))]
        heapq.heapify(available)
        profits = []
        heapq.heapify_max(profits)

        for i in range(k):
            while available and available[0][0] <= w:
                temp = heapq.heappop(available)
                heapq.heappush_max(profits, temp[1])
            if profits:
                w += heapq.heappop_max(profits)
        return w