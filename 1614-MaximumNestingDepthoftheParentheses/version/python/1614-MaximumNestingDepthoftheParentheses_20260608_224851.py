# Last updated: 6/8/2026, 10:48:51 PM
# Use top element of stack like a log and carry forward the operations
1class Solution:
2    def minLength(self, s: str) -> int:
3        x=list(s[0])
4        for i in range(1,len(s)):
5           
6            if len(x)>0 and s[i]=='B' and x[-1]=='A':
7                x.pop()
8            elif len(x)>0 and s[i]=='D' and x[-1]=='C':
9                x.pop()
10            else:
11                x.append(s[i])
12            
13        return len(x)
14        