# Last updated: 5/31/2026, 11:34:17 PM
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        dir=k//(n-1)
        pos=k%(n-1)

        if dir%2==0:
                return (pos)
  
        elif dir%2!=0:
                return(n-1-pos)
       
