# Last updated: 5/31/2026, 11:35:43 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                d[nums[i]]-=i
                if abs(d[nums[i]])<=k:
                    return True
                else:
                    d[nums[i]]=i
        return False 