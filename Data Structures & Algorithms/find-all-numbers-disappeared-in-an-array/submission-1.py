class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Optimized but tricky
        for num in nums:
            index = abs(num) - 1
            nums[index] = -1 * abs(nums[index])
        #end for
        result_list = []
        #print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                result_list.append(i+1)
            #end if
        #end for
        return result_list