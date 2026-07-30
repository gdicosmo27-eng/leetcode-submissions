class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []

        for i, (n1, n2) in enumerate(edges):
            adj[n1].append([succProb[i], n2])
            adj[n2].append([succProb[i], n1])
        
        maxHeap = []
        maxprob = {}
        heapq.heappush_max(maxHeap, [1, start_node])

        while maxHeap:
            succ, n1 = heapq.heappop_max(maxHeap)
            if n1 in maxprob:
                continue
            maxprob[n1] = succ
            for succ2, n2 in adj[n1]:
                if n2 not in maxprob:
                    heapq.heappush_max(maxHeap, [succ * succ2, n2])
        
        if end_node in maxprob: 
            return maxprob[end_node] 
        else:
            return 0

