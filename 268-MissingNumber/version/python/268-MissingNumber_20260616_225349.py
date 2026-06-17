# Last updated: 6/16/2026, 10:53:49 PM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        left=1
7        right=n
8
9        while left<=right:
10            mid=(left+right)//2
11
12            if isBadVersion(mid):
13                right=mid-1
14
15            else:
16                left=mid+1
17        return left
18