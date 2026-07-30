class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(i, current_sum):
            if current_sum == target:
                return True
            if i >= len(nums) or current_sum > target:
                return False
            
            return dfs(i + 1, current_sum + nums[i]) or dfs(i + 1, current_sum)

        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        if dfs(0, 0):
            return True
        return False


