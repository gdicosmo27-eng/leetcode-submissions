class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
     L, R, k = 0, 0, 0
     seen = set()

     while R < len(nums):
        if nums[R] not in seen:
            seen.add(nums[R])
            R += 1
            L += 1
            k += 1
        else:
            del nums[R]
     return k
