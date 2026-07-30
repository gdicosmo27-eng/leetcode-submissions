class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        finished = set()
        topSort = []

        def dfs(src):
            if src in visited:
                return False
            if src in finished:
                return True

            visited.add(src)
            for dst in adj[src]:
                if not dfs(dst):
                    return False
            visited.remove(src)
            finished.add(src)
            topSort.append(src)
            return True
        
        for i in range(numCourses):
            if i not in finished:
                if not dfs(i):
                    return []
        
        topSort.reverse()
        return topSort