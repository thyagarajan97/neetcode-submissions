class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decr_stack = []
        result_temp = [0] * len(temperatures)
        for index in range(len(temperatures) - 1, -1, -1):
            while ((decr_stack) and (temperatures[index] >= temperatures[decr_stack[-1]])):
                decr_stack.pop()
            #end while
            if decr_stack and (temperatures[index] < temperatures[decr_stack[-1]]):
                result_temp[index] = decr_stack[-1]
            #end if
            decr_stack.append(index)
        #end for
        result_temp = [result_temp[index]-index  if result_temp[index] != 0 else 0 for index in range(len(result_temp))]
        return result_temp