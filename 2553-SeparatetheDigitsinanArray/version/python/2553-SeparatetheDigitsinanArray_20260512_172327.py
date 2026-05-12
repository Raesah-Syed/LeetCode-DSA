# Last updated: 5/12/2026, 5:23:27 PM
# Use a tuple instead of dictionary
1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        
4        # Helper to count 1s in binary (the "Hamming Weight")
5        def count_bits(n):
6            count = 0
7            while n > 0:
8                count += n % 2
9                n //= 2
10            return count
11
12        # Sort using a tuple: (bit_count, original_number)
13        # 1. Primary sort: bit_count
14        # 2. Secondary sort (tie-breaker): the number itself
15        arr.sort(key=lambda x: (count_bits(x), x))
16        
17        return arr