# Last updated: 6/6/2026, 2:18:26 PM
1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        l=len(cardPoints)
4        w=cardPoints[:l-k]
5        s=sum(w)
6        m=s
7        
8        for i in range(l-k,l):
9            
10            s+=cardPoints[i]-cardPoints[i-(l-k)]
11            m=min(m,s)
12        
13        return(sum(cardPoints)-m)
14
15 