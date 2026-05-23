# Last updated: 5/23/2026, 5:53:28 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If our current candidate was knocked out, pick a new one
            if count == 0:
                candidate = num
                
            # If the number matches the candidate, they gain momentum. 
            # If it's an opponent, they lose momentum.
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate