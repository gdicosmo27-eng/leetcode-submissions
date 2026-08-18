class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dup_res = []
        cur_sub = []

        def helper(i):
            if i >= len(nums):
                dup_res.append(cur_sub.copy())
                return
            
            cur_sub.append(nums[i])
            helper(i + 1)
            cur_sub.pop()
            helper(i + 1)

        helper(0)
        dup = set()
        res = []
        for r in dup_res:
            r.sort()
            r = tuple(r)
            if r not in dup:
                res.append(r)
            dup.add(r)
    
        return res

