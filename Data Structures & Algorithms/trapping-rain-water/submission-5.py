class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        r = len(height) - 1
        #Left-max is the max-left value to the left of the index, excluding the index
        left_max = height[l]
        #right-max is the max-right value to the right of the index, excluding the index
        right_max = height[r]
        index = 0
        while l < r:
            if left_max <= right_max:
                #Move the left pointer
                l+=1
                left_max = max(left_max, height[l])
                water+=(left_max -height[l])
            else:
                #Move the right pointer
                r-=1
                right_max = max(right_max, height[r])
                water+=(right_max-height[r])
            #end if
        #end while
        return water