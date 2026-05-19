# Last updated: 5/18/2026, 6:26:03 PM
# Use dictionary and difference of numbers from target
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        d={}
4        for i in range(len(nums)):
5            if nums[i] not in d:
6                d[target-nums[i]]=i
7            else:
8                return (d[nums[i]],i)
9        