# Last updated: 5/31/2026, 11:35:28 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        #p=0
        m=s
        #m=float(s/k)
        i=0

        while (i+k<len(nums)):            
            s+=nums[i+k]-nums[i]
            #p=float(s/k)
            m=max(m,s)
            i=i+1
        return m/k
            