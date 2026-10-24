class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        invert_sum_dict = {}
        for index, num in enumerate(nums):
            invert_sum = target-num
            # print(invert_sum)
            if invert_sum_dict.get(invert_sum) is not None:
                # print('yes')
                #Target-num is present in the dict
                return sorted([index, invert_sum_dict[invert_sum]])
            else:
                invert_sum_dict[num] = index
            #end if
        #end for
    #end def