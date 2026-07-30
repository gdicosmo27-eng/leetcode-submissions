class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for prereq, nxt in prerequisites:
            adj[prereq].append(nxt)
            indegree[nxt] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        topo = []

        while queue:
            node = queue.popleft()
            topo.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)   
        
        reachable = {i: set() for i in range(numCourses)}
        for node in reversed(topo):  
            for neighbor in adj[node]:
                reachable[node].add(neighbor)       
                reachable[node] |= reachable[neighbor]
                
        return [vj in reachable[uj] for uj, vj in queries]
            