# Last updated: 5/12/2026, 5:48:03 PM
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        # Helper to count 1s in binary (the "Hamming Weight")
        def count_bits(n):
            count = 0
            while n > 0:
                count += n % 2
                n //= 2
            return count

        # Sort using a tuple: (bit_count, original_number)
        # 1. Primary sort: bit_count
        # 2. Secondary sort (tie-breaker): the number itself
        arr.sort(key=lambda x: (count_bits(x), x))
        
        return arr