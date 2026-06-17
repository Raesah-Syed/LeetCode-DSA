# Last updated: 6/17/2026, 3:19:04 PM
1class Solution:
2    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
3        d={}
4        for mi in range(len(mat)):
5            d[mi]=mat[mi].count(1)
6        
7        sd = dict(sorted(d.items(), key=lambda item: item[1]))
8        return(list(sd.keys())[:k])