class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #This is a very-tricky problem, can only solve if seen before
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            #end if
        #end while
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
            #end if
        #end while
        return slow

