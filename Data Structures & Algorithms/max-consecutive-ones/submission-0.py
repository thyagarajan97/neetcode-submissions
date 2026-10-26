class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        curr_cnt = 0
        for i in nums:
            if i == 0:
                max_cnt = max(curr_cnt, max_cnt)
                curr_cnt = 0
            else:
                curr_cnt +=1
            #end if
        #end for
        max_cnt = max(curr_cnt, max_cnt)
        return max_cnt
            