# Last updated: 5/31/2026, 11:36:06 PM
class Solution:
    
    def isValid(self, s: str) -> bool:
        s1=[]
        for i in s:
            
            if len(s1)==0:
                s1.append(i)
            
            else:
                if (s1[-1]=='(' and i==')') or (s1[-1]=='[' and i==']') or (s1[-1]=='{' and i=='}'):
                    s1.pop()
                else:
                    s1.append(i)
        if len(s1)==0:
            return True
        return False
