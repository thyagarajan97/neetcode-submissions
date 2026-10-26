class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        import heapq
        l1 = list(map(lambda x: int(x), nums[:k]))
        heapq.heapify(l1)
        for num in nums[k:]:
            if int(num) > l1[0]:
                heapq.heappushpop(l1, int(num))
        #end for
        
        return str(l1[0])
