# Last updated: 6/6/2026, 5:35:01 PM
1class Solution:
2    def maxSum(self, nums: List[int], m: int, k: int) -> int:
3        
4        c=Counter(nums[:k])
5        s=sum(nums[:k])
6        
7        if len(c)>=m:
8            ma=s
9        else:
10            ma=0
11        if len(nums)==k and len(c)>=m:
12            return(sum(nums))
13        
14        for n in range(k,len(nums)):
15            s+=nums[n]
16            s-=nums[n-k]
17            
18            c[nums[n]]+=1
19            c[nums[n-k]]-=1
20            
21            if c[nums[n-k]]==0:
22                del c[nums[n-k]]
23            if len(c)>=m:
24                ma=max(ma,s)
25        return(ma)
26            
27        
28
29 
30        