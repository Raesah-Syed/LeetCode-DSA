# Last updated: 6/10/2026, 11:41:57 PM
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s=[]

        for l in logs:

            if s and l=='../':
                s.pop()
            elif l=='./':
                continue
            else:
                if l!='../':
                    s.append(l)
        
        
        return len(s)