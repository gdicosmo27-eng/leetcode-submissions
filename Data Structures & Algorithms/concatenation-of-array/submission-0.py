class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        index = 0
        while (len(ans) < 2 * len(nums)):
            for i in range (len(nums)):
                ans.append(nums[i])
                index += 1
        return ans