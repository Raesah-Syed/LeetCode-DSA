# Last updated: 6/7/2026, 7:11:18 PM
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        c,m=0,0
4        
5        for a in s:
6            if a=='(':
7                c+=1
8            elif a==')':
9                c-=1
10            else:
11                continue
12            m=max(m,c)
13        return(m)