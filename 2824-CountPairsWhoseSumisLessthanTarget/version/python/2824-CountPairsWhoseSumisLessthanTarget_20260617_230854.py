# Last updated: 6/17/2026, 11:08:54 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        
4        def getd(c: int):
5            d=1
6            x=0
7
8            for w in weights:
9                if x+w <=c:
10                    x+=w
11                else:
12                    d+=1
13                    x=w
14            print(d)
15            return d
16
17        left,right=max(weights),sum(weights)
18        ans=right
19
20        while left<=right:
21
22            mid=(left+right)//2
23
24            if getd(mid)<=days:
25                ans=mid
26                right=mid-1
27            
28            else:
29                left=mid+1
30        
31        return ans