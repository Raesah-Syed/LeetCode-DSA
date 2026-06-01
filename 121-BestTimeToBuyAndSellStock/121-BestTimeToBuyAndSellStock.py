# Last updated: 5/31/2026, 11:35:57 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price found so far
            if price < min_price:
                min_price = price
            # Calculate profit if sold today and update max_profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit