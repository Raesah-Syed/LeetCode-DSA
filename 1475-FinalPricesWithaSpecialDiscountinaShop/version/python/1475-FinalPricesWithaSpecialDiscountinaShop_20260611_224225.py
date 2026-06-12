# Last updated: 6/11/2026, 10:42:25 PM
# consider all cases to be covered in code
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        p=[]
4        for a in asteroids:
5            if a>0:
6                p.append(a)
7            elif a<0:
8                
9                
10                while p and p[-1]>0 and abs(a)>abs(p[-1]):
11                    p.pop()
12                if len(p)==0 or p[-1]<0:
13                    p.append(a)
14                
15                elif abs(a)==abs(p[-1]):
16                    p.pop()
17                
18        return(p)
19                