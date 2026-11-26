class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)
        l, r = min_weight, max_weight
        def can_carry_before_days(weights, cap, days_limit):
            curr_weight = 0
            days_to_carry = 1
            #function which tells whether we can carry the load before the given days if cap = cap
            for weight in weights:
                curr_weight = curr_weight + weight
                if curr_weight > cap:
                    days_to_carry+=1
                    curr_weight=weight
                #end if
            #end for
            if days_to_carry <= days_limit:
                return True
            return False
        #end def
        ret_val = days
        while l <= r:
            mid=(l+r)//2
            if can_carry_before_days(weights, mid, days):
                #returns True
                ret_val = mid
                #Save result and Eliminate right-space and search further to the left
                r=mid-1
            else:
                l=mid+1
        #end while
        return ret_val