# Last updated: 5/20/2026, 11:12:40 PM
# check for special characters
1import string
2
3class Solution:
4    def isPalindrome(self, s: str) -> bool:
5        i = 0
6        l = len(s) - 1
7        s = s.lower()  # do this once, outside the loop
8
9        while i < l:
10            if not s[i].isalnum():  # skip non-alphanumeric (covers spaces too)
11                i += 1
12                continue
13            if not s[l].isalnum():
14                l -= 1
15                continue
16            if s[i] != s[l]:
17                return False
18            i += 1
19            l -= 1
20
21        return True