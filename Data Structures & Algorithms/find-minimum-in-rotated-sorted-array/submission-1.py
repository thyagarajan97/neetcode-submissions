class Solution:
  def findMin(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) -1
    ret_val = nums[0]
    while l<=r:
      mid = (l+r)//2
      if nums[mid] >= nums[l]:
          #check if left space is sorted if yes discard by updating l
          #left half is sorted
          ret_val = min(ret_val, nums[l])
          #Skip the left-half
          l = mid +1
          #print(f'{nums[mid]}, Searching in right-half {nums[l:r+1]}')
      elif nums[mid] <= nums[r]:
          #check if right space is sorted if yes discard by updating r
          ret_val = min(ret_val, nums[mid])
          r = mid-1
          #print(f'{nums[mid]}, Searching in left-half {nums[l:r+1]}')
      #end if
    #end while
    return ret_val
  #end def