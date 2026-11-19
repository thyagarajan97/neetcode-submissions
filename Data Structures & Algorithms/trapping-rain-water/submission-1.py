class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 1
        r = len(height) - 2
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        l_max = 0
        r_max = 0
        for _ in range(len(height) - 1):
            left_max[l] = max(height[l-1], left_max[l-1])
            l+=1
            right_max[r] = max(height[r+1], right_max[r+1])
            r-=1
        #end for
        #print(left_max)
        #print(right_max)
        for i in range(len(height)):
            if (min(left_max[i], right_max[i]) - height[i]) < 0:
                continue
            water+=min(left_max[i], right_max[i]) - height[i]
        #end for
        return water