# Last updated: 6/9/2026, 12:10:31 AM
1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        s=[]
4        r=prices[:]
5
6        for i in range(len(prices)):
7
8            while s and prices[s[-1]]>=prices[i]:
9                ui=s.pop()
10                r[ui]-=prices[i]
11            
12            s.append(i)
13
14        return r
15
16       
17           