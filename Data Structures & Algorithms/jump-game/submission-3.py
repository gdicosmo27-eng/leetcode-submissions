class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1 and nums[i] != 0:
            # We can jump a maximum of nums[i] forward
            # But we want to maximize the next jump too
            max_jump = nums[i]
            if i + max_jump >= len(nums) - 1:
                i += max_jump
                break
            best_jump = nums[i]
            for j in range(i + nums[i], i, -1):
                if (j - i) + nums[j] > max_jump:
                    max_jump = (j - i) + nums[j]
                    best_jump = (j - i)
            i += best_jump
        
        return i >= len(nums) - 1


            
