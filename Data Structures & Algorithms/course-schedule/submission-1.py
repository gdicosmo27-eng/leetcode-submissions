class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)

        visited = set()
        finished = set()

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
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True