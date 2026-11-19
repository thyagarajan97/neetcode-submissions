def calculate_nse(heights):
    mono_stack = []
    result_arr = [len(heights)] * len(heights)
    for index in range(len(heights) - 1, -1, -1):
        while (len(mono_stack) != 0) and heights[index] <= heights[mono_stack[-1]]:
            mono_stack.pop()
        #end while
        if mono_stack:
            result_arr[index] = mono_stack[-1]
        #end if
        mono_stack.append(index)
    #end for
    return result_arr

def calculate_pse(heights):
    mono_stack = []
    result_arr = [-1] * len(heights)
    for index in range(len(heights)):
        while (len(mono_stack) != 0) and heights[index] <= heights[mono_stack[-1]]:
            mono_stack.pop()
        #end while
        if mono_stack:
            result_arr[index] = mono_stack[-1]
        #end if
        mono_stack.append(index)
        #print([heights[index] for index in mono_stack])
    #end for
    return result_arr
#end def

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = calculate_pse(heights)
        nse = calculate_nse(heights)
        #Area-calculation
        max_area = 0
        for index in range(len(heights)):
            area = heights[index] * ((nse[index] - pse[index]) - 1)
            max_area = max(area, max_area)
        #end for
        return max_area