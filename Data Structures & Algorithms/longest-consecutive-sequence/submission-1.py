class UnionFind:
    def __init__(self, nums):
        self.par = {}
        self.rank = {}

        for n in nums:
            self.par[n] = n
            self.rank[n] = 1
    
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]   # add sizes together
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        if not nums:
            return 0
        maxRank = 1

        for n in nums:
            if (n + 1) in uf.par:
                uf.union(n, n + 1)
            parent = uf.find(n)
            maxRank = max(maxRank, uf.rank[parent])
        
        return maxRank
        