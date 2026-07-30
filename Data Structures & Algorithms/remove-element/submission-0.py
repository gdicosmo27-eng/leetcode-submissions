class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        init_size = len(nums)
        removed = 0
        for n in range(len(nums) -1, -1, -1):
            if nums[n] == val:
                del nums[n]
                removed += 1
        return init_size - removed
                