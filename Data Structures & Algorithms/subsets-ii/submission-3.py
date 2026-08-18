class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_sub = []
        nums.sort()

        def helper(i):
            if i >= len(nums):
                res.append(cur_sub.copy())
                return
            
            cur_sub.append(nums[i])
            helper(i + 1)
            cur_sub.pop()
            
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            helper(i + 1)

        helper(0)
        return res

