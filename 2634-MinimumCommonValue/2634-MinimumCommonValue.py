# Last updated: 6/16/2026, 10:56:32 PM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[len(nums1)-1]<nums2[0]:
            return -1
        for n in nums1:

            left,right=0,len(nums2)-1

            while left<=right:
                mid=(left+right)//2

                if nums2[mid]==n:
                    return n
                
                elif nums2[mid]<n:
                    left=mid+1
                
                else:
                    right=mid-1
        return -1

