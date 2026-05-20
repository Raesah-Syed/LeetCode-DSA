# Last updated: 5/19/2026, 10:04:34 PM
# use merge sort
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3       if len(nums)<=1:
4            return nums
5
6       mid=len(nums)//2
7       left=self.sortArray(nums[:mid])
8       right=self.sortArray(nums[mid:])
9    
10       res,l,r=[],0,0
11
12       while l<len(left) and r<len(right):
13           if left[l]<right[r]:
14               res.append(left[l])
15               l+=1
16           else:
17               res.append(right[r])
18               r+=1
19       return res+left[l:]+right[r:]