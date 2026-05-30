# Last updated: 5/29/2026, 10:19:07 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        # The window of k elements can start from index 0 up to len(arr) - k
4        left, right = 0, len(arr) - k
5        
6        while left < right:
7            mid = (left + right) // 2
8            
9            # Compare the distance of the start element vs the end element of the window
10            # If x - arr[mid] > arr[mid + k] - x, the element at mid+k is closer,
11            # so the window must start further to the right.
12            if x - arr[mid] > arr[mid + k] - x:
13                left = mid + 1
14            else:
15                # Otherwise, the current 'mid' is a potential starting point
16                right = mid
17        
18        # 'left' is the starting index of our k-sized window
19        return arr[left : left + k]
20