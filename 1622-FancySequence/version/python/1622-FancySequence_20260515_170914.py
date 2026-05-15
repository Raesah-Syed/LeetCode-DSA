# Last updated: 5/15/2026, 5:09:14 PM
1
2class Solution:
3    def maximumAmount(self, coins: List[List[int]]) -> int:
4        m, n = len(coins), len(coins[0])
5
6    # dp[i][j][k] = max coins at (i,j) using k neutralizations
7        dp = [[[-float('inf')]*3 for _ in range(n)] for _ in range(m)]
8
9        # Base case: top-left cell, 0 neutralizations used
10        dp[0][0][0] = coins[0][0]
11
12        # If (0,0) is negative, we can neutralize it (use 1 neutralization)
13        if coins[0][0] < 0:
14            dp[0][0][1] = 0
15
16        for i in range(m):
17            for j in range(n):
18                if i == 0 and j == 0: continue
19                for k in range(3):       # k = neutralizations used so far
20                    best = -float('inf')
21
22                    # Can we come from the top?
23                    if i > 0 and dp[i-1][j][k] != -float('inf'):
24                        best = max(best, dp[i-1][j][k])
25
26                    # Can we come from the left?
27                    if j > 0 and dp[i][j-1][k] != -float('inf'):
28                        best = max(best, dp[i][j-1][k])
29
30                    if best == -float('inf'): continue
31
32                    val = coins[i][j]
33                    # Option 1: take the cell value (positive or negative)
34                    dp[i][j][k] = max(dp[i][j][k], best + val)
35
36                    # Option 2: neutralize (only if negative AND k < 2)
37                    if val < 0 and k < 2:
38                        dp[i][j][k+1] = max(dp[i][j][k+1], best)
39
40        # Answer: best result at bottom-right, any k used
41        return max(dp[m-1][n-1])