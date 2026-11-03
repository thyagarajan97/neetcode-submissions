class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        #Using a single pointer to keep finding the sum at every-point
        max_sum = nums[0]
        curr_sum = nums[0]
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                curr_sum+=nums[r]
                max_sum = max(max_sum, curr_sum)
                continue
            #end if
            curr_sum = nums[r]
        #end for
        return max_sum
            
