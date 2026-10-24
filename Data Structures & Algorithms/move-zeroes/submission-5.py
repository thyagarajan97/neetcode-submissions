class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        if len(nums) < 2:
            return nums
        for r in range(len(nums)):
            #print(f'Left = {l}, right = {r}, nums = {nums}')
            #if num is not 0 swap l and r
            if (nums[r] != 0):
                #print(f'swapping: {nums[r]}')
                nums[l + 1] = nums[r]
                l+=1
                #print(f'After swapping: {nums}')
            #end if
        #end for
        nums[l+1:] = [0] * (len(nums) - l - 1 )
        #print(nums)



        