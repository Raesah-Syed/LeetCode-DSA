# Last updated: 6/7/2026, 6:43:21 PM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for n in freq:
            if n+1 in freq:
                res = max(res, freq[n] + freq[n+1])
        return res