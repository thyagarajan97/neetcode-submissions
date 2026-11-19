from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window_len = 0
        monotonic_queue = deque()
        ret_list = []
        for r in range(len(nums)):
            if window_len == k: #Need to get the maximum now
                #print('****Reached window-length****')
                ret_list.append(nums[monotonic_queue[0]])
                l+=1 #Sliding the window
                window_len-=1
            #end if
            while len(monotonic_queue) != 0 and l > monotonic_queue[0]:
                #print('popping left from monotonic_queue')
                monotonic_queue.popleft()
            #end if
            while len(monotonic_queue) != 0 and nums[monotonic_queue[-1]] < nums[r]:
                #print('popping right from monotonic_queue')
                monotonic_queue.pop()
            #end while
            monotonic_queue.append(r)
            window_len+=1
            #print(f'Window-length: {window_len}, deque: {[nums[item] for item in monotonic_queue]}, l = {l}, r= {r}, ret_list = {ret_list}')
            #print('------------------')
        #end for
        ret_list.append(nums[monotonic_queue[0]])
        return ret_list
    #end def
#end class