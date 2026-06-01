# Last updated: 5/31/2026, 11:35:26 PM
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # The window of k elements can start from index 0 up to len(arr) - k
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare the distance of the start element vs the end element of the window
            # If x - arr[mid] > arr[mid + k] - x, the element at mid+k is closer,
            # so the window must start further to the right.
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                # Otherwise, the current 'mid' is a potential starting point
                right = mid
        
        # 'left' is the starting index of our k-sized window
        return arr[left : left + k]
