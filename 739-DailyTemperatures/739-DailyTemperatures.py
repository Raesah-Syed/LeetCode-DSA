# Last updated: 6/12/2026, 6:14:19 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r=[0]*len(temperatures)
        s=[]
                
        for i in range(len(temperatures)):

            while s and temperatures[i]>temperatures[s[-1]]:
                pi=s.pop()
                r[pi]=i-pi
            s.append(i)
        return(r)

