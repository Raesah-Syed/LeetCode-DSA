# Last updated: 6/20/2026, 11:49:59 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        def binary_search(left: int, right: int) -> int:
            # Base case: when left meets right, we've pinned down the missing index
            if left >= right:
                return left
            
            mid = (left + right) // 2
            
            if nums[mid] > mid:
                # Pass left and mid to search the left half
                return binary_search(left, mid)
            else:
                # Pass mid + 1 and right to search the right half
                return binary_search(mid + 1, right)
        
        # Initial call spans from index 0 to len(nums)
        return binary_search(0, len(nums))