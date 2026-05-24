# Last updated: 5/23/2026, 7:57:14 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0  # The left side of our window
        max_length = 0
        
        # 'right' acts as your loop variable moving through the string
        for right in range(len(s)):
            # If the character already exists, shrink the window from the left
            while s[right] in sub:
                sub.remove(s[left])
                left += 1  # Move the left pointer forward
            
            # Now that duplicates are gone, safely add the character
            sub.add(s[right])
            
            # The size of a window from 'left' to 'right' is always: right - left + 1
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length