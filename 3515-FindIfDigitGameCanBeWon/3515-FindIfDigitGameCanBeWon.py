# Last updated: 5/11/2026, 12:16:35 PM
class Solution(object):
    def canAliceWin(self, nums):
        ss,ds=0,0
    
        for n in nums:
            if n<10:
                ss+=n
            else:
                ds+=n
        return ds!=ss
           