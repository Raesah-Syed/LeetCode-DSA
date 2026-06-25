# Last updated: 6/25/2026, 1:59:25 PM
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        result = ""
4        
5        while columnNumber > 0:
6            columnNumber -= 1
7            # Prepend the character to avoid a reverse step at the end
8            result = chr(columnNumber % 26 + 65) + result
9            columnNumber //= 26
10            
11        return result