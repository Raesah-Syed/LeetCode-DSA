# Last updated: 5/13/2026, 11:43:07 PM
class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        d = 0
        started = False  # This tracks if we've found our first '1'

        while n > 0:
            bit = n & 1
            
            if bit == 1:
                if started:
                    # We found a '1' and we were already counting
                    d += 1 
                    max_gap = max(max_gap, d)
                    d = 0 # Reset for the next gap
                else:
                    # This is our very first '1'
                    started = True
                    d = 0
            
            elif bit == 0:
                if started:
                    # Only count distance if we've found the first '1'
                    d += 1
            
            n >>= 1 # Move to next bit
            
        return max_gap