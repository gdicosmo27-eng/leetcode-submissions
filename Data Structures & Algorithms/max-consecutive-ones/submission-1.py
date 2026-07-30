class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        high = count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            if count > high:
                high = count
        return high