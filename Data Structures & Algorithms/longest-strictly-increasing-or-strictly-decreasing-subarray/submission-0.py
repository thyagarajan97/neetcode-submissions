class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_increasing = 1
        l = 0
        temp = nums[l]
        #Increasing array
        for r in range(1, len(nums)):
            window = (r - l) + 1
            if nums[r] > nums[r-1]:
                longest_increasing = max(window, longest_increasing)
                continue
            else:
                l  = r
            #end if       
        #end for
        #Decreasing array
        longest_decreasing = 1
        l = 0
        for r in range(1, len(nums)):
            window = (r - l) + 1
            if nums[r] < nums[r-1]:
                longest_decreasing = max(window, longest_decreasing)
                continue
            else:
                l  = r
            #end if
        #end for
        return max(longest_increasing, longest_decreasing)