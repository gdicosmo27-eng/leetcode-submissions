class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        nums.sort()
        res = []

        for i in range(1, len(nums) - 1):
            L, R = 0, len(nums) - 1
            while L < i and R > i:
                cur_sum = nums[i] + nums[L] + nums[R]
                if cur_sum > 0:
                    R -= 1
                elif cur_sum < 0:
                    L += 1
                else:
                    if (nums[i], nums[L], nums[R]) not in hashmap:
                        hashmap[(nums[i], nums[L], nums[R])] = True
                        res.append((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                
        return res

                

            