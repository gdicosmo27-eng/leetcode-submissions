class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, cur_max = 0, float('-inf')
        res = []
        for r in range(k):
            if nums[r] > cur_max:
                cur_max = nums[r]

        for r in range(k, len(nums)):
            res.append(cur_max)

            if nums[l] == cur_max:
                cur_max = float('-inf')
                for i in range(l + 1, r + 1):
                    if nums[i] > cur_max:
                        cur_max = nums[i]
            
            if nums[r] > cur_max:
                cur_max = nums[r]

            l += 1
        
        res.append(cur_max)

        return res

