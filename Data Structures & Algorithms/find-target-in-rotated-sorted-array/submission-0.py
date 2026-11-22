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
      if nums[mid] >= nums[l] and (target >= nums[l] and target <= nums[mid]):
          #check if left space is sorted if yes discard by updating l
          r = mid -1
          #print(f'Checking sorted left-array')
      elif nums[mid] >= nums[l]:
          #check if left space is sorted if yes discard by updating l
          l = mid +1
          #print(f'Checking Unsorted right-array')
      elif nums[mid] <= nums[r] and (target >= nums[mid] and target <= nums[r]):
          #check if right space is sorted if yes discard by updating r
          l = mid + 1
          #print(f'Checking sorted right-array')
      elif nums[mid] <= nums[r]:
          r = mid -1
          #print(f'{nums[mid]}, Searching in left-half {nums[l:r+1]}')
      #end if
      #print(f'Checking {nums[l:r+1]}')
    #end while
    return ret_val
        