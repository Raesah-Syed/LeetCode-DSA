# Last updated: 6/16/2026, 10:46:31 PM
1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        
4        for n in nums1:
5
6            left,right=0,len(nums2)-1
7
8            while left<=right:
9                mid=(left+right)//2
10
11                if nums2[mid]==n:
12                    return n
13                
14                elif nums2[mid]<n:
15                    left=mid+1
16                
17                else:
18                    right=mid-1
19        return -1
20
21