# Last updated: 6/16/2026, 11:21:45 PM
# If it is a perfect square, mid*mid will return True, otherwise after the entire loop runs we return False
1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        
4        left,right=2,num//2
5
6        if num<2:
7            return True
8
9        while left<=right:
10
11            mid=(left+right)//2
12
13            if mid*mid==num:
14                return True
15            
16            elif mid*mid<num:
17                left=mid+1
18            
19            else:
20                right=mid-1
21        
22        return False