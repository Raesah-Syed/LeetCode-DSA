# Last updated: 6/15/2026, 7:28:49 PM
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
16
17            if guess(mid)==0:
18                return mid
19            
20            elif guess(mid)==1:
21                left=mid+1
22            
23            elif guess(mid)==-1:
24                right=mid
25
26
27
28