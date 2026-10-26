class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      #Brute force
      from collections import Counter
      count_dict = Counter(nums)
      max_val = -1
      max_key = ''
      for k, v in count_dict.items():
        if v > max_val:
            max_val = max(max_val, v)
            max_key = k
        #end if
      #end for
      return max_key