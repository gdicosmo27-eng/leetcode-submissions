class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for ui, vi, ti in times:
            adj[ui].append([vi, ti])
        
        minHeap = [[0, k]]
        shortest = {}
        total_time = 0

        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            if u1 in shortest:
                continue
            shortest[u1] = t1
            for vi, ti in adj[u1]:
                if vi not in shortest:
                    heapq.heappush(minHeap, [t1 + ti, vi])
            total_time = shortest[u1]

        if len(shortest) != n:
            return -1
        return total_time
        