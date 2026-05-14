# Last updated: 5/13/2026, 11:44:13 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        c=0
4        for i in range(len(grid)):
5            for j in grid[i]:
6                if j<0:
7                    c+=1
8        return c
9        