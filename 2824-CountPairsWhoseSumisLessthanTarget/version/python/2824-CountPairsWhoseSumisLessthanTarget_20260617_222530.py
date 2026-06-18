# Last updated: 6/17/2026, 10:25:30 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3   
4        def getk(k: int)-> int:
5            c=0
6            for p in piles:
7                
8                if p<=k:
9                    c+=1
10                else:
11                    c+=(p+k-1)//k
12            #print (c)
13            return c
14
15        left,right=1,max(piles)
16        ans=right
17        while left<=right:
18            
19            mid=(left+right)//2
20
21            if getk(mid)<=h:
22                ans=mid
23                right=mid-1
24            
25            else:
26                left=mid+1
27        
28        return ans
29            
30        
31