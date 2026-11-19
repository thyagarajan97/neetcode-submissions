class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute force
        max_water = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            water = (r - l)  * min(heights[l], heights[r])
            max_water = max(water, max_water)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            #end if
        #end while
        return max_water