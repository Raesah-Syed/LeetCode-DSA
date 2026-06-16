# Last updated: 6/15/2026, 6:30:45 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        left,right=0,len(nums)
5
6        while (left<right):
7
8            mid=(left+right)//2
9
10            if nums[mid]==target:
11                return mid
12            elif nums[mid]<target:
13                left=mid+1
14            elif nums[mid]>target:
15                right=mid
16
17        return -1