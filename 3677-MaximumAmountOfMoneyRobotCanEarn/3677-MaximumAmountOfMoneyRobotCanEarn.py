# Last updated: 5/15/2026, 5:07:57 PM
from functools import cache

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

    # dp[i][j][k] = max coins at (i,j) using k neutralizations
        dp = [[[-float('inf')]*3 for _ in range(n)] for _ in range(m)]

        # Base case: top-left cell, 0 neutralizations used
        dp[0][0][0] = coins[0][0]

        # If (0,0) is negative, we can neutralize it (use 1 neutralization)
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                for k in range(3):       # k = neutralizations used so far
                    best = -float('inf')

                    # Can we come from the top?
                    if i > 0 and dp[i-1][j][k] != -float('inf'):
                        best = max(best, dp[i-1][j][k])

                    # Can we come from the left?
                    if j > 0 and dp[i][j-1][k] != -float('inf'):
                        best = max(best, dp[i][j-1][k])

                    if best == -float('inf'): continue

                    val = coins[i][j]
                    # Option 1: take the cell value (positive or negative)
                    dp[i][j][k] = max(dp[i][j][k], best + val)

                    # Option 2: neutralize (only if negative AND k < 2)
                    if val < 0 and k < 2:
                        dp[i][j][k+1] = max(dp[i][j][k+1], best)

        # Answer: best result at bottom-right, any k used
        return max(dp[m-1][n-1])