class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixTotal = 0
        prefix = []
        for n in nums:
            prefixTotal += n
            prefix.append(prefixTotal)
      
        L, R = 0, 0
        minLength = float('inf')

        while R < len(nums):
            preR = prefix[R]
            preL = prefix[L - 1] if L > 0 else 0

            if preR - preL >= target:
                if minLength > (R - L) + 1:
                    minLength = (R - L) + 1
                L += 1
            else:
                R += 1
        
        return minLength if minLength < float('inf') else 0

            


            
            
