# Last updated: 5/15/2026, 11:44:11 PM
# Use sliding window and max function to allocate the character that is duplicated and comes right after the first duplicate
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        sub = set()
4        left = 0  # The left side of our window
5        max_length = 0
6        
7        # 'right' acts as your loop variable moving through the string
8        for right in range(len(s)):
9            # If the character already exists, shrink the window from the left
10            while s[right] in sub:
11                sub.remove(s[left])
12                left += 1  # Move the left pointer forward
13            
14            # Now that duplicates are gone, safely add the character
15            sub.add(s[right])
16            
17            # The size of a window from 'left' to 'right' is always: right - left + 1
18            current_window_size = right - left + 1
19            max_length = max(max_length, current_window_size)
20            
21        return max_length