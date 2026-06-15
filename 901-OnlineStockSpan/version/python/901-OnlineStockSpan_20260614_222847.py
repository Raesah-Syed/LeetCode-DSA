# Last updated: 6/14/2026, 10:28:47 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        file=path.split('/')
4        s=[]
5
6        for f in file:
7            if f=='' or f=='.':
8                continue
9            elif f=='..':
10                if s:
11                    s.pop()
12            else:
13                s.append(f)
14        
15        return("/"+"/".join(s))
16
17