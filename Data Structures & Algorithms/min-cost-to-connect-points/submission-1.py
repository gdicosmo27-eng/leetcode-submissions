class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()

        heap = [[0, points[0][0], points[0][1]]]
        mst = []
        
        while heap:
            dist, x1, y1 = heapq.heappop(heap)
            if (x1, y1) in visited:
                continue
            
            visited.add((x1, y1))
            mst.append(dist)
            if len(visited) == len(points):
                return sum(mst)

            for x2, y2 in points:
                if (x2, y2) not in visited:  
                    manhattan = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, [manhattan, x2, y2])
