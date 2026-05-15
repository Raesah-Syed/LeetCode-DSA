# Last updated: 5/14/2026, 11:42:49 PM
1class Solution:
2    def maximumAmount(self, coins: List[List[int]]) -> int:
3        m, n = len(coins), len(coins[0])
4        
5        # We use a 3D DP table to track the 'r' (skips) logic
6        # dp[i][j][k] stores the max coins at cell (i, j) with 'k' skips used
7        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
8        
9        # Base Case: Starting point
10        dp[0][0][0] = coins[0][0]
11        if coins[0][0] < 0:
12            dp[0][0][1] = 0 # Skip used for the first cell if it's a robber
13            
14        for i in range(m):
15            for j in range(n):
16                for k in range(3):
17                    if dp[i][j][k] == float('-inf'):
18                        continue
19                    
20                    # Look at adjacent possibilities: Right and Down
21                    for di, dj in [(0, 1), (1, 0)]:
22                        ni, nj = i + di, j + dj
23                        
24                        if ni < m and nj < n:
25                            # Option 1: Treat it like a normal cell (Add the value)
26                            dp[ni][nj][k] = max(dp[ni][nj][k], dp[i][j][k] + coins[ni][nj])
27                            
28                            # Option 2: Use your 'r' logic (If it's a robber and r < 2)
29                            if coins[ni][nj] < 0 and k + 1 < 3:
30                                # We 'neutralize' by not adding the negative value
31                                dp[ni][nj][k+1] = max(dp[ni][nj][k+1], dp[i][j][k])
32                                
33        # The answer is the maximum value at the final cell regardless of skips used
34        return max(dp[m-1][n-1])