# Last updated: 5/18/2026, 8:16:34 PM
# Swap positions and set the val to a character. Count the digits only
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        i=0
4        j=len(nums)-1
5        
6        while i<=len(nums)-1:
7            if nums[i]==val:
8                nums[i]=nums[j]
9                nums[j]='a'
10                j=j-1
11                
12            else:
13                i=i+1
14        return sum(str(x).isdigit() for x in nums)