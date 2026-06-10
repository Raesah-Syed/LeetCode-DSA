# Last updated: 6/9/2026, 9:58:31 PM
# Check both cases: It could either be that the letter is followed by an upper and lower or lower and upper
1class Solution:
2    def makeGood(self, s: str) -> str:
3        r=[]
4        for i in s:
5            if r and i.isupper() and r[-1]==i.lower() or (r and i.islower() and r[-1]==i.upper()):
6                r.pop()
7                continue
8            else:
9                r.append(i)
10        return "".join(r)
11
12