# Last updated: 6/18/2026, 11:45:14 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        left,right=0,len(nums)-1
5
6        while left<=right:
7
8            mid=(left+right)//2
9
10            if nums[mid]==target:
11                return mid
12
13            if nums[mid]>=nums[right]:
14
15                if target>=nums[left] and target<nums[mid]:
16                    right=mid-1
17                else:
18                    left=mid+1
19
20            else:
21
22                if target>nums[mid] and target<=nums[right]:
23                    left=mid+1
24                else:
25                    right=mid-1
26        
27        return -1