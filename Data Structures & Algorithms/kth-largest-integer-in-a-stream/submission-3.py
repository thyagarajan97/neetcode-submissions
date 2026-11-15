import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums[:k]
        self.k = k
        heapq.heapify(self.min_heap)
        for val in nums[k:]:
            if val >= self.min_heap[0]:
                heapq.heappushpop(self.min_heap, val)
            #end if
        #end for

    def add(self, val: int) -> int:
        if self.k > len(self.min_heap):
            heapq.heappush(self.min_heap , val)
        else:
            if val >= self.min_heap[0]:
                heapq.heappushpop(self.min_heap, val)
        #end if
        return self.min_heap[0]
