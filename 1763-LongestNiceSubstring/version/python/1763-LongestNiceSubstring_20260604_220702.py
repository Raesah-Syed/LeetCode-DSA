# Last updated: 6/4/2026, 10:07:02 PM
1from collections import Counter
2
3class Solution:
4    def checkInclusion(self, s1: str, s2: str) -> bool:
5        n1, n2 = len(s1), len(s2)
6        if n1 > n2: return False
7        
8        # 1. Create target frequency map for s1
9        s1_counts = Counter(s1)
10        # 2. Initialize frequency map for the first window in s2
11        window_counts = Counter(s2[:n1])
12        
13        # 3. Slide the window across s2
14        # We only need to check up to n2 - n1
15        for i in range(n2 - n1):
16            # If frequency maps match, we found a permutation
17            if window_counts == s1_counts:
18                return True
19            
20            # Slide: Remove the character leaving (left side)
21            left_char = s2[i]
22            window_counts[left_char] -= 1
23            if window_counts[left_char] == 0:
24                del window_counts[left_char]
25            
26            # Slide: Add the character entering (right side)
27            right_char = s2[i + n1]
28            window_counts[right_char] += 1
29            
30        # Check the final window after the loop
31        return window_counts == s1_counts