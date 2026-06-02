# Last updated: 6/1/2026, 11:14:26 PM
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        s=set()
        while(i+k<=len(blocks)):
            s.add(blocks[i:i+k].count('W'))
            
            i=i+1
        
        return(min(s))