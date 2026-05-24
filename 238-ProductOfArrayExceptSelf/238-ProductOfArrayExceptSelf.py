# Last updated: 5/23/2026, 7:56:31 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Calculate Prefix Products
        # After this, answer[i] contains product of all elements to the left of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix Products on the fly and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer