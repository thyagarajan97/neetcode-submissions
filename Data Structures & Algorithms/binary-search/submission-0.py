class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = (r + l)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                #search in right-half
                l = mid + 1
            else:
                r = mid -1
            #end if
        #end while
        return -1