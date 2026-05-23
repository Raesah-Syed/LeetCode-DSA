# Last updated: 5/23/2026, 5:53:08 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       if len(nums)<=1:
            return nums

       mid=len(nums)//2
       left=self.sortArray(nums[:mid])
       right=self.sortArray(nums[mid:])
    
       res,l,r=[],0,0

       while l<len(left) and r<len(right):
           if left[l]<right[r]:
               res.append(left[l])
               l+=1
           else:
               res.append(right[r])
               r+=1
       return res+left[l:]+right[r:]