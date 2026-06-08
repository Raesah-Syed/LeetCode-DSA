# Last updated: 6/7/2026, 7:17:15 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        c,m=0,0
        
        for a in s:
            if a=='(':
                c+=1
            elif a==')':
                c-=1
            else:
                continue
            m=max(m,c)
        return(m)