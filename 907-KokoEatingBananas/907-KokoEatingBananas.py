# Last updated: 6/18/2026, 11:30:05 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
   
        def getk(k: int)-> int:
            c=0
            for p in piles:
                
                if p<=k:
                    c+=1
                else:
                    c+=(p+k-1)//k
            #print (c)
            return c

        left,right=1,max(piles)
        ans=right
        while left<=right:
            
            mid=(left+right)//2

            if getk(mid)<=h:
                ans=mid
                right=mid-1
            
            else:
                left=mid+1
        
        return ans
            
        
