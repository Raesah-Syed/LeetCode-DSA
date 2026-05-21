# Last updated: 5/21/2026, 3:24:01 PM
# This question only has 3 distinct values so write solution around it
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        low = 0
4        mid = 0
5        high = len(nums) - 1
6        
7        while mid <= high:
8            if nums[mid] == 0:
9                # Send 0 to the front zone
10                nums[low], nums[mid] = nums[mid], nums[low]
11                low += 1
12                mid += 1
13            elif nums[mid] == 1:
14                # 1 is already in the middle zone
15                mid += 1
16            else: # nums[mid] == 2
17                # Send 2 to the back zone
18                nums[mid], nums[high] = nums[high], nums[mid]
19                # High moves inward, mid stays to evaluate the swapped element
20                high -= 1