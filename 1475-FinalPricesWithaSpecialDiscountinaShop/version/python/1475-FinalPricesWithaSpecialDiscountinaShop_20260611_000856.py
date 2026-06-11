# Last updated: 6/11/2026, 12:08:56 AM
# isdigit() does not account for -ve numbers
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3
4        s=[]
5
6        for t in tokens:
7                           
8            if t=='+':
9                x=int(s.pop())+int(s.pop())
10                s.append(x)
11            elif t=='-':
12                y=int(s.pop())
13                x=int(s.pop())
14                s.append(x-y)
15            elif t=='*':
16                x=int(s.pop())*int(s.pop())
17                s.append(x)
18            elif t=='/':
19                y=s.pop()
20                x=s.pop()
21                r=int(x)/int(y)
22                s.append(r)
23            else:
24                s.append(t)
25        
26        return(int(s[0]))