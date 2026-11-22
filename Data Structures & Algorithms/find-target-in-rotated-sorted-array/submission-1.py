class Solution:
  def search(self, nums: List[int], target) -> int:
    l = 0
    r = len(nums) -1
    ret_val = -1
    while l<=r:
      mid = (l+r)//2
      if nums[mid] == target:
        return mid
      #end if
      if nums[mid] >= nums[l]:
          #check if left space is sorted if yes discard by updating l
          if (target >= nums[l] and target <= nums[mid]):
            r = mid -1
            #print(f'Checking sorted left-array')
          else:
            l = mid+1
            #print(f'Checking Unsorted right-array')
      else:
          #check if right space is sorted if yes discard by updating r
          if (target >= nums[mid] and target <= nums[r]):
            l = mid + 1
            #print(f'Checking sorted right-array')
          else:
            #print(f'Checking Unsorted left-array')
            r = mid -1
          #end if
      #end else
      #print(f'Checking {nums[l:r+1]}')
    #end while
    return ret_val
  #end def