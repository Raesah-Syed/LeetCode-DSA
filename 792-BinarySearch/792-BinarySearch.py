# Last updated: 6/18/2026, 11:30:08 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left,right=0,len(nums)

        while (left<right):

            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid

        return -1