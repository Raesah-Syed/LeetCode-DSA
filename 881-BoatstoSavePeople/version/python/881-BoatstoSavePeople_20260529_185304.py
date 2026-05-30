# Last updated: 5/29/2026, 6:53:04 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        i=0
4        j=len(height)-1
5        ma=0
6
7        while i<j:
8            area=(j-i)* min(height[i],height[j])
9            #print(area)
10            if area>ma:
11                ma=area
12            if height[i]<height[j]:
13                i=i+1
14            else:
15                j=j-1
16        return(ma)
17            