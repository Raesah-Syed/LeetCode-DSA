# Last updated: 5/18/2026, 8:45:02 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        candidate = None
4        count = 0
5        
6        for num in nums:
7            # If our current candidate was knocked out, pick a new one
8            if count == 0:
9                candidate = num
10                
11            # If the number matches the candidate, they gain momentum. 
12            # If it's an opponent, they lose momentum.
13            if num == candidate:
14                count += 1
15            else:
16                count -= 1
17                
18        return candidate