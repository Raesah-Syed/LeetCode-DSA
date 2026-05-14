# Last updated: 5/13/2026, 10:36:04 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        
4        result = 0
5        for i in range(32):
6        # Shift result left and OR it with the rightmost bit of n
7            result = (result << 1) | (n & 1)
8        # Shift n right to move to the next bit
9            n >>= 1
10        return result
11