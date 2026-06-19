# Last updated: 6/18/2026, 11:29:10 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        
4        left,right=0,len(nums)-1
5
6        while left<right:
7
8            mid=(left+right)//2
9
10            if nums[mid]>nums[right]:
11                left=mid+1
12            else:
13                right=mid
14
15        return nums[right]
16