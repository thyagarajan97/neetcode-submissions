class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if val != nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            #end if
        #end for
        return l