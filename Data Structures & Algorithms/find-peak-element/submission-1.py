class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ret_val = len(nums) - 1
        while (l<=r):
            mid = (l+r)//2
            if (mid != (len(nums) - 1)) and (nums[mid] > nums[mid+1]):
                ret_val = mid
                r=mid-1
                #break
            else:
                l=mid+1
        #end while
        return ret_val