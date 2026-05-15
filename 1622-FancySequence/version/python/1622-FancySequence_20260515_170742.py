# Last updated: 5/15/2026, 5:07:42 PM
# USE DP
1from functools import cache
2
3class Solution:
4    def maximumAmount(self, coins: List[List[int]]) -> int:
5        m, n = len(coins), len(coins[0])
6
7    # dp[i][j][k] = max coins at (i,j) using k neutralizations
8        dp = [[[-float('inf')]*3 for _ in range(n)] for _ in range(m)]
9
10        # Base case: top-left cell, 0 neutralizations used
11        dp[0][0][0] = coins[0][0]
12
13        # If (0,0) is negative, we can neutralize it (use 1 neutralization)
14        if coins[0][0] < 0:
15            dp[0][0][1] = 0
16
17        for i in range(m):
18            for j in range(n):
19                if i == 0 and j == 0: continue
20                for k in range(3):       # k = neutralizations used so far
21                    best = -float('inf')
22
23                    # Can we come from the top?
24                    if i > 0 and dp[i-1][j][k] != -float('inf'):
25                        best = max(best, dp[i-1][j][k])
26
27                    # Can we come from the left?
28                    if j > 0 and dp[i][j-1][k] != -float('inf'):
29                        best = max(best, dp[i][j-1][k])
30
31                    if best == -float('inf'): continue
32
33                    val = coins[i][j]
34                    # Option 1: take the cell value (positive or negative)
35                    dp[i][j][k] = max(dp[i][j][k], best + val)
36
37                    # Option 2: neutralize (only if negative AND k < 2)
38                    if val < 0 and k < 2:
39                        dp[i][j][k+1] = max(dp[i][j][k+1], best)
40
41        # Answer: best result at bottom-right, any k used
42        return max(dp[m-1][n-1])