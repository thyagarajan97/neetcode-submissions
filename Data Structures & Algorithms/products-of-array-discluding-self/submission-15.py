class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)
        #result_arr = [1] * len(nums)
        #build prefix
        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1] *nums[i-1]
        #build suffix
        for i in range(len(nums) - 2, -1, -1):
            suffix_arr[i] = suffix_arr[i+1] * nums[i+1]
        #build result
        #print(prefix_arr)
        #print(suffix_arr)
        result_iter = zip(prefix_arr, suffix_arr)
        return [elem[0] * elem[1] for elem in result_iter]