class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        l1 = list(zip(position, speed))
        l1.sort(key = lambda x: x[0], reverse = True)
        positions = ((target-elem[0])/elem[1] for elem in l1)
        for elem in positions:
            stack.append(elem)
            if (len(stack) >= 2) and (stack[-2] >= stack[-1]):
                #the 2nd element of the stack is faster than the 1st-one; hence merge by popping
                #[3, 2.5] -> 3
                stack.pop()
            #end if
        #end for
        return len(stack)