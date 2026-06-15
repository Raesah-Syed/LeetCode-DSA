# Last updated: 6/14/2026, 11:42:54 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        file=path.split('/')
        s=[]

        for f in file:
            if f=='' or f=='.':
                continue
            elif f=='..':
                if s:
                    s.pop()
            else:
                s.append(f)
        
        return("/"+"/".join(s))

