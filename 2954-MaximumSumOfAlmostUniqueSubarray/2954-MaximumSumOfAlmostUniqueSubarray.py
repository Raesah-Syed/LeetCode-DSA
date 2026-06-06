# Last updated: 6/6/2026, 5:35:16 PM
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        c=Counter(nums[:k])
        s=sum(nums[:k])
        
        if len(c)>=m:
            ma=s
        else:
            ma=0
        if len(nums)==k and len(c)>=m:
            return(sum(nums))
        
        for n in range(k,len(nums)):
            s+=nums[n]
            s-=nums[n-k]
            
            c[nums[n]]+=1
            c[nums[n-k]]-=1
            
            if c[nums[n-k]]==0:
                del c[nums[n-k]]
            if len(c)>=m:
                ma=max(ma,s)
        return(ma)
            
        

 
        