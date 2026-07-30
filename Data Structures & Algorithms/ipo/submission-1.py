import heapq
class twoHeap:
    def __init__(self, profits, capital):
        self.minheap = [(capital[i], profits[i]) for i in range(len(capital))]
        heapq.heapify(self.minheap)
        self.maxheap = []
        heapq.heapify_max(self.maxheap)

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        th = twoHeap(profits, capital)
        
        for i in range(k):
            while th.minheap and th.minheap[0][0] <= w:
               project = heapq.heappop(th.minheap)
               heapq.heappush_max(th.maxheap, project[1])

            if th.maxheap:
                w += heapq.heappop_max(th.maxheap)
        
        return w

            
