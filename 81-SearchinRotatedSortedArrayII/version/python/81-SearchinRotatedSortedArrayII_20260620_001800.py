# Last updated: 6/20/2026, 12:18:00 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        
4        left,right=0,len(nums)-1
5
6        while left<=right:
7
8            mid=(left+right)//2
9
10            if nums[mid]==target:
11                return True
12            
13            if nums[mid]==nums[left]==nums[right]:
14                left+=1
15                right-=1
16            
17            elif nums[mid]<=nums[right]:
18                if nums[mid]<target<=nums[right]:
19                    left=mid+1
20                else:
21                    right=mid-1
22            
23            else:
24                if nums[left]<=target<nums[mid]:
25                    right=mid-1
26                else:
27                    left=mid+1
28        return False