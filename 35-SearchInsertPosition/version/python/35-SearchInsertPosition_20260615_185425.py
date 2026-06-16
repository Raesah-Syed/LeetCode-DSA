# Last updated: 6/15/2026, 6:54:25 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        
4        left,right=0,len(nums)
5
6        while (left<right):
7
8            mid=(left+right)//2
9
10            if nums[mid]==target:
11                return mid
12
13            elif nums[mid]<target:
14                left=mid+1
15            
16            elif nums[mid]>target:
17                right=mid
18        
19        return left