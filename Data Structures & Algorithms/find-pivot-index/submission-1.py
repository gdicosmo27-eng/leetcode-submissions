class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            pre = leftSum
            leftSum += nums[i]
            post = total - leftSum

            if pre == post:
                return i
        
        return -1
