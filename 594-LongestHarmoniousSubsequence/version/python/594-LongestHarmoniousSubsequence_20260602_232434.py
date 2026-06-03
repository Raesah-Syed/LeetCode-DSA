# Last updated: 6/2/2026, 11:24:34 PM
1class Solution:
2    def findLHS(self, nums: List[int]) -> int:
3        freq = Counter(nums)
4        res = 0
5        for n in freq:
6            if n+1 in freq:
7                res = max(res, freq[n] + freq[n+1])
8        return res