class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        cur_perm = []
        N = len(nums)

        def helper(i):
            if len(cur_perm) == N:
                perms.append(cur_perm.copy())
                return
            if i >= N:
                return
            
            for n in nums:
                cur_perm.append(n)
                pos = nums.index(n)
                del nums[pos]
                helper(i + 1)
    
                nums.insert(pos, n)
                cur_perm.pop()
                helper(i + 1)
        
        helper(0)
        return perms



            
