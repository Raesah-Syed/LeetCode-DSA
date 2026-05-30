# Last updated: 5/29/2026, 7:11:11 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        i=0
4        buy=inf
5        p=0
6        while i<len(prices):
7            if prices[i]<buy:
8                buy=prices[i]
9            elif prices[i]>buy:
10                p+=prices[i]-buy
11                buy=prices[i]
12            i=i+1
13        return(p)
14