# Last updated: 6/18/2026, 11:30:03 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def getd(c: int):
            d=1
            x=0

            for w in weights:
                if x+w <=c:
                    x+=w
                else:
                    d+=1
                    x=w
            print(d)
            return d

        left,right=max(weights),sum(weights)
        ans=right

        while left<=right:

            mid=(left+right)//2

            if getd(mid)<=days:
                ans=mid
                right=mid-1
            
            else:
                left=mid+1
        
        return ans