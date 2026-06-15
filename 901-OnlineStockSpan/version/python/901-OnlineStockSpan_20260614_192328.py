# Last updated: 6/14/2026, 7:23:28 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        s=[]
4
5        cars=sorted(zip(position,speed), reverse=True)
6        
7        for pos,spd in cars:
8            x=(target-pos)/spd
9
10            if not s or x>s[-1]:
11                s.append(x)
12        
13        return len(s)