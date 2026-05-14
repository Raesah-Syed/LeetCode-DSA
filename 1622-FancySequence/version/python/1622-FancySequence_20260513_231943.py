# Last updated: 5/13/2026, 11:19:43 PM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        max_gap = 0
4        d = 0
5        started = False  # This tracks if we've found our first '1'
6
7        while n > 0:
8            bit = n & 1
9            
10            if bit == 1:
11                if started:
12                    # We found a '1' and we were already counting
13                    d += 1 
14                    max_gap = max(max_gap, d)
15                    d = 0 # Reset for the next gap
16                else:
17                    # This is our very first '1'
18                    started = True
19                    d = 0
20            
21            elif bit == 0:
22                if started:
23                    # Only count distance if we've found the first '1'
24                    d += 1
25            
26            n >>= 1 # Move to next bit
27            
28        return max_gap