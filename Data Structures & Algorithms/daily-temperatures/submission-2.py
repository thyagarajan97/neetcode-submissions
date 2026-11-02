class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decr_stack = []
        result_temp = [0] * len(temperatures)
        for index in range(len(temperatures) - 1, -1, -1):
            while ((decr_stack) and (temperatures[index] >= temperatures[decr_stack[-1]])):
                decr_stack.pop()
            #end while
            if decr_stack and (temperatures[index] < temperatures[decr_stack[-1]]):
                result_temp[index] = (decr_stack[-1] - index)
            #end if
            decr_stack.append(index)
        #end for
        return result_temp