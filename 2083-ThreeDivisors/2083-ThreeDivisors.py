# Last updated: 5/31/2026, 11:34:24 PM
class Solution:
    def isThree(self, n: int) -> bool:
        c=0
        i=1
        while (i<=n):
            if n%i==0:
                c+=1
            i+=1
        if c==3:
            return True
        else:
            return False
