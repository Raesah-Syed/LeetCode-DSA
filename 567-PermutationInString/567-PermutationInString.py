# Last updated: 6/7/2026, 6:43:24 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)

        if n1>n2:
            return False

        s=Counter(s1)
        window= Counter(s2[:n1])
        
        for i in range(n2-n1):

            if window==s:
                return True
            
            else:

                r=s2[i+n1]
                window[r]+=1

                l=s2[i]
                window[l]-=1

                if window[l]==0:
                    del window[l]
    

        if window==s:
            return True
        else:
            return False