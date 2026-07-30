class Solution:
    def helper(self, i, nums, curSub, subsets):
        if i >= len(nums):
            subsets.append(curSub.copy())
            return
        
        # Include the number at current index
        curSub.append(nums[i])
        self.helper(i + 1, nums, curSub, subsets)
        curSub.pop()
        
        # Do not include the number at current index
        self.helper(i + 1, nums, curSub, subsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curSub = []

        self.helper(0, nums, curSub, subsets)
        return subsets