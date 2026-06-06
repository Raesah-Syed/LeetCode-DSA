# Last updated: 6/6/2026, 5:37:47 PM
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=len(cardPoints)
        w=cardPoints[:l-k]
        s=sum(w)
        m=s
        
        for i in range(l-k,l):
            
            s+=cardPoints[i]-cardPoints[i-(l-k)]
            m=min(m,s)
        
        return(sum(cardPoints)-m)

 