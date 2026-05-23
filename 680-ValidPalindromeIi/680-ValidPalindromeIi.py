# Last updated: 5/23/2026, 5:53:12 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a specific substring is a pure palindrome
        def is_pure_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i = 0
        l = len(s) - 1

        while i < l:
            if s[i] != s[l]:
                # Mismatch found! We have exactly ONE deletion allowance.
                # Path 1: Skip the left character -> check remaining range (i + 1 to l)
                # Path 2: Skip the right character -> check remaining range (i to l - 1)
                return is_pure_palindrome(i + 1, l) or is_pure_palindrome(i, l - 1)
            
            i += 1
            l -= 1

        return True