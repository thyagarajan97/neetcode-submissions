class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l=0 #buy_index
        for r in range(len(prices)): #r is sell index
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if prices[l] > prices[r]: #A loss
                l=r
        #end for
        return max_profit