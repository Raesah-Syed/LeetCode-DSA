# Last updated: 6/4/2026, 11:26:46 PM
# Use counters on both strings and get the first substring of length s1 and slide through s2
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1=len(s1)
4        n2=len(s2)
5
6        if n1>n2:
7            return False
8
9        s=Counter(s1)
10        window= Counter(s2[:n1])
11        
12        for i in range(n2-n1):
13
14            if window==s:
15                return True
16            
17            else:
18
19                r=s2[i+n1]
20                window[r]+=1
21
22                l=s2[i]
23                window[l]-=1
24
25                if window[l]==0:
26                    del window[l]
27    
28
29        if window==s:
30            return True
31        else:
32            return False