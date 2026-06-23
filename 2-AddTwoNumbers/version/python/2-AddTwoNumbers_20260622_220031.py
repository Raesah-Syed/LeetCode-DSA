# Last updated: 6/22/2026, 10:00:31 PM
# Floyd's Tortoise and Hare (Cycle Detection)
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        
4        slow=nums[0]
5        fast=nums[0]
6
7        while True:
8            slow=nums[slow]
9            fast=nums[nums[fast]]
10            if slow==fast:
11                break
12
13        slow=nums[0]
14        while slow!=fast:
15            slow=nums[slow]
16            fast=nums[fast]
17        
18        return slow