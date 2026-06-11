# Last updated: 6/10/2026, 11:42:45 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:

        x=[]

        for i in s:
            if x and x[-1]==i:
                x.pop()
            else:
                x.append(i)
        
        return "".join(x)

        

        