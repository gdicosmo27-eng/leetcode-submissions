class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jump_count = 0
        
        while i < len(nums) - 1:
            max_jump = nums[i]
            best_jump = nums[i]
            if i + best_jump >= len(nums) - 1:
                jump_count += 1
                break
            for j in range(i + nums[i], i, -1):
                if (j - i) + nums[j] > max_jump:
                    max_jump = (j - i) + nums[j]
                    best_jump = (j - i)
            i += best_jump
            jump_count += 1
        
        return jump_count
