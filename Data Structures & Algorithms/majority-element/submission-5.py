class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # A very-tricky algo, will only work when same elem count > n//2
        result = 0
        elem = nums[0]
        for num in nums:
            if elem == num:
                result+=1
            else:
                result-=1
            #end if
            if result < 0:
                result = 0
                elem = num
            #end if
        #end for
        return elem