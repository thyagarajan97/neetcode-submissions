class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for r in range(1, len(nums)):
            #window = r - l + 1
            if nums[r] > nums[r-1]:
                curr_sum+=nums[r]
                max_sum = max(max_sum, curr_sum)
                continue
            else:
                curr_sum = nums[r]
            #end if
        #end for
        return max_sum
            
