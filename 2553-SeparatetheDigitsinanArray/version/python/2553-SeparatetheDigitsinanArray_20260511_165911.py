# Last updated: 5/11/2026, 4:59:11 PM
# This solution uses math to separate each digit and adds it to a list.
1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        ans=[]
4        for n in nums:
5            l=len(str(n))-1
6            if n<10:
7                ans.append(n)
8            else:
9                while l>=0:
10                    ans.append(int(n/pow(10,l)))
11                    n=n%pow(10,l)
12                    l-=1
13        return ans