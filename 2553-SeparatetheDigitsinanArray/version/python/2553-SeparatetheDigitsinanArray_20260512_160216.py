# Last updated: 5/12/2026, 4:02:16 PM
# Take the min and second min number and add it to the first element of array
1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        
4        first = nums[0]       
5        min1 = inf   
6        min2 = inf 
7
8        for n in nums[1:]:
9            if n < min1:
10                min2 = min1    
11                min1 = n       
12            elif n < min2:
13                min2 = n       
14                
15        return first + min1 + min2