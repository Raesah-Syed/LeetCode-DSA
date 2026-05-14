# Last updated: 5/13/2026, 11:46:42 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        
6        # Start at bottom-left corner
7        r = rows - 1
8        c = 0
9        count = 0
10        
11        while r >= 0 and c < cols:
12            if grid[r][c] < 0:
13                # If this is negative, everything to its right is negative!
14                count += (cols - c)
15                # Move up to the next row
16                r -= 1
17            else:
18                # If this is positive, move right to find a negative
19                c += 1
20                
21        return count