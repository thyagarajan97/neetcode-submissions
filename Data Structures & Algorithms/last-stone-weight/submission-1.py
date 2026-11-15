class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        #Negate the values and create a max-heap
        #Using a max-heap as always need top values
        invert_stone = list(map(lambda x: x * -1, stones))
        
        heapq.heapify(invert_stone)
        #print(list(map(lambda x: x * -1, invert_stone)))
        while invert_stone and len(invert_stone) != 1:
            #print(f'Heap-len: {len(invert_stone)}')
            #Poppping the top-2 elements
            x = -1 * heapq.heappop(invert_stone)
            y = -1 * heapq.heappop(invert_stone)
            if x < y:
                heapq.heappush(invert_stone, -1 * (y-x))
            elif x > y:
                heapq.heappush(invert_stone, -1 * (x-y))
            #end if
        #end while
        #print(f'Heap-len: {len(invert_stone)}')
        return (invert_stone[0] * -1) if len(invert_stone) == 1 else 0