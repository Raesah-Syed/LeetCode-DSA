# Last updated: 6/18/2026, 10:52:43 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        left, right = 0, len(nums) - 1
4        
5        while left <= right:
6            mid = left + (right - left) // 2
7            
8            if nums[mid] == target:
9                return True
10                
11            # The tricky case: duplicates at boundaries prevent us from knowing which side is sorted
12            if nums[left] == nums[mid] == nums[right]:
13                left += 1
14                right -= 1
15            
16            # Left half is strictly sorted
17            elif nums[left] <= nums[mid]:
18                if nums[left] <= target < nums[mid]:
19                    right = mid - 1
20                else:
21                    left = mid + 1
22                    
23            # Right half is strictly sorted
24            else:
25                if nums[mid] < target <= nums[right]:
26                    left = mid + 1
27                else:
28                    right = mid - 1
29                    
30        return False