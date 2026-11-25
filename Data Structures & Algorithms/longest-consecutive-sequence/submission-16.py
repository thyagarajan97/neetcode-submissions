class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) == 1:
            return 1
        if len(nums_set) == 0:
            return 0
        max_count = 1
        count = 1
        for num in nums_set:
            if num-1 not in nums_set: #indicates we have reached a left-boundary
                elem = num
                #Then keep checking forward
                while ((elem+1) in nums_set):
                    elem = elem+1
                    count+=1
                #end while
                max_count = max(count, max_count)
                count = 1
            #end if
        return max_count
            