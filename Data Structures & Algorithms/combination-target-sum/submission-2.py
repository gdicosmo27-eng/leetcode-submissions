class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        cur_combo = []

        def backtrack(i):
            total = sum(cur_combo)
            if i >= len(nums) or total > target:
                return
            if total == target:
                combos.append(cur_combo.copy())
                return
            
            cur_combo.append(nums[i])
            backtrack(i)
            cur_combo.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return combos