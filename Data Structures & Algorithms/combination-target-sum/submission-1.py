class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []

        def helper(i, nums, target, currComb, combs):
            if sum(currComb) == target:
                combs.append(currComb.copy())
                return
            if i >= len(nums) or sum(currComb) > target:
                return

            for j in range(i, len(nums)):
                currComb.append(nums[j])
                helper(j, nums, target, currComb, combs)
                currComb.pop()

        helper(0, nums, target, [], combs)
        return combs