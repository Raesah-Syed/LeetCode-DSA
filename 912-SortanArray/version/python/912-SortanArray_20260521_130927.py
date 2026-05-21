# Last updated: 5/21/2026, 1:09:27 PM
# Use function to make it easy
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        # Helper function to check if a specific substring is a pure palindrome
4        def is_pure_palindrome(left: int, right: int) -> bool:
5            while left < right:
6                if s[left] != s[right]:
7                    return False
8                left += 1
9                right -= 1
10            return True
11
12        i = 0
13        l = len(s) - 1
14
15        while i < l:
16            if s[i] != s[l]:
17                # Mismatch found! We have exactly ONE deletion allowance.
18                # Path 1: Skip the left character -> check remaining range (i + 1 to l)
19                # Path 2: Skip the right character -> check remaining range (i to l - 1)
20                return is_pure_palindrome(i + 1, l) or is_pure_palindrome(i, l - 1)
21            
22            i += 1
23            l -= 1
24
25        return True