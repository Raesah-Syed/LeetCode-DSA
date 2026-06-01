# Last updated: 5/31/2026, 11:36:44 PM
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        res=[s[0],s[1]]

        for i in range(2,len(s)):
            if not (s[i]==res[-1]==res[-2]):
                res.append(s[i])
            
        return ("".join(res))