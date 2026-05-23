# Last updated: 5/23/2026, 5:53:22 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        if len(s)<len(nums):
            return True
        else: 
            return False
            