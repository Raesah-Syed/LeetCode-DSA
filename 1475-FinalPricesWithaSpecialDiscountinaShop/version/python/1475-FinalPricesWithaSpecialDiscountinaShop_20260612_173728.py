# Last updated: 6/12/2026, 5:37:28 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        r=[0]*len(temperatures)
4        s=[]
5                
6        for i in range(len(temperatures)):
7
8            while s and temperatures[i]>temperatures[s[-1]]:
9                pi=s.pop()
10                r[pi]=i-pi
11            s.append(i)
12        return(r)
13
14