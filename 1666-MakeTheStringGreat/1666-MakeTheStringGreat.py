# Last updated: 6/10/2026, 11:41:58 PM
class Solution:
    def makeGood(self, s: str) -> str:
        r=[]
        for i in s:
            if r and i.isupper() and r[-1]==i.lower() or (r and i.islower() and r[-1]==i.upper()):
                r.pop()
                continue
            else:
                r.append(i)
        return "".join(r)

