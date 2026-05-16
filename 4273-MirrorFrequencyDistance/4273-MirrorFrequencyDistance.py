# Last updated: 5/16/2026, 4:53:52 PM
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        t=0
        f=set()
        def mirror(x:chr)->chr:
            if x.isdigit():
                return str(9-int(x))
            else:
                return chr(219-ord(x))
        for i in s:
            if i not in f:
                
                m=mirror(i)
                t+=abs(s.count(i)-s.count(m))
                f.add(i)
                f.add(m)
        return t
            
