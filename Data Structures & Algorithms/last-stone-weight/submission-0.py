class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        
        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, -(x - y))
            
        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        else:
            return 0
            

