class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        hashmap[nums[0]] = 0
        R = 1

        while R < len(nums):
            if hashmap.get(target - nums[R], -1) >= 0:
                return [hashmap[target - nums[R]], R]
            else:
                hashmap[nums[R]] = R
                R += 1