# Last updated: 6/16/2026, 10:48:00 PM
# Make sure to do an initial check at the beginning to reduce time complexity. Optimized the code with the check by 90%
1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        if nums1[len(nums1)-1]<nums2[0]:
4            return -1
5        for n in nums1:
6
7            left,right=0,len(nums2)-1
8
9            while left<=right:
10                mid=(left+right)//2
11
12                if nums2[mid]==n:
13                    return n
14                
15                elif nums2[mid]<n:
16                    left=mid+1
17                
18                else:
19                    right=mid-1
20        return -1
21
22