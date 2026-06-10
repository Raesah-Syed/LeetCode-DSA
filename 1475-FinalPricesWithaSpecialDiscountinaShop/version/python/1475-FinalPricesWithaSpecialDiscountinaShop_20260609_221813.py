# Last updated: 6/9/2026, 10:18:13 PM
# Handle cases where there are no directories at all
1class Solution:
2    def minOperations(self, logs: List[str]) -> int:
3        s=[]
4
5        for l in logs:
6
7            if s and l=='../':
8                s.pop()
9            elif l=='./':
10                continue
11            else:
12                if l!='../':
13                    s.append(l)
14        
15        
16        return len(s)