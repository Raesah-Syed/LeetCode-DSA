class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0
        y=1

        while y<=len(nums)-1:
            if nums[x]==0:
                if nums[y]!=0:
                    nums[x],nums[y]=nums[y],nums[x]
                    x+=1
                    y+=1
                elif nums[y]==0:
                    y+=1
            else:
                x+=1
                y+=1
