# Last updated: 6/20/2026, 11:49:57 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        n1=set(nums1)
        n2=set(nums2)
        for n in n1:
            d[n]=d.get(n,0)+1
     
        for n in n2:
            d[n]=d.get(n,0)-1

        r= [k for k,v in d.items() if v==0]
        return(r)
