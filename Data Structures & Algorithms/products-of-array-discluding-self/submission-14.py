class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        postfix_arr = [1] * len(nums)
        i = 1
        j = len(nums) - 2
        for _ in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
            postfix_arr[j] = postfix_arr[j + 1] * nums[j + 1]
            i+=1
            j-=1
        #end for

        return [prefix_arr[i] * postfix_arr[i] for i in range(len(nums))]
        