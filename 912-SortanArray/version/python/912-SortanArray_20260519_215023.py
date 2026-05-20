# Last updated: 5/19/2026, 9:50:23 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        if len(nums) <= 1:
4            return nums
5        
6        # 1. SPLIT: Break the list down the middle
7        mid = len(nums) // 2
8        left = self.sortArray(nums[:mid])
9        right = self.sortArray(nums[mid:])
10        
11        # 2. COMBINE: Zip the sorted halves together
12        res, l, r = [], 0, 0
13        while l < len(left) and r < len(right):
14            if left[l] < right[r]:
15                res.append(left[l]); l += 1
16            else:
17                res.append(right[r]); r += 1
18                
19        # Append whatever numbers are left over
20        return res + left[l:] + right[r:]