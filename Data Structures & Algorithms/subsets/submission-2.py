class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Can either include or not include each number
        res = []
        cur_set = []
        
        def backtrack(idx):
            if idx >= len(nums):
                res.append(cur_set.copy())
                return
            
            cur_set.append(nums[idx])
            backtrack(idx + 1)
            cur_set.pop()
            backtrack(idx + 1)
        
        backtrack(0)
        return res
            
