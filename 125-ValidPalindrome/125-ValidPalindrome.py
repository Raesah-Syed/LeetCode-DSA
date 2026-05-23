# Last updated: 5/23/2026, 5:53:29 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        l = len(s) - 1
        s = s.lower()

        while i < l:
            # Safely skip non-alphanumeric from the left
            while i < l and not s[i].isalnum():
                i += 1
                
            # Safely skip non-alphanumeric from the right
            while i < l and not s[l].isalnum():
                l -= 1
                
            # Perform the actual character comparison
            if s[i] != s[l]:
                return False
                
            i += 1
            l -= 1

        return True