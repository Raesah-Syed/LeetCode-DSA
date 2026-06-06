# Last updated: 6/6/2026, 11:24:27 AM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left = 0
4        current_sum = 0
5        min_len = float('inf')
6        
7        # 'right' pointer expands the window
8        for right in range(len(nums)):
9            current_sum += nums[right]
10            
11            # 'left' pointer contracts the window as long as it's valid
12            # This is the "sliding" part that makes it O(N)
13            while current_sum >= target:
14                min_len = min(min_len, right - left + 1)
15                current_sum -= nums[left]
16                left += 1
17                
18        return 0 if min_len == float('inf') else min_len