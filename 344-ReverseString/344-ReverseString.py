# Last updated: 5/23/2026, 5:53:21 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        #s.append('')
        x=len(s)-1
        while i<=x:
            temp=s[x]
            s[x]=s[i]
            s[i]=temp
            i+=1
            x-=1
