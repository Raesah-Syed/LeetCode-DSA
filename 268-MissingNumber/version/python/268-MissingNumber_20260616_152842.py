# Last updated: 6/16/2026, 3:28:42 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        d={}
4        n1=set(nums1)
5        n2=set(nums2)
6        for n in n1:
7            d[n]=d.get(n,0)+1
8     
9        for n in n2:
10            d[n]=d.get(n,0)-1
11
12        r= [k for k,v in d.items() if v==0]
13        return(r)
14