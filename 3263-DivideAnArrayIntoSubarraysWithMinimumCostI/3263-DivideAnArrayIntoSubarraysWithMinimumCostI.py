# Last updated: 5/12/2026, 5:47:48 PM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        first = nums[0]       
        min1 = inf   
        min2 = inf 

        for n in nums[1:]:
            if n < min1:
                min2 = min1    
                min1 = n       
            elif n < min2:
                min2 = n       
                
        return first + min1 + min2