# Last updated: 6/17/2026, 10:24:53 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        piles.sort()
4
5        def getk(k: int)-> int:
6            c=0
7            for p in piles:
8                
9                if p<=k:
10                    c+=1
11                else:
12                    c+=(p+k-1)//k
13            #print (c)
14            return c
15
16        left,right=1,max(piles)
17        ans=right
18        while left<=right:
19            
20            mid=(left+right)//2
21
22            if getk(mid)<=h:
23                ans=mid
24                right=mid-1
25            
26            else:
27                left=mid+1
28        
29        return ans
30            
31        
32