# Last updated: 6/15/2026, 11:37:57 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        nums.sort()
4        
5        def binary_search(left: int, right: int) -> int:
6            # Base case: when left meets right, we've pinned down the missing index
7            if left >= right:
8                return left
9            
10            mid = (left + right) // 2
11            
12            if nums[mid] > mid:
13                # Pass left and mid to search the left half
14                return binary_search(left, mid)
15            else:
16                # Pass mid + 1 and right to search the right half
17                return binary_search(mid + 1, right)
18        
19        # Initial call spans from index 0 to len(nums)
20        return binary_search(0, len(nums))