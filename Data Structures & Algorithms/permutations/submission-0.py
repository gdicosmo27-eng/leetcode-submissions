class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            nextperm = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    nextperm.append(pCopy)
            perms = nextperm
        
        return perms