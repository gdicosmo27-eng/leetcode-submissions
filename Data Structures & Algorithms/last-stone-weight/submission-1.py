class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            x, y = heapq.heappop_max(max_heap), heapq.heappop_max(max_heap)
            if x > y:
                heapq.heappush_max(max_heap, (x - y))
            
        return heapq.heappop(max_heap) if len(max_heap) else 0

