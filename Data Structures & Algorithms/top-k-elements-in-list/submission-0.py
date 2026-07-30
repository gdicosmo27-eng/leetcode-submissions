class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        heap = []
        res = set()
        
        for n in nums:
            hashmap[n] += 1
            heapq.heappush_max(heap, (hashmap[n], n))

        while k > 0:
            freq, num = heapq.heappop_max(heap)
            if num not in res:
                res.add(num)
                k -= 1
        
        return list(res)


