# Last updated: 6/18/2026, 10:30:02 PM
1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4        
5        while left <= right:
6            mid = (left + right) // 2
7            
8            if nums[mid] == target:
9                return mid
10            
11            # Check if the left half is sorted
12            if nums[left] <= nums[mid]:
13                # Check if target lies within the sorted left half
14                if nums[left] <= target < nums[mid]:
15                    right = mid - 1
16                else:
17                    left = mid + 1
18            # Otherwise, the right half must be sorted
19            else:
20                # Check if target lies within the sorted right half
21                if nums[mid] < target <= nums[right]:
22                    left = mid + 1
23                else:
24                    right = mid - 1
25                    
26        return -1