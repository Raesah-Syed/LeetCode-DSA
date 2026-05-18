# Last updated: 5/17/2026, 10:19:49 PM
# Use set to get rid of dups and compare lengths
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        s=set(nums)
4        if len(s)<len(nums):
5            return True
6        else: 
7            return False
8            