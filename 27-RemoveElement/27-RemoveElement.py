# Last updated: 5/23/2026, 7:57:12 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        j=len(nums)-1
        
        while i<=len(nums)-1:
            if nums[i]==val:
                nums[i]=nums[j]
                
                nums[j]='a'
                j=j-1
                
            else:
                i=i+1
        return sum(str(x).isdigit() for x in nums)