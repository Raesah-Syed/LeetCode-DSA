# Last updated: 6/12/2026, 6:19:01 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s=[]

        for t in tokens:
                           
            if t=='+':
                x=int(s.pop())+int(s.pop())
                s.append(x)
            elif t=='-':
                y=int(s.pop())
                x=int(s.pop())
                s.append(x-y)
            elif t=='*':
                x=int(s.pop())*int(s.pop())
                s.append(x)
            elif t=='/':
                y=s.pop()
                x=s.pop()
                r=int(x)/int(y)
                s.append(r)
            else:
                s.append(t)
        
        return(int(s[0]))