# Last updated: 5/20/2026, 10:30:59 PM
# Opposite direction pointers to traverse from last and first then swap them until reached middle
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        i=0
7        #s.append('')
8        x=len(s)-1
9        while i<=x:
10            temp=s[x]
11            s[x]=s[i]
12            s[i]=temp
13            i+=1
14            x-=1
15