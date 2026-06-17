# Last updated: 6/17/2026, 4:02:46 PM
# Iterate through each row like performing binary search on a list and return True if target found else return False if the loop has finished
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        for m in matrix:
4
5            left,right=0,len(m)-1
6
7            while left<=right:
8
9                mid=(left+right)//2
10
11                if m[mid]==target:
12                    return True
13                elif m[mid]<target:
14                    left=mid+1
15                else:
16                    right=mid-1
17        
18        return False