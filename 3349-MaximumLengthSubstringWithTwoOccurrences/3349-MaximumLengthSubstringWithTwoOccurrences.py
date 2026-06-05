# Last updated: 6/4/2026, 10:07:13 PM
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        counts = {}
        
        for right in range(len(s)):
            if s[right] not in counts:
                counts[s[right]]=1
            else:      
                counts[s[right]] += 1
            
            # If frequency exceeds 2, shrink the window from the left
            while counts[s[right]] > 2:
                char_left = s[left]
                counts[char_left] -= 1
                left += 1
            
            # The current window [left, right] is valid
            max_len = max(max_len, right - left + 1)
            
        return max_len