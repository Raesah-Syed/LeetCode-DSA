# Last updated: 5/12/2026, 5:47:49 PM
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            l=len(str(n))-1
            if n<10:
                ans.append(n)
            else:
                while l>=0:
                    ans.append(int(n/pow(10,l)))
                    n=n%pow(10,l)
                    l-=1
        return ans