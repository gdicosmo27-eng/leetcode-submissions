class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]

        for n in nums:
            counts[n] += 1
        
        i = 0
        for j in range(len(counts)):
            for n in range(counts[j]):
                nums[i] = j
                i += 1
        return nums





        