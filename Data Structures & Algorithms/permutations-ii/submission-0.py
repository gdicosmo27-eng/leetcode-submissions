class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = {()}

        for n in nums:
            nextperm = set()
            for p in perm:
                for i in range(len(p) + 1):
                    pCopy = list(p)
                    pCopy.insert(i, n)
                    nextperm.add(tuple(pCopy))
            perm = nextperm
        
        return [list(p) for p in perm]