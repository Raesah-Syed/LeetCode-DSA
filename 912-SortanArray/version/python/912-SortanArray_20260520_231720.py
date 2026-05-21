# Last updated: 5/20/2026, 11:17:20 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        i = 0
4        l = len(s) - 1
5        s = s.lower()
6
7        while i < l:
8            # Safely skip non-alphanumeric from the left
9            while i < l and not s[i].isalnum():
10                i += 1
11                
12            # Safely skip non-alphanumeric from the right
13            while i < l and not s[l].isalnum():
14                l -= 1
15                
16            # Perform the actual character comparison
17            if s[i] != s[l]:
18                return False
19                
20            i += 1
21            l -= 1
22
23        return True