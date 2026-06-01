# Last updated: 5/31/2026, 11:35:56 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cs=0
        cn=0
        longest=0
        ns=set(nums)
        
        for n in ns:

            if (n-1) not in ns:
                cn=n
                cs=1

            while cn+1 in ns:
                cs+=1
                n=n+1
                cn=n
            
            longest=max(longest,cs)
        
    
        return(longest)
        
             
