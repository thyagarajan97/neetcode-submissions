from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ret_list = []
        mono_deque = deque()
        l = 0
        for r in range(len(nums)):
            while mono_deque and nums[r] > nums[mono_deque[-1]]:
                mono_deque.pop()
            #end while
            mono_deque.append(r)
            if (r-l+1) == k:
                #print(check_window)
                ret_list.append(nums[mono_deque[0]])
                l+=1
            #end if
            if mono_deque and l > mono_deque[0]:
                mono_deque.popleft()
            #print(f'l={l}, r= {r}, {[nums[elem] for elem in mono_deque]}')
        #end for
        #ret_list.append(mono_deque[0])
        return ret_list