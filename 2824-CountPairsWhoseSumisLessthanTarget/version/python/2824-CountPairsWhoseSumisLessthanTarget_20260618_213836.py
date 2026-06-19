# Last updated: 6/18/2026, 9:38:36 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        # 1. Right boundary must be an indexable element (len - 1)
4        left, right = 0, len(nums) - 1
5        
6        # 2. Use left < right so we stop exactly when left == right
7        while left < right:
8            mid = (left + right) // 2
9            
10            # 3. Compare mid with the right anchor
11            if nums[mid] > nums[right]:
12                # The left half is sorted perfectly, so the inflection point 
13                # (and minimum) MUST be in the right half.
14                left = mid + 1
15            else:
16                # The right half is sorted perfectly, meaning nums[mid] 
17                # could be the minimum, or the minimum is to its left.
18                right = mid
19                
20        # When left == right, they point exactly to the minimum element
21        return nums[left]