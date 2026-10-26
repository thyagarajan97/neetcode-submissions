class MedianFinder:

    import heapq
    def __init__(self):
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.max_heap = []
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if (not self.max_heap) and (not self.min_heap):
            #First Iteration -> Add to the max-heap
            heapq.heappush(self.max_heap, -1 * num)
            return
        #end if
        #Incoming number is less than max of the max-heap
        if num < (-1 * self.max_heap[0]):
            heapq.heappush(self.max_heap, -1 * num)
        else:
            heapq.heappush(self.min_heap, num)
        #end if

        if abs(len(self.max_heap) - len(self.min_heap)) <= 1:
            return
        else:
            #Need to balance the heaps as diff > 2
            if len(self.max_heap) > len(self.min_heap):
                #Pop from max and insert into min
                heapq.heappush(self.min_heap, (- 1 * heapq.heappop(self.max_heap)))
            else:
                #Pop from min and insert to max
                heapq.heappush(self.max_heap, (-1 * heapq.heappop(self.min_heap)))
            #end if
        #end if

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            #print('equal')
            return (self.min_heap[0] + (-1 * (self.max_heap[0]))) / 2
        elif len(self.max_heap) > len(self.min_heap):
            #print('max is larger')
            return -1 * self.max_heap[0]
        else:
            #print('min is larger')
            return self.min_heap[0] 


        