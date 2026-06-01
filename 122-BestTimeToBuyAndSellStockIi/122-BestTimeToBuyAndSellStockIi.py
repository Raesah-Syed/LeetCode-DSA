# Last updated: 5/31/2026, 11:35:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        buy=inf
        p=0
        while i<len(prices):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]>buy:
                p+=prices[i]-buy
                buy=prices[i]
            i=i+1
        return(p)
