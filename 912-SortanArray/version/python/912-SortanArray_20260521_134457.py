# Last updated: 5/21/2026, 1:44:57 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        d={}
4        l=[]
5        for n in nums:
6            if n not in d:
7                d[n]=1
8            else:
9                d[n]+=1
10        kel= sorted(d, key=d.get, reverse=True)
11        return (kel[:k])