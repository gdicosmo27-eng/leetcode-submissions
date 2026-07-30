class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for dst, src in prerequisites:
            adj[src].append(dst)

        curCycle = set()
        finished = set()

        topSort = []

        def dfs(src):
            if src in curCycle:
                return False
            if src in finished:
                return True
            
            curCycle.add(src)
            for dst in adj[src]:
                if not dfs(dst):
                    return False
            curCycle.remove(src)
            finished.add(src)
            topSort.append(src)
            return True
        
        for i in range(numCourses):
            if i not in finished:
                if not dfs(i):
                    return []

        topSort.reverse()
        return topSort