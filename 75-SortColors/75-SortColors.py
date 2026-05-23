# Last updated: 5/23/2026, 5:53:31 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Send 0 to the front zone
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in the middle zone
                mid += 1
            else: # nums[mid] == 2
                # Send 2 to the back zone
                nums[mid], nums[high] = nums[high], nums[mid]
                # High moves inward, mid stays to evaluate the swapped element
                high -= 1