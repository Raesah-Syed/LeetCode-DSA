# Last updated: 5/31/2026, 11:36:09 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        ma=0

        while i<j:
            area=(j-i)* min(height[i],height[j])
            #print(area)
            if area>ma:
                ma=area
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return(ma)
            