class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                x=d[nums[i]]
                if abs(x-i)<=k:
                    return True
            d[nums[i]]=i
        return False