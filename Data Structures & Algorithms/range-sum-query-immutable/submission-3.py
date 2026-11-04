class NumArray:

    #Using cummulative sum to make the searching more efficient
    def __init__(self, nums: List[int]):
        self.nums = nums
        #Padding a extra 0 at the end to skip the if-condition check
        self.cumm_sum = [0] + [0] * len(nums)
        self.cumm_sum[1] = nums[0]
        for i in range(1, len(nums)):
            self.cumm_sum[i + 1] = self.cumm_sum[i+1-1] + self.nums[i]
        #end for
        print(self.cumm_sum)

    def sumRange(self, left: int, right: int) -> int:
        return (self.cumm_sum[right+1] - self.cumm_sum[left + 1 - 1])
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)