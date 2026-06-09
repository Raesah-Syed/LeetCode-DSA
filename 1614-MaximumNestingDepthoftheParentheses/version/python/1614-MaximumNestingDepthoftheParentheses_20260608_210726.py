# Last updated: 6/8/2026, 9:07:26 PM
# Compare the top of stack and pop if element is in string.
1class Solution:
2    def removeDuplicates(self, s: str) -> str:
3
4        x=[]
5
6        for i in s:
7            if x and x[-1]==i:
8                x.pop()
9            else:
10                x.append(i)
11        
12        return "".join(x)
13
14        
15
16        