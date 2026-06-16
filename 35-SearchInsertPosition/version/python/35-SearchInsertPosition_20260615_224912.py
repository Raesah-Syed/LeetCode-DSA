# Last updated: 6/15/2026, 10:49:12 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        
4        if x<2:
5            return x
6
7        left,right=2,x//2
8
9        while left<=right:
10
11            mid=(left+right)//2
12
13            if mid*mid==x:
14                return mid
15            elif mid*mid<x:
16                left=mid+1
17            else:
18                right=mid-1
19        
20        return right