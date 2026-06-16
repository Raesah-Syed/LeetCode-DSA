# Last updated: 6/15/2026, 7:33:28 PM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        
11        left,right=1,n
12
13        while(left<=right):
14            
15            mid=(left+right)//2
16            res=guess(mid)
17            
18            if res==0:
19                return mid
20            
21            elif res==1:
22                left=mid+1
23            
24            elif res==-1:
25                right=mid-1
26
27
28
29