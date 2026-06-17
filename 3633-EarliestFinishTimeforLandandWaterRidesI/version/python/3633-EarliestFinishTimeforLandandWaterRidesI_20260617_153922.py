# Last updated: 6/17/2026, 3:39:22 PM
1class Solution:
2    def countPairs(self, nums: List[int], target: int) -> int:
3        # 1. Sort the array first (Do this only once!)
4        nums.sort()
5        
6        left = 0
7        right = len(nums) - 1
8        count = 0
9        
10        # 2. Use two pointers to find valid pairs
11        while left < right:
12            if nums[left] + nums[right] < target:
13                # If the current pair is valid, then all pairs between 
14                # left and right using this 'left' element are also valid.
15                count += (right - left)
16                left += 1  # Move left pointer to try a larger element
17            else:
18                right -= 1 # Move right pointer to make the sum smaller
19                
20        return count