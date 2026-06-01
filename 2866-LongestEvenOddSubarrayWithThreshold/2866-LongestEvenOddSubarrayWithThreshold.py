# Last updated: 5/31/2026, 11:34:20 PM
class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        max_len = 0
        current_len = 0
        
        for i in range(len(nums)):
            # Condition 1: Check if we are starting or continuing a sequence
            if current_len == 0:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    current_len = 1
            else:
                # Condition 2: Check for alternating parity and threshold limit
                if nums[i] <= threshold and (nums[i] % 2 != nums[i-1] % 2):
                    current_len += 1
                # Condition 3: If broken, check if current element can start a new sequence
                elif nums[i] % 2 == 0 and nums[i] <= threshold:
                    current_len = 1
                else:
                    current_len = 0
            
            max_len = max(max_len, current_len)
            
        return max_len