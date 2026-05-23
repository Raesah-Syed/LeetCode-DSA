# Last updated: 5/23/2026, 5:52:21 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,l1,l2=0,0,len(word1),len(word2)
        res=''

        while i<l1 and j<l2 :
            res+=word1[i]+word2[j]
            i=i+1
            j=j+1
        if i<l1:
            res+=word1[i:l1]
        if j<l2:
            res+=word2[j:l2]
        return(res)