# Last updated: 6/7/2026, 4:49:04 PM
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 1. Total customers satisfied regardless of your secret power
        # (This is your "g=0" loop)
        satisfied_already = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
        # 2. Initial window sum of only the grumpy customers (g=1)
        current_bonus = sum(c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1)
        max_bonus = current_bonus
        
        # 3. Slide the window, updating ONLY based on grumpy members
        for i in range(minutes, len(customers)):
            # Add the new person into the bonus window if they are grumpy
            if grumpy[i] == 1:
                current_bonus += customers[i]
            
            # Remove the person leaving the window if they were grumpy
            if grumpy[i - minutes] == 1:
                current_bonus -= customers[i - minutes]
                
            max_bonus = max(max_bonus, current_bonus)
            
        return satisfied_already + max_bonus