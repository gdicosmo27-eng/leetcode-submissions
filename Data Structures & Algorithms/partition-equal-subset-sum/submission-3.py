class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = set()
        dp.add(0)

        for n in nums:
            dp_next = set()
            for p in dp:
                dp_next.add(p)
                dp_next.add(p + n)
            dp = dp_next
        
        return target in dp