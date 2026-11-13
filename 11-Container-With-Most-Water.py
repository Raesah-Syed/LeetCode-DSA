class Solution:
    def maxArea(self, height: list[int]) -> int:
        m=-1
        x=len(height)-1
        i=0
            
        while i<=x:
            area=min(height[i],height[x])*(x-i)
            m=max(m,area)
            if height[i]<height[x]:
                i=i+1
            else:
                x=x-1
        
        return (m)
