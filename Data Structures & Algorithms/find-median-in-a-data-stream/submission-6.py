class MedianFinder:
    import heapq
    def __init__(self):
        self.min_heap = []
        self.max_heap= []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        #For case where both are empty, insert to min-heap
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, num)
        else:
            #Comparing with the min-heap val
            if num < self.min_heap[0]:
                #Needs to be inserted to the max-heap
                heapq.heappush(self.max_heap, -1 * num)
            else:
                #Needs to be inserted to the min-heap
                heapq.heappush(self.min_heap, num)
            #end if
        #end if
        #Min-heap is larger than max-heap
        if (len(self.min_heap) - len(self.max_heap)) > 1:
            #Pop elem from min-heap and push to max-heap
            elem = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * elem)
        elif (len(self.max_heap) - len(self.min_heap)) > 1:
            #max-heap is larger than min-heap
            #Pop elem from max-heap and push to min-heap
            elem = heapq.heappop(self.max_heap) * -1
            heapq.heappush(self.min_heap, elem)
        #end if


    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        else:
            #Equal-length
            return ( (- 1 * self.max_heap[0]) + self.min_heap[0])/2
        