# Last updated: 5/11/2026, 12:16:33 PM
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        x= maxWeight//w
        return min(x,n*n)