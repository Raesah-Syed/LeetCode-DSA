# Last updated: 6/12/2026, 6:14:20 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        p=[]
        for a in asteroids:
            if a>0:
                p.append(a)
            elif a<0:
                
                
                while p and p[-1]>0 and abs(a)>abs(p[-1]):
                    p.pop()
                if len(p)==0 or p[-1]<0:
                    p.append(a)
                
                elif abs(a)==abs(p[-1]):
                    p.pop()
                
        return(p)
                