class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        result_list = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while mono_stack and temperatures[i] >= temperatures[mono_stack[-1]]:
                mono_stack.pop()
            #print(mono_stack)
            if mono_stack:
                result_list[i] = (mono_stack[-1] - i)
            #end if
            mono_stack.append(i)
        #end for
        return result_list