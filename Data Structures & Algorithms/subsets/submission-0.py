class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_set = []
        def dfs(i, result_set):
            if i>= len(nums):
                result_set.append(sub_set.copy())
                return
            #end if
            sub_set.append(nums[i])
            dfs(i+1, result_set)
            sub_set.pop()
            dfs(i+1, result_set)
        #end dfs

        result_set = []
        dfs(0, result_set)
        return result_set
