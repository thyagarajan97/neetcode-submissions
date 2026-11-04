class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Brute-force
        result_set = set([i for i in range(1, len(nums) + 1)])
        for num in nums:
            if num in result_set:
                result_set.remove(num)
        #end for
        return list(result_set)