# Last updated: 5/17/2026, 10:51:25 PM
# use dictionary to track the letters in both strings
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        d={}
4        for i in s:
5            if i not in d:
6                d[i]=1
7            else:
8                d[i]+=1
9        for j in t:
10            if j not in d:
11                return False
12            else:
13                d[j]-=1
14        for x in d.values():
15            if x!=0:
16                return False
17        return True
18            
19        