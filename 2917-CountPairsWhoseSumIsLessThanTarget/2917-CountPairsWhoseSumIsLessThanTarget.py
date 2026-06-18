# Last updated: 6/17/2026, 11:12:34 PM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # 1. Sort the array first (Do this only once!)
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        # 2. Use two pointers to find valid pairs
        while left < right:
            if nums[left] + nums[right] < target:
                # If the current pair is valid, then all pairs between 
                # left and right using this 'left' element are also valid.
                count += (right - left)
                left += 1  # Move left pointer to try a larger element
            else:
                right -= 1 # Move right pointer to make the sum smaller
                
        return count