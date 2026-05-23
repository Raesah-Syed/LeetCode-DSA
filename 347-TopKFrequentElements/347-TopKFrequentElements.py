# Last updated: 5/23/2026, 5:53:19 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        kel= sorted(d, key=d.get, reverse=True)
        return (kel[:k])