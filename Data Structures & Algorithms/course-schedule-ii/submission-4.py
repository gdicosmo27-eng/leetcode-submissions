class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[b].append(a)
        
        visited = set()
        path = set()
        topSort = []

        def dfs(src):
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)

            path.add(src)
            for nxt in adj[src]:
                if not dfs(nxt):
                    return False
            path.remove(src)
            topSort.append(src)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        topSort.reverse()
        return topSort



