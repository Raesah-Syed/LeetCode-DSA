# Last updated: 6/16/2026, 10:37:00 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Calculate how many positive integers are missing before arr[mid]
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
                
        # After the loop, 'right' is the largest index where missing < k.
        # The kth missing number will be: arr[right] + (k - missing_at_right)
        # Which simplifies beautifully to: left + k
        return left + k