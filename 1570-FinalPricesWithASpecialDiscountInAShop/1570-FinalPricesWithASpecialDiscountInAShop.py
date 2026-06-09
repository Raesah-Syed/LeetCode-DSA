# Last updated: 6/9/2026, 12:11:04 AM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        r=prices[:]

        for i in range(len(prices)):

            while s and prices[s[-1]]>=prices[i]:
                ui=s.pop()
                r[ui]-=prices[i]
            
            s.append(i)

        return r

       
           