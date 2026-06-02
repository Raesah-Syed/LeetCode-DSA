# Last updated: 6/2/2026, 5:09:03 PM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        left = 0
4        max_len = 0
5        counts = {}
6        
7        for right in range(len(s)):
8            if s[right] not in counts:
9                counts[s[right]]=1
10            else:      
11                counts[s[right]] += 1
12            
13            # If frequency exceeds 2, shrink the window from the left
14            while counts[s[right]] > 2:
15                char_left = s[left]
16                counts[char_left] -= 1
17                left += 1
18            
19            # The current window [left, right] is valid
20            max_len = max(max_len, right - left + 1)
21            
22        return max_len