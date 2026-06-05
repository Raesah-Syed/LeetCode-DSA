# Last updated: 6/4/2026, 10:07:28 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1, n2 = len(s1), len(s2)
4        if n1 > n2: return False
5        
6        # 1. Create target frequency map for s1
7        s1_counts = Counter(s1)
8        # 2. Initialize frequency map for the first window in s2
9        window_counts = Counter(s2[:n1])
10        
11        # 3. Slide the window across s2
12        # We only need to check up to n2 - n1
13        for i in range(n2 - n1):
14            # If frequency maps match, we found a permutation
15            if window_counts == s1_counts:
16                return True
17            
18            # Slide: Remove the character leaving (left side)
19            left_char = s2[i]
20            window_counts[left_char] -= 1
21            if window_counts[left_char] == 0:
22                del window_counts[left_char]
23            
24            # Slide: Add the character entering (right side)
25            right_char = s2[i + n1]
26            window_counts[right_char] += 1
27            
28        # Check the final window after the loop
29        return window_counts == s1_counts