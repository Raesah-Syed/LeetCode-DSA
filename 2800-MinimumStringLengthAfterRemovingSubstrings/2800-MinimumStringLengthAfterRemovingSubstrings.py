# Last updated: 6/8/2026, 10:49:07 PM
class Solution:
    def minLength(self, s: str) -> int:
        x=list(s[0])
        for i in range(1,len(s)):
           
            if len(x)>0 and s[i]=='B' and x[-1]=='A':
                x.pop()
            elif len(x)>0 and s[i]=='D' and x[-1]=='C':
                x.pop()
            else:
                x.append(s[i])
            
        return len(x)
        