# Last updated: 5/21/2026, 1:53:48 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        # Strategy: Keep finding the max element and swapping it to the back boundary
4        high = len(nums) - 1
5        
6        while high > 0:
7            max_idx = 0
8            # Find the index of the largest element in the remaining unsorted portion
9            for i in range(1, high + 1):
10                if nums[i] > nums[max_idx]:
11                    max_idx = i
12            
13            # SWAP the max element to the back boundary (don't overwrite!)
14            nums[max_idx], nums[high] = nums[high], nums[max_idx]
15            
16            # Move the boundary inward
17            high -= 1