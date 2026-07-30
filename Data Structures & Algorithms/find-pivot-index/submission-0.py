class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for n in nums:
            prefix.append(total)
            total += n


        for i in range(len(nums)):
            pre = prefix[i]

            post = total - prefix[i + 1] if i != len(nums) - 1 else 0

            if pre == post:
                return i
        
        return -1
