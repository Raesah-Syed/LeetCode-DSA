# Last updated: 5/28/2026, 9:23:33 PM
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min=inf
        for t in tasks:
            if t[0]+t[1]<min:
                min=t[0]+t[1]
        
        return (min)