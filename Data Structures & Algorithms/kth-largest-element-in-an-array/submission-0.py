class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Using a min-heap
        elems = nums[:k]
        import heapq
        heapq.heapify(elems)
        for elem in nums[k:]:
            if elem >= elems[0]:
                heapq.heappushpop(elems, elem)
            #end if
        #end for
        return elems[0]