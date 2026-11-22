import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_banana_rate = 1 #At-least one banana can be consumed
        max_banana_rate = max(piles) #This is the max-rate at which bananas can be consumed
        #Helper function which will calculate if the given rate is sufficient
        def is_rate_sufficient(rate, piles, limit):
            temp_hours = 0
            for i in range(len(piles)):
                temp_hours+=math.ceil(piles[i]/rate) #Dividing the no of bananas in pile/the rate gives the no of hours needed
                #Need to round-up; i.e take the ceil value
            #end for
            return temp_hours <= limit
        #end def
        #Will give a result_set as Eg: [False, False, True, True, True]
        #i.e with rate of 1 nope, 2 nope, 3 yes, 4, yes, 5 yes
        #We need to find the 1st True
        l = min_banana_rate
        r = max_banana_rate
        final_result = -1
        #Find the 1st True
        while l<=r:
            mid = (l+r)//2
            if is_rate_sufficient(mid, piles, h) == True:
                r=mid-1
                final_result = mid
            else:
                l=mid+1
            #end if
        #end while
        return final_result
