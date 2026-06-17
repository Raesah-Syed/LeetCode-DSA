# Last updated: 6/16/2026, 10:30:56 PM
1class Solution:
2    def findKthPositive(self, arr: List[int], k: int) -> int:
3        left, right = 0, len(arr) - 1
4        
5        while left <= right:
6            mid = (left + right) // 2
7            # Calculate how many positive integers are missing before arr[mid]
8            missing = arr[mid] - (mid + 1)
9            
10            if missing < k:
11                left = mid + 1
12            else:
13                right = mid - 1
14                
15        # After the loop, 'right' is the largest index where missing < k.
16        # The kth missing number will be: arr[right] + (k - missing_at_right)
17        # Which simplifies beautifully to: left + k
18        return left + k