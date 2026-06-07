# Last updated: 6/6/2026, 6:56:28 PM
1class Solution:
2    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
3        # 1. Total customers satisfied regardless of your secret power
4        # (This is your "g=0" loop)
5        satisfied_already = sum(c for c, g in zip(customers, grumpy) if g == 0)
6        
7        # 2. Initial window sum of only the grumpy customers (g=1)
8        current_bonus = sum(c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1)
9        max_bonus = current_bonus
10        
11        # 3. Slide the window, updating ONLY based on grumpy members
12        for i in range(minutes, len(customers)):
13            # Add the new person into the bonus window if they are grumpy
14            if grumpy[i] == 1:
15                current_bonus += customers[i]
16            
17            # Remove the person leaving the window if they were grumpy
18            if grumpy[i - minutes] == 1:
19                current_bonus -= customers[i - minutes]
20                
21            max_bonus = max(max_bonus, current_bonus)
22            
23        return satisfied_already + max_bonus