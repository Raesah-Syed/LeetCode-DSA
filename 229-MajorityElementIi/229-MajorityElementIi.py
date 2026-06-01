# Last updated: 5/31/2026, 11:35:41 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=len(nums)//3
        res=[]
        
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
    
        for k,v in d.items():
            if v>l:
                res.append(k)
        
        return(res)


       