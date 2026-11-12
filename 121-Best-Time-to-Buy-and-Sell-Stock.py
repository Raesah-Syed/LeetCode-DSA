class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=float(inf)
        sell=float(-inf)
        m=0
        r=0

        for p in range(0,len(prices)):

            if prices[p]<buy:
                buy=prices[p]
            
            elif prices[p]>buy:
                sell=prices[p]
                pr=sell-buy
                if pr>m:
                    m=pr
                    r=p+1
        return m