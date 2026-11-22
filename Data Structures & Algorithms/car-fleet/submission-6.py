class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Create a tuple of pos, unit-of-time to reach target
        new_list = []
        for elem in zip(position, speed):
            new_list.append(tuple([elem[0], ((target - elem[0])/elem[1])]))
        #end for
        new_list.sort(key=lambda x: x[0],reverse = True)
        #print(new_list)
        temp_stack = [new_list[0][1]]
        #print(temp_stack)
        for elem in new_list:
            if elem[1] > temp_stack[-1]:
                temp_stack.append(elem[1])
            #end if
        #end for
        #print(temp_stack)
        return len(temp_stack)
                