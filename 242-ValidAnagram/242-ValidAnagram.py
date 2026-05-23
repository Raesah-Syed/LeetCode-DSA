# Last updated: 5/23/2026, 5:53:21 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in t:
            if j not in d:
                return False
            else:
                d[j]-=1
        for x in d.values():
            if x!=0:
                return False
        return True
            
        