# Last updated: 6/14/2026, 11:42:08 PM
class Solution:
    def decodeString(self, s: str) -> str:
        x = []
        d = 0  # Still tracking bracket depth if you want, but cur_num is key
        r = ''
        cur_num = 0  # Track the multiplier cleanly
        
        for i in s:
            if i.isdigit():
                # Correctly builds multi-digit numbers (like 10 or 300)
                cur_num = cur_num * 10 + int(i)
                
            elif i == '[':
                d += 1
                # FIXED: Push the string built so far and its multiplier together
                x.append((r, cur_num))
                r = ''       # Reset for the new string inside brackets
                cur_num = 0  # Reset for the next number
                
            elif i.isalpha():
                # Accumulate ordinary characters
                r += i
                
            elif i == ']':
                d -= 1
                # FIXED: Pop the outer context safely
                prev_str, num = x.pop()
                # Multiply current string and append it right onto the previous context
                r = prev_str + (r * num)
                
        return r