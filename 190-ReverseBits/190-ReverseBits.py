# Last updated: 5/14/2026, 9:16:09 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for _ in range(32): # Use the bit-length (usually 32 or 64)
    # 1. Peek at the last bit of n
            bit = n & 1
    
    # 2. Push that bit onto the end of res
            res = (res << 1) | bit
    
    # 3. Chop the last bit off n to move to the next one
            n = n >> 1
        return res