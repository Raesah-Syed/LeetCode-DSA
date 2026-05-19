# Last updated: 5/18/2026, 8:29:05 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        n=len(nums)
4        i=0
5        j=len(nums)-1
6        
7        while i<=len(nums)-1:
8            if nums[i]==val:
9                nums[i]=nums[j]
10                
11                nums[j]='a'
12                j=j-1
13                
14            else:
15                i=i+1
16        return sum(str(x).isdigit() for x in nums)