class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        
        total = 0
        for i in range(0, len(nums)):
            self.prefix.append(total)
            total += nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix[right] + self.nums[right]) - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)