# Last updated: 5/31/2026, 11:35:47 PM
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        # 1. Update Buy Point: Normalize k
        k %= n 
        
        # 2. Sell and Lock: Reverse segments to achieve rotation
        # Reverse all: [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
        nums.reverse()
        # Reverse first k: [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
        nums[0:k] = reversed(nums[0:k])
        # Reverse rest: [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
        nums[k:] = reversed(nums[k:])