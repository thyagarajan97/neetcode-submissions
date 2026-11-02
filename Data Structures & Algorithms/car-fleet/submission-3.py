class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        l1 = list(zip(position, speed))
        l1.sort(key = lambda x: x[0], reverse = True)
        positions = ((target-elem[0])/elem[1] for elem in l1)
        for elem in positions:
            #print(elem)
            stack.append(elem)
            if (len(stack) >= 2) and (stack[-2] >= stack[-1]):
                #merge the 2 elems to become the smaller-one
                stack.pop()
            #end if
        #end for
        return len(stack)