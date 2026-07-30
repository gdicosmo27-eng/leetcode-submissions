class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0

            return dfs(i + 1, current_sum + nums[i]) + dfs(i + 1, current_sum - nums[i])
        
        total = dfs(0, 0)

        return total