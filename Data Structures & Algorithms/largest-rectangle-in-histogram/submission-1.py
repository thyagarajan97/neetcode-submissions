class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        max_area = 0
        stack: List[int] = []  # stores indices with increasing heights

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                top = stack.pop()
                right_wall = i - 1
                left_wall = stack[-1] if stack else -1
                width = right_wall - left_wall
                max_area = max(max_area, heights[top] * width)
            stack.append(i)

        right_wall = n - 1
        while stack:
            top = stack.pop()
            left_wall = stack[-1] if stack else -1
            width = right_wall - left_wall
            max_area = max(max_area, heights[top] * width)

        return max_area