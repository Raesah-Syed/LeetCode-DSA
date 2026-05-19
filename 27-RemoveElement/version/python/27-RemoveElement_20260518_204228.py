# Last updated: 5/18/2026, 8:42:28 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        d={}
4        for n in nums:
5            if n not in d:
6                d[n]=1
7            else:
8                d[n]+=1
9        
10        return max(d, key=d.get)