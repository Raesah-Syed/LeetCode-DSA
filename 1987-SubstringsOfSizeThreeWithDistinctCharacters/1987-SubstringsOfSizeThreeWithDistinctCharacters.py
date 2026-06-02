# Last updated: 6/1/2026, 10:50:58 PM
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        # Iterate only up to the point where a 3-character window can exist
        for i in range(len(s) - 2):
            # Take the window of size 3
            x = s[i:i+3]
            
            # Check if all 3 characters are unique
            if len(set(x)) == 3:
                count += 1
                
        return count