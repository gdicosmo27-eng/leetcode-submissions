class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda point: (point[0]**2 + point[1]**2, point)
        min_heap = list(map(distance, points))
        heapq.heapify(min_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res