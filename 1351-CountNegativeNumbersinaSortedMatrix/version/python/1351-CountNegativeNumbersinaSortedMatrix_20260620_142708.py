# Last updated: 6/20/2026, 2:27:08 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        x=0
4        for g in grid:
5
6            left,right=0,len(g)-1
7            c=0
8            while left<=right:
9
10                mid=(left+right)//2
11
12                if g[mid]<0:
13                    right=mid-1
14                
15                else:
16                    left=mid+1
17                c=len(g)-left
18            x+=c
19        return(x)
20
21                