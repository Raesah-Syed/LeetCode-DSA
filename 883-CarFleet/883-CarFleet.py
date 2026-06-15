# Last updated: 6/14/2026, 11:41:55 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=[]

        cars=sorted(zip(position,speed), reverse=True)
        
        for pos,spd in cars:
            x=(target-pos)/spd

            if not s or x>s[-1]:
                s.append(x)
        
        return len(s)