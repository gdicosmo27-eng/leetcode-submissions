class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        target = total_sum // 2

        dp = set()
        dp.add(0)

        for n in nums:
            next_dp = set()
            for s in dp:
                next_dp.add(s)
                next_dp.add(s + n)
            dp = next_dp
        
        return target in dp