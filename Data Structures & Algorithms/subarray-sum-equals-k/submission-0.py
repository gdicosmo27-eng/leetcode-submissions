class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        leftSum = 0
        res = 0

        for i in range(len(nums)):
            cache[leftSum] += 1
            leftSum += nums[i]
            res += cache[leftSum - k]
            
        return res


        
        

                    



        
