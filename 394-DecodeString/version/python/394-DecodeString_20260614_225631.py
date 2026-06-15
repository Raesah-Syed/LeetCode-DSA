# Last updated: 6/14/2026, 10:56:31 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        x = []
4        d = 0  # Still tracking bracket depth if you want, but cur_num is key
5        r = ''
6        cur_num = 0  # Track the multiplier cleanly
7        
8        for i in s:
9            if i.isdigit():
10                # Correctly builds multi-digit numbers (like 10 or 300)
11                cur_num = cur_num * 10 + int(i)
12                
13            elif i == '[':
14                d += 1
15                # FIXED: Push the string built so far and its multiplier together
16                x.append((r, cur_num))
17                r = ''       # Reset for the new string inside brackets
18                cur_num = 0  # Reset for the next number
19                
20            elif i.isalpha():
21                # Accumulate ordinary characters
22                r += i
23                
24            elif i == ']':
25                d -= 1
26                # FIXED: Pop the outer context safely
27                prev_str, num = x.pop()
28                # Multiply current string and append it right onto the previous context
29                r = prev_str + (r * num)
30                
31        return r