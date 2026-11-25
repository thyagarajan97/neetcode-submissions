class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculate_nse(heights):
            #nse array should store the index of the next-smaller element
            nse = [len(heights)] * len(heights)
            #nse = [-1] * len(heights)
            mono_stack = []
            for i in range(len(heights)-1, -1, -1):
                #Mono-increasing
                while mono_stack and  heights[mono_stack[-1]] >= heights[i]:
                    mono_stack.pop()
                #end while
                #print(mono_stack)
                if mono_stack:
                    nse[i] = mono_stack[-1]
                    #nse[i] = heights[mono_stack[-1]]
                mono_stack.append(i)
            #end for
            return nse
        #end def
        def calculate_pse(heights):
            #nse array should store the index of the next-smaller element
            #nse = [len(heights)] * len(heights)
            pse = [-1] * len(heights)
            mono_stack = []
            for i in range(len(heights)):
                #Mono-increasing
                while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                    mono_stack.pop()
                #end while
                #print(mono_stack)
                if mono_stack:
                    #nse[i] = mono_stack[-1]
                    pse[i] = mono_stack[-1]
                mono_stack.append(i)
            #end for
            return pse
        #end def
        nse = calculate_nse(heights)
        pse = calculate_pse(heights)
        max_area = 0
        for i in range(len(heights)):
            area = heights[i] * (nse[i] - pse[i] - 1)
            max_area = max(max_area, area)
        return max_area